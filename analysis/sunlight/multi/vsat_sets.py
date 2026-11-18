"""ESTIMATE: best sets of 1-4 VSAT spots by combined sunlight (time at least one spot has >= half the Sun's disc above
its horizon), ground level, 2-hour steps over 18.6 years. Greedy selection (good for coverage problems).
Constraint DD-013: all spots within 3 km (straight line) of one PMC location; PMC candidates = every candidate spot."""
import math, json, numpy as np
R = 1737400.
P = np.vstack([np.load('focus_pts.npy')[:, :2], np.load('rim_pts.npy')[:, :2]])
S = np.vstack([np.load('focus_series.npy'), np.load('rim_series.npy')]) >= 0.5
single = S.mean(1)
keep = single >= 0.40; P, S, single = P[keep], S[keep], single[keep]
# drop near-duplicates (< 150 m), keep brighter
order = np.argsort(-single); sel = []
for i in order:
    if all(math.hypot(*(P[i] - P[j])) >= 150 for j in sel): sel.append(i)
P, S, single = P[sel], S[sel], single[sel]
print('spots', len(P), flush=True)

def ll(x, y):
    rho = math.hypot(x, y); return -(90 - math.degrees(2 * math.atan(rho / (2 * R)))), math.degrees(math.atan2(x, y))
def longest(mask):
    m = np.concatenate([[0], mask.astype(np.int8), [0]]); d = np.diff(m); s = np.where(d == 1)[0]; e = np.where(d == -1)[0]
    return int(((e - s).max() if len(s) else 0) * 2)
def greedy(idx, k=4):
    cur = np.zeros(S.shape[1], bool); chosen = []; res = []
    for _ in range(k):
        cand = [i for i in idx if i not in chosen]
        if not cand: break
        cov = np.array([(cur | S[i]).mean() for i in cand])
        b = cand[int(cov.argmax())]; chosen.append(b); cur |= S[b]
        res.append((list(chosen), cur.mean() * 100, longest(~cur)))
    return res

out = {}
# unconstrained
out['any'] = greedy(list(range(len(P))))
# DD-013: within 3 km of a PMC placed at a candidate spot
best = {}
for c in range(len(P)):
    if single[c] < 0.55: continue
    idx = [i for i in range(len(P)) if math.hypot(*(P[i] - P[c])) <= 3000]
    for chosen, cov, lb in greedy(idx):
        k = len(chosen)
        if k not in best or cov > best[k][1]: best[k] = (chosen, cov, lb, c)
out['dd013'] = [best[k] for k in sorted(best)]

def describe(chosen, pmc=None):
    rows = []
    for i in chosen:
        la, lo = ll(*P[i]); rows.append({'lat': round(la, 4), 'lon': round(lo, 2), 'single_pct': round(single[i] * 100, 1),
                                         'to_pmc_km': round(math.hypot(*(P[i] - P[pmc])) / 1000, 2) if pmc is not None else None})
    d = [round(math.hypot(*(P[a] - P[b])) / 1000, 2) for n, a in enumerate(chosen) for b in chosen[n + 1:]]
    return rows, d
report = {'any': [], 'dd013': []}
for chosen, cov, lb in out['any']:
    rows, d = describe(chosen); report['any'].append({'k': len(chosen), 'either_lit_pct': round(cov, 1), 'longest_blackout_h': lb, 'spots': rows, 'pair_dist_km': d})
for chosen, cov, lb, c in out['dd013']:
    rows, d = describe(chosen, c); la, lo = ll(*P[c])
    report['dd013'].append({'k': len(chosen), 'either_lit_pct': round(cov, 1), 'longest_blackout_h': lb, 'pmc': [round(la, 4), round(lo, 2)], 'spots': rows, 'pair_dist_km': d})
json.dump(report, open('vsat_sets.json', 'w'), indent=1)
for key in ('any', 'dd013'):
    print('==', key)
    for r in report[key]:
        print(r['k'], r['either_lit_pct'], '% lit; longest blackout', r['longest_blackout_h'], 'h; dists', r['pair_dist_km'])
        for s in r['spots']: print('    ', s)
