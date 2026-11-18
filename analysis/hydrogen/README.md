# Hydrogen map (M00)

Builds `assets/sites/focus-landing-hydrogen.jpg` and `assets/sites/south-pole-lend-hydrogen.jpg`.

Data: NASA LRO LEND averaged south-polar products (ALDS, 2009-09-15 to 2016-09-14) from the
[PDS Geosciences Node](https://pds-geosciences.wustl.edu/missions/lro/lend.htm). Hydrogen in the top ~1 m lowers the
flux of epithermal neutrons leaving the surface; we use the collimated sensors (CSETN).

Method (Open Moon processing, not a NASA product):
1. `prep_lend.py`: combine the two periods per 0.5° cell (inverse-variance weighted).
2. `hydro.py`: Gaussian smoothing with σ = 10 km; neutron dip = 1 − rate / median rate at 80–84°S; significance z = dip / standard error.
3. "High hydrogen" = dip ≥ 1.28 % (the top 10 % of smoothed cells south of 84°S) **and** z ≥ 3.
4. `mk_lh.py`: overlays high hydrogen (blue) on LOLA slope ≤ 8° (green).

Limits: LEND cells are 0.5° (~15 km); smoothing blurs further, so blue areas show regions, not individual craters.
A neutron dip shows hydrogen, not its form (ice, solar-wind hydrogen or hydrated minerals). For NASA's own
calibrated water-equivalent map see Sanin et al. 2017 (Icarus 283).

## Ice candidates (`mk_lhi.py`)

Adds ice candidates in blue and switches hydrogen to purple. Ice candidates are the permanently shadowed regions
from NASA GSFC's LPSR product (`LPSR_80S_20MPP_ADJ.SHP`, [PGDA product 90](https://pgda.gsfc.nasa.gov/products/90))
inside Shackleton and de Gerlache, where published ice detections are reported (Li et al. 2018; Li et al. 2026),
plus the ShadowCam high-reflectance spot at 88.5352°S, 97.4007°W. Other shadowed regions are outlined only.
`psr_focus.pkl` is built by filtering the shapefile to the focus-area bounding box with pyshp.
