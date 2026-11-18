---
id_code: "C09.1"
milestone: M08
order: 5
title: Regolith radiation shielding
summary: "A delivered arch over the habitat modules, covered with at least 2 m of loose regolith. It cuts the crew's radiation dose, steadies the temperature and stops micrometeoroids, while leaving a gallery so the habitat can still be inspected."
trl: 4
spec:
  - {k: "Cover depth", v: "≥2 m everywhere, 3 m on the roof (plan design choice)"}
  - {k: "Areal density", v: "~300 g/cm² at 2 m, ~450 g/cm² at 3 m (ESTIMATE, 1.5 g/cm³ placed regolith)"}
  - {k: "Modelled dose inside", v: "~150 mSv per 180 days at 2 m, ~100 mSv at 3 m (one OLTARIS study, no EVA)"}
  - {k: "When", v: "Finished and dose-checked before the first crew lands (M08, DD-005)"}
  - {k: "Regolith moved", v: "~4,300 t (2 m) to ~6,800 t (3 m) for 3 modules (ESTIMATE; PROVISIONAL, from MPH-sized modules in a line)"}
  - {k: "Placement time", v: "~225–355 days with 4 excavators at 200 kg/h each (ESTIMATE)"}
  - {k: "Static load on arch", v: "~4.9 kPa (2 m) to ~7.3 kPa (3 m) (ESTIMATE)"}
  - {k: "Arch structure mass", v: "~10 t (ESTIMATE, ~330 m² at ~30 kg/m²; PROVISIONAL)"}
  - {k: "Clear envelope", v: "5 m wide × 4.5 m high × 26 m long over 3 modules in a line (PROVISIONAL; DD-007 puts the 3 modules side by side, so the arch shape will change once the module design exists)"}
  - {k: "Design life", v: "≥10 years (matches the habitat module life)"}
  - {k: "Delivery", v: "Arch and dosimetry on one heavy cargo lander; regolith is local"}
subcomponents:
  - name: Support arch
    desc: "A metal vault built over the modules carries the regolith, so the habitat skin never touches it."
    parts: ["Corrugated aluminium arch segments", "Footings on a graded, compacted pad", "Flexible membrane over the arch", "Load cells and strain gauges", "Geo-mat netting to steepen the outer slopes"]
    tech: "NASA Lunar Safe Haven baseline concept 1.1A"
    trl: 3
  - name: Regolith overburden
    desc: "Loose regolith is dug, carried and piled over the arch, then lightly compacted in layers."
    parts: ["Excavator fleet (C05.1)", "Layer compaction roller", "Depth survey markers", "Slope profile surveys (lidar)"]
    tech: "IPEx / RASSOR excavation; Lunar Safe Haven bulk overburden"
    trl: 4
  - name: End walls and entrances
    desc: "The open ends of the vault are closed with stacked regolith bags and a bent entrance tunnel so radiation has no straight path in."
    parts: ["Regolith-filled Vectran bags", "Bag filling station", "Dog-leg entrance tunnel", "Dust door at the tunnel mouth"]
    tech: "Lunar Safe Haven concept 1.2 (sandbags)"
    trl: 3
  - name: Inspection gallery
    desc: "A crawl space between the module and the arch lets crew or a small robot check seals, hatches and the hull."
    parts: ["0.5–1 m crawl space around each module", "Fixed cameras and lights", "Removable arch access panels", "Small inspection robot on a rail"]
    tech: "Lunar Safe Haven access goal; ISS external inspection practice"
    trl: 4
  - name: Thermal pass-through
    desc: "Regolith is a near-perfect insulator, so a buried module can neither radiate nor conduct its heat away. Almost all of it is piped out to radiators on the surface."
    parts: ["Pumped fluid loop through the overburden", "Surface radiator panels with dust covers", "Insulated pipe sleeves", "Habitat heaters for low-load periods"]
    tech: "ISS external active thermal control heritage"
    trl: 5
  - name: Dosimetry network
    desc: "Area monitors, personal dosimeters and a dose-versus-depth test stack measure what the shield really does."
    parts: ["HERA-class area monitors in each module", "Crew Active Dosimeters (one per person)", "Passive dosimeters for whole-stay totals", "Regolith dose-depth test stack (20 to >100 g/cm²)", "Data link to Earth radiation team"]
    tech: "HERA and Crew Active Dosimeter (Artemis I); NASA thick-shield experiment concept"
    trl: 7
