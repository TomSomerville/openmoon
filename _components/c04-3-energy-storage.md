---
id_code: "C04.3"
milestone: M04
order: 3
title: Energy storage (regenerative fuel cells and batteries)
summary: "The fission battery takes all of the reactor's output through a charger and battery management system, and the base draws fission power only from it. Regenerative fuel cells store solar energy as hydrogen and oxygen for long shadows. Li-ion also handles fast peaks and start-ups."
trl: 5
spec:
  - {k: "Stored energy", v: "~3 MWh net (30 kW essential load for 100 h)"}
  - {k: "Fuel cell power", v: "30 kW continuous in 2 × 25 kW modules (plan design)"}
  - {k: "Round-trip efficiency", v: "~35% modelled at the south pole; ~80% theoretical maximum"}
  - {k: "Reactants", v: "~150 kg H₂ + ~1.2 t O₂ from ~1.4 t water (ESTIMATE)"}
  - {k: "Gas pressure", v: "Up to ~12.4 MPa (1,800 psia)"}
  - {k: "RFC mass", v: "4.6–9.4 t at 320–650 Wh/kg; ~3 t new hardware if ISRU tanks are shared (ESTIMATE)"}
  - {k: "Fission battery", v: "160 kWh per 20 kWe reactor in 2 strings, ~1 t at 160 Wh/kg, with charger and BMS (plan design, DD-002)"}
  - {k: "Li-ion peak buffer", v: "~100 kWh, ~0.6 t at 160 Wh/kg (plan design)"}
  - {k: "Recharge power", v: "~29–43 kW of solar over 200–300 h (ESTIMATE)"}
  - {k: "Delivery", v: "Medium lander; tanks may arrive with the M06 oxygen plant"}
subcomponents:
  - name: Electrolyser
    desc: "Splits water into hydrogen and oxygen using daytime power, and pumps the gases up to storage pressure inside the stack."
    parts: ["PEM electrolyser stack with reinforced membrane", "High-pressure water feed pump", "Hydrogen and oxygen water separators", "Water recirculation pump", "Stack pressure enclosure"]
    tech: "NASA GRC breadboard RFC (balanced pressure to 12.4 MPa)"
    trl: 5
  - name: Fuel cell stack
    desc: "Recombines hydrogen and oxygen into water and electricity during shadow."
    parts: ["PEM fuel cell stack, non-flow-through", "Passive internal water separation", "Auxiliary cell for product-water degassing", "Reactant pressure regulators", "Stack voltage monitor"]
    tech: "NASA GRC breadboard RFC"
    trl: 5
  - name: Reactant storage
    desc: "Holds the hydrogen and oxygen between charge and discharge."
    parts: ["Spherical hydrogen tanks", "Spherical oxygen tanks", "Tank heaters (keep above 4 °C)", "Latching valves", "Pressure and temperature sensors", "Hydrogen leak detectors"]
    tech: "Composite pressure vessels; shared with M06 ISRU tanks where possible"
    trl: 5
  - name: Water management
    desc: "Collects product water and keeps it clean enough to electrolyse again."
    parts: ["Product water tank", "Deionising bed", "Water quality sensor", "Make-up water link to M06 water plant", "Freeze protection"]
    tech: "RFC breadboard water loop"
    trl: 4
  - name: Thermal control
    desc: "Removes stack waste heat by day and keeps water and gas lines warm in the dark."
    parts: ["Coolant pump loop", "Heat exchangers", "Radiator panel", "Insulated enclosure (MLI)", "Heaters"]
    tech: "RFC breadboard thermal loop"
    trl: 5
  - name: Fission charger and BMS
    desc: "Ends the reactor's 3 kV AC line at the base. Converts it to battery charging voltage, and the battery management system controls charging, balances cells and stops charging when full (Reactor > BMS > Battery > Base, DD-002)."
    parts: ["Step-down transformer and rectifier (UMIC-class AC-to-DC converter)", "Charge controller per battery string", "Battery management system: cell voltage, current and temperature monitoring", "Cell balancing", "String isolation contactors", "Command link to the reactor controller"]
    tech: "NASA GRC UMIC AC-to-DC converter (2023); terrestrial and ISS battery management practice"
    trl: 4
  - name: Fission battery strings
    desc: "Store the reactor's output and feed the base bus. Sized for 8 hours at full reactor output, enough to ride through one reactor restart."
    parts: ["160 kWh per 20 kWe reactor, in two independent strings", "Commercial Li-ion cells", "Module heaters and heated enclosure", "Discharge converter to the 120 V DC base bus"]
    tech: "COTS cell packs as used in NASA FSP concept"
    trl: 5
  - name: Li-ion battery modules
    desc: "Cover fast load steps, fuel cell warm-up and reactor start-up."
    parts: ["Commercial 18650 cells (LG MJ1 class)", "Battery management electronics", "Spare string", "Module heaters", "Heated enclosure"]
    tech: "COTS cell packs as used in NASA FSP concept"
    trl: 6
  - name: Power electronics and control
    desc: "Connects storage to the grid and runs the system without people."
    parts: ["Bidirectional DC–DC converter to the 120 VDC microgrid", "Small flight computer (CubeSat class)", "Safe-state logic", "Telemetry link"]
    tech: "NASA GRC RFC breadboard controller"
    trl: 5
