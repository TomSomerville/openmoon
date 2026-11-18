"""Crops of NASA LROC NAC south polar mosaics (1 m/px, PDS) around the Open Moon primary base.
Products: NAC_POLE_SOUTH_CM_MAX (maximum-pixel mosaic, least shadow) and CM_AVG (average). Read by window from the tiled PYR.TIF over HTTP.
Usage: python3 mk_nac_lighting.py OUTDIR"""
import sys, math, numpy as np, rasterio
from rasterio.windows import from_bounds
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]
U = ('/vsicurl/https://pds.mcp.nasa.gov/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/'
     'LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/NAC_POLE_SOUTH_{p}/NAC_POLE_SOUTH_{p}_P878S2925.{ext}')
FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; F = lambda s: ImageFont.truetype(FB, s)
R = 1737400.
def xy(lat, lon):
    rho = 2 * R * math.tan(math.radians(90 + lat) / 2); L = math.radians(lon); return rho * math.sin(L), rho * math.cos(L)
BASE = xy(-88.445, -63.44); B3 = xy(-88.4411, -62.44)
def _read(prod, half, px):
    cx, cy = BASE
    for k in range(5):
        try:
            with rasterio.open(U.format(p=prod, ext='PYR.TIF')) as d:
                w = from_bounds(cx - half, cy - half, cx + half, cy + half, d.transform)
                return d.read(1, window=w, out_shape=(px, px), resampling=rasterio.enums.Resampling.average).astype(float)
        except rasterio.errors.RasterioIOError:
            if k == 4: raise
def crop(prod, half, px):
    cx, cy = BASE; a = _read(prod, half, px)
    v = a[a > 0]; lo, hi = np.percentile(v, 1), np.percentile(v, 99.5)
    g = np.clip((a - lo) / (hi - lo), 0, 1) ** 0.8 * 255
    im = Image.fromarray(g.astype('uint8')).convert('RGB'); dr = ImageDraw.Draw(im); s = px / (2 * half)
    for (x, y), lab, col in ((BASE, 'Base', (255, 60, 200)), (B3, 'B3', (255, 160, 0))):
        X = (x - cx + half) * s; Y = (cy + half - y) * s
        if 0 <= X < px and 0 <= Y < px:
            dr.ellipse((X - 7, Y - 7, X + 7, Y + 7), outline=col, width=3)
            dr.text((X + 10, Y - 10), lab, font=F(18), fill=col, stroke_width=3, stroke_fill='black')
    bar = 500 if half > 1000 else 100; dr.rectangle((14, px - 26, 14 + bar * s, px - 20), fill='white')
    dr.text((14, px - 50), '%d m' % bar, font=F(16), fill='white', stroke_width=3, stroke_fill='black')
    return im
def cap(im, t):
    dr = ImageDraw.Draw(im); dr.rectangle((0, 0, im.width, 30), fill='black'); dr.text((8, 6), t, font=F(17), fill='white'); return im
for prod, half, px, name, t in (('CM_MAX', 2000, 1000, 'primary-base-nac-max-4km', 'LROC NAC maximum-pixel mosaic (least shadow), 4 × 4 km, 1 m/px'),
                                ('CM_MAX', 600, 1200, 'primary-base-nac-max-1km', 'LROC NAC maximum-pixel mosaic, 1.2 × 1.2 km, full 1 m/px'),
                                ('CM_AVG', 2000, 1000, 'primary-base-nac-avg-4km', 'LROC NAC average mosaic, 4 × 4 km (not used on the site)')):
    cap(crop(prod, half, px), t).save('%s/%s.jpg' % (OUT, name), quality=88); print(name, flush=True)
