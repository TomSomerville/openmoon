"""Sunlight maps for the focus area: NASA GSFC average solar illumination (18.6-yr mean, ground level, 60 m/px),
and VSAT candidate ground (well-lit and slope <= 15 deg), with NASA's best-lit regions of interest (PGDA product 78)."""
import sys, os, math, glob, numpy as np, shapefile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../hydrogen'))
from render import read, px2m, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
import rasterio
from rasterio.windows import from_bounds
ILL, ROIDIR, OUTDIR = sys.argv[1], sys.argv[2], sys.argv[3]
font = lambda sz: ImageFont.truetype(FB, int(sz))
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); RES = 60
with rasterio.open(ILL) as r:
    w = from_bounds(*B, transform=r.transform).round_offsets().round_lengths()
    il = r.read(1, window=w).astype(float); il[il == -32768] = np.nan; il *= 4e-5 * 100   # percent of time sunlit
H, W = il.shape
sl = np.array(Image.fromarray(read('LDSM_83S_10MPP_ADJ', B, 40).astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
hs = np.array(Image.fromarray(np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, 40)).astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
hv = np.clip((hs - np.percentile(hs, 1)) / (np.percentile(hs, 99) - np.percentile(hs, 1)), 0, 1)
base = np.stack([hv * 255] * 3, -1)
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
UP = 2  # draw at 2x for crisp labels

def decorate(im, title, legend_rows, legend_title, ramp=None, numbers=()):
    im = im.resize((W * UP, H * UP), Image.NEAREST); dr = ImageDraw.Draw(im); k = W * UP / 1400
    F, Fs = font(24 * k), font(16 * k)
    q = lambda x, y: (m2p(x, y)[0] * UP, m2p(x, y)[1] * UP)
    for lat_, lon_, diam, lab, side in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton', 'r'), (-88.5, -87.1, 32.4, 'de Gerlache', 'l'), (-89.51, -84.61, 13.0, 'Spudis', 't')]:
        x, y = q(*lonlat2m(lat_, lon_)); rr = diam * 500 / RES * UP
        dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 230, 255), width=max(2, int(3 * k)))
        if side == 't': dr.text((x, y - rr - 6 * k), lab, font=F, fill=(0, 230, 255), anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
        else: dr.text((x + (rr + 8 * k if side == 'r' else -rr - 8 * k), y), lab, font=F, fill=(0, 230, 255), anchor='lm' if side == 'r' else 'rm', stroke_width=3, stroke_fill=(0, 0, 0))
    x, y = q(*lonlat2m(-89.427, -113.82)); dr.text((x, y), 'Shackleton–de Gerlache Ridge', font=font(15 * k), fill='white', anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
    # NASA best-lit regions of interest
    names = {'Site01': 'NASA Site 1: Connecting ridge', 'Site04': 'NASA Site 4: Shackleton rim', 'Site07': 'NASA Site 7: Peak near Shackleton', 'Site11': 'NASA Site 11: de Gerlache rim'}
    offs = {'Site01': (0, 34), 'Site04': (60, -40), 'Site07': (0, -34), 'Site11': (0, -34)}
    for f in sorted(glob.glob(os.path.join(ROIDIR, '*_ROIs.shp'))):
        key = os.path.basename(f).split('_')[0]; sf = shapefile.Reader(f); cs = []
        for s in sf.shapes():
            pts = [q(px_, py_) for px_, py_ in s.points]
            if len(pts) > 2: dr.polygon(pts, outline=(255, 0, 255))
            bb = s.bbox; cs.append(q((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2))
        cx = sum(c[0] for c in cs) / len(cs); cy = sum(c[1] for c in cs) / len(cs); r = 11 * k
        dr.ellipse((cx - r, cy - r, cx + r, cy + r), outline=(255, 0, 255), width=int(4 * k))
        ox, oy = offs.get(key, (0, -34))
        if not numbers: dr.text((cx + ox * k, cy + oy * k), names.get(key, key), font=Fs, fill=(255, 120, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
    for n, (X, Y) in enumerate(numbers, 1):
        x, y = q(X, Y); dr.text((x + 10 * k, y - 10 * k), str(n), font=font(20 * k), fill='white', anchor='lb', stroke_width=4, stroke_fill=(200, 30, 0))
    hgt = int((len(legend_rows) * 30 + 50 + (40 if ramp else 0)) * k)
    if numbers: lx, ly = W * UP - int(720 * k), int(50 * k)
    else: lx, ly = int(20 * k), H * UP - hgt
    dr.rectangle((lx - 10 * k, ly - 10 * k, lx + 700 * k, ly + hgt - 18 * k), fill=(0, 0, 0))
    dr.text((lx, ly + 14 * k), legend_title, font=Fs, fill='white', anchor='ld'); yy = ly + 26 * k
    if ramp:
        lw = int(450 * k); g = ramp(np.linspace(0, 90, lw))
        for i in range(lw): dr.line([(lx + i, yy), (lx + i, yy + 18 * k)], fill=tuple(int(c) for c in g[i]))
        for v in (0, 30, 50, 70, 90): xx = lx + lw * v / 90; dr.text((xx, yy + 22 * k), f'{v}%', font=Fs, fill='white', anchor='mt')
        yy += 50 * k
    for c, t in legend_rows:
        if c is None: dr.ellipse((lx + 10 * k, yy, lx + 28 * k, yy + 18 * k), outline=(255, 0, 255), width=int(3 * k))
        else: dr.rectangle((lx, yy, lx + 40 * k, yy + 18 * k), fill=c)
        dr.text((lx + 50 * k, yy + 9 * k), t, font=Fs, fill='white', anchor='lm'); yy += 30 * k
    L = 10000 / RES * UP; sx = W * UP - L - 30 * k; sy = H * UP - 30 * k
    dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H * UP - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
    dr.rectangle((0, 0, W * UP, int(30 * k)), fill=(0, 0, 0)); dr.text((10 * k, 6 * k), title, font=Fs, fill='white')
    im.thumbnail((2400, 2400), Image.LANCZOS); return im

# 1) raw illumination (inferno-like ramp)
stops = np.array([0, 20, 40, 60, 90.]); cols = np.array([[0, 0, 4], [87, 16, 110], [188, 55, 84], [249, 142, 9], [252, 255, 164]], float)
ramp = lambda v: np.stack([np.interp(np.clip(v, 0, 90), stops, cols[:, c]) for c in range(3)], -1)
raw = Image.fromarray(ramp(np.nan_to_num(il)).astype('uint8'))
decorate(raw, 'Focus area: average solar illumination at ground level, 18.6-year mean, 60 m/px. NASA GSFC PGDA (Mazarico et al. 2011, AVGVISIB_85S_060M).',
         [(None, 'NASA best-lit regions of interest (PGDA product 78)')], 'Time in sunlight (% of 18.6 years, at the surface)', ramp).save(os.path.join(OUTDIR, 'focus-sunlight-raw.jpg'), quality=85, optimize=True)
# 2) VSAT candidate ground: slope <= 15 deg and sunlit >= 40 / 50 / 60 %
ok = sl <= 15
tiers = [(80, (255, 60, 0))]
rgb = base.copy()
for t, c in reversed(tiers): rgb = np.where(((il >= t) & ok)[..., None], base * 0.25 + np.array(c) * 0.75, rgb)
# grow small patches so they stay visible after downsampling
im = Image.fromarray(rgb.clip(0, 255).astype('uint8'))
# markers: small high-sun patches are invisible at page scale, so mark each 1 km cell holding them
dr0 = ImageDraw.Draw(im); BIN = int(1000 / RES); spots = []
for j in range(0, H, BIN):
    for i in range(0, W, BIN):
        blk = np.where(ok[j:j + BIN, i:i + BIN], il[j:j + BIN, i:i + BIN], np.nan)
        if np.all(np.isnan(blk)): continue
        mx = np.nanmax(blk)
        if mx >= 80:
            jj, ii = np.unravel_index(np.nanargmax(blk), blk.shape); y, x = j + jj, i + ii
            c = (255, 60, 0); r = 7
            dr0.ellipse((x - r, y - r, x + r, y + r), fill=c, outline=(0, 0, 0))
            X = B[0] + (x + 0.5) * RES; Y = B[3] - (y + 0.5) * RES; rho = math.hypot(X, Y)
            spots.append((mx, -(90 - math.degrees(2 * math.atan(rho / (2 * 1737400.)))), math.degrees(math.atan2(X, Y)), X, Y))
spots.sort(reverse=True)
sites = []
for sp in spots:
    if all(math.hypot(sp[3] - a, sp[4] - b) >= 3000 for a, b in sites): sites.append((sp[3], sp[4]))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vsat_spots.csv'), 'w') as fh:
    fh.write('sunlit_pct,lat,lon_east,x_m,y_m\n')
    for sp in spots: fh.write('%.1f,%.4f,%.3f,%.0f,%.0f\n' % sp)
rows = [((255, 60, 0), 'Sunlit ≥80% of the time, slope ≤15° (dot marks each 1 km cell)'), (None, 'NASA best-lit regions of interest: Sites 1, 4, 7, 11 (PGDA product 78)')]
decorate(im, 'Focus area: VSAT sites, sunlit ≥80% at ground level and slope ≤15°. Sunlight: NASA GSFC PGDA; slope: NASA LOLA LDSM.',
         rows, 'VSAT sites (ground-level sunlight; a 10 m mast sees more)', numbers=sites).save(os.path.join(OUTDIR, 'focus-vsat-candidates.jpg'), quality=85, optimize=True)
for t in (70, 80, 85): print('sunlit>=%d%% & slope<=15: %.1f km2' % (t, ((il >= t) & ok).sum() * RES * RES / 1e6))
