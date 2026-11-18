---
id_code: "C04.2"
milestone: M04
order: 2
title: Vertical solar array towers
summary: "Tall masts that lift sun-tracking solar blankets above the shadows of polar terrain. NASA's 10 kW-class VSAT is the only tower type (DD-004); the number is set by the Phase 1 load budget."
trl: 5
spec:
  - {k: "Power", v: "10 kW per tower (NASA VSAT class)"}
  - {k: "Height", v: "≥10 m to bottom of arrays, ~16 m total"}
  - {k: "Array area", v: "36 m²"}
  - {k: "Cells", v: "Triple-junction, ~30% efficient"}
  - {k: "Mass", v: "~1 t per tower (ESTIMATE)"}
  - {k: "Slope", v: "Up to 15° at set-down, self-levelling"}
  - {k: "Life", v: "10 years at the south pole"}
  - {k: "Night survival", v: "≥96 h in darkness"}
  - {k: "Quantity", v: "N × 10 kW on 2–3 ridge points; N set by the Phase 1 load budget (provisional 10 for costing) (DD-004)"}
  - {k: "Output", v: "3 kV AC, 3-phase, 1 kHz made at the tower: array regulator, UMIC-class inverter, 1 kHz step-up transformer (DD-013)"}
  - {k: "Run to PMC", v: "≤10 km of cable from every tower (DD-013, DD-014)"}
  - {k: "Delivery", v: "Small landers for the first towers; medium landers can carry several"}
subcomponents:
  - name: Mast and deployer
    desc: "Lifts the arrays at least 10 m above the ground, and can lower them again for a move."
    parts: ["Telescoping box sections, rolled lenticular boom or helical metal band", "Winch or roller deployer", "Mast root fitting", "Retraction drive", "Load and position sensors"]
    tech: "NASA GRD; Lockheed Martin, Honeybee LAMPS and Astrobotic VSAT prototypes"
    trl: 5
  - name: Solar array blankets
    desc: "Flexible solar blankets that roll or fold out along the mast."
    parts: ["Triple-junction cells (30.7% XTJ Prime class)", "Flexible blanket substrate", "Roll-out composite booms (ROSA)", "Blanket harness", "Cover glass and coatings"]
    tech: "Redwire ROSA / iROSA on the ISS"
    trl: 6
  - name: Gimbal and sun tracking
    desc: "Keeps the mast plumb and turns the arrays to follow the low polar Sun."
    parts: ["Two-axis levelling actuators", "Azimuth rotator with slip ring", "Sun sensors", "Inclinometer", "Pointing controller"]
    tech: "NASA GRD three-axis gimbal; Astrobotic parallel-manipulator gimbal"
    trl: 5
  - name: Base and lander interface
    desc: "Holds the tower on rough ground and gets it off the lander."
    parts: ["Tripod or sled base with levelling legs", "Launch locks", "Offload interface (self-propelled or towed cart)", "Ballast or ground anchors", "Cable connector for the source line to the PMC"]
    tech: "VSAT prototype bases; Astrobotic VOLT rover base"
    trl: 5
  - name: Power electronics and night survival
    desc: "Turns the array's DC into 3 kV, 3-phase, 1 kHz AC at the tower for the line to the power management controller (PMC) (DD-013), reduces or cuts output on PMC command when storage is full, and keeps the tower alive in the dark (DD-008)."
    parts: ["Maximum-power-point converters", "Array regulator and shunt (sequential shunt unit heritage) to curtail output", "Disconnect contactor to isolate the tower", "UMIC-class low-voltage inverter (parallel 1 kW modules, DC to under 100 V AC) (DD-013)", "1 kHz step-up transformer to 3 kV AC, next to the tower (DD-013)", "Curtailment control on PMC command", "Survival battery", "Heaters and thermostats", "Avionics and radio"]
    tech: "NASA GRC UMIC; ISS sequential shunt unit; VSAT prototype avionics"
    trl: 4
  - name: Dust protection
    desc: "Limits dust build-up on the cells, mechanisms and radiators."
    parts: ["Electrodynamic dust shield on cells", "Mechanism seals", "Radiator coatings", "MLI enclosure for electronics"]
    tech: "NASA KSC Electrodynamic Dust Shield"
    trl: 5
