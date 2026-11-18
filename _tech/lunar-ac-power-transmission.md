---
slug: lunar-ac-power-transmission
title: "Lunar AC power transmission (3 kVac, 1 kHz)"
redirect_from: /technology/high-voltage-dc-lunar-cable/
alternatives:
  - {name: "High-voltage DC cable (±2.8 to ±4 kV)", compare: "Lighter: NASA found DC significantly lighter than AC above 3–4 kV, and a 2022 NASA review found ±4 kVDC mass-optimal for a 3 km, 40 kW link. But it needs high-voltage radiation-hard switches that do not exist, about four times as many parts as AC, and DC breakers that are still research. Open Moon's original design (see DD-001).", status: "Studied by NASA in 2008 and 2022; no flight hardware; NASA dropped it as its baseline in 2022.", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf"}
  - {name: "Lower-voltage DC tether (500 V to 1.5 kV)", compare: "Stays inside the voltage range that radiation-hard parts can handle today and suits light, mobile loads such as rovers. For a 40 kW, 3 km link it needs far more conductor mass than a 3 kV line.", status: "NASA's TYMPO project aimed for flight readiness in 2024; Astrobotic's LunaGrid-Lite (1 kW, ~500 m) passed critical design review in Aug 2025.", url: "https://ntrs.nasa.gov/citations/20230005730"}
  - {name: "Wireless power beaming (laser, millimetre-wave, microwave)", compare: "No cable to lay or damage, and useful for moving or very distant users. For bulk power from a heavy fission plant, its 13-27% end-to-end efficiency would add 30-60 t of extra generating capacity.", status: "Low maturity at power; the best-known demonstration sent 400 W over 330 m at 20% efficiency (US Navy PTROL, 2019).", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf"}
  - {name: "Superconducting cable", compare: "Almost lossless and the conductor weighs only a few kg per km, but it needs coolant hoses, cryocoolers and radiators. NASA estimated more than 3 t of support hardware and about 18 kW of cooling power for a 1 km line.", status: "Judged not feasible for the Moon by NASA Glenn (2022).", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf"}
  - {name: "Carbon nanotube (CNT) rope conductor", compare: "Very strong, fatigue-resistant and stable over a wide temperature range. Today its conductivity per kilogram is 6-10 times worse than copper, so it is not yet lighter.", status: "Research stage; small samples have beaten copper's specific conductivity but full cables have not.", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf"}
links:
  - {title: "Thomas, Granger, Csank & Gardner, NASA GRC: Establishing a Lunar Surface Power Grid (trade study selecting 3 kV AC)", url: "https://ntrs.nasa.gov/citations/20220011587", kind: official, date: "Aug 2022"}
  - {title: "Thomas et al., NASA GRC: A Modular AC to DC Interface Converter (UMIC) to Enable Lunar Surface Power Transmission (AIAA ASCEND)", url: "https://ntrs.nasa.gov/citations/20230013309", kind: paper, date: "Sep 2023"}
  - {title: "Mason et al., NASA/DOE: Key Design Trades for a Near-term Lunar Fission Surface Power System (NETS 2025)", url: "https://ntrs.nasa.gov/citations/20250000841", kind: paper, date: "2025"}
  - {title: "Klopp, Thomas & Csank, NASA GRC: An Experimental Study of Losses in High Voltage AC Lunar Power Cables (SciTech 2026)", url: "https://ntrs.nasa.gov/citations/20250011012", kind: paper, date: "Dec 2025"}
  - {title: "Barth & Pike, NASA GRC: Lunar Power Transmission for Fission Surface Power (NETS 2022)", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", kind: official, date: "Feb 2022"}
  - {title: "Oleson et al.: A Deployable 40 kWe Lunar Fission Surface Power Concept (NETS 2022)", url: "https://ntrs.nasa.gov/citations/20220004670", kind: official, date: "May 2022"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", kind: official, date: "Apr 2022"}
  - {title: "Kerslake, NASA GRC: Lunar Surface-to-Surface Power Transfer (STAIF 2008)", url: "https://ntrs.nasa.gov/citations/20080008842", kind: official, date: "Feb 2008"}
  - {title: "Birchenough & Hervol: Test results from a simulated high-voltage lunar power transmission line", url: "https://ntrs.nasa.gov/citations/20080010852", kind: official, date: "2008"}
  - {title: "Yang et al., NASA JPL: A High Voltage Tethered Power System for Planetary Surface Applications (TYMPO)", url: "https://ntrs.nasa.gov/citations/20230005730", kind: paper, date: "Mar 2022"}
  - {title: "NASA: 2023 NASA Tipping Point selections (Astrobotic 1 km cable demonstration)", url: "https://www.nasa.gov/general/2023-nasa-tipping-point-selections/", kind: official, date: "Jul 2023"}
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review, flight model underway", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", kind: official, date: "Aug 2025"}
  - {title: "Wikipedia: Utility frequency (why 400 Hz is used in aircraft and spacecraft)", url: "https://en.wikipedia.org/wiki/Utility_frequency", kind: wiki, date: "2026"}
  - {title: "Wikipedia: Electric power transmission (Earth grid voltages for comparison)", url: "https://en.wikipedia.org/wiki/Electric_power_transmission", kind: wiki, date: "2026"}
---

## What it is

Lunar AC power transmission is a three-phase, 3,000 V, 1,000 Hz power line laid across the Moon's surface. It carries electricity from power plants, such as a fission reactor or solar towers, to users a few kilometres away. In Open Moon every such line ends at the power management controller (PMC), and the distribution grid carries the power on to every user's service connection. Raising the voltage lowers the current, so thinner, lighter wire can carry the same power. This is NASA's lunar grid baseline, set in a [2022 NASA Glenn trade study](https://ntrs.nasa.gov/citations/20220011587). NASA/DOE's [2025 fission reactor reference design](https://ntrs.nasa.gov/citations/20250000841) uses the same link.

For comparison, the US grid on Earth runs at 60 Hz, with long-distance lines mostly at [230–500 kV](https://en.wikipedia.org/wiki/Electric_power_transmission). The lunar grid is far smaller: tens of kilowatts over 1–3 km, so 3 kV is enough. Open Moon's standard power run is 3 km of cable or less (DD-013); extended runs of up to 10 km are allowed at about 10–15% loss (DD-014). Its 1 kHz frequency is unusually high. Aircraft and spacecraft use 400 Hz because ["transformers and motors for 400 Hz are much smaller and lighter"](https://en.wikipedia.org/wiki/Utility_frequency), and NASA's lunar grid takes the same idea further.

## Why NASA chose it, and when

| When | What NASA found |
|---|---|
| Feb 2022 | A NASA Glenn review of transmission for 40 kW fission power found high-voltage metal cable best. It identified about ±4,000 VDC as mass-optimal for 3 km, but it [states it is not a NASA preference](https://ntrs.nasa.gov/citations/20220002315). |
| Aug 2022 | The NASA grid trade study compared 1.2–6 kV, DC and three-phase AC, at 60 Hz to 1 kHz. **1 kHz was the lightest AC option; 3 kV AC was the mass-optimal feasible design** ([NASA](https://ntrs.nasa.gov/citations/20220011587)). |
| Sep 2023 | NASA published the [UMIC](https://ntrs.nasa.gov/citations/20230013309), which connects 120 V DC space equipment to a 3 kV AC grid. |
| 2025 | NASA/DOE's reactor reference design adopted a 3 kVac, 1 kHz link, "selected to leverage" the UMIC ([NASA](https://ntrs.nasa.gov/citations/20250000841)). |
| Dec 2025 | NASA tested AC cables with regolith simulant in vacuum. It found no major losses, and frequency did not change the results ([NASA](https://ntrs.nasa.gov/citations/20250011012)). |

NASA's reason, in its own words: a DC grid is "practically limited to 1.2-1.5 kV, due to lack of high voltage rad-hard switches", whereas AC is "easier to increase voltage and expand, as transformers can change voltage". It concludes: "These facts drove team to select AC" ([NASA, 2022](https://ntrs.nasa.gov/citations/20220011587)).

## Why Open Moon uses it

Milestone M04 builds the base's power grid. Every source line, from the reactor and the solar towers, ends at the base PMC. The PMC routes the power over the grid, or into storage (design changes DD-003 and DD-008). The grid works like a national grid: each habitat module and facility, such as the oxygen plant, has its own service connection that turns 3 kV AC into 120 V DC for its panel (DD-009). The reactor has to sit away from the crew: NASA's design puts the user interface [1 km away](https://ntrs.nasa.gov/citations/20250000841), and the oxygen plant needs power over [3–5 km](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf). Open Moon's standard run is 3 km of cable (DD-013), and an ISRU plant at NASA's 3–5 km can be fed by an extended run of up to 10 km (DD-014).

Efficiency matters because fission power is heavy, about [0.25–0.27 kg per watt](https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf). Every watt lost in the cable means more reactor mass. Using NASA's AC baseline means a NASA-designed reactor's 3 kV AC output can run straight down its source line to the PMC, and Open Moon can use NASA's interface converters, instead of developing high-voltage DC parts no one makes yet.

![Plan view, not to scale: solar towers on ridge points and an LR-1-class reactor 1–3 km away behind terrain each send a 3 kV AC source line to the PMC near the habitat zone; the 3 kV AC distribution grid runs from the PMC to a service connection at each habitat module and facility](/assets/tech/base-power-site-layout.svg)

## How it works

![Diagram: three conversion chains, each built at the source. VSAT: native DC, array regulator and shunt, UMIC-class low-voltage inverter, 1 kHz step-up transformer, 3 kV AC. Kilopower: eight Stirling alternators at about 12 V AC and 100 Hz, one controller each rectifying to DC, a shared DC bus, a UMIC-class inverter, a 1 kHz transformer, 3 kV AC. LR-1: 3 kV AC at the reactor output, with the frequency matched to 1 kHz by the vendor or a converter. Every source then runs 3 km of cable or less to the PMC as standard, or up to 10 km as an extended run](/assets/tech/source-to-3kv-conversion.svg)

Each power source's inverters produce low-voltage AC right at the source. A transformer next to the source raises it to 3 kV for the cable, so only low-voltage switches are needed (DD-013). At the far end, another transformer lowers it, and NASA's [Universal Modular Interface Converter](https://ntrs.nasa.gov/citations/20230013309) (UMIC) turns it into 120 V DC for equipment. In Open Moon a UMIC-class converter sits in each unit's service connection (DD-009). The UMIC is built from parallel, standard 1 kW inverter modules, with DC switch modules to isolate faults. Parallel units share load by droop control.

The Brayton reactor option's three-phase alternators can feed the 3 kVac step-up transformer directly, at about [90% PMAD efficiency](https://ntrs.nasa.gov/citations/20250000841). The Stirling option needs an extra converter stage and reaches about 83%. The cable lies on the surface: NASA says ["burying the cable is not advised due to the poor thermal conductivity of the regolith"](https://ntrs.nasa.gov/citations/20250000841).

| Parameter | Value | Source |
|---|---|---|
| Voltage | 3 kV AC, three-phase | [NASA 2022](https://ntrs.nasa.gov/citations/20220011587) |
| Frequency | 1 kHz (lowest-mass AC option) | [NASA 2022](https://ntrs.nasa.gov/citations/20220011587) |
| User side | 120 V DC | [NASA UMIC](https://ntrs.nasa.gov/citations/20230013309) |
| Converter building block | 1 kW inverter module | [NASA UMIC](https://ntrs.nasa.gov/citations/20230013309) |
| Efficiency target | >85% transmission system | [NASA UMIC](https://ntrs.nasa.gov/citations/20230013309) |
| Mass target | <0.55 kg/m | [NASA UMIC](https://ntrs.nasa.gov/citations/20230013309) |
| Main cable and spool | 325 kg per 1 km | [NASA 2025](https://ntrs.nasa.gov/citations/20250000841) |
| Usable distance at 100 kW, 8 AWG, 1 kHz | 3 kV to ~600 m; 6 kV to 2.5 km; 18 kV to 20 km | [NASA 2022](https://ntrs.nasa.gov/api/citations/20220011587/downloads/APS4DS_Establishing_Lunar_Grid_V3.pdf) |
| Open Moon run length | ≤3 km standard; ≤10 km extended at ~10–15% loss (plan design) | DD-013, DD-014 |
| Worst case, 20 kW over 3 km | 3.85 A per phase; ~5.9 mm² Al for ≤3% loss, ~3.5 mm² for ≤5% (this plan's arithmetic) | [C04.4](/plan/components/c04-4-ac-grid/) |
| Same cable, 20 kW over 10 km | ~45 Ω per conductor; ~2.0 kW loss (~10%) and ~10% voltage drop; up to ~15% with plan margin (this plan's arithmetic and ESTIMATE) | [C04.4](/plan/components/c04-4-ac-grid/) |
| Voltage sensitivity | 1 kVac adds 570 kg; no gain above 3 kVac at 1 km | [NASA 2025](https://ntrs.nasa.gov/citations/20250000841) |

## Limitations and open issues

- **Heavier than ideal DC.** NASA's own study says DC is ["significantly lighter than AC for voltages above 3-4 kV"](https://ntrs.nasa.gov/citations/20220011587). AC is chosen because its parts can be built, not because it is the lightest in theory.
- **Early converter hardware.** NASA has bench-tested a single [1 kW UMIC module](https://ntrs.nasa.gov/citations/20230013309) and simulated parallel units. A full multi-kilowatt unit has not been tested in vacuum.
- **Stability without rotating machines.** Every source is an inverter, so the grid's frequency and voltage are held entirely by control software ([UMIC droop control](https://ntrs.nasa.gov/citations/20230013309)).
- **Longer grids.** NASA notes that grids much larger than Artemis scale may need a [lower frequency](https://ntrs.nasa.gov/citations/20220011587) to avoid stability and propagation problems. That is why Open Moon keeps 3 km as its standard run, allows extended runs only up to 10 km, each after its own 1 kHz charging and stability analysis, and rejects anything longer (DD-013, DD-014). NASA has not published 1 kHz charging and stability data for a 10 km run of this cable.
- **Insulation in vacuum.** Vacuum-rated high-voltage cables that avoid partial discharge are [still being studied](https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf).
- **Surface exposure.** Because the cable is not buried, it faces rover traffic and micrometeoroids. NASA's first cable-laying demonstration was scoped at [1 km](https://www.nasa.gov/general/2023-nasa-tipping-point-selections/), and Astrobotic's 2025 design lays [500 m](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/).
