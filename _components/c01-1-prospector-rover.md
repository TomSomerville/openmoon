---
id_code: "C01.1"
milestone: M01
order: 1
title: Prospector rover
summary: "A small solar-powered rover that drives into permanently shadowed craters, drills to 1 m and measures the ice it finds. Two are built, and each flies on a different lander."
trl: 6
spec:
  - {k: "Role", v: "Map hydrogen while driving; drill and assay ice to 1 m depth"}
  - {k: "Mass", v: "~260 kg incl. 30% margin (ESTIMATE; VIPER was ~475 kg)"}
  - {k: "Instruments", v: "Neutron spectrometer, 1 m drill, mass spectrometer, stereo cameras and lights"}
  - {k: "Speed", v: "~10 cm/s prospecting, ~20 cm/s top (VIPER figures)"}
  - {k: "PSR sortie", v: "~6 h per trip into shadow (ESTIMATE, VIPER planning case)"}
  - {k: "Dark survival", v: "96 h target (VIPER requirement)"}
  - {k: "Battery", v: "~4 kWh Li-ion, ~25 kg (ESTIMATE)"}
  - {k: "Earth link", v: "X-band direct-to-Earth plus LunaNet S-band relay; store-and-forward in shadow"}
  - {k: "Quantity", v: "2 flight units + 1 ground test unit"}
  - {k: "Delivery class", v: "Small lander with 300+ kg capacity (e.g. Griffin, 625 kg) or Blue Moon Mk1"}
subcomponents:
  - name: Chassis and mobility
    desc: "A four-wheel, independently steered chassis that can crab, turn on the spot and climb out of soft crater floors."
    parts: ["Aluminium frame and deck", "Four wheel modules with drive and steer motors", "Crab-walking steering for traction in soft soil", "Instrument bay under the belly", "Lander release and egress ramp interface"]
    tech: "VIPER four-module independent steering"
    trl: 6
  - name: Power and thermal
    desc: "Solar panels charge a battery in sunlight; a warm electronics box, insulation and radioisotope heaters keep the rover alive in the cold."
    parts: ["Vertical side-mounted solar panels (low Sun angle at the pole)", "~4 kWh Li-ion battery", "Warm electronics box with multi-layer insulation", "Radioisotope heater units (about 1 W each)", "Switchable radiator for sunlit driving"]
    tech: "VIPER power and thermal design; flight-proven RHUs"
    trl: 6
  - name: Drill
    desc: "A 1 m rotary-percussive drill that brings up cuttings in 10 cm bites and logs temperature and strength with depth."
    parts: ["Auger and bit with temperature sensor", "Rotary and percussive actuators", "Deployment stage with depth control", "Downhole heater and second temperature sensor", "Cuttings delivery to the mass spectrometer's view"]
    tech: "Honeybee TRIDENT (flew on PRIME-1, IM-2)"
    trl: 7
  - name: Mass spectrometer
    desc: "A quadrupole mass spectrometer that identifies the gases released from drill cuttings and from the soil under the rover."
    parts: ["Ion source and quadrupole analyser", "Faraday cup and electron-multiplier detectors", "Inlet facing the drill cuttings", "Control electronics"]
    tech: "NASA KSC / INFICON MSolo (flew on PRIME-1, IM-2)"
    trl: 7
  - name: Neutron spectrometer
    desc: "Counts neutrons leaking from the soil to map hydrogen in the top metre while driving, so the drill goes where hydrogen is highest."
    parts: ["Thermal neutron detector", "Epithermal neutron detector", "High-voltage supply and front-end electronics", "Data processing module"]
    tech: "VIPER NSS (NASA Ames, Lockheed Martin)"
    trl: 6
  - name: Communications
    desc: "Three radios: direct-to-Earth when Earth is up, LunaNet relay when it is not, and a local link to a rim mast or lander."
    parts: ["X-band high-gain antenna on the mast", "X-band omni antennas", "LunaNet S-band proximity radio", "Local WLAN / LTE device module", "Onboard data store for store-and-forward"]
    tech: "VIPER X-band DTE; LunaNet v5; Nokia LTE device module"
    trl: 6
  - name: Navigation and imaging
    desc: "Stereo cameras and LED lights let the rover see and plan short drives in total darkness."
    parts: ["Gimbaled stereo navigation cameras on a ~2 m mast", "Fixed rear stereo cameras", "Hazard cameras near each wheel", "LED headlights", "Sun sensor and inertial unit"]
    tech: "VIPER navigation camera and lighting suite"
    trl: 6
