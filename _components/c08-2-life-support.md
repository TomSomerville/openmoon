---
id_code: "C08.2"
milestone: M08
order: 2
title: Life support system
summary: "ISS-derived equipment that keeps the habitat air breathable and recycles water for 6 people continuously and 9 at handover peaks, topped up with oxygen and water from the M06 pilot plants."
trl: 7
spec:
  - {k: "Crew supported", v: "6 continuous, 9 for ~2 weeks at each handover (DD-006); 6.5-month tours"}
  - {k: "Layout", v: "Three strings, one per habitat module, each sized for 3 people (plan design; placement set with the module design, DD-007)"}
  - {k: "Cabin atmosphere", v: "8.2 psia, 34% O₂ (NASA exploration atmosphere; design choice)"}
  - {k: "O₂ demand", v: "5.37 kg/day for 6, 8.06 kg/day for 9 (BVAD)"}
  - {k: "O₂ generation", v: "~5.4 kg/day nominal each (ISS OGA class, 12 lbm/day); 3 units"}
  - {k: "CO₂ removal", v: "4.6 kg/day at 2 torr each (4BCO2 class); 3 units"}
  - {k: "Water recovery", v: "≥90%; 98% shown on ISS with brine processor"}
  - {k: "O₂ recovery from CO₂", v: "~50% (Sabatier, methane vented)"}
  - {k: "Mass", v: "~2 t per string installed (ESTIMATE, the earlier 4-crew figure, now a placeholder)"}
  - {k: "Power", v: "Part of the 20–50 kW habitat load (breakdown TBD)"}
  - {k: "Power interface", v: "Inside each module: branch circuits on that module's 120 V DC panel. Any life-support processing outside the habitats has its own service connection and panel (plan design, DD-009)"}
subcomponents:
  - name: Atmosphere control and monitoring
    desc: "Holds cabin pressure and oxygen fraction, adds nitrogen to make up leaks, and measures the main gases."
    parts: ["Pressure control valves and relief valves", "Nitrogen and oxygen storage tanks", "Major constituent analyser (N₂, O₂, CO₂, H₂, CH₄, H₂O)", "Cabin fans and humidity condensing heat exchanger"]
    tech: "ISS pressure control and Major Constituent Analyzer"
    trl: 8
  - name: Oxygen generation
    desc: "Splits water into oxygen for the cabin and hydrogen for the Sabatier reactor."
    parts: ["Electrolysis cell stack", "Power supply module", "Water recirculation loop and deioniser bed", "Hydrogen sensors and hydrogen outlet"]
    tech: "ISS Oxygen Generation Assembly (OGA)"
    trl: 9
  - name: CO₂ removal
    desc: "Pulls exhaled CO₂ out of the cabin air with regenerable sorbent beds."
    parts: ["Two desiccant beds", "Two zeolite sorbent beds", "Valves and blower", "Pleated dust filter", "CO₂ outlet to Sabatier or vent"]
    tech: "ISS 4-Bed CO₂ Scrubber (4BCO2), CDRA heritage"
    trl: 7
  - name: Trace contaminant control
    desc: "Removes gases released by people, materials and equipment."
    parts: ["Activated charcoal bed (heavy organics, ammonia)", "High-temperature catalytic oxidiser (methane, CO, light organics)", "Post-sorbent bed for acid gases", "Particulate filters"]
    tech: "ISS Trace Contaminant Control Subassembly (TCCS)"
    trl: 9
  - name: Water recovery
    desc: "Turns urine, sweat, humidity and wash water back into drinking water."
    parts: ["Urine Processor Assembly (vacuum distillation)", "Brine Processor Assembly", "Water Processor Assembly (filters and catalytic reactor)", "Potable water storage and quality monitor"]
    tech: "ISS Water Recovery System with BPA"
    trl: 9
  - name: CO₂ reduction (Sabatier)
    desc: "Combines CO₂ with hydrogen from the oxygen generator to make water, which is fed back to electrolysis."
    parts: ["Sabatier catalytic reactor", "Water separator", "Methane vent line", "Controller and sensors"]
    tech: "ISS Sabatier (ACLS / CRS heritage)"
    trl: 8
  - name: Fire detection and suppression
    desc: "Finds a fire early and puts it out without making the cabin unbreathable."
    parts: ["Photoelectric smoke detectors in ventilation intakes", "Portable fire extinguishers", "Emergency breathing masks", "Post-fire atmosphere clean-up filters"]
    tech: "ISS Fire Detection and Suppression system"
    trl: 8
