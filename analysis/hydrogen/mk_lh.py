"""Landing (slope <=8 deg) + high-hydrogen map for the Open Moon focus area,
and a pole-wide LEND hydrogen map. Run from this folder after read.py/render.py/hydro.py."""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
from render import read, px2m, lonlat2m, FB
from hydro import supp_grid, THR, ZMIN
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../assets/sites/')

def font(sz): return ImageFont.truetype(FB, int(sz))

def labels(dr, m2p, k, res, show_rim2=True):
    F = font(24 * k)
    for lat_, lon_, diam, lab, side in [(-(89 + 40 / 60), 129 + 47 / 60, 21.0, 'Shackleton', 'r'),
                                         (-88.5, -87.1, 32.4, 'de Gerlache', 'l'),
                                         (-89.51, -84.61, 13.0, 'Spudis', 't')]:
        x, y = m2p(*lonlat2m(lat_, lon_)); rr = diam * 500 / res
        dr.ellipse((x - rr, y - rr, x + rr, y + rr), outline=(0, 230, 255), width=max(2, int(3 * k)))
        if side == 't':
            dr.text((x, y - rr - 6 * k), lab, font=F, fill=(0, 230, 255), anchor='md', stroke_width=3, stroke_fill=(0, 0, 0))
        else:
            dr.text((x + (rr + 8 * k if side == 'r' else -rr - 8 * k), y), lab, font=F, fill=(0, 230, 255),
                    anchor='lm' if side == 'r' else 'rm', stroke_width=3, stroke_fill=(0, 0, 0))
    x, y = m2p(*lonlat2m(-89.427, -113.82))
    dr.text((x, y), 'Shackleton–de Gerlache Ridge', font=font(15 * k), fill='white', anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
    if show_rim2:
        rx0, ry1 = px2m(537, 643); rx1, ry0 = px2m(609, 715); p0 = m2p(rx0, ry1); p1 = m2p(rx1, ry0)
        dr.rectangle((*p0, *p1), outline=(255, 255, 0), width=max(2, int(3 * k)))
        dr.text((p0[0], p0[1] - 6 * k), 'de Gerlache Rim 2', font=F, fill=(255, 255, 0), anchor='ld', stroke_width=3, stroke_fill=(0, 0, 0))

def focus_map():
    fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1); RES = 40
    S, Z = supp_grid(B, 1000.)
    s = read('LDSM_83S_10MPP_ADJ', B, RES); h = read('LDEM_83S_10MPP_ADJ_HILL', B, RES)
    H, W = s.shape
    up = lambda a: np.array(Image.fromarray(a.astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
    high = (up(S) >= THR) & (up(Z) >= ZMIN)
    hv = np.nan_to_num(h); hv = np.clip((hv - np.percentile(hv, 1)) / (np.percentile(hv, 99) - np.percentile(hv, 1)), 0, 1)
    base = np.stack([hv * 255] * 3, -1)
    rgb = np.where((s <= 8)[..., None], base * 0.45 + np.array([0, 170, 0]) * 0.55, base)
    rgb = np.where(high[..., None], rgb * 0.55 + np.array([30, 110, 255]) * 0.45, rgb)
    im = Image.fromarray(rgb.clip(0, 255).astype('uint8')); dr = ImageDraw.Draw(im)
    k = max(W, H) / 1400; Fs = font(16 * k)
    m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
    labels(dr, m2p, k, RES)
    lx, ly = int(20 * k), H - int(95 * k)
    dr.rectangle((lx - 10 * k, ly - 34 * k, lx + 600 * k, H - 8 * k), fill=(0, 0, 0))
    dr.text((lx, ly - 6 * k), 'Landing + hydrogen', font=Fs, fill='white', anchor='ld')
    dr.rectangle((lx, ly, lx + 40 * k, ly + 18 * k), fill=(60, 150, 60)); dr.text((lx + 50 * k, ly + 9 * k), 'Slope ≤8° (landable); steeper ground left uncoloured', font=Fs, fill='white', anchor='lm')
    dr.rectangle((lx, ly + 30 * k, lx + 40 * k, ly + 48 * k), fill=(90, 140, 240)); dr.text((lx + 50 * k, ly + 39 * k), 'High hydrogen: LEND neutron dip in top 10% south of 84°S', font=Fs, fill='white', anchor='lm')
    L = 10000 / RES; sx = W - L - 30 * k; sy = H - 30 * k
    dr.rectangle((sx - 10 * k, sy - 34 * k, sx + L + 10 * k, H - 8 * k), fill=(0, 0, 0)); dr.line([(sx, sy), (sx + L, sy)], fill='white', width=int(4 * k))
    dr.text((sx + L / 2, sy - 6 * k), '10 km', font=Fs, fill='white', anchor='md')
    dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0))
    dr.text((10 * k, 6 * k), 'Open Moon focus area: landable ground and high hydrogen. Slope: NASA GSFC LOLA (Barker et al. 2023). Hydrogen: NASA LRO LEND (PDS), processed by Open Moon.', font=Fs, fill='white')
    im.thumbnail((2400, 2400), Image.LANCZOS); im.save(OUT + 'focus-landing-hydrogen.jpg', quality=85, optimize=True)
    return float(high.mean() * 100), float(((s <= 8) & high).mean() * 100)