risks:
  - {sev: Critical, title: "At 2 m, one model gives ~165 mSv per 6.5-month tour (this plan's arithmetic from ~150 mSv per 180 days), so about 3.6 tours reach the 600 mSv career limit even with no EVA", fix: "Build 3 m on the roof where people sleep (~110 mSv per tour, ~5.5 tours); run OLTARIS on the real geometry; give each person a dose budget and cap their number of tours."}
  - {sev: High, title: "No measured dose-depth data exists beyond ~100 g/cm², and studies disagree (2 m minimum vs 3–7 m)", fix: "Fly the regolith dose-depth test stack before crew arrive; measure inside the finished shield; add depth if numbers are worse than models."}
  - {sev: High, title: "Burial is slow: ~1 year with 4 excavators at 200 kg/h, ~3–5 years at the IPEx design rate, and it must now finish before the first crew lands (DD-005)", fix: "Start piling as soon as the arch is up; add excavators; set the first crew date by measured burial progress."}
  - {sev: High, title: "Arch failure would drop tonnes of regolith onto a pressurised module", fix: "Design the arch to carry the full load on its own with margin; monitor load cells; add regolith in even layers on both sides."}
  - {sev: Medium, title: "A buried hull cannot be seen or repaired", fix: "Keep the inspection gallery and access panels; never pile regolith directly on the module."}
  - {sev: High, title: "Buried modules overheat: regolith conducts only ~0.003–0.013 W/m·K, so the cover passes ~0.05–0.2 kW against a 20–50 kW habitat load, and a pumped-loop failure has no passive backup", fix: "Surface radiators on two independent pumped loops; size them for the 9-person peak load before burial; load-shed plan if a loop fails; keep heaters for low-power periods."}
  - {sev: Medium, title: "No lunar bag-filling system exists yet", fix: "Use bulk regolith for most of the cover; limit bags to end walls; develop and test a filler on Earth first."}
  - {sev: Medium, title: "Dust gets into the gallery and entrance", fix: "Dust door at the tunnel mouth; membrane over the arch; sintered ground at the entrance."}
