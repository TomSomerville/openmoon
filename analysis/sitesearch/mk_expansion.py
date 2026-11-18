"""Room to grow at the primary base (DD-020): ground <=8 deg (NASA LOLA LDSM, 10 m/px) within 5 km, the connected
flat patch holding the base, and ground reachable over <=15 deg. Usage: mk_expansion.py OUT.jpg"""
import sys, os, math, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont
N = lonlat2m(-88.4365, -62.46); B3 = lonlat2m(-88.3693, -62.11); W = 6000; RES = 10
bb = (N[0] - W, N[1] - W, N[0] + W, N[1] + W)
s = read('LDSM_83S_10MPP_ADJ', bb, RES); h = np.nan_to_num(read('LDEM_83S_10MPP_ADJ_HILL', bb, RES)); H, Wd = s.shape
c = (H // 2, Wd // 2); yy, xx = np.mgrid[0:H, 0:Wd]; d = np.hypot(yy - c[0], xx - c[1]) * RES
flat = s <= 8; lab, _ = ndimage.label(flat); patch = lab == lab[c]
km2 = lambda m: m.sum() * RES * RES / 1e6
lab15, _ = ndimage.label(s <= 15); drive = lab15 == lab15[c]
sizes = np.bincount(lab.ravel()); big = np.isin(lab, np.where(sizes * RES * RES / 1e6 >= 0.05)[0][1:])
stats = {'patch': km2(patch)}
for r in (2000, 3000, 5000):
    m = d <= r; stats[r] = (km2(flat & m), km2(flat & big & drive & m))
hv = np.clip((h - np.percentile(h, 1)) / (np.percentile(h, 99) - np.percentile(h, 1)), 0, 1)
rgb = np.stack([hv * 255] * 3, -1) * 0.75
rgb = np.where((flat & (d <= 5000))[..., None], rgb * 0.45 + np.array([60, 200, 90]) * 0.55, rgb)
rgb = np.where(patch[..., None], rgb * 0.3 + np.array([0, 230, 120]) * 0.7, rgb)
im = Image.fromarray(rgb.clip(0, 255).astype('uint8')).resize((1600, 1600), Image.LANCZOS); k = 1600 / Wd
dr = ImageDraw.Draw(im); F = lambda z: ImageFont.truetype(FB, int(z))
cx, cy = c[1] * k, c[0] * k
for r in (2000, 3000, 5000):
    rr = r / RES * k; dr.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline='white', width=3)
    dr.text((cx + rr * 0.71 + 6, cy - rr * 0.71), '%d km' % (r // 1000), font=F(26), fill='white', stroke_width=4, stroke_fill='black')
pts = []
for i in range(10):
    a = math.pi / 2 + i * math.pi / 5; R_ = 22 if i % 2 == 0 else 10; pts.append((cx + R_ * math.cos(a), cy - R_ * math.sin(a)))
dr.polygon(pts, fill=(255, 60, 200), outline='black')
bx, by = (B3[0] - bb[0]) / RES * k, (bb[3] - B3[1]) / RES * k
dr.ellipse((bx - 11, by - 11, bx + 11, by + 11), fill=(255, 140, 0), outline='black', width=3)
dr.text((bx + 16, by), 'B3', font=F(24), fill=(255, 190, 90), anchor='lm', stroke_width=4, stroke_fill='black')
rows = [((0, 230, 120), 'Connected flat patch with the base: %.1f km²' % stats['patch']), ((90, 180, 110), 'Other ground ≤8° within 5 km'),
        ((255, 60, 200), 'Primary base (DD-020)'), ((255, 140, 0), 'VSAT B3 (DD-021)')]
dr.rectangle((0, 0, 1600, 40), fill='black')
dr.text((10, 10), 'Room to grow at the primary base. Slope: NASA GSFC LOLA LDSM, 10 m/px (Barker et al. 2023); Open Moon measurement.', font=F(20), fill='white')
y = 56; dr.rectangle((10, 46, 640, 56 + len(rows) * 34 + 8), fill='black')
for col, t in rows: dr.rectangle((22, y + 6, 54, y + 26), fill=col); dr.text((66, y + 16), t, font=F(22), fill='white', anchor='lm'); y += 34
L = 1000 / RES * k; dr.rectangle((1600 - L - 40, 1540, 1580, 1590), fill='black'); dr.line([(1600 - L - 30, 1575), (1570, 1575)], fill='white', width=4); dr.text((1600 - L / 2 - 30, 1560), '1 km', font=F(20), fill='white', anchor='mm')
im.save(sys.argv[1], quality=88)
print(stats)
