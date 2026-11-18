"""Ground layer for the site search (Open Moon processing of NASA data):
slope (LOLA LDSM, 40 m), share of ground <=8 deg within 1 km, radius of the largest all-<=8 deg circle,
distance to the ice-candidate floors (Shackleton, de Gerlache; NASA GSFC LPSR), LEND neutron dip.
Usage (run in analysis data folder with cache): ground.py psr_focus.pkl -> ground.npz"""
import sys, os, math, pickle, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../slope'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../hydrogen'))
from render import read, px2m, lonlat2m
from hydro import supp_grid
from scipy import ndimage, signal
from PIL import Image, ImageDraw
RES = 40
fx0, fy1 = px2m(292, 518); fx1, fy0 = px2m(953, 989); B = (fx0, fy0, fx1, fy1)
s = np.nan_to_num(read('LDSM_83S_10MPP_ADJ', B, RES), nan=90.); H, W = s.shape
flat = s <= 8
r = int(1000 / RES); yy, xx = np.mgrid[-r:r + 1, -r:r + 1]; disc = (xx ** 2 + yy ** 2 <= r * r).astype(float)
frac = signal.fftconvolve(flat.astype(float), disc, mode='same') / disc.sum()
fdisc = ndimage.distance_transform_edt(flat) * RES
m2p = lambda x, y: ((x - B[0]) / RES, (B[3] - y) / RES)
P = pickle.load(open(sys.argv[1], 'rb'))
CANDS = [(lonlat2m(-89.67, 129.78), 10.5e3), (lonlat2m(-88.5, -87.1), 16.2e3)]
ice = Image.new('L', (W, H), 0); di = ImageDraw.Draw(ice)
for gid, area, name, b, rings in P:
    cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    if not (area > 1 and any(math.hypot(cx - p[0], cy - p[1]) < rad for p, rad in CANDS)): continue
    for ring in rings:
        sa = 0.5 * (ring[:-1, 0] * ring[1:, 1] - ring[1:, 0] * ring[:-1, 1]).sum()
        di.polygon([m2p(x, y) for x, y in ring], fill=255 if sa < 0 else 0)
ice = np.array(ice) > 0
dice = ndimage.distance_transform_edt(~ice) * RES
Sg, Zg = supp_grid(B, 1000.)
hyd = np.array(Image.fromarray(Sg.astype('float32'), mode='F').resize((W, H), Image.BILINEAR))
np.savez('ground.npz', B=np.array(B), res=RES, s=s.astype('float32'), frac=frac.astype('float32'), fdisc=fdisc.astype('float32'),
         dice=dice.astype('float32'), ice=ice, hyd=hyd.astype('float32'))
print('grid', W, H, 'flat %.1f%%' % (flat.mean() * 100), 'ice px', ice.sum())
