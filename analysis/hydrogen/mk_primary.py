"""Primary base site map (DD-015): slope classes everywhere, ice candidates (blue) and hydrogen (purple),
the two VSAT sites nearest the base. Everything else removed."""
import sys, os, math, pickle, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB, cmap_classes
from hydro import supp_grid, THR, ZMIN
from PIL import Image, ImageDraw, ImageFont
PSR, OUT = sys.argv[1], sys.argv[2]
font = lambda sz: ImageFont.truetype(FB, int(sz))
base = lonlat2m(-88.4453, -63.44); mine = lonlat2m(-88.3664, -78.31)
cx, cy = (base[0] * 0.45 + mine[0] * 0.55), (base[1] * 0.45 + mine[1] * 0.55)
HW, HH = 17500, 13500; RES = 20
B = (cx - HW, cy - HH, cx + HW, cy + HH)
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
cand = Image.new('L', (W, H), 0); oth = Image.new('L', (W, H), 0); dc, do = ImageDraw.Draw(cand), ImageDraw.Draw(oth)
for gid, area, name, b, rings in P:
    if b[2] < B[0] or b[0] > B[2] or b[3] < B[1] or b[1] > B[3] or area < 0.05: continue
    d = dc if name.strip() == 'HNP_822627_2686284' else do
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
for lv in (0.6, 0.7, 0.8, 0.9):
    a[edges(Su >= lv)] = (200, 60, 255)