risks:
  - {sev: High, title: "Even at 10 m, the best single point is in shadow 4–8% of the time.", fix: "Spread towers over two or three ridge points that are shadowed at different times; back them up with fission (C04.1) and storage (C04.3)."}
  - {sev: High, title: "Every tower must be within 10 km of cable run of the PMC (DD-014), and runs that long lose 10–15% of the tower's power.", fix: "M00 picks VSAT points up to 20 km apart around one PMC for the best combined light; size cables for the accepted loss; no runs longer than 10 km for now."}
  - {sev: High, title: "Tall masts can buckle or tip on slopes or soft regolith.", fix: "Use active plumbness control and wide levelling legs; test full-height towers on regolith simulant slopes before flight."}
  - {sev: High, title: "All prototype designs were above their mass goals at preliminary design.", fix: "Budget ~1 t per 10 kW tower now (ESTIMATE); fly the first towers and measure before buying the rest."}
  - {sev: High, title: "Dust thrown up by landers can sandblast and coat the arrays.", fix: "Keep towers 1 km+ from landing pads (M05); vertical blankets shed falling dust; electrodynamic dust shields."}
  - {sev: Medium, title: "Using only 10 kW towers means many towers, landings and ridge sites for a large solar fleet (DD-004).", fix: "Size the fleet from the Phase 1 load budget; carry several towers per medium lander; revisit VSAT-XL if it reaches flight-like testing."}
  - {sev: Medium, title: "Mechanisms may jam in deep cold when retracting for a move.", fix: "Thermal-vacuum cycle every mechanism at worst cold; carry spare motors; design so a stuck tower still makes power where it stands."}
  - {sev: Medium, title: "No flight demonstration of a vertical lunar array is funded yet.", fix: "Push for the flight demo NASA's project has proposed for 2028–2029, or fly the first Open Moon 10 kW tower as that demo."}
