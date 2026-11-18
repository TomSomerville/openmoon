import sys, math; sys.path.insert(0,'.')
from read import *
from PIL import Image, ImageDraw, ImageFont
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def cmap(s):
    # 0 green -> 10 yellow -> 25 orange -> 60+ red (linear between stops)
    stops=np.array([0,10,25,60.]); cols=np.array([[0,170,0],[255,230,0],[255,140,0],[220,0,0]],float)
    s=np.clip(s,0,60); out=np.zeros(s.shape+(3,))
    for c in range(3): out[...,c]=np.interp(s,stops,cols[:,c])
    return out
CLASSES=[(0,8,(0,170,0),'≤8°'),(8,15,(255,220,0),'8–15°'),(15,20,(255,140,0),'15–20°'),(20,91,(220,0,0),'≥20°')]
def cmap_classes(s):
    out=np.zeros(s.shape+(3,))
    for lo,hi,c,_ in CLASSES:
        m=(s>lo if lo>0 else s>=lo)&(s<=hi) if hi<91 else (s>lo)
        if lo==0: m=s<=hi
        out[m]=c
    return out
def lonlat2m(lat,lon):
    R=1737400.; colat=math.radians(90+lat); rho=2*R*math.tan(colat/2); L=math.radians(lon)
    return rho*math.sin(L), rho*math.cos(L)
def make(name,bounds,res,out,alpha=0.6,threshold_mode=False,annot=(),title=''):
    s=read('LDSM_83S_10MPP_ADJ',bounds,res)
    h=read('LDEM_83S_10MPP_ADJ_HILL',bounds,res)
    hv=np.nan_to_num(h,nan=0); hv=(hv-np.percentile(hv,1))/(np.percentile(hv,99)-np.percentile(hv,1)+1e-9); hv=np.clip(hv,0,1)
    base=np.stack([hv*255]*3,-1)
    if threshold_mode=='classes':
        col=cmap_classes(s)
    elif threshold_mode:
        col=np.where((s<=15)[...,None],np.array([0,200,0.]),np.array([220,0,0.]))
    else: col=cmap(s)
    valid=~np.isnan(s)
    rgb=np.where(valid[...,None], base*(1-alpha)+col*alpha, base)
    im=Image.fromarray(rgb.astype('uint8')); d=ImageDraw.Draw(im)
    W,H=im.size; k=max(W,H)/1400
    F=ImageFont.truetype(FB,int(24*k)); Fs=ImageFont.truetype(FB,int(16*k))
    def m2p(x,y): return ((x-bounds[0])/res,(bounds[3]-y)/res)
    for a in annot:
        if a[0]=='circle':
            _,lat,lon,diam,lab,side=a; x,y=m2p(*lonlat2m(lat,lon)); r=diam*500/res
            d.ellipse((x-r,y-r,x+r,y+r),outline=(0,230,255),width=max(2,int(3*k)))
            d.text((x+(r+8*k if side=='r' else -r-8*k),y),lab,font=F,fill=(0,230,255),anchor='lm' if side=='r' else 'rm',stroke_width=3,stroke_fill=(0,0,0))
        if a[0]=='box':
            _,bx,lab=a; p0=m2p(bx[0],bx[3]); p1=m2p(bx[2],bx[1])
            d.rectangle((*p0,*p1),outline=(255,255,0),width=max(2,int(3*k)))
            d.text((p0[0],p0[1]-6*k),lab,font=F,fill=(255,255,0),anchor='ld',stroke_width=3,stroke_fill=(0,0,0))
        if a[0]=='star':
            x,y=m2p(0,0); r=7*k; d.ellipse((x-r,y-r,x+r,y+r),fill=(0,255,0),outline=(0,0,0))
            d.text((x+10*k,y-10*k),'South Pole',font=Fs,fill=(255,255,255),anchor='ld',stroke_width=3,stroke_fill=(0,0,0))
    # legend
    lw,lh=int(420*k),int(18*k); lx,ly=int(20*k),H-int(80*k)
    d.rectangle((lx-10*k,ly-34*k,lx+lw+10*k,H-8*k),fill=(0,0,0))
    if threshold_mode=='classes':
        n=len(CLASSES)
        for i,(lo,hi,c,lab) in enumerate(CLASSES):
            x0=lx+lw*i/n; d.rectangle((x0,ly,lx+lw*(i+1)/n,ly+lh),fill=c); d.text((x0+lw/n/2,ly+lh+6*k),lab,font=Fs,fill='white',anchor='mt')
        d.text((lx,ly-6*k),'Slope class (Open Moon landing rules)',font=Fs,fill='white',anchor='ld')
    elif threshold_mode:
        d.rectangle((lx,ly,lx+lw//2,ly+lh),fill=(0,200,0)); d.rectangle((lx+lw//2,ly,lx+lw,ly+lh),fill=(220,0,0))
        d.text((lx,ly-6*k),'Slope ≤15° (landing-suitable) | >15°',font=Fs,fill='white',anchor='ld')
    else:
        g=cmap(np.linspace(0,60,lw)); 
        for i in range(lw): d.line([(lx+i,ly),(lx+i,ly+lh)],fill=tuple(int(c) for c in g[i]))
        for v in (0,10,25,45,60):
            xx=lx+lw*v/60; d.line([(xx,ly+lh),(xx,ly+lh+5*k)],fill='white',width=2); d.text((xx,ly+lh+6*k),f'{v}°'+('+' if v==60 else ''),font=Fs,fill='white',anchor='mt')
        xx=lx+lw*15/60; d.line([(xx,ly-3*k),(xx,ly+lh)],fill='white',width=max(2,int(3*k)))
        d.text((lx,ly-6*k),'Slope (°)  — white tick: 15° landing limit',font=Fs,fill='white',anchor='ld')
    # scale bar 10 km or 2 km
    sb=10000 if (bounds[2]-bounds[0])>40000 else 2000; L=sb/res
    sx=W-L-30*k; sy=H-30*k
    d.rectangle((sx-10*k,sy-34*k,sx+L+10*k,H-8*k),fill=(0,0,0)); d.line([(sx,sy),(sx+L,sy)],fill='white',width=max(3,int(4*k)))
    d.text((sx+L/2,sy-6*k),f'{sb//1000} km',font=Fs,fill='white',anchor='md')
    if title:
        d.rectangle((0,0,W,int(30*k)),fill=(0,0,0)); d.text((10*k,6*k),title,font=Fs,fill='white')
    im.save(out,quality=90)
    v=s[valid]; return dict(le8=float((v<=8).mean()*100),b8_15=float(((v>8)&(v<=15)).mean()*100),b15_20=float(((v>15)&(v<=20)).mean()*100),gt20=float((v>20).mean()*100),px=valid.size,valid=int(valid.sum()),le15=float((v<=15).mean()*100),p50=float(np.median(v)),p95=float(np.percentile(v,95)),max=float(v.max()))
