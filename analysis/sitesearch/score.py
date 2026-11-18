"""Rank base sites over the focus area (plan design weights, ESTIMATE power figures).
For every candidate base point on ground <=8 deg: the VSAT pair within 10 km whose longest shared darkness is
<= 7 days with the shortest longest cable run; distance to ice-candidate floors; flat ground; LEND hydrogen.
Usage: score.py ground.npz pairs.npz out.json"""
import sys, json, math, numpy as np
G = np.load(sys.argv[1]); Q = np.load(sys.argv[2])
B, RES = G['B'], float(G['res']); s, frac, fdisc, dice, hyd = G['s'], G['frac'], G['fdisc'], G['dice'], G['hyd']
P, single, I, J, lit, ld = Q['P'], Q['single'], Q['I'], Q['J'], Q['lit'], Q['ld']
R = 1737400.
def ll(x, y):
    rho = math.hypot(x, y); return -(90 - math.degrees(2 * math.atan(rho / (2 * R)))), math.degrees(math.atan2(x, y))
MAXRUN, MAXDARK = 10000., 7.0
ok = ld <= MAXDARK; I7, J7, lit7, ld7 = I[ok], J[ok], lit[ok], ld[ok]
print('pairs', len(I), 'pairs <= 7 d', ok.sum())
step = 10   # 400 m grid
rr, cc = np.mgrid[0:s.shape[0]:step, 0:s.shape[1]:step]; rr, cc = rr.ravel(), cc.ravel()
cand = (s[rr, cc] <= 8) & (fdisc[rr, cc] >= 150) & (dice[rr, cc] <= 25000) & (dice[rr, cc] >= 300)   # not on the shadowed ice floor itself
rr, cc = rr[cand], cc[cand]
X = B[0] + (cc + 0.5) * RES; Y = B[3] - (rr + 0.5) * RES
print('base points', len(X))
def power(Xb, Yb):
    """best feasible pair (<=7 d, both <=10 km) minimising the longest run; returns run, lit, dark, i, j"""
    out = []
    for k0 in range(0, len(Xb), 300):
        d = np.hypot(Xb[k0:k0 + 300, None] - P[None, :, 0], Yb[k0:k0 + 300, None] - P[None, :, 1])
        run = np.maximum(d[:, I7], d[:, J7]); run[run > MAXRUN] = np.inf
        key = run - lit7[None, :] * 1e-3            # shortest run, then more sunlight
        b = key.argmin(1); rb = run[np.arange(len(b)), b]
        for q, (bi, rv) in enumerate(zip(b, rb)):
            out.append((rv, lit7[bi], ld7[bi], I7[bi], J7[bi]) if np.isfinite(rv) else (np.inf, 0, 99, -1, -1))
    return out
pw = power(X, Y)
run = np.array([p[0] for p in pw]); feas = np.isfinite(run)
print('feasible base points (a pair <= 7 d within 10 km):', feas.sum())
ice_km = dice[rr, cc] / 1000; fl = frac[rr, cc]; fd = fdisc[rr, cc]; hy = hyd[rr, cc]
# plan-design score: cable 0.3, ice 0.3, flat 0.3, hydrogen 0.1
sc = (0.3 * (1 - np.where(feas, run, MAXRUN) / MAXRUN) + 0.3 * (1 - np.minimum(ice_km, 25) / 25)
      + 0.3 * (0.5 * fl + 0.5 * np.minimum(fd, 500) / 500) + 0.1 * np.clip((hy - 0.5) / 0.6, 0, 1))
sc[~feas] = -1
# pick distinct sites: best first, suppress others within 5 km
order = np.argsort(-sc); picked = []
for k in order:
    if sc[k] < 0 or len(picked) >= 12: break
    if all(math.hypot(X[k] - X[p], Y[k] - Y[p]) > 5000 for p in picked): picked.append(k)