risks:
  - {sev: Critical, title: "Fire risk is higher in a 34% oxygen atmosphere", fix: "Strict materials control, ISS-class smoke detection in every ventilation intake, water-mist or CO₂ extinguishers, masks for every crew member, and the option to run at a lower O₂ fraction"}
  - {sev: High, title: "At a 9-person handover, CO₂ removal runs at ~71% of three units' capacity at 2 torr (9.77 kg/day made vs 13.8 kg/day), and losing one unit leaves 9.2 kg/day, below the load", fix: "Fly three 4BCO2-class units; if one fails during a handover, accept up to 3 torr (6.8 kg/day per unit) or shorten the handover; LiOH canisters as an emergency backup"}
  - {sev: High, title: "ISS CO₂ removal has cost more crew hours than any other ISS system, mostly from zeolite dust", fix: "Use the 4BCO2 design, which targets 3 years with no unplanned maintenance; carry spare beds and valves"}
  - {sev: High, title: "Urine processor recovery fell from 85% design to 70% in service on ISS", fix: "Add the Brine Processor Assembly; size water reserves on 90% recovery, not 98%"}
  - {sev: High, title: "Lunar dust in the cabin clogs fans, filters and valves", fix: "Dust lock and suitports (C08.3); extra pre-filters on all air inlets; scheduled filter changes"}
  - {sev: Medium, title: "Sabatier vents methane, so only ~50% of O₂ is recovered from CO₂", fix: "Accept on the Moon; make up oxygen with M06 regolith oxygen; consider methane pyrolysis later"}
  - {sev: Medium, title: "Uncrewed 3-month run can hide failures that only appear under crew load", fix: "Simulate loads for 6 people, and for 9 for at least 2 weeks, with CO₂, humidity and water injection during the uncrewed run"}
sources:
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): Life Support Baseline Values and Assumptions", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "NASA: Environmental Control and Life Support Systems reference", url: "https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss", date: "Apr 2025"}
  - {title: "Space.com: ISS hits 98% water recycling milestone", url: "https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone", date: "Jun 2023"}
  - {title: "Wikipedia: ISS ECLSS", url: "https://en.wikipedia.org/wiki/ISS_ECLSS", date: "2026"}
  - {title: "Takada et al., ICES-2019-107: Advanced Oxygen Generation Assembly for Exploration Missions", url: "https://ntrs.nasa.gov/api/citations/20190030425/downloads/20190030425.pdf", date: "Jul 2019"}
  - {title: "Cmarik et al., ICES-2020-178: 4-Bed CO₂ Scrubber, from design to build", url: "https://ntrs.nasa.gov/api/citations/20205003542/downloads/ICES-2020-178.docx", date: "2020"}
  - {title: "Yates et al., ICES-2019-103: Hydrogen recovery by methane pyrolysis (Sabatier ~50% O₂ recovery)", url: "https://ntrs.nasa.gov/api/citations/20190030371/downloads/20190030371.pdf", date: "Jul 2019"}
  - {title: "NASA TM 20210026041: Adsorbents and catalysts for atmosphere revitalization (TCCS)", url: "https://ntrs.nasa.gov/citations/20210026041", date: "Dec 2021"}
  - {title: "NASA NTRS 20030053429: Overview of ISS U.S. Fire Detection and Suppression System", url: "https://ntrs.nasa.gov/citations/20030053429", date: "2001"}
  - {title: "NASA NTRS 20220015741: Medical lessons learned from the Exploration Atmospheres study (8.2 psia, 34% O₂)", url: "https://ntrs.nasa.gov/citations/20220015741", date: "2022"}
---

{% include decision-note.html id="DD-006" extra="Life support was sized for 4 crew on 30-day sorties. It is now sized for 6 people all the time and 9 for about two weeks at each handover, on 6.5-month tours." %}

## What it does

Life support keeps the crew alive inside the three connected habitat modules (C08.1). It controls pressure and gas mix, makes oxygen, removes CO₂ and trace gases, recycles water, and detects and fights fire. Every major unit has flown on the ISS. The work in M08 is to package them for 1/6 g, dust, **6 people continuously and 9 at handover peaks** (DD-006), and to run them uncrewed before the first crew lands.

## How it works