a[edges(mod | hi)] = (255, 255, 255)
im = Image.fromarray(a)
CONT = [(lv, edges(Su >= lv)) for lv in (0.6, 0.7, 0.8, 0.9)]
e = oth & ~(np.roll(oth, 1, 0) & np.roll(oth, -1, 0) & np.roll(oth, 1, 1) & np.roll(oth, -1, 1))
e = e | np.roll(e, 1, 0) | np.roll(e, 1, 1)
a = np.array(im); a[e] = (120, 200, 255); im = Image.fromarray(a); dr = ImageDraw.Draw(im)
k = W / 1400; F = font(24 * k); Fs = font(17 * k)
for lv, em in CONT:  # label each contour once, at its point nearest the frame centre
    ys_, xs_ = np.nonzero(em)
    if len(xs_) == 0: continue
    i_ = np.argmin((xs_ - W * 0.6) ** 2 + (ys_ - H * 0.35) ** 2)
    dr.text((xs_[i_], ys_[i_]), '%.1f%%' % lv, font=font(18 * k), fill=(230, 160, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
# arrow to the nearest high-hydrogen zone
FS = np.load('focus_S.npy'); FZ = np.load('focus_Z.npy'); from render import px2m as _p
fx0_, fy1_ = _p(292, 518); jj_, ii_ = np.nonzero((FS >= THR) & (FZ >= ZMIN))
HXs = fx0_ + (ii_ + 0.5) * 1000; HYs = fy1_ - (jj_ + 0.5) * 1000
dd = np.hypot(HXs - base[0], HYs - base[1]); n_ = dd.argmin(); tx, ty = HXs[n_], HYs[n_]
ux, uy = (tx - base[0]) / dd[n_], (ty - base[1]) / dd[n_]
# point where the ray from the base leaves the frame
tmax = min([t for t in ((B[2] - base[0]) / ux if ux > 0 else (B[0] - base[0]) / ux if ux < 0 else 1e9,
                        (B[3] - base[1]) / uy if uy > 0 else (B[1] - base[1]) / uy if uy < 0 else 1e9) if t > 0])
ex, ey = m2p(base[0] + ux * (tmax - 1500), base[1] + uy * (tmax - 1500)); sx_, sy_ = m2p(base[0] + ux * (tmax - 6000), base[1] + uy * (tmax - 6000))
dr.line([(sx_, sy_), (ex, ey)], fill=(220, 90, 255), width=int(6 * k))
ang = math.atan2(ey - sy_, ex - sx_); hl = 22 * k
dr.polygon([(ex + 6 * k * math.cos(ang), ey + 6 * k * math.sin(ang)), (ex - hl * math.cos(ang - 0.45), ey - hl * math.sin(ang - 0.45)), (ex - hl * math.cos(ang + 0.45), ey - hl * math.sin(ang + 0.45))], fill=(220, 90, 255))
dr.text((sx_ - 10 * k, sy_ + 18 * k), 'High hydrogen zone, %.0f km' % (dd[n_] / 1000), font=Fs, fill=(235, 170, 255), anchor='rm', stroke_width=3, stroke_fill=(0, 0, 0))
# features
x, y = m2p(*lonlat2m(-88.5, -87.1)); rr = 16200 / RES
dr.arc((x - rr, y - rr, x + rr, y + rr), 0, 360, fill=(0, 230, 255), width=int(3 * k))
dr.text((x + rr * 0.15, y + rr * 0.55), 'de Gerlache', font=F, fill=(0, 230, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
x, y = m2p(*lonlat2m(-88.5352, -97.4007))
if 0 <= x < W and 0 <= y < H:
    r = 9 * k; dr.ellipse((x - r, y - r, x + r, y + r), fill='white', outline=(20, 120, 255), width=3)
# DD-016: mine grid (rim VSATs + mine PMC) and base grid (own VSATs)
MV = [(-88.4657, -67.872, 75.1), (-88.3937, -68.686, 71.9)]
BV = [(-88.6652, -68.42, 82.7), (-88.7108, -68.28, 53.8), (-88.4411, -62.44, 50.4)]
bx, by = m2p(*base); mx, my = m2p(*mine)
mp = m2p(*lonlat2m(-88.3937, -68.686)); mp = (mp[0] - 26 * k, mp[1] + 6 * k)   # mine PMC beside VSAT M2
# base grid lines
for la, lo, p_ in BV:
    x, y = m2p(*lonlat2m(la, lo)); dr.line([(bx, by), (x, y)], fill=(255, 140, 0), width=int(4 * k))
# mine grid lines
for la, lo, p_ in MV:
    x, y = m2p(*lonlat2m(la, lo)); dr.line([mp, (x, y)], fill=(80, 230, 255), width=int(4 * k))
for q in range(0, 100, 4):
    t0, t1 = q / 100, min(1, (q + 2) / 100)
    dr.line([(mp[0] + (mx - mp[0]) * t0, mp[1] + (my - mp[1]) * t0), (mp[0] + (mx - mp[0]) * t1, mp[1] + (my - mp[1]) * t1)], fill=(80, 230, 255), width=int(4 * k))
for n, (la, lo, p_) in enumerate(BV, 1):
    x, y = m2p(*lonlat2m(la, lo)); r = 12 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(255, 140, 0), outline='black', width=3)
    dkm = math.hypot(*(np.array(lonlat2m(la, lo)) - np.array(base))) / 1000
    if n < 3:
        dr.text((x - 18 * k, y + (-14 if n == 1 else 16) * k), 'Base VSAT B%d: %.1f%% sunlit, %.1f km to base' % (n, p_, dkm), font=Fs, fill=(255, 190, 90), anchor='rm', stroke_width=3, stroke_fill=(0, 0, 0))
    else:
        dr.text((x + 16 * k, y - 12 * k), 'B3 backup/charging: %.1f%% sunlit, %.1f km' % (p_, dkm), font=Fs, fill=(255, 190, 90), anchor='lb', stroke_width=3, stroke_fill=(0, 0, 0))
for n, (la, lo, p_) in enumerate(MV, 1):
    x, y = m2p(*lonlat2m(la, lo)); r = 12 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(80, 230, 255), outline='black', width=3)
    dr.text((x + 18 * k, y + (-18 if n == 1 else 18) * k), 'Mine VSAT M%d: %.1f%% sunlit' % (n, p_), font=Fs, fill=(150, 240, 255), anchor='lm', stroke_width=3, stroke_fill=(0, 0, 0))
r = 11 * k; dr.rectangle((mp[0] - r, mp[1] - r, mp[0] + r, mp[1] + r), fill='white', outline=(80, 230, 255), width=3)
dr.text((mp[0] - 16 * k, mp[1]), 'Mine PMC', font=Fs, fill='white', anchor='rm', stroke_width=3, stroke_fill=(0, 0, 0))
r = 12 * k; dr.rectangle((mx - r, my - r, mx + r, my + r), fill=(40, 130, 255), outline='white', width=3)
dr.text((mx, my + 20 * k), 'Ice mine: floor edge, ~8.3 km feeder from the mine PMC', font=Fs, fill='white', anchor='mt', stroke_width=3, stroke_fill=(0, 0, 0))
pts = []
for i in range(10):
    ang = math.pi / 2 + i * math.pi / 5; R_ = 22 * k if i % 2 == 0 else 10 * k; pts.append((bx + R_ * math.cos(ang), by - R_ * math.sin(ang)))
dr.polygon(pts, fill=(255, 60, 200), outline='black')
dr.text((bx + 26 * k, by), 'PRIMARY BASE  88.445°S, 63.44°W', font=F, fill=(255, 120, 220), anchor='lm', stroke_width=4, stroke_fill=(0, 0, 0))
# legend
rows = [((0, 170, 0), 'Slope ≤8° (landable)'), ((255, 220, 0), 'Slope 8–15°'), ((255, 140, 0), 'Slope 15–20°'), ((220, 0, 0), 'Slope ≥20°'),
        ((40, 130, 255), 'Ice candidate: de Gerlache shadowed floor'), ((120, 200, 255), 'Outline: other shadowed areas (no ice data)'),
        ((255, 140, 0), 'Base grid: VSATs B1–B2 (long runs), B3 backup/charging (DD-017)'), ((80, 230, 255), 'Ice-mine grid: VSATs M1–M2, mine PMC, feeder (DD-016)'),
        ((150, 40, 200), 'High hydrogen (LEND, top 10%), off-map: arrow'), ((175, 80, 230), 'Moderate hydrogen (top 25%), white edge'), ((200, 60, 255), 'Purple tint and lines: LEND dip 0.6–0.9% (darker = more H)')]
lx, ly = int(20 * k), int(48 * k)
dr.rectangle((lx - 10 * k, ly - 10 * k, lx + 520 * k, ly + (len(rows) * 30 + 40) * k), fill=(0, 0, 0))
dr.text((lx, ly + 12 * k), 'Primary base site (DD-015)', font=Fs, fill='white', anchor='lm'); yy = ly + 34 * k
for c, t in rows:
    dr.rectangle((lx, yy, lx + 40 * k, yy + 18 * k), fill=c); dr.text((lx + 50 * k, yy + 9 * k), t, font=Fs, fill='white', anchor='lm'); yy += 30 * k
L = 5000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '5 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(32 * k)), fill=(0, 0, 0))
dr.text((10 * k, 7 * k), 'Primary base site. Slope & shadowed areas: NASA GSFC LOLA (Barker et al. 2023). Hydrogen: NASA LRO LEND (PDS), Open Moon processing. VSAT sunlight: NASA GSFC (Mazarico et al. 2011).', font=font(14 * k), fill='white')
im.thumbnail((2400, 2400), Image.LANCZOS); im.save(OUT, quality=88, optimize=True)
print('hydrogen in frame: high %.1f%%, moderate %.1f%%' % (hi.mean() * 100, mod.mean() * 100))
