"""Site selection overview (DD-015, DD-016, DD-017): both base sites with their final power layouts, slope classes,
ice candidates (blue) and hydrogen (purple). Explored-but-dropped VSAT options are left out.
Usage: mk_overview.py psr_focus.pkl OUT.jpg   (run where focus_S.npy / focus_Z.npy are)"""
import sys, os, math, pickle, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB, cmap_classes
from hydro import supp_grid, THR, ZMIN
from PIL import Image, ImageDraw, ImageFont
PSR, OUT = sys.argv[1], sys.argv[2]
font = lambda sz: ImageFont.truetype(FB, int(sz))
frame_base = lonlat2m(-88.4453, -63.44)   # map frame stays as first drawn
base = lonlat2m(-88.4262, -63.30); mine = lonlat2m(-88.3664, -78.31)   # primary base moved to the flat-patch centre (DD-020)
backup = lonlat2m(-89.559, -163.66); shack = lonlat2m(-89.67, 129.78)
KEY = [frame_base, mine, backup, shack, lonlat2m(-88.7108, -68.28), lonlat2m(-88.5, -87.1)]
xs_k = [p[0] for p in KEY]; ys_k = [p[1] for p in KEY]; M = 9000; RES = 40
B = (min(xs_k) - M, min(ys_k) - M, max(xs_k) + M, max(ys_k) + M + 6000)
s = read('LDSM_83S_10MPP_ADJ', B, RES); h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, RES)); H, W = s.shape
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
basergb = np.stack([hv * 255] * 3, -1)
rgb = basergb * 0.45 + cmap_classes(np.nan_to_num(s)) * 0.55
# hydrogen
S, Z = supp_grid(B, 500.)
up = lambda a: np.array(Image.fromarray(a.astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
Su, Zu = up(S), up(Z)
hi = (Su >= THR) & (Zu >= ZMIN); mod = (Su >= 0.98) & (Zu >= ZMIN) & ~hi
tint = np.clip((Su - 0.75) / 0.35, 0, 1)[..., None] * 0.30 * (Zu >= 2)[..., None]
rgb = rgb * (1 - tint) + np.array([170, 60, 230]) * tint
rgb = np.where(hi[..., None], rgb * 0.35 + np.array([150, 40, 200]) * 0.65, rgb)
rgb = np.where(mod[..., None], rgb * 0.45 + np.array([170, 70, 230]) * 0.55, rgb)
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
# ice: de Gerlache floor (candidate) filled, other PSRs outlined
P = pickle.load(open(PSR, 'rb'))
CANDS = [(shack, 10.5e3), (lonlat2m(-88.5, -87.1), 16.2e3)]
cand = Image.new('L', (W, H), 0); oth = Image.new('L', (W, H), 0); dc, do = ImageDraw.Draw(cand), ImageDraw.Draw(oth)
for gid, area, name, b, rings in P:
    if b[2] < B[0] or b[0] > B[2] or b[3] < B[1] or b[1] > B[3] or area < 0.05: continue
    cx_, cy_ = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    is_c = area > 1 and any(math.hypot(cx_ - p[0], cy_ - p[1]) < rad for p, rad in CANDS)
    if not is_c and area < 0.3: continue
    d = dc if is_c else do
    for r in rings:
        sa = 0.5 * (r[:-1, 0] * r[1:, 1] - r[1:, 0] * r[:-1, 1]).sum()
        d.polygon([m2p(x, y) for x, y in r], fill=255 if sa < 0 else 0)
cand = np.array(cand) > 0; oth = np.array(oth) > 0
rgb = np.where(cand[..., None], rgb * 0.3 + np.array([20, 120, 255]) * 0.7, rgb)
im = Image.fromarray(rgb.clip(0, 255).astype('uint8'))
# hydrogen contours (LEND neutron dip) across the frame
def edges(mask):
    e_ = mask & ~(np.roll(mask, 1, 0) & np.roll(mask, -1, 0) & np.roll(mask, 1, 1) & np.roll(mask, -1, 1))
    for _ in range(2): e_ = e_ | np.roll(e_, 1, 0) | np.roll(e_, 1, 1) | np.roll(e_, -1, 0) | np.roll(e_, -1, 1)
    return e_
a = np.array(im)
a[edges(mod | hi)] = (255, 255, 255)
im = Image.fromarray(a)
e = oth & ~(np.roll(oth, 1, 0) & np.roll(oth, -1, 0) & np.roll(oth, 1, 1) & np.roll(oth, -1, 1))
e = e | np.roll(e, 1, 0) | np.roll(e, 1, 1)
a = np.array(im); a[e] = (120, 200, 255); im = Image.fromarray(a); dr = ImageDraw.Draw(im)
k = W / 1700; F = font(26 * k); Fs = font(18 * k)

def star(x, y, col, R=22):
    pts = []
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5; R_ = R * k if i % 2 == 0 else R * 0.45 * k; pts.append((x + R_ * math.cos(ang), y - R_ * math.sin(ang)))
    dr.polygon(pts, fill=col, outline='black')
def dot(x, y, col, r=11):
    dr.ellipse((x - r * k, y - r * k, x + r * k, y + r * k), fill=col, outline='black', width=3)
def txt(x, y, t, col, anc='lm', f=None):
    dr.text((x, y), t, font=f or Fs, fill=col, anchor=anc, stroke_width=3, stroke_fill=(0, 0, 0))
P2 = lambda la, lo: m2p(*lonlat2m(la, lo))
# craters
for la, lo, dia, lab, off in [(-88.5, -87.1, 32.4, 'de Gerlache', (0.0, 0.62)), (-89.67, 129.78, 21.0, 'Shackleton', (0.0, -1.18)), (-89.51, -84.61, 13.0, 'Spudis', (0.0, -1.25))]:
    x, y = P2(la, lo); rr = dia * 500 / RES
    dr.arc((x - rr, y - rr, x + rr, y + rr), 0, 360, fill=(0, 230, 255), width=int(3 * k))
    txt(x + rr * off[0], y + rr * off[1], lab, (0, 230, 255), 'mm', F)
x, y = P2(-88.5352, -97.4007); r = 8 * k; dr.ellipse((x - r, y - r, x + r, y + r), fill='white', outline=(20, 120, 255), width=3)
txt(x + 14 * k, y, 'ShadowCam bright spot', 'white')
OR, CY = (255, 140, 0), (80, 230, 255)
# ---- primary: base grid (B1-B3) and isolated ice-mine grid (M1-M2, PMC, feeder)
BV = [('B1', -88.6652, -68.42, 82.7), ('B2', -88.7108, -68.28, 53.8), ('B3', -88.4411, -62.44, 50.4)]
MV = [('M1', -88.4657, -67.872, 75.1), ('M2', -88.3937, -68.686, 71.9)]
bx, by = m2p(*base); mx, my = m2p(*mine)
mp = P2(-88.3937, -68.686); mp = (mp[0] - 22 * k, mp[1] + 6 * k)
for n, la, lo, p_ in BV:
    x, y = P2(la, lo); dr.line([(bx, by), (x, y)], fill=OR, width=int(4 * k))
for n, la, lo, p_ in MV:
    x, y = P2(la, lo); dr.line([mp, (x, y)], fill=CY, width=int(4 * k))
for q in range(0, 100, 5):
    t0, t1 = q / 100, min(1, (q + 2.5) / 100)
    dr.line([(mp[0] + (mx - mp[0]) * t0, mp[1] + (my - mp[1]) * t0), (mp[0] + (mx - mp[0]) * t1, mp[1] + (my - mp[1]) * t1)], fill=CY, width=int(4 * k))
for n, la, lo, p_ in BV:
    x, y = P2(la, lo); dot(x, y, OR)
lab = {'B1': (16, -2, 'lm'), 'B2': (16, 14, 'lm'), 'B3': (14, -14, 'lb')}
for n, la, lo, p_ in BV:
    x, y = P2(la, lo); dx, dy, an = lab[n]; txt(x + dx * k, y + dy * k, '%s %.1f%%' % (n, p_), (255, 190, 90), an)
for n, la, lo, p_ in MV:
    x, y = P2(la, lo); dot(x, y, CY)
    txt(x + (-6 if n == 'M1' else 14) * k, y + (-14 if n == 'M1' else 14) * k, '%s %.1f%%' % (n, p_), (150, 240, 255), 'rb' if n == 'M1' else 'lt')
r = 10 * k; dr.rectangle((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), fill='white', outline=CY, width=3)
txt(mp[0] - 16 * k, mp[1] + 4 * k, 'Mine PMC', 'white', 'rt')
r = 11 * k; dr.rectangle((mx - r, my - r, mx + r, my + r), fill=(40, 130, 255), outline='white', width=3)
txt(mx, my + 18 * k, 'Ice mine', 'white', 'mt')
star(bx, by, (255, 60, 200), 26)
txt(bx + 28 * k, by - 6 * k, 'PRIMARY BASE', (255, 120, 220), 'lb', F)
txt(bx + 28 * k, by + 2 * k, '88.426°S, 63.30°W', (255, 160, 230), 'lt')
# ---- backup: Connecting ridge trio on 3 km runs to a ridge PMC, extended run to the base
AV = [('A1', -89.4745, -137.53, 81.9), ('A2', -89.3807, -140.91, 59.6), ('A3', -89.4176, -134.94, 48.3)]
rp = P2(-89.438, -137.65); kx, ky = m2p(*backup)
dr.line([(kx, ky), rp], fill=OR, width=int(4 * k))
for n, la, lo, p_ in AV:
    x, y = P2(la, lo); dr.line([rp, (x, y)], fill=OR, width=int(4 * k))
for n, la, lo, p_ in AV:
    x, y = P2(la, lo); dot(x, y, OR, 10)
lab = {'A1': (-14, -6, 'rb'), 'A2': (-14, 0, 'rm'), 'A3': (14, -10, 'lb')}
for n, la, lo, p_ in AV:
    x, y = P2(la, lo); dx, dy, an = lab[n]; txt(x + dx * k, y + dy * k, '%s %.1f%%' % (n, p_), (255, 190, 90), an)
r = 10 * k; dr.rectangle((rp[0] - r, rp[1] - r, rp[0] + r, rp[1] + r), fill='white', outline=OR, width=3)
star(kx, ky, (170, 90, 255), 24)
txt(kx + 26 * k, ky - 6 * k, 'BACKUP BASE', (205, 160, 255), 'lb', F)
txt(kx + 26 * k, ky + 2 * k, '89.559°S, 163.66°W', (215, 185, 255), 'lt')
# legend
rows = [((0, 170, 0), 'Slope ≤8° (landable)'), ((255, 220, 0), 'Slope 8–15°'), ((255, 140, 0), 'Slope 15–20°'), ((220, 0, 0), 'Slope ≥20°'),
        ((40, 130, 255), 'Ice candidate: Shackleton and de Gerlache shadowed floors'), ((120, 200, 255), 'Outline: other shadowed areas (no ice data)'),
        ((150, 40, 200), 'High hydrogen (LEND, top 10%)'), ((175, 80, 230), 'Moderate hydrogen (top 25%), white edge'), ((200, 60, 255), 'Purple tint: LEND neutron dip (darker = more hydrogen)'),
        ((255, 60, 200), 'Primary base (DD-015)'), ((170, 90, 255), 'Backup base (DD-015)'),
        (OR, 'Base power: VSATs (B, A) and cables; % = sunlit (NASA map)'), (CY, 'Primary ice-mine grid: M1–M2, mine PMC, feeder (DD-016)'),
        ((255, 255, 255), 'White square: PMC · blue square: ice mine')]
L = 10000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(32 * k)), fill=(0, 0, 0))
dr.text((10 * k, 7 * k), 'Site selection. Slope & shadowed areas: NASA GSFC LOLA (Barker et al. 2023). Hydrogen: NASA LRO LEND (PDS), Open Moon processing. Ice: Li et al. 2018, 2026. VSAT sunlight: NASA GSFC (Mazarico et al. 2011).', font=font(14 * k), fill='white')
PW = int(640 * k); full = Image.new('RGB', (W + PW, H), (0, 0, 0)); full.paste(im, (0, 0)); im = full; dr = ImageDraw.Draw(im)
lx, ly = W + int(24 * k), int(56 * k)
dr.text((lx, ly + 12 * k), 'Chosen base sites and final power layouts', font=Fs, fill='white', anchor='lm'); yy = ly + 34 * k
for c, t in rows:
    dr.rectangle((lx, yy, lx + 40 * k, yy + 18 * k), fill=c); dr.text((lx + 50 * k, yy + 9 * k), t, font=Fs, fill='white', anchor='lm'); yy += 30 * k
im.thumbnail((2600, 2600), Image.LANCZOS); im.save(OUT, quality=88, optimize=True)
print('size', W, H, 'high H %.1f%%' % (hi.mean() * 100))
