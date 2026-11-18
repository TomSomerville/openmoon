---
id_code: "C04.4"
milestone: M04
order: 4
redirect_from: /plan/components/c04-4-hvdc-grid/
title: 3 kV AC grid and cable-laying rover
summary: "A 3 kV, 3-phase, 1 kHz AC grid, NASA's lunar baseline, that carries power from every source to the power management controller (PMC), and from the PMC out to every unit like a national grid. Each habitat module and facility has its own service connection that delivers 120 V DC to its panel. Every source converts to 3 kV AC on the spot and sits within 3 km of cable run of the PMC as standard, or up to 10 km on an extended run (DD-013, DD-014). A small rover lays the cable on the surface."
trl: 4
spec:
  - {k: "Trunk", v: "3 kV AC, 3-phase, 1 kHz (NASA baseline; design change DD-001)"}
  - {k: "User voltage", v: "120 V DC at each unit's DC panel (NASA space power standard); AC only from a unit's own inverter (DD-009)"}
  - {k: "Interface converter", v: "UMIC: parallel 1 kW inverter modules plus line-frequency transformers"}
  - {k: "Link length", v: "Standard ≤3 km per run (DD-013); extended up to 10 km at ~10–15% loss, with receiving-end voltage regulation and a 1 kHz stability analysis per run; beyond 10 km rejected (DD-014)"}
  - {k: "Source-end conversion", v: "At every source: low-voltage UMIC-class inverter + 1 kHz step-up transformer to 3 kV AC; LR-1 at 3 kV, 3-phase, 1 kHz at its output (DD-013)"}
  - {k: "Efficiency target", v: ">85% transmission system (UMIC target)"}
  - {k: "Mass target", v: "<0.55 kg/m transmission system (UMIC target)"}
  - {k: "Cable mass", v: "325 kg per 1 km main cable and spool (NASA 2025 reference); ~1 t per 3 km run, ~3.3 t per 10 km extended run (this plan's arithmetic)"}
  - {k: "Service connections", v: "One per unit: 3 habitat modules plus each facility (DD-009); no separate microgrids"}
  - {k: "Rover", v: "1 cable layer, ~1 km reel (~0.33 t) per trip"}
  - {k: "Fault location", v: "Time-domain reflectometry from each node"}
