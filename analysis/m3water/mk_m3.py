"""M3 surface water within 10 km of the primary base, over LOLA slope, with base locations.
Data: Li et al. 2023 M3 water maps (USGS PDS4 archive, doi:10.17189/gmce-w279), six maps (one per magnetotail
period), saved by read_m3.py in data/m3water/. Open Moon processing, not a USGS or NASA product:
 - values < -1e30 are fill; the value exactly 20 ppm is undocumented and very common, so it is treated as no data;
 - each pixel = mean of the maps that have a value there;
 - resampled (nearest) from simple cylindrical to the polar stereographic grid of the LOLA slope map.
Usage: python3 mk_m3.py OUT.jpg"""
import sys, os, glob, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../slope'))
from render import read, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]; DATA = os.path.join(HERE, '..', '..', 'data', 'm3water')
R = 1737400.
BASE = (-88.4365, -62.46)
SITES = [('Base', -88.4365, -62.46), ('B3', -88.3693, -62.11), ('B1 + M1', -88.4657, -67.872), ('B2 + M2', -88.3937, -68.686)]
bx, by = lonlat2m(*BASE)
HW = 12000; RES = 20
B = (bx - HW, by - HW, bx + HW, by + HW)
s = read('LDSM_83S_10MPP_ADJ', B, RES); h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, RES)); H, W = s.shape
xs = B[0] + RES * (np.arange(W) + .5); ys = B[3] - RES * (np.arange(H) + .5)
X, Y = np.meshgrid(xs, ys); rho = np.hypot(X, Y)
LON = np.degrees(np.arctan2(X, Y)); LAT = np.degrees(2 * np.arctan(rho / (2 * R))) - 90
files = sorted(glob.glob(os.path.join(DATA, '*.npz'))); maps = []
for f in files:
    z = np.load(f); a = z['a'].astype('float64'); t = z['t']
    a[(a < -1e30) | (a == 20.0)] = np.nan
    col = np.floor((LON - t[2]) / t[0]).astype(int); row = np.floor((LAT - t[5]) / t[4]).astype(int)
    ok = (row >= 0) & (row < a.shape[0]) & (col >= 0) & (col < a.shape[1])
    g = np.full(LAT.shape, np.nan); g[ok] = a[row[ok], col[ok]]; maps.append(g)
M = np.stack(maps); n = np.isfinite(M).sum(0)
w = np.where(n > 0, np.nansum(M, 0) / np.maximum(n, 1), np.nan)
inside = np.hypot(X - bx, Y - by) <= 10000
v = w[inside & np.isfinite(w)]
q = lambda x: dict(n=int(x.size), mean=round(float(x.mean())), median=round(float(np.median(x))),
                   p10=round(float(np.percentile(x, 10))), p90=round(float(np.percentile(x, 90)))) if x.size else dict(n=0)
st = dict(note='M3 water (ppm) within 10 km of 88.4365S 62.46W; Open Moon processing', cells=int(inside.sum()),
          coverage=round(v.size / inside.sum(), 3), all=q(v),
          per_map={os.path.basename(f)[:-4]: q(m[inside & np.isfinite(m)]) for f, m in zip(files, maps)})
for lo, hi in ((0, 8), (8, 15), (15, 90)):
    st[f'slope_{lo}_{hi}'] = q(w[inside & np.isfinite(w) & (s > lo) & (s <= hi)])