def row(k, label=None):
    r_, li, dk, i, j = pw[k] if isinstance(k, (int, np.integer)) else k
    return None
res = []
for k in picked:
    rv, li, dk, i, j = pw[k]
    la, lo = ll(X[k], Y[k])
    d_ = np.hypot(P[:, 0] - X[k], P[:, 1] - Y[k]); v_ = ok & (d_[I] <= MAXRUN) & (d_[J] <= MAXRUN); kb = np.where(v_)[0][lit[v_].argmax()]
    bestlit = {'lit_pct': round(float(lit[kb]) * 100, 1), 'longest_dark_d': round(float(ld[kb]), 1), 'longest_run_km': round(float(max(d_[I[kb]], d_[J[kb]])) / 1000, 1),
               'towers': [[round(v, 4) for v in ll(*P[I[kb]])], [round(v, 4) for v in ll(*P[J[kb]])]], 'tx': [float(P[I[kb]][0]), float(P[J[kb]][0])], 'ty': [float(P[I[kb]][1]), float(P[J[kb]][1])]}
    res.append({'best_lit_option': bestlit, 'lat': round(la, 4), 'lon': round(lo, 2), 'score': round(float(sc[k]), 3), 'longest_run_km': round(rv / 1000, 1),
                'lit_pct': round(li * 100, 1), 'longest_dark_d': round(float(dk), 1), 'ice_km': round(float(ice_km[k]), 1),
                'flat_1km_pct': round(float(fl[k]) * 100), 'flat_disc_m': int(fd[k] * 2), 'lend_dip_pct': round(float(hy[k]), 2),
                'towers': [[round(v, 4) for v in ll(*P[i])] + [round(float(single[i]) * 100, 1)], [round(v, 4) for v in ll(*P[j])] + [round(float(single[j]) * 100, 1)]],
                'x': float(X[k]), 'y': float(Y[k]), 'tx': [float(P[i][0]), float(P[j][0])], 'ty': [float(P[i][1]), float(P[j][1])]})
# reference points evaluated the same way
import importlib.util
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '../slope'))
from render import lonlat2m
refs = {}
for name, (la, lo) in {'Current primary': (-88.4453, -63.44), 'Current backup': (-89.559, -163.66), 'Black circle': (-88.1677, -72.72), 'Purple circle': (-88.6883, -68.30)}.items():
    x, y = lonlat2m(la, lo); c = int((x - B[0]) / RES); r = int((B[3] - y) / RES)
    rv, li, dk, i, j = power(np.array([x]), np.array([y]))[0]
    # best pair regardless of the 7-day rule, for comparison
    d = np.hypot(P[:, 0] - x, P[:, 1] - y); v = (d[I] <= MAXRUN) & (d[J] <= MAXRUN)
    kbest = np.where(v)[0][np.lexsort((-lit[v], ld[v]))[0]] if v.any() else None
    refs[name] = {'longest_run_km': None if not np.isfinite(rv) else round(rv / 1000, 1), 'lit_pct': round(li * 100, 1), 'longest_dark_d': round(float(dk), 1),
                  'min_dark_any_pair_d': None if kbest is None else round(float(ld[kbest]), 1),
                  'ice_km': round(float(dice[r, c]) / 1000, 1), 'flat_1km_pct': round(float(frac[r, c]) * 100), 'flat_disc_m': int(fdisc[r, c] * 2),
                  'lend_dip_pct': round(float(hyd[r, c]), 2), 'slope': round(float(s[r, c]), 1)}
json.dump({'sites': res, 'refs': refs}, open(sys.argv[3], 'w'), indent=1)
for r_ in res: print({k: v for k, v in r_.items() if k not in ('towers', 'x', 'y', 'tx', 'ty', 'best_lit_option')}, '| best-lit:', {k: v for k, v in r_['best_lit_option'].items() if k in ('lit_pct','longest_dark_d','longest_run_km')})
for k, v in refs.items(): print(k, v)
