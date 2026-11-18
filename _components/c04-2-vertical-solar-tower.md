---
id_code: "C04.2"
milestone: M04
order: 2
title: Vertical solar array towers
summary: "Tall masts that lift sun-tracking solar blankets above the shadows of polar terrain. Two 10 kW towers and two 50 kW towers give the base its daytime power."
trl: 5
spec:
  - {k: "Power", v: "10 kW (VSAT) and 50 kW (VSAT-XL) per tower"}
  - {k: "Height", v: "≥10 m to bottom of arrays, ~16 m total (10 kW); 34 m (XL)"}
  - {k: "Array area", v: "36 m² (10 kW); ~180 m² (XL, ESTIMATE)"}
  - {k: "Cells", v: "Triple-junction, ~30% efficient"}
  - {k: "Mass", v: "~1 t per 10 kW tower; ~3 t per XL tower (ESTIMATE)"}
  - {k: "Slope", v: "Up to 15° at set-down, self-levelling"}
  - {k: "Life", v: "10 years at the south pole"}
  - {k: "Night survival", v: "≥96 h in darkness"}
  - {k: "Quantity", v: "2 × 10 kW + 2 × 50 kW on 2–3 ridge points"}
  - {k: "Delivery", v: "Small landers (10 kW); medium lander such as Griffin (XL)"}
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
    parts: ["Tripod or sled base with levelling legs", "Launch locks", "Offload interface (self-propelled or towed cart)", "Ballast or ground anchors", "Cable connector for the source line to the BMS"]
    tech: "VSAT prototype bases; Astrobotic VOLT rover base"
    trl: 5
  - name: Power electronics and night survival
    desc: "Conditions array power for the line to the BMS hub, follows BMS commands to curtail when storage is full, and keeps the tower alive in the dark."
    parts: ["Maximum-power-point converters", "Line interface converter (UMIC class) to the BMS source line", "Curtailment control on BMS command", "Survival battery", "Heaters and thermostats", "Avionics and radio"]
    tech: "NASA GRC UMIC; VSAT prototype avionics"
    trl: 4
  - name: Dust protection
    desc: "Limits dust build-up on the cells, mechanisms and radiators."
    parts: ["Electrodynamic dust shield on cells", "Mechanism seals", "Radiator coatings", "MLI enclosure for electronics"]
    tech: "NASA KSC Electrodynamic Dust Shield"
    trl: 5
risks:
  - {sev: High, title: "Even at 10 m, the best single point is in shadow 4–8% of the time.", fix: "Spread towers over two or three ridge points that are shadowed at different times; back them up with fission (C04.1) and storage (C04.3)."}
  - {sev: High, title: "Tall masts can buckle or tip on slopes or soft regolith.", fix: "Use active plumbness control and wide levelling legs; test full-height towers on regolith simulant slopes before flight."}
  - {sev: High, title: "All prototype designs were above their mass goals at preliminary design.", fix: "Budget ~1 t per 10 kW tower now (ESTIMATE); fly the 10 kW towers first and learn before buying the XL."}
  - {sev: High, title: "Dust thrown up by landers can sandblast and coat the arrays.", fix: "Keep towers 1 km+ from landing pads (M05); vertical blankets shed falling dust; electrodynamic dust shields."}
  - {sev: Medium, title: "VSAT-XL is still a ground prototype of the deployment system only.", fix: "Treat the 50 kW towers as step 3 of the build; keep an option to fly four more 10 kW towers instead."}
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
---

## What it does

