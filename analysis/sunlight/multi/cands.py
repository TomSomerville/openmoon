import sys, math, numpy as np
sys.path.insert(0,'/tmp/claude-0/-home-user-openmoon/22f9fb57-346f-5949-b7d3-c6e2d377f58f/scratchpad/slope')
from render import read, px2m
import rasterio
from rasterio.windows import from_bounds
from PIL import Image
fx0,fy1=px2m(292,518); fx1,fy0=px2m(953,989); B=(fx0,fy0,fx1,fy1); RES=60
with rasterio.open('../illum/AVGVISIB_85S_060M_201608.TIF') as r:
    w=from_bounds(*B,transform=r.transform).round_offsets().round_lengths(); il=r.read(1,window=w).astype(float); il[il==-32768]=np.nan; il*=4e-3
H,W=il.shape
sl=np.array(Image.fromarray(read('LDSM_83S_10MPP_ADJ',B,40).astype('float32'),mode='F').resize((W,H),Image.BILINEAR))
BIN=int(1000/RES); out=[]
for j in range(0,H,BIN):
    for i in range(0,W,BIN):
        blk=np.where(sl[j:j+BIN,i:i+BIN]<=15,il[j:j+BIN,i:i+BIN],np.nan)
        if np.all(np.isnan(blk)) or np.nanmax(blk)<60: continue
        jj,ii=np.unravel_index(np.nanargmax(blk),blk.shape); y,x=j+jj,i+ii
        X=B[0]+(x+0.5)*RES; Y=B[3]-(y+0.5)*RES
        out.append((X,Y,np.nanmax(blk)))
np.save('cands.npy',np.array(out)); print(len(out),'candidate cells >=60% ground')
