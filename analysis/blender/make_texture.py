"""From the fetched LROC NAC maximum-pixel mosaic (fetch_nac.py, 2 m/px, 20 x 20 km, same bounds as the height map):
- texture_2m.jpg   10000 x 10000 colour texture for Blender (contrast stretched)
- texture_4k.jpg   4096 x 4096 version
- site images: all-sun view and flat-ground (<=8 deg) overlay of the base area.
Usage: make_texture.py NACDIR BLENDER_OUT SITE_ASSETS"""
import sys, os, math, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, lonlat2m, FB
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont
Image.MAX_IMAGE_PIXELS = None
NAC, BO, SA = sys.argv[1:4]
a = np.load(os.path.join(NAC, 'full.npy')).astype('float32'); B = np.load(os.path.join(NAC, 'bounds.npy')); N = a.shape[0]
v = a[a > 0]; lo, hi = np.percentile(v, 0.5), np.percentile(v, 99.7)
g = (np.clip((a - lo) / (hi - lo), 0, 1) ** 0.85 * 255).astype('uint8')
im = Image.fromarray(g)
im.save(os.path.join(BO, 'texture_2m.jpg'), quality=90); im.resize((4096, 4096), Image.LANCZOS).save(os.path.join(BO, 'texture_4k.jpg'), quality=92)
C = lonlat2m(-88.4262, -63.30); HALF = (B[2] - B[0]) / 2; F = lambda z: ImageFont.truetype(FB, int(z))
def markers(img, px_per_m, x0, y1, star=True):
    dr = ImageDraw.Draw(img); k = img.width / 1600
    P = [('B1', (-88.6652, -68.42), (255, 140, 0)), ('B2', (-88.7108, -68.28), (255, 140, 0)), ('B3', (-88.3693, -62.11), (255, 140, 0)),
         ('M1', (-88.4657, -67.872), (0, 220, 255)), ('M2', (-88.3937, -68.686), (0, 220, 255))]
    for n, (la, lo_), col in P:
        x, y = lonlat2m(la, lo_); X = (x - x0) * px_per_m; Y = (y1 - y) * px_per_m
        if 0 <= X < img.width and 0 <= Y < img.height:
            r = 8 * k; dr.ellipse((X - r, Y - r, X + r, Y + r), fill=col, outline='black', width=max(2, int(2 * k)))
            dr.text((X + 12 * k, Y), n, font=F(20 * k), fill=col, anchor='lm', stroke_width=max(2, int(3 * k)), stroke_fill='black')
    X = (C[0] - x0) * px_per_m; Y = (y1 - C[1]) * px_per_m; pts = []
    for i in range(10):
        an = math.pi / 2 + i * math.pi / 5; R_ = (16 if i % 2 == 0 else 7) * k; pts.append((X + R_ * math.cos(an), Y - R_ * math.sin(an)))
    dr.polygon(pts, fill=(255, 60, 200), outline='black'); return dr
def bar(img, px_per_m, metres, label, title):
    dr = ImageDraw.Draw(img); k = img.width / 1600; L = metres * px_per_m
    dr.rectangle((img.width - L - 40 * k, img.height - 56 * k, img.width - 14 * k, img.height - 12 * k), fill='black')
    dr.line([(img.width - L - 28 * k, img.height - 22 * k), (img.width - 28 * k, img.height - 22 * k)], fill='white', width=max(3, int(4 * k)))
    dr.text((img.width - L / 2 - 28 * k, img.height - 40 * k), label, font=F(18 * k), fill='white', anchor='mm')
    dr.rectangle((0, 0, img.width, 34 * k), fill='black'); dr.text((10 * k, 8 * k), title, font=F(17 * k), fill='white')
# site image 1: all-sun view, 20 km
S = 1600; base = Image.fromarray(g).resize((S, S), Image.LANCZOS).convert('RGB'); ppm = S / (2 * HALF)
markers(base, ppm, B[0], B[3]); bar(base, ppm, 2000, '2 km', 'All-sun view, 20 × 20 km around the primary base: LROC NAC maximum-pixel mosaic, 1 m/px (NASA/GSFC/ASU)')
base.save(os.path.join(SA, 'primary-base-allsun.jpg'), quality=88)
# site image 2: flat-ground overlay, 20 km
sl = read('LDSM_83S_10MPP_ADJ', tuple(B), 10); flat = sl <= 8
lab, _ = ndimage.label(flat); patch = lab == lab[sl.shape[0] // 2, sl.shape[1] // 2]
fl = np.array(Image.fromarray((flat * 255).astype('uint8')).resize((S, S), Image.NEAREST)) > 0
pa = np.array(Image.fromarray((patch * 255).astype('uint8')).resize((S, S), Image.NEAREST)) > 0
rgb = np.array(Image.fromarray(g).resize((S, S), Image.LANCZOS).convert('RGB')).astype('float32')
rgb = np.where(fl[..., None], rgb * 0.55 + np.array([40, 200, 90]) * 0.45, rgb)
e = pa & ~ndimage.binary_erosion(pa, iterations=2); rgb[e] = (60, 255, 140)
ov = Image.fromarray(rgb.clip(0, 255).astype('uint8')); markers(ov, ppm, B[0], B[3])
bar(ov, ppm, 2000, '2 km', 'Flat ground ≤8° (green; bright outline = 4.8 km² patch with the base). Slope: NASA LOLA 10 m; image: LROC NAC (NASA/GSFC/ASU)')
ov.save(os.path.join(SA, 'primary-base-allsun-flat.jpg'), quality=88)
print('ok', N, 'lo %.0f hi %.0f' % (lo, hi), 'black %.1f%%' % ((a == 0).mean() * 100))
