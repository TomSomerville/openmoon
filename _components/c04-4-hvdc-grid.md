---
id_code: "C04.4"
milestone: M04
order: 4
title: HVDC grid and cable-laying rover
summary: "High-voltage DC cables, converters and switches that link the reactor, solar towers and storage to the habitat and oxygen plant. A small rover lays and covers the cable."
trl: 4
spec:
  - {k: "Trunk voltage", v: "±4 kVDC (8 kV pole to pole)"}
  - {k: "User voltage", v: "120 VDC microgrids"}
  - {k: "Conductor", v: "Aluminium, FEP insulation, vacuum rated"}
  - {k: "Trunk length", v: "1–3 km per link; ≥3 km laid in M04"}
  - {k: "Cable efficiency", v: "95% at 3 km, 40 kW"}
  - {k: "Cable mass", v: "~240 kg per 3 km, 40 kW link (NASA-derived)"}
  - {k: "Converters", v: "Modular DC–DC, ~96% each; ~78% Stirling-to-user end to end"}
  - {k: "Microgrids", v: "2 (habitat, ISRU) plus source nodes"}
  - {k: "Rover", v: "1 cable layer, ~0.4 t reel per trip (ESTIMATE)"}
  - {k: "Fault location", v: "Time-domain reflectometry from each node"}
subcomponents:
  - name: Transmission cable
    desc: "Carries power 1–3 km at high voltage so the conductor can be thin and light."
    parts: ["Aluminium conductor (≥16 AWG)", "FEP insulation (design stress 4.4 kV/mm)", "Outer FEP jacket", "Vacuum-rated HV connectors and splices", "Cable markers"]
    tech: "NASA GRC transmission studies; terrestrial HV cable practice"
    trl: 4
  - name: High-voltage converters
    desc: "Step voltage up at each source and down at each user, using stacks of low-voltage switches."
    parts: ["Series-stacked DC–DC modules (175 V class switches)", "High-frequency isolation transformers", "Filter capacitors", "Universal Modular Interface Converter (UMIC) to 120 VDC", "AC–DC tie converter for an AC reactor interface"]
    tech: "NASA GRC ABSS converter (to 600 V); MIPS/UMIC"
    trl: 4
  - name: Switchgear and protection
    desc: "Isolates faults quickly so one bad cable or load cannot drop the whole grid."
    parts: ["Solid-state DC circuit breakers", "Mechanical disconnects for maintenance", "Current-limiting in converters", "Insulation monitoring and grounding", "Surge protection"]
    tech: "Ohio State T-Breaker / DC energy router (NASA LuSTR)"
    trl: 3
  - name: Microgrids and control
    desc: "Runs habitat and ISRU as separate local grids that can share power over the trunk."
    parts: ["120 VDC buses and power distribution units", "Regional grid controller", "Local microgrid controllers", "Priority load-shedding tables", "Earth link for remote operation"]
    tech: "NASA Artemis Base Camp microgrid studies; Autonomous Power Control project"
    trl: 5
  - name: Cable-laying rover
    desc: "Carries a cable reel from the lander, unreels it along a surveyed route and covers it."
    parts: ["Rover chassis and drive", "Powered reel with tension control", "Cable guide and payout counter", "Shallow plough or regolith cover blade", "Route cameras and lidar"]
    tech: "Astrobotic LunaGrid-Lite CubeRover and cable deployer"
    trl: 5
  - name: Fault location and monitoring
    desc: "Finds and locates cable faults without sending a rover to walk the whole line."
    parts: ["Time-domain reflectometer at each node", "Insulation resistance monitor", "Partial-discharge sensors", "Current and voltage sensors", "Fault log to the grid controller"]
    tech: "Terrestrial TDR practice, to be adapted for lunar use"
    trl: 4
