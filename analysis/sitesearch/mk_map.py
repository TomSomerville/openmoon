"""Map of the ranked base sites (site search). Usage: mk_map.py ground.npz sitesearch.json OUT.jpg"""
import sys, os, json, math, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB, cmap_classes
from PIL import Image, ImageDraw, ImageFont
G = np.load(sys.argv[1]); J = json.load(open(sys.argv[2])); B = G['B']; RES = float(G['res'])
s = G['s']; ice = G['ice']; H, W = s.shape
h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', tuple(B), 40)); h = h[:H, :W]
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
rgb = np.stack([hv * 255] * 3, -1) * 0.5 + cmap_classes(s) * 0.5
rgb = np.where(ice[..., None], rgb * 0.3 + np.array([20, 120, 255]) * 0.7, rgb)
im = Image.fromarray(rgb.clip(0, 255).astype('uint8')); im.thumbnail((2200, 2200), Image.LANCZOS); k = im.width / W
dr = ImageDraw.Draw(im); F = lambda z: ImageFont.truetype(FB, int(z))
m2p = lambda x, y: ((x - B[0]) / RES * k, (B[3] - y) / RES * k)
def txt(x, y, t, c, a='lm', z=22): dr.text((x, y), t, font=F(z), fill=c, anchor=a, stroke_width=4, stroke_fill='black')
for n, r in enumerate(J['sites'][:8], 1):
    bx, by = m2p(r['x'], r['y'])
    for tx, ty in zip(r['tx'], r['ty']):
        x, y = m2p(tx, ty); dr.line([(bx, by), (x, y)], fill=(255, 140, 0), width=3); dr.ellipse((x - 6, y - 6, x + 6, y + 6), fill=(255, 140, 0), outline='black', width=2)
    dr.ellipse((bx - 15, by - 15, bx + 15, by + 15), fill='white', outline='black', width=3); dr.text((bx, by), str(n), font=F(20), fill='black', anchor='mm')
for name, (la, lo), col in (('Current primary', (-88.4453, -63.44), (255, 60, 200)), ('Current backup', (-89.559, -163.66), (170, 90, 255))):
    x, y = m2p(*lonlat2m(la, lo)); pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5; R_ = 18 if i % 2 == 0 else 8; pts.append((x + R_ * math.cos(a), y - R_ * math.sin(a)))
    dr.polygon(pts, fill=col, outline='black')
rows = [((0, 170, 0), 'Slope ≤8°'), ((255, 220, 0), '8–15°'), ((255, 140, 0), '15–20°'), ((220, 0, 0), '≥20°'), ((40, 130, 255), 'Ice-candidate floors'),
        ((255, 255, 255), 'Ranked site (1 = best), with its tower pair (orange)'), ((255, 60, 200), 'Current primary (star)'), ((170, 90, 255), 'Current backup (star)')]
lx, ly = 16, 50; dr.rectangle((6, 40, 560, 50 + len(rows) * 30 + 10), fill='black')
for c, t in rows: dr.rectangle((lx, ly + 4, lx + 30, ly + 20), fill=c); dr.text((lx + 40, ly + 12), t, font=F(18), fill='white', anchor='lm'); ly += 30
dr.rectangle((0, 0, im.width, 34), fill='black')
dr.text((8, 8), 'Site search (ESTIMATE): towers ≤10 km, shared darkness ≤7 days. Slope & ice floors: NASA GSFC LOLA; sunlight: Open Moon model over LOLA.', font=F(17), fill='white')
im.save(sys.argv[3], quality=88); print(im.size)
