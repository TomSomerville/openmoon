"""Read the M3 water maps (Li et al. 2023, USGS PDS4 archive doi:10.17189/gmce-w279) in a window around the primary base
and save them to data/m3water/. Window: 80-45 deg W, 87.6-89.2 deg S. Run once; mk_m3.py uses the saved windows."""
import os,sys,numpy as np,rasterio
from rasterio.windows import from_bounds
os.environ['CURL_CA_BUNDLE']='/root/.ccr/ca-bundle.crt'; os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR'
B='/vsicurl/https://asc-pds-individual-investigations.s3.us-west-2.amazonaws.com/moon_m3_lunarwater_li_2023/data/WaterMaps/'
names=['DawnMagnetosheath','ExitDawnMagnetosheath','FirstHalfCentralMagnetotail','SecondHalfCentralMagnetotail','DuskMagnetosheath','BeforeDuskMagnetosheath']
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','m3water'); os.makedirs(OUT,exist_ok=True)
for n in names:
    with rasterio.open(B+f'M3_ppmWater_{n}.tif') as ds:
        if n==names[0]: print(ds.width,ds.height,ds.crs,ds.transform,ds.nodata,ds.block_shapes,ds.profile.get('compress'))
        # degrees -> metres in equirect (R=1737400)
        k=1.0  # the GeoTIFF transform is in degrees
        w=from_bounds(-80*k,-89.2*k,-45*k,-87.6*k,ds.transform)
        a=ds.read(1,window=w); t=ds.window_transform(w)
        np.savez_compressed(os.path.join(OUT,n+'.npz'),a=a.astype('float32'),t=np.array(t)[:6])
        v=a[np.isfinite(a)&(a>0)&(a<1e5)]
        print(n,a.shape,'valid',v.size, (np.percentile(v,[5,50,95]) if v.size else None), 'min/max',np.nanmin(a),np.nanmax(a))
