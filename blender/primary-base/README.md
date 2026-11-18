# Primary base terrain for Blender (1:1 scale)

Terrain of the Open Moon primary base and the 10 km around it, at true size, ready to render in Blender.

- **Centre:** the primary base, 88.4365°S, 62.46°W (north rim of de Gerlache crater; moved here by design change DD-023).
- **Area:** 20 × 20 km, centred on the base.
- **Units:** metres. 1 Blender unit = 1 m.

## Files

| File | What it is |
|---|---|
| `heightmap_5m.tif` | Height in metres, 4000 × 4000 px at 5 m/px, float32 GeoTIFF (south polar stereographic). Best for the BlenderGIS add-on or GIS tools. |
| `heightmap_5m_16bit.png` | The same heights as a 16-bit greyscale PNG: black = lowest point, white = highest. Use it for a Displace modifier. |
| `heightmap_5m_curved.tif` | As `heightmap_5m.tif`, with the Moon's curvature applied. The ground drops 28.8 m at the middle of each edge and 57.6 m at the corners, relative to the centre (this plan's arithmetic). Use it for long, low views to the horizon. |
| `mesh_20m.ply` | Ready-made mesh: 1000 × 1000 vertices at 20 m spacing, with UVs. Z = height above the lowest point. |
| `texture_2m.jpg` | Colour texture: 10000 × 10000 px at 2 m/px, from LROC's maximum-pixel mosaic, which shows each spot at its brightest so most shadows are removed. |
| `texture_4k.jpg` | The same texture at 4096 × 4096, for quick previews. |
| `source_mask.png` | Where the 5 m heights came from (white) and where the 10 m heights were used (grey). |
| `info.json` | Exact bounds, height range and the other numbers below. |

## Key numbers

| | Value |
|---|---|
| Size | 20,000 × 20,000 m |
| Lowest point | −1,786.5 m |
| Highest point | +1,815.0 m |
| Height range (Displace strength) | **3,601.5 m** |
| Base height above the lowest point | 2,823.5 m |

The heights are relative to a 1,737.4 km lunar sphere.

## Option 1: import the mesh (fastest)

1. **File → Import → Stanford PLY**, choose `mesh_20m.ply`. The terrain is centred on the origin: X is east and Y is north in the map grid, and Z is up.
2. Add a material. In the Shader Editor, connect an **Image Texture** node with `texture_2m.jpg` to Base Color, using the mesh's UV map.
3. If the texture appears flipped, set the Image Texture's projection mapping to flip in Y. The image's top edge is the terrain's +Y edge.

## Option 2: Displace modifier (full 5 m detail)

1. **Add → Mesh → Plane**, then in the N panel set the dimensions to **20000 m × 20000 m**.
2. Add a **Subdivision Surface** modifier (Simple), or subdivide in Edit Mode. About 2000 × 2000 faces gives 10 m detail; 4000 × 4000 gives the full 5 m. In Cycles you can turn on Adaptive Subdivision instead.
3. Add a **Displace** modifier:
   - Texture: `heightmap_5m_16bit.png`, colour space **Non-Color**.
   - Texture coordinates: **UV**.
   - Strength: **3601.5**.
   - Midlevel: **0**.
4. Give the plane a material with `texture_2m.jpg` on its UVs.

## Option 3: BlenderGIS add-on

Import `heightmap_5m.tif` (or `heightmap_5m_curved.tif`) as a DEM. Heights come in at true metres.

## Lighting the scene

The Sun is always low here. The maximum Sun elevation at this latitude is about 3° (colatitude 1.57° plus the Sun's maximum declination of about 1.54°; this plan's arithmetic).

- Use a Sun lamp at 1–3° elevation for realistic light.
- There is no air, so turn off atmosphere and haze, and use a black background.

## Sources and credit

- **Heights, 5 m/px:** NASA GSFC, LOLA high-resolution topography for lunar south pole sites, Site 11 (de Gerlache rim). [PGDA product 78](https://pgda.gsfc.nasa.gov/products/78). Used for 35.9% of the area. Its median offset from the 10 m data is 0.95 m, which is removed before blending.
- **Heights, 10 m/px:** NASA GSFC, LOLA LDEM_83S_10MPP_ADJ (Barker et al. 2023). [PGDA product 90](https://pgda.gsfc.nasa.gov/products/90). Resampled to 5 m and feathered over 500 m into the 5 m data.
- **Texture:** LROC NAC south-pole maximum-pixel mosaic, tiles P878S2925 and P892S3150, 1 m/px, averaged to 2 m/px. Credit NASA/GSFC/Arizona State University. [NASA PDS](https://pds.mcp.nasa.gov/data/index.html#/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/).
- **Processing:** Open Moon. Scripts are in `analysis/blender/` (`make_heightmap.py`, `fetch_nac.py`, `make_texture.py`).

## Limits

- Boulders and craters smaller than about 5–10 m are not in the heights. The 1 m photo texture shows some of them visually.
- Black areas in the texture were in shadow in every photo LROC took.
