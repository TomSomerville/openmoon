# Base site search (ESTIMATE)

Open Moon's search of the focus area (~180 × 130 km around the south pole) for base sites. Not yet adopted in the plan.

- `pairs.py`: every pair of candidate VSAT spots up to 20 km apart (2,000+ spots from `analysis/sunlight/multi`), with combined sunlight and the longest time both are dark (ground level, 2-hour steps, 18.6 years).
- `ground.py`: NASA LOLA slope (40 m), share of ground ≤8° within 1 km, largest all-≤8° circle, distance to the Shackleton and de Gerlache ice-candidate floors (NASA GSFC LPSR), LEND neutron dip.
- `score.py`: base points every 400 m on ground ≤8°, off the ice floors, with a flat circle at least 300 m across. A site qualifies only if a tower pair, each tower ≤10 km away (DD-014), keeps shared darkness ≤7 days. The score (plan design) weights the longest cable 0.3, ice distance 0.3, flat ground 0.3 and hydrogen 0.1. Sites closer than 5 km are merged.
- `mk_map.py` → `map.jpg`; results in `results.json`.

Limits: spots below 30 % sunlight, and spots below 50 % outside the de Gerlache rim and the primary area, are not in the tower set, so some complementary towers may be missed. Pairs only (no trios). Routes from base to ice are not checked.