At the south pole the Sun skims the horizon, so hills and crater rims cast very long shadows. A tall tower lifts its arrays out of those shadows and catches more hours of sun<sup class="r">[1](#s1)</sup>. On the Shackleton connecting ridge, the best point is lit 92% of the time at 2 m height and 96% at 10 m<sup class="r">[10](#s10)</sup>. Each tower turns that sunlight into 10 or 50 kW for the grid. The towers can also be lowered and moved<sup class="r">[1](#s1)</sup>.

## How it works

- **Mast.** NASA's reference design needs at least 10 m from the ground to the bottom of the arrays. It uses 36 m² of array and is about 16 m tall when deployed, built from six telescoping segments of about 3 m each<sup class="r">[4](#s4)</sup>. The three industry prototypes use different masts<sup class="r">[3](#s3)</sup>:
  - Lockheed Martin: a rolled lenticular boom.
  - Honeybee Robotics: a helical metal band.
  - Astrobotic: a ROSA-based mast on a self-propelled cart.
- **Blankets.** Redwire's ROSA roll-out arrays have flown on the ISS since 2017. Each iROSA wing gives more than 28 kW from 30.7%-efficient cells<sup class="r">[8](#s8)</sup>. Astrobotic's towers use ROSA<sup class="r">[3](#s3)</sup><sup class="r">[5](#s5)</sup>.
- **Tracking.** A gimbal makes the mast plumb on slopes of up to 15° and turns the arrays toward the Sun. A slip ring lets it rotate continuously<sup class="r">[4](#s4)</sup>.
- **VSAT-XL.** Astrobotic's 50 kW tower is 34 m tall and 12.5 m wide<sup class="r">[5](#s5)</sup>. It tracks the Sun, levels itself, and is designed to sit on top of the Griffin lander<sup class="r">[6](#s6)</sup>. A NASA SBIR Phase II contract runs from June 2025 to June 2027<sup class="r">[7](#s7)</sup>.
- **Dust and night.** Some designs add NASA's electrodynamic dust shield<sup class="r">[3](#s3)</sup>. The towers must survive 96 hours of darkness and last up to ten years<sup class="r">[2](#s2)</sup>.

## Sizing

- **10 kW tower (ESTIMATE).** Sunlight carries 1,361 W/m²<sup class="r">[13](#s13)</sup>. 36 m² × 1,361 W/m² × 0.307 ≈ 15 kW at the cells. A combined factor of about 0.67, for cell packing, heat, pointing and wiring losses, gives 10 kW.
- **50 kW tower (ESTIMATE).** 50 kW ÷ (1,361 × 0.307 × 0.67) ≈ 180 m² of array.
- **Fleet (plan design).**

| Item | Number | Peak power | Mass (ESTIMATE) |
|---|---|---|---|
| 10 kW tower | 2 | 20 kW | ~2 t |
| 50 kW XL tower | 2 | 100 kW | ~6 t |
| **Total** | **4** | **120 kW** | **~8 t** |

- **Why several ridges.** Two points about 8 km apart on a Shackleton ridge are lit a combined ~94% of a lunar year<sup class="r">[11](#s11)</sup>. Shadows of up to about 100 hours remain<sup class="r">[12](#s12)</sup>, so fission and storage still carry the night.

## Testing and qualification

1. **Ground prototypes.** Honeybee Robotics and Astrobotic tested their prototypes in JSC's Chamber A in summer 2024; the chamber reaches 20 K<sup class="r">[2](#s2)</sup>. Astrobotic's tower was tested for stability, gimbal action and sun tracking on regolith simulant in NASA Glenn's SLOPE facility<sup class="r">[9](#s9)</sup>.
2. **Life cycling.** Deploy and retract each tower many times in cold vacuum. Run the gimbal for a 10-year equivalent number of turns.
3. **Dust and slope.** Run full-height deployments on a 15° simulant slope, and blast samples with dust from simulated landings.
4. **Flight demo.** NASA's VSAT project has argued for a flight demonstration around 2028–2029<sup class="r">[3](#s3)</sup>. The first Open Moon 10 kW tower could fill that role.
5. **On the Moon.** Measure power against predicted illumination for one full year before relying on the tower for essential loads.

## Open questions

- What is the real flight mass of a 10 kW tower and of the XL?
- Which ridge points give the least overlap in shadow time for the actual landing site?
- Should the XL be a fixed tower (Astrobotic 2025) or have a mobile version (Astrobotic 2024)<sup class="r">[5](#s5)</sup><sup class="r">[6](#s6)</sup>?
- How fast do cells degrade from dust, radiation and thermal cycling over 10 years at the pole?
- Each tower sends its power over a 3 kV AC, 1 kHz line (design change DD-001) to the BMS hub, which routes it to the grid or to storage (design change DD-003). Could Astrobotic's proposed high-voltage AC output<sup class="r">[3](#s3)</sup> feed that line more directly?
