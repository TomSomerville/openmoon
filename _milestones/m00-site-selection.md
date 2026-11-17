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
  - {name: "Lunar Reconnaissance Orbiter (LRO)", use: "Terrain, imagery, temperature and radar data for site selection", status: "Operating; funded to support Artemis and CLPS site characterisation", trl: 9, src: 1}
  - {name: "ShadowCam on KPLO/Danuri", use: "Images inside permanently shadowed craters", status: "Operating; mission expected to end about late 2027 to early 2028", trl: 9, src: 2}
  - {name: "Chandrayaan-2 orbiter DFSAR radar", use: "Radar evidence of subsurface ice", status: "Operating in 2026", trl: 9, src: 3}
  - {name: "NASA Artemis south-pole candidate regions", use: "Starting shortlist of pre-screened regions", status: "9 regions published Oct 2024 (for Artemis III)", trl: 9, src: 4}
sources:
  - {title: "NASA FY2026 budget request summary (LRO funding for Artemis/CLPS site characterisation)", url: "https://www.nasa.gov/wp-content/uploads/2025/05/fy2026-budget-request-summary-briefing-finalv2-05292025-430pm.pdf", date: "May 2025"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "Drishti IAS: Chandrayaan-2 finds evidence of possible subsurface ice (secondary)", url: "https://www.drishtiias.com/daily-updates/daily-news-analysis/chandrayaan-2-finds-evidence-of-possible-subsurface-ice-on-moon", date: "May 2026"}
  - {title: "NASA NTRS 20250011660: Artemis III Site Selection Update", url: "https://ntrs.nasa.gov/citations/20250011660", date: "2026"}
  - {title: "Peak of eternal light (Bussey et al. 2010; Speyerer & Robinson 2013 figures), Wikipedia", url: "https://en.wikipedia.org/wiki/Peak_of_eternal_light", date: "accessed Nov 2026"}
  - {title: "LROC: Islands in the Dark (Shackleton rim illumination)", url: "https://www.lroc.asu.edu/images/1105", date: ""}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "NASA: Shrinking Moon causing moonquakes and faults near lunar south pole", url: "https://www.nasa.gov/solar-system/moon/shrinking-moon-causing-moonquakes-and-faults-near-lunar-south-pole/", date: "Jan 2024"}
  - {title: "NASA: Artemis Accords (Section 11, deconfliction and safety zones)", url: "https://www.nasa.gov/artemis-accords/", date: ""}
  - {title: "NASA: Uzbekistan becomes 77th Artemis Accords signatory", url: "https://nasa.gov/organizations/oiir/artemis-accords/nasa-welcomes-uzbekistan-as-newest-artemis-accords-signatory", date: "Oct 2026"}
  - {title: "UNOOSA: Outer Space Treaty (Article II)", url: "https://www.unoosa.org/pdf/publications/ST_SPACE_51E.pdf", date: ""}
  - {title: "NASA Moon Base – Phases", url: "https://www.nasa.gov/moonbase-phases/", date: "2026"}
risks:
  - {sev: High, title: "ShadowCam's mission ends around late 2027 to early 2028, cutting off new images inside shadowed craters", fix: "Request targeted ShadowCam imaging of candidate PSRs now; archive everything; plan our own prospecting in M01"}
  - {sev: High, title: "Other programmes want the same few sunlit ridges (NASA Moon Base, China's Chang'e-7 near Shackleton)", fix: "Choose a primary and backup site; publish plans early and coordinate under Artemis Accords deconfliction; design for shared infrastructure"}
  - {sev: High, title: "Young fault scarps and landslide-prone slopes near some candidate regions (e.g. de Gerlache Rim 2)", fix: "Map scarps from LROC NAC; keep pads, reactors and habitats off and away from young faults"}
  - {sev: Medium, title: "Earth is only visible from the south pole about half of each month", fix: "Treat relay satellites as mandatory (M03); pick sites with long Earth-visibility windows for the first lander"}
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
| Three Shackleton-rim points combined | >90% | LROC<sup class="r">[6](#s6)</sup> |

**Design consequence:** spread solar arrays across two or three nearby high points so that at least one is almost always lit, and raise them on masts. The longest darkness at a single point can still be days long, so the base still needs storage and fission power (see M04).

## Step-by-step

1. **Build the open site database.** Pull LRO LOLA, LROC, Diviner and Mini-RF data<sup class="r">[1](#s1)</sup>, ShadowCam images<sup class="r">[2](#s2)</sup> and Chandrayaan-2 radar products<sup class="r">[3](#s3)</sup> into one public GIS.
2. **Start from NASA's shortlist.** NASA cut its Artemis III list to nine regions in October 2024: Peak near Cabeus B, Haworth, Malapert Massif, Mons Mouton Plateau, Mons Mouton, Nobile Rim 1 and 2, de Gerlache Rim 2 and Slater Plain<sup class="r">[4](#s4)</sup>. These are already screened for landing safety, light and Earth visibility.
3. **Model light and temperature** hour by hour, for every candidate, at several mast heights.
4. **Map hazards.** Include young fault scarps: NASA-funded work links the shrinking Moon to faults and moonquakes near the south pole, including a scarp in de Gerlache Rim 2, and some shadowed slopes are prone to landslides<sup class="r">[8](#s8)</sup>.
5. **Rank ice targets.** ShadowCam found little widespread surface ice, but some 20–50 m patches consistent with more than 10% ice<sup class="r">[2](#s2)</sup>. Ice is patchy, so M01 must confirm it on the ground.
6. **Check communications.** Earth is in view from the south pole for only about half of each month<sup class="r">[7](#s7)</sup>, so relay coverage is a hard requirement.
7. **Decide, publish and notify.** Under the Outer Space Treaty no one can claim territory<sup class="r">[11](#s11)</sup>. The Artemis Accords (77 signatories as of October 2026<sup class="r">[10](#s10)</sup>) ask operators to give notice and coordinate to avoid harmful interference<sup class="r">[9](#s9)</sup>. Open Moon publishes its site plan and follows that practice.

> Open question for contributors: which two sites give the best combination of illumination, ice access and distance from other programmes' planned activity?
