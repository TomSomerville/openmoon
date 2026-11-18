---
id_code: "C04.4"
milestone: M04
order: 4
redirect_from: /plan/components/c04-4-hvdc-grid/
title: 3 kV AC grid and cable-laying rover
summary: "A 3 kV, 3-phase, 1 kHz AC grid, NASA's lunar baseline, that carries power from every source to the BMS hub, and from the BMS out to the habitat, oxygen plant and other loads. Transformers and modular converters connect 120 V DC equipment. A small rover lays and covers the cable."
trl: 4
spec:
  - {k: "Trunk", v: "3 kV AC, 3-phase, 1 kHz (NASA baseline; design change DD-001)"}
  - {k: "User voltage", v: "120 V DC microgrids (NASA space power standard)"}
  - {k: "Interface converter", v: "UMIC: parallel 1 kW inverter modules plus line-frequency transformers"}
  - {k: "Link length", v: "1–3 km per link; ≥3 km laid in M04"}
  - {k: "Efficiency target", v: ">85% transmission system (UMIC target)"}
  - {k: "Mass target", v: "<0.55 kg/m transmission system (UMIC target)"}
  - {k: "Cable mass", v: "325 kg per 1 km main cable and spool (NASA 2025 reference)"}
  - {k: "Microgrids", v: "2 (habitat, ISRU) plus source nodes"}
  - {k: "Rover", v: "1 cable layer, ~1 km reel (~0.33 t) per trip"}
  - {k: "Fault location", v: "Time-domain reflectometry from each node"}
subcomponents:
  - name: Transmission cable
    desc: "Three-phase cable carrying power 1–3 km at 3 kV so conductors stay thin."
    parts: ["Three aluminium conductors", "FEP insulation rated with margin for 3 kV in vacuum", "Outer abrasion-resistant jacket", "Vacuum-rated HV connectors and splices", "Cable markers"]
    tech: "NASA GRC AC cable tests in vacuum with regolith simulant (2025)"
    trl: 4
  - name: Transformers
    desc: "Step 120 V-class inverter output up to 3 kV at each source, and back down at each user. This is the reason NASA chose AC."
    parts: ["1 kHz line-frequency transformers", "High-voltage AC relay module", "Thermal path to radiator", "Insulation for vacuum operation"]
    tech: "NASA UMIC design; NASA FSP 2025 reference (3 kVac step-up)"
    trl: 4
  - name: Universal Modular Interface Converters (UMIC)
    desc: "Connect 120 V DC equipment and microgrids to the AC grid, in both directions."
    parts: ["Standard 1 kW single-phase inverter modules in parallel", "DC switch modules for fault isolation and current limiting", "AC output filters and 3-phase relays", "Ethernet controller", "Housekeeping power module"]
    tech: "NASA GRC UMIC (STMD), 1 kW module bench-tested 2023"
    trl: 4
  - name: Switchgear and protection
    desc: "Isolates faults quickly so one bad cable or load cannot drop the whole grid."
    parts: ["High-voltage AC relays and breakers", "DC switch modules on the 120 V side", "Current limiting in inverters", "Insulation monitoring and grounding", "Surge protection"]
    tech: "UMIC relay and DC switch modules; terrestrial AC protection practice"
    trl: 4
  - name: Microgrids and control
    desc: "Runs habitat and ISRU as separate local grids that share power over the trunk. With no spinning machines, inverters must hold frequency and voltage themselves."
    parts: ["120 V DC buses and power distribution units", "Droop control in every UMIC (shares load between parallel units)", "Regional grid controller", "Priority load-shedding tables", "Earth link for remote operation"]
    tech: "NASA UMIC droop control (simulated and bench tested, 2023)"
    trl: 4
  - name: Cable-laying rover
    desc: "Carries a cable reel from the lander, unreels it along a surveyed route on the surface."
    parts: ["Rover chassis and drive", "Powered reel with tension control", "Cable guide and payout counter", "Crossing-protector placer (ramps over cable at rover crossings)", "Route cameras and lidar"]
    tech: "Astrobotic LunaGrid-Lite (AC cable demo); NASA FSP utility-rover concept"
    trl: 5
  - name: Fault location and monitoring
    desc: "Finds and locates cable faults without sending a rover to walk the whole line."
    parts: ["Time-domain reflectometer at each node", "Insulation resistance monitor", "Partial-discharge sensors", "Current and voltage sensors", "Fault log to the grid controller"]
    tech: "Terrestrial TDR practice, to be adapted for lunar use"
    trl: 4
