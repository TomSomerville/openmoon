---
slug: lunar-reconnaissance-orbiter-lro
title: "Lunar Reconnaissance Orbiter (LRO)"
alternatives:
  - {name: "ShadowCam on KPLO/Danuri", compare: "A NASA camera on Korea's Danuri orbiter, built from the LROC Narrow Angle Camera design but about 200 times more sensitive, so it can image inside permanently shadowed craters that LROC cannot see well. It complements LRO rather than replacing it: it is one camera, with no laser altimeter, thermal radiometer or radar.", status: "Operating; team released new data to the Planetary Data System in Aug 2026", url: "https://www.shadowcam.asu.edu/"}
  - {name: "Chandrayaan-2 orbiter (OHRC, TMC-2, DFSAR)", compare: "India's polar orbiter carries a 0.32 m high-resolution camera, a stereo terrain camera for elevation models and a dual-frequency radar that can probe for buried ice. It covers many of LRO's jobs, but its data are less widely used in US/Artemis planning tools and it has no laser altimeter.", status: "Operating in lunar orbit since Aug 2019", url: "https://www.isro.gov.in/Chandrayaan2_science.html"}
  - {name: "SELENE/Kaguya archive data (JAXA)", compare: "Japan's 2007-2009 orbiter carried a terrain camera, laser altimeter and radar sounder. Its archived data are free and useful for cross-checking LRO, but nothing new can be collected and its resolution is coarser than LROC NAC and LOLA at the poles.", status: "Mission ended with a planned impact in Jun 2009; data archived at JAXA DARTS", url: "https://darts.isas.jaxa.jp/planet/pdap/selene/"}
  - {name: "Chang'e 2 global maps (CNSA)", compare: "China's orbiter produced a global image map at 7 m resolution and elevation models at 20 m and 50 m, free to download since 2018. Good for a global baseline, but far coarser than LRO for landing-hazard mapping and no longer collecting.", status: "Left lunar orbit in 2011; archive data only", url: "https://en.wikipedia.org/wiki/Chang%27e_2"}
