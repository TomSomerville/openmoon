# Sunlight and VSAT locations (M00)

`mk_sun.py ILLUM_TIF ROI_DIR assets/sites` builds `focus-sunlight-raw.jpg` and `focus-vsat-candidates.jpg`,
and writes `vsat_spots.csv` (best sunlit 60 m pixel in each 1 km cell with ≥70 % sunlight and slope ≤15°).

Data:
- Average solar illumination, 18.6-year mean, ground level, 85–90°S at 60 m/px: `AVGVISIB_85S_060M_201608.TIF`
  from NASA GSFC PGDA [product 69](https://pgda.gsfc.nasa.gov/products/69) (cite Mazarico et al. 2011, Icarus 211).
  Stored as int16; multiply by 4e-5 for the fraction of time sunlit.
- NASA's best-lit regions of interest (ROI shapefiles) for Sites 01, 04, 07 and 11 from
  [product 78](https://pgda.gsfc.nasa.gov/products/78) (Barker et al.).
- Slope: LOLA LDSM via `../slope/read.py`.

Plan design: VSAT sites = sunlit ≥70 % at ground level and slope ≤15° (NASA's VSAT terrain-slope goal
with a 10 m mast). Ground-level sunlight understates what a 10 m mast sees.