risks:
  - {sev: Critical, title: "The lander tips over or crashes and the rover never drives off (as on IM-1, IM-2 and ispace M2)", fix: "Fly the two rovers on two different lander providers. Design the egress so the rover can still drive off a lander that is leaning by up to ~15° (design target)."}
  - {sev: High, title: "Cold of about 25 K in shadowed craters drains the battery and can freeze mechanisms", fix: "Keep sorties short (~6 h), park in sunlight to recharge, use radioisotope heaters and a well-insulated warm box, and qualify the drill and wheels in a cryo chamber."}
  - {sev: High, title: "Radioisotope heaters need nuclear launch authorization, which adds paperwork and schedule", fix: "Start the NSPM-20 launch authorization process at the start of the project. Keep an electric-heater-only design as a fallback, accepting shorter sorties."}
  - {sev: High, title: "Ice is patchy, so a few drill holes may miss it or overstate it", fix: "Use the neutron spectrometer to pick drill sites. Drill a grid of several holes in each PSR, not one deep hole."}
  - {sev: Medium, title: "No line of sight to Earth or a relay from inside a crater", fix: "Store data on board and send it when back in view. Use the rim relay mast (C03.2) once it is installed."}
  - {sev: Medium, title: "Lander exhaust and the rover's own outgassing contaminate the mass spectrometer data, as MSolo saw on IM-2", fix: "Drive well away from the lander before sampling. Record a lander exhaust baseline and a rover outgassing baseline first."}
  - {sev: Medium, title: "The rover gets stuck in soft, fluffy crater-floor soil", fix: "Use crab-walking steering, which VIPER tested on slopes. Test in lunar soil simulant at cryogenic temperature."}
