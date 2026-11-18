# Open Moon data cache

These files were downloaded or computed for the plan. They are kept here so that later work never has to download them again. They are not published on the website (excluded in `_config.yml`).

## Use

To rebuild the working-folder layout the analysis scripts expect:

```bash
python3 -I analysis/data_tools.py restore WORKDIR
```

After adding new downloads to a working folder, store them here:

```bash
python3 -I analysis/data_tools.py pack WORKDIR
```

`analysis/slope/read.py` also checks `data/lola_cache/` before reading NASA's servers, and saves every new window there.

## Contents

| Folder | What | Source |
|---|---|---|
| `lola/` | LOLA heights, 80 m / 60 m / 20 m grids (int16, 0.25 m steps, split into parts); Site 11 5 m DEM (de Gerlache rim) | NASA GSFC PGDA [product 90](https://pgda.gsfc.nasa.gov/products/90) (LDEM_83S), [product 78](https://pgda.gsfc.nasa.gov/products/78) (Site11_final_adj_5mpp_surf) |
| `lola_cache/` | Windows of LOLA slope (LDSM), height (LDEM) and hillshade read for the maps (slope in 0.01°, height in 0.25 m, hillshade 8-bit) | NASA GSFC PGDA [product 90](https://pgda.gsfc.nasa.gov/products/90) |
| `illum/` | Average solar illumination map, 60 m/px (AVGVISIB_85S_060M_201608), and best-lit regions-of-interest shapefiles | NASA GSFC PGDA [product 69](https://pgda.gsfc.nasa.gov/products/69), [product 78](https://pgda.gsfc.nasa.gov/products/78) |
| `psr/` | Permanently shadowed regions inside the focus area (from LPSR_80S_20MPP_ADJ) | NASA GSFC PGDA [product 90](https://pgda.gsfc.nasa.gov/products/90) |
| `lend/` | LRO LEND neutron data (raw ALDS products) and the focus-area hydrogen grids | NASA [PDS Geosciences Node](https://pds-geosciences.wustl.edu/missions/lro/lend.htm) |
| `lroc/` | LROC NAC maximum-pixel mosaic, 20 × 20 km, 2 m/px (lossless PNG + polar stereographic bounds): `nac_max` around the DD-020 point, `nac_max_D` around the current base (DD-023, in two halves) | NASA/GSFC/Arizona State University, [NASA PDS](https://pds.mcp.nasa.gov/data/index.html#/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/) |
| `sunlight/` | Open Moon 18.6-year sunlight series for 2,243 spots (packed bits: lit = at least half the Sun's disc above the horizon), the spots' positions, and Sun directions every 2 hours (ESTIMATE) | Open Moon model over LOLA terrain; Sun from the NAIF kernels below |
| `blender/` | "Cesium Man" 3D figure used for scale in the M00 renders (CesiumMan.glb, with its licence file), and the Blender and image scripts that built the scene and renders (`build.py`, `move_base.py`, `towers_dd024.py`, `tower_cam.py`, `recentre.py` for the terrain recentred on the DD-023 base, `label.ps1`). The scene file itself (84 MB) is not stored here. | Figure © 2017 Cesium, CC BY 4.0, [Khronos glTF Sample Assets](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/CesiumMan); terrain from `blender/primary-base` |
| `spice/` | de421.bsp, moon_pa_de421_1900-2050.bpc, moon_080317.tf | NASA/JPL [NAIF generic kernels](https://naif.jpl.nasa.gov/naif/data_generic.html) |

All files are under 100 MB (GitHub's limit); larger arrays are split by rows.
