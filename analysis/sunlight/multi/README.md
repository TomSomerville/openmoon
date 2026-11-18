# Multiple VSAT placements (ESTIMATE)

Open Moon's own calculation, used on the M00 page "Multiple VSAT placements".

1. `get_dem.py` reads NASA LOLA `LDEM_83S_10MPP_ADJ` at 80 m (whole tile) and 20 m (focus area); the 20 m grid is
   block-averaged to 60 m for the near field.
2. `horizon_sun.py` holds the horizon tracer (720 directions, out to 210 km, lunar curvature) and Sun directions every
   2 h for 18.6 years from NAIF kernels `de421.bsp`, `moon_pa_de421_1900-2050.bpc`, `moon_080317.tf` (frame MOON_ME_DE421).
   Ground-level check: at 60 random points it matches NASA GSFC's AVGVISIB_85S_060M map, mean −1.6 points, RMS 2.2, r = 0.99.
3. `rim_pairs.py` (de Gerlache rim, 1,172 spots) and `focus_series.py` (691 spots: best spot in each 1 km cell with
   ≥50 % sunlight at ground level) store each spot's lit/dark time series ("lit" = at least half the Sun's disc above the horizon).
4. `vsat_sets.py` picks the best 1–4 spots greedily by combined sunlight (time at least one spot is lit), with no limit and
   with DD-013 (all spots within 3 km straight line of one PMC). Results: `vsat_sets.json`. `mk_sets.py` draws the map.

All values are at ground level; a 10 m mast sees more sun.
