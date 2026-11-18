import sys, numpy as np
sys.path.insert(0,'/tmp/claude-0/-home-user-openmoon/22f9fb57-346f-5949-b7d3-c6e2d377f58f/scratchpad/slope')
import read as R
# far field: whole 83S tile at 80 m (overview level 2)
far=R._read('LDEM_83S_10MPP_ADJ',(-216400,-216400,216400,216400),80); np.save('dem80.npy',far.astype('float32')); print('far',far.shape,np.nanmin(far),np.nanmax(far),flush=True)
# near field: focus area + 12 km margin at 20 m (overview level 0)
x0,y1=R.px2m(292,518); x1,y0=R.px2m(953,989); m=12000
b=(x0-m,y0-m,x1+m,y1+m); near=R._read('LDEM_83S_10MPP_ADJ',b,20); np.save('dem20.npy',near.astype('float32')); np.save('dem20_bounds.npy',np.array(b)); print('near',near.shape,flush=True)
