"""ESTIMATE: animated sunlight and shadow over the primary base and the 10 km around it, for one lunar day.
Shadows: Open Moon horizon calculation over NASA LOLA terrain (10 m near the base, then 20 m and 80 m out to 200 km),
with lunar curvature. Sun directions: NASA/JPL DE421 (MOON_ME frame), every 12 hours (from analysis/sunlight).
Usage: base_anim.py SEASON(summer|winter) OUT.gif   (run in the folder holding dem20/dem80 and anim_sun_*.npy)"""
import sys, os, math, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont
SEASON, OUT = sys.argv[1], sys.argv[2]
R = 1737400.
C = np.array(lonlat2m(-88.4365, -62.46)); HALF = 10000.; G = 40.
d80 = np.load('dem80.npy'); B80 = (-216400., -216400., 216400., 216400.)
d20 = np.load('dem20.npy'); B20 = tuple(np.load('dem20_bounds.npy'))
NB = (C[0] - 15000, C[1] - 15000, C[0] + 15000, C[1] + 15000)
d10 = np.nan_to_num(read('LDEM_83S_10MPP_ADJ', NB, 10)).astype('float32')
def bil(dem, b, res, x, y):
    c = (x - b[0]) / res - 0.5; r = (b[3] - y) / res - 0.5; H, W = dem.shape
    c0 = np.clip(np.floor(c).astype(int), 0, W - 2); r0 = np.clip(np.floor(r).astype(int), 0, H - 2)
    fc = np.clip(c - c0, 0, 1); fr = np.clip(r - r0, 0, 1)
    return dem[r0, c0] * (1 - fc) * (1 - fr) + dem[r0, c0 + 1] * fc * (1 - fr) + dem[r0 + 1, c0] * (1 - fc) * fr + dem[r0 + 1, c0 + 1] * fc * fr