subcomponents:
  - name: Transmission cable
    desc: "Three-phase cable carrying power up to 3 km per standard run (DD-013), or up to 10 km per extended run (DD-014), at 3 kV so conductors stay thin."
    parts: ["Three aluminium conductors", "FEP insulation rated with margin for 3 kV in vacuum", "Outer abrasion-resistant jacket", "Vacuum-rated HV connectors and splices", "Cable markers"]
    tech: "NASA GRC AC cable tests in vacuum with regolith simulant (2025)"
    trl: 4
  - name: Transformers
    desc: "Step low-voltage inverter output up to 3 kV right next to each source, and back down at each user. A transformer has no switches, so only low-voltage switches are needed. This is the reason NASA chose AC (DD-013)."
    parts: ["1 kHz step-up transformer at every source (VSAT tower, KRUSTY-class unit; LR-1 per its vendor)", "1 kHz line-frequency transformers at each service connection", "High-voltage AC relay module", "Thermal path to radiator", "Insulation for vacuum operation"]
    tech: "NASA UMIC design; NASA FSP 2025 reference (3 kVac step-up)"
    trl: 4
  - name: Universal Modular Interface Converters (UMIC)
    desc: "Connect 120 V DC equipment to the AC grid, in both directions. A UMIC-class converter is the heart of every unit's service connection (DD-009), and a UMIC-class inverter sits at every DC source (DD-013)."
    parts: ["Standard 1 kW single-phase inverter modules in parallel", "DC switch modules for fault isolation and current limiting", "AC output filters and 3-phase relays", "Ethernet controller", "Housekeeping power module"]
    tech: "NASA GRC UMIC (STMD), 1 kW module bench-tested 2023"
    trl: 4
  - name: Switchgear and protection
    desc: "Isolates faults quickly so one bad cable or load cannot drop the whole grid."
    parts: ["High-voltage AC relays and breakers", "DC switch modules on the 120 V side", "Current limiting in inverters", "Insulation monitoring and grounding", "Surge protection"]
    tech: "UMIC relay and DC switch modules; terrestrial AC protection practice"
    trl: 4
  - name: Service connections
    desc: "Each habitat module and facility connects to the grid like a house: its own service drop, step-down and rectifier to 120 V DC, meter and main breaker, feeding its own DC panel. Each can be isolated without affecting the others (DD-009)."
    parts: ["Service drop (tap and short cable from the 3 kV AC grid)", "UMIC-class step-down and rectifier, 3 kV AC to 120 V DC", "Energy meter reporting to the PMC", "Main breaker or disconnect", "120 V DC panel and subpanels with a breaker per branch circuit", "Optional unit inverter and local AC subpanel, chosen by each unit"]
    tech: "NASA GRC UMIC (2023); Space Station Freedom 120 V DC secondary distribution; terrestrial service-entrance practice"
    trl: 4
  - name: Grid control
    desc: "With no spinning machines, inverters must hold frequency and voltage themselves. The PMC sets what each source supplies and which service connections stay closed."
    parts: ["Droop control in every UMIC (shares load between parallel units)", "Grid controller (the PMC energy management function, C04.3)", "Priority load-shedding tables, by service connection", "Earth link for remote operation"]
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
  - {sev: Medium, title: "Much longer grids may need a lower frequency to avoid stability and propagation problems (NASA). Extended runs of up to 10 km (DD-014) go beyond NASA's 1–3 km Artemis scale, and NASA has not published 1 kHz charging and stability data for this cable.", fix: "Keep 1 kHz; 3 km stays the standard run (DD-013); approve each extended run up to 10 km only after its own 1 kHz cable-charging and stability analysis, with receiving-end voltage regulation or transformer taps; runs beyond 10 km are rejected (DD-014); study voltage and frequency again before any longer expansion."}
  - {sev: High, title: "The 3 km standard run (DD-013) cannot reach the best-lit pair of ridge points (~8 km apart) or ISRU sites that NASA expects at 3–5 km. Extended runs up to 10 km (DD-014) can, at ~10–15% loss.", fix: "Site selection (M00) puts at least one point of the pair within 10 km and keeps each run 10 km or less; ISRU plants at 3–5 km on extended runs; size generation for the extra loss; PSR work beyond 10 km on the mobile power cart (PW.5) or a local source."}
  - {sev: Medium, title: "LR-1's alternator frequency is not set by NASA; its 2025 reference Brayton alternators ran at 2 kHz.", fix: "Specify 3 kV, 3-phase, 1 kHz at the reactor output, or add a frequency converter at the reactor end (open, DD-013)."}
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
  - {title: "Button, NASA TM-104510: Development and testing of a source subsystem for the PMAD DC test bed (160 V primary, 120 V secondary)", url: "https://ntrs.nasa.gov/api/citations/19910016888/downloads/19910016888.pdf", date: "Aug 1991"}
  - {title: "Wikipedia: Service drop", url: "https://en.wikipedia.org/wiki/Service_drop", date: "2026"}
  - {title: "Wikipedia: Distribution board", url: "https://en.wikipedia.org/wiki/Distribution_board", date: "2026"}
  - {title: "INL/NASA: Fission Surface Power Technical Maturation Webinar (reference PMAD: Brayton 240 Vrms, 2 kHz; Stirling 350 V DC to 3 kVac)", url: "https://inl.gov/content/uploads/2024/11/FSP-Technical-Maturation-Webinar-Final-250924-1.pdf", date: "Sep 2025"}
  - {title: "Austin et al., IEEE TNS: Inclusion of radiation environment variability for reliability estimates for SiC power MOSFETs (single-event burnout)", url: "https://ntrs.nasa.gov/api/citations/20205000795/downloads/2020-561-Austin-Final-Paper-TNS.pdf", date: "Jan 2020"}
  - {title: "NASA Glenn: SPARC Industry Day presentation (Lunar Reactor-1 requirements)", url: "https://sam.gov/api/prod/opps/v3/opportunities/resources/files/6b927f8dc6c843749a45b2c0589bf0e7/download", date: "Sep 2026"}
