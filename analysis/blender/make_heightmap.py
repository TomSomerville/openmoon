"""Height map of the primary base and 10 km around it (20 x 20 km, 5 m/px) for Blender.
Heights: NASA GSFC LOLA 5 m/px de Gerlache rim DEM (PGDA product 78, Site11) where it exists, else LOLA 10 m/px
(LDEM_83S_10MPP_ADJ, PGDA product 90) resampled to 5 m, offset-matched and feathered across the seam.
Outputs to OUTDIR: heightmap_5m.tif (float32 metres, polar stereographic), heightmap_5m_16bit.png, heightmap_5m_curved.tif
(lunar curvature applied), source_mask.png, mesh_20m.ply (UV-mapped), info.json.  Usage: make_heightmap.py OUTDIR"""
import sys, os, json, math, numpy as np, rasterio
from rasterio.windows import from_bounds
from rasterio.transform import from_origin
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m
from scipy import ndimage
from PIL import Image
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
os.environ['CURL_CA_BUNDLE'] = os.environ.get('CURL_CA_BUNDLE', '/root/.ccr/ca-bundle.crt')
R = 1737400.; C = lonlat2m(-88.4262, -63.30); HALF = 10000.; RES = 5.
B = (C[0] - HALF, C[1] - HALF, C[0] + HALF, C[1] + HALF); N = int(2 * HALF / RES)
d10 = np.nan_to_num(read('LDEM_83S_10MPP_ADJ', B, 10)).astype('float64')
h = np.array(Image.fromarray(d10.astype('float32'), mode='F').resize((N, N), Image.BICUBIC)).astype('float64')
S11 = os.environ.get('SITE11_TIF', '/vsicurl/https://pgda.gsfc.nasa.gov/data/LOLA_5mpp/Site11/Site11_final_adj_5mpp_surf.tif')   # set SITE11_TIF to a local copy if remote reads fail
with rasterio.open(S11) as d:
    w = from_bounds(*B, transform=d.transform)
    a = d.read(1, window=w, out_shape=(N, N), boundless=True, fill_value=np.nan, masked=False).astype('float64')
    nod = d.nodata
if nod is not None: a[a == nod] = np.nan
a[~np.isfinite(a) | (np.abs(a) > 20000)] = np.nan
has = np.isfinite(a)
off = float(np.nanmedian(a[has] - h[has])) if has.any() else 0.0
a = a - off
# feather: weight 1 inside the 5 m area, falling to 0 over 500 m at its edge
wgt = np.clip(ndimage.distance_transform_edt(has) * RES / 500., 0, 1)
hm = np.where(has, wgt * a + (1 - wgt) * h, h)
# outputs
tr = from_origin(B[0], B[3], RES, RES)
crs = 'PROJCS["Moon south polar stereographic",GEOGCS["Moon 2000",DATUM["D_Moon_2000",SPHEROID["Moon_2000_IAU_IAG",1737400.0,0.0]],PRIMEM["Greenwich",0],UNIT["Decimal_Degree",0.0174532925199433]],PROJECTION["Polar_Stereographic"],PARAMETER["latitude_of_origin",-90],PARAMETER["central_meridian",0],PARAMETER["scale_factor",1],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["Meter",1]]'
def save_tif(name, arr):
    with rasterio.open(os.path.join(OUT, name), 'w', driver='GTiff', width=N, height=N, count=1, dtype='float32', crs=crs, transform=tr,
                       compress='deflate', predictor=3, tiled=True) as o: o.write(arr.astype('float32'), 1)
save_tif('heightmap_5m.tif', hm)
xs = (np.arange(N) + 0.5) * RES - HALF; XX, YY = np.meshgrid(xs, xs)
curved = hm - (XX ** 2 + YY ** 2) / (2 * R)
save_tif('heightmap_5m_curved.tif', curved)
lo, hi = float(hm.min()), float(hm.max())
Image.fromarray(np.round((hm - lo) / (hi - lo) * 65535).astype('uint16')).save(os.path.join(OUT, 'heightmap_5m_16bit.png'))
Image.fromarray((np.where(has, 255, 90)).astype('uint8')).resize((1000, 1000)).save(os.path.join(OUT, 'source_mask.png'))
# UV-mapped mesh at 20 m (1001 x 1001 vertices), metres, X east-ish / Y north-ish in the map grid, Z = height above the lowest point
step = 4; sub = hm[::step, ::step]; n = sub.shape[0]
vx = np.tile(np.arange(n) * RES * step - HALF, n); vy = np.repeat(HALF - np.arange(n) * RES * step, n); vz = (sub - lo).ravel()
uu = np.tile(np.arange(n) / (n - 1), n); vv = np.repeat(1 - np.arange(n) / (n - 1), n)
verts = np.zeros(n * n, dtype=[('x', '<f4'), ('y', '<f4'), ('z', '<f4'), ('s', '<f4'), ('t', '<f4')])
verts['x'], verts['y'], verts['z'], verts['s'], verts['t'] = vx, vy, vz, uu, vv
ii = np.arange(n - 1); I, J = np.meshgrid(ii, ii, indexing='ij'); a0 = (I * n + J).ravel()
faces = np.zeros(2 * len(a0), dtype=[('n', 'u1'), ('a', '<i4'), ('b', '<i4'), ('c', '<i4')]); faces['n'] = 3
faces['a'][0::2], faces['b'][0::2], faces['c'][0::2] = a0, a0 + n, a0 + 1
faces['a'][1::2], faces['b'][1::2], faces['c'][1::2] = a0 + 1, a0 + n, a0 + n + 1
with open(os.path.join(OUT, 'mesh_20m.ply'), 'wb') as f:
    f.write(('ply\nformat binary_little_endian 1.0\ncomment Open Moon primary base terrain, NASA LOLA, metres\nelement vertex %d\nproperty float x\nproperty float y\nproperty float z\nproperty float s\nproperty float t\nelement face %d\nproperty list uchar int vertex_indices\nend_header\n' % (n * n, len(faces))).encode())
    f.write(verts.tobytes()); f.write(faces.tobytes())
bz = float(hm[N // 2, N // 2])
info = {'centre_lat_lon': [-88.4262, -63.30], 'size_m': 2 * HALF, 'pixel_m': RES, 'pixels': N, 'bounds_polar_stereographic_m': [float(v) for v in B],
        'height_min_m': round(lo, 2), 'height_max_m': round(hi, 2), 'height_range_m': round(hi - lo, 2), 'base_height_m': round(bz, 2),
        'base_height_above_min_m': round(bz - lo, 2), 'share_from_5m_dem_pct': round(float(has.mean()) * 100, 1), 'site11_offset_vs_10m_m': round(off, 2),
        'curvature_drop_at_edge_mid_m': round(HALF ** 2 / (2 * R), 1), 'curvature_drop_at_corner_m': round(2 * HALF ** 2 / (2 * R), 1),
        'mesh': {'file': 'mesh_20m.ply', 'grid': n, 'spacing_m': RES * step}}
json.dump(info, open(os.path.join(OUT, 'info.json'), 'w'), indent=1); print(json.dumps(info, indent=1))
