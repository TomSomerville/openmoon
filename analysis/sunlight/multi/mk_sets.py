"""Map of best multi-VSAT sets (ESTIMATE): DD-013 set (within 3 km of one PMC) and unconstrained set."""
import sys, json, math, numpy as np
sys.path.insert(0, '../slope')
from render import read, px2m, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
rep = json.load(open('vsat_sets.json')); OUT = sys.argv[1]
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); RES = 40
h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, RES)); H, W = h.shape
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
im = Image.fromarray((np.stack([hv * 255] * 3, -1)).astype('uint8')); dr = ImageDraw.Draw(im)
k = W / 1400; font = lambda sz: ImageFont.truetype(FB, int(sz * k))
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
for la, lo, dia, lab, side in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton', 'r'), (-88.5, -87.1, 32.4, 'de Gerlache', 'l'), (-89.51, -84.61, 13.0, 'Spudis', 't')]:
    x, y = m2p(*lonlat2m(la, lo)); rr = dia * 500 / RES
    dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 230, 255), width=int(3 * k))
    t = (x, y - rr - 6 * k) if side == 't' else ((x + rr + 8 * k, y) if side == 'r' else (x - rr - 8 * k, y))
    dr.text(t, lab, font=font(24), fill=(0, 230, 255), anchor='md' if side == 't' else ('lm' if side == 'r' else 'rm'), stroke_width=3, stroke_fill=(0, 0, 0))
# DD-013 set: PMC + 3 km circle + 4 spots (green)
s4 = rep['dd013'][3]; px, py = m2p(*lonlat2m(*s4['pmc'])); r3 = 3000 / RES
dr.ellipse((px - r3, py - r3, px + r3, py + r3), outline=(80, 255, 80), width=int(3 * k))
dr.rectangle((px - 9 * k, py - 9 * k, px + 9 * k, py + 9 * k), fill=(255, 255, 255), outline=(0, 0, 0), width=2)
for n, s in enumerate(s4['spots'], 1):
    x, y = m2p(*lonlat2m(s['lat'], s['lon'])); r = 9 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(60, 220, 60), outline=(0, 0, 0), width=2)
# unconstrained set (blue)
for n, s in enumerate(rep['any'][3]['spots'], 1):
    x, y = m2p(*lonlat2m(s['lat'], s['lon'])); r = 10 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(40, 120, 255), outline='white', width=2)
    dr.text((x + 13 * k, y - 13 * k), 'B%d' % n, font=font(20), fill=(140, 190, 255), anchor='lb', stroke_width=3, stroke_fill=(0, 0, 0))
pts = [m2p(*lonlat2m(s['lat'], s['lon'])) for s in rep['any'][3]['spots']]
for i in range(len(pts)):
    for j in range(i + 1, len(pts)): dr.line([pts[i], pts[j]], fill=(40, 120, 255), width=max(1, int(1.5 * k)))
base_im = Image.fromarray((np.stack([hv * 255] * 3, -1)).astype('uint8'))
# inset: 8 x 8 km around the PMC, enlarged
half = 4000 / RES; Z = 5
ins = base_im.crop((int(px - half), int(py - half), int(px + half), int(py + half))).resize((int(2 * half * Z), int(2 * half * Z)), Image.LANCZOS)
di = ImageDraw.Draw(ins); c0 = (px - half, py - half); q = lambda x, y: ((x - c0[0]) * Z, (y - c0[1]) * Z)
cx, cy = q(px, py); rr = r3 * Z
di.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=(80, 255, 80), width=int(4 * k))
di.rectangle((cx - 12 * k, cy - 12 * k, cx + 12 * k, cy + 12 * k), fill='white', outline='black', width=2)
di.text((cx + 16 * k, cy + 4 * k), 'PMC', font=font(22), fill='white', anchor='lt', stroke_width=3, stroke_fill=(0, 0, 0))
for n, s_ in enumerate(s4['spots'], 1):
    x, y = q(*m2p(*lonlat2m(s_['lat'], s_['lon']))); r = 13 * k
    di.ellipse((x - r, y - r, x + r, y + r), fill=(60, 220, 60), outline='black', width=2)
    di.text((x + 16 * k, y - 16 * k), 'A%d' % n, font=font(24), fill=(170, 255, 170), anchor='lb', stroke_width=3, stroke_fill=(0, 0, 0))
L1 = 1000 / RES * Z; di.line([(20 * k, ins.height - 25 * k), (20 * k + L1, ins.height - 25 * k)], fill='white', width=int(4 * k))
di.text((20 * k + L1 / 2, ins.height - 30 * k), '1 km', font=font(18), fill='white', anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
di.rectangle((0, 0, ins.width - 1, ins.height - 1), outline=(80, 255, 80), width=int(4 * k))
di.rectangle((0, 0, ins.width, 34 * k), fill=(0, 0, 0)); di.text((10 * k, 8 * k), 'Set A, 3 km around the PMC', font=font(18), fill='white')
ix, iy = int(20 * k), H - ins.height - int(20 * k)
im.paste(ins, (ix, iy)); dr = ImageDraw.Draw(im)
dr.line([(px - r3, py + r3), (ix + ins.width, iy)], fill=(80, 255, 80), width=int(2 * k))
Fs = font(16); lx, ly = W - int(760 * k), int(50 * k)
dr.rectangle((lx - 10 * k, ly - 10 * k, lx + 740 * k, ly + 140 * k), fill=(0, 0, 0))
dr.text((lx, ly + 10 * k), 'Multiple VSAT placements (ESTIMATE, ground-level sunlight)', font=Fs, fill='white', anchor='lm')
dr.ellipse((lx + 8 * k, ly + 32 * k, lx + 26 * k, ly + 50 * k), fill=(60, 220, 60)); dr.text((lx + 40 * k, ly + 41 * k), 'A1–A4: best set within 3 km of one PMC (DD-013): 93.2% lit', font=Fs, fill='white', anchor='lm')
dr.ellipse((lx + 8 * k, ly + 62 * k, lx + 26 * k, ly + 80 * k), fill=(40, 120, 255)); dr.text((lx + 40 * k, ly + 71 * k), 'B1–B4: best set with no distance limit: 99.3% lit', font=Fs, fill='white', anchor='lm')
dr.rectangle((lx + 8 * k, ly + 92 * k, lx + 26 * k, ly + 110 * k), fill='white'); dr.text((lx + 40 * k, ly + 101 * k), 'PMC (power management centre) with 3 km radius', font=Fs, fill='white', anchor='lm')
L = 10000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0)); dr.text((10 * k, 6 * k), 'Focus area: best VSAT sets by combined sunlight. ESTIMATE: Open Moon horizon calculation over NASA LOLA terrain and NASA/JPL DE421 Sun positions, 18.6 years.', font=Fs, fill='white')
im.thumbnail((2400, 2400), Image.LANCZOS); im.save(OUT, quality=85, optimize=True); print('saved')