sources:
  - {title: "NASA RELEASE 22-090: Vertical Solar Array Technology awards", url: "https://www.nasa.gov/?p=142765", date: "Aug 2022"}
  - {title: "NASA: From Houston to the Moon, Johnson's thermal vacuum chamber tests lunar solar technology", url: "https://www.nasa.gov/centers-and-facilities/johnson/from-houston-to-the-moon-johnsons-thermal-vacuum-chamber-tests-lunar-solar-technology", date: "2024"}
  - {title: "NASA GCD: Vertical Solar Array Technology project annual review", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
  - {title: "Belbin, Mills & Chan, NASA LaRC: Government Reference Design of the VSAT Demonstrator", url: "https://ntrs.nasa.gov/api/citations/20240004914/downloads/VSAT%20Mechanisms%20Abstract%2020240418.pdf", date: "Apr 2024"}
  - {title: "Astrobotic: awarded lunar power study with VSAT-XL", url: "https://www.astrobotic.com/astrobotic-awarded-lunar-power-study-with-vsat-xl/", date: "Aug 2024"}
  - {title: "Astrobotic: developing XL solar array tech for lunar power infrastructure", url: "https://www.astrobotic.com/astrobotic-developing-xl-solar-array-tech-for-lunar-power-infrastructure/", date: "Jul 2025"}
  - {title: "Contract record 80NSSC25C0032: Astrobotic VSAT-XL SBIR Phase II", url: "https://app.govly.com/public/awards/CONT_AWD_80NSSC25C0032_8000_-NONE-_-NONE--aaa6914c18a199d84114b1235a5d51c3", date: "Jun 2025"}
  - {title: "Redwire: second pair of iROSA solar arrays delivered", url: "https://rdw.com/newsroom/redwire-successfully-delivers-second-pair-of-irosa-solar-arrays-to-augment-international-space-station-power-supply", date: "Jun 2022"}
  - {title: "SatNews: Astrobotic's LunaGrid VSAT enters thermal vacuum testing (press)", url: "https://satnews.com/2024/07/20/astrobotics-lunagrids-vertical-solar-array-technology-vsat-enters-tvac/", date: "Jul 2024"}
  - {title: "Gläser et al. 2014, Icarus: Illumination at the lunar south pole", url: "https://ui.adsabs.harvard.edu/abs/2014Icar..243...78G", date: "2014"}
  - {title: "Wikipedia: Peak of eternal light", url: "https://en.wikipedia.org/wiki/Peak_of_eternal_light", date: "2026"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Wikipedia: Solar constant", url: "https://en.wikipedia.org/wiki/Solar_constant", date: "2026"}
  - {title: "Button, NASA TM-104510: Development and testing of a source subsystem for the PMAD DC test bed (sequential shunt unit)", url: "https://ntrs.nasa.gov/api/citations/19910016888/downloads/19910016888.pdf", date: "Aug 1991"}
  - {title: "Wikipedia: Electrical system of the International Space Station", url: "https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station", date: "2026"}
  - {title: "Thomas et al., NASA GRC: A Modular AC to DC Interface Converter (UMIC) to Enable Lunar Surface Power Transmission", url: "https://ntrs.nasa.gov/citations/20230013309", date: "Sep 2023"}
  - {title: "Thomas, Granger, Csank & Gardner, NASA GRC: Establishing a Lunar Surface Power Grid", url: "https://ntrs.nasa.gov/api/citations/20220011587/downloads/APS4DS_Establishing_Lunar_Grid_V3.pdf", date: "Aug 2022"}
---

## What it does

{% include decision-note.html id="DD-004" extra="The plan first used two 10 kW VSATs and two 50 kW VSAT-XL towers. It now uses 10 kW VSATs only, with the number set by the Phase 1 load budget." %}

At the south pole the Sun skims the horizon, so hills and crater rims cast very long shadows. A tall tower lifts its arrays out of those shadows and catches more hours of sun<sup class="r">[1](#s1)</sup>. On the Shackleton connecting ridge, the best point is lit 92% of the time at 2 m height and 96% at 10 m<sup class="r">[10](#s10)</sup>. Each tower turns that sunlight into 10 kW and sends it to the power management controller (PMC), which routes it to the grid or to storage (design changes DD-003 and DD-008).

**Curtailment and disconnect (plan design, DD-008).** When demand is met and storage is full, the PMC tells each tower to reduce or cut its output. The tower's array regulator does this by shunting array strings, and a disconnect contactor can isolate the whole tower. This is ISS heritage: the station's sequential shunt unit shunts and unshunts array strings to hold the ~160 V DC primary bus<sup class="r">[14](#s14)</sup><sup class="r">[15](#s15)</sup>. The towers can also be lowered and moved<sup class="r">[1](#s1)</sup>.

**Conversion at the tower, and 10 km at most (design changes DD-013 and DD-014).** Solar cells make DC. VSAT's array voltage is not published; for comparison, the ISS arrays run a ~160 V DC bus<sup class="r">[14](#s14)</sup><sup class="r">[15](#s15)</sup>. Each tower turns that DC into 3 kV AC on the spot (plan design):
1. **Array regulator and shunt.** Holds the DC bus and curtails or disconnects on PMC command (DD-008).
2. **UMIC-class inverter.** Parallel 1 kW modules turn DC into under 100 V AC<sup class="r">[16](#s16)</sup>.
3. **1 kHz step-up transformer.** Raises it to 3 kV, 3-phase, 1 kHz, the grid standard (DD-001). The transformer has no switches, so only low-voltage switches are needed. NASA limits a DC grid to 1.2–1.5 kV for lack of radiation-hard high-voltage switches<sup class="r">[17](#s17)</sup>.

Astrobotic's VSAT team already proposed high-voltage AC transmission using NASA Glenn's UMIC<sup class="r">[3](#s3)</sup>. Every tower must sit within **10 km of cable run** of the PMC.

{% include decision-note.html id="DD-013" extra="Each tower had a 'line interface converter' with no set distance. Now the tower converts to 3 kV AC itself and stands within 10 km of cable run of the PMC." %}

## How it works

- **Mast.** NASA's reference design needs at least 10 m from the ground to the bottom of the arrays. It uses 36 m² of array and is about 16 m tall when deployed, built from six telescoping segments of about 3 m each<sup class="r">[4](#s4)</sup>. The three industry prototypes use different masts<sup class="r">[3](#s3)</sup>:
  - Lockheed Martin: a rolled lenticular boom.
  - Honeybee Robotics: a helical metal band.
  - Astrobotic: a ROSA-based mast on a self-propelled cart.
- **Blankets.** Redwire's ROSA roll-out arrays have flown on the ISS since 2017. Each iROSA wing gives more than 28 kW from 30.7%-efficient cells<sup class="r">[8](#s8)</sup>. Astrobotic's towers use ROSA<sup class="r">[3](#s3)</sup><sup class="r">[5](#s5)</sup>.
- **Tracking.** A gimbal makes the mast plumb on slopes of up to 15° and turns the arrays toward the Sun. A slip ring lets it rotate continuously<sup class="r">[4](#s4)</sup>.
- **Not used: VSAT-XL.** Astrobotic's 50 kW, 34 m tower<sup class="r">[5](#s5)</sup> is still a ground deployment prototype under a NASA SBIR contract to June 2027<sup class="r">[7](#s7)</sup>. The plan keeps it as an alternative only (DD-004).
- **Dust and night.** Some designs add NASA's electrodynamic dust shield<sup class="r">[3](#s3)</sup>. The towers must survive 96 hours of darkness and last up to ten years<sup class="r">[2](#s2)</sup>.

## Sizing

- **10 kW tower (ESTIMATE).** Sunlight carries 1,361 W/m²<sup class="r">[13](#s13)</sup>. 36 m² × 1,361 W/m² × 0.307 ≈ 15 kW at the cells. A combined factor of about 0.67, for cell packing, heat, pointing and wiring losses, gives 10 kW.
- **Fleet (plan design, DD-004).** The number of towers will be set by the Phase 1 load budget, which is not done yet. Until then the plan costs a provisional fleet:

| Item | Number | Peak power | Mass (ESTIMATE) |
|---|---|---|---|
| 10 kW tower | 10 (provisional) | 100 kW | ~10 t |

- **Why several ridges.** Two points about 8 km apart on a Shackleton ridge are lit a combined ~94% of a lunar year<sup class="r">[11](#s11)</sup>. Shadows of up to about 100 hours remain<sup class="r">[12](#s12)</sup>, so fission and storage still carry the night.
- **Spacing (DD-014).** DD-013's 3 km limit kept such points from sharing one PMC. With up to 10 km of cable per run, points up to 20 km apart can share one PMC, at 10–15% loss on the longest runs. M00 uses this for the de Gerlache rim (site 5 with the crater's east rim, about 20 km apart).

## Testing and qualification

1. **Ground prototypes.** Honeybee Robotics and Astrobotic tested their prototypes in JSC's Chamber A in summer 2024; the chamber reaches 20 K<sup class="r">[2](#s2)</sup>. Astrobotic's tower was tested for stability, gimbal action and sun tracking on regolith simulant in NASA Glenn's SLOPE facility<sup class="r">[9](#s9)</sup>.
2. **Life cycling.** Deploy and retract each tower many times in cold vacuum. Run the gimbal for a 10-year equivalent number of turns.
3. **Dust and slope.** Run full-height deployments on a 15° simulant slope, and blast samples with dust from simulated landings.
4. **Flight demo.** NASA's VSAT project has argued for a flight demonstration around 2028–2029<sup class="r">[3](#s3)</sup>. The first Open Moon 10 kW tower could fill that role.
5. **On the Moon.** Measure power against predicted illumination for one full year before relying on the tower for essential loads.

## Open questions

- What is the real flight mass of a 10 kW tower?
- Which ridge points give the least overlap in shadow time for the actual landing site, using only points within 10 km of cable run of the PMC (DD-013, DD-014)?
- What DC voltage does a VSAT array deliver to its regulator and inverter? It is not published.
- How many towers does the Phase 1 load budget call for, and on which ridge points?
- How fast do cells degrade from dust, radiation and thermal cycling over 10 years at the pole?
- Each tower sends its power over a 3 kV AC, 1 kHz line of no more than 10 km (design changes DD-001, DD-013 and DD-014) to the PMC, which routes it to the grid or to storage (design changes DD-003 and DD-008). Could Astrobotic's proposed high-voltage AC output<sup class="r">[3](#s3)</sup> serve as the tower's inverter and transformer?