---

## What it does

The grid moves power from where it is made to where it is used. NASA's reactor reference design places the user interface 1 km from the reactor<sup class="r">[3](#s3)</sup>, and NASA says the oxygen plant needs power over 3–5 km<sup class="r">[6](#s6)</sup>. Open Moon's standard power run is 3 km (DD-013), and ISRU plants at NASA's 3–5 km are fed by extended runs of up to 10 km (DD-014). NASA's baseline is two independent microgrids, one for the habitat and one for ISRU, each with its own sources, joined by a primary line so they can share power<sup class="r">[6](#s6)</sup>.

**Every source goes through the PMC (design changes DD-003 and DD-008).** Source lines from the reactor and the solar towers run to the power management controller (PMC, C04.3), not straight to users. The PMC then sends power out over the grid to meet demand, or into storage. So the grid has two parts: source lines into the PMC, and the distribution grid from the PMC to every unit.

**A national grid, and every unit a house (design change DD-009).** Open Moon does not build NASA's two separate microgrids. The distribution grid is one 3 kV AC network, like a national grid. Each habitat module and each facility has its own service connection to it, like a house<sup class="r">[12](#s12)</sup>.

**3 km standard, 10 km extended, converted at the source (design changes DD-013 and DD-014).** Every generation source sits within 3 km of cable run of the PMC as standard (DD-013), or up to 10 km on an extended run at about 10–15% loss (DD-014), and converts to 3 kV, 3-phase, 1 kHz AC right where it stands. See [Source-end conversion](#source-end-conversion-dd-010) below.

## Service connections

![Diagram: the 3 kV AC grid feeds three habitat modules and a water electrolysis plant, each through its own service connection: service drop, UMIC-class step-down and rectifier to 120 V DC, meter, main breaker, then a 120 V DC panel with branch circuits such as life support, lighting, galley, avionics and heaters; habitats have an optional unit inverter feeding a local AC subpanel; any one connection can be opened without affecting the others](/assets/tech/base-power-service-connection.svg)

Each service connection has the same parts (plan design):
1. **Service drop.** A tap on the 3 kV AC grid and a short cable to the unit.
2. **Step-down and rectify.** A UMIC-class converter turns 3 kV AC into 120 V DC. NASA built the UMIC to connect 120 V DC space equipment to a 3 kV AC grid, with DC switch modules to isolate faults and a relay to disconnect the transformer<sup class="r">[2](#s2)</sup>.
3. **Meter.** Measures what the unit draws and reports it to the PMC.
4. **Main breaker.** Disconnects the whole unit.
5. **DC panel.** A 120 V DC panel, and subpanels where needed, split the feed into branch circuits, each with its own breaker, like a distribution board<sup class="r">[13](#s13)</sup>. Space Station Freedom also converted its primary bus to 120 V DC for its users<sup class="r">[11](#s11)</sup>.
6. **AC only if the unit needs it.** The grid does not supply AC to units. A unit that needs AC has its own inverter, fed from its DC panel, feeding a local AC subpanel for that unit only. Each unit chooses its own inverter and AC voltage.

**Who has one.** Each of the 3 habitat modules (DD-007). Each facility: the regolith water-extraction plant, water electrolysis (H₂/O₂), the oxygen plant, life-support processing outside the habitats, comms nodes, rover chargers, greenhouses and the propellant depot.

**Protection benefit.** Any service connection can be opened without affecting the others. A fault inside one unit trips its own main breaker, not the grid. When the PMC must shed load, it opens whole service connections, lowest priority first (plan design).

## Layout

![Plan view, not to scale: 10 kW VSAT towers on two or three ridge points and an LR-1-class reactor 1–3 km away behind terrain each send a 3 kV AC source line to the PMC near the habitat zone; the 3 kV AC distribution grid runs from the PMC to a service connection at each habitat module and facility; landing pads sit at least 1 km from the towers](/assets/tech/base-power-site-layout.svg)

![One-line diagram: source lines at 3 kV AC into PMC main switching units A and B with a cross-tie; battery strings on each unit through BCDUs; fuel cells discharge only into the battery; the 3 kV AC distribution grid feeds a service connection with a 120 V DC panel at each habitat module and facility](/assets/tech/base-power-one-line.svg)

- **Source lines** run from each solar tower and from the reactor to the PMC, one line per source (plan design, DD-003).
- **Distribution grid** runs from the PMC to every unit. At each unit's service connection a UMIC-class converter turns 3 kV AC into 120 V DC<sup class="r">[2](#s2)</sup> (plan design, DD-009).
- **Distances.** Standard source runs are 3 km of cable or less (plan design, DD-013); extended runs reach up to 10 km (plan design, DD-014). The reactor sits 1–3 km from the habitat zone (plan design, DD-002); NASA's reference design uses a 1 km link<sup class="r">[3](#s3)</sup>. NASA's estimate for ISRU is power over 3–5 km<sup class="r">[6](#s6)</sup>, so ISRU plants at that distance are fed by extended runs (DD-014), and work beyond 10 km uses the mobile power cart (PBS PW.5) or a local source (open).
- **On the surface.** All lines lie on the surface, as NASA advises<sup class="r">[3](#s3)</sup>. They keep away from rover routes, with ramps at crossings (plan design).

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
- **Control.** Parallel UMICs share load using droop control, adjusting frequency and voltage slightly with load, so no central controller is needed to balance them<sup class="r">[2](#s2)</sup>. A regional controller sends power to the highest-priority loads first, such as the crewed habitat<sup class="r">[6](#s6)</sup>. In Open Moon that controller is the PMC, and it sheds load by opening service connections (DD-009).
- **Reactor interface.** NASA's 2025 design couples the Brayton option's 3-phase alternators straight to the 3 kVac step-up transformer, at about 90% PMAD efficiency. The Stirling option needs an extra converter stage and reaches about 83%<sup class="r">[3](#s3)</sup>. In Open Moon the far end of that line is the PMC (C04.3), not a grid user (DD-003).
- **Cable laying.** Astrobotic's LunaGrid-Lite pairs a 4U CubeRover with a robotic cable deployer. It is planned to carry 1 kW over 500 m<sup class="r">[7](#s7)</sup>. Earlier plans used 1 km at 1 kV and 1 kHz AC<sup class="r">[8](#s8)</sup>, the same frequency as NASA's grid.
- **Lay it on the surface.** NASA's 2025 design keeps the cable on the surface, where it has a 180° view to space for shedding heat. It says "burying the cable is not advised due to the poor thermal conductivity of the regolith"<sup class="r">[3](#s3)</sup>.
- **Fault location.** A time-domain reflectometer sends a pulse down the line and times the echo from any impedance change<sup class="r">[9](#s9)</sup>.

## Source-end conversion (DD-013)

![Diagram: three conversion chains, each built at the source. VSAT: native DC, array regulator and shunt, UMIC-class low-voltage inverter, 1 kHz step-up transformer, 3 kV AC. Kilopower: eight Stirling alternators at about 12 V AC and 100 Hz, one controller each rectifying to DC, a shared DC bus, a UMIC-class inverter, a 1 kHz transformer, 3 kV AC. LR-1: 3 kV AC at the reactor output, with the frequency matched to 1 kHz by the vendor or a converter. Every source then runs 3 km of cable or less to the PMC as standard, or up to 10 km as an extended run](/assets/tech/source-to-3kv-conversion.svg)

Each source makes its own 3 kV, 3-phase, 1 kHz AC (plan design, DD-013):
- **Low-voltage inverter, then transformer.** A UMIC-class inverter of parallel 1 kW modules turns the source's DC into under 100 V AC, and a 1 kHz transformer next to the source steps it up to 3 kV<sup class="r">[2](#s2)</sup>. Only low-voltage switches are used; the transformer has none. There are no high-voltage DC lines.
- **Why low-voltage switches.** NASA limits a DC grid to 1.2–1.5 kV "due to lack of high voltage rad-hard switches"<sup class="r">[1](#s1)</sup>. For 1200 V silicon carbide MOSFETs, derating the voltage by 50% "does not eliminate the risk" of heavy-ion single-event burnout<sup class="r">[15](#s15)</sup>. NASA's reference design notes that AC "allows use of existing flight-rated switches without stacking"<sup class="r">[14](#s14)</sup>.
- **VSAT.** Array DC (voltage not published; the ISS arrays hold ~160 V DC<sup class="r">[11](#s11)</sup>) → array regulator and shunt → inverter → transformer.
- **KRUSTY-class.** Eight Stirling alternators, each about 12 V AC at ~100 Hz → one controller per engine rectifies to DC → one DC bus (voltage not published) → inverter → transformer. NASA's 2025 Stirling reference does the same at 40 kWe: controllers to 350 V DC, then DC-to-AC and a transformer to 3 kVac<sup class="r">[14](#s14)</sup>. See the [Kilopower / KRUSTY card](/technology/kilopower-krusty-fission-test/).
- **LR-1.** 3 kV RMS AC is required, but no frequency is set<sup class="r">[16](#s16)</sup>. NASA's 2025 Brayton reference alternators gave 240 Vrms, 2 kHz, 3-phase<sup class="r">[14](#s14)</sup>. The plan requires **3 kV, 3-phase, 1 kHz at the reactor output**, by vendor specification or a frequency converter at the reactor end (**open**).

**Why 3 km.** For 100 kW on 8 AWG cable at 1 kHz, NASA's grid study gives 3 kV as usable to about 600 m and 6 kV to 2.5 km, rising to 18 kV for 20 km, and warns that "long distances beyond Artemis may require dropping to lower frequency (TBD)"<sup class="r">[1](#s1)</sup>. NASA's Artemis working scale is 1–3 km links at "elevated voltage (2 kV+)"<sup class="r">[6](#s6)</sup>. The base's links carry 20 kW or less, so a 3 km standard run keeps them inside NASA's 3 kV, 1 kHz design scale (plan design). An extended run of up to 10 km goes beyond it, so each one needs its own 1 kHz charging and stability analysis before approval (plan design, DD-014).

## Sizing

The worst case under DD-013 is the 20 kWe reactor link over the full 3 km (this plan's arithmetic, unity power factor; aluminium at 26.5 nΩ·m and 2,699 kg/m³<sup class="r">[10](#s10)</sup>):

| Quantity | Working | ≤3% loss | ≤5% loss |
|---|---|---|---|
| Current per phase at 3 kV | 20 kW ÷ (√3 × 3 kV) | 3.85 A | 3.85 A |
| Allowed loss | 3% or 5% × 20 kW | 600 W | 1,000 W |
| Resistance per conductor, 3 km | loss ÷ (3 × 3.85²) | 13.5 Ω (4.5 Ω/km) | 22.5 Ω (7.5 Ω/km) |
| Aluminium area | 26.5 nΩ·m ÷ (Ω per m) | ~5.9 mm² | ~3.5 mm² |
| Aluminium mass, 3 conductors × 3 km | area × 9 km × 2,699 kg/m³ | ~143 kg | ~86 kg |
| NASA reference, cable + spool | 1 km main cable<sup class="r">[3](#s3)</sup> | 325 kg per km | 325 kg per km |

- **At 8 AWG** (8.37 mm², the size NASA's grid study used<sup class="r">[1](#s1)</sup>), the loss is about 2.1% (422 W) and the aluminium weighs about 203 kg (this plan's arithmetic).
- **A 10 kW tower link** carries half the current, about 1.9 A, and a quarter of the loss on the same cable (this plan's arithmetic).
- Insulation, jacket and spool, not metal, make up most of the cable mass. NASA's 325 kg per km is the planning figure: about 1 t per 3 km run, and about 3.3 t per 10 km extended run (this plan's arithmetic).

**Extended run: the same cable over 10 km (this plan's arithmetic, DD-014).** Same 20 kW, 3 kV, 3-phase, unity power factor, 3.85 A per phase, and the ~5.9 mm² conductor sized for 3% at 3 km:

| Run on the same cable | Resistance per conductor | Resistive loss | Voltage drop |
|---|---|---|---|
| 3 km | ~13.5 Ω | ~0.6 kW (~3%) | ~3% |
| 10 km | ~45 Ω | ~2.0 kW (~10%) | ~10% |

| Run on NASA's 8 AWG (8.37 mm²) | Resistance per conductor | Resistive loss |
|---|---|---|
| 3 km | ~9.5 Ω | ~0.42 kW (~2.1%) |
| 10 km | ~32 Ω | ~1.4 kW (~7%) |

- **Why the band goes up to ~15% (ESTIMATE, plan margin).** Two effects are not in the tables. First, the current rises a little as the voltage sags: if the load holds 20 kW at the receiving end, the current rises to about 4.3 A and the loss to about 2.5 kW, about 11% of the power sent (this plan's arithmetic). Second, the 1 kHz reactive effects, cable charging current and inductance, are not quantified, because NASA has not published them for this cable. NASA warns that "long distances beyond Artemis may require dropping to lower frequency (TBD) to avoid stability, propagation issues"<sup class="r">[1](#s1)</sup>.
- **Conditions (plan design).** Voltage regulation or transformer taps at the receiving end, for the ~10% sag. An analysis of 1 kHz cable charging and stability for that run before it is approved. Optionally, a thicker cable.
- **Thicker cable.** At constant loss, cable mass rises with the square of distance. Holding 3% at 10 km needs about 20 mm² per conductor, about 1.6 t of aluminium for 3 conductors × 10 km, against ~143 kg at 3 km (this plan's arithmetic).

- **Voltage check.** NASA found no mass benefit above 3 kVac for a 1 km link, because higher voltage pushed wire sizes below the smallest practical gauge. Dropping to 1 kVac added 570 kg<sup class="r">[3](#s3)</sup>.

## Testing and qualification

1. **Cable samples.** Partial-discharge and breakdown tests in vacuum at −173 to +130 °C (the lunar range<sup class="r">[6](#s6)</sup>), with dust; then flex and abrasion. NASA's 2025 tests already showed no major losses from simulant, coiled or buried<sup class="r">[4](#s4)</sup>.
2. **UMIC.** Scale from NASA's single 1 kW module<sup class="r">[2](#s2)</sup> to a multi-kilowatt unit with transformers. Run thermal-vacuum and radiation tests.
3. **Hardware-in-the-loop grid.** Run several UMICs in parallel on simulated sources and service connections. Inject load steps and faults and check stability and that only the faulted service connection trips.
4. **Rover field trials.** Lay and recover 1 km reels of cable on simulant slopes, and splice three of them into a full 3 km run (DD-013), and ten into a 10 km extended run (DD-014). Measure tension, payout accuracy and how the cable lies on rough ground.
5. **On the Moon.** Use LunaGrid-Lite's flight results<sup class="r">[7](#s7)</sup> to set the first route. Energise each link at low voltage first, then 3 kV. Record its TDR signature as a baseline.

## Open questions

- How should surface cables be protected from rover traffic and micrometeoroids, given that NASA advises against burial<sup class="r">[3](#s3)</sup>?
- Will LR-1 deliver 1 kHz itself, or does the reactor end need a frequency converter (DD-013)?
- What DC bus voltage will a KRUSTY-class unit's controllers hold, and does it match a UMIC-class inverter's 120 V DC input (DD-013)?
- Which ridge points and ISRU sites need extended runs, and how much illumination does the base gain from them against ~10–15% loss each (DD-013, DD-014)?
- What are the 1 kHz cable charging current, inductance and stability margin of a 10 km run of this cable? NASA has not published them, and each extended run needs this analysis before approval (DD-014).
- Does an extended run need receiving-end voltage regulation, transformer taps, or a thicker cable (DD-014)?
- How far beyond 10 km must the mobile power cart reach for PSR work (DD-014)?
- How do many inverter-only sources share control, with the PMC setting how much each one supplies?
- How large should each service connection be? Each unit's rating waits for the Phase 1 load budget.
- If radiation-hard high-voltage switches mature, would a DC upgrade be worth revisiting? (See DD-001.)
- Can aluminium cable later be made on the Moon (M12)?