sources:
  - {title: "Zhang et al., Science Advances: first measurements of the radiation dose on the lunar surface (Chang'e-4)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "Savage, IAC-24 abstract: Radiation shielding for long-term lunar settlements with regolith (OLTARIS, BON2020)", url: "https://iafastro.directory/iac/paper/id/82864/abstract-pdf/IAC-24,D3,IP,1,x82864.brief.pdf", date: "2024"}
  - {title: "NASA OCHMO-TB-020: Design for ionizing radiation protection (NASA-STD-3001 technical brief)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf", date: "Dec 2022"}
  - {title: "Clowdsley, NASA LaRC: Protecting astronauts from space radiation on the lunar surface (LSIC talk)", url: "https://ntrs.nasa.gov/api/citations/20210009760/downloads/Clowdsley_Lunar_Radiation_Talk_v2.pdf", date: "Feb 2021"}
  - {title: "Simonsen and Slaba, NASA: Galactic cosmic radiation shielding, science on the lunar surface (NASEM)", url: "https://ntrs.nasa.gov/api/citations/20250006713/downloads/nasem_presentation%20v07012025%20vf.pdf", date: "2025"}
  - {title: "Grande et al., NASA: Protecting crew and surface systems with a long-duration Lunar Safe Haven (ASCEND 2021)", url: "https://ntrs.nasa.gov/api/citations/20210022066/downloads/Grande_Lunar%20Safe%20Haven_ASCEND%202021_Full_v2b.docx.pdf", date: "2021"}
  - {title: "Connolly, NASA JSC: An engineering guide to lunar geotechnical properties", url: "https://ntrs.nasa.gov/api/citations/20220014634/downloads/Final%20IEEE%20paper%20formatted%20footnote%20added.pdf", date: "2023"}
  - {title: "Nagihara et al., LPSC 2015: Restoration of the Apollo heat flow experiments metadata", url: "https://ntrs.nasa.gov/api/citations/20150004428/downloads/20150004428.pdf", date: "2015"}
  - {title: "Evans et al., NASA MSFC: Meteoroid risk assessment of lunar habitat concepts", url: "https://ntrs.nasa.gov/api/citations/20060024733/downloads/20060024733.pdf", date: "2006"}
  - {title: "NASA: Artemis I radiation measurements validate Orion safety for astronauts", url: "https://www.nasa.gov/humans-in-space/artemis-i-radiation-measurements-validate-orion-safety-for-astronauts/", date: "Oct 2024"}
  - {title: "NASA NTRS: IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", date: "2024"}
  - {title: "Langseth et al., Proc. Lunar Sci. Conf.: Revised lunar heat-flow values (Apollo 15 and 17 regolith conductivity)", url: "https://www.osti.gov/biblio/5787569", date: "1976"}
  - {title: "Hayne et al., JGR Planets: Global regolith thermophysical properties of the Moon from Diviner", url: "https://arxiv.org/pdf/1711.00977", date: "2017"}
  - {title: "NASA GRC (via C08.1): habitat power draw 20–50 kW for 4 crew", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
---

## What it does

Unshielded, the lunar surface gives about **1,369 µSv per day**<sup class="r">[1](#s1)</sup>. That is about 246 mSv in six months, or about 271 mSv in a 6.5-month tour (this plan's arithmetic), against NASA's **600 mSv** career limit<sup class="r">[3](#s3)</sup>. This component puts a thick layer of regolith between the crew and the sky. The same layer also steadies the temperature and stops micrometeoroids.

## How much regolith? There is no single NASA number

NASA has not set a design depth for regolith shielding. The published work points in different directions:

- **Thin shields.** NASA guidance is to surround crew with about 20 g/cm² of hydrogen-rich material. Adding more non-hydrogen material beyond that can *raise* the dose, unless you add metres of it, as in a buried habitat<sup class="r">[4](#s4)</sup>.
- **One OLTARIS study.** Dose rose with regolith depth up to about 1 m, because of secondary particles. The study concluded that **at least 2 m** is needed. That gives about **150 mSv per 180-day mission**, and 3 m gives about **100 mSv**. These figures assume no EVA<sup class="r">[2](#s2)</sup>.
- **NASA Lunar Safe Haven study.** It used a **3 m threshold and a 7 m goal**<sup class="r">[6](#s6)</sup>.
- **Data gap.** NASA lists dose behind more than 100 g/cm² as unmeasured. It proposes a lunar test that puts a detector under thicker and thicker layers of regolith<sup class="r">[5](#s5)</sup>.

Open Moon keeps its working value of **≥2 m everywhere**. It builds **3 m over the sleeping quarters**, because sleep is where crew spend the most hours. It then checks the result with OLTARIS and with measurements.

## When it is built

- **Before the first crew (plan design, DD-005).** The ≥2 m cover everywhere and the 3 m cover over the sleeping quarters are finished in Phase 1, by robots, before crew 1 lands.
- **Why.** There are no sorties any more. An unshielded 6.5-month tour would cost about 271 mSv, 45% of the 600 mSv career limit (this plan's arithmetic). Piling regolith next to an occupied module would also put people and excavators in the same work zone.
- **Cost of the choice.** The burial time in the sizing table below sits directly on the path to the first crew landing.
- **Layout.** DD-007 places three standard modules side by side and connects them. The arch was sized for three MPH-sized modules in a line, so its figures are provisional until the module design exists.

## How it works

**Support arch.** Following NASA's Lunar Safe Haven baseline, a delivered metal structure is built over the habitat and regolith is piled on top. The regolith never touches the habitat skin, and the outside of the habitat stays reachable for maintenance<sup class="r">[6](#s6)</sup>.

**Placement.** The study found that loose regolith works without any processing. It also found that digging and dumping need little power, generally under 200 W<sup class="r">[6](#s6)</sup>. The study team took the angle of repose to be about 55°. Geo-mats could steepen the slopes and shrink the footprint<sup class="r">[6](#s6)</sup>.

**End walls.** The study looked at Vectran sandbags, but noted that no system for filling them exists yet<sup class="r">[6](#s6)</sup>. Open Moon uses bags only to close the vault ends.

**Thermal.** Regolith is one of the best natural insulators known. This cuts both ways.

- **How good an insulator.** Apollo 15 and 17 long-term heater runs put the bulk regolith at **0.009–0.013 W/m·K**<sup class="r">[12](#s12)</sup>. Diviner orbital data gives **0.00074 W/m·K at the surface**, rising to **0.0034 W/m·K at about 1 m** depth<sup class="r">[13](#s13)</sup>. The near-surface fines are poor conductors because the loose grains touch at few points and there is no air between them.
- **Good: steady surroundings.** Apollo heat-flow sensors below 90 cm read within about 0.1 K of their December 1974 values when checked in 1975<sup class="r">[8](#s8)</sup>. Under 2–3 m of cover, the habitat sees almost none of the surface swing between lunar day and night. The modules need far less heater power in shadow than on the open surface, and the hull stops thermal cycling.
- **Bad: heat cannot leave.** The crew, the electronics and life support turn nearly all of the habitat's 20–50 kW<sup class="r">[14](#s14)</sup> into heat. Through 2 m of regolith only a fraction of a kilowatt gets out (see Sizing). The rest would warm the module and the soil around it with no limit. So nearly all of the heat must go out on a pumped fluid loop to radiators on the surface, and that loop is life-critical: if it stops, the cover provides no passive backup.
- **Placement matters.** The crawl-space gallery between hull and arch is in vacuum, so the hull exchanges heat with the arch only by radiation. Pipe runs through the overburden need insulated sleeves so the loop doesn't lose or gain heat on the way to the radiators.

**Micrometeoroids.** A NASA study found that impact risk drives wall thickness and burial depth<sup class="r">[9](#s9)</sup>. The Lunar Safe Haven study says thick regolith gives ample micrometeorite protection. It rejected an ISS-style Whipple shield (about 11.5 cm thick) as the only protection, because it stops too little radiation<sup class="r">[6](#s6)</sup>.

**Dosimetry.** HERA area monitors and Crew Active Dosimeters were tested on the ISS and flew on Artemis I<sup class="r">[10](#s10)</sup>.

## Sizing (ESTIMATE)

The arch's clear space is 5 m × 4.5 m × 26 m. The slopes are 45°, which is more conservative than 55°. Placed regolith is taken as 1.5 g/cm³. For comparison, natural regolith is 1.30 g/cm³ at the surface and 1.52 g/cm³ at 10 cm depth<sup class="r">[7](#s7)</sup>.

| Cover (PROVISIONAL) | Volume | Mass | Days at 4 × 200 kg/h | Days at 4 × 42 kg/h (IPEx target<sup class="r">[11](#s11)</sup>) |
|---|---|---|---|---|
| 2 m | ~2,900 m³ | ~4,300 t | ~225 | ~1,070 |
| 3 m | ~4,550 m³ | ~6,800 t | ~355 | ~1,690 |

**Load on the arch:** 3 m × 1,500 kg/m³ × 1.62 m/s² ≈ **7.3 kPa** (4.9 kPa at 2 m).

**Heat leak through the cover:** q = k × ΔT ÷ thickness. Take k = 0.0034–0.013 W/m·K<sup class="r">[12](#s12)</sup><sup class="r">[13](#s13)</sup>, a 100 K difference between the warm inner face and the cold ground, and 2 m of cover. That gives 0.17–0.65 W/m². Over the ~330 m² arch, about **55–215 W** gets out. That is **under 1%** of a 20–50 kW habitat load<sup class="r">[14](#s14)</sup>. The 100 K difference is an assumption. Even if it were several times larger, conduction would still remove only a few percent.

## Testing and qualification

1. Load-test a full-scale arch segment on Earth to 2× the 3 m load, with simulated moonquake shaking.
2. Pile simulant over a mock-up and measure the slopes and how the layers settle.
3. Model the full geometry in OLTARIS<sup class="r">[4](#s4)</sup>.
4. On the Moon, fly the dose-depth stack first<sup class="r">[5](#s5)</sup>.
5. Build the arch, bury it, and survey the depth.
6. Compare the HERA readings inside with the readings outside before the first crew lands (M08 exit criterion).

## Open questions

- How deep is deep enough? Can a measured dose-depth curve be produced before the habitat modules are buried (Year 7 on the roadmap)?
- Does the 1 m secondary-radiation peak appear for real south-pole regolith?
- What angle of repose does excavated polar regolith hold in practice?
- How many 6.5-month tours can one person fly within 600 mSv once EVA dose is added?
- How does the arch change for three modules side by side (DD-007)?
- How warm does the regolith next to the arch get over 10 years of small heat leaks, and does that matter for the arch or the hull?
