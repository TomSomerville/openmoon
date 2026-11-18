# Multiple VSAT placements (ESTIMATE)

Open Moon's own calculation, used on the M00 page "Multiple VSAT placements".

1. `get_dem.py` reads NASA LOLA `LDEM_83S_10MPP_ADJ` at 80 m (whole tile) and 20 m (focus area); the 20 m grid is
   block-averaged to 60 m for the near field.
2. `horizon_sun.py` holds the horizon tracer (720 directions, out to 210 km, lunar curvature) and Sun directions every
   2 h for 18.6 years from NAIF kernels `de421.bsp`, `moon_pa_de421_1900-2050.bpc`, `moon_080317.tf` (frame MOON_ME_DE421).
   Ground-level check: at 60 random points it matches NASA GSFC's AVGVISIB_85S_060M map, mean −1.6 points, RMS 2.2, r = 0.99.
3. `rim_pairs.py` (de Gerlache rim, 1,172 spots) and `focus_series.py` (691 spots: best spot in each 1 km cell with
   ≥50 % sunlight at ground level) store each spot's lit/dark time series ("lit" = at least half the Sun's disc above the horizon).
4. de Gerlache rim near site 5 (88.6652°S, 68.42°W), best 1–4 VSATs by combined sunlight (time at least one spot is lit):
   best pair by exhaustive search, then the best 3rd and 4th spot.
   - `dg_sets3.py`: option 1, base/PMC at site 5, spots within 10 km (DD-014), and the old 3 km rule for comparison → `dg_sets.json`.
   - `dg_sets4.py` (uses `dg_sets2.py`): option 2, PMC anywhere, all spots within a 10 km circle (up to 20 km apart) → `dg_sets_span20.json`.
   - `mk_dg_sets.py` draws `assets/sites/de-gerlache-vsat-sets.jpg`.

All values are at ground level; a 10 m mast sees more sun.
5. `vsat_sets.py` → `vsat_sets.json`: best 1–4 VSAT sets across the whole focus area (set A within 3 km of one PMC, on the Connecting ridge; set B with no limit). `mk_sets.py` draws `assets/sites/focus-vsat-sets.jpg`.
