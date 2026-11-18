---
id_code: M06
order: 6
title: Oxygen and water pilot plants
phase: 1
window: "2029–2033"
summary: Make the first oxygen from rock and the first water from polar ice at pilot scale, proving the processes that every later milestone depends on.
objective: "Operate an oxygen-from-regolith pilot plant and a water-from-ice pilot plant on the surface, each making at least 10 t per year, and store the products, before the first crew depends on them."
trl_min: 4
depends_on: [M01, M04, M05]
spec:
  - {k: "Oxygen plant", v: "Molten regolith electrolysis or carbothermal, ≥10 t O₂/yr"}
  - {k: "Water plant", v: "Excavate icy regolith in a PSR, heat, capture, purify; ≥10 t H₂O/yr"}
  - {k: "Power", v: "18 kW (NASA study efficiency) to ~120 kW (2024 demo efficiency) for 10 t/yr"}
  - {k: "Power interface", v: "Each plant (oxygen, water extraction, water electrolysis, storage) has its own service connection to the M04 grid and its own 120 V DC panel (plan design, DD-009); every plant within 3 km of cable run of the PMC as standard, or up to 10 km on an extended run at ~10–15% loss; PSR work beyond 10 km on the mobile power cart or a local source (DD-013, DD-014)"}
  - {k: "Storage", v: "Liquid oxygen and water tanks"}
