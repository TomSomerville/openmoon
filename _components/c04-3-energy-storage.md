---
id_code: "C04.3"
milestone: M04
order: 3
title: BMS and energy storage (power routing, batteries, regenerative fuel cells)
summary: "The BMS is the hub of the base's power: every source feeds it, and it routes power to the grid to meet demand, into storage, or both. Storage is a Li-ion battery bank for peaks and reactor restarts, and regenerative fuel cells that store surplus as hydrogen and oxygen for long shadows."
trl: 5
spec:
  - {k: "Stored energy", v: "~3 MWh net (30 kW essential load for 100 h)"}
  - {k: "Fuel cell power", v: "30 kW continuous in 2 × 25 kW modules (plan design)"}
  - {k: "Round-trip efficiency", v: "~35% modelled at the south pole; ~80% theoretical maximum"}
  - {k: "Reactants", v: "~150 kg H₂ + ~1.2 t O₂ from ~1.4 t water (ESTIMATE)"}
  - {k: "Gas pressure", v: "Up to ~12.4 MPa (1,800 psia)"}
  - {k: "RFC mass", v: "4.6–9.4 t at 320–650 Wh/kg; ~3 t new hardware if ISRU tanks are shared (ESTIMATE)"}
  - {k: "BMS", v: "Central routing hub in two independent halves (A/B) with a cross-tie; all sources in, grid and storage out (plan design, DD-003)"}
  - {k: "Li-ion battery bank", v: "~260 kWh: 160 kWh per 20 kWe reactor (8 h ride-through) + ~100 kWh for peaks; ~1.6 t at 160 Wh/kg; several strings (plan design)"}
  - {k: "Recharge power", v: "~29–43 kW of BMS surplus (solar or reactor) over 200–300 h (ESTIMATE)"}
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
  - name: BMS routing hub
    desc: "Receives every source (reactor, solar towers) and decides, moment to moment, whether power goes to the grid to meet demand, into storage, or both. Feeds the grid from the battery when generation is short, has the fuel cells recharge the battery (their output goes only to the battery, never to the feeders), and sheds loads by priority as a last resort (DD-003)."
    parts: ["Input converters for each source (UMIC-class AC-to-DC for the 3 kV AC lines)", "Common DC bus, split into halves A and B with a cross-tie", "Output converters to the 3 kV AC trunk and 120 V DC microgrids", "Routing and priority controller with load-shedding tables", "Source and feeder switching to either half", "Fuel-cell discharge path to the battery strings only (no path to the feeders)", "Command links to the reactor, solar towers and fuel cells", "Telemetry and Earth link"]
    tech: "NASA GRC UMIC bidirectional converter (2023); NASA lunar microgrid priority control concept; ISS power management practice"
    trl: 4
  - name: Li-ion battery bank
    desc: "Fast storage behind the BMS. Covers load steps, fuel cell warm-up, and 8 hours of reactor output for a reactor restart. The BMS manages each cell: voltage, current, temperature, balancing and charge limits."
    parts: ["~260 kWh in several independent strings", "Commercial Li-ion cells (LG MJ1 class, 18650)", "Cell monitoring and balancing electronics", "String isolation contactors", "Module heaters and heated enclosure", "Spare string"]
    tech: "COTS cell packs as used in NASA FSP concept"
    trl: 5
  - name: Power electronics and control
    desc: "Connects the fuel cells and electrolyser to the BMS and runs them without people."
    parts: ["Bidirectional DC–DC converter to the BMS bus", "Small flight computer (CubeSat class)", "Safe-state logic", "Telemetry link"]
    tech: "NASA GRC RFC breadboard controller"
    trl: 5
risks:
  - {sev: Critical, title: "Every watt passes through the BMS (DD-003); a BMS fault could cut every source off from every load.", fix: "Two independent BMS halves (A/B), each able to carry the essential loads, with a cross-tie; every source and feeder switchable to either half; battery in several strings; ground-test failover before flight."}
  - {sev: High, title: "The BMS routing software sets priorities for the whole base and must work through gaps in contact with Earth.", fix: "Simple, fixed priority tables (life support first); hardware-in-the-loop tests of every routing case; safe default if the controller resets."}
  - {sev: Critical, title: "Low round-trip efficiency (~35% at the pole): every 1 kWh delivered needs about 3 kWh of daytime power.", fix: "The BMS sends any surplus, solar or reactor, to the electrolyser once the battery is full; size solar for recharge; choose lower electrolyser pressure and better membranes to raise efficiency."}
  - {sev: High, title: "The NASA breadboard needed five manual restarts in 550 hours, four from thermal control and one from water management.", fix: "Run a long closed-loop test with redundant thermal control and automatic recovery before flight."}
  - {sev: High, title: "Only open-loop operation has been shown; gases were vented, not stored and reused.", fix: "Add a closed-loop ground test at ≥5 kW for many simulated lunar cycles as a gate before buying flight units."}
  - {sev: High, title: "Hydrogen crossing into oxygen nears the flammability limit above ~2,000 psia.", fix: "Keep storage at or below ~1,800 psia; add hydrogen-in-oxygen sensors and automatic shutdown."}
  - {sev: High, title: "Mass: 3 MWh of storage is 5–9 t of hardware.", fix: "Share tanks and water with the M06 oxygen plant; use modular 25 kW units; let the reactor, through the BMS, carry the essential load through the night."}
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