links:
  - {title: "NASA Science: Lunar Reconnaissance Orbiter mission page", url: "https://science.nasa.gov/mission/lro/", kind: official, date: "Oct 2026"}
  - {title: "NASA FY2026 Budget Technical Supplement (LRO, PS-24 and PS-28/29)", url: "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf", kind: official, date: "May 2025"}
  - {title: "Vondrak et al.: Lunar Reconnaissance Orbiter (LRO): Observations for Lunar Exploration and Science (NTRS 20110013489)", url: "https://ntrs.nasa.gov/citations/20110013489", kind: paper, date: "Feb 2010"}
  - {title: "LROC: About LROC and LRO (cameras, data volume)", url: "https://www.lroc.asu.edu/about", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA: NASA's LRO Moves Closer to the Lunar Surface", url: "https://www.nasa.gov/feature/goddard/nasas-lro-moves-closer-to-the-lunar-surface", kind: official, date: "May 2015"}
  - {title: "NASA: Teaching an Old Spacecraft New Tricks to Continue Exploring the Moon", url: "https://www.nasa.gov/missions/teaching-an-old-spacecraft-new-tricks-to-continue-exploring-the-moon/", kind: official, date: "Feb 2021"}
  - {title: "Deboeck et al.: Control of the LRO Reaction Wheel Angular Momentum Using Attitude Slews (NTRS 20240009215)", url: "https://ntrs.nasa.gov/citations/20240009215", kind: paper, date: "Jul 2024"}
  - {title: "Mazarico et al.: Orbit Determination of the Lunar Reconnaissance Orbiter: Status After Seven Years (NTRS 20180007208)", url: "https://ntrs.nasa.gov/citations/20180007208", kind: paper, date: "Oct 2017"}
  - {title: "LROC: Islands in the Dark (Shackleton-de Gerlache ridge illumination)", url: "https://www.lroc.asu.edu/images/1105", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA PGDA: A New View of the Lunar South Pole from LOLA (polar elevation and slope maps)", url: "https://pgda.gsfc.nasa.gov/products/90", kind: data, date: "accessed Nov 2026"}
  - {title: "PDS Geosciences Node: LRO data archive (Diviner, LEND, LOLA, Mini-RF)", url: "https://pds-geosciences.wustl.edu/missions/lro/default.htm", kind: data, date: "accessed Nov 2026"}
  - {title: "LROC Lunar QuickMap (browser GIS of LRO data)", url: "https://quickmap.lroc.asu.edu/", kind: data, date: "accessed Nov 2026"}
  - {title: "Wikipedia: Lunar Reconnaissance Orbiter", url: "https://en.wikipedia.org/wiki/Lunar_Reconnaissance_Orbiter", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Wikipedia: Mini-RF", url: "https://en.wikipedia.org/wiki/Mini-RF", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Wikipedia: Diviner (radiometer)", url: "https://en.wikipedia.org/wiki/Diviner_%28radiometer%29", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

The Lunar Reconnaissance Orbiter (LRO) is a NASA robotic spacecraft that has orbited the Moon since 2009. It was built and is run by NASA's Goddard Space Flight Center. It launched on 18 June 2009 and began its primary mission on 15 September 2009 in a circular polar orbit about 50 km up ([Vondrak et al.](https://ntrs.nasa.gov/citations/20110013489)). It was meant to map the Moon at new scales, find safe landing sites, look for resources and measure radiation ([Vondrak et al.](https://ntrs.nasa.gov/citations/20110013489)).

NASA calls it the longest-lived lunar orbiting mission ever. Its data let NASA and its partners choose safe landing sites and find south-pole areas with water ice and long sunlight ([NASA](https://science.nasa.gov/mission/lro/)). The spacecraft had a launch mass of about 1,916 kg and about 1,850 W of power. The mission cost was reported as US$504 million for LRO itself ([Wikipedia](https://en.wikipedia.org/wiki/Lunar_Reconnaissance_Orbiter)).

LRO is still working. NASA's FY2026 budget request keeps it running at about $22 million a year through FY2030. NASA says it supports commercial CLPS landings and provides data products for Artemis ([NASA FY2026 budget](https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf)).

## Why Open Moon uses it

LRO is the main data source for milestone M00, site selection. We need terrain, imagery, temperature and radar data to choose a base site with a sunlit ridge for solar power near a shadowed crater that may hold ice. LRO provides all four from one spacecraft:

- **Terrain:** LOLA elevation and slope maps, down to 20 m per pixel over 80-90°S ([NASA PGDA](https://pgda.gsfc.nasa.gov/products/90)). We use them to model sunlight across many years.
- **Imagery:** LROC Narrow Angle Camera images at 0.5 m scale ([LROC](https://www.lroc.asu.edu/about)) for mapping boulders, craters and fault scarps at every pad and building spot.
- **Temperature:** Diviner has measured -238 °C in south-polar craters ([Wikipedia](https://en.wikipedia.org/wiki/Diviner_%28radiometer%29)). This tells us where ice can survive.
- **Radar:** Mini-RF radar data on possible ice ([Wikipedia](https://en.wikipedia.org/wiki/Mini-RF)).

LRO data already show that parts of the ridge between Shackleton and de Gerlache craters are lit up to 90% of the time, but no point is lit all the time ([LROC](https://www.lroc.asu.edu/images/1105)). That finding shapes our power design. All of it is free through the [Planetary Data System](https://pds-geosciences.wustl.edu/missions/lro/default.htm) and tools like [QuickMap](https://quickmap.lroc.asu.edu/). Without LRO we would have to fly our own mapping orbiter before choosing a site.

## How it works

LRO carries six instruments and one radar technology demonstration ([Vondrak et al.](https://ntrs.nasa.gov/citations/20110013489)). It flies a polar orbit, so over time it passes over every part of the Moon. In May 2015 NASA lowered the orbit to pass 20 km over the south pole and 165 km over the north pole. This made LOLA's laser returns stronger and let Diviner see smaller features near the south pole ([NASA](https://www.nasa.gov/feature/goddard/nasas-lro-moves-closer-to-the-lunar-surface)).

| Item | Value |
|---|---|
| Launch | 18 June 2009 ([NASA](https://science.nasa.gov/mission/lro/)) |
| Orbit | Polar, 20 km over south pole, 165 km over north pole (since 2015) ([NASA](https://www.nasa.gov/feature/goddard/nasas-lro-moves-closer-to-the-lunar-surface)) |
| LROC NAC | 0.5 m scale, 5 km swath ([LROC](https://www.lroc.asu.edu/about)) |
| LROC WAC | 100 m/pixel, 7 colour bands, 60 km swath ([LROC](https://www.lroc.asu.edu/about)) |
| Mini-RF radar | 30 m/pixel, 12.6 cm and 4.2 cm bands ([Wikipedia](https://en.wikipedia.org/wiki/Mini-RF)) |
| Other instruments | CRaTER (radiation), Diviner (temperature), LAMP (UV), LEND (neutrons), LOLA (laser altimeter) ([Vondrak et al.](https://ntrs.nasa.gov/citations/20110013489)) |
| Downlink | 310 Gbit per Ka-band pass, up to 4 passes a day, about 155 GB/day ([LROC](https://www.lroc.asu.edu/about)) |
| Position accuracy | Under 10 m with radio tracking and GRAIL gravity data ([Mazarico et al.](https://ntrs.nasa.gov/citations/20180007208)) |
| Annual cost | About $22 million (FY2026 request) ([NASA FY2026 budget](https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf)) |

Each instrument team processes its own data and delivers the final products to the Planetary Data System ([LROC](https://www.lroc.asu.edu/about)).

## Limitations and open issues

- **Ageing spacecraft.** In 2018 NASA switched off LRO's inertial measurement unit because it was wearing out. LRO now points using star trackers and a new algorithm, which must avoid Sun, Earth and Moon glare ([NASA](https://www.nasa.gov/missions/teaching-an-old-spacecraft-new-tricks-to-continue-exploring-the-moon/)).
- **Fuel is finite.** Momentum unloads are LRO's main fuel use. Special attitude slews are projected to extend fuel life by several years ([Deboeck et al.](https://ntrs.nasa.gov/citations/20240009215)). We found no public figure for fuel left or a planned end date.
- **Radar transmitter failed.** Mini-RF's transmitter failed in January 2011. It now only receives radar signals sent from Earth ([Wikipedia](https://en.wikipedia.org/wiki/Mini-RF)). So new LRO radar coverage of candidate sites is limited.
- **Dark craters are hard to image.** LROC needs sunlight. ShadowCam was built to be about 200 times more sensitive to see inside shadowed regions ([ShadowCam](https://www.shadowcam.asu.edu/)).
- **Funding depends on budgets.** The FY2026 request keeps LRO flat at about $22 million a year, but this is a request, not a guarantee ([NASA FY2026 budget](https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf)).
- **Orbital data are not ground truth.** Ice and boulder maps from orbit still need checking on the surface, which is why Open Moon plans its own prospecting after site selection.