risks:
  - {sev: High, title: "UMIC is early: NASA has bench-tested a single 1 kW module and simulated parallel units; a full multi-kilowatt UMIC has not been tested in vacuum.", fix: "Build on NASA's UMIC programme; test parallel modules, transformers and droop control in thermal-vacuum before flight."}
  - {sev: High, title: "An AC grid with no rotating machines must be held stable entirely by inverters.", fix: "Droop control in every UMIC (NASA's approach); hardware-in-the-loop tests with sudden load steps and faults; keep links short."}
  - {sev: High, title: "High voltage in vacuum risks partial discharge and arcing, made worse by abrasive dust on insulation.", fix: "Insulation margin, sealed connectors, and partial-discharge testing in vacuum with dust before flight."}
  - {sev: High, title: "Cables on the surface can be damaged by rovers, thermal cycling and micrometeoroids, but NASA advises against burying them because regolith conducts heat poorly and the cable needs its view to space to shed heat.", fix: "Lay cables on the surface along surveyed routes away from traffic; protect only rover crossings with ramps; separate the main feeds to limit common failures; build a ring so every node has two paths."}
  - {sev: Medium, title: "AC cable is heavier than DC would be at higher voltage (NASA says DC is significantly lighter above 3–4 kV).", fix: "Accepted trade-off (DD-001): AC uses parts that exist; revisit if radiation-hard high-voltage switches become available."}
  - {sev: Medium, title: "Much longer grids may need a lower frequency to avoid stability and propagation problems (NASA).", fix: "Keep 1 kHz for the base's 1–3 km links; study frequency again before any long-distance expansion."}
  - {sev: Medium, title: "Laying long cables on rough terrain can snag or overstress the cable; LunaGrid-Lite's demo length dropped from 1 km to 500 m.", fix: "Survey routes from orbit and by rover first; use 1 km reels with field splices; monitor tension and payout."}
sources:
  - {title: "Thomas, Granger, Csank & Gardner, NASA GRC: Establishing a Lunar Surface Power Grid (trade study selecting 3 kV AC)", url: "https://ntrs.nasa.gov/citations/20220011587", date: "Aug 2022"}
  - {title: "Thomas et al., NASA GRC: A Modular AC to DC Interface Converter (UMIC) to Enable Lunar Surface Power Transmission (AIAA ASCEND)", url: "https://ntrs.nasa.gov/citations/20230013309", date: "Sep 2023"}
  - {title: "Mason et al., NASA/DOE: Key Design Trades for a Near-term Lunar Fission Surface Power System (NETS 2025)", url: "https://ntrs.nasa.gov/citations/20250000841", date: "2025"}
  - {title: "Klopp, Thomas & Csank, NASA GRC: An Experimental Study of Losses in High Voltage AC Lunar Power Cables (SciTech 2026)", url: "https://ntrs.nasa.gov/citations/20250011012", date: "Dec 2025"}
  - {title: "Barth & Pike, NASA GRC: Lunar Power Transmission for Fission Surface Power (NETS-2022)", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", date: "Feb 2022"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", date: "2025"}
  - {title: "SatNews: Astrobotic's LunaGrid VSAT enters thermal vacuum testing (press)", url: "https://satnews.com/2024/07/20/astrobotics-lunagrids-vertical-solar-array-technology-vsat-enters-tvac/", date: "Jul 2024"}
  - {title: "Wikipedia: Time-domain reflectometer", url: "https://en.wikipedia.org/wiki/Time-domain_reflectometer", date: "2026"}
  - {title: "Wikipedia: Aluminium", url: "https://en.wikipedia.org/wiki/Aluminium", date: "2026"}
