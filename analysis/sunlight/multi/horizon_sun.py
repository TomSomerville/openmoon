"""ESTIMATE: average fraction of time sunlit at given heights above the ground, for candidate points.

Method (Open Moon's own calculation):
- Horizon: for each point, 720 azimuths (0.5 deg); terrain elevation angle along each ray from NASA LOLA LDEM
  (20 m/px within 12 km, 80 m/px to 210 km), with lunar curvature (sphere R = 1737.4 km).
- Sun: direction in the Moon ME frame every 2 hours over 18.6 years (2010-01-01 onward), from NASA/JPL DE421 +
  moon_pa_de421 + moon_080317.tf (via skyfield).
- Sunlit fraction of the solar disc: linear across the disc (radius 0.2666 deg) above the horizon at the Sun's azimuth.
Output: CSV with ground (0.5 m), 5 m and 10 m averages.
"""
import sys, math, numpy as np
R = 1737400.0
far = np.load('dem80.npy'); FB = (-216400., -216400., 216400., 216400.); FR = 80.
near = np.load('dem60.npy'); NB = tuple(np.load('dem60_bounds.npy')); NR = 60.
sun = np.load('sun_me.npy').astype(float)          # 3 x T unit vectors, Moon ME frame
cands = np.load('cands.npy')                        # X, Y, ground % from NASA map

def bilin(dem, b, res, x, y):
    c = (x - b[0]) / res - 0.5; r = (b[3] - y) / res - 0.5
    H, W = dem.shape
    c0 = np.clip(np.floor(c).astype(int), 0, W - 2); r0 = np.clip(np.floor(r).astype(int), 0, H - 2)
    fc = np.clip(c - c0, 0, 1); fr = np.clip(r - r0, 0, 1)
    v = (dem[r0, c0] * (1 - fc) * (1 - fr) + dem[r0, c0 + 1] * fc * (1 - fr) + dem[r0 + 1, c0] * (1 - fc) * fr + dem[r0 + 1, c0 + 1] * fc * fr)
    inside = (c >= 0) & (c <= W - 1) & (r >= 0) & (r <= H - 1)
    return np.where(inside, v, np.nan)

AZ = np.radians(np.arange(0, 360, 0.5))                    # map-plane azimuth from +y, clockwise toward +x
D_near = np.arange(60., 12000., 60.); D_far = np.arange(12000., 210000., 80.)

def horizon(X, Y, hgt):
    z0 = bilin(near, NB, NR, np.array([X]), np.array([Y]))[0] + hgt
    hz = np.full(AZ.size, -90.0)
    for D, dem, b, res in ((D_near, near, NB, NR), (D_far, far, FB, FR)):
        xs = X + np.outer(np.sin(AZ), D); ys = Y + np.outer(np.cos(AZ), D)
        z = bilin(dem, b, res, xs, ys)
        ang = np.degrees(np.arctan2(z - z0 - D ** 2 / (2 * R), D))
        hz = np.maximum(hz, np.nanmax(np.where(np.isnan(ang), -90, ang), axis=1))
    return hz

def sunlit_fraction(X, Y, hz):
    rho = math.hypot(X, Y); lat = -(math.pi / 2 - 2 * math.atan(rho / (2 * R))); lon = math.atan2(X, Y)
    u = np.array([math.cos(lat) * math.cos(lon), math.cos(lat) * math.sin(lon), math.sin(lat)])
    e = np.array([-math.sin(lon), math.cos(lon), 0.0]); n = np.cross(u, e)
    su, se, sn = u @ sun, e @ sun, n @ sun
    elev = np.degrees(np.arcsin(np.clip(su, -1, 1)))
    # map-plane direction of the Sun: north -> (sin lon, cos lon), east -> (cos lon, -sin lon)
    vx = sn * math.sin(lon) + se * math.cos(lon); vy = sn * math.cos(lon) - se * math.sin(lon)
    az = np.degrees(np.arctan2(vx, vy)) % 360
    i = az / 0.5; i0 = np.floor(i).astype(int) % AZ.size; f = i - np.floor(i)
    h = hz[i0] * (1 - f) + hz[(i0 + 1) % AZ.size] * f
    rs = 0.2666
    return float(np.clip((elev - h + rs) / (2 * rs), 0, 1).mean() * 100)

out = ['x_m,y_m,lat,lon_east,nasa_ground_pct,est_0m_pct,est_5m_pct,est_10m_pct']
for k, (X, Y, g) in enumerate(cands):
    res = [sunlit_fraction(X, Y, horizon(X, Y, hgt)) for hgt in (0.5, 5.0, 10.0)]
    rho = math.hypot(X, Y); lat = -(90 - math.degrees(2 * math.atan(rho / (2 * R)))); lon = math.degrees(math.atan2(X, Y))
    out.append('%.0f,%.0f,%.4f,%.3f,%.1f,%.1f,%.1f,%.1f' % (X, Y, lat, lon, g, *res))
    print(k, out[-1], flush=True)
open('sun_at_height_60.csv', 'w').write('\n'.join(out) + '\n')
print('done', flush=True)
