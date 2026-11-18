import sys, math, json, pickle, numpy as np, csv
sys.path.insert(0,'../slope'); from render import read, px2m, lonlat2m
import rasterio
R=1737400.
fx0,fy1=px2m(292,518); fx1,fy0=px2m(953,989); B=(fx0,fy0,fx1,fy1)
mpp=(fx1-fx0)/2400.
def img2m(x,y): return fx0+x*1.2*mpp, fy1-y*1.2*mpp
def ll(X,Y):
    rho=math.hypot(X,Y); return -(90-math.degrees(2*math.atan(rho/(2*R)))), math.degrees(math.atan2(X,Y))
sites={'Circle 1 (north rim of de Gerlache)':img2m(908.6,507.0),'Circle 2 (Connecting ridge, by Shackleton)':img2m(1331.6,880.6)}
# slope 40 m grid
sl=read('LDSM_83S_10MPP_ADJ',B,40)
def slope_at(X,Y,rad):
    c=int((X-B[0])/40); r=int((B[3]-Y)/40); n=int(rad/40)
    w=sl[max(0,r-n):r+n+1,max(0,c-n):c+n+1]; return float(sl[r,c]), float((w<=8).mean()*100)
# NASA illumination
il_ds=rasterio.open('../illum/AVGVISIB_85S_060M_201608.TIF')
def illum(X,Y,rad=0):
    if rad==0: return float(list(il_ds.sample([(X,Y)]))[0][0])*4e-3
    from rasterio.windows import from_bounds
    w=from_bounds(X-rad,Y-rad,X+rad,Y+rad,transform=il_ds.transform); a=il_ds.read(1,window=w).astype(float)*4e-3; return float(a.max())
# PSRs
P=pickle.load(open('../psr/psr_focus.pkl','rb'))
CANDS={'Shackleton floor':(lonlat2m(-89.67,129.78),10.5e3),'de Gerlache floor':(lonlat2m(-88.5,-87.1),16.2e3)}
def psr_dist(X,Y,which=None,minarea=0.0):
    best=1e12
    for g,a,n,b,rings in P:
        if a<minarea: continue
        cx,cy=(b[0]+b[2])/2,(b[1]+b[3])/2
        if which is not None:
            (px,py),rad=CANDS[which]
            if a<1 or math.hypot(cx-px,cy-py)>rad: continue
        if math.hypot(cx-X,cy-Y)-max(b[2]-b[0],b[3]-b[1])>best: continue
        for r in rings:
            d=np.hypot(r[:,0]-X,r[:,1]-Y).min(); best=min(best,d)
    return best/1000
# hydrogen high zone (1 km grid over focus)
S=np.load('../slope/focus_S.npy'); Z=np.load('../slope/focus_Z.npy'); hi=(S>=1.28)&(Z>=3)
jj,ii=np.nonzero(hi); HX=B[0]+(ii+0.5)*1000; HY=B[3]-(jj+0.5)*1000
def hyd(X,Y):
    c=int((X-B[0])/1000); r=int((B[3]-Y)/1000); return float(S[r,c]), float(np.hypot(HX-X,HY-Y).min()/1000)
# VSAT sets
M='/home/user/openmoon/analysis/sunlight/multi/'
A=json.load(open(M+'vsat_sets.json'))['dd013'][3]; C=json.load(open(M+'dg_sets.json'))['dd014_10km'][3]; D=json.load(open(M+'dg_sets_span20.json'))['span20_pmc10'][3]
spots=[(float(r['x_m']),float(r['y_m']),float(r['sunlit_pct'])) for r in csv.DictReader(open('/home/user/openmoon/analysis/sunlight/vsat_spots.csv'))]
def dkm(X,Y,la,lo): x,y=lonlat2m(la,lo); return math.hypot(x-X,y-Y)/1000
out={}
for name,(X,Y) in sites.items():
    la,lo=ll(X,Y); s0,f8=slope_at(X,Y,1000)
    o={'lat':round(la,4),'lon':round(lo,2),'slope_deg':round(s0,1),'landable_within_1km_pct':round(f8,0),'sunlit_ground_pct':round(illum(X,Y),1),'best_sunlit_within_1km':round(illum(X,Y,1000),1),
       'to_de_gerlache_floor_km':round(psr_dist(X,Y,'de Gerlache floor'),1),'to_shackleton_floor_km':round(psr_dist(X,Y,'Shackleton floor'),1),
       'to_nearest_psr_0.5km2_km':round(psr_dist(X,Y,None,0.5),2),'to_shadowcam_spot_km':round(dkm(X,Y,-88.5352,-97.4007),1),
       'hydrogen_dip_here_pct':round(hyd(X,Y)[0],2),'to_high_hydrogen_km':round(hyd(X,Y)[1],1),
       'to_site5_km':round(dkm(X,Y,-88.6652,-68.42),1),'to_ridge_pmc_km':round(dkm(X,Y,*A['pmc']),1),'to_opt2_pmc_km':round(dkm(X,Y,*D['pmc']),1),
       'setA_dists_km':[round(dkm(X,Y,s['lat'],s['lon']),1) for s in A['spots']],'setC_dists_km':[round(dkm(X,Y,s['lat'],s['lon']),1) for s in C['spots']],'setD_dists_km':[round(dkm(X,Y,s['lat'],s['lon']),1) for s in D['spots']]}
    near=sorted([(math.hypot(x-X,y-Y)/1000,p) for x,y,p in spots])
    o['vsat_sites_80_within_10km']=[ (round(d,1),p) for d,p in near if p>=80 and d<=10]
    o['vsat_sites_70_within_10km']=len([1 for d,p in near if p>=70 and d<=10])
    o['nearest_80_site']=[(round(d,1),p) for d,p in near if p>=80][:1]
    out[name]=o
json.dump(out,open('colony.json','w'),indent=1)
for k,v in out.items(): print(k); [print('  ',a,':',b) for a,b in v.items()]
