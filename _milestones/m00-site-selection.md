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
  - "Illumination modelled for at least an 18.6-year cycle at mast heights of 0, 10 and 20 m, from LOLA terrain data."
  - "Hazard maps (slopes, boulders, craters, young fault scarps) at the best available LROC NAC resolution for every planned landing, pad and building location."
  - "Earth-visibility and relay-coverage analysis showing how many hours per month each site can talk to Earth directly."
  - "Site plan published openly and notified to other lunar operators under Artemis Accords deconfliction practice."
workstreams:
  - name: Data assembly
    desc: Gather every public data set for the south pole into one open GIS.
    items: ["LRO LOLA terrain and LROC imagery", "LRO Diviner temperatures", "ShadowCam images inside PSRs", "Chandrayaan-2 DFSAR radar"]
  - name: Illumination and thermal
    desc: Model sunlight and temperature hour by hour across years.
    items: ["Ray-traced horizon models", "Longest-night statistics per point", "Mast-height trade study"]
  - name: Hazards
    desc: Map everything that can tip a lander or a building.
    items: ["Slope and roughness maps", "Boulder counts", "Young fault scarps and landslide-prone slopes"]
  - name: Resources
    desc: Rank PSRs by likely ice and by how hard they are to reach.
    items: ["Neutron and radar hydrogen maps", "ShadowCam ice patches", "Access-road slope to each PSR"]
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
sources:
  - {title: "NASA FY2026 Budget Technical Supplement (Lunar Reconnaissance Orbiter, PS-28/29)", url: "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf", date: "May 2025"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "ISRO: Chandrayaan-2 DFSAR observations reveal subsurface ice in lunar south polar regions", url: "https://www.isro.gov.in/Chandrayaan2_Dual_Frequency_Synthetic_Aperture_Radar.html", date: "May 2026"}
  - {title: "NASA NTRS 20250011660: Artemis III Site Selection Update", url: "https://ntrs.nasa.gov/citations/20250011660", date: "2026"}
  - {title: "Peak of eternal light (Bussey et al. 2010; Speyerer & Robinson 2013 figures), Wikipedia", url: "https://en.wikipedia.org/wiki/Peak_of_eternal_light", date: "accessed Nov 2026"}
  - {title: "LROC: Islands in the Dark (Shackleton rim illumination)", url: "https://www.lroc.asu.edu/images/1105", date: ""}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "NASA: Shrinking Moon causing moonquakes and faults near lunar south pole", url: "https://www.nasa.gov/solar-system/moon/shrinking-moon-causing-moonquakes-and-faults-near-lunar-south-pole/", date: "Jan 2024"}
  - {title: "NASA: Artemis Accords (Section 11, deconfliction and safety zones)", url: "https://www.nasa.gov/artemis-accords/", date: ""}
  - {title: "NASA: Uzbekistan becomes 77th Artemis Accords signatory", url: "https://nasa.gov/organizations/oiir/artemis-accords/nasa-welcomes-uzbekistan-as-newest-artemis-accords-signatory", date: "Oct 2026"}
  - {title: "UNOOSA: Outer Space Treaty (Article II)", url: "https://www.unoosa.org/pdf/publications/ST_SPACE_51E.pdf", date: ""}
  - {title: "NASA Moon Base – Phases", url: "https://www.nasa.gov/moonbase-phases/", date: "2026"}
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
risks:
  - {sev: High, title: "ShadowCam's mission is expected to end in early 2028, cutting off new images inside shadowed craters", fix: "Request targeted ShadowCam imaging of candidate PSRs now; archive everything; plan our own prospecting in M01"}
  - {sev: High, title: "Other programmes want the same few sunlit ridges (NASA Moon Base, China's Chang'e-7 near Shackleton)", fix: "Choose a primary and backup site; publish plans early and coordinate under Artemis Accords deconfliction; design for shared infrastructure"}
  - {sev: High, title: "Young fault scarps and landslide-prone slopes near some candidate regions (e.g. de Gerlache Rim 2)", fix: "Map scarps from LROC NAC; keep pads, reactors and habitats off and away from young faults"}
  - {sev: Medium, title: "Even at the best base site studied by JPL, Earth is in direct view only about half the time", fix: "Treat relay satellites as mandatory (M03); pick sites with long Earth-visibility windows for the first lander"}
  - {sev: Medium, title: "Some illumination figures in the literature are second-hand or model-dependent", fix: "Re-run illumination ourselves from LOLA terrain data and publish the code"}
---

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

