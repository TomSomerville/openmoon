"""ESTIMATE: animated sunlight and shadow over the Open Moon focus area for one lunar day.
Shadows from NASA LOLA terrain (80 m) and Sun directions from NASA/JPL DE421 (MOON_ME frame), every 12 hours.
Usage: anim.py NAME OUT.gif"""
import sys, math, csv, numpy as np
sys.path.insert(0, '../slope')
from render import read, px2m, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
NAME, OUT = sys.argv[1], sys.argv[2]
R = 1737400.0
dem = np.load('dem80.npy'); DB = (-216400., -216400., 216400., 216400.); DR = 80.
suns = np.load('anim_sun_%s.npy' % NAME); times = open('anim_t_%s.txt' % NAME).read().split('\n')
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); G = 250.
xs = np.arange(B[0] + G / 2, B[2], G); ys = np.arange(B[3] - G / 2, B[1], -G)
X, Y = np.meshgrid(xs, ys); H, W = X.shape

def bil(x, y):
    c = (x - DB[0]) / DR - 0.5; r = (DB[3] - y) / DR - 0.5
    c0 = np.clip(np.floor(c).astype(int), 0, dem.shape[1] - 2); r0 = np.clip(np.floor(r).astype(int), 0, dem.shape[0] - 2)
    fc = np.clip(c - c0, 0, 1); fr = np.clip(r - r0, 0, 1)
    return dem[r0, c0] * (1 - fc) * (1 - fr) + dem[r0, c0 + 1] * fc * (1 - fr) + dem[r0 + 1, c0] * (1 - fc) * fr + dem[r0 + 1, c0 + 1] * fc * fr

Z0 = bil(X, Y) + 0.5
rho = np.hypot(X, Y); lat = -(math.pi / 2 - 2 * np.arctan(rho / (2 * R))); lon = np.arctan2(X, Y)
U = np.stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])     # local up, ME frame
E = np.stack([-np.sin(lon), np.cos(lon), np.zeros_like(lon)]); N = np.cross(U, E, axis=0)
D = np.concatenate([np.arange(G, 30000, G), np.arange(30000, 200000, 1000.)])
hs = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, 40)).astype('float32')
hs = np.array(Image.fromarray(hs, mode='F').resize((W, H), Image.BILINEAR))
hv = np.clip((hs - np.percentile(hs, 1)) / (np.percentile(hs, 99) - np.percentile(hs, 1)), 0, 1)
SC = 1.3   # output scale (keeps the GIF small)
font = lambda sz: ImageFont.truetype(FB, int(sz))
m2p = lambda x, y: ((x - B[0]) / G * SC, (B[3] - y) / G * SC)
sites = [(float(r['x_m']), float(r['y_m']), float(r['sunlit_pct'])) for r in csv.DictReader(open('/home/user/openmoon/analysis/sunlight/vsat_spots.csv'))]
frames = []
# fixed palette: shaded grey-to-navy ramp plus the label and dot colours, so dots keep their colour
cols = []
for t in np.linspace(0, 1, 12):
    for g in np.linspace(0, 255, 18):
        c = np.array([g, g, g]) * (0.15 + 0.85 * t) + np.array([10, 20, 60]) * (1 - t) * 0.6; cols.append(tuple(int(v) for v in np.clip(c, 0, 255)))
cols += [(255, 140, 0), (255, 230, 0), (0, 230, 255), (0, 200, 230), (255, 255, 255), (0, 0, 0), (220, 220, 220)]
cols = cols[:256]; flat = [v for c in cols for v in c] + [0] * (768 - 3 * len(cols))
PAL = Image.new('P', (1, 1)); PAL.putpalette(flat)
for k in range(suns.shape[1]):
    s = suns[:, k]
    su = np.tensordot(s, U, 1); se = np.tensordot(s, E, 1); sn = np.tensordot(s, N, 1)
    elev = np.degrees(np.arcsin(np.clip(su, -1, 1)))
    vx = sn * np.sin(lon) + se * np.cos(lon); vy = sn * np.cos(lon) - se * np.sin(lon); nv = np.hypot(vx, vy) + 1e-12
    vx /= nv; vy /= nv
    mx = np.full((H, W), -90.0)
    for d in D:
        z = bil(X + vx * d, Y + vy * d)
        mx = np.maximum(mx, np.degrees(np.arctan2(z - Z0 - d * d / (2 * R), d)))
    lit = np.clip((elev - mx + 0.2666) / 0.5332, 0, 1)
    base = np.stack([hv * 255] * 3, -1)
    rgb = base * (0.15 + 0.85 * lit[..., None]) + np.array([10, 20, 60]) * (1 - lit[..., None]) * 0.6
    im = Image.fromarray(rgb.clip(0, 255).astype('uint8')).resize((int(W * SC), int(H * SC)), Image.BILINEAR)
    dr = ImageDraw.Draw(im); F = font(15); Fs = font(11)
    for la, lo, dia, lab in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton'), (-88.5, -87.1, 32.4, 'de Gerlache'), (-89.51, -84.61, 13.0, 'Spudis')]:
        x, y = m2p(*lonlat2m(la, lo)); rr = dia * 500 / G * SC
        dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 200, 230), width=2)
        dr.text((x, y - rr - 4), lab, font=F, fill=(0, 230, 255), anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
    for X0, Y0, p in sites:
        x, y = m2p(X0, Y0); r = 4 if p >= 80 else 3
        dr.ellipse((x - r, y - r, x + r, y + r), fill=(255, 140, 0) if p >= 80 else (255, 230, 0), outline=(0, 0, 0))
    sub = math.degrees(math.asin(s[2]))
    dr.rectangle((0, 0, W * SC, 22), fill=(0, 0, 0))
    dr.text((6, 5), '%s UTC   ·   Sun %.2f° %s of the lunar equator   ·   ESTIMATE (Open Moon shadow calculation)' % (times[k], abs(sub), 'south' if sub < 0 else 'north'), font=Fs, fill='white')
    dr.rectangle((0, H * SC - 20, W * SC, H * SC), fill=(0, 0, 0))
    dr.text((6, H * SC - 16), 'Lit = bright, shadow = dark. Dots: VSAT sites (orange ≥80%, yellow 70–80% average sunlight). Terrain: NASA LOLA; Sun: NASA/JPL DE421.', font=Fs, fill=(220, 220, 220))
    frames.append(im.quantize(palette=PAL, dither=Image.Dither.NONE))
    print(k, flush=True)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=180, loop=0, optimize=True)
print('saved', OUT, flush=True)
