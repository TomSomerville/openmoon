# Slope maps for site selection (M00)

Reproduces the slope images in `assets/sites/` from NASA Goddard's LOLA slope
map (LDSM_83S_10MPP_ADJ) and hillshade (LDEM_83S_10MPP_ADJ_HILL), product page
https://pgda.gsfc.nasa.gov/products/90 (cite Barker et al. 2023, doi:10.3847/PSJ/acf3e1).

- `read.py` reads only the needed window over HTTP, tile by tile, retrying empty tiles.
- `render.py` colours slope in four classes: ≤8° green, 8–15° yellow, 15–20° orange, ≥20° red (threshold_mode="classes").

Requires `pip install rasterio pillow numpy`. Box positions come from NASA's
Oct 2024 nine-region map (pole marker and 50 km scale bar), so they are approximate.
