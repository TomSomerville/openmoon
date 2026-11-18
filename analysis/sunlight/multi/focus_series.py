import csv, math, numpy as np
src=open('rim_pairs.py').read()
pre=src.split("cx,cy=lonlat2m")[0]; ns={}; exec(pre,ns)
fn=src[src.index('R=ns['):src.index('S=np.array')]; exec(fn,ns)
pts=np.load('cands50.npy')
print('points',len(pts),flush=True)
S=[]
for i,(x,y,_) in enumerate(pts):
    S.append(ns['series'](x,y))
    if i%50==0: print(i,flush=True)
np.save('focus_series.npy',np.array(S)); np.save('focus_pts.npy',pts); print('done',flush=True)