risks:
  - {sev: Critical, title: "Radiation-hard switches are rated only ~120–160 V, far below ±4 kV, and DC breakers for space are still research.", fix: "Use series-stacked modules of flight-rated switches; keep AC transmission with transformers as a fallback; let trunk voltage be chosen per link."}
  - {sev: High, title: "Sources may arrive with different interfaces: the reactor draft asks for 3 kV AC, and LunaGrid targets 1 kV AC.", fix: "Put a standard tie converter (UMIC class) at every source and user, so the trunk standard is fixed in one place."}
  - {sev: High, title: "High voltage in vacuum risks partial discharge and arcing, made worse by abrasive dust on insulation.", fix: "Use a 5× insulation margin, sealed connectors, and partial-discharge testing in vacuum with dust before flight."}
  - {sev: High, title: "Cables on the surface can be damaged by rovers, thermal cycling and micrometeoroids; NASA's sizing had no impact shielding or redundancy.", fix: "Cover or bury cables; mark crossings; build a ring so every node has two paths."}
  - {sev: Medium, title: "Laying long cables on rough terrain can snag or overstress the cable; LunaGrid-Lite's demo length dropped from 1 km to 500 m.", fix: "Survey routes from orbit and by rover first; use 1 km reels with field splices; monitor tension and payout."}
  - {sev: Medium, title: "DC faults are hard to interrupt because current never passes through zero.", fix: "Converters limit fault current within microseconds; solid-state breakers open the faulted section; mechanical switches isolate it after."}
  - {sev: Medium, title: "Sunlit cables run hot, raising aluminium resistance and losses.", fix: "Cover cables with regolith; size for the hot case; monitor line losses."}
