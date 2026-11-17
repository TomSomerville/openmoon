---
slug: chandrayaan-2-orbiter-dfsar-radar
title: "Chandrayaan-2 orbiter DFSAR radar"
alternatives:
  - {name: "LRO Mini-RF (NASA)", compare: "S-band radar at 30 m per pixel on NASA's Lunar Reconnaissance Orbiter. It covers the same polar craters, but at one shorter wavelength it sees less deep, and its transmitter failed in January 2011, so it now works only in bistatic mode with Earth-based transmitters.", status: "Receiver still operating on LRO; monostatic imaging ended in 2011", url: "https://en.wikipedia.org/wiki/Mini-RF"}
  - {name: "Chandrayaan-1 Mini-SAR", compare: "DFSAR's S-band-only predecessor (2.5 GHz, about 150 m resolution). It mapped both poles and flagged over 40 north-polar craters with high CPR, but has no L-band, no full polarimetry and much coarser pixels.", status: "Mission lost in August 2009 after 312 days; archive data only", url: "https://en.wikipedia.org/wiki/Chandrayaan-1"}
  - {name: "ShadowCam on KPLO/Danuri", compare: "Optical camera that images surface frost inside shadowed craters using light scattered from sunlit rims. It sees only the top surface, not metres down, but gives a direct, sharp picture with no roughness ambiguity.", status: "Operating in extended mission", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/"}
  - {name: "Orbital neutron spectroscopy (LRO LEND)", compare: "Measures hydrogen in roughly the top metre from neutron counts. It detects hydrogen rather than ice itself, and its maps are much coarser than radar images, so it cannot pick a drill site alone.", status: "Flying on LRO", url: "https://en.wikipedia.org/wiki/Lunar_Reconnaissance_Orbiter"}
links:
  - {title: "ISRO: Chandrayaan-2 DFSAR observations reveal subsurface ice in lunar south polar regions", url: "https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html", kind: official, date: "May 2026"}
  - {title: "ISRO: Advanced DFSAR data products for the lunar polar regions", url: "https://www.isro.gov.in/Lunar_Polar_Region.html", kind: official, date: "Nov 2025"}
  - {title: "ISRO: Chandrayaan-2 science payloads (DFSAR description)", url: "https://www.isro.gov.in/Chandrayaan2_science.html", kind: official, date: ""}
  - {title: "ISRO: Chandrayaan-2 orbiter payload list", url: "https://www.isro.gov.in/chandrayaan2-payloads.html", kind: official, date: ""}
  - {title: "Sinha et al., Subsurface ice in doubly shadowed craters as revealed by Chandrayaan-2 DFSAR (npj Space Exploration)", url: "https://doi.org/10.1038/s44453-026-00038-9", kind: paper, date: "May 2026"}
  - {title: "McVann et al., Anomalous craters at the lunar south pole imaged using Chandrayaan-2 DFSAR (LPSC 2025)", url: "https://www.hou.usra.edu/meetings/lpsc2025/pdf/1580.pdf", kind: paper, date: "Mar 2025"}
  - {title: "ISSDC PRADAN: Chandrayaan-2 DFSAR data archive", url: "https://pradan.issdc.gov.in/ch2/protected/browse.xhtml?id=sar", kind: data, date: ""}
  - {title: "ISSDC Chandrayaan-2 MapBrowse (polar mosaic viewer)", url: "https://chmapbrowse.issdc.gov.in/MapBrowse/", kind: data, date: ""}
  - {title: "Chandrayaan-2, Wikipedia", url: "https://en.wikipedia.org/wiki/Chandrayaan-2", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Lunar water, Wikipedia", url: "https://en.wikipedia.org/wiki/Lunar_water", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Mini-RF, Wikipedia", url: "https://en.wikipedia.org/wiki/Mini-RF", kind: wiki, date: "accessed Nov 2026"}
  - {title: "NASA NTRS 20250011660: Artemis III Site Selection Update", url: "https://ntrs.nasa.gov/citations/20250011660", kind: official, date: "2026"}
---

## What it is

The Dual Frequency Synthetic Aperture Radar (DFSAR) is an imaging radar on India's Chandrayaan-2 orbiter. It works in two microwave bands, L and S, and is [the first fully polarimetric SAR to study the Moon](https://www.isro.gov.in/Chandrayaan2_science.html). It was built by ISRO's [Space Applications Centre (SAC) in Ahmedabad](https://en.wikipedia.org/wiki/Chandrayaan-2). An independent team calls Chandrayaan-2 [the first L-band planetary mission](https://www.hou.usra.edu/meetings/lpsc2025/pdf/1580.pdf).

Chandrayaan-2 launched on [22 July 2019 and reached lunar orbit on 20 August 2019](https://en.wikipedia.org/wiki/Chandrayaan-2). The Vikram lander crashed, but the orbiter kept working, and its planned life was [extended from one year to about 7.5 years](https://en.wikipedia.org/wiki/Chandrayaan-2). By November 2025, [about 1,400 DFSAR datasets](https://www.isro.gov.in/Lunar_Polar_Region.html) had been turned into polar mosaics from 80 to 90 degrees latitude, north and south. ISRO released them free as [Level 3C products](https://www.isro.gov.in/Lunar_Polar_Region.html) on the [PRADAN archive](https://pradan.issdc.gov.in/ch2/protected/browse.xhtml?id=sar).

In May 2026, scientists at the Physical Research Laboratory reported [radar signs of possible subsurface ice under four doubly shadowed craters](https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html) near the south pole. They looked at [nine such craters inside Faustini, Haworth and Shoemaker](https://doi.org/10.1038/s44453-026-00038-9). The strongest case is a [1.1 km crater inside Faustini](https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html) with a lobate, flow-like rim.

## Why Open Moon uses it

Open Moon needs to land near ice it can actually dig. Cameras see only the surface. DFSAR's L-band sees [about 5 m down, twice as deep as S-band](https://www.isro.gov.in/chandrayaan2-payloads.html), so it is one of the few orbital tools that hints at buried ice.

In **M00 (site selection)**, DFSAR polar mosaics go into the open site database next to LRO and ShadowCam data. They help rank ice targets inside and near candidate regions. Haworth, one of the craters in the 2026 study, is also on [NASA's Artemis III region list](https://ntrs.nasa.gov/citations/20250011660). The radar results then point **M01** prospecting at the best places to check on the ground.

Without DFSAR, the plan would lean on older S-band data and neutron maps. Those either see shallower or blur over kilometres, so the risk of drilling in a dry spot would rise.

## How it works

DFSAR is [two SAR systems, L and S band, sharing one wide-band antenna](https://www.isro.gov.in/Chandrayaan2_science.html). It sends radar pulses sideways from orbit and builds a sharp image as the spacecraft moves. In full-polarimetric mode it [sends and receives in both vertical and horizontal polarisations](https://www.isro.gov.in/Lunar_Polar_Region.html).

The key test for ice is how the echo's polarisation changes. Ice buried in regolith scatters radar many times, which raises the **circular polarization ratio (CPR)**. But rough, rocky ground does that too. The 2026 study adds a second test: [CPR above 1 together with a degree of polarization (DOP) below 0.13](https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html) points to volume scattering from ice, not rocks.

| Specification | Value |
|---|---|
| Bands | L and S ([ISRO](https://www.isro.gov.in/Chandrayaan2_science.html)) |
| Exact centre frequencies | Not given on ISRO's public pages |
| Polarimetry | Circular and full ([ISRO](https://www.isro.gov.in/chandrayaan2-payloads.html)) |
| Resolution options | 2-75 m ([ISRO](https://www.isro.gov.in/chandrayaan2-payloads.html)) |
| Best resolution | 2 m slant range, about ten times better than earlier lunar SARs ([ISRO](https://www.isro.gov.in/Chandrayaan2_science.html)) |
| Incidence angles | 9-35 degrees ([ISRO](https://www.isro.gov.in/chandrayaan2-payloads.html)) |
| L-band penetration | About 5 m ([ISRO](https://www.isro.gov.in/chandrayaan2-payloads.html)) |
| Polar mosaic pixel | 25 m, full-pol L-band ([ISRO](https://www.isro.gov.in/Lunar_Polar_Region.html)) |
| Orbit | About 100 km circular ([Wikipedia](https://en.wikipedia.org/wiki/Chandrayaan-2)) |

Polar mosaics include CPR, a roughness measure (SERD), a T-ratio linked to dielectric constant, and scattering decompositions. Users can view them in [CH2 MapBrowse](https://chmapbrowse.issdc.gov.in/MapBrowse/).

## Limitations and open issues

- **Radar evidence is indirect.** High CPR [is not uniquely diagnostic of either roughness or ice](https://en.wikipedia.org/wiki/Lunar_water). The new CPR plus DOP test helps, but the 2026 result is still described as [possible](https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html) ice. Only ground truth can confirm it.
- **Thick ice only.** Radar ice signatures need [relatively pure ice at least a couple of metres thick](https://en.wikipedia.org/wiki/Lunar_water). Radar of the LCROSS impact site in Cabeus suggested [ice there is in small pieces mixed through the regolith](https://en.wikipedia.org/wiki/Lunar_water), which radar may miss.
- **No ice amount.** Quantitative water-ice estimation is a [stated objective](https://www.isro.gov.in/Chandrayaan2_science.html), but this research found no published DFSAR ice-concentration map.
- **Small, scattered targets.** The positive craters are about a kilometre across and sit in [~25 K doubly shadowed terrain](https://doi.org/10.1038/s44453-026-00038-9). Landing or driving there is very hard.
- **Coverage gaps.** Many polar shadowed craters [have not been studied in detail](https://www.hou.usra.edu/meetings/lpsc2025/pdf/1580.pdf) for lack of high-resolution, fully polarimetric coverage.
- **Ageing spacecraft.** The orbiter is past seven years in orbit, close to its [~7.5-year planned life](https://en.wikipedia.org/wiki/Chandrayaan-2). No end date or follow-on L-band lunar radar is confirmed.