risks:
  - {sev: Critical, title: "All fission power passes through the charger, BMS and fission battery (DD-002); a fault there cuts the base off from the reactor.", fix: "Two independent strings, each with its own charger and BMS; either string alone can take the full 20 kWe; a failed string isolates itself and the reactor dumps surplus to its parasitic load radiator."}
  - {sev: Critical, title: "Low round-trip efficiency (~35% at the pole): every 1 kWh delivered needs about 3 kWh of daytime power.", fix: "Size solar for recharge; choose lower electrolyser pressure and better membranes to raise efficiency. Fission power reaches the base only through its battery, so it cannot recharge the fuel cells directly."}
  - {sev: High, title: "The NASA breadboard needed five manual restarts in 550 hours, four from thermal control and one from water management.", fix: "Run a long closed-loop test with redundant thermal control and automatic recovery before flight."}
  - {sev: High, title: "Only open-loop operation has been shown; gases were vented, not stored and reused.", fix: "Add a closed-loop ground test at ≥5 kW for many simulated lunar cycles as a gate before buying flight units."}
  - {sev: High, title: "Hydrogen crossing into oxygen nears the flammability limit above ~2,000 psia.", fix: "Keep storage at or below ~1,800 psia; add hydrogen-in-oxygen sensors and automatic shutdown."}
  - {sev: High, title: "Mass: 3 MWh of storage is 5–9 t of hardware.", fix: "Share tanks and water with the M06 oxygen plant; use modular 25 kW units; let the fission battery carry the essential load through the night."}
  - {sev: Medium, title: "Tank heating is a large parasitic load in shadow.", fix: "Bury or berm tanks; route fuel cell waste heat to them; test whether dry gas tanks can run colder."}
  - {sev: Medium, title: "Li-ion cells lose capacity sharply in the cold and stop working below about −60 °C.", fix: "Keep batteries in heated enclosures inside the habitat or ISRU plant thermal zone."}
  - {sev: Medium, title: "ISRU water may carry contaminants that poison membranes.", fix: "Deionise make-up water; keep the RFC water loop separate except for metered top-ups."}
