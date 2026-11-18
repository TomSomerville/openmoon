"""Survey LROC NAC south-pole sub-solar-longitude mosaics (1 m/px, NASA PDS) around a point: how much of a 2 km box
is covered and lit in each lighting bin. Usage: survey_bins.py LAT LON"""
import sys, math, time, numpy as np, rasterio
from rasterio.windows import from_bounds
U = ('/vsicurl/https://pds.mcp.nasa.gov/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/'
     'LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/NAC_POLE_SOUTH_{p}/NAC_POLE_SOUTH_{p}_P878S2925.{e}')
R = 1737400.
la, lo = float(sys.argv[1]), float(sys.argv[2])
rho = 2 * R * math.tan(math.radians(90 + la) / 2); cx, cy = rho * math.sin(math.radians(lo)), rho * math.cos(math.radians(lo))
def rd(p, half=1000, px=200):
    for e in ('PYR.TIF', 'TIF'):
        for k in range(4):
            try:
                with rasterio.open(U.format(p=p, e=e)) as d:
                    w = from_bounds(cx - half, cy - half, cx + half, cy + half, d.transform)
                    return d.read(1, window=w, out_shape=(px, px)).astype(float)
            except Exception as ex:
                err = str(ex); time.sleep(8 * (k + 1))
                if '404' in err: break
    return None
for b in ['MAX', 'AVG', '005', '035'] + ['%03d' % v for v in range(145, 360, 10)]:
    a = rd('CM_' + b)
    if a is None: print(b, 'unavailable', flush=True); continue
    cov = (a > 0).mean(); v = a[a > 0]
    lit = (v > max(20, np.percentile(v, 95) * 0.25)).mean() if len(v) else 0
    print(b, 'cover %.0f%%' % (cov * 100), 'median %.0f' % (np.median(v) if len(v) else 0), 'p10 %.0f' % (np.percentile(v, 10) if len(v) else 0), 'lit %.0f%%' % (lit * 100), flush=True)
    time.sleep(4)