cost: {low: 3.8, high: 9.8, note: "two pilot plants plus storage; delivery is the largest part"}
cost_items:
  - {item: "Pilot plant development (oxygen + water)", low: 0.5, high: 1.5, basis: "ESTIMATE; Blue Alchemist's 2023 NASA Tipping Point award was $34.7M for an earlier stage [src 11]"}
  - {item: "Delivery of oxygen plant (~3 t, medium lander)", low: 1.2, high: 3.0, basis: "3 t × $0.4–1.0M/kg (mass ESTIMATE)"}
  - {item: "Delivery of water plant + PSR excavator (~3 t)", low: 1.2, high: 3.0, basis: "3 t × $0.4–1.0M/kg (mass ESTIMATE)"}
  - {item: "Delivery of tanks, liquefier, electrolyser (~2 t)", low: 0.8, high: 2.0, basis: "2 t × $0.4–1.0M/kg (mass ESTIMATE)"}
  - {item: "Operations and science, 3 years", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "Oxygen plant runs autonomously for at least 6 months and produces at least 10 t of O₂ per year at a rate that scales with added modules."
  - "Water plant extracts water from PSR regolith and delivers purified water to storage at a rate of at least 10 t per year."
  - "Products are stored without loss for at least one month (cryogenic oxygen boil-off measured)."
  - "Energy per kilogram of product measured and published, to size the full plants in M11."
workstreams:
  - name: Oxygen from regolith
    desc: Split oxygen out of rock, which is about 41–45% oxygen by mass.
    items: ["Molten regolith electrolysis (Lunar Resources, Blue Alchemist)", "Carbothermal reduction (Sierra Space) as alternative", "Feedstock from M05 stockpiles"]
  - name: Water from ice
    desc: Mine icy regolith in a permanently shadowed crater.
    items: ["Excavator rated for ~40 K", "Heating in a sealed chamber to release water", "Cold-trap capture and filtration"]
  - name: Water processing
    desc: Clean water and split it on demand.
    items: ["Filtration and contaminant removal", "Water electrolysis (H₂/O₂) plant (ISS OGA heritage), on its own service connection (DD-009)", "Shared tanks with power storage (M04)"]
  - name: Storage
    desc: Keep the products.
    items: ["Liquid oxygen tanks with cryocoolers", "Water tanks kept above freezing", "Boil-off measurement"]
  - name: Scale-up data
    desc: Measure everything needed to size the full plants.
    items: ["kWh per kg O₂ and H₂O", "Electrode and crucible wear", "Feedstock variability"]
technologies:
  - {name: "Molten regolith electrolysis (NASA + Lunar Resources)", use: "Oxygen from rock", status: "2024: 25 kg of simulant processed in vacuum, 0.07 kg O₂/h for 9 h", trl: 4, new: true, src: 1}
  - {name: "Carbothermal reduction (Sierra Space + NASA)", use: "Oxygen from rock (alternative)", status: "Flight-like reactor ran automated in JSC dirty thermal-vacuum chamber (2024); key hardware matured to TRL 6", trl: 6, src: 2}
  - {name: "Blue Origin Blue Alchemist", use: "Oxygen plus silicon, iron, aluminium", status: "Passed CDR Sep 2025; autonomous demo in simulated lunar environment planned 2026", trl: 5, new: true, src: 4}
  - {name: "Molten salt electrolysis (Metalysis process, ESA)", use: "Oxygen with metal by-product", status: "ESA prototype plant opened 2020; extracts oxygen and leaves a mix of metals", trl: 4, new: true, src: 5}
  - {name: "ISS Oxygen Generation Assembly", use: "Water electrolysis", status: "Flight-proven since 2007; nominal 5.4 kg O₂/day", trl: 9, src: 6}
  - {name: "Ice excavation (NASA Break the Ice)", use: "Mining icy regolith", status: "Challenge winners 2024; designs ground-tested", trl: 4, new: true, src: 7}
sources:
  - {title: "NASA NTRS: Molten regolith electrolysis ground demonstration (ICES 2026)", url: "https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf", date: "2026"}
  - {title: "NASA NTRS 20250004151: Carbothermal oxygen production reactor testing", url: "https://ntrs.nasa.gov/citations/20250004151", date: "2025"}
  - {title: "WUSTL: Chemical composition of lunar soil", url: "https://sites.wustl.edu/meteoritesite/items/the-chemical-composition-of-lunar-soil", date: ""}
  - {title: "Blue Origin: Blue Alchemist hits major milestone", url: "https://www.blueorigin.com/news/blue-alchemist-hits-major-milestone-toward-permanent-sustainable-lunar-infrastructure", date: "Sep 2025"}
  - {title: "ESA: ESA opens oxygen plant making air out of moondust", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust", date: "Jan 2020"}
  - {title: "NASA NTRS 20190030425: ISS Oxygen Generation Assembly", url: "https://ntrs.nasa.gov/api/citations/20190030425/downloads/20190030425.pdf", date: "2019"}
  - {title: "NASA: Break the Ice Lunar Challenge winners", url: "https://www.nasa.gov/centers-and-facilities/marshall/california-teams-win-1-5-million-in-nasas-break-the-ice-lunar-challenge", date: "Jun 2024"}
  - {title: "Colozza, NASA/CR: ISRU plant power (1.63 kg/h O₂ at 25.83 kW)", url: "https://ntrs.nasa.gov/citations/20200001622", date: "Mar 2020"}
  - {title: "NASA Kennedy: NASA Kennedy breathes life into Moon soil testing", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing", date: "2025"}
  - {title: "NASA M2M-30044 Lunar Surface Data Book", url: "https://ntrs.nasa.gov/api/citations/20250002845/downloads/M2M-30044%20Lunar%20Surface%20Data%20Book%20Baseline_Final.pdf", date: "2025"}
  - {title: "NASA: 2023 NASA Tipping Point selections", url: "https://www.nasa.gov/general/2023-nasa-tipping-point-selections/", date: "Jul 2023"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface (ISRU power over 3–5 km)", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
risks:
  - {sev: Critical, title: "Oxygen-from-rock is only proven at small scale on the ground (0.07 kg/h, ~100 kWh/kg); a 10 t/yr plant needs ~1.1 kg/h and, at demo efficiency, ~120 kW", fix: "Modular cells; ground-test a full-size module and measure kWh/kg before flight; start at the output the grid can power and add cells as efficiency is proven; run two different processes"}
  - {sev: Critical, title: "Ice may be scarcer or deeper than hoped", fix: "Size the water plant from M01 drilling, not orbital estimates; oxygen-from-rock doesn't need ice and covers breathing oxygen"}
  - {sev: High, title: "Electrode and crucible wear at ~1,600 °C (MRE)", fix: "Carry spares; measure wear rates; choose inert anode materials qualified in ground tests"}
  - {sev: High, title: "Mining equipment must work at about 25–40 K inside PSRs", fix: "Short excursions from sunlit side; heated electronics; cable power from the grid"}
  - {sev: Medium, title: "Contaminants in polar ice (CO, NH₃, CH₄, mercury were seen by LCROSS)", fix: "Multi-stage purification; treat contaminants as by-products where useful"}
---

## Why this is the most important milestone

- **Oxygen** is most of the mass a crew uses: for breathing, and as the bulk of rocket propellant.
- **Shipping is expensive.** At today's published prices of $1.2M per kg to the surface (see M02), every tonne made locally instead of shipped saves on the order of a billion dollars.
- **Rock is mostly oxygen.** Lunar rock and soil is about **41–45% oxygen by mass**<sup class="r">[3](#s3)</sup>.
- **Polar ice gives water directly.** LCROSS found ejecta water "on the order of five percent"<sup class="r">[10](#s10)</sup>.

## How ready are the processes?

| Process | Best demonstration so far | Readiness |
|---|---|---|
| Molten regolith electrolysis | 0.07 kg O₂/h for 9 h from 25 kg simulant, in vacuum, 2024<sup class="r">[1](#s1)</sup>; NASA's first molecular oxygen from this process<sup class="r">[9](#s9)</sup> | TRL 4 |
| Carbothermal reduction | Flight-like reactor, automated, in NASA's "dirty" thermal-vacuum chamber, 2024<sup class="r">[2](#s2)</sup> | TRL 6 |
| Blue Alchemist (MRE) | CDR passed Sep 2025; demo planned for 2026<sup class="r">[4](#s4)</sup> | TRL 5 (estimate) |
| Molten salt electrolysis (Metalysis) | ESA prototype plant (2020); oxygen out, a mix of metals left<sup class="r">[5](#s5)</sup> | TRL 4 |
| Water electrolysis | ISS OGA, flight-proven, 5.4 kg O₂/day<sup class="r">[6](#s6)</sup> | TRL 9 |

None of the regolith processes has run on the Moon yet. That's why this is a **pilot**, and why two different oxygen processes are flown.

## Sizing (this plan's arithmetic)

- **Production rate.** 10 t of O₂ a year works out to about 1.14 kg/h.
- **Power: the big uncertainty.**
  - NASA's 2020 study puts a 1.63 kg/h plant at about 26 kW<sup class="r">[8](#s8)</sup>, roughly **16 kWh per kg** of oxygen. On that basis the pilot needs about 18 kW.
  - NASA's 2024 electrolysis demo ran at about 9 kW peak for 0.07 kg/h<sup class="r">[1](#s1)</sup>. That is about **100 kWh per kg** (this plan's arithmetic from the published figures).
  - At demo efficiency, the 26 kW budgeted from M04 would make only about **2 t a year**. Reaching 10 t a year would need about **120 kW**.
  - Demonstration reactors are small and lose most of their heat, so efficiency should improve with size. How much it improves is exactly what this pilot has to measure.
- **Who it supports.** At 0.895 kg of O₂ per person per day (NASA BVAD, see M09), 10 t a year is enough to breathe for about **30 people**. Most of the oxygen will eventually go to propellant instead (M11).

## Power: one service connection per plant

{% include decision-note.html id="DD-009" extra="The ISRU plants used to share one ISRU microgrid. Each plant now has its own service connection and panel." %}

Each plant connects to the M04 grid like a house: a service drop, a UMIC-class converter to 120 V DC, a meter, a main breaker and its own 120 V DC panel (plan design, see C04.4). That applies to the oxygen plant, the water-extraction plant, the water electrolysis (H₂/O₂) plant and the storage site. A fault in one plant trips only its own breaker, and the power system can shed one plant without touching the others.

**Within 3 km of the PMC as standard, 10 km at most (design changes DD-013 and DD-014).** The standard power run in the base is 3 km of cable or less (plan design, DD-013). NASA expects ISRU to need power over 3–5 km<sup class="r">[12](#s12)</sup>. So the oxygen plant, the water-extraction and electrolysis plants and the storage site sit within 3 km of cable run of the PMC where they can, and otherwise run on grid power over an extended run of up to 10 km, at about 10–15% loss, with voltage regulation at the plant end and a 1 kHz stability analysis for the run (plan design, DD-014). Ice mining inside a shadowed crater more than 10 km of cable away is powered by the mobile power cart (PBS PW.5) or a local source, and the water is carried back to the plants by tanker (open; see C06.2).

{% include decision-note.html id="DD-013" extra="The plants could sit wherever the ice and the regolith stockpile were. Now they must sit within 3 km of cable run of the PMC." %}

{% include decision-note.html id="DD-014" extra="Plants at NASA's 3–5 km distance can now run on grid power over extended runs of up to 10 km." %}

## Step-by-step

1. **Ground-qualify a full-size module** of each process on Earth, using simulant matched to the M01 soil data.
2. **Land the oxygen plant** next to the M05 regolith stockpile, within 3 km of cable run of the PMC, or up to 10 km on an extended run (DD-013, DD-014), and connect it to the grid through its own service connection.
3. **Land the water plant** with a cold-rated excavator at the edge of the best PSR from M01, with its own service connection. If that PSR edge is more than 3 km of cable from the PMC, feed it by an extended run of up to 10 km (DD-014); beyond 10 km, power the mine from the mobile power cart (PW.5) or a local source (DD-013, DD-014).
4. **Run continuously for six months.** Measure output, energy per kg and wear.
5. **Store and use the products.** Liquefy and store oxygen; feed water into the M04 fuel-cell storage and keep a reserve for the crew.
6. **Publish all the data** to size the full plants in M11.