sources:
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Cain et al., NASA GRC: Performance of a Regenerative Fuel Cell System for the Lunar Surface (NTRS 20260002730)", url: "https://ntrs.nasa.gov/citations/20260002730", date: "Apr 2026"}
  - {title: "Smith et al., NASA GRC: Lunar South Pole Regenerative Fuel Cell System Efficiency Analysis", url: "https://ntrs.nasa.gov/api/citations/20220010931/downloads/E-20059%20Conference%20Paper.pdf", date: "2022"}
  - {title: "Smith et al., NASA/TM-20210014627: Lunar Equator Regenerative Fuel Cell System Efficiency Analysis", url: "https://ntrs.nasa.gov/citations/20210014627", date: "Aug 2022"}
  - {title: "Oleson et al., NASA GRC: A Deployable 40 kWe Lunar Fission Surface Power Concept (NETS 2022)", url: "https://ntrs.nasa.gov/citations/20220004670", date: "May 2022"}
  - {title: "JPL: Low-temperature lithium-ion batteries for lunar and planetary missions (poster)", url: "https://www.jpl.nasa.gov/site/research/media/posters/2021/R21219p.pdf", date: "2021"}
  - {title: "Wikipedia: Faraday constant", url: "https://en.wikipedia.org/wiki/Faraday_constant", date: "2026"}
  - {title: "NASA Glenn: SPARC Industry Day presentation (Lunar Reactor-1 requirements)", url: "https://sam.gov/api/prod/opps/v3/opportunities/resources/files/6b927f8dc6c843749a45b2c0589bf0e7/download", date: "Sep 2026"}
  - {title: "Thomas et al., NASA GRC: A Modular AC to DC Interface Converter (UMIC) to Enable Lunar Surface Power Transmission", url: "https://ntrs.nasa.gov/citations/20230013309", date: "Sep 2023"}
---

## What it does

{% include decision-note.html id="DD-002" extra="Storage now includes the fission battery: the reactor only charges it, and the base draws fission power only from it." %}

Storage has two jobs.

**1. Fission battery (Reactor > BMS > Battery > Base).** The reactor's 3 kV AC line ends here. A charger converts it to battery voltage, and the battery management system (BMS) watches each cell, balances them and stops charging when the battery is full. The base draws its fission power only from this battery. An LR-1-class reactor makes at least 20 kWe and must accept any load from 0 to 100%, dumping the rest into its parasitic load radiator<sup class="r">[8](#s8)</sup>, so the BMS can cut charging at any time. NASA Glenn has built a modular AC-to-DC converter for this kind of lunar link<sup class="r">[9](#s9)</sup>.

