import os, sys, numpy as np, rasterio
from rasterio.windows import from_bounds
from rasterio.enums import Resampling
os.environ.setdefault('CURL_CA_BUNDLE','/root/.ccr/ca-bundle.crt')
os.environ.setdefault('GDAL_DISABLE_READDIR_ON_OPEN','EMPTY_DIR')
os.environ['GDAL_HTTP_MAX_RETRY']='8'; os.environ['GDAL_HTTP_RETRY_DELAY']='3'; os.environ['VSI_CACHE']='FALSE'; os.environ['GDAL_HTTP_MULTIRANGE']='SERIAL'
BASE='/vsicurl/https://pgda.gsfc.nasa.gov/data/LOLA_20mpp/'
DATA=os.environ.get('OPENMOON_DATA',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data'))
def kind(name,a):
    if name: return 'slope' if 'LDSM' in name else 'hill' if 'HILL' in name else 'dem'
    v=a[np.isfinite(a)]; lo,hi=float(v.min()),float(v.max())
    if lo<-0.5 or hi>300: return 'dem'
    if hi<=90.5: return 'slope'
    return 'hill'
def pack(a,path,name=None):
    os.makedirs(os.path.dirname(path),exist_ok=True); k=kind(name,a); nan=~np.isfinite(a)
    if k=='dem': q=np.round(np.nan_to_num(a)*4).astype('int16'); q[nan]=-32768
    elif k=='slope': q=np.round(np.nan_to_num(a)*100).astype('int16'); q[nan]=-32768
    else: q=np.clip(np.round(np.nan_to_num(a)),0,255).astype('uint8')
    np.savez_compressed(path,q=q,kind=k,name=name or '')
def unpack(path):
    z=np.load(path); q=z['q']; k=str(z['kind'])
    if k=='hill': return q.astype('float32')
    a=q.astype('float32')/(4. if k=='dem' else 100.); a[q==-32768]=np.nan; return a
# NASA map georeference: pole px, px per km
P0=(745.8,762.3); PXKM=182/50.0
def px2m(x,y): return ((x-P0[0])/PXKM*1000, (P0[1]-y)/PXKM*1000)
def read(name, bounds_m, res):
    import hashlib,time
    key='cache_'+hashlib.md5(repr((name,[round(b) for b in bounds_m],res)).encode()).hexdigest()+'.npy'
    if os.path.exists(key): return np.load(key)
    pk=os.path.join(DATA,'lola_cache',key[:-4]+'.npz')          # permanent cache in the repository (data/)
    if os.path.exists(pk):
        a=unpack(pk); np.save(key,a); return a
    for t in range(5):
        try:
            a=_read(name,bounds_m,res); np.save(key,a); pack(a,pk,name); return a
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
                    bad+=1; time.sleep(2+2*t)
                    try: r.close()
                    except Exception: pass
                    for t2 in range(10):
                        try: r=rasterio.open(path,**kw); break
                        except Exception: time.sleep(5+5*t2)
    r.close(); print(name,res,'tile retries',bad,flush=True)
    return out
