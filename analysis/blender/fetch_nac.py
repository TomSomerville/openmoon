"""Fetch a 20 x 20 km window of a NASA LROC NAC south-pole mosaic (1 m/px, PDS) around the primary base, averaged to
RES m/px, from the two tiles that cover it. Strips are cached in OUTDIR so the run can resume.
Usage: fetch_nac.py PRODUCT OUTDIR [RES=2]   e.g. fetch_nac.py CM_MAX nac_max 2"""
import os, sys, time, math, numpy as np, rasterio
from rasterio.windows import from_bounds
os.environ.update({'GDAL_HTTP_MAX_RETRY': '12', 'GDAL_HTTP_RETRY_DELAY': '6', 'GDAL_DISABLE_READDIR_ON_OPEN': 'EMPTY_DIR',
                   'CURL_CA_BUNDLE': os.environ.get('CURL_CA_BUNDLE', '/root/.ccr/ca-bundle.crt'), 'VSI_CACHE': 'TRUE', 'VSI_CACHE_SIZE': '200000000'})
PROD, OUT = sys.argv[1], sys.argv[2]; RES = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
U = ('/vsicurl/https://pds.mcp.nasa.gov/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/'
     'LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/NAC_POLE_SOUTH_{p}/NAC_POLE_SOUTH_{p}_{t}.PYR.TIF')
TILES = ['P878S2925', 'P892S3150']
R = 1737400.; la, lo = -88.4262, -63.30
rho = 2 * R * math.tan(math.radians(90 + la) / 2); CX, CY = rho * math.sin(math.radians(lo)), rho * math.cos(math.radians(lo))
HALF = 10000.; B = (CX - HALF, CY - HALF, CX + HALF, CY + HALF)
N = int(2 * HALF / RES); STRIP = 1000.   # metres per strip
os.makedirs(OUT, exist_ok=True)
for k in range(int(2 * HALF / STRIP)):
    f = os.path.join(OUT, 'strip_%02d.npy' % k)
    if os.path.exists(f): continue
    top = B[3] - k * STRIP; bot = top - STRIP; rows = int(STRIP / RES)
    acc = np.zeros((rows, N), np.float32); got = np.zeros((rows, N), bool)
    for t in TILES:
        for attempt in range(8):
            try:
                with rasterio.open(U.format(p=PROD, t=t)) as d:
                    w = from_bounds(B[0], bot, B[2], top, d.transform)
                    a = d.read(1, window=w, out_shape=(rows, N), boundless=True, fill_value=0,
                               resampling=rasterio.enums.Resampling.average).astype(np.float32)
                m = a > 0; acc[m] = a[m]; got |= m; break
            except Exception as e:
                print('strip', k, t, 'retry', attempt, str(e)[:80], flush=True); time.sleep(20 * (attempt + 1))
        else:
            print('strip', k, t, 'FAILED', flush=True)
    np.save(f, acc.astype(np.uint8)); print('strip', k, 'done, covered %.0f%%' % (got.mean() * 100), flush=True)
    time.sleep(3)
full = np.vstack([np.load(os.path.join(OUT, 'strip_%02d.npy' % k)) for k in range(int(2 * HALF / STRIP))])
np.save(os.path.join(OUT, 'full.npy'), full); np.save(os.path.join(OUT, 'bounds.npy'), np.array(B))
print('DONE', full.shape, 'covered %.1f%%' % ((full > 0).mean() * 100), flush=True)
