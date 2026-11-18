"""Focus-area map: landable ground (slope <=8 deg, green), high hydrogen (LEND, purple),
ice candidates (blue): permanently shadowed regions (NASA GSFC LPSR) of Shackleton and de Gerlache,
where published ice detections are reported, plus the ShadowCam high-reflectance spot."""
import sys, os, math, pickle, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, px2m, lonlat2m, FB
from hydro import supp_grid, THR, ZMIN
from PIL import Image, ImageDraw, ImageFont
PSR = sys.argv[1] if len(sys.argv) > 1 else 'psr_focus.pkl'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'focus-landing-hydrogen-ice.jpg'
font = lambda sz: ImageFont.truetype(FB, int(sz))
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); RES = 40
s = read('LDSM_83S_10MPP_ADJ', B, RES); h = read('LDEM_83S_10MPP_ADJ_HILL', B, RES); H, W = s.shape
S, Z = supp_grid(B, 1000.)
up = lambda a: np.array(Image.fromarray(a.astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
high = (up(S) >= THR) & (up(Z) >= ZMIN)
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
# PSR rasters
psrs = pickle.load(open(PSR, 'rb'))
CANDS = {'Shackleton': (lonlat2m(-89.67, 129.78), 10.5e3), 'de Gerlache': (lonlat2m(-88.5, -87.1), 16.2e3)}
cand = Image.new('L', (W, H), 0); other = Image.new('L', (W, H), 0)
dc, do = ImageDraw.Draw(cand), ImageDraw.Draw(other)
def signed_area(r): x, y = r[:, 0], r[:, 1]; return 0.5 * (x[:-1] * y[1:] - x[1:] * y[:-1]).sum()
for gid, area, name, b, rings in psrs:
    cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    is_c = area > 1 and any(math.hypot(cx - p[0], cy - p[1]) < rad for p, rad in CANDS.values())
    if not is_c and area < 0.5: continue
    d = dc if is_c else do
    for r in rings:
        pts = [m2p(x, y) for x, y in r]
        if len(pts) < 3: continue
        d.polygon(pts, fill=255 if signed_area(r) < 0 else 0)   # shapefile: outer rings clockwise
cand = np.array(cand) > 0; other = np.array(other) > 0
hv = np.nan_to_num(h); hv = np.clip((hv - np.percentile(hv, 1)) / (np.percentile(hv, 99) - np.percentile(hv, 1)), 0, 1)
base = np.stack([hv * 255] * 3, -1)
rgb = np.where((s <= 8)[..., None], base * 0.45 + np.array([0, 170, 0]) * 0.55, base)
rgb = np.where(high[..., None], rgb * 0.55 + np.array([150, 40, 200]) * 0.45, rgb)
rgb = np.where(cand[..., None], rgb * 0.3 + np.array([20, 120, 255]) * 0.7, rgb)
im = Image.fromarray(rgb.clip(0, 255).astype('uint8'))
# thin outline for other PSRs (no published ice data)
edge = other & ~(np.roll(other, 1, 0) & np.roll(other, -1, 0) & np.roll(other, 1, 1) & np.roll(other, -1, 1))
edge = edge | np.roll(edge, 1, 0) | np.roll(edge, 1, 1) | np.roll(edge, -1, 0) | np.roll(edge, -1, 1)
a = np.array(im); a[edge] = (170, 225, 255); im = Image.fromarray(a)
dr = ImageDraw.Draw(im); k = max(W, H) / 1400; F = font(24 * k); Fs = font(16 * k)
for lat_, lon_, diam, lab, side in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton', 'r'), (-88.5, -87.1, 32.4, 'de Gerlache', 'l'), (-89.51, -84.61, 13.0, 'Spudis', 't')]:
    x, y = m2p(*lonlat2m(lat_, lon_)); rr = diam * 500 / RES
    dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 230, 255), width=max(2, int(3 * k)))
    if side == 't': dr.text((x, y - rr - 6 * k), lab, font=F, fill=(0, 230, 255), anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
    else: dr.text((x + (rr + 8 * k if side == 'r' else -rr - 8 * k), y), lab, font=F, fill=(0, 230, 255), anchor='lm' if side == 'r' else 'rm', stroke_width=3, stroke_fill=(0, 0, 0))
x, y = m2p(*lonlat2m(-89.427, -113.82)); dr.text((x, y), 'Shackleton–de Gerlache Ridge', font=font(15 * k), fill='white', anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
rx0, ry1 = px2m(537, 643); rx1, ry0 = px2m(609, 715); p0 = m2p(rx0, ry1); p1 = m2p(rx1, ry0)
dr.rectangle((*p0, *p1), outline=(255, 255, 0), width=max(2, int(3 * k))); dr.text((p0[0], p0[1] - 6 * k), 'de Gerlache Rim 2', font=F, fill=(255, 255, 0), anchor='ld', stroke_width=3, stroke_fill=(0, 0, 0))
# ShadowCam spot
x, y = m2p(*lonlat2m(-88.5352, -97.4007)); r = 9 * k
dr.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255), outline=(20, 120, 255), width=int(3 * k))
dr.text((x - 14 * k, y), 'ShadowCam bright spot', font=Fs, fill='white', anchor='rm', stroke_width=3, stroke_fill=(0, 0, 0))
# VSAT layouts (ESTIMATE): Connecting ridge set A, de Gerlache option 1 (C) and option 2 (D)
import json as _j
_M = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../sunlight/multi/')
_A = _j.load(open(_M + 'vsat_sets.json'))['dd013'][3]
_C = _j.load(open(_M + 'dg_sets.json'))['dd014_10km'][3]
_D = _j.load(open(_M + 'dg_sets_span20.json'))['span20_pmc10'][3]
def _pmc(la, lo, col, lab, off):
    x, y = m2p(*lonlat2m(la, lo)); r = 11 * k
    dr.rectangle((x - r, y - r, x + r, y + r), fill='white', outline=col, width=int(3 * k))
    dr.text((x + off[0] * k, y + off[1] * k), lab, font=Fs, fill='white', anchor='lm', stroke_width=3, stroke_fill=(0, 0, 0))
    return x, y
