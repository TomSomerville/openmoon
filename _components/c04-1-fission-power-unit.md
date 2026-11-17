---
id_code: "C04.1"
milestone: M04
order: 1
title: Fission surface power unit
summary: "A small nuclear reactor that makes about 40 kW of electricity day and night for ten years. It carries the base through polar darkness that solar towers and storage cannot cover."
trl: 4
spec:
  - {k: "Output", v: "40 kWe net at the user (plan baseline); grid accepts any 20–100 kWe unit"}
  - {k: "Reactor heat", v: "~175 kWt (Stirling) to ~230 kWt (Brayton), NASA reference designs"}
  - {k: "Mass", v: "~6.8 t (Stirling) to ~7.5 t (Brayton) incl. 20% growth; older deployable concept ~10 t"}
  - {k: "Conversion", v: "4 × ~12 kWe Stirling or closed Brayton strings; ≥75% power after first failure"}
  - {k: "Radiators", v: "~140 m² (Stirling) to ~180 m² (Brayton)"}
  - {k: "Crew distance", v: "≥1 km behind a 36° shadow shield; ≤5 rem/yr at 1 km"}
  - {k: "Design life", v: "10 years (NASA reference); ≥5 years (LR-1 draft)"}
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
    parts: ["4 × ~12.6 kW Stirling converters (or 4 × ~11.7 kWe Brayton units)", "Linear alternators (Stirling) or 2 kHz three-phase alternators (Brayton)", "Hot-end heat exchangers", "Cold-end coolant interface", "Gas bearings"]
    tech: "KRUSTY Stirling converters; NASA Glenn Brayton test units"
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
    desc: "Runs the reactor and converters by itself, matches load, and steps voltage up for the long cable."
    parts: ["Neutron and temperature sensors", "Reactor control computer and Ka-band radio", "Stirling or Brayton controllers", "Start-up Li-ion battery (~4 kWh)", "Step-up converters or transformers", "User interface pallet with 120 VDC outputs"]
    tech: "NASA GRC Stirling controllers; ISS-class PMAD"
    trl: 4
  - name: Deployment and lander interface
    desc: "Gets the unit off the cargo lander and the user interface out to the grid tie point."
    parts: ["Reactor pallet adapter on lander", "User interface pallet on a sled", "1 km high-voltage cable spool", "Utility rover for towing", "Levelling legs"]
    tech: "NASA DAC3 concept of operations"
    trl: 4
risks:
  - {sev: Critical, title: "The US requirement keeps changing (40 kWe Stirling in 2022, ≥100 kWe Brayton in 2025, ≥20 kWe Brayton in the 2026 draft) and no reactor contract exists.", fix: "Specify only the grid interface (power range, voltage, fault behaviour) and buy whichever unit flies first; keep the solar-plus-storage fallback in C04.2 and C04.3."}
  - {sev: Critical, title: "Radiation dose to crew if the unit lands or is placed wrongly.", fix: "Land the reactor ≥1 km from the crew zone, inside the shield's 36° shadow; add terrain or berms; monitor dose all the time at the user point."}
  - {sev: High, title: "A converter string fails; the 2022 concept carried no spares, so each lost pair cost about a quarter of output.", fix: "Use four 25% strings with separate radiator loops and controllers, and size the base's essential load below 75% of output."}
  - {sev: High, title: "Lunar dust on hundreds of square metres of radiator could cut heat rejection; the effect is not yet measured.", fix: "Fund NASA's radiator dust tests to completion; place the unit far from landing pads; add 20% radiator area margin."}
  - {sev: High, title: "Mass growth: the 2022 design hit ~10 t against a 6 t goal.", fix: "Keep the reactor on its lander (the lightest NASA option) and move only the ~1 t user interface pallet."}
  - {sev: High, title: "Radiation-hard power switches are rated far below the transmission voltage.", fix: "Use transformers (AC) or stacked low-voltage modules (DC) for step-up; see C04.4."}
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
---

## What it does

The fission unit is the base's night-time anchor. Polar sites can be dark for up to about 100 hours at a time<sup class="r">[1](#s1)</sup>, and the US reactor draft asks for operation through at least 354 hours of darkness<sup class="r">[5](#s5)</sup>. A reactor of about 40 kWe covers the oxygen pilot plant or the habitat through any shadow, and lets the solar towers handle the daytime peaks.

## How it works