{% include decision-note.html id="DD-003" extra="This component now includes the BMS, the hub every source feeds and every load and store draws from." %}

![Diagram: fission reactors and solar towers feed the BMS; the grid is fed by generation or by the battery, and the fuel cells recharge the battery; surplus with storage full is curtailed or dumped to the reactor's parasitic load radiator](/assets/tech/base-power-bms-flow.svg)

**The BMS.** Every source sends its power to the BMS: the reactor's 3 kV AC line and the solar towers. The BMS decides whether that power goes to the grid to meet demand, into storage, or some of each (design change DD-003). **The grid is fed only by generation passing through the BMS, or by the battery.** The fuel cells never feed the grid directly; when they discharge, they recharge the battery. In this plan BMS means the whole power management and routing system, including battery cell management.

Default routing (plan design):
1. Meet grid demand, highest priority first. NASA's lunar microgrid concept also serves the highest-priority loads, such as the crewed habitat, first<sup class="r">[1](#s1)</sup>.
2. Charge the Li-ion battery with surplus.
3. With the battery full, run the electrolyser to fill the fuel-cell tanks.
4. With all storage full, curtail solar and let the reactor dump surplus into its parasitic load radiator. An LR-1-class reactor must accept any load from 0 to 100%<sup class="r">[8](#s8)</sup>, so the BMS can change its draw at any time.
5. When short: the battery feeds the grid, the fuel cells recharge the battery, and as a last resort loads are shed by priority.

NASA Glenn has built a modular, bidirectional converter between 120 V DC equipment and the 3 kV AC grid<sup class="r">[9](#s9)</sup>, the kind of converter the BMS uses at each input and output.

![One-line diagram: each solar tower and the reactor send 3 kV AC over a source line to an input converter on BMS half A or half B, joined by a cross-tie; Li-ion battery strings hang off each half; the fuel cells are charged from BMS surplus and discharge only into the battery, with no direct path to the grid; output converters send 3 kV AC feeders to transformers and UMICs at the 120 V DC habitat and ISRU microgrids](/assets/tech/base-power-one-line.svg)

**Inside the hub (plan design).** Each source line ends at an input converter on half A or half B. The two halves are DC buses joined by a cross-tie, and any source or feeder can be switched to either half. Battery strings hang off both halves: a starter string on half A and the reactor ride-through strings on half B. The fuel-cell electrolyser draws from the bus; the fuel cells discharge only into the battery strings. Output converters feed the 3 kV AC feeders to the microgrids.

**Storage** has two layers behind the BMS:
- **Li-ion battery bank** for fast response: load steps, fuel cell warm-up, and 8 hours of reactor output for a reactor restart.
- **Regenerative fuel cells** for long shadows and the years before the reactor arrives. They are charged by BMS surplus and, when they discharge, they recharge the battery rather than feeding the grid. Polar shadows last up to about 100 hours<sup class="r">[1](#s1)</sup>. A regenerative fuel cell (RFC) stores more energy per kilogram than batteries: 320–650 Wh/kg against about 160 Wh/kg for packaged Li-ion<sup class="r">[1](#s1)</sup>.

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
| Li-ion: reactor ride-through (plan design) | 20 kWe × 8 h = 160 kWh ÷ 160 Wh/kg | ~1 t per reactor |
| Li-ion: peaks (plan design) | 100 kWh ÷ 160 Wh/kg | ~0.6 t |
| Reactor energy into the BMS | 20 kWe × 24 h | 480 kWh/day |

Modelled south-pole efficiency is 34.8% for a 10 kW RFC and 36.6% at 50 kW. Above about 25 kW there is little gain, so two 25 kW units give redundancy at almost no cost in efficiency<sup class="r">[3](#s3)</sup>. With a 50% round-trip efficiency, the solar array must make about 3 times the RFC's output power<sup class="r">[4](#s4)</sup>.

## Testing and qualification

1. **Done.** NASA Glenn's breadboard RFC ran autonomously for more than 550 hours of simulated lunar cycles, at balanced pressures up to 12.4 MPa. It ran open-loop (bottled gas in, products vented) and had five unplanned safe-state stops<sup class="r">[2](#s2)</sup>.
2. **Closed-loop breadboard.** Store and reuse the same gas and water for many simulated cycles, with no venting.
3. **5–25 kW engineering unit.** Test in thermal vacuum with flight-like tanks, at the cold sink temperatures of the chosen site.
4. **Tank sharing test.** Run the RFC with water from an ISRU simulant loop (M06) to check membrane life.
5. **On the Moon.** Start with a single 25 kW module carrying only non-essential loads. Move essential loads onto it after a full year without faults.
6. **BMS.** Build both halves on the ground with simulated sources and loads. Test every routing case: demand only, surplus to battery, surplus to electrolyser, storage full, shortfall, and loss of half A or B. On the Moon, half A arrives with the first solar tower, so the BMS is proven on solar power before the reactor lands.

## Open questions

- Where exactly should the BMS hub sit to keep source cables short while staying close to the habitat? The plan puts it near the habitat zone (see the M04 site layout).
- Can dry gas tanks sit at lunar shadow temperatures instead of being heated above 4 °C?
- What membrane thickness and pressure give the best balance for this base's duty cycle?
- How long do PEM stacks last over thousands of lunar charge cycles?
- Could cryogenic oxygen from the M06 plant replace part of the oxygen tankage?