_LAB = []
def _set(spots, col, pre, pmcxy):
    for s_ in spots:
        x, y = m2p(*lonlat2m(s_['lat'], s_['lon']))
        if pmcxy: dr.line([pmcxy, (x, y)], fill=col, width=max(2, int(2 * k)))
    for n, s_ in enumerate(spots, 1):
        x, y = m2p(*lonlat2m(s_['lat'], s_['lon'])); r = 8 * k
        dr.ellipse((x - r, y - r, x + r, y + r), fill=col, outline='black', width=2)
        _LAB.append((x, y, '%s%d' % (pre, n), col))
RIDGE, OPT1, OPT2 = (255, 120, 40), (255, 215, 0), (0, 235, 235)
pa = _pmc(*_A['pmc'], RIDGE, 'Ridge PMC', (16, 24))
_set(_A['spots'], RIDGE, 'A', pa)
s5 = m2p(*lonlat2m(-88.6652, -68.42))
_set(_C['spots'], OPT1, 'C', s5)
dr.polygon([(s5[0], s5[1] - 14 * k), (s5[0] - 12 * k, s5[1] + 9 * k), (s5[0] + 12 * k, s5[1] + 9 * k)], fill='white', outline='black')
dr.text((s5[0] - 16 * k, s5[1] + 18 * k), 'Site 5 base', font=Fs, fill='white', anchor='rm', stroke_width=3, stroke_fill=(0, 0, 0))
pd = _pmc(*_D['pmc'], OPT2, 'Option 2 PMC', (16, 0))
_set(_D['spots'], OPT2, 'D', pd)
# group labels for spots within ~1.5 km (37 px at 40 m/px)
groups = []
for x, y, t, c in _LAB:
    for g_ in groups:
        if math.hypot(x - g_[0], y - g_[1]) < 1500 / RES: g_[2].append((t, c)); break
    else: groups.append([x, y, [(t, c)]])
for x, y, items in groups:
    txt = ', '.join(t for t, _ in items); col = items[0][1]
    dr.text((x + 14 * k, y - 14 * k), txt, font=Fs, fill=col, anchor='lb', stroke_width=3, stroke_fill=(0, 0, 0))
lx, ly = int(20 * k), H - int(270 * k)
dr.rectangle((lx - 10 * k, ly - 34 * k, lx + 760 * k, H - 8 * k), fill=(0, 0, 0))
dr.text((lx, ly - 6 * k), 'Landing, hydrogen, ice candidates and VSAT layouts', font=Fs, fill='white', anchor='ld')
rows = [((60, 150, 60), 'Slope ≤8° (landable); steeper ground uncoloured'),
        ((150, 80, 190), 'High hydrogen: LEND neutron dip, top 10% south of 84°S'),
        ((40, 130, 255), 'Ice candidate: shadowed floor with published ice detections'),
        ((150, 210, 255), 'Outline: other permanently shadowed areas (no ice data)'),
        (RIDGE, 'VSAT set A1–A4, Connecting ridge, 3 km runs: 93.0% (3), 93.2% (4) lit'),
        (OPT1, 'VSATs C1–C4, base at site 5: 85.0% lit with 4'),
        (OPT2, 'VSATs D1–D4, PMC across de Gerlache: 89.2% lit with 4'),
        ((255, 255, 255), 'Square: PMC · triangle: site 5 base · VSAT figures are ESTIMATES')]
for i, (c, t) in enumerate(rows):
    yy = ly + i * 30 * k; dr.rectangle((lx, yy, lx + 40 * k, yy + 18 * k), fill=c); dr.text((lx + 50 * k, yy + 9 * k), t, font=Fs, fill='white', anchor='lm')
L = 10000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0))
dr.text((10 * k, 6 * k), 'Focus area. Slope & PSRs: NASA GSFC LOLA (Barker et al. 2023). Hydrogen: NASA LRO LEND (PDS), processed by Open Moon. Ice: Li et al. 2018 (M3), Li et al. 2026 (ShadowCam).', font=Fs, fill='white')
im.thumbnail((2400, 2400), Image.LANCZOS); im.save(OUT, quality=85, optimize=True)
print('landable %.1f%%, high H %.1f%%, ice-candidate PSR %.1f km2' % ((s <= 8).mean() * 100, high.mean() * 100, cand.sum() * RES * RES / 1e6))