print(json.dumps(st, indent=1)); json.dump(st, open(os.path.join(DATA, 'stats_10km.json'), 'w'), indent=1)
# ---- render (display only: water averaged over ~300 m, about one M3 pixel; slope outlines from 100 m means)
def boxmean(a, r):
    f = np.isfinite(a); v = np.where(f, a, 0.)
    cs = lambda z: np.pad(z, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    S, N = cs(v), cs(f.astype(float)); H_, W_ = a.shape
    y0 = np.clip(np.arange(H_) - r, 0, H_); y1 = np.clip(np.arange(H_) + r + 1, 0, H_)
    x0 = np.clip(np.arange(W_) - r, 0, W_); x1 = np.clip(np.arange(W_) + r + 1, 0, W_)
    box = lambda C: C[y1][:, x1] - C[y0][:, x1] - C[y1][:, x0] + C[y0][:, x0]
    n_ = box(N); return np.where(n_ > 0.3 * (2 * r + 1) ** 2, box(S) / np.maximum(n_, 1), np.nan)
wd = boxmean(w, 7)
sd = boxmean(np.nan_to_num(s), 2)
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
rgb = np.stack([hv * 200] * 3, -1)
STOPS = [(0, (40, 40, 120)), (100, (40, 120, 220)), (250, (40, 200, 200)), (500, (240, 230, 60)), (1000, (250, 120, 30)), (2000, (230, 30, 30))]
def cm(x):
    out = np.zeros(np.shape(x) + (3,)); xp = [p for p, _ in STOPS]
    for c in range(3): out[..., c] = np.interp(x, xp, [col[c] for _, col in STOPS])
    return out
fin = np.isfinite(wd)
rgb = np.where(fin[..., None], rgb * 0.3 + cm(np.nan_to_num(wd)) * 0.7, rgb)
def edges(m):
    e = m & ~(np.roll(m, 1, 0) & np.roll(m, -1, 0) & np.roll(m, 1, 1) & np.roll(m, -1, 1)); return e | np.roll(e, 1, 0) | np.roll(e, 1, 1)
a = rgb.clip(0, 255).astype('uint8')
a[edges(np.nan_to_num(sd) > 8)] = (255, 255, 255)
a[edges(np.nan_to_num(sd) > 15)] = (0, 0, 0)
im = Image.fromarray(a); dr = ImageDraw.Draw(im); k = W / 960
Fs = ImageFont.truetype(FB, int(15 * k))
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
cx, cy = m2p(bx, by); r = 10000 / RES
dr.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 0, 255), width=int(3 * k))
for name, la, lo in SITES:
    x, y = m2p(*lonlat2m(la, lo)); rr = (10 if name == 'Base' else 7) * k
    dr.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(255, 0, 255) if name == 'Base' else (255, 160, 0), outline='black', width=int(2 * k))
    dr.text((x + 12 * k, y), name, font=Fs, fill='white', anchor='lm', stroke_width=int(3 * k), stroke_fill='black')
pad = 12 * k; lw = 330 * k; lh = 205 * k
dr.rectangle((pad, pad, pad + lw, pad + lh), fill=(0, 0, 0))
dr.text((pad + 10 * k, pad + 8 * k), 'M3 surface water (ppm), top ~1 mm', font=Fs, fill='white')
bw = lw - 20 * k
for i in range(int(bw)):
    c = tuple(int(x) for x in cm(np.array([2000 * i / bw]))[0])
    dr.line((pad + 10 * k + i, pad + 32 * k, pad + 10 * k + i, pad + 48 * k), fill=c)
for val in (0, 500, 1000, 1500, 2000):
    dr.text((pad + 10 * k + bw * val / 2000, pad + 52 * k), str(val), font=Fs, fill='white', anchor='mt')
yy = pad + 80 * k
for txt, col in (('White line: slope over 8°', (255, 255, 255)), ('Black line: slope over 15°', (160, 160, 160)),
                 ('Grey shading only: no M3 value', (150, 150, 150)), ('Magenta circle: 10 km from the base', (255, 0, 255)),
                 ('Orange: solar towers (DD-024)', (255, 160, 0))):
    dr.text((pad + 10 * k, yy), txt, font=Fs, fill=col); yy += 24 * k
dr.text((W - pad, H - pad), 'Water: Li et al. 2023 M3 maps (USGS PDS4). Slope: NASA GSFC LOLA. Open Moon processing.',
        font=Fs, fill='white', anchor='rb', stroke_width=int(3 * k), stroke_fill='black')
im.save(OUT, quality=88); print('wrote', OUT, im.size)