xs = np.arange(C[0] - HALF + G / 2, C[0] + HALF, G); ys = np.arange(C[1] + HALF - G / 2, C[1] - HALF, -G)
X, Y = np.meshgrid(xs, ys); H, W = X.shape
Z0 = bil(d10, NB, 10., X, Y) + 1.0
rho = np.hypot(X, Y); lat = -(math.pi / 2 - 2 * np.arctan(rho / (2 * R))); lon = np.arctan2(X, Y)
U = np.stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])
E = np.stack([-np.sin(lon), np.cos(lon), np.zeros_like(lon)]); N = np.cross(U, E, axis=0)
STEPS = [(d10, NB, 10., np.arange(20., 5000., 40.)), (d20, B20, 20., np.arange(5000., 30000., 100.)), (d80, B80, 80., np.arange(30000., 200000., 800.))]
suns = np.load('anim_sun_%s.npy' % SEASON)
# background: LOLA hillshade at 10 m, flat patch outline, markers
OUTPX = 800; k = OUTPX / (2 * HALF)
hs = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', (C[0] - HALF, C[1] - HALF, C[0] + HALF, C[1] + HALF), 10)).astype('float32')
hv = np.clip((hs - np.percentile(hs, 1)) / (np.percentile(hs, 99) - np.percentile(hs, 1)), 0, 1)
hv = np.array(Image.fromarray((hv * 255).astype('uint8')).resize((OUTPX, OUTPX), Image.LANCZOS)) / 255.
sl = read('LDSM_83S_10MPP_ADJ', (C[0] - HALF, C[1] - HALF, C[0] + HALF, C[1] + HALF), 10)
lab, _ = ndimage.label(sl <= 8); patch = lab == lab[sl.shape[0] // 2, sl.shape[1] // 2]
pe = np.array(Image.fromarray((patch * 255).astype('uint8')).resize((OUTPX, OUTPX), Image.NEAREST)) > 0
edge = pe & ~ndimage.binary_erosion(pe, iterations=2)
m2p = lambda x, y: ((x - (C[0] - HALF)) * k, ((C[1] + HALF) - y) * k)
# DD-024: base towers B1/B2 stand beside mine towers M1/M2; B4 + M3 are the first expansion towers (old B2 spot)
PTS = [('B1+M1', (-88.4657, -67.872), (255, 140, 0)), ('B2+M2', (-88.3937, -68.686), (255, 140, 0)), ('B3', (-88.3693, -62.11), (255, 140, 0)),
       ('B4+M3 (expansion)', (-88.7108, -68.28), (0, 220, 255))]
cols = []
for t in np.linspace(0, 1, 12):
    for g in np.linspace(0, 255, 18):
        c = np.array([g, g, g]) * (0.15 + 0.85 * t) + np.array([10, 20, 60]) * (1 - t) * 0.6; cols.append(tuple(int(v) for v in np.clip(c, 0, 255)))
cols += [(255, 140, 0), (0, 220, 255), (255, 60, 200), (60, 230, 120), (255, 255, 255), (0, 0, 0), (220, 220, 220)]
PAL = Image.new('P', (1, 1)); PAL.putpalette([v for c in cols[:256] for v in c] + [0] * (768 - 3 * len(cols[:256])))
F = lambda z: ImageFont.truetype(FB, int(z))
frames = []; litbase = []
for kf in range(suns.shape[1]):
    s = suns[:, kf]
    su = np.tensordot(s, U, 1); se = np.tensordot(s, E, 1); sn = np.tensordot(s, N, 1)
    elev = np.degrees(np.arcsin(np.clip(su, -1, 1)))
    vx = sn * np.sin(lon) + se * np.cos(lon); vy = sn * np.cos(lon) - se * np.sin(lon); nv = np.hypot(vx, vy) + 1e-12; vx /= nv; vy /= nv
    mx = np.full((H, W), -90.0, 'float32')
    for dem, b, res, D in STEPS:
        for d in D:
            z = bil(dem, b, res, X + vx * d, Y + vy * d)
            np.maximum(mx, np.degrees(np.arctan2(z - Z0 - d * d / (2 * R), d)), out=mx)
    lit = np.clip((elev - mx + 0.2666) / 0.5332, 0, 1)
    litbase.append(lit[H // 2, W // 2])
    L = np.array(Image.fromarray((lit * 255).astype('uint8')).resize((OUTPX, OUTPX), Image.BILINEAR)) / 255.
    rgb = np.stack([hv * 255] * 3, -1) * (0.15 + 0.85 * L[..., None]) + np.array([10, 20, 60]) * (1 - L[..., None]) * 0.6
    rgb[edge] = (60, 230, 120)
    im = Image.fromarray(rgb.clip(0, 255).astype('uint8')); dr = ImageDraw.Draw(im)
    for n, (la, lo), col in PTS:
        x, y = m2p(*lonlat2m(la, lo)); dr.ellipse((x - 6, y - 6, x + 6, y + 6), fill=col, outline='black', width=2)
        dr.text((x + 9, y), n, font=F(14), fill=col, anchor='lm', stroke_width=3, stroke_fill='black')
    bx, by = m2p(*C); pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5; R_ = 11 if i % 2 == 0 else 5; pts.append((bx + R_ * math.cos(a), by - R_ * math.sin(a)))
    dr.polygon(pts, fill=(255, 60, 200), outline='black')
    dr.rectangle((0, 0, OUTPX, 24), fill='black')
    dr.text((8, 5), '%s season · day %4.1f of the lunar day · base %s' % ('Best' if SEASON == 'summer' else 'Worst', kf * 0.5, 'lit' if lit[H // 2, W // 2] > 0.5 else 'in shadow'), font=F(14), fill='white')
    dr.rectangle((0, OUTPX - 22, OUTPX, OUTPX), fill='black')
    dr.text((8, OUTPX - 17), 'ESTIMATE · 20 × 20 km · green: flat patch · star: base · orange: initial towers · cyan: expansion towers · LOLA terrain, DE421 Sun', font=F(11), fill=(220, 220, 220))
    frames.append(im.quantize(palette=PAL, dither=Image.Dither.NONE)); print(kf, flush=True)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=200, loop=0, optimize=True)
print('base lit in %d of %d frames' % (sum(v > 0.5 for v in litbase), len(litbase)))