sources:
  - {title: "NASA NTRS: VIPER Mission Overview (Andrews)", url: "https://ntrs.nasa.gov/api/citations/20205000864/downloads/2020-04-14%2C%20VIPER%20Mission%20Overview%20(Andrews).pdf", date: "Apr 2020"}
  - {title: "NASA Science: VIPER rover and instruments", url: "https://science.nasa.gov/mission/viper/rover-and-instruments", date: "accessed Nov 2026"}
  - {title: "NASA NTRS: The VIPER mission, a resource-mapping mission (Ennico-Smith et al.)", url: "https://ntrs.nasa.gov/api/citations/20220005327/downloads/VIPER-SRR-June2022-Ennico.pdf", date: "Jun 2022"}
  - {title: "NASA: Lunar drill technology passes tests on the Moon (PRIME-1)", url: "https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/", date: "May 2025"}
  - {title: "NASA NTRS: MSolo PRIME-1 overview and results", url: "https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf", date: "2026"}
  - {title: "NASA: Radioisotope Heater Units fact sheet", url: "https://science.nasa.gov/resource/radioisotope-heater-units-fact-sheet/", date: ""}
  - {title: "UCLA Diviner: lunar temperatures", url: "https://www.diviner.ucla.edu/science", date: ""}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Astrobotic Lunar Landers Payload User's Guide", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", date: "Mar 2025"}
  - {title: "NASA: LunaNet Interoperability Specification v5", url: "https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf", date: "Jan 2025"}
  - {title: "NSPM-20: Launch of spacecraft containing space nuclear systems", url: "https://www.govinfo.gov/content/pkg/DCPD-201900558/html/DCPD-201900558.htm", date: "Aug 2019"}
  - {title: "Firefly: Blue Ghost lunar lander", url: "https://fireflyspace.com/blue-ghost", date: "accessed Nov 2026"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
---

## What it does

The prospector rover answers one question for M01: **how much ice is in the ground, and how deep is it?** It drives across a crater floor and maps hydrogen as it goes. Where the hydrogen signal is strongest, it stops, drills to 1 m and identifies the gases that come out. It is a smaller, cheaper version of NASA's VIPER, and it carries instruments that have already flown.

## How it works

- **Chassis and mobility.** VIPER used four wheel modules, each steered independently. It drove at about 20 cm/s, or 10 cm/s while prospecting<sup class="r">[1](#s1)</sup>, and could climb slopes of up to 15°<sup class="r">[2](#s2)</sup>. VIPER's team tested crab-walking on a 15° upslope with a 45° cross slope<sup class="r">[1](#s1)</sup>. We copy that layout on a smaller frame.
- **Power and thermal.** The polar Sun is always low, so the solar panels stand vertically on the rover's sides. Crater floors can fall to about 25 K<sup class="r">[7](#s7)</sup>. A radioisotope heater unit gives about 1 W of heat with no power draw<sup class="r">[6](#s6)</sup>. NSPM-20 covers RHUs, so they need launch authorization<sup class="r">[12](#s12)</sup>. VIPER was designed to survive 96 h of darkness and to work for about 6 h inside a PSR<sup class="r">[1](#s1)</sup>. We use the same targets.
- **Drill.** TRIDENT is a 1 m rotary-percussive drill. It lifts cuttings in 10 cm bites and has temperature sensors at the bit and 20 cm above it<sup class="r">[3](#s3)</sup>. The VIPER version weighs 18 kg, including launch locks. It draws under 5 W idle and about 20 W while augering, with peaks of 175 W, and it reaches 100 cm in under an hour<sup class="r">[1](#s1)</sup>. On IM-2 all its actuators, heaters and sensors worked, but the lander lay on its side<sup class="r">[4](#s4)</sup>.
- **Mass spectrometer.** MSolo is a quadrupole instrument covering 2–100 amu. It weighs 6 kg and draws about 35 W while scanning<sup class="r">[1](#s1)</sup>. It worked on IM-2, but the gases it saw came from the lander or from Earth<sup class="r">[5](#s5)</sup>.
- **Neutron spectrometer.** VIPER's NSS weighs 1.9 kg and draws 1.6 W. It detects 0.5 wt% water-equivalent hydrogen in the top metre while driving at 10 cm/s<sup class="r">[1](#s1)</sup>.
- **Communications.** VIPER's X-band link sent 256 kbps to Earth through its high-gain antenna (as high as 4 Mbps) and received 2 kbps on the omni antenna<sup class="r">[1](#s1)</sup>. We add a LunaNet S-band radio so the rover can use relays<sup class="r">[11](#s11)</sup>, plus a local wireless link. Astrobotic landers already offer 802.11n WLAN to deployed payloads<sup class="r">[9](#s9)</sup>. Nokia's LTE device module reached the Moon on IM-2. It was drawing power normally after landing, but it later got too cold to connect<sup class="r">[10](#s10)</sup>.
- **Navigation.** VIPER carried gimbaled stereo cameras on a 2 m mast, fixed rear stereo cameras, hazard cameras by each wheel, and LED lights<sup class="r">[3](#s3)</sup>. We keep the same layout.

## Sizing

Mass budget (ESTIMATE, except where cited):

| Item | Mass (kg) | Basis |
|---|---|---|
| Drill (TRIDENT class) | 18 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Mass spectrometer | 6 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Neutron spectrometer | 1.9 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Battery, 4 kWh | 25 | 4,000 Wh ÷ 160 Wh/kg<sup class="r">[8](#s8)</sup> |
| Cameras, lights, mast | 10 | ESTIMATE |
| Avionics and radios | 20 | ESTIMATE |
| Solar panels | 15 | ESTIMATE |
| Thermal (box, insulation, RHUs, radiator) | 15 | ESTIMATE |
| Chassis, wheels, motors | 90 | ESTIMATE |
| **Subtotal** | **~201** | |
| **With 30% margin** | **~260** | 201 × 1.3 |

That is about half of VIPER's ~475 kg<sup class="r">[1](#s1)</sup>. It is too heavy for Blue Ghost (up to 240 kg<sup class="r">[13](#s13)</sup>) but fits Griffin (625 kg<sup class="r">[9](#s9)</sup>).

Energy for one sortie into a PSR (ESTIMATE): driving 100 W + avionics and radios 60 W + MSolo 35 W + lights 30 W + heaters 50 W + drill 20 W ≈ 300 W. Over 6 h that is 300 × 6 = 1.8 kWh, so a 4 kWh battery gives more than 2× margin. For dark survival, 4,000 Wh ÷ 96 h ≈ 42 W on average for heaters and the computer. About 10 RHUs (≈ 10 W<sup class="r">[6](#s6)</sup>) cover a quarter of that.

## Testing and qualification

1. **Instruments.** Reuse flight designs (TRIDENT, MSolo, NSS) with only small changes, and re-run their acceptance tests.
2. **Engineering model.** Build a full-size rover and drive it in soil simulant on 15° slopes, as VIPER did<sup class="r">[1](#s1)</sup>.
3. **Cryo and vacuum.** VIPER drilled 1 m into soil simulant doped with 5% water and chilled to −100 °C in a thermal-vacuum chamber, and tested its wheels and steering in thermal vacuum<sup class="r">[1](#s1)</sup>. We repeat this, colder, closer to PSR conditions. Run a full 6 h sortie and a 96 h dark-survival case on the whole rover in thermal vacuum.
4. **Dark field test.** Drive in the dark using only the rover's lights and cameras, as VIPER did at NASA Ames<sup class="r">[1](#s1)</sup>.
5. **Flight units.** Run vibration, shock and EMI tests to the environments in each lander's user guide.
6. **On the Moon.** First drive away from the lander and drill a "dry" hole in sunlight to record the contamination baseline. Then make short PSR sorties, longer each time.

## Open questions

- Can the rover drive off a lander that is leaning by 10–15°? What ramp design copes with that?
- How many RHUs can we get, and on what schedule, under NSPM-20 and the available Pu-238 supply?
- Is a 6 h sortie enough to drill several holes, or do we need a bigger battery?
- ShadowCam found that surface ice is patchy<sup class="r">[14](#s14)</sup>. How many drill holes per PSR give a useful ice estimate?
- Should one rover carry a near-infrared spectrometer (NIRVSS class) in place of some drill time?
