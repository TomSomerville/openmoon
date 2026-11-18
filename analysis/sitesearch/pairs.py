"""ESTIMATE (Open Moon): every pair of candidate VSAT spots up to 20 km apart, with combined sunlight (time at least
one is lit) and the longest time both are dark. Ground level, 2-hour steps over 18.6 years (see analysis/sunlight/multi).
Run in the folder holding focus/rim/near3 _pts.npy and _series.npy. Output: pairs.npz"""
import numpy as np, math, time
P = np.vstack([np.load(f + '_pts.npy')[:, :2] for f in ('focus', 'rim', 'near3')])
S = np.vstack([np.load(f + '_series.npy') for f in ('focus', 'rim', 'near3')]) >= 0.5
single = S.mean(1)
o = np.argsort(-single); keep = []
for i in o:                                   # drop near-duplicates (< 150 m), keep the brighter
    if single[i] < 0.30: continue
    if not keep or np.hypot(*(P[keep] - P[i]).T).min() >= 150: keep.append(i)
P, S, single = P[keep], S[keep], single[keep]; n, T = S.shape
print('spots', n, flush=True)
D = ~S
def longest(dark):
    m = np.concatenate([[0], dark.astype(np.int8), [0]]); d = np.diff(m); s = np.where(d == 1)[0]; e = np.where(d == -1)[0]
    return ((e - s).max() if len(s) else 0) * 2 / 24
Pk = np.packbits(S, axis=1); pc = np.unpackbits(np.arange(256, dtype=np.uint8)[:, None], axis=1).sum(1)
I, J, LIT, LD = [], [], [], []; t0 = time.time()
for i in range(n):
    dist = np.hypot(*(P[i + 1:] - P[i]).T); js = np.where(dist <= 20000)[0] + i + 1
    if len(js) == 0: continue
    cov = pc[Pk[i] | Pk[js]].sum(1) / T
    for j, c in zip(js, cov):
        I.append(i); J.append(j); LIT.append(c); LD.append(longest(D[i] & D[j]))
    if i % 100 == 0: print(i, len(I), '%.0fs' % (time.time() - t0), flush=True)
np.savez('pairs.npz', P=P, single=single, I=np.array(I), J=np.array(J), lit=np.array(LIT), ld=np.array(LD))
print('pairs', len(I), 'with longest dark <= 7 d:', int((np.array(LD) <= 7).sum()))
