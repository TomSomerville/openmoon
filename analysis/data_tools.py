"""Keep downloaded and derived data in the repository (data/) so nothing has to be downloaded again.

    python3 -I analysis/data_tools.py pack WORKDIR      # copy a working folder's data into data/ (compact formats)
    python3 -I analysis/data_tools.py restore WORKDIR   # rebuild the working-folder layout the analysis scripts expect

WORKDIR layout (what the scripts read, relative to their working folder):
  sun10/  dem20.npy dem60.npy dem80.npy (+_bounds), {focus,rim,near3}_pts.npy, {focus,rim,near3}_series.npy,
          sun_me.npy, cands.npy, anim_sun_*.npy, anim_t_*.txt, SPICE kernels
  slope/  cache_*.npy (LOLA windows), focus_S.npy, focus_Z.npy
  psr/psr_focus.pkl   lola5/Site11_surf.tif   illum/   lend/   nac_max*/full.npy + bounds.npy
Formats in data/: heights int16 in 0.25 m, slope int16 in 0.01 deg, hillshade uint8, sunlit series as packed bits
(lit = at least half the Sun's disc above the horizon), mosaics as lossless PNG. Files are kept under 95 MB
(GitHub's limit is 100 MB); larger arrays are split by rows."""
import os, sys, glob, shutil, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'slope'))
from read import pack as pack_window, unpack as unpack_window
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
LIMIT = 48e6   # GitHub recommends files under 50 MB
COPY = [('sun10/sun_me.npy', 'sunlight'), ('sun10/cands.npy', 'sunlight'), ('sun10/de421.bsp', 'spice'),
        ('sun10/moon_pa_de421_1900-2050.bpc', 'spice'), ('sun10/moon_080317.tf', 'spice'),
        ('sun10/dem20_bounds.npy', 'lola'), ('sun10/dem60_bounds.npy', 'lola'),
        ('slope/focus_S.npy', 'lend'), ('slope/focus_Z.npy', 'lend'), ('psr/psr_focus.pkl', 'psr'),
        ('lola5/Site11_surf.tif', 'lola'), ('illum/AVGVISIB_85S_060M_201608.TIF', 'illum')]
def save_split(arr, base):
    """save an int array compressed, split into row chunks so each file stays under LIMIT"""
    for f in glob.glob(base + '.part*.npz'): os.remove(f)
    n = 1
    while True:
        rows = np.array_split(np.arange(arr.shape[0]), n); ok = True
        for i, r in enumerate(rows):
            np.savez_compressed('%s.part%d.npz' % (base, i), q=arr[r[0]:r[-1] + 1])
            if os.path.getsize('%s.part%d.npz' % (base, i)) > LIMIT: ok = False
        if ok: return n
        for f in glob.glob(base + '.part*.npz'): os.remove(f)
        n += 1
def load_split(base):
    return np.concatenate([np.load(f)['q'] for f in sorted(glob.glob(base + '.part*.npz'), key=lambda s: int(s.split('.part')[1].split('.')[0]))])
