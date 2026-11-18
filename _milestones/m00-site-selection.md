---
id_code: M00
order: 0
title: Programme set-up and site selection
phase: 0
window: "2026–2027"
summary: Pick the base site, and a backup, using data already returned by lunar orbiters, before anything is built for it.
objective: "Choose a primary and a backup site near the lunar south pole that give the most sunlight, an access route to permanently shadowed ice, safe terrain for landing and building, and workable communications with Earth. Set up the open-source engineering programme that runs every later milestone."
trl_min: 9
depends_on: []
spec:
  - {k: Team, v: "Engineering and science core team plus open contributors"}
  - {k: Hardware, v: "None flown; uses existing orbital data"}
  - {k: Output, v: "Site certification package, open data set"}
cost: {low: 0.05, high: 0.15, note: "people and computing only; no flight hardware"}
cost_items:
  - {item: "Core engineering team, 2 years", low: 0.04, high: 0.11, basis: "ESTIMATE: 60–150 full-time staff at ~$350k loaded cost per year"}
  - {item: "Computing, data processing, illumination modelling", low: 0.005, high: 0.02, basis: "ESTIMATE"}
  - {item: "Legal, international coordination", low: 0.005, high: 0.02, basis: "ESTIMATE"}
exit_criteria:
  - "Primary and backup sites chosen, each with a sunlit ridge for solar power within cable distance of a permanently shadowed region (PSR) that may hold ice."
  - "Base and PMC point chosen within 10 km of cable run of every planned generation site (each VSAT ridge point and the reactor) and of the ISRU plants, using standard runs of 3 km or less where possible and extended runs of up to 10 km where needed, with the combined illumination of the ridge points inside that reach reported (DD-013, DD-014)."
  - "Illumination modelled for at least an 18.6-year cycle at mast heights of 0, 10 and 20 m, from LOLA terrain data."
  - "Hazard maps (slopes, boulders, craters, young fault scarps) at the best available LROC NAC resolution for every planned landing, pad and building location."
  - "Every landing point on ground of 8° or less (NASA's crewed-lander tilt limit), checked against the lander's own published slope limit (10° for the landers that publish one; see the Lander candidates page)."
  - "Hydrogen (LEND) and ice-candidate maps published for the primary and backup sites, with the M01 prospecting targets chosen from them."
  - "Earth-visibility and relay-coverage analysis showing how many hours per month each site can talk to Earth directly."
  - "Site plan published openly and notified to other lunar operators under Artemis Accords deconfliction practice."
workstreams:
  - name: Data assembly
    desc: Gather every public data set for the south pole into one open GIS.
    items: ["LRO LOLA terrain and LROC imagery", "LRO Diviner temperatures", "ShadowCam images inside PSRs", "Chandrayaan-2 DFSAR radar"]
  - name: Illumination and thermal
    desc: Model sunlight and temperature hour by hour across years.
    items: ["Ray-traced horizon models", "Longest-night statistics per point", "Mast-height trade study", "Best combined light from ridge points within 3 km (standard) and 10 km (extended) of cable run of each candidate base point (DD-013, DD-014)"]
  - name: Hazards
    desc: Map everything that can tip a lander or a building.
    items: ["Slope classes from LOLA LDSM: ≤8°, 8–15°, 15–20°, ≥20° (done for the focus area, Nov 2026)", "Lander slope limits for ten landers (done, Nov 2026)", "Boulder counts", "Young fault scarps and landslide-prone slopes"]
  - name: Resources
    desc: Rank PSRs by likely ice and by how hard they are to reach.
    items: ["LEND hydrogen map of the focus area (done, Nov 2026)", "Ice candidates: Shackleton and de Gerlache shadowed floors, ShadowCam bright spot (done, Nov 2026)", "M3 ice detections plotted on the focus map", "Access-road slope to each PSR"]
  - name: Communications geometry
    desc: Work out when each site can see Earth and where relay satellites are needed.
    items: ["Earth-visibility hours per month", "Relay orbit coverage", "Surface line-of-sight between sites"]
  - name: Programme and legal
    desc: Set up the open-source programme and coordinate with other operators.
    items: ["Open data and CC BY-SA licensing", "Artemis Accords notification", "Partner and procurement strategy"]
technologies:
  - {name: "Lunar Reconnaissance Orbiter (LRO)", use: "Terrain, imagery, temperature and radar data for site selection", status: "Operating; FY2026 budget request continues operations to support CLPS deliveries, landing-site characterisation and Artemis", trl: 9, src: 1}
  - {name: "ShadowCam on KPLO/Danuri", use: "Images inside permanently shadowed craters", status: "Operating in extended mission; expected to end in early 2028 when its battery runs out in a lunar eclipse", trl: 9, src: 2}
  - {name: "Chandrayaan-2 orbiter DFSAR radar", use: "Radar evidence of subsurface ice", status: "DFSAR data showed possible subsurface ice under four doubly shadowed craters (ISRO, May 2026)", trl: 9, src: 3}
  - {name: "NASA Artemis south-pole candidate regions", use: "Starting shortlist of pre-screened regions", status: "9 regions published Oct 2024 (for Artemis III)", trl: 9, src: 4}
  - {name: "LRO LOLA slope and shadow maps (NASA GSFC)", use: "Slope classes and permanently shadowed region outlines for the focus area", status: "10 m/px south-pole products published 2023 (Barker et al.)", trl: 9, src: 18}
  - {name: "LRO LEND neutron detector", use: "Hydrogen in the top ~1 m", status: "South-polar averaged data 2009–2016 in NASA PDS; ~15 km cells", trl: 9, src: 21}
  - {name: "Chandrayaan-1 Moon Mineralogy Mapper (M3)", use: "Surface water-ice detections", status: "Ice spectra published 2018, clustered near Shackleton; one example in de Gerlache", trl: 9, src: 25}
