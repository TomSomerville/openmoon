"""Raw LOLA slope (LDSM, degrees) for the focus area on a continuous scale, no classes."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, px2m, lonlat2m, FB
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1] if len(sys.argv) > 1 else 'focus-slope-raw.jpg'
font = lambda sz: ImageFont.truetype(FB, int(sz))
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); RES = 40
s = read('LDSM_83S_10MPP_ADJ', B, RES); H, W = s.shape
# viridis stops, 0..45 degrees
stops = np.array([0, 11.25, 22.5, 33.75, 45.]); cols = np.array([[68, 1, 84], [59, 82, 139], [33, 145, 140], [94, 201, 98], [253, 231, 37]], float)
def ramp(v):
    v = np.clip(v, 0, 45); return np.stack([np.interp(v, stops, cols[:, c]) for c in range(3)], -1)
im = Image.fromarray(ramp(np.nan_to_num(s)).astype('uint8')); dr = ImageDraw.Draw(im)
k = max(W, H) / 1400; F = font(24 * k); Fs = font(16 * k)
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
for lat_, lon_, diam, lab, side in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton', 'r'), (-88.5, -87.1, 32.4, 'de Gerlache', 'l'), (-89.51, -84.61, 13.0, 'Spudis', 't')]:
    x, y = m2p(*lonlat2m(lat_, lon_)); rr = diam * 500 / RES
    dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline='white', width=max(2, int(2 * k)))
    if side == 't': dr.text((x, y - rr - 6 * k), lab, font=F, fill='white', anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
    else: dr.text((x + (rr + 8 * k if side == 'r' else -rr - 8 * k), y), lab, font=F, fill='white', anchor='lm' if side == 'r' else 'rm', stroke_width=3, stroke_fill=(0, 0, 0))
lx, ly, lw = int(20 * k), H - int(80 * k), int(450 * k)
dr.rectangle((lx - 10 * k, ly - 34 * k, lx + lw + 20 * k, H - 8 * k), fill=(0, 0, 0))
dr.text((lx, ly - 6 * k), 'Slope, degrees (raw LDSM values)', font=Fs, fill='white', anchor='ld')
g = ramp(np.linspace(0, 45, lw))
for i in range(lw): dr.line([(lx + i, ly), (lx + i, ly + 18 * k)], fill=tuple(int(c) for c in g[i]))
for v in (0, 8, 15, 20, 30, 45):
    xx = lx + lw * v / 45; dr.line([(xx, ly + 18 * k), (xx, ly + 24 * k)], fill='white', width=2); dr.text((xx, ly + 26 * k), f'{v}°' + ('+' if v == 45 else ''), font=Fs, fill='white', anchor='mt')
L = 10000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k)); dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0))
dr.text((10 * k, 6 * k), 'Focus area: raw slope, 40 m/px (averaged from 10 m). Data: NASA GSFC PGDA LOLA LDSM_83S_10MPP_ADJ (Barker et al. 2023, doi:10.3847/PSJ/acf3e1).', font=Fs, fill='white')
im.thumbnail((2400, 2400), Image.LANCZOS); im.save(OUT, quality=85, optimize=True); print('saved', OUT)
