"""Render 4 x 4 km crops of LROC NAC south-pole sub-solar-longitude mosaics around the primary base.
Usage: render_bins.py OUTDIR BIN [BIN ...]"""
import sys, time, math, numpy as np, rasterio
from rasterio.windows import from_bounds
from PIL import Image, ImageDraw, ImageFont
U = ('/vsicurl/https://pds.mcp.nasa.gov/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/'
     'LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/NAC_POLE_SOUTH_{p}/NAC_POLE_SOUTH_{p}_P878S2925.{e}')
R = 1737400.; FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
xy = lambda la, lo: (2 * R * math.tan(math.radians(90 + la) / 2) * math.sin(math.radians(lo)), 2 * R * math.tan(math.radians(90 + la) / 2) * math.cos(math.radians(lo)))
BASE = xy(-88.4365, -62.46); B3 = xy(-88.3693, -62.11)
def rd(p, half, px):
    cx, cy = BASE
    for e in ('PYR.TIF', 'TIF'):
        for k in range(4):
            try:
                with rasterio.open(U.format(p=p, e=e)) as d:
                    w = from_bounds(cx - half, cy - half, cx + half, cy + half, d.transform)
                    return d.read(1, window=w, out_shape=(px, px), resampling=rasterio.enums.Resampling.average).astype(float)
            except Exception as ex:
                if '404' in str(ex): break
                time.sleep(10 * (k + 1))
    return None
for b in sys.argv[2:]:
    half, px = 2000, 1000
    a = rd('CM_' + b, half, px)
    if a is None: print(b, 'failed', flush=True); continue
    v = a[a > 0]; lo, hi = np.percentile(v, 1), np.percentile(v, 99.5)
    g = (np.clip((a - lo) / (hi - lo), 0, 1) ** 0.8 * 255).astype('uint8')
    im = Image.fromarray(g).convert('RGB'); dr = ImageDraw.Draw(im); s = px / (2 * half)
    c = int(px / 2); print(b, 'base pixel value %.0f (median %.0f)' % (a[c-5:c+5, c-5:c+5].mean(), np.median(v)), flush=True)
    for (x, y), lab, col in ((BASE, 'Base', (255, 60, 200)), (B3, 'B3', (255, 160, 0))):
        X = (x - BASE[0] + half) * s; Y = (BASE[1] + half - y) * s
        if 0 <= X < px and 0 <= Y < px:
            dr.ellipse((X - 8, Y - 8, X + 8, Y + 8), outline=col, width=3); dr.text((X + 11, Y - 11), lab, font=ImageFont.truetype(FB, 18), fill=col, stroke_width=3, stroke_fill='black')
    im.save('%s/bin_%s.jpg' % (sys.argv[1], b), quality=88); time.sleep(5)
