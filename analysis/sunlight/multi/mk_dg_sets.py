"""Map: de Gerlache rim VSAT layouts (ESTIMATE). Option 1: base/PMC at site 5, VSATs within 10 km.
Option 2: PMC between site 5 and the east rim, VSATs within 10 km of it (up to 20 km apart). DD-014."""
import sys, json, math, numpy as np
sys.path.insert(0, '../slope')
from render import read, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
o1 = json.load(open('dg_sets.json'))['dd014_10km'][3]; o2 = json.load(open('dg_sets_span20.json'))['span20_pmc10'][3]
cx, cy = lonlat2m(-88.75, -82.0); H0 = 30000
B = (cx - H0 * 1.25, cy - H0, cx + H0 * 1.25, cy + H0); RES = 40
h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', B, RES)); H, W = h.shape
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
im = Image.fromarray((np.stack([hv * 255] * 3, -1)).astype('uint8')); dr = ImageDraw.Draw(im)
k = W / 1400; font = lambda sz: ImageFont.truetype(FB, int(sz * k))
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES); g = lambda la, lo: m2p(*lonlat2m(la, lo))
x, y = g(-88.5, -87.1); rr = 16200 / RES
dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 230, 255), width=int(3 * k)); dr.text((x, y), 'de Gerlache', font=font(26), fill=(0, 230, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
# option 1
sx, sy = g(-88.6652, -68.42); r10 = 10000 / RES
dr.ellipse((sx - r10, sy - r10, sx + r10, sy + r10), outline=(255, 170, 0), width=int(3 * k))
for n, s in enumerate(o1['spots'], 1):
    x, y = g(s['lat'], s['lon']); r = 10 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(255, 170, 0), outline='black', width=2)
    ox, oy, an = {1: (-14, -10, 'rb'), 2: (14, -12, 'lb'), 3: (14, -12, 'lb'), 4: (14, -12, 'lb')}[n]
    dr.text((x + ox * k, y + oy * k), 'C%d' % n, font=font(20), fill=(255, 200, 80), anchor=an, stroke_width=3, stroke_fill=(0, 0, 0))
dr.polygon([(sx, sy - 16 * k), (sx - 14 * k, sy + 10 * k), (sx + 14 * k, sy + 10 * k)], fill='white', outline='black')
dr.text((sx + 40 * k, sy + 30 * k), 'Site 5 (base, option 1)', font=font(18), fill='white', anchor='lt', stroke_width=3, stroke_fill=(0, 0, 0))
# option 2
px, py = g(*o2['pmc'])
dr.ellipse((px - r10, py - r10, px + r10, py + r10), outline=(80, 200, 255), width=int(3 * k))
for n, s in enumerate(o2['spots'], 1):
    x, y = g(s['lat'], s['lon']); r = 10 * k
    dr.ellipse((x - r, y - r, x + r, y + r), fill=(60, 140, 255), outline='white', width=2)
    ox, oy, an = {1: (-14, -14, 'rb'), 2: (14, 10, 'lt'), 3: (14, -4, 'lm'), 4: (-14, 14, 'rt')}[n]
    dr.text((x + ox * k, y + oy * k), 'D%d' % n, font=font(20), fill=(150, 200, 255), anchor=an, stroke_width=3, stroke_fill=(0, 0, 0))
dr.rectangle((px - 10 * k, py - 10 * k, px + 10 * k, py + 10 * k), fill='white', outline='black', width=2)
dr.text((px + 14 * k, py), 'PMC (option 2)', font=font(18), fill='white', anchor='lm', stroke_width=3, stroke_fill=(0, 0, 0))
Fs = font(16); lx, ly = int(20 * k), int(50 * k)
dr.rectangle((lx - 10 * k, ly - 10 * k, lx + 720 * k, ly + 120 * k), fill=(0, 0, 0))
dr.text((lx, ly + 10 * k), 'VSAT layouts on the de Gerlache rim (ESTIMATE, ground-level sunlight; DD-014: ≤10 km of cable)', font=Fs, fill='white', anchor='lm')
dr.ellipse((lx + 8 * k, ly + 32 * k, lx + 26 * k, ly + 50 * k), fill=(255, 170, 0)); dr.text((lx + 40 * k, ly + 41 * k), 'Option 1, C1–C4: base at site 5, VSATs within 10 km: 85.0% lit', font=Fs, fill='white', anchor='lm')
dr.ellipse((lx + 8 * k, ly + 62 * k, lx + 26 * k, ly + 80 * k), fill=(60, 140, 255)); dr.text((lx + 40 * k, ly + 71 * k), 'Option 2, D1–D4: PMC between site 5 and the east rim: 89.2% lit', font=Fs, fill='white', anchor='lm')
dr.text((lx + 40 * k, ly + 101 * k), 'Circles: 10 km reach around each PMC', font=Fs, fill=(200, 200, 200), anchor='lm')
L = 10000 / RES; sx2 = W - L - 30 * k; sy2 = H - 30 * k
dr.rectangle((sx2 - 10 * k, sy2 - 34 * k, sx2 + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx2, sy2), (sx2 + L, sy2)], fill='white', width=int(4 * k)); dr.text((sx2 + L / 2, sy2 - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0)); dr.text((10 * k, 6 * k), 'de Gerlache crater: best VSAT sets. ESTIMATE: Open Moon horizon calculation over NASA LOLA terrain, NASA/JPL DE421 Sun positions, 18.6 years.', font=Fs, fill='white')
im.thumbnail((2400, 2400), Image.LANCZOS); im.save(sys.argv[1], quality=85, optimize=True); print('saved', im.size)