sources:
  - {title: "Barth & Pike, NASA GRC: Lunar power transmission for fission surface power", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", date: "2022"}
  - {title: "Oleson et al., NASA GRC: A Deployable 40 kWe Lunar Fission Surface Power Concept (NETS 2022)", url: "https://ntrs.nasa.gov/citations/20220004670", date: "May 2022"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "INL/NASA: Fission Surface Power Technical Maturation Webinar", url: "https://inl.gov/content/uploads/2024/11/FSP-Technical-Maturation-Webinar-Final-250924-1.pdf", date: "Sep 2025"}
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", date: "2025"}
  - {title: "SatNews: Astrobotic's LunaGrid VSAT enters thermal vacuum testing (press)", url: "https://satnews.com/2024/07/20/astrobotics-lunagrids-vertical-solar-array-technology-vsat-enters-tvac/", date: "Jul 2024"}
  - {title: "NewSpace Economy: What NASA's SPARC procurement reveals about Lunar Reactor-1 (secondary)", url: "https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/", date: "Sep 2026"}
  - {title: "Wikipedia: Time-domain reflectometer", url: "https://en.wikipedia.org/wiki/Time-domain_reflectometer", date: "2026"}
  - {title: "Wikipedia: Aluminium", url: "https://en.wikipedia.org/wiki/Aluminium", date: "2026"}
  - {title: "NASA GCD: Vertical Solar Array Technology project annual review", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
---

## What it does

The grid moves power from where it is made to where it is used. The reactor sits 1–3 km from users<sup class="r">[1](#s1)</sup>, and the oxygen plant needs power over 3–5 km<sup class="r">[3](#s3)</sup>. NASA's baseline is two independent microgrids, one for the habitat and one for ISRU, each with its own sources. A primary line lets them share power<sup class="r">[3](#s3)</sup>.

## How it works

- **Why high voltage.** At fixed efficiency, conductor mass falls with the square of voltage until insulation mass takes over<sup class="r">[1](#s1)</sup>. For a 40 kW, 3 km, 95% efficient aluminium DC cable, the lightest point is about ±4,000 VDC<sup class="r">[1](#s1)</sup>. The same 3 km cable weighs 3,300 kg at 500 V but 240 kg at 2,800 V<sup class="r">[2](#s2)</sup>. A DC cable is a little lighter than an AC cable at the same rating<sup class="r">[1](#s1)</sup>.
- **Cable.** NASA assumed FEP insulation at 4.4 kV/mm (5 times the minimum breakdown thickness), a 0.6 mm FEP jacket, and conductors no thinner than 16 AWG. The design had no micrometeoroid shielding<sup class="r">[1](#s1)</sup>.
- **Converters.** Fully space-qualified silicon switches are limited to 160 V, so DC step-up needs stacked modules<sup class="r">[1](#s1)</sup>. NASA's series-stacked step-down converter has run up to 600 V<sup class="r">[1](#s1)</sup>. A DC link needs about 4 times as many parts as an AC link<sup class="r">[1](#s1)</sup>. In NASA's 40 kWe concept, the step-down converter was 96.1% efficient and the distribution unit 98.4%. It fed eight 5 kWe outputs at 120 VDC<sup class="r">[2](#s2)</sup>. Sources will not all speak the same language. The US reactor draft asks for a 3 kV AC interface at 1 km<sup class="r">[7](#s7)</sup>, and Astrobotic proposed high-voltage AC for its towers<sup class="r">[10](#s10)</sup>. Open Moon therefore puts a tie converter at every source. NASA's UMIC is a bidirectional, modular converter that joins 120 VDC microgrids to the transmission line<sup class="r">[3](#s3)</sup>.
- **Protection.** DC breakers must put out an arc, because DC current never passes through zero; high-voltage DC breakers are still being researched<sup class="r">[1](#s1)</sup>. Ohio State is building a modular "T-Breaker" DC energy router for lunar microgrids under NASA funding<sup class="r">[3](#s3)</sup>.
- **Control.** Each microgrid controls its own power. A regional controller makes power go to the highest-priority loads, such as the crewed habitat<sup class="r">[3](#s3)</sup>.
- **Cable laying.** Astrobotic's LunaGrid-Lite pairs a 4U CubeRover with a robotic cable deployer. It is planned to carry 1 kW over 500 m of abrasion-resistant cable, with a high-voltage converter co-designed by NASA Glenn<sup class="r">[5](#s5)</sup>. Earlier plans said 1 km, at a target of 1 kV and 1 kHz AC<sup class="r">[6](#s6)</sup>. Open Moon needs a larger rover of the same kind for heavier ±4 kV cable.
- **Fault location.** A time-domain reflectometer sends a pulse down the line and times the echo from any impedance change. An open circuit echoes with the same polarity and a short with the opposite polarity<sup class="r">[8](#s8)</sup>.

## Sizing

One 40 kW, 3 km link (this plan's arithmetic):

| Quantity | Working | Result |
|---|---|---|
| Current at ±4 kV | 40 kW ÷ 8 kV | 5 A |
| Allowed loss (95%) | 5% × 40 kW | 2 kW (0.7 W/m<sup class="r">[1](#s1)</sup>) |
| Loop resistance | 2,000 W ÷ 5² | 80 Ω over 6 km = 13.3 Ω/km |
| Aluminium area | 26.5 nΩ·m<sup class="r">[9](#s9)</sup> ÷ 0.0133 Ω/m | ~2.0 mm² |
| Aluminium mass | 2.0 mm² × 6 km × 2,699 kg/m³<sup class="r">[9](#s9)</sup> | ~32 kg |
| Whole cable incl. insulation | NASA, 2,800 V case<sup class="r">[2](#s2)</sup> | ~240 kg |
| Same power at 120 V | 40 kW ÷ 120 V | 333 A (impractical) |

Insulation, not metal, dominates cable mass at these voltages.

- **Reel mass (ESTIMATE).** NASA's 1 km cable plus spool was 325 kg in its 3 kV AC reference<sup class="r">[4](#s4)</sup>. A 1 km ±4 kV reel of about 0.3–0.4 t is a fair planning figure, so the rover lays 3 km in three trips.
- **Fault location (ESTIMATE).** With signal speed about 66% of light speed<sup class="r">[8](#s8)</sup>, a 1 µs echo means a fault about 100 m away. 10 ns timing locates it to about 1 m.

## Testing and qualification

1. **Cable samples.** Run partial-discharge and breakdown tests in vacuum at −173 to +130 °C (the lunar range<sup class="r">[3](#s3)</sup>), with dust. Then flex and abrasion tests.
2. **Converter stack.** Raise the stacked converter from 600 V to ±4 kV in steps. Irradiate the parts for single-event effects.
3. **Hardware-in-the-loop microgrid.** Connect real converters to simulated sources and loads. Inject faults and check that only the faulted section trips.
4. **Rover field trials.** Lay and recover 1 km of cable on simulant slopes. Measure tension, payout accuracy and cover depth.
5. **On the Moon.** Use LunaGrid-Lite's flight results<sup class="r">[5](#s5)</sup> to set the first route. Energise each link at low voltage first, then at full voltage. Map its TDR signature as a baseline.

## Open questions

- DC or AC trunk? NASA studies call the masses comparable, but AC needs fewer parts<sup class="r">[1](#s1)</sup><sup class="r">[4](#s4)</sup>.
- How deep must cable be buried to survive heat, micrometeoroids and rover traffic?
- Can one standard tie converter serve the reactor, solar towers, storage and users?
- Which lunar-qualified DC breaker design will be ready first?
- Can aluminium cable later be made on the Moon (M12)?
