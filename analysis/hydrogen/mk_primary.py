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
rgb = np.where(hi[..., None], rgb * 0.5 + np.array([150, 40, 200]) * 0.5, rgb)
rgb = np.where(mod[..., None], rgb * 0.75 + np.array([170, 110, 220]) * 0.25, rgb)
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
e = oth & ~(np.roll(oth, 1, 0) & np.roll(oth, -1, 0) & np.roll(oth, 1, 1) & np.roll(oth, -1, 1))
e = e | np.roll(e, 1, 0) | np.roll(e, 1, 1)
a = np.array(im); a[e] = (120, 200, 255); im = Image.fromarray(a); dr = ImageDraw.Draw(im)
k = W / 1400; F = font(24 * k); Fs = font(17 * k)
# features
x, y = m2p(*lonlat2m(-88.5, -87.1)); rr = 16200 / RES
dr.arc((x - rr, y - rr, x + rr, y + rr), 0, 360, fill=(0, 230, 255), width=int(3 * k))
dr.text((x + rr * 0.15, y + rr * 0.55), 'de Gerlache', font=F, fill=(0, 230, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
x, y = m2p(*lonlat2m(-88.5352, -97.4007))
if 0 <= x < W and 0 <= y < H:
    r = 9 * k; dr.ellipse((x - r, y - r, x + r, y + r), fill='white', outline=(20, 120, 255), width=3)
# VSATs: two closest sites to the base
V = [(-88.4657, -67.872, 75.1, 3.7), (-88.3937, -68.686, 71.9, 4.7)]
bx, by = m2p(*base); mx, my = m2p(*mine)
for n, (la, lo, p, d) in enumerate(V, 1):
    x, y = m2p(*lonlat2m(la, lo))
    dr.line([(bx, by), (x, y)], fill=(255, 140, 0), width=int(3 * k))
    for q in range(0, 100, 5):
        t0, t1 = q / 100, min(1, (q + 2.5) / 100)
        dr.line([(x + (mx - x) * t0, y + (my - y) * t0), (x + (mx - x) * t1, y + (my - y) * t1)], fill='white', width=int(3 * k))
for n, (la, lo, p, d) in enumerate(V, 1):
    x, y = m2p(*lonlat2m(la, lo)); r = 12 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(255, 140, 0), outline='black', width=3)
    oy = -20 if n == 1 else 20
    dr.text((x + 18 * k, y + oy * k), 'VSAT %d: %.1f%% sunlit, %.1f km to base' % (n, p, d), font=Fs, fill=(255, 190, 90), anchor='lm', stroke_width=3, stroke_fill=(0, 0, 0))
r = 12 * k; dr.rectangle((mx - r, my - r, mx + r, my + r), fill=(40, 130, 255), outline='white', width=3)
dr.text((mx, my + 20 * k), 'Ice mine: floor edge, 8–9 km from the VSATs', font=Fs, fill='white', anchor='mt', stroke_width=3, stroke_fill=(0, 0, 0))
pts = []
for i in range(10):
    ang = math.pi / 2 + i * math.pi / 5; R_ = 22 * k if i % 2 == 0 else 10 * k; pts.append((bx + R_ * math.cos(ang), by - R_ * math.sin(ang)))
dr.polygon(pts, fill=(255, 60, 200), outline='black')
dr.text((bx + 26 * k, by), 'PRIMARY BASE  88.445°S, 63.44°W', font=F, fill=(255, 120, 220), anchor='lm', stroke_width=4, stroke_fill=(0, 0, 0))
# legend
rows = [((0, 170, 0), 'Slope ≤8° (landable)'), ((255, 220, 0), 'Slope 8–15°'), ((255, 140, 0), 'Slope 15–20°'), ((220, 0, 0), 'Slope ≥20°'),
        ((40, 130, 255), 'Ice candidate: de Gerlache shadowed floor'), ((120, 200, 255), 'Outline: other shadowed areas (no ice data)'),
        ((150, 40, 200), 'High hydrogen (LEND, top 10%)'), ((185, 140, 225), 'Moderate hydrogen (top 25%)')]
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
