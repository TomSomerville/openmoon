import sys,os,math,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
L=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cells.npz')
d=np.load(L); X,Y,r,err,lat,ref=d['X'],d['Y'],d['r'],d['err'],d['lat'],float(d['ref'])
ok=np.isfinite(r); X,Y,r,err=X[ok],Y[ok],r[ok],err[ok]
SIG=10000.; THR=1.28; ZMIN=3.0
def supp_grid(bounds,step):
    xs=np.arange(bounds[0]+step/2,bounds[2],step); ys=np.arange(bounds[3]-step/2,bounds[1],-step)
    S=np.zeros((len(ys),len(xs))); Z=np.zeros_like(S)
    near=(X>bounds[0]-5*SIG)&(X<bounds[2]+5*SIG)&(Y>bounds[1]-5*SIG)&(Y<bounds[3]+5*SIG)
    x,y,rr,ee=X[near],Y[near],r[near],err[near]
    for j,py in enumerate(ys):
        for i,px in enumerate(xs):
            g=np.exp(-((x-px)**2+(y-py)**2)/(2*SIG**2)); w=g/ee**2
            m=(w*rr).sum()/w.sum(); se=1/np.sqrt(w.sum())
            S[j,i]=(1-m/ref)*100; Z[j,i]=(ref-m)/se
    return S,Z
