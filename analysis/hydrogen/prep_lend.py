"""Read NASA LRO LEND averaged south-polar products (PDS) and save per-cell
collimated epithermal neutron (CSETN) count rates for hydro.py.

Download first (PDS Geosciences Node):
  https://pds-geosciences.wustl.edu/lro/lro-l-lend-2-edr-v1/lrolen_0xxx/data/2009/20090915/lend_rdr_alds_20090915.dat
  https://pds-geosciences.wustl.edu/lro/lro-l-lend-2-edr-v1/lrolen_0xxx/data/2011/20111211/lend_rdr_alds_20111211.dat
Each file: 14400 rows x 310 bytes, 0.5 x 0.5 degree cells poleward of 80 S (see the .lbl/.xml labels).
"""
import numpy as np
dt = np.dtype([('t0', 'S23'), ('t1', 'S23'), ('lat', '>f4'), ('lon', '>f4'), ('sp', '>f4')] +
              [(f'{n}_{k}', '>f4') for n in ['STN1', 'SETN', 'STN2', 'STN3', 'CSETN'] for k in ['exp', 'rate', 'err']] +
              [('rest', 'V%d' % (310 - 118))])
A = [np.fromfile(f, dtype=dt) for f in ['lend_rdr_alds_20090915.dat', 'lend_rdr_alds_20111211.dat']]
lat = A[0]['lat'].astype(float); lon = A[0]['lon'].astype(float)
# inverse-variance combination of the two periods
num = sum(np.where(a['CSETN_exp'] > 0, a['CSETN_rate'] / a['CSETN_err'] ** 2, 0) for a in A)
iv = sum(np.where(a['CSETN_exp'] > 0, 1 / np.maximum(a['CSETN_err'].astype(float), 1e-6) ** 2, 0) for a in A)
r = np.where(iv > 0, num / np.maximum(iv, 1e-12), np.nan)
err = np.where(iv > 0, 1 / np.sqrt(np.maximum(iv, 1e-12)), np.nan)
R = 1737400.  # south polar stereographic, as the LOLA products
rho = 2 * R * np.tan(np.radians(90 + lat) / 2)
X, Y = rho * np.sin(np.radians(lon)), rho * np.cos(np.radians(lon))
ref = np.median(r[np.isfinite(r) & (lat < -80) & (lat > -84)])  # reference: 80-84 S median
np.savez('cells.npz', X=X, Y=Y, r=r, err=err, lat=lat, lon=lon, ref=ref)
print('reference rate', ref)