---

{% include decision-note.html id="DD-001" extra="This component was first designed as a ±4 kV DC grid, following NASA Glenn's February 2022 transmission review. It was redesigned on 18 November 2026 to NASA's 3 kV AC, 1 kHz baseline." %}

## What it does

The grid moves power from where it is made to where it is used. NASA's reactor reference design places the user interface 1 km from the reactor<sup class="r">[3](#s3)</sup>, and the oxygen plant needs power over 3–5 km<sup class="r">[6](#s6)</sup>. NASA's baseline is two independent microgrids, one for the habitat and one for ISRU, each with its own sources, joined by a primary line so they can share power<sup class="r">[6](#s6)</sup>.

**Every source goes through the BMS (design change DD-003).** Source lines from the reactor and the solar towers run to the BMS hub (C04.3), not straight to users. The BMS then sends power out over the grid to meet demand, or into storage. So the grid has two kinds of line: source lines into the BMS, and feeders from the BMS to the microgrids and loads. NASA's two-microgrid layout still applies on the output side.

{% include decision-note.html id="DD-003" extra="Sources no longer feed users directly over the trunk; every line from a source ends at the BMS hub." %}

## Why 3 kV AC at 1 kHz: NASA's reasoning

| When | What NASA found | Source |
|---|---|---|
| Feb 2022 | Reviewed lunar transmission for 40 kW fission power. High-voltage metal cable is the best option; laid out AC and DC hardware challenges. Explicitly not a NASA preference. | Barth & Pike<sup class="r">[5](#s5)</sup> |
| Aug 2022 | Trade study across 1.2–6 kV, DC and 3-phase AC, 60 Hz to 1 kHz. **1 kHz gave the lowest mass; 3 kV AC was the mass-optimal feasible design.** | Thomas et al.<sup class="r">[1](#s1)</sup> |
| Sep 2023 | Published the UMIC, which connects 120 V DC equipment to a 3 kV AC grid at 1 kHz. | Thomas et al.<sup class="r">[2](#s2)</sup> |
| 2025 | Government reactor reference design uses a 3 kVac, 1 kHz link to a user 1 km away, selected to leverage UMIC. | Mason et al.<sup class="r">[3](#s3)</sup> |
| Dec 2025 | Tested AC cables in vacuum with regolith simulant: no major losses; frequency did not change results. | Klopp et al.<sup class="r">[4](#s4)</sup> |

NASA's own words on the choice:

> "DC grid practically limited to 1.2-1.5 kV, due to lack of high voltage rad-hard switches … AC easier to increase voltage and expand, as transformers can change voltage in AC-DC designs … These facts drove team to select AC."<sup class="r">[1](#s1)</sup>

The same study says DC would be "significantly lighter than AC for voltages above 3-4 kV"<sup class="r">[1](#s1)</sup>. So AC is not the lightest grid in theory. It is the lightest one that can be built with radiation-hard parts that exist.

## How it works

- **Transformers do the voltage change.** Each source's inverters make low-voltage AC, and a transformer raises it to 3 kV. At each user a transformer lowers it again<sup class="r">[2](#s2)</sup>. Transformers need no high-voltage semiconductor switches, which is the problem that rules out high-voltage DC<sup class="r">[1](#s1)</sup>.
- **UMIC.** Built from parallel, standard 1 kW single-phase inverter modules converting between 120 V DC and under 100 V AC, then one or more transformers to 3 kV. DC switch modules isolate DC faults, a high-voltage relay can disconnect the transformer, and an Ethernet controller coordinates the modules<sup class="r">[2](#s2)</sup>. NASA's targets are over 85% transmission system efficiency and under 0.55 kg per metre<sup class="r">[2](#s2)</sup>.
- **Control.** Parallel UMICs share load using droop control, adjusting frequency and voltage slightly with load, so no central controller is needed to balance them<sup class="r">[2](#s2)</sup>. A regional controller sends power to the highest-priority loads first, such as the crewed habitat<sup class="r">[6](#s6)</sup>.
- **Reactor interface.** NASA's 2025 design couples the Brayton option's 3-phase alternators straight to the 3 kVac step-up transformer, at about 90% PMAD efficiency. The Stirling option needs an extra converter stage and reaches about 83%<sup class="r">[3](#s3)</sup>. In Open Moon the far end of that line is the BMS hub (C04.3), not a grid user (DD-003).
- **Cable laying.** Astrobotic's LunaGrid-Lite pairs a 4U CubeRover with a robotic cable deployer. It is planned to carry 1 kW over 500 m<sup class="r">[7](#s7)</sup>. Earlier plans used 1 km at 1 kV and 1 kHz AC<sup class="r">[8](#s8)</sup>, the same frequency as NASA's grid.
- **Lay it on the surface.** NASA's 2025 design keeps the cable on the surface, where it has a 180° view to space for shedding heat. It says "burying the cable is not advised due to the poor thermal conductivity of the regolith"<sup class="r">[3](#s3)</sup>.
- **Fault location.** A time-domain reflectometer sends a pulse down the line and times the echo from any impedance change<sup class="r">[9](#s9)</sup>.

## Sizing

One 40 kW, 3-phase link, the largest planned (this plan's arithmetic, unity power factor). The 20 kWe reactor link carries half this current:

| Quantity | Working | Result |
|---|---|---|
| Current per phase at 3 kV | 40 kW ÷ (√3 × 3 kV) | ~7.7 A |
| Allowed loss (95% cable efficiency) | 5% × 40 kW | 2 kW |
| Resistance per conductor, 3 km | 2,000 W ÷ (3 × 7.7²) | ~11 Ω (3.7 Ω/km) |
| Aluminium area | 26.5 nΩ·m<sup class="r">[10](#s10)</sup> ÷ 0.0037 Ω/m | ~7 mm² |
| Aluminium mass, 3 conductors × 3 km | 7 mm² × 9 km × 2,699 kg/m³<sup class="r">[10](#s10)</sup> | ~170 kg |
| NASA reference, cable + spool | 1 km main cable<sup class="r">[3](#s3)</sup> | 325 kg per km |

Insulation, jacket and spool, not metal, make up most of the cable mass. NASA's 325 kg per km is the planning figure: about 1 t for 3 km.

- **Voltage check.** NASA found no mass benefit above 3 kVac for a 1 km link, because higher voltage pushed wire sizes below the smallest practical gauge. Dropping to 1 kVac added 570 kg<sup class="r">[3](#s3)</sup>.

## Testing and qualification

1. **Cable samples.** Partial-discharge and breakdown tests in vacuum at −173 to +130 °C (the lunar range<sup class="r">[6](#s6)</sup>), with dust; then flex and abrasion. NASA's 2025 tests already showed no major losses from simulant, coiled or buried<sup class="r">[4](#s4)</sup>.
2. **UMIC.** Scale from NASA's single 1 kW module<sup class="r">[2](#s2)</sup> to a multi-kilowatt unit with transformers. Run thermal-vacuum and radiation tests.
3. **Hardware-in-the-loop microgrid.** Run several UMICs in parallel on simulated sources and loads. Inject load steps and faults and check stability and that only the faulted section trips.
4. **Rover field trials.** Lay and recover 1 km of cable on simulant slopes. Measure tension, payout accuracy and how the cable lies on rough ground.
5. **On the Moon.** Use LunaGrid-Lite's flight results<sup class="r">[7](#s7)</sup> to set the first route. Energise each link at low voltage first, then 3 kV. Record its TDR signature as a baseline.

## Open questions

- How should surface cables be protected from rover traffic and micrometeoroids, given that NASA advises against burial<sup class="r">[3](#s3)</sup>?
- How do many inverter-only sources share control, with the BMS hub setting how much each one supplies?
- If radiation-hard high-voltage switches mature, would a DC upgrade be worth revisiting? (See DD-001.)
- Can aluminium cable later be made on the Moon (M12)?
