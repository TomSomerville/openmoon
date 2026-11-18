"""ESTIMATE: de Gerlache rim near site 5. Best pair by exhaustive search, then best 3rd and 4th spot added.
(a) DD-013: all spots fit in a 3 km circle (the PMC at its centre); spots within 8 km of site 5.
(b) whole de Gerlache rim, no distance limit."""
import math, json, sys, itertools, numpy as np
sys.path.insert(0, '../slope'); from render import lonlat2m
R = 1737400.
P = np.load('rim_pts.npy')[:, :2]; S = np.load('rim_series.npy') >= 0.5; single = S.mean(1)
s5 = np.array(lonlat2m(-88.6652, -68.42))
def ll(p):
    rho = math.hypot(*p); return round(-(90 - math.degrees(2 * math.atan(rho / (2 * R)))), 4), round(math.degrees(math.atan2(p[0], p[1])), 2)
def longest(mask):
    m = np.concatenate([[0], mask.astype(np.int8), [0]]); d = np.diff(m); st = np.where(d == 1)[0]; en = np.where(d == -1)[0]
    return int(((en - st).max() if len(st) else 0) * 2)
def mec(pts):
    pts = [np.array(p) for p in pts]; best = None
    cands = [(a + b) / 2 for a, b in itertools.combinations(pts, 2)] if len(pts) > 1 else [pts[0]]
    for a, b, c in itertools.combinations(pts, 3):
        d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
        if abs(d) < 1e-9: continue
        ux = ((a @ a) * (b[1] - c[1]) + (b @ b) * (c[1] - a[1]) + (c @ c) * (a[1] - b[1])) / d
        uy = ((a @ a) * (c[0] - b[0]) + (b @ b) * (a[0] - c[0]) + (c @ c) * (b[0] - a[0])) / d
        cands.append(np.array([ux, uy]))
    for c in cands:
        r = max(np.hypot(*(p - c)) for p in pts)
        if best is None or r < best[0]: best = (r, c)
    return best
def run(idx, limit):
    idx = [i for i in idx if single[i] >= 0.30]
    St = S[idx]; best = (0, None)
    for a in range(len(idx)):
        cov = (St[a][None, :] | St[a + 1:]).mean(1)
        for j in np.argsort(-cov):
            b = a + 1 + j; d = math.hypot(*(P[idx[a]] - P[idx[b]]))
            if d < 150 or (limit and d > 2 * limit): continue
            if cov[j] > best[0]: best = (cov[j], [idx[a], idx[b]])
            break
    ch = best[1]; res = []
    cur = S[ch[0]].copy(); res.append(([ch[0]], cur.mean(), longest(~cur)))
    cur = S[ch[0]] | S[ch[1]]; res.append((list(ch), cur.mean(), longest(~cur)))
    for _ in range(2):
        bestc = (cur.mean(), None)
        for i in idx:
            if i in ch or any(math.hypot(*(P[i] - P[j])) < 150 for j in ch): continue
            if limit and mec([P[j] for j in ch + [i]])[0] > limit: continue
            c = (cur | S[i]).mean()
            if c > bestc[0]: bestc = (c, i)
        if bestc[1] is None: break
        ch = ch + [bestc[1]]; cur = cur | S[bestc[1]]; res.append((list(ch), cur.mean(), longest(~cur)))
    return res
near = [i for i in range(len(P)) if math.hypot(*(P[i] - s5)) <= 22000]
rep = {}
for key, idx, limit in (('span20_pmc10', near, 10000),):
    rep[key] = []
    for ch, cov, lb in run(idx, limit):
        r, c = mec([P[j] for j in ch]) if len(ch) > 1 else (0, P[ch[0]])
        rep[key].append({'k': len(ch), 'either_lit_pct': round(cov * 100, 1), 'longest_blackout_h': lb, 'pmc': ll(c), 'pmc_radius_km': round(r / 1000, 2),
                         'spots': [{'lat': ll(P[i])[0], 'lon': ll(P[i])[1], 'single_pct': round(single[i] * 100, 1), 'to_pmc_km': round(math.hypot(*(P[i] - c)) / 1000, 2), 'to_site5_km': round(math.hypot(*(P[i] - s5)) / 1000, 2)} for i in ch],
                         'pair_dist_km': [round(math.hypot(*(P[a] - P[b])) / 1000, 2) for n, a in enumerate(ch) for b in ch[n + 1:]]})
json.dump(rep, open('dg_sets_span20.json', 'w'), indent=1)
for key in rep:
    print('==', key)
    for r in rep[key]:
        print(r['k'], r['either_lit_pct'], '%; blackout', r['longest_blackout_h'], 'h; PMC', r['pmc'], 'radius', r['pmc_radius_km'], 'km; dists', r['pair_dist_km'])
        for s_ in r['spots']: print('   ', s_)