- **Atmosphere.** The ISS runs at sea-level pressure, 101.3 kPa<sup class="r">[4](#s4)</sup>. This plan's design choice is NASA's candidate exploration atmosphere: **8.2 psia with 34% oxygen**. NASA tested it in chambers for future habitats and pre-spacewalk procedures. NASA notes that lower pressure needs more oxygen, which may raise fire risk, and its chamber trials had several cases of decompression sickness<sup class="r">[10](#s10)</sup>.
- **Oxygen.** The ISS Oxygen Generation Assembly splits water. It was designed for **12 lbm/day (~5.4 kg)**, enough for 4 crew, and can run between 5.1 and 20.4 lbm/day<sup class="r">[5](#s5)</sup>.
- **CO₂ removal.** The new 4-Bed CO₂ Scrubber removes 4 crew-equivalents of CO₂: **4.6 kg/day at 2 torr**, 6.8 kg/day at 3 torr. It aims for 3 years with no unplanned maintenance. Its predecessor, CDRA, cost more crew hours than any other ISS system, mostly because of zeolite dust<sup class="r">[6](#s6)</sup>.
- **Trace gases.** A charcoal bed, a catalytic oxidiser and a lithium hydroxide bed<sup class="r">[2](#s2)</sup>. The oxidiser runs at 400 °C and needs 120 W on average<sup class="r">[8](#s8)</sup>.
- **Water.** The urine processor was designed for 85% recovery but runs at 70%<sup class="r">[4](#s4)</sup>. Adding the brine processor raised total ISS water recovery from 93–94% to **98%** in 2023<sup class="r">[3](#s3)</sup>. NASA's reference page still quotes about 90% for routine use<sup class="r">[2](#s2)</sup>.
- **Sabatier.** It turns CO₂ and hydrogen into water and methane. Venting the methane loses hydrogen, so only about **50%** of the oxygen in CO₂ comes back<sup class="r">[7](#s7)</sup>.
- **Fire.** ISS uses photoelectric smoke detectors in the ventilation intakes and portable extinguishers holding 6 lb of CO₂ at 850 psi that empty in 45 s<sup class="r">[9](#s9)</sup>.

## Sizing: daily mass balance, 6 and 9 people

Per-person values from NASA BVAD Rev2, Table 3-31 and Table 4-20 (early planetary base)<sup class="r">[1](#s1)</sup>, multiplied by 6 and by 9 (this plan's arithmetic).

| Stream | Per person (kg/day) | 6 people (kg/day) | 9 people (kg/day) |
|---|---|---|---|
| O₂ consumed | 0.895 | 5.37 | 8.06 |
| CO₂ produced | 1.085 | 6.51 | 9.77 |
| Drinking water | 3.217 | 19.30 | 28.95 |
| Water in food | 0.760 | 4.56 | 6.84 |
| Food solids | 0.800 | 4.80 | 7.20 |
| Hygiene water (flush, wash, shower) | 1.98 | 11.88 | 17.82 |
| Urine water out | 1.420 | 8.52 | 12.78 |
| Breath and sweat water out | 2.946 | 17.68 | 26.51 |
| Metabolic water made | 0.490 | 2.94 | 4.41 |

What the equipment must do (ESTIMATE, from the table; three strings, one per module):

- **OGA.** 6 people need 5.37 kg/day: 33% of three units' 16.3 kg/day nominal, or one unit at 99%. 9 people need 8.06 kg/day: 49% of three units. One unit can run up to 20.4 lbm/day (~9.3 kg)<sup class="r">[5](#s5)</sup>. Water feed is 5.37 × 9/8 = **6.04 kg/day** for 6.
- **4BCO2.** 6 people make 6.51 kg/day: 47% of three units at 2 torr (13.8 kg/day), and 71% if one unit is down. 9 people make 9.77 kg/day: 71% of three units.
- **Sabatier** gets 5.37 ÷ 8 = 0.67 kg/day of hydrogen for 6 people and returns about **3.0 kg/day** of water, roughly half the OGA feed.
- **Water make-up** for 6 (conservative, ignoring water from food and metabolism): (1 − 0.90) × (19.30 + 11.88) + (6.04 − 3.0) ≈ **6.2 kg/day**, or ~1.2 t per 198-day tour. For 9 people it is about **9.2 kg/day**. Open loop would need ~37 kg/day for 6.

## Testing and qualification

1. **Integrated ground test** of the full system in a closed chamber at 8.2 psia, 34% O₂, with six people for several weeks and nine for two weeks.
2. **Dust test.** Inject lunar simulant into the air loop and measure filter and fan life.
3. **1/6 g check.** Fly the water separators and Sabatier on parabolic flights to prove gas-liquid separation works in partial gravity.
4. **On the Moon, uncrewed.** Run for 3 months with simulated loads for 6 people, and 9 for at least 2 weeks (CO₂, humidity, water), before the first crew.
5. **First crew.** Measure the real balance against this table; adjust M06 top-up rates before the first handover.

## Open questions

- Is 8.2 psia / 34% O₂ safe enough for fire, or should the first crews run at a higher pressure?
- How do the urine and water processors behave in 1/6 g? ISS data is all from microgravity.
- How much nitrogen leaks per day from the habitat and dust lock? This sets the nitrogen still shipped from Earth.
- Can M06 water meet drinking standards without extra treatment?
