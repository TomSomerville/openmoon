---
id_code: "C04.1"
milestone: M04
order: 1
title: Fission surface power unit
summary: "An LR-1-class nuclear reactor that makes at least 20 kW of electricity day and night for at least five years. It feeds the base power management controller (PMC), which routes its power to the grid or to storage, carrying the base through polar darkness. KRUSTY-class 1 kWe units can serve small remote loads."
trl: 4
spec:
  - {k: "Output", v: "≥20 kWe at 3 kV RMS AC after any single failure (LR-1-class, plan baseline); KRUSTY-class 1 kWe for small loads (DD-002)"}
  - {k: "Output interface", v: "3 kV, 3-phase, 1 kHz at the reactor output (plan requirement, DD-010); SPARC sets 3 kV RMS but no frequency: vendor spec or frequency converter at the reactor end (open)"}
  - {k: "Run to PMC", v: "≤3 km of cable (DD-010)"}
  - {k: "Output path", v: "3 kV AC line to the base PMC, which routes power to the grid, to storage, or both (C04.3, DD-003, DD-008); excess to the parasitic load radiator"}
  - {k: "Reactor heat", v: "Not yet designed for LR-1; NASA 40 kWe references ~175 kWt (Stirling) to ~230 kWt (Brayton)"}
  - {k: "Mass", v: "<15 t incl. lander adapters (LR-1 cap); NASA 40 kWe references 6.8–7.5 t incl. 20% growth"}
  - {k: "Conversion", v: "Closed Brayton (LR-1 requirement); KRUSTY-class units use Stirling"}
  - {k: "Radiators", v: "NASA 40 kWe references ~140 m² (Stirling) to ~180 m² (Brayton)"}
  - {k: "Crew distance", v: "≥1 km behind a 36° shadow shield; ≤5 rem/yr at 1 km; no more than 3 km of cable run to the PMC (DD-010)"}
  - {k: "Design life", v: "≥5 years at full power (LR-1); 10 years (NASA 40 kWe reference)"}
  - {k: "Start-up", v: "Remote, about 8 h to full power"}
  - {k: "Delivery", v: "1 heavy cargo lander; reactor pallet stays on the lander"}
subcomponents:
  - name: Reactor core
    desc: "Makes the heat. HALEU fuel pins in a hydride moderator, surrounded by a reflector that controls the chain reaction."
    parts: ["HALEU uranium nitride fuel pins", "Yttrium hydride moderator", "Beryllium oxide reflector", "Control drums or sliding reflector with actuators", "Launch shutdown lock (plan design choice)"]
    tech: "KRUSTY (2018) heritage; NASA/DOE reference design"
    trl: 4
  - name: Power conversion
    desc: "Turns reactor heat into electricity. Free-piston Stirling engines or closed Brayton turbines, in four independent strings."
    parts: ["Closed Brayton turboalternator strings (LR-1 requirement; NASA 40 kWe reference used 4 × ~11.7 kWe)", "Three-phase alternators on the turbine shaft", "Recuperator and gas cooler", "Hot-end heat exchanger", "Gas bearings"]
    tech: "NASA Glenn Brayton test units; SR-1 Freedom flight (2028); KRUSTY Stirling converters for KRUSTY-class units"
    trl: 4
  - name: Heat transport
    desc: "Moves heat from the core to the converters without pumps, using sealed sodium heat pipes."
    parts: ["Sodium heat pipes", "NaK or gas-plenum primary heat exchanger", "Heat-pipe wicks (Na–Mo, steel)", "Insulation and thermal shield"]
    tech: "KRUSTY sodium heat pipes"
    trl: 5
  - name: Radiators
    desc: "Throws away the waste heat to space. Two vertical wings of panels with water heat pipes."
    parts: ["Composite panels, 2.5 × 2 m each", "Embedded titanium–water heat pipes", "Pumped water manifold and pumps", "Scissor deployment mechanism", "Parasitic load (shunt) radiator"]
    tech: "ISS radiator heritage; NASA GRC composite panels"
    trl: 5
  - name: Radiation shield
    desc: "A one-sided shadow shield that protects the crew zone, plus distance."
    parts: ["Lithium hydride neutron layer", "Tungsten gamma layer", "Shield structure and cooling", "Keep-out zone markers and dosimeters"]
    tech: "NASA/DOE reference shield"
    trl: 4
  - name: Control, instrumentation and power management
    desc: "Runs the reactor and converters by itself, matches load, and steps voltage up for the long cable to the base PMC."
    parts: ["Neutron and temperature sensors", "Reactor control computer and Ka-band radio", "Brayton (or Stirling) controllers", "Start-up Li-ion battery (~4 kWh)", "Step-up transformers to 3 kV RMS AC, 3-phase, 1 kHz at the output (DD-010)", "Frequency converter at the reactor end if the vendor's alternator frequency is not 1 kHz (open, DD-010)", "KRUSTY-class units: controller DC bus, UMIC-class inverter and 1 kHz step-up transformer at the unit (DD-010)", "Command and data link to the PMC (C04.3)"]
    tech: "NASA GRC Stirling controllers; ISS-class PMAD"
    trl: 4
  - name: Deployment and lander interface
    desc: "Gets the unit off the cargo lander and the user interface out to the start of the source line to the PMC."
    parts: ["Reactor pallet adapter on lander", "User interface pallet on a sled", "1 km high-voltage cable spools, up to 3 for a 3 km run (DD-010)", "Utility rover for towing", "Levelling legs"]
    tech: "NASA DAC3 concept of operations"
    trl: 4
