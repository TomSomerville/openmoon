---
id_code: "C08.2"
milestone: M08
order: 2
title: Life support system
summary: "ISS-derived equipment that keeps the habitat air breathable and recycles water for four crew, topped up with oxygen and water from the M06 pilot plants."
trl: 7
spec:
  - {k: "Crew supported", v: "4 (design point), 30-day stays"}
  - {k: "Cabin atmosphere", v: "8.2 psia, 34% O₂ (NASA exploration atmosphere; design choice)"}
  - {k: "O₂ demand", v: "3.58 kg/day for 4 crew (BVAD)"}
  - {k: "O₂ generation", v: "~5.4 kg/day nominal (ISS OGA class, 12 lbm/day)"}
  - {k: "CO₂ removal", v: "4.6 kg/day at 2 torr (4BCO2 class); 2 units"}
  - {k: "Water recovery", v: "≥90%; 98% shown on ISS with brine processor"}
  - {k: "O₂ recovery from CO₂", v: "~50% (Sabatier, methane vented)"}
  - {k: "Mass", v: "~2 t installed (ESTIMATE)"}
  - {k: "Power", v: "Part of the 20–50 kW habitat load (breakdown TBD)"}
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
  - {sev: High, title: "CO₂ removal runs close to capacity (4.34 kg/day made vs 4.6 kg/day removed at 2 torr)", fix: "Fly two 4BCO2-class units and run both when crew are aboard; LiOH canisters as an emergency backup"}
  - {sev: High, title: "ISS CO₂ removal has cost more crew hours than any other ISS system, mostly from zeolite dust", fix: "Use the 4BCO2 design, which targets 3 years with no unplanned maintenance; carry spare beds and valves"}
  - {sev: High, title: "Urine processor recovery fell from 85% design to 70% in service on ISS", fix: "Add the Brine Processor Assembly; size water reserves on 90% recovery, not 98%"}
  - {sev: High, title: "Lunar dust in the cabin clogs fans, filters and valves", fix: "Dust lock and suitports (C08.3); extra pre-filters on all air inlets; scheduled filter changes"}
  - {sev: Medium, title: "Sabatier vents methane, so only ~50% of O₂ is recovered from CO₂", fix: "Accept on the Moon; make up oxygen with M06 regolith oxygen; consider methane pyrolysis later"}
  - {sev: Medium, title: "Uncrewed 3-month run can hide failures that only appear under crew load", fix: "Simulate crew load with CO₂, humidity and water injection during the uncrewed run"}
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

## What it does

Life support keeps four people alive inside the habitat (C08.1). It controls pressure and gas mix, makes oxygen, removes CO₂ and trace gases, recycles water, and detects and fights fire. Every major unit has flown on the ISS. The work in M08 is to package them for 1/6 g, dust and a 30-day crew.

## How it works

- **Atmosphere.** The ISS runs at sea-level pressure, 101.3 kPa<sup class="r">[4](#s4)</sup>. This plan's design choice is NASA's candidate exploration atmosphere: **8.2 psia with 34% oxygen**. NASA tested it in chambers for future habitats and pre-spacewalk procedures. NASA notes that lower pressure needs more oxygen, which may raise fire risk, and its chamber trials had several cases of decompression sickness<sup class="r">[10](#s10)</sup>.
- **Oxygen.** The ISS Oxygen Generation Assembly splits water. It was designed for **12 lbm/day (~5.4 kg)**, enough for 4 crew, and can run between 5.1 and 20.4 lbm/day<sup class="r">[5](#s5)</sup>.
- **CO₂ removal.** The new 4-Bed CO₂ Scrubber removes 4 crew-equivalents of CO₂: **4.6 kg/day at 2 torr**, 6.8 kg/day at 3 torr. It aims for 3 years with no unplanned maintenance. Its predecessor, CDRA, cost more crew hours than any other ISS system, mostly because of zeolite dust<sup class="r">[6](#s6)</sup>.
- **Trace gases.** A charcoal bed, a catalytic oxidiser and a lithium hydroxide bed<sup class="r">[2](#s2)</sup>. The oxidiser runs at 400 °C and needs 120 W on average<sup class="r">[8](#s8)</sup>.
- **Water.** The urine processor was designed for 85% recovery but runs at 70%<sup class="r">[4](#s4)</sup>. Adding the brine processor raised total ISS water recovery from 93–94% to **98%** in 2023<sup class="r">[3](#s3)</sup>. NASA's reference page still quotes about 90% for routine use<sup class="r">[2](#s2)</sup>.
- **Sabatier.** It turns CO₂ and hydrogen into water and methane. Venting the methane loses hydrogen, so only about **50%** of the oxygen in CO₂ comes back<sup class="r">[7](#s7)</sup>.
- **Fire.** ISS uses photoelectric smoke detectors in the ventilation intakes and portable extinguishers holding 6 lb of CO₂ at 850 psi that empty in 45 s<sup class="r">[9](#s9)</sup>.

## Sizing: daily mass balance, 4 crew

Per-person values from NASA BVAD Rev2, Table 3-31 and Table 4-20 (early planetary base)<sup class="r">[1](#s1)</sup>, multiplied by 4.

| Stream | Per person (kg/day) | 4 crew (kg/day) |
|---|---|---|
| O₂ consumed | 0.895 | 3.58 |
| CO₂ produced | 1.085 | 4.34 |
| Drinking water | 3.217 | 12.87 |
| Water in food | 0.760 | 3.04 |
| Food solids | 0.800 | 3.20 |
| Hygiene water (flush, wash, shower) | 1.98 | 7.92 |
| Urine water out | 1.420 | 5.68 |
| Breath and sweat water out | 2.946 | 11.78 |
| Metabolic water made | 0.490 | 1.96 |

What the equipment must do (ESTIMATE, from the table):

- **OGA** load 3.58 ÷ 5.44 = 66%. Water feed 3.58 × 9/8 = **4.03 kg/day**.
- **4BCO2** load 4.34 ÷ 4.6 = 94% at 2 torr. Too tight for one unit, so two are flown.
- **Sabatier** gets 3.58 ÷ 8 = 0.45 kg/day of hydrogen. That reduces about 2.4 kg of CO₂ and returns about **2.0 kg/day** of water, roughly half the OGA feed.
- **Water make-up** (conservative, ignoring water from food and metabolism): (1 − 0.90) × (12.87 + 7.92) + (4.03 − 2.0) ≈ **4.1 kg/day**, or ~123 kg for a 30-day sortie. Open loop would need ~25 kg/day, or ~750 kg.

## Testing and qualification

1. **Integrated ground test** of the full system in a closed chamber at 8.2 psia, 34% O₂, with four people for 30 days.
2. **Dust test.** Inject lunar simulant into the air loop and measure filter and fan life.
3. **1/6 g check.** Fly the water separators and Sabatier on parabolic flights to prove gas-liquid separation works in partial gravity.
4. **On the Moon, uncrewed.** Run for 3 months with simulated crew loads (CO₂, humidity, water) before the first crew.
5. **Sortie 1.** Measure the real balance against this table; adjust M06 top-up rates.

## Open questions

- Is 8.2 psia / 34% O₂ safe enough for fire, or should early sorties run at a higher pressure?
- How do the urine and water processors behave in 1/6 g? ISS data is all from microgravity.
- How much nitrogen leaks per day from the habitat and dust lock? This sets the nitrogen still shipped from Earth.
- Can M06 water meet drinking standards without extra treatment?
