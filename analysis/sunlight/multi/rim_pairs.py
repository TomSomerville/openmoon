import sys, math, numpy as np, rasterio
from rasterio.windows import from_bounds
from PIL import Image
src=open('sun_at_height_60.py').read().split("out = ['x_m")[0]; ns={}; exec(src,ns)
sys.path.insert(0,'../slope'); from render import read, lonlat2m
cx,cy=lonlat2m(-88.5,-87.1); Rr=16200.
B=(cx-24000,cy-24000,cx+24000,cy+24000)
with rasterio.open('../illum/AVGVISIB_85S_060M_201608.TIF') as r:
    w=from_bounds(*B,transform=r.transform).round_offsets().round_lengths(); il=r.read(1,window=w).astype(float)*4e-3
    T=r.window_transform(w)
H,W=il.shape
sl=np.array(Image.fromarray(read('LDSM_83S_10MPP_ADJ',B,40).astype('float32'),mode='F').resize((W,H),Image.BILINEAR))
jj,ii=np.mgrid[0:H,0:W]; X=T.c+(ii+0.5)*T.a; Y=T.f+(jj+0.5)*T.e
d=np.hypot(X-cx,Y-cy)
ok=(d>Rr-4000)&(d<Rr+5000)&(il>=40)&(sl<=15)
# thin: best pixel per 500 m cell
pts=[]
for j in range(0,H,8):
    for i in range(0,W,8):
        b=np.where(ok[j:j+8,i:i+8],il[j:j+8,i:i+8],-1)
        if b.max()<0: continue
        a,c=np.unravel_index(b.argmax(),b.shape); pts.append((X[j+a,i+c],Y[j+a,i+c],b.max()))
pts=np.array(pts); print('rim points',len(pts),flush=True)
R=ns['R']; sun=ns['sun']
def series(X0,Y0):
    hz=ns['horizon'](X0,Y0,0.5)
    rho=math.hypot(X0,Y0); lat=-(math.pi/2-2*math.atan(rho/(2*R))); lon=math.atan2(X0,Y0)
    u=np.array([math.cos(lat)*math.cos(lon),math.cos(lat)*math.sin(lon),math.sin(lat)]); e=np.array([-math.sin(lon),math.cos(lon),0.]); n=np.cross(u,e)
    su,se,sn=u@sun,e@sun,n@sun; elev=np.degrees(np.arcsin(np.clip(su,-1,1)))
    vx=sn*math.sin(lon)+se*math.cos(lon); vy=sn*math.cos(lon)-se*math.sin(lon)
    az=np.degrees(np.arctan2(vx,vy))%360; k=az/0.5; k0=np.floor(k).astype(int)%720; f=k-np.floor(k)
    h=hz[k0]*(1-f)+hz[(k0+1)%720]*f
    return np.clip((elev-h+0.2666)/0.5332,0,1).astype('float32')
S=np.array([series(x,y) for x,y,_ in pts]); np.save('rim_series.npy',S); np.save('rim_pts.npy',pts)
print('done',S.shape,flush=True)
