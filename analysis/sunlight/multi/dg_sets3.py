"""ESTIMATE: de Gerlache rim, base/PMC at site 5 (88.6652 S, 68.42 W). Best 1-4 VSAT spots with
(a) every spot within 10 km of the PMC (DD-014), (b) within 3 km (DD-013) for comparison.
Best pair by exhaustive search, then best 3rd and 4th spot added."""
import math, json, sys, numpy as np
sys.path.insert(0, '../slope'); from render import lonlat2m
R = 1737400.
P = np.load('rim_pts.npy')[:, :2]; S = np.load('rim_series.npy') >= 0.5; single = S.mean(1)
s5 = np.array(lonlat2m(-88.6652, -68.42))
def ll(p):
    rho = math.hypot(*p); return round(-(90 - math.degrees(2 * math.atan(rho / (2 * R)))), 4), round(math.degrees(math.atan2(p[0], p[1])), 2)
def longest(mask):
    m = np.concatenate([[0], mask.astype(np.int8), [0]]); d = np.diff(m); st = np.where(d == 1)[0]; en = np.where(d == -1)[0]
    return int(((en - st).max() if len(st) else 0) * 2)
def run(limit):
    idx = [i for i in range(len(P)) if math.hypot(*(P[i] - s5)) <= limit and single[i] >= 0.30]
    St = S[idx]; res = []
    a1 = int(np.argmax(St.mean(1))); cur = St[a1]; res.append(([idx[a1]], cur.mean(), longest(~cur)))
    best = (0, None)
    for a in range(len(idx)):
        cov = (St[a][None, :] | St[a + 1:]).mean(1)
        if len(cov) and cov.max() > best[0]: best = (cov.max(), [idx[a], idx[a + 1 + int(cov.argmax())]])
    ch = best[1]; cur = S[ch[0]] | S[ch[1]]; res.append((list(ch), cur.mean(), longest(~cur)))
    for _ in range(2):
        cov = np.array([(cur | S[i]).mean() if i not in ch else -1 for i in idx]); b = idx[int(cov.argmax())]
        ch = ch + [b]; cur = cur | S[b]; res.append((list(ch), cur.mean(), longest(~cur)))
    return res
rep = {}
for key, lim in (('dd014_10km', 10000), ('dd013_3km', 3000)):
    rep[key] = []
    for ch, cov, lb in run(lim):
        rep[key].append({'k': len(ch), 'either_lit_pct': round(cov * 100, 1), 'longest_blackout_h': lb,
                         'spots': [{'lat': ll(P[i])[0], 'lon': ll(P[i])[1], 'single_pct': round(single[i] * 100, 1), 'to_base_km': round(math.hypot(*(P[i] - s5)) / 1000, 2)} for i in ch],
                         'pair_dist_km': [round(math.hypot(*(P[a] - P[b])) / 1000, 2) for n, a in enumerate(ch) for b in ch[n + 1:]]})
json.dump(rep, open('dg_sets.json', 'w'), indent=1)
for key in rep:
    print('==', key)
    for r in rep[key]:
        print(r['k'], r['either_lit_pct'], '%; blackout', r['longest_blackout_h'], 'h; dists', r['pair_dist_km'])
        for s_ in r['spots']: print('   ', s_)