def pack(W):
    for sub in ('lola', 'lola_cache', 'sunlight', 'spice', 'lend', 'psr', 'illum', 'lroc'): os.makedirs(os.path.join(DATA, sub), exist_ok=True)
    for src, dst in COPY:
        p = os.path.join(W, src)
        if os.path.exists(p): shutil.copy2(p, os.path.join(DATA, dst, os.path.basename(p)))
    for f in glob.glob(os.path.join(W, 'illum', '*')):
        if os.path.isfile(f) and not f.endswith('.TIF'): shutil.copy2(f, os.path.join(DATA, 'illum', os.path.basename(f)))
    if os.path.isdir(os.path.join(W, 'lend')): shutil.copytree(os.path.join(W, 'lend'), os.path.join(DATA, 'lend', 'raw'), dirs_exist_ok=True)
    for f in glob.glob(os.path.join(W, 'sun10', 'anim_*')): shutil.copy2(f, os.path.join(DATA, 'sunlight', os.path.basename(f)))
    for g in ('dem20', 'dem60', 'dem80'):
        p = os.path.join(W, 'sun10', g + '.npy')
        if os.path.exists(p):
            a = np.load(p); q = np.round(np.nan_to_num(a) * 4).astype('int16'); q[~np.isfinite(a)] = -32768
            print(g, 'parts', save_split(q, os.path.join(DATA, 'lola', g)), flush=True)
    for nm in ('focus', 'rim', 'near3'):
        pts = os.path.join(W, 'sun10', nm + '_pts.npy'); ser = os.path.join(W, 'sun10', nm + '_series.npy')
        if os.path.exists(ser):
            s = np.load(ser, mmap_mode='r'); bits = np.packbits(np.asarray(s) >= 0.5, axis=1)
            np.savez_compressed(os.path.join(DATA, 'sunlight', nm + '_lit_bits.npz'), bits=bits, n=s.shape[1])
            shutil.copy2(pts, os.path.join(DATA, 'sunlight', nm + '_pts.npy')); print(nm, 'series packed', flush=True)
    for d in ('slope', 'sun10'):
        for f in glob.glob(os.path.join(W, d, 'cache_*.npy')):
            out = os.path.join(DATA, 'lola_cache', os.path.basename(f)[:-4] + '.npz')
            if not os.path.exists(out): pack_window(np.load(f), out)
    for d in glob.glob(os.path.join(W, 'nac_max*')):
        if os.path.exists(os.path.join(d, 'full.npy')):
            od = os.path.join(DATA, 'lroc', os.path.basename(d)); os.makedirs(od, exist_ok=True)
            Image.fromarray(np.load(os.path.join(d, 'full.npy'))).save(os.path.join(od, 'full.png'), optimize=True)
            shutil.copy2(os.path.join(d, 'bounds.npy'), os.path.join(od, 'bounds.npy')); print(d, 'mosaic saved', flush=True)
    tot = sum(os.path.getsize(f) for f in glob.glob(os.path.join(DATA, '**', '*'), recursive=True) if os.path.isfile(f))
    big = [f for f in glob.glob(os.path.join(DATA, '**', '*'), recursive=True) if os.path.isfile(f) and os.path.getsize(f) > LIMIT]
    print('data/ total %.0f MB; files over limit: %s' % (tot / 1e6, big))
def restore(W):
    for sub in ('sun10', 'slope', 'psr', 'lola5', 'illum', 'lend'): os.makedirs(os.path.join(W, sub), exist_ok=True)
    for src, dst in COPY:
        p = os.path.join(DATA, dst, os.path.basename(src))
        if os.path.exists(p): shutil.copy2(p, os.path.join(W, src))
    for f in glob.glob(os.path.join(DATA, 'illum', '*')): shutil.copy2(f, os.path.join(W, 'illum', os.path.basename(f)))
    if os.path.isdir(os.path.join(DATA, 'lend', 'raw')): shutil.copytree(os.path.join(DATA, 'lend', 'raw'), os.path.join(W, 'lend'), dirs_exist_ok=True)
    for f in glob.glob(os.path.join(DATA, 'sunlight', 'anim_*')): shutil.copy2(f, os.path.join(W, 'sun10', os.path.basename(f)))
    for g in ('dem20', 'dem60', 'dem80'):
        if glob.glob(os.path.join(DATA, 'lola', g + '.part*.npz')):
            q = load_split(os.path.join(DATA, 'lola', g)); a = q.astype('float32') / 4; a[q == -32768] = np.nan
            np.save(os.path.join(W, 'sun10', g + '.npy'), a)
    for nm in ('focus', 'rim', 'near3'):
        z = os.path.join(DATA, 'sunlight', nm + '_lit_bits.npz')
        if os.path.exists(z):
            d = np.load(z); np.save(os.path.join(W, 'sun10', nm + '_series.npy'), np.unpackbits(d['bits'], axis=1)[:, :int(d['n'])].astype('uint8'))
            shutil.copy2(os.path.join(DATA, 'sunlight', nm + '_pts.npy'), os.path.join(W, 'sun10', nm + '_pts.npy'))
    for f in glob.glob(os.path.join(DATA, 'lola_cache', 'cache_*.npz')):
        a = unpack_window(f)
        for d in ('slope', 'sun10'): np.save(os.path.join(W, d, os.path.basename(f)[:-4] + '.npy'), a)
    for d in glob.glob(os.path.join(DATA, 'lroc', 'nac_max*')):
        od = os.path.join(W, os.path.basename(d)); os.makedirs(od, exist_ok=True)
        np.save(os.path.join(od, 'full.npy'), np.array(Image.open(os.path.join(d, 'full.png')))); shutil.copy2(os.path.join(d, 'bounds.npy'), os.path.join(od, 'bounds.npy'))
    print('restored into', W)
if __name__ == '__main__':
    {'pack': pack, 'restore': restore}[sys.argv[1]](sys.argv[2])