sources:
  - {title: "NASA FY2026 Budget Technical Supplement (Lunar Reconnaissance Orbiter, PS-28/29)", url: "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf", date: "May 2025"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "ISRO: Chandrayaan-2 DFSAR observations reveal subsurface ice in lunar south polar regions", url: "https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html", date: "May 2026"}
  - {title: "NASA NTRS 20250011660: Artemis III Site Selection Update", url: "https://ntrs.nasa.gov/citations/20250011660", date: "Mar 2026"}
  - {title: "Peak of eternal light (Bussey et al. 2010; Speyerer & Robinson 2013 figures), Wikipedia", url: "https://en.wikipedia.org/wiki/Peak_of_eternal_light", date: "accessed Nov 2026"}
  - {title: "LROC: Islands in the Dark (Shackleton rim illumination)", url: "https://www.lroc.asu.edu/images/1105", date: ""}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "NASA: Shrinking Moon causing moonquakes and faults near lunar south pole", url: "https://www.nasa.gov/solar-system/moon/shrinking-moon-causing-moonquakes-and-faults-near-lunar-south-pole/", date: "Jan 2024"}
  - {title: "NASA: Artemis Accords (Section 11, deconfliction and safety zones)", url: "https://www.nasa.gov/artemis-accords/", date: ""}
  - {title: "NASA: Uzbekistan becomes 77th Artemis Accords signatory", url: "https://nasa.gov/organizations/oiir/artemis-accords/nasa-welcomes-uzbekistan-as-newest-artemis-accords-signatory", date: "Oct 2026"}
  - {title: "UNOOSA: Outer Space Treaty (Article II)", url: "https://www.unoosa.org/pdf/publications/ST_SPACE_51E.pdf", date: ""}
  - {title: "NASA Moon Base – Phases", url: "https://www.nasa.gov/moonbase-phases/", date: "Mar 2026"}
  - {title: "JPL IPN Progress Report 42-176: Lunar pole illumination and communications maps (Bryant)", url: "https://ipnpr.jpl.nasa.gov/progress_report/42-176/176C.html", date: "Feb 2009"}
  - {title: "NASA: NASA Provides Update on Artemis III Moon Landing Regions (map of nine regions, credit NASA/GSFC/ASU/JSC/AGDT)", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/", date: "Oct 2024"}
  - {title: "Shackleton (crater), Wikipedia (IAU/WGPSN coordinates and diameter)", url: "https://en.wikipedia.org/wiki/Shackleton_(crater)", date: "accessed Nov 2026"}
  - {title: "de Gerlache (crater), Wikipedia (IAU/WGPSN coordinates and diameter)", url: "https://en.wikipedia.org/wiki/De_Gerlache_(crater)", date: "accessed Nov 2026"}
  - {title: "NASA: NASA Identifies Candidate Regions for Landing Next Americans on Moon (original 13 regions)", url: "https://www.nasa.gov/news-release/nasa-identifies-candidate-regions-for-landing-next-americans-on-moon/", date: "Aug 2022"}
  - {title: "NASA GSFC PGDA: A New View of the Lunar South Pole from LOLA (LDSM slope and hillshade maps, 10 m/px; Barker et al. 2023, Planet. Sci. J. 4, 183, doi:10.3847/PSJ/acf3e1)", url: "https://pgda.gsfc.nasa.gov/products/90", date: "2023"}
  - {title: "LROC (NASA/GSFC/Arizona State University): Shackleton–de Gerlache Ridge maps, sheets 1–3", url: "https://lroc.im-ldi.com/data/support/popular_downloads/LROC_Shackleton_deGerlache_Ridge_maps.zip", date: "Mar 2024"}
  - {title: "NASA Science: Hydrogen at the Lunar Poles: How Much Water Is There? (summary of Sanin et al. 2017, Icarus 283)", url: "https://science.nasa.gov/wp-content/uploads/2023/05/NuggetHydrogenAtTheLunarPoles20170210.pdf", date: "Feb 2017"}
  - {title: "NASA PDS Geosciences Node: LRO LEND data (averaged south-polar products ALDS, 2009–2016)", url: "https://pds-geosciences.wustl.edu/missions/lro/lend.htm", date: "accessed Nov 2026"}
  - {title: "Feldman et al. 2000, Polar hydrogen deposits on the Moon (J. Geophys. Res.)", url: "https://earthref.org/ERR/61400/", date: "2000"}
  - {title: "NASA Ames Astrogram, Aug 2018: Ice confirmed at the Moon's poles (M3 surface-ice map, Li et al. 2018)", url: "https://www.nasa.gov/centers-and-facilities/ames/nasa-ames-astrogram-august-2018/", date: "Aug 2018"}
  - {title: "NASA Science: LRO Science and Data (map of possible water-ice deposits at the south pole)", url: "https://science.nasa.gov/mission/lro/science-and-data/", date: "accessed Nov 2026"}
  - {title: "Li et al. 2018, Direct evidence of surface exposed water ice in the lunar polar regions (PNAS)", url: "https://europepmc.org/article/PMC/PMC6130389", date: "Aug 2018"}
  - {title: "Li et al. 2026, Searching for surficial water ice in lunar permanently shaded regions (PSRs) with ShadowCam (Science Advances)", url: "https://europepmc.org/article/PMC/PMC12998505", date: "Mar 2026"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface (1–3 km links; ISRU power over 3–5 km)", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "NASA: Three companies to help NASA advance solar array technology for Moon (VSAT, up to 32 feet)", url: "https://www.nasa.gov/news-release/three-companies-to-help-nasa-advance-solar-array-technology-for-moon/", date: "Aug 2022"}
  - {title: "NASA NTRS: Vertical Solar Array Technology annual review (key performance parameters)", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
  - {title: "NASA GSFC PGDA: Lunar Polar Illumination (average solar illumination maps; Mazarico et al. 2011, Icarus 211)", url: "https://pgda.gsfc.nasa.gov/products/69", date: "accessed Nov 2026"}
  - {title: "NASA GSFC PGDA: High-Resolution LOLA Topography for Lunar South Pole Sites (best-lit regions of interest)", url: "https://pgda.gsfc.nasa.gov/products/78", date: "accessed Nov 2026"}
  - {title: "Gläser et al. 2014, Illumination conditions at the lunar south pole using high resolution digital terrain models from LOLA (Icarus 243)", url: "https://ui.adsabs.harvard.edu/abs/2014Icar..243...78G", date: "2014"}
risks:
  - {sev: High, title: "ShadowCam's mission is expected to end in early 2028, cutting off new images inside shadowed craters", fix: "Request targeted ShadowCam imaging of candidate PSRs now; archive everything; plan our own prospecting in M01"}
  - {sev: High, title: "Other programmes want the same few sunlit ridges (NASA Moon Base, China's Chang'e-7 near Shackleton)", fix: "Choose a primary and backup site; publish plans early and coordinate under Artemis Accords deconfliction; design for shared infrastructure"}
  - {sev: High, title: "Young fault scarps and landslide-prone slopes near some candidate regions (e.g. de Gerlache Rim 2)", fix: "Map scarps from LROC NAC; keep pads, reactors and habitats off and away from young faults"}
  - {sev: Medium, title: "Even at the best base site studied by JPL, Earth is in direct view only about half the time", fix: "Treat relay satellites as mandatory (M03); pick sites with long Earth-visibility windows for the first lander"}
  - {sev: High, title: "The standard power run is 3 km of cable to the base PMC (DD-013), but the best published pair of Shackleton-ridge points (~94% combined light) is about 8 km apart, and NASA expects ISRU to need power over 3–5 km. Extended runs of up to 10 km (DD-014) reach both, at ~10–15% loss and with 1 kHz stability not yet analysed", fix: "Rank candidate base points by the combined light of ridge points within a 10 km cable reach, preferring 3 km standard runs; for the 8 km pair, put at least one point within 10 km and keep each run 10 km or less; feed ISRU plants at 3–5 km by extended runs; plan PSR work beyond 10 km on the mobile power cart (PW.5) or a local source"}
  - {sev: Medium, title: "Some illumination figures in the literature are second-hand or model-dependent", fix: "Re-run illumination ourselves from LOLA terrain data and publish the code"}
  - {sev: High, title: "Ice in the focus area is unconfirmed: Shackleton's evidence is mixed and de Gerlache has only two candidate detections", fix: "Send M01 prospectors to the crater rims next to both shadowed floors; keep a backup site with stronger hydrogen"}
  - {sev: Medium, title: "The strongest hydrogen (LEND) and the ice-candidate craters are in different parts of the focus area", fix: "Treat hydrogen and ice as separate targets; measure both on the ground before choosing the base site"}
  - {sev: Medium, title: "No lander publishes a certified slope limit above 10°, and IM-1 tipped over on 12° ground", fix: "Land only on ground of 8° or less; confirm each pad with ~1 m LROC NAC hazard maps"}
---

## Where the site search stands (November 2026)

- **Focus area chosen:** about 180 × 130 km around the south pole, centred on the Shackleton–de Gerlache Ridge, between Shackleton, Spudis and de Gerlache craters. It includes NASA's de Gerlache Rim 2 candidate region.
- **Slope mapped:** 43 % of the focus area is 8° or less, Open Moon's landing limit; 78 % is 15° or less.
- **Landers compared:** no lander publishes a certified slope limit above 10° ([Lander candidates]({{ '/landers/' | relative_url }})).
- **Hydrogen mapped:** 13 % of the focus area is high hydrogen in NASA's LEND data, mostly in the upper right (around 88°S, 0–60°E), away from the craters.
- **Ice candidates:** the shadowed floors of Shackleton and de Gerlache (483 km² together) have published but unconfirmed ice detections. Spudis and the ridge craters have no ice data.
- **Next:** choose primary and backup sites from these layers, then prove the ice and hydrogen on the ground in M01.

## Why the south pole

NASA's own architecture work explains the choice: near the south pole some ridges are sunlit most of the time, while nearby craters stay permanently in shadow and cold enough to trap water ice<sup class="r">[7](#s7)</sup>. That pairing, near-constant solar power next to frozen water, is what makes a self-sustaining base possible without inventing new technology. NASA's 2026 Moon Base programme also targets the south pole<sup class="r">[12](#s12)</sup>, so a base there can share transport, relays and data.

## How sunny is "near-eternal light"?

No point on the Moon is sunlit all the time<sup class="r">[6](#s6)</sup>. The best points are close:

| Location | Share of the year sunlit | Source |
|---|---|---|
| Shackleton ridge (89.68°S) | ~81% | Bussey et al. 2010, via<sup class="r">[5](#s5)</sup> |
| Peaks near Shackleton | ~82% and ~86% | same |
| de Gerlache ridge | ~85% | same |
| Malapert Mountain | ~74% | same |
| Two Shackleton-ridge points ~8 km apart, combined | ~94% | same |
| Best points on the Shackleton–de Gerlache ridge | up to ~90% | LROC<sup class="r">[6](#s6)</sup> |

**Design consequence:** spread solar arrays across two or three nearby high points so that at least one is almost always lit, and raise them on masts. The longest darkness at a single point can still be days long<sup class="r">[5](#s5)</sup>, so the base still needs storage and fission power. In this plan the reactor and the solar towers both feed a central power management controller (PMC), which sends power to the base or into storage (see M04 and design changes DD-003 and DD-008).

**Site constraint: power sources within 3 km of the base as standard, 10 km at most (design changes DD-013 and DD-014).** The standard power run is 3 km of cable from a solar tower or reactor to the base PMC (plan design, DD-013). This is NASA's Artemis working scale of 1–3 km links<sup class="r">[27](#s27)</sup>. Extended runs of up to 10 km are allowed, at about 10–15% transmission loss (this plan's arithmetic and ESTIMATE), with voltage regulation at the receiving end and a 1 kHz stability analysis for each run (plan design, DD-014). Beyond 10 km is rejected. The two Shackleton-ridge points that reach ~94% together are about 8 km apart<sup class="r">[5](#s5)</sup>, so both cannot be within 3 km of one base. With extended runs, both can be reached: at least one point must be within 10 km of cable run, and each run must be 10 km or less (plan design). Site selection must still find the best combined light, preferring standard runs, and report the cable length and loss of every extended run (open). NASA expects ISRU to need power over 3–5 km<sup class="r">[27](#s27)</sup>; plants at that distance now run on grid power over extended runs (DD-014). Ice mining beyond 10 km uses the mobile power cart (PBS PW.5) or a local source (open).

{% include decision-note.html id="DD-014" extra="DD-013 put the ~94% ridge-point pair out of reach. Extended runs of up to 10 km bring it back, at about 10–15% loss." %}

{% include decision-note.html id="DD-013" extra="Before this, the plan put solar towers on two or three ridge points at any distance and cited the ~94% two-point figure without a distance limit." %}

## Candidate regions map

![NASA's nine candidate landing regions near the lunar south pole, with Shackleton crater, de Gerlache crater and the Connecting Ridge added, and the Open Moon focus area outlined in red]({{ '/assets/sites/south-pole-candidate-regions.jpg' | relative_url }})

*Base map: NASA's October 2024 map of the nine candidate regions (yellow boxes), an LRO Wide Angle Camera mosaic, credit NASA/GSFC/ASU/JSC/AGDT<sup class="r">[14](#s14)</sup>. Open Moon additions: Shackleton (89.67°S 129.78°E, 21 km)<sup class="r">[15](#s15)</sup> and de Gerlache (88.5°S 87.1°W, 32.4 km)<sup class="r">[16](#s16)</sup> in cyan, placed from their published coordinates using NASA's pole marker and 50 km scale bar; the Connecting Ridge in orange, drawn rim to rim and **approximate** (no published outline yet); the Open Moon focus area in red.*

## Focus area: Shackleton – de Gerlache

{% include decision-note.html id="DD-010" extra="The primary and backup sites will be chosen inside this area." %}

Open Moon's site search concentrates on the area outlined in red, about 180 × 130 km around the south pole. It contains:

- **Shackleton crater**, whose rim the south pole lies on<sup class="r">[15](#s15)</sup>.
- **de Gerlache crater**, which has a permanently shadowed pocket in its interior<sup class="r">[16](#s16)</sup>.
- **The Connecting Ridge** between them, with the sunniest points studied so far (see the table above).
- **de Gerlache Rim 2**, the one current NASA candidate region inside the area<sup class="r">[14](#s14)</sup>. A young fault scarp has been mapped there (see the risks above)<sup class="r">[8](#s8)</sup>.

Connecting Ridge and Connecting Ridge Extension were on NASA's original 2022 list of 13 regions<sup class="r">[17](#s17)</sup> but are not among the nine published in 2024. NASA has not said why, and says regions removed for Artemis III are not ruled out for future exploration<sup class="r">[14](#s14)</sup>.

![Close-up of the Open Moon focus area: de Gerlache Rim 2, de Gerlache crater, the Connecting Ridge and Shackleton crater]({{ '/assets/sites/shackleton-de-gerlache-focus.jpg' | relative_url }})

*Close-up of the focus area (same sources and caveats as above).*

## Terrain slope in the focus area

Slope comes from NASA Goddard's LOLA slope map (LDSM) at 10 m per pixel<sup class="r">[18](#s18)</sup>.

### Raw slope data

The LDSM values as published, in degrees, on a continuous scale with no classes (averaged to 40 m per pixel for the whole focus area). The data file is [LDSM_83S_10MPP_ADJ.TIF](https://pgda.gsfc.nasa.gov/data/LOLA_20mpp/LDSM_83S_10MPP_ADJ.TIF) (7.5 GB) on NASA Goddard's [product page](https://pgda.gsfc.nasa.gov/products/90).

![Raw LOLA slope in degrees across the Open Moon focus area, dark flat to yellow steep]({{ '/assets/sites/focus-slope-raw.jpg' | relative_url }})

### Slope classes

{% include decision-note.html id="DD-011" extra="Rovers, masts and towers may still work on steeper ground within their own limits." %}

{% include decision-note.html id="DD-012" %}

Laid over NASA's LOLA hillshade. Open Moon colours slope in four classes, set from what landers can actually handle (see [Lander candidates]({{ '/landers/' | relative_url }})):

| Colour | Slope | Why this break |
|---|---|---|
| Green | ≤8° | NASA's tilt limit for crewed landers after touchdown is 8° |
| Yellow | 8–15° | Published robotic lander limits stop at 10° (Nova-C design, Griffin "easily tolerate"); landing here needs care |
| Orange | 15–20° | Above every published lander limit |
| Red | ≥20° | Crater walls and steep scarps |

The boxes are placed using the alignment of the NASA map above, so their edges are approximate.

| Area | ≤8° | 8–15° | 15–20° | ≥20° | Median | Steepest | Resolution |
|---|---|---|---|---|---|---|---|
| Focus area (red box, ~180 × 130 km) | 43% | 35% | 14% | 8% | 9.2° | 42.4° | 40 m/px |
| de Gerlache Rim 2 (NASA box as drawn, ~20 × 20 km) | 22% | 42% | 25% | 12% | 12.9° | 41.8° | 10 m/px |

*Computed by Open Moon from the LDSM data<sup class="r">[18](#s18)</sup>. The drawn Rim 2 box includes part of de Gerlache crater's inner wall, which is much of its steep ground. At full 10 m resolution the steepest point on Shackleton's wall is 52.5°; the 40 m map averages such spots down.*

![Slope classes across the Open Moon focus area: green ≤8°, yellow 8–15°, orange 15–20°, red ≥20°]({{ '/assets/sites/focus-slope-classes.jpg' | relative_url }})

### de Gerlache Rim 2 close-up (10 m/px)

![Slope classes across NASA's de Gerlache Rim 2 candidate region]({{ '/assets/sites/de-gerlache-rim2-slope-classes.jpg' | relative_url }})

**Limits of this analysis.** At 10 m per pixel, boulders and small craters that can tip a lander are not resolved; NASA's own criteria also weigh lighting and Earth visibility. Final pads need LROC NAC hazard maps at about 1 m per pixel (exit criteria above).

## The Shackleton–de Gerlache Ridge (LROC maps)

The LROC team's 2024 map set<sup class="r">[19](#s19)</sup> (NAC images at 2 m per pixel) describes the ridge as a "30-kilometer-long topographic high" that meets Shackleton's rim at Rickinson crater and "dog-legs around Vincent crater up towards de Gerlache crater". Key facts from the sheets:

- **Summit:** 1959.5 m elevation at 89.4385°S, 222.82°E, with "favorable solar illumination, and Earth visibility".
- **Slope:** within the mapped area, median 11.5°, average 12.2° (from 20 m LOLA data). Slopes on the Spudis crater side are "generally above 15°" and on the Henson crater side "above 10°".
- **Best ground:** "relatively benign slopes for landers and rovers ... especially the stretch from Cheetham crater up to the ridge summit and the rim of Shackleton crater 'above' Rickinson crater."
- **Ice targets:** small craters along the ridge (Worsley, Vincent, Holness, Marston, Wild, Cheetham, Wordie, McCarthy, Kerr, Hurley) "host permanently shadowed regions, which may harbor volatiles".

The ridge actually bends around Spudis crater, so the straight orange line on the maps above is only a rough guide.

![LROC Shackleton–de Gerlache Ridge, sheet 1: multi-lighting controlled mosaic]({{ '/assets/sites/lroc-ridge-sheet1-controlled-mosaic.jpg' | relative_url }})

![LROC Shackleton–de Gerlache Ridge, sheet 2: topographic mosaic with contours and slope histogram]({{ '/assets/sites/lroc-ridge-sheet2-topographic.jpg' | relative_url }})

![LROC Shackleton–de Gerlache Ridge, sheet 3: oblique views]({{ '/assets/sites/lroc-ridge-sheet3-oblique-views.jpg' | relative_url }})

*Sheets 1–3 credit NASA/GSFC/Arizona State University (LROC), March 2024, reduced from 21,600 × 14,400 px. Full-resolution sheets are in the source download<sup class="r">[19](#s19)</sup>.*

## Sunlight and VSAT locations

### How high NASA's VSAT goes

NASA's Vertical Solar Array Technology (VSAT) arrays "autonomously deploy up to 32 feet high" (about 10 m) and retract to move<sup class="r">[28](#s28)</sup>. NASA's key performance parameters set the mast height at a **5 m threshold and a 10 m goal**, measured from the ground to where the solar blanket attaches; and terrain stability at a **10° slope with a 5 m mast (threshold) and 15° with a 10 m mast (goal)**<sup class="r">[29](#s29)</sup>. Each array is 10 kW<sup class="r">[29](#s29)</sup>.

Height matters at the pole because the Sun skims the horizon: on the Shackleton–de Gerlache ridge, sunlight rises from 92.27 % of the time at 2 m to 95.65 % at 10 m<sup class="r">[32](#s32)</sup>.

### Average sunlight (NASA data)

NASA Goddard's average solar illumination over a full 18.6-year lunar cycle, at ground level, 60 m per pixel<sup class="r">[30](#s30)</sup>. Magenta circles are NASA's own best-lit regions of interest at the Connecting Ridge (Site 1), Shackleton rim (Site 4), Peak near Shackleton (Site 7) and de Gerlache rim (Site 11)<sup class="r">[31](#s31)</sup>.

![Average sunlight at ground level across the Open Moon focus area, with NASA's best-lit regions of interest]({{ '/assets/sites/focus-sunlight-raw.jpg' | relative_url }})

### Where VSATs could go

VSAT sites (plan design) are spots on slopes of 15° or less (the VSAT goal with a 10 m mast) that are sunlit at ground level:

- **Orange dots, sites 1–6:** sunlit at least **80 %** of the time.
- **Yellow dots, sites 7–16:** sunlit **70–80 %** of the time.

Spots below 70 % are left out. Each dot marks a 1 km cell holding such a spot, and the numbers match the table below; the spots themselves cover about 0.1 km² (≥80 %) and 0.6 km² (≥70 %) of the focus area. Magenta circles are NASA's regions of interest (Sites 1, 4, 7 and 11). Dots and percentages in the table are **ground-level** figures from NASA's map; a 10 m mast sees more sun. No spot in the focus area reaches 90 % at ground level; the highest is 88.4 %.

![VSAT sites in the Open Moon focus area: orange dots sunlit at least 80 %, yellow dots 70–80 %, slope of 15° or less, with NASA's regions of interest circled]({{ '/assets/sites/focus-vsat-candidates.jpg' | relative_url }})

The 16 sites (best single 60 m pixel in each, ground level, slope ≤15°), from NASA's illumination map<sup class="r">[30](#s30)</sup>:

| # | Dot | Site | Best spot | Sunlit (ground) |
|---|---|---|---|---|
| 1 | Orange | Connecting ridge, NASA Site 1 (beside LROC's ridge summit, 89.4385°S, 137.18°W) | 89.4745°S, 137.53°W | 88.4 % |
| 2 | Orange | Shackleton west rim, NASA Site 4, where the ridge meets Shackleton | 89.6857°S, 163.04°W | 87.1 % |
| 3 | Orange | Peak near Shackleton, NASA Site 7 | 88.8082°S, 123.78°E | 86.0 % |
| 4 | Orange | Shackleton west rim, NASA Site 4 | 89.7837°S, 156.07°W | 85.5 % |
| 5 | Orange | de Gerlache rim, NASA Site 11 | 88.6652°S, 68.42°W | 82.7 % |
| 6 | Orange | Lower edge of the map, about 61 km from the pole | 87.9870°S, 166.40°W | 80.4 % |
| 7 | Yellow | Ridge, south of Spudis | 89.3158°S, 114.23°W | 79.4 % |
| 8 | Yellow | Lower-left corner of the map | 85.8282°S, 116.34°W | 78.5 % |
| 9 | Yellow | Near the pole, on Shackleton's rim, about 6 km from the pole | 89.8104°S, 54.16°E | 78.1 % |
| 10 | Yellow | East rim of de Gerlache (where the ridge meets de Gerlache) | 89.0039°S, 96.38°W | 78.0 % |
| 11 | Yellow | Lower right of the map, about 67 km from the pole | 87.7940°S, 144.43°E | 77.1 % |
| 12 | Yellow | de Gerlache rim, NASA Site 11 | 88.4657°S, 67.87°W | 75.1 % |
| 13 | Yellow | Lower-left corner of the map | 85.6815°S, 116.61°W | 73.9 % |
| 14 | Yellow | Shackleton rim, by the pole | 89.8861°S, 148.19°W | 72.9 % |
| 15 | Yellow | Near the Peak near Shackleton | 88.8604°S, 132.20°E | 72.5 % |
| 16 | Yellow | Below-right of Shackleton, about 21 km from the pole | 89.2990°S, 127.34°E | 72.2 % |

*Open Moon's reading of NASA's map (sites are cells within 3 km of each other); the cell list is in `analysis/sunlight/vsat_spots.csv`. NASA ranks Site 1 (Connecting ridge) as having the most area with average sunlight above 70 % at 1 m height, with its regions 4–6 the most favourable<sup class="r">[31](#s31)</sup>. At 10 m, the Connecting ridge is lit 95.65 % of the time<sup class="r">[32](#s32)</sup>, the only published value above 90 % here.*

- **Best VSAT ground:** the Connecting ridge (site 1) and Shackleton's west rim (sites 2 and 4), all on the Shackleton–de Gerlache Ridge. With the yellow sites along the same ridge (7, 10 and 14), a chain of VSATs along the ridge could feed a base there.
- **Spread out for shadows:** no spot is lit all the time. Two ridge points about 8 km apart are lit a combined ~94 % of the year (see the sunlight table above), so the plan spreads VSATs over several of these sites.
- **Landing vs. set-down:** VSAT sites can be up to 15°, but the lander carrying each VSAT still lands on 8° or less (DD-011) and the VSAT moves to its site.

### Light over time (ESTIMATE)

Sunlight and shadow across the focus area over one lunar day (about 29.5 Earth days, one frame every 12 hours), in the best and the worst season for the south pole. Open Moon's own shadow calculation over NASA's LOLA terrain<sup class="r">[18](#s18)</sup> with Sun positions from NASA/JPL's DE421 ephemeris (**ESTIMATE**). Dots are the VSAT sites above.

**Best season: 23 October – 21 November 2027**, with the Sun at its most southerly.

![Animation of sunlight and shadow over the Open Moon focus area during one lunar day in October–November 2027]({{ '/assets/sites/focus-sunlight-summer-2027.gif' | relative_url }})

**Worst season: 12 April – 12 May 2027**, with the Sun at its most northerly. The de Gerlache rim and the ridge are lit, while Shackleton's rim stays dark for days.

![Animation of sunlight and shadow over the Open Moon focus area during one lunar day in April–May 2027]({{ '/assets/sites/focus-sunlight-winter-2027.gif' | relative_url }})

### Multiple VSAT placements on the de Gerlache rim (ESTIMATE)

No single spot is lit all the time, so the base needs several VSATs placed where their dark periods do not line up. NASA publishes only average sunlight, not when each spot is lit, so Open Moon calculated light and shadow over time itself (**ESTIMATE**, this plan's own calculation). For 1,172 spots on and around the de Gerlache rim it traced the horizon over NASA's LOLA terrain<sup class="r">[18](#s18)</sup> and tested it against the Sun's position every 2 hours for 18.6 years, using NASA/JPL's DE421 ephemeris. The method matches NASA's illumination map<sup class="r">[30](#s30)</sup> within 1.6 points on average at 60 random test points (RMS 2.2 points), but for the best-lit rim spots it reads several points lower than NASA's map (for example 70.8 % against 82.7 % at site 5). So **use these figures to compare layouts; the true values are likely somewhat higher.** A spot counts as lit when at least half the Sun's disc is above its horizon. All figures are at ground level; a 10 m mast sees more sun.

The standard power run is 3 km of cable (DD-013); extended runs of up to 10 km are allowed at about 10–15% transmission loss (DD-014), so VSATs on extended runs can be up to 20 km apart. Straight-line distances are used here; real cable routes will be somewhat longer.

![VSAT layouts on the de Gerlache rim: option 1 with the base at site 5, option 2 with the PMC between site 5 and the crater's east rim]({{ '/assets/sites/de-gerlache-vsat-sets.jpg' | relative_url }})

**Option 1: base and PMC at site 5, VSATs within 10 km of it (orange, C1–C4).** Spots more than 3 km from the PMC need extended runs (DD-014).

| VSATs | Time at least one is lit | Longest time all are dark | Spot added (sunlit alone, ESTIMATE) | Distance from site 5 |
|---|---|---|---|---|
| 1 | 72.4 % | 336 h (14 days) | best single spot: 88.4651°S, 67.85°W (72.4 %) | 6.1 km |
| 2 | 84.2 % | 142 h (5.9 days) | C1 88.3745°S, 69.29°W (56.3 %) + C2 88.6812°S, 68.11°W (62.5 %) | 8.8 km, 0.5 km |
| 3 | 84.7 % | 142 h (5.9 days) | + C3 88.3931°S, 68.66°W (66.9 %) | 8.3 km |
| 4 | 85.0 % | 142 h (5.9 days) | + C4 88.9562°S, 74.55°W (40.2 %) | 9.6 km |

C1 and C2 are 9.4 km apart; the four spots are 0.8–18.0 km apart. Keeping every VSAT on a standard 3 km run instead gives 84.0 % with two VSATs and 84.5 % with four, with a longest blackout of 148 h.

**Option 2: PMC between site 5 and the crater's east rim (blue, D1–D4).** The PMC sits inside the crater rim at about 88.88°S, 80.3°W, so a VSAT near site 5 and one on the east rim are each within 10 km of it. All four spots need extended runs (DD-014).

| VSATs | Time at least one is lit | Longest time all are dark | Spot added (sunlit alone, ESTIMATE) | Distance to PMC / to site 5 |
|---|---|---|---|---|
| 2 | 87.5 % | 102 h (4.3 days) | D1 near site 5, 88.7035°S, 67.52°W (40.6 %) + D2 east rim, 89.0032°S, 96.55°W (61.0 %) | 9.8 km / 1.3 km; 9.8 km / 19.9 km |
| 3 | 88.8 % | 102 h (4.3 days) | + D3 east rim, 89.0147°S, 92.47°W (66.4 %) | 7.8 km / 18.0 km |
| 4 | 89.2 % | 100 h (4.2 days) | + D4 by site 5, 88.6812°S, 68.11°W (62.5 %) | 9.8 km / 0.5 km |

D1 and D2 are 19.5 km apart; the four spots are 0.8–19.7 km apart.

- **Pairing across the crater works best.** A VSAT near site 5 and one on the east rim, where the ridge meets de Gerlache (site 10 on the map above), are lit at different times. Option 2 reaches 89.2 % with four VSATs and cuts the longest blackout to about 4 days.
- **VSATs close together share shadows.** In option 1 the 3rd and 4th VSAT add only 0.5 and 0.3 points, because nearby spots see almost the same horizon. They add power, not hours of sun.
- **The base can still sit at site 5 in option 2** if the PMC is placed separately: site 5 is about 10 km from that PMC, so it connects through the distribution grid. Where the PMC goes is a design choice for M04.
- **No layout reaches 100 %.** Even option 2 leaves about 11 % of the time with every VSAT dark, in stretches of up to about 4 days, so storage and fission power (M04) are still needed.

The analysis scripts and full results are in `analysis/sunlight/multi/`.

## Hydrogen

Hydrogen matters to Open Moon whether it sits in water ice or is bound in the soil: either way it is a raw material (extraction is planned in later milestones). Orbiters map hydrogen in the top metre or so by counting neutrons leaving the surface; hydrogen slows them, so fewer escape. A neutron dip shows hydrogen but not its form: ice, solar-wind hydrogen or hydrated minerals<sup class="r">[22](#s22)</sup>.

### NASA's map

NASA's LRO LEND team converted the neutron data to water-equivalent hydrogen (WEH). Enhancements sit "near and in areas of permanent shadow"; the highest value is about 0.54 wt% water in Cabeus crater (location 1S), assuming the hydrogen is water spread evenly through the top 1 m<sup class="r">[20](#s20)</sup>.

![NASA LEND map of water-equivalent hydrogen around the lunar south pole, with enhanced locations 1S to 8S marked]({{ '/assets/sites/nasa-lend-weh-south-pole.jpg' | relative_url }})

![NASA LEND water-equivalent hydrogen in Cabeus crater]({{ '/assets/sites/nasa-lend-weh-cabeus.jpg' | relative_url }})

*NASA Science, from Sanin et al. 2017<sup class="r">[20](#s20)</sup>. Permanently shadowed areas are outlined in grey; scale 0–0.5 wt% WEH.*

### Open Moon's hydrogen map from the LEND data

We downloaded NASA's LEND south-polar data (0.5° cells, 2009–2016)<sup class="r">[21](#s21)</sup> and mapped the dip in collimated epithermal neutrons, smoothed over 10 km, against the 80–84°S average. **High hydrogen** means a dip of at least 1.28 % (the top 10 % of the region south of 84°S) that is at least three times its statistical error. This is Open Moon processing, not a NASA product; the scripts are in `analysis/hydrogen/`.

![Hydrogen from NASA LEND data around the south pole to 84°S, with the Open Moon focus area outlined]({{ '/assets/sites/south-pole-lend-hydrogen.jpg' | relative_url }})

## Ice candidates

Ice candidates are places where instruments have reported signs of water ice at or near the surface. None in the focus area is confirmed; the evidence for and against is in the [ice research]({{ site.repo }}/blob/main/research/ice/south-pole-water-ice.md).

### NASA's maps

![NASA map of surface water ice detected by the Moon Mineralogy Mapper at the lunar south pole (left) and north pole (right)]({{ '/assets/sites/nasa-m3-polar-ice-2018.jpg' | relative_url }})

*Surface ice detected by NASA's Moon Mineralogy Mapper (M3) on Chandrayaan-1: south pole left, north pole right. Ice locations are shown in cyan over surface temperature (darker is colder). At the south pole most of the ice is in craters<sup class="r">[23](#s23)</sup><sup class="r">[25](#s25)</sup>.*

![NASA LRO map of areas of the Moon's south pole with possible deposits of water ice, shown in blue]({{ '/assets/sites/nasa-lro-south-pole-possible-ice.jpg' | relative_url }})

*"Areas of the Moon's south pole with possible deposits of water ice, shown in blue. The map is based on data taken by NASA's Lunar Reconnaissance Orbiter."<sup class="r">[24](#s24)</sup>*

### Ice candidates in the focus area

Blue marks the permanently shadowed floors of Shackleton (233 km²) and de Gerlache (242 km²), outlined from NASA Goddard's shadow map<sup class="r">[18](#s18)</sup>, where published ice detections are reported<sup class="r">[25](#s25)</sup>. The white dot is ShadowCam's unexplained bright spot at 88.5352°S, 97.4007°W, inside de Gerlache's shadowed floor<sup class="r">[26](#s26)</sup>. Pale outlines are other permanently shadowed areas with no published ice data, including Spudis and the small craters along the ridge.

![Ice candidates in the Open Moon focus area: shadowed floors of Shackleton and de Gerlache in blue, ShadowCam bright spot, other shadowed areas outlined]({{ '/assets/sites/focus-ice-candidates.jpg' | relative_url }})

- **Shackleton:** a bright floor in LOLA data, radar results allowing some ice in its walls, and nearby M3 ice spectra; but Kaguya and ShadowCam found no exposed ice, and part of the floor gets above 110 K in summer.
- **de Gerlache:** one M3 ice spectrum and the ShadowCam bright spot, which needs more viewing angles to test.

## All layers combined

Green: slope of 8° or less (landable for every published lander rule); steeper ground is left uncoloured. **Purple:** high hydrogen from LEND. **Blue:** ice candidates. White dot: ShadowCam bright spot.

![Open Moon focus area: landable ground of 8° or less in green, high hydrogen in purple, ice-candidate shadowed floors in blue]({{ '/assets/sites/focus-landing-hydrogen.jpg' | relative_url }})

- **Landable:** 43 % of the focus area is 8° or less.
- **Hydrogen:** 13 % is high hydrogen, mostly the upper right (toward 0–60°E, around 88°S); 4.6 % is both landable and high hydrogen. It does not cover Shackleton, Spudis, the ridge or de Gerlache Rim 2.
- **Ice candidates:** 483 km² of shadowed crater floor in Shackleton and de Gerlache, with landable ground on the rims next to both.
- **Why hydrogen and ice candidates differ:** LEND averages the top ~1 m over ~15 km cells, while M3 and LOLA see the top millimetres or microns at a few hundred metres. A thin frost or small patches can show in one and not the other. Only ground measurements (M01) can settle it.

## Step-by-step

1. **Build the open site database.** Pull LRO LOLA, LROC, Diviner and Mini-RF data<sup class="r">[1](#s1)</sup>, ShadowCam images<sup class="r">[2](#s2)</sup> and Chandrayaan-2 radar products<sup class="r">[3](#s3)</sup> into one public GIS.
2. **Start from NASA's shortlist, then narrow to a focus area.** NASA cut its Artemis III list to nine regions in October 2024: Peak near Cabeus B, Haworth, Malapert Massif, Mons Mouton Plateau, Mons Mouton, Nobile Rim 1 and 2, de Gerlache Rim 2 and Slater Plain<sup class="r">[4](#s4)</sup>. These are already screened for landing safety, light and Earth visibility. Open Moon has chosen the Shackleton–de Gerlache area, which includes de Gerlache Rim 2 (see above).
3. **Model light and temperature** hour by hour, for every candidate, at several mast heights. For each candidate base point, find the ridge points within 3 km of cable run (standard) and within 10 km (extended), and their combined light (DD-013, DD-014).
4. **Map hazards.** Slope is mapped for the focus area in four classes from NASA's LOLA data, with 8° as the landing limit (done). Also include young fault scarps: NASA-funded work links the shrinking Moon to faults and moonquakes near the south pole, including a scarp in de Gerlache Rim 2, and some shadowed slopes are prone to landslides<sup class="r">[8](#s8)</sup>.
5. **Rank ice targets.** ShadowCam found little widespread surface ice, but some 20–50 m patches consistent with more than 10% ice<sup class="r">[2](#s2)</sup>. Ice is patchy, so M01 must confirm it on the ground. For the focus area, hydrogen from LEND and ice candidates from M3, LOLA and ShadowCam are now mapped (see above).
6. **Check communications.** Earth visibility varies from site to site: some Earth-facing areas see Earth almost all the time, others never do<sup class="r">[7](#s7)</sup>. At the best proposed base site in a JPL study, direct-to-Earth links were available only about 51% of the time<sup class="r">[13](#s13)</sup>, so relay coverage is a hard requirement.
7. **Decide, publish and notify.** Under the Outer Space Treaty no one can claim territory<sup class="r">[11](#s11)</sup>. The Artemis Accords (78 signatories after Vietnam joined on 28 October 2026<sup class="r">[9](#s9)</sup>) ask operators to give notice and coordinate to avoid harmful interference<sup class="r">[9](#s9)</sup>. Open Moon publishes its site plan and follows that practice.

> Open question for contributors: within the focus area, which two sites give the best combination of landable ground (≤8°), illumination, access to the Shackleton and de Gerlache shadowed floors and the LEND hydrogen zone, and distance from other programmes' planned activity?