**2. Solar storage.** It covers the hours when no sunlight reaches the towers and the fission battery alone is not enough. It also covers the years before the reactor arrives. Polar shadows last up to about 100 hours<sup class="r">[1](#s1)</sup>. A regenerative fuel cell (RFC) stores more energy per kilogram than batteries: 320–650 Wh/kg against about 160 Wh/kg for packaged Li-ion<sup class="r">[1](#s1)</sup>. Batteries stay in the system for fast peaks.

## How it works

- **Charge.** By day, a PEM electrolyser splits water. The stack compresses its own gases, so no separate compressor is needed<sup class="r">[2](#s2)</sup>.
- **Discharge.** In shadow, a PEM fuel cell recombines the gases into water and electricity. Making the fuel cell large and running it at low current density gives the best efficiency without much extra mass<sup class="r">[3](#s3)</sup>.
- **Tanks.** In large systems, gas storage is nearly 60% of RFC mass<sup class="r">[3](#s3)</sup>. Spherical tanks raise specific energy by about 50%<sup class="r">[3](#s3)</sup>. In NASA's equator study, cryogenic storage dropped efficiency below 15%, so gas storage is used<sup class="r">[3](#s3)</sup>.
- **Pressure.** Lower electrolyser pressure raises efficiency. Going from 4,000 to 2,000 psia gains 3–5 points. Above ~2,000 psia, hydrogen leaking into the oxygen nears the flammability limit<sup class="r">[3](#s3)</sup>.
- **Losses.** For a 50 kW RFC, parasitic loads during discharge add up to about 3.9 kW. Power electronics take 2.5 kW, tank heaters 0.7 kW, and pumps and valves the rest<sup class="r">[3](#s3)</sup>. The model keeps the tanks above 4 °C<sup class="r">[3](#s3)</sup>.
- **Batteries.** NASA's fission concept used a 4 kWh pack of commercial cells at about 173 Wh/kg, with a spare string<sup class="r">[5](#s5)</sup>. The best low-temperature Li-ion cells work only down to −60 °C and need heaters in shadow<sup class="r">[6](#s6)</sup>.

## Sizing

| Step | Arithmetic | Result |
|---|---|---|
| Net energy needed | 30 kW × 100 h (M04 design case) | 3.0 MWh |
| Fuel cell gross output | 3.0 MWh + ~8% parasitics<sup class="r">[3](#s3)</sup> | ~3.24 MWh |
| Energy per kg of water (ESTIMATE) | 2 × 96,485 C/mol<sup class="r">[7](#s7)</sup> × 0.8 V cell = 42.9 Wh/mol; × 55.5 mol/kg | ~2.38 kWh/kg |
| Water cycled | 3.24 MWh ÷ 2.38 kWh/kg | ~1.36 t |
| Hydrogen / oxygen | 2/18 and 16/18 of the water | ~152 kg H₂ / ~1.21 t O₂ |
| Tank volume at 12.4 MPa, 20 °C (ESTIMATE, ideal gas, +7% for H₂) | H₂ ~16 m³; O₂ ~7.4 m³ | ~24 m³ |
| Charge energy | 3.0 MWh ÷ 0.35 round-trip<sup class="r">[3](#s3)</sup> | ~8.6 MWh |
| Recharge power (ESTIMATE) | 8.6 MWh over 200–300 h of sun | ~29–43 kW |
| RFC system mass | 3 MWh ÷ 320–650 Wh/kg<sup class="r">[1](#s1)</sup> | 4.6–9.4 t |
| Same energy in Li-ion | 3 MWh ÷ 160 Wh/kg<sup class="r">[1](#s1)</sup> | ~19 t |
| Li-ion peak buffer (plan design) | 100 kWh ÷ 160 Wh/kg | ~0.6 t |
| Fission battery (plan design, DD-002) | 20 kWe × 8 h = 160 kWh ÷ 160 Wh/kg | ~1 t per reactor |
| Fission energy into the battery | 20 kWe × 24 h | 480 kWh/day |

Modelled south-pole efficiency is 34.8% for a 10 kW RFC and 36.6% at 50 kW. Above about 25 kW there is little gain, so two 25 kW units give redundancy at almost no cost in efficiency<sup class="r">[3](#s3)</sup>. With a 50% round-trip efficiency, the solar array must make about 3 times the RFC's output power<sup class="r">[4](#s4)</sup>.

## Testing and qualification

1. **Done.** NASA Glenn's breadboard RFC ran autonomously for more than 550 hours of simulated lunar cycles, at balanced pressures up to 12.4 MPa. It ran open-loop (bottled gas in, products vented) and had five unplanned safe-state stops<sup class="r">[2](#s2)</sup>.
2. **Closed-loop breadboard.** Store and reuse the same gas and water for many simulated cycles, with no venting.
3. **5–25 kW engineering unit.** Test in thermal vacuum with flight-like tanks, at the cold sink temperatures of the chosen site.
4. **Tank sharing test.** Run the RFC with water from an ISRU simulant loop (M06) to check membrane life.
5. **On the Moon.** Start with a single 25 kW module carrying only non-essential loads. Move essential loads onto it after a full year without faults.
6. **Fission battery.** Before the reactor lands, test the charger, BMS and both strings on solar power. Check that a string fault isolates only that string, and that a full battery stops charging cleanly.

## Open questions

- Should the fission battery also feed the regenerative fuel cells, so spare reactor power can be stored for long shadows?
- Can dry gas tanks sit at lunar shadow temperatures instead of being heated above 4 °C?
- What membrane thickness and pressure give the best balance for this base's duty cycle?
- How long do PEM stacks last over thousands of lunar charge cycles?
- Could cryogenic oxygen from the M06 plant replace part of the oxygen tankage?
