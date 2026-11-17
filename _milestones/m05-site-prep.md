---
id_code: M05
order: 5
title: Site preparation, landing pads and roads
phase: 1
window: "2028–2032"
summary: Robots build hardened landing pads, roads and protective berms so landers stop sandblasting the base and rovers can drive safely between sites.
objective: "Build at least two hardened landing pads that stop rocket exhaust from blasting regolith across the base, graded roads linking pads, power towers, the reactor, the ISRU plant and the habitat zone, and berms that shield key equipment from ejecta and radiation."
trl_min: 5
depends_on: [M01, M02, M04]
spec:
  - {k: Pads, v: "2 hardened pads (small/medium landers first, then heavy)"}
  - {k: Roads, v: "~5 km graded and compacted"}
  - {k: Berms, v: "Ejecta berms around pads; shielding berm for the reactor"}
  - {k: Fleet, v: "4 excavators + 2 sintering/construction robots"}
cost: {low: 3.2, high: 8.1, note: "robot fleet plus delivery; pad material is mostly local regolith"}
cost_items:
  - {item: "Excavator robots ×4 (IPEx / RASSOR class)", low: 0.1, high: 0.3, basis: "ESTIMATE"}
  - {item: "Delivery of excavators (~2 t, medium landers)", low: 0.8, high: 2.0, basis: "2 t × $0.4–1.0M/kg (mass ESTIMATE; RASSOR 2.0 is 66 kg each [src 3], IPEx larger)"}
  - {item: "Regolith sintering / construction robots ×2", low: 0.2, high: 0.5, basis: "ESTIMATE; ICON's NASA R&D contract alone is $57.2M [src 4]"}
  - {item: "Delivery of construction robots (~3 t)", low: 1.2, high: 3.0, basis: "3 t × $0.4–1.0M/kg (ESTIMATE)"}
  - {item: "Binder / additives shipped from Earth (~2 t)", low: 0.8, high: 2.0, basis: "2 t × $0.4–1.0M/kg (ESTIMATE); only if sintering alone is not enough"}
  - {item: "Engineering and operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "At least two hardened pads survive repeated landings with no measurable damage to equipment beyond 500 m."
  - "Graded roads connect every fixed site; rovers drive them autonomously."
  - "Ejecta berms around each pad and a shielding berm at the reactor."
  - "Measured ejecta during a landing on a hardened pad confirms the model used for the keep-out zones."
workstreams:
  - name: Excavation
    desc: Dig, move and level regolith.
    items: ["IPEx-class excavators (bucket drums)", "Grading and compaction", "Stockpiles for ISRU and berms"]
  - name: Landing pads
    desc: A hard surface that does not erode under a rocket plume.
    items: ["Laser or microwave sintered regolith", "Interlocking sintered pavers", "Regolith-polymer pad as fallback"]
  - name: Roads
    desc: Smooth, mapped routes between sites.
    items: ["Graded and compacted regolith", "Sintered surface on busy sections", "Marker beacons for navigation"]
  - name: Berms
    desc: Walls of piled regolith.
    items: ["Ejecta berms around pads", "Reactor shield berm", "Later: habitat burial (M09)"]
  - name: Dust control
    desc: Keep dust off everything that matters.
    items: ["Pads 1+ km from solar towers", "Sintered work areas", "Dust-tolerant seals and connectors"]
technologies:
  - {name: "NASA ISRU Pilot Excavator (IPEx)", use: "Excavation and grading", status: "TRL 5 design (2024); target 42 kg/h, 10 t over an 11-day mission; no flight date", trl: 5, src: 1}
  - {name: "RASSOR 2.0", use: "Light excavation", status: "66 kg; rated for at least 2.7 t of regolith per day (ground tests)", trl: 5, src: 3}
  - {name: "ICON Project Olympus (laser vitreous transformation)", use: "Pads, roads and structures from regolith", status: "$57.2M NASA contract through 2028; flew Duneflow test on New Shepard 2025", trl: 4, new: true, src: 4}
  - {name: "Sintered basalt pavers / regolith-polymer pads", use: "Landing pads", status: "Hot-fire tested on the ground by NASA KSC", trl: 4, new: true, src: 5}
sources:
  - {title: "NASA NTRS: IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", date: "2024"}
  - {title: "NASA NTRS: ISRU Pilot Excavator design and scaling", url: "https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf", date: "2022"}
  - {title: "NASA NTRS 20150022134: RASSOR 2.0", url: "https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf", date: "2015"}
  - {title: "ICON: ICON to develop lunar surface construction system with $57.2M NASA award", url: "https://www.iconbuild.com/newsroom/icon-to-develop-lunar-surface-construction-system-with-57-2-million-nasa-award", date: "Nov 2022"}
  - {title: "NASA: NASA tests landing pad materials for future lunar missions", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-tests-landing-pad-materials-for-future-lunar-missions", date: ""}
  - {title: "NASA NTRS: In-situ lunar launch and landing pad construction with regolith and thermoset polymers", url: "https://ntrs.nasa.gov/api/citations/20220000334/downloads/In%20situ%20Lunar%20Launch%20and%20Landing%20Pad%20Construction%20with%20Regolith%20and%20Thermoset%20Polymers%20ASCE%20Earth%20and%20Space%202022%20Paper%20SUBMITTED.pdf", date: "2022"}
  - {title: "NASA NTRS 20120000029: Lunar plume ejecta (Apollo 12 / Surveyor III)", url: "https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf", date: "2012"}
  - {title: "NASA: NASA enables construction technology for Moon and Mars exploration (Olympus, Duneflow)", url: "https://www.nasa.gov/directorates/stmd/nasa-enables-construction-technology-for-moon-and-mars-exploration/", date: "2025"}
  - {title: "Gaier, NASA/TM-2005-213610: The effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "NASA: Break the Ice Lunar Challenge winners", url: "https://www.nasa.gov/centers-and-facilities/marshall/california-teams-win-1-5-million-in-nasas-break-the-ice-lunar-challenge", date: "Jun 2024"}
risks:
  - {sev: Critical, title: "Rocket exhaust blasts regolith at roughly 300–2,000 m/s; Apollo 12 sandblasted Surveyor III ~160 m away", fix: "Hardened pads before heavy landers; berms; keep solar towers, reactor and habitat well away from pads"}
  - {sev: High, title: "Sintering a pad that survives a large methane/oxygen engine has not been demonstrated on the Moon", fix: "Test small pads with small landers first; regolith-polymer pad as fallback; scale up step by step"}
  - {sev: High, title: "Dust damages seals and mechanisms; every Apollo sample seal leaked", fix: "Dust-tolerant designs, covers, and sintered surfaces around work sites"}
  - {sev: Medium, title: "Excavation rates on the Moon are unproven (IPEx targets are design goals, not measured)", fix: "Bring more excavators than needed; measure real rates in the first month and replan"}
  - {sev: Medium, title: "Regolith properties at the site differ from simulants", fix: "Use M01 geotechnical data; adjust sintering settings on site"}
---

## Why pads come before habitats

When a lander touches down on bare regolith, its exhaust throws dust and rocks outward at roughly **300 to 2,000 m/s**. Some of that is fast enough to reach lunar orbit<sup class="r">[7](#s7)</sup>. In 1969 Apollo 12 landed about 160 m from the Surveyor III probe and sandblasted it<sup class="r">[7](#s7)</sup>. A base that expects regular cargo and crew landings has to stop this, or every landing damages the solar arrays, radiators and habitats already there.

## What exists today

- **Excavation.** NASA's IPEx is at TRL 5. It's designed to dig 10 t of regolith at 42 kg/h over an 11-day mission<sup class="r">[1](#s1)</sup><sup class="r">[2](#s2)</sup>. Its smaller predecessor, RASSOR 2.0 (66 kg), is rated for at least 2.7 t a day<sup class="r">[3](#s3)</sup>. These are ground-tested design figures, not lunar measurements.
- **Construction.** ICON's Project Olympus holds a $57.2M NASA contract through 2028 to build pads, roads and habitats by laser-melting regolith<sup class="r">[4](#s4)</sup>. Its Duneflow experiment flew on New Shepard in 2025<sup class="r">[8](#s8)</sup>.
- **Pad tests.** NASA has hot-fire tested sintered basalt pavers and regolith-polymer pads against rocket engines on the ground<sup class="r">[5](#s5)</sup><sup class="r">[6](#s6)</sup>.

## Step-by-step

1. **Survey.** Use M01 geotechnical data and the M00 hazard maps to set pad and road locations.
2. **Land the excavators** on a small lander, on the pad site itself.
3. **Grade and compact** the first pad area and the roads to the power towers.
4. **Sinter pad 1 in stages**, then test it with a small lander. Measure ejecta with cameras and witness plates.
5. **Scale up:** a larger pad 2 for medium and heavy landers, plus berms.
6. **Build roads and stockpiles.** Pile excavated regolith for the M06 ISRU feedstock and for the M09 habitat burial.

## Dust is a design requirement, not an afterthought

NASA's review of Apollo found that lunar dust abraded, clogged and fouled equipment, and that every Apollo sample container seal was compromised<sup class="r">[9](#s9)</sup>. Every Open Moon mechanism has to:

- tolerate dust
- be covered when idle
- work on sintered ground wherever possible