risks:
  - {sev: Critical, title: "The US requirement keeps changing (40 kWe Stirling in 2022, ≥100 kWe Brayton in 2025, ≥20 kWe Brayton in the 2026 draft) and no reactor contract exists.", fix: "Plan on the LR-1 minimum of 20 kWe (DD-002); specify only the interface to the PMC (3 kV AC, 0–100% load, fault data) and buy whichever unit flies first; keep the solar-plus-storage fallback in C04.2 and C04.3."}
  - {sev: High, title: "A KRUSTY-class flight unit does not exist; only a DARPA–Los Alamos ground-test agreement (Oct 2026) is active.", fix: "Use KRUSTY-class units only for small, non-critical loads; do not depend on them for the habitat."}
  - {sev: Critical, title: "Radiation dose to crew if the unit lands or is placed wrongly.", fix: "Land the reactor ≥1 km from the crew zone, inside the shield's 36° shadow; add terrain or berms; monitor dose all the time at the user point."}
  - {sev: High, title: "A converter string fails; the 2022 concept carried no spares, so each lost pair cost about a quarter of output.", fix: "Use four 25% strings with separate radiator loops and controllers, and size the base's essential load below 75% of output."}
  - {sev: High, title: "Lunar dust on hundreds of square metres of radiator could cut heat rejection; the effect is not yet measured.", fix: "Fund NASA's radiator dust tests to completion; place the unit far from landing pads; add 20% radiator area margin."}
  - {sev: High, title: "Mass growth: the 2022 design hit ~10 t against a 6 t goal, and LR-1 allows up to 15 t.", fix: "Keep the reactor on its lander (the lightest NASA option) and move only the ~1 t user interface pallet; budget 7.5–15 t delivery."}
  - {sev: High, title: "Radiation-hard power switches are rated far below the transmission voltage.", fix: "Step up with a transformer after a low-voltage inverter at the source, so only low-voltage switches are used (DD-010); see C04.4."}
  - {sev: Medium, title: "The LR-1 requirements set 3 kV RMS AC but no frequency, and NASA's 2025 Brayton reference ran its alternators at 2 kHz; the base grid runs at 1 kHz.", fix: "Specify 3 kV, 3-phase, 1 kHz at the reactor output in any purchase, or add a frequency converter at the reactor end (open, DD-010)."}
  - {sev: Medium, title: "Organic parts in Stirling alternators and superalloys in vacuum may degrade over 10 years.", fix: "Complete the irradiation and metal-vaporisation tests now running at NASA and DOE before flight design freeze."}
  - {sev: Medium, title: "Nuclear launch approval and fuel supply can slip the schedule.", fix: "Start approval paperwork at contract award; size the first two years of the base to run on solar plus storage."}
