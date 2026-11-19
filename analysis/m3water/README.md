# M3 surface water around the primary base (M01)

Builds `assets/milestones/m3-water-base-10km.jpg` and `data/m3water/stats_10km.json`.

Data: Li et al. 2023 Moon Mineralogy Mapper (M3) water maps, USGS PDS4 archive
([Astropedia page](https://astrogeology.usgs.gov/search/map/lunar_m3_water_map_pds4_archive), doi:10.17189/gmce-w279).
Six global maps in simple cylindrical projection (~280 m per pixel), one per period of the Moon's orbit through
Earth's magnetotail. Water is OH plus H2O in the top ~1 mm, from the 3 µm band: ppm = 5000 × ESPAT, ±20%.

1. `read_m3.py` reads a window (80–45°W, 87.6–89.2°S) from each map over HTTP and saves it to `data/m3water/`.
2. `mk_m3.py` resamples to the LOLA polar stereographic grid, averages the maps per pixel, takes statistics inside
   10 km of the base (88.4365°S, 62.46°W), and draws the map over LOLA slope (PGDA product 90).

Open Moon choices (not from the archive):
- Values below −1e30 are fill.
- 47% of pixels in the window are exactly 20 ppm. The archive does not explain this value; it is treated as no data.
  If those pixels are real low readings, the median within 10 km falls from ~260 ppm to ~34 ppm.
- The display smooths water over ~300 m (about one M3 pixel) and slope over 100 m; statistics use unsmoothed values.