- **Core.** NASA's 40 kWe concept uses about 20% enriched uranium nitride pellets, sodium–molybdenum heat pipes and a yttrium hydride moderator, at about 250 kWth<sup class="r">[2](#s2)</sup>. KRUSTY proved the basic idea in 2018. It ran a heat-pipe reactor with Stirling converters for 28 hours, at up to 5 kWt and 880 °C fuel temperature, and it followed the converters' load demand on its own<sup class="r">[4](#s4)</sup>.
- **Heat pipes.** KRUSTY was the first reactor cooled mainly by heat pipes. Its sodium pipes began carrying real power once the core reached about 500 °C<sup class="r">[4](#s4)</sup>.
- **Stirling or Brayton.** NASA's 2025 reference design compared the two<sup class="r">[3](#s3)</sup>:

| | Free-piston Stirling | Closed Brayton |
|---|---|---|
| Units | 4 × 12.6 kW | 4 × 11.7 kWe |
| Converter efficiency | 29% | 20% |
| Mass per converter | 250 kg | 300 kg |
| Radiator area | 140 m² | 180 m² |
| Power electronics efficiency | 83% | 90% |
| Total with 20% growth | 6.8 t | 7.5 t |

Stirling is about 10% lighter. Brayton gives simpler power electronics<sup class="r">[3](#s3)</sup>. NASA's 2025 request and the 2026 Lunar Reactor-1 draft both name closed Brayton<sup class="r">[6](#s6)</sup><sup class="r">[5](#s5)</sup>. NASA rated 10 kWe-class Stirling at TRL 5 and Brayton at TRL 4<sup class="r">[3](#s3)</sup>. Open Moon accepts either.
- **Radiators.** These are polymer composite panels with titanium–water heat pipes, 2.5 × 2 m each, arranged in two wings<sup class="r">[3](#s3)</sup>. An earlier ISS-style design needed 133.4 m² at the pole and 62% more at the equator<sup class="r">[2](#s2)</sup>.
- **Shield.** A directional shield with a 36° included angle keeps the dose below 5 rem/yr at 1 km<sup class="r">[3](#s3)</sup>. In the 2022 concept, the lithium hydride and tungsten shield weighed 1,250 kg<sup class="r">[2](#s2)</sup>.
- **Control and power.** Stirling engines need a constant electrical load. The controllers therefore dump unused power into a resistor bank or radiator<sup class="r">[2](#s2)</sup>. A 4 kWh Li-ion battery handles start-up<sup class="r">[2](#s2)</sup>.
- **Deployment.** In NASA's reference option, the reactor pallet (about 6 t) stays on its lander. A rover tows the user interface pallet (about 1 t) to the end of a 1 km cable. Start-up takes about 8 hours<sup class="r">[3](#s3)</sup>.

## Sizing

NASA 2025 reference masses in kg<sup class="r">[3](#s3)</sup>:

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

- **Specific mass (this plan's arithmetic).** 6,820 kg ÷ 40 kWe ≈ 170 kg/kWe. NASA's 2022 figure was 250–270 kg/kW<sup class="r">[1](#s1)</sup>.
- **Dose at greater distance (ESTIMATE).** Dose falls with 1/r²<sup class="r">[3](#s3)</sup>. At 2 km, the 1 km limit of 5 rem/yr becomes about 1.25 rem/yr. This ignores scatter from the ground.
- **Cable.** At 3 km, NASA's transmission study prefers about ±4 kVDC<sup class="r">[7](#s7)</sup>; see C04.4.

## Testing and qualification

1. **Components.** Irradiate fuel, moderator, alternator organics and sensors. Run long vacuum tests on heat pipes and superalloys<sup class="r">[3](#s3)</sup>.
2. **Engineering test unit.** Build a full non-nuclear system with electric heaters in place of the core, as the Lunar Reactor-1 draft requires<sup class="r">[5](#s5)</sup>. Test it in thermal vacuum with radiators and the full cable.
3. **Nuclear ground test.** Repeat the KRUSTY method at flight scale: zero-power criticals, then a powered run with load-following and loss-of-cooling transients<sup class="r">[4](#s4)</sup>.
4. **Dust and deployment.** Load radiators with regolith simulant. Practise towing the user interface pallet on slopes up to 10°<sup class="r">[5](#s5)</sup>.
5. **On the Moon.** Commission it step by step: radiation mapping, power setpoint changes, string shutdown and restart, and day–night transients<sup class="r">[3](#s3)</sup>. M04 exit requires 40 kWe for six months.

## Open questions

- Which converter will the first flight unit actually use, and will its grid tie be 3 kV AC (as in the draft)<sup class="r">[5](#s5)</sup> or DC?
- How much does dust really reduce radiator performance after years near active landing pads?
- Can a regolith berm replace part of the 1.4–1.5 t shield, and at what rover effort?
- What is the best spare strategy: a fifth converter string, or a second smaller reactor later?
- How is the unit made safe and stored at end of life?