**Design consequence:** spread solar arrays across two or three nearby high points so that at least one is almost always lit, and raise them on masts. The longest darkness at a single point can still be days long<sup class="r">[5](#s5)</sup>, so the base still needs storage and fission power (see M04).

## Candidate regions map

![NASA's nine candidate landing regions near the lunar south pole, with Shackleton crater, de Gerlache crater and the Connecting Ridge added, and the Open Moon focus area outlined in red]({{ '/assets/sites/south-pole-candidate-regions.jpg' | relative_url }})

*Base map: NASA's October 2024 map of the nine candidate regions (yellow boxes), an LRO Wide Angle Camera mosaic, credit NASA/GSFC/ASU/JSC/AGDT<sup class="r">[14](#s14)</sup>. Open Moon additions: Shackleton (89.67°S 129.78°E, 21 km)<sup class="r">[15](#s15)</sup> and de Gerlache (88.5°S 87.1°W, 32.4 km)<sup class="r">[16](#s16)</sup> in cyan, placed from their published coordinates using NASA's pole marker and 50 km scale bar; the Connecting Ridge in orange, drawn rim to rim and **approximate** (no published outline yet); the Open Moon focus area in red.*

## Focus area: Shackleton – de Gerlache

Open Moon's site search concentrates on the area outlined in red, about 180 × 130 km around the south pole. It contains:

- **Shackleton crater**, whose rim the south pole lies on<sup class="r">[15](#s15)</sup>.
- **de Gerlache crater**, which has a permanently shadowed pocket in its interior<sup class="r">[16](#s16)</sup>.
- **The Connecting Ridge** between them, with the sunniest points studied so far (see the table above).
- **de Gerlache Rim 2**, the one current NASA candidate region inside the area<sup class="r">[14](#s14)</sup>. A young fault scarp has been mapped there (see the risks above)<sup class="r">[8](#s8)</sup>.

Connecting Ridge and Connecting Ridge Extension were on NASA's original 2022 list of 13 regions<sup class="r">[17](#s17)</sup> but are not among the nine published in 2024. NASA has not said why, and says regions removed for Artemis III are not ruled out for future exploration<sup class="r">[14](#s14)</sup>.

![Close-up of the Open Moon focus area: de Gerlache Rim 2, de Gerlache crater, the Connecting Ridge and Shackleton crater]({{ '/assets/sites/shackleton-de-gerlache-focus.jpg' | relative_url }})

*Close-up of the focus area (same sources and caveats as above).*

## Terrain slope in the focus area

Slope comes from NASA Goddard's LOLA slope map (LDSM) at 10 m per pixel<sup class="r">[18](#s18)</sup>, laid over NASA's LOLA hillshade. Open Moon colours it in four classes, set from what landers can actually handle (see [Lander candidates]({{ '/landers/' | relative_url }})):

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

### Landable ground, hydrogen and ice candidates

Green marks ground with slope of 8° or less (landable for every published lander rule); steeper ground is left uncoloured. **Purple** marks high hydrogen from LEND. **Blue** marks ice candidates: the permanently shadowed floors of Shackleton (233 km²) and de Gerlache (242 km²), outlined from NASA Goddard's shadow map<sup class="r">[18](#s18)</sup>, where published ice detections are reported (see the [ice research]({{ site.repo }}/blob/main/research/ice/south-pole-water-ice.md)). The white dot is ShadowCam's unexplained bright spot at 88.5352°S, 97.4007°W, inside de Gerlache's shadowed floor. Thin pale outlines are other permanently shadowed areas with no published ice data, including Spudis and the small craters along the ridge.

![Open Moon focus area: landable ground of 8° or less in green, high hydrogen in purple, ice-candidate shadowed floors in blue]({{ '/assets/sites/focus-landing-hydrogen.jpg' | relative_url }})

- **Landable:** 43 % of the focus area is 8° or less.
- **Hydrogen:** 13 % is high hydrogen, mostly the upper right (toward 0–60°E, around 88°S); 4.6 % is both landable and high hydrogen. It does not cover Shackleton, Spudis, the ridge or de Gerlache Rim 2.
- **Ice candidates:** Shackleton's floor has a bright floor in LOLA data, radar results allowing some ice in its walls, and nearby M3 ice spectra, but Kaguya and ShadowCam found no exposed ice. de Gerlache has one M3 ice spectrum and the ShadowCam bright spot. None is confirmed.
- **Why hydrogen and ice candidates differ:** LEND averages the top ~1 m over ~15 km cells, while M3 and LOLA see the top millimetres or microns at a few hundred metres. A thin frost or small patches can show in one and not the other. Only ground measurements (M01) can settle it.

## Step-by-step

1. **Build the open site database.** Pull LRO LOLA, LROC, Diviner and Mini-RF data<sup class="r">[1](#s1)</sup>, ShadowCam images<sup class="r">[2](#s2)</sup> and Chandrayaan-2 radar products<sup class="r">[3](#s3)</sup> into one public GIS.
2. **Start from NASA's shortlist.** NASA cut its Artemis III list to nine regions in October 2024: Peak near Cabeus B, Haworth, Malapert Massif, Mons Mouton Plateau, Mons Mouton, Nobile Rim 1 and 2, de Gerlache Rim 2 and Slater Plain<sup class="r">[4](#s4)</sup>. These are already screened for landing safety, light and Earth visibility.
3. **Model light and temperature** hour by hour, for every candidate, at several mast heights.
4. **Map hazards.** Include young fault scarps: NASA-funded work links the shrinking Moon to faults and moonquakes near the south pole, including a scarp in de Gerlache Rim 2, and some shadowed slopes are prone to landslides<sup class="r">[8](#s8)</sup>.
5. **Rank ice targets.** ShadowCam found little widespread surface ice, but some 20–50 m patches consistent with more than 10% ice<sup class="r">[2](#s2)</sup>. Ice is patchy, so M01 must confirm it on the ground.
6. **Check communications.** Earth visibility varies from site to site: some Earth-facing areas see Earth almost all the time, others never do<sup class="r">[7](#s7)</sup>. At the best proposed base site in a JPL study, direct-to-Earth links were available only about 51% of the time<sup class="r">[13](#s13)</sup>, so relay coverage is a hard requirement.
7. **Decide, publish and notify.** Under the Outer Space Treaty no one can claim territory<sup class="r">[11](#s11)</sup>. The Artemis Accords (78 signatories after Vietnam joined on 28 October 2026<sup class="r">[9](#s9)</sup>) ask operators to give notice and coordinate to avoid harmful interference<sup class="r">[9](#s9)</sup>. Open Moon publishes its site plan and follows that practice.

> Open question for contributors: which two sites give the best combination of illumination, ice access and distance from other programmes' planned activity?