sources:
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Oleson et al., NASA GRC: A Deployable 40 kWe Lunar Fission Surface Power Concept (NETS 2022)", url: "https://ntrs.nasa.gov/citations/20220004670", date: "May 2022"}
  - {title: "INL/NASA: Fission Surface Power Technical Maturation Webinar (government reference design)", url: "https://inl.gov/content/uploads/2024/11/FSP-Technical-Maturation-Webinar-Final-250924-1.pdf", date: "Sep 2025"}
  - {title: "Poston et al.: Results of the KRUSTY nuclear system test", url: "https://ntrs.nasa.gov/citations/20205009351", date: "2020"}
  - {title: "NewSpace Economy: What NASA's SPARC procurement reveals about Lunar Reactor-1 (secondary)", url: "https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/", date: "Sep 2026"}
  - {title: "NASA: NASA seeks industry feedback on fission surface power", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-seeks-industry-feedback-on-fission-surface-power/", date: "Aug 2025"}
  - {title: "Barth & Pike, NASA GRC: Lunar power transmission for fission surface power", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", date: "2022"}
  - {title: "NASA Glenn: SPARC Industry Day presentation (Lunar Reactor-1 requirements)", url: "https://sam.gov/api/prod/opps/v3/opportunities/resources/files/6b927f8dc6c843749a45b2c0589bf0e7/download", date: "Sep 2026"}
---

## What it does

{% include decision-note.html id="DD-002" extra="This component was first sized as one 40 kWe-class reactor feeding the grid directly. On 18 November 2026 it changed to an LR-1-class 20 kWe reactor (or KRUSTY-class 1 kWe units for small loads). Its first rule, that the reactor only charges a battery, was later widened by DD-003." %}

{% include decision-note.html id="DD-003" extra="The reactor feeds the power management controller (PMC; called the BMS until DD-008), which decides whether its power goes to the grid, to storage, or both." %}

The fission unit is the base's night-time anchor. Polar sites can be dark for up to about 100 hours at a time<sup class="r">[1](#s1)</sup>, and the US reactor draft asks for operation through at least 354 hours of darkness<sup class="r">[5](#s5)</sup>. An LR-1-class reactor makes at least 20 kWe after any single failure<sup class="r">[8](#s8)</sup>, which is 480 kWh a day (this plan's arithmetic).

**It feeds the PMC.** The 3 kV AC line from the reactor ends at the base power management controller (PMC, C04.3). The PMC sends the power to the grid to meet demand, into storage, or some of each (design changes DD-003 and DD-008). When demand is met and storage is full, the PMC tells the reactor to send its excess power to its parasitic load radiator (PLR). LR-1 is required to accept any load from 0 to 100% of its output and to start up into that radiator<sup class="r">[8](#s8)</sup>, so this needs nothing special from the reactor.

**Two reactor types (DD-002).**
- **LR-1-class, 20 kWe.** The base reactor. NASA is buying it through SPARC; no design or award yet<sup class="r">[8](#s8)</sup>. See the [Lunar Reactor-1 card](/technology/us-lunar-reactor-1-sparc/).
- **KRUSTY-class, 1 kWe.** A Kilopower-type Stirling unit for small remote loads, such as a comms or science node. KRUSTY proved the reactor in 2018, but no flight unit is being built<sup class="r">[4](#s4)</sup>. See the [Kilopower / KRUSTY card](/technology/kilopower-krusty-fission-test/).

**Interface and distance (design change DD-010).** The plan's interface requirement is **3 kV, 3-phase, 1 kHz at the reactor's output**, with no more than **3 km** of cable run to the PMC. LR-1 must deliver 3 kV RMS AC, but its requirements do not set the frequency<sup class="r">[8](#s8)</sup>. NASA's 2025 reference Brayton alternators gave 240 Vrms at 2 kHz, 3-phase, stepped up by a transformer<sup class="r">[3](#s3)</sup>. Whether 1 kHz is specified to the vendor or made by a frequency converter at the reactor end is **open**. A KRUSTY-class unit converts its controllers' DC bus to 3 kV AC with its own inverter and transformer (see the [Kilopower / KRUSTY card](/technology/kilopower-krusty-fission-test/)).

{% include decision-note.html id="DD-010" extra="The reactor link was described as 1–3 km with no set maximum or frequency." %}

## How it works

- **Core.** NASA's 40 kWe concept uses about 20% enriched uranium nitride pellets, sodium–molybdenum heat pipes and a yttrium hydride moderator, at about 250 kWth<sup class="r">[2](#s2)</sup>. KRUSTY proved the basic idea in 2018. It ran a heat-pipe reactor with Stirling converters for 28 hours, at up to 5 kWt and 880 °C fuel temperature, and it followed the converters' load demand on its own<sup class="r">[4](#s4)</sup>.
- **Heat pipes.** KRUSTY was the first reactor cooled mainly by heat pipes. Its sodium pipes began carrying real power once the core reached about 500 °C<sup class="r">[4](#s4)</sup>.
- **Stirling or Brayton.** NASA's 2025 reference design (40 kWe) compared the two<sup class="r">[3](#s3)</sup>:

| | Free-piston Stirling | Closed Brayton |
|---|---|---|
| Units | 4 × 12.6 kW | 4 × 11.7 kWe |
| Converter efficiency | 29% | 20% |
| Mass per converter | 250 kg | 300 kg |
| Radiator area | 140 m² | 180 m² |
| Power electronics efficiency | 83% | 90% |
| Total with 20% growth | 6.8 t | 7.5 t |

Stirling is about 10% lighter. Brayton gives simpler power electronics<sup class="r">[3](#s3)</sup>. NASA's 2025 request and the 2026 Lunar Reactor-1 draft both name closed Brayton<sup class="r">[6](#s6)</sup><sup class="r">[5](#s5)</sup>. NASA rated 10 kWe-class Stirling at TRL 5 and Brayton at TRL 4<sup class="r">[3](#s3)</sup>. The base reactor is therefore Brayton; only KRUSTY-class units use Stirling.
- **Radiators.** These are polymer composite panels with titanium–water heat pipes, 2.5 × 2 m each, arranged in two wings<sup class="r">[3](#s3)</sup>. An earlier ISS-style design needed 133.4 m² at the pole and 62% more at the equator<sup class="r">[2](#s2)</sup>.
- **Shield.** A directional shield with a 36° included angle keeps the dose below 5 rem/yr at 1 km<sup class="r">[3](#s3)</sup>. In the 2022 concept, the lithium hydride and tungsten shield weighed 1,250 kg<sup class="r">[2](#s2)</sup>.
- **Control and power.** Stirling engines need a constant electrical load. The controllers therefore dump unused power into a resistor bank or radiator<sup class="r">[2](#s2)</sup>. A 4 kWh Li-ion battery handles start-up<sup class="r">[2](#s2)</sup>.
- **Deployment.** In NASA's reference option, the reactor pallet (about 6 t) stays on its lander. A rover tows the user interface pallet (about 1 t) to the end of a 1 km cable. Start-up takes about 8 hours<sup class="r">[3](#s3)</sup>.

## Sizing

LR-1 has no published design yet; its cap is 15,000 kg including lander adapters<sup class="r">[8](#s8)</sup>. The best published breakdown is NASA's 2025 40 kWe reference, in kg<sup class="r">[3](#s3)</sup>:

| Item | Brayton | Stirling |
|---|---|---|
| Reactor | 1,413 | 1,132 |
| Shield | 1,500 | 1,370 |
| Power conversion | 1,182 | 995 |
| Heat rejection | 884 | 701 |
| Local power electronics | 401 | 613 |
| User interface pallet (incl. 325 kg cable and spool) | 872 | 872 |
| **Total with 20% growth** | **7,502** | **6,820** |

Worked numbers:

- **Specific mass (this plan's arithmetic).** 6,820 kg ÷ 40 kWe ≈ 170 kg/kWe. NASA's 2022 figure was 250–270 kg/kW<sup class="r">[1](#s1)</sup>. At LR-1's cap, 15,000 kg ÷ 20 kWe = 750 kg/kWe; the plan budgets 7.5–15 t per unit.
- **Dose at greater distance (ESTIMATE).** Dose falls with 1/r²<sup class="r">[3](#s3)</sup>. At 2 km, the 1 km limit of 5 rem/yr becomes about 1.25 rem/yr. This ignores scatter from the ground.
- **Cable.** The unit connects over a 3 kV, 1 kHz AC link of no more than 3 km (DD-010), NASA's lunar grid baseline and LR-1's required voltage<sup class="r">[8](#s8)</sup>, to the PMC at the base. At NASA's 325 kg per km<sup class="r">[3](#s3)</sup>, a full 3 km run is about 1 t of cable and spool (this plan's arithmetic) (see C04.3, C04.4 and design changes DD-001, DD-002, DD-003 and DD-008).

## Testing and qualification

1. **Components.** Irradiate fuel, moderator, alternator organics and sensors. Run long vacuum tests on heat pipes and superalloys<sup class="r">[3](#s3)</sup>.
2. **Engineering test unit.** Build a full non-nuclear system with electric heaters in place of the core, as the Lunar Reactor-1 draft requires<sup class="r">[5](#s5)</sup>. Test it in thermal vacuum with radiators and the full cable.
3. **Nuclear ground test.** Repeat the KRUSTY method at flight scale: zero-power criticals, then a powered run with load-following and loss-of-cooling transients<sup class="r">[4](#s4)</sup>.
4. **Dust and deployment.** Load radiators with regolith simulant. Practise towing the user interface pallet on slopes up to 10°<sup class="r">[5](#s5)</sup>.
5. **On the Moon.** Commission it step by step: start-up into the parasitic load radiator, radiation mapping, power setpoint changes, string shutdown and restart, and day–night transients<sup class="r">[3](#s3)</sup><sup class="r">[8](#s8)</sup>. Then test the PMC hand-offs: switch between serving the grid and charging storage, fill storage, and check the reactor moves the surplus to its radiator smoothly. M04 exit requires 20 kWe to the PMC for six months.

## Open questions

- Will anyone build a flight KRUSTY-class unit, or will small loads need radioisotope or solar power instead?
- Will the LR-1 vendor deliver 1 kHz, or does the plan add a frequency converter at the reactor end (DD-010)?
- Should a second LR-1-class unit come early, so the base is not dependent on one reactor?
- How much does dust really reduce radiator performance after years near active landing pads?
- Can a regolith berm replace part of the 1.4–1.5 t shield, and at what rover effort?
- What is the best spare strategy: a fifth converter string, or a second smaller reactor later?
- How is the unit made safe and stored at end of life?