def pole_map():
    R0 = 180000.; B = (-R0, -R0, R0, R0); STEP = 1500.
    S, Z = supp_grid(B, STEP)
    h = read('LDEM_83S_10MPP_ADJ_HILL', B, 80)
    H, W = h.shape
    up = lambda a: np.array(Image.fromarray(a.astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
    Su, Zu = up(S), up(Z)
    hv = np.nan_to_num(h); hv = np.clip((hv - np.percentile(hv, 1)) / (np.percentile(hv, 99) - np.percentile(hv, 1)), 0, 1)
    base = np.stack([hv * 255] * 3, -1)
    hi = (Su >= THR) & (Zu >= ZMIN)
    mod = (Su >= 0.98) & (Zu >= ZMIN) & ~hi            # 0.98 % = top 25 % south of 84 S
    blue = np.array([20, 90, 255])
    a = np.where(hi, 0.7, np.where(mod, 0.25, 0.0))
    rgb = base * (1 - a[..., None]) + blue * a[..., None]
    im = Image.fromarray(rgb.clip(0, 255).astype('uint8')); dr = ImageDraw.Draw(im)
    k = max(W, H) / 1400; F = font(22 * k); Fs = font(16 * k)
    m2p = lambda x, y: ((x - B[0]) / 80, (B[3] - y) / 80)
    # outline of high-hydrogen areas
    edge = (hi ^ np.roll(hi, 1, 0)) | (hi ^ np.roll(hi, 1, 1))
    ys, xs = np.nonzero(edge)
    for x, y in zip(xs, ys): dr.ellipse((x - 2 * k, y - 2 * k, x + 2 * k, y + 2 * k), fill=(255, 255, 255))
    fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989)
    dr.rectangle((*m2p(fx0, fy1), *m2p(fx1, fy0)), outline=(230, 30, 30), width=int(4 * k))
    p = m2p(fx0, fy1); dr.text((p[0], p[1] - 6 * k), 'Open Moon focus area', font=F, fill=(255, 80, 80), anchor='ld', stroke_width=3, stroke_fill=(0, 0, 0))
    for lat_ in (-85, -88):  # latitude rings
        import math
        rho = 2 * 1737400 * math.tan(math.radians(90 + lat_) / 2) / 80; c = m2p(0, 0)
        dr.ellipse((c[0] - rho, c[1] - rho, c[0] + rho, c[1] + rho), outline=(200, 200, 200), width=1)
        dr.text((c[0] + 4 * k, c[1] - rho - 2 * k), f'{-lat_}°S', font=Fs, fill=(220, 220, 220), anchor='ld', stroke_width=2, stroke_fill=(0, 0, 0))
    for lon_, lab in ((0, '0°'), (90, '90°E'), (180, '180°'), (-90, '90°W')):
        x, y = m2p(*lonlat2m(-84.6, lon_)); dr.text((x, y), lab, font=Fs, fill='white', anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0))
    lx, ly = int(20 * k), H - int(95 * k)
    dr.rectangle((lx - 10 * k, ly - 34 * k, lx + 640 * k, H - 8 * k), fill=(0, 0, 0))
    dr.text((lx, ly - 6 * k), 'LEND neutron dip (hydrogen in top ~1 m)', font=Fs, fill='white', anchor='ld')
    c1 = tuple(int(v) for v in base.mean() * 0.3 + blue * 0.7); c2 = tuple(int(v) for v in base.mean() * 0.75 + blue * 0.25)
    dr.rectangle((lx, ly, lx + 40 * k, ly + 18 * k), fill=c1, outline='white', width=2); dr.text((lx + 50 * k, ly + 9 * k), 'High: dip ≥1.28 % (top 10 % south of 84°S)', font=Fs, fill='white', anchor='lm')
    dr.rectangle((lx, ly + 30 * k, lx + 40 * k, ly + 48 * k), fill=c2); dr.text((lx + 50 * k, ly + 39 * k), 'Moderate: dip 0.98–1.28 % (top 25 %)', font=Fs, fill='white', anchor='lm')
    dr.rectangle((0, 0, W, int(30 * k)), fill=(0, 0, 0))
    dr.text((10 * k, 6 * k), 'South pole to 84°S: hydrogen from NASA LRO LEND collimated epithermal neutrons, 2009–2016 (PDS), processed by Open Moon. Base: NASA LOLA hillshade.', font=Fs, fill='white')
    im.thumbnail((2000, 2000), Image.LANCZOS); im.save(OUT + 'south-pole-lend-hydrogen.jpg', quality=85, optimize=True)

if __name__ == '__main__':
    import sys as _s
    if 'pole' not in _s.argv: print('focus high-H share %, landable AND high-H share %:', focus_map())
    pole_map(); print('done')
