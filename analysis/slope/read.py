import os, sys, numpy as np, rasterio
from rasterio.windows import from_bounds
from rasterio.enums import Resampling
os.environ.setdefault('CURL_CA_BUNDLE','/root/.ccr/ca-bundle.crt')
os.environ.setdefault('GDAL_DISABLE_READDIR_ON_OPEN','EMPTY_DIR')
os.environ['GDAL_HTTP_MAX_RETRY']='8'; os.environ['GDAL_HTTP_RETRY_DELAY']='3'; os.environ['VSI_CACHE']='FALSE'; os.environ['GDAL_HTTP_MULTIRANGE']='SERIAL'
BASE='/vsicurl/https://pgda.gsfc.nasa.gov/data/LOLA_20mpp/'
# NASA map georeference: pole px, px per km
P0=(745.8,762.3); PXKM=182/50.0
def px2m(x,y): return ((x-P0[0])/PXKM*1000, (P0[1]-y)/PXKM*1000)
def read(name, bounds_m, res):
    import hashlib,time
    key='cache_'+hashlib.md5(repr((name,[round(b) for b in bounds_m],res)).encode()).hexdigest()+'.npy'
    if os.path.exists(key): return np.load(key)
    for t in range(5):
        try:
            a=_read(name,bounds_m,res); np.save(key,a); return a
        except Exception as e:
            print('retry',t,e); time.sleep(5)
    raise
def _read(name, bounds_m, res):
    import time
    from rasterio.windows import Window
    lvl={10:None,20:0,40:1,80:2}[res]
    kw={} if lvl is None else {'OVERVIEW_LEVEL':lvl}
    path=BASE+name+'.TIF'
    r=rasterio.open(path,**kw)
    w=from_bounds(*bounds_m, transform=r.transform).round_offsets().round_lengths()
    c0,r0,W,H=int(w.col_off),int(w.row_off),int(w.width),int(w.height)
    out=np.empty((H,W),'float32'); B=512; bad=0
    for ry in range((r0//B)*B, r0+H, B):
        for cx in range((c0//B)*B, c0+W, B):
            a0,b0=max(ry,r0),max(cx,c0); a1,b1=min(ry+B,r0+H),min(cx+B,c0+W)
            for t in range(10):
                try:
                    a=r.read(1,window=Window(b0,a0,b1-b0,a1-a0))
                    if np.all(np.isnan(a)) or np.all(a==0): raise IOError('empty tile')
                    out[a0-r0:a1-r0,b0-c0:b1-c0]=a; break
                except Exception as e:
                    if t==9: raise RuntimeError('tile failed %d,%d: %s'%(a0,b0,e))
                    bad+=1; time.sleep(2+2*t); r.close(); r=rasterio.open(path,**kw)
    r.close(); print(name,res,'tile retries',bad,flush=True)
    return out
