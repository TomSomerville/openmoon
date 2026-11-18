---
id_code: "C01.1"
milestone: M01
order: 1
title: Prospector rover
summary: "A small solar-powered rover that drives into permanently shadowed craters. It scoops loose soil, drills ice-cemented ground into cuttings to 1 m, and bakes both in a sealed chamber to measure how much water actually comes out. Two are built, and each flies on a different lander."
trl: 4
spec:
  - {k: "Role", v: "Map hydrogen while driving; scoop and drill icy soil, bake it and measure the water released, down to 1 m"}
  - {k: "Heritage", v: "NASA Resource Prospector (drill brushes cuttings into a sealed oven) and NASA Curiosity (scoop and drill feed ovens on one rover)"}
  - {k: "Mass", v: "~320 kg incl. 30% margin (ESTIMATE; VIPER was ~475 kg)"}
  - {k: "Instruments", v: "Neutron spectrometer, 1 m drill, scoop arm with rasp, bake chamber with cold trap, mass spectrometer, stereo cameras and lights"}
  - {k: "Bake chamber", v: "~250 cm³ sealed, reusable crucible, ~0.4 kg of soil per batch, heated in steps to 450 °C (plan design)"}
  - {k: "Energy per batch", v: "~150 Wh (ESTIMATE, see Sizing)"}
  - {k: "Speed", v: "~10 cm/s prospecting, ~20 cm/s top (VIPER figures)"}
  - {k: "PSR sortie", v: "~6 h per trip into shadow (ESTIMATE, VIPER planning case)"}
  - {k: "Dark survival", v: "96 h target (VIPER requirement)"}
  - {k: "Battery", v: "~4 kWh Li-ion, ~25 kg (ESTIMATE)"}
  - {k: "Earth link", v: "X-band direct-to-Earth plus LunaNet S-band relay; store-and-forward in shadow"}
  - {k: "Quantity", v: "2 flight units + 1 ground test unit"}
  - {k: "Delivery class", v: "Small lander with 350+ kg capacity (e.g. Griffin, 625 kg) or Blue Moon Mk1"}
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
    desc: "A 1 m rotary-percussive drill that breaks hard, ice-cemented ground into cuttings. It lifts them in 10 cm bites and brushes each bite straight into the bake-chamber funnel, so every bite gives water content at its own depth. It also logs temperature and drilling strength with depth."
    parts: ["Auger and tungsten carbide bit with temperature sensor", "Rotary and percussive actuators", "Deployment stage with depth control", "Downhole heater and second temperature sensor", "Brush and funnel that drop each bite into the bake chamber (Resource Prospector layout)"]
    tech: "Honeybee TRIDENT (flew on PRIME-1, IM-2); Resource Prospector drill-to-oven delivery"
    trl: 6
  - name: Scoop arm
    desc: "A small robotic arm with a bladed scoop picks up loose soil and small debris from the surface and the floor of short trenches. A powered rasp under the scoop chips hard icy ground into fragments, as on Phoenix. A screen keeps out stones too big for the chamber."
    parts: ["4-degree-of-freedom arm, about 1.5 m reach (plan design; Phoenix arm was 2.4 m)", "Scoop with front blade and hardened secondary blade", "Motorised rasp in a rear chamber of the scoop, also used to vibrate samples loose", "Vibrated inlet screen, about 10 mm openings (plan design)", "Arm camera and scoop temperature sensor"]
    tech: "Phoenix Robotic Arm and Icy Soil Acquisition Device (Mars, 2008); Curiosity scoop and sample handling (Mars, 2012)"
    trl: 6
  - name: Bake chamber
    desc: "A sealed, reusable oven that weighs each batch of scooped soil or drill cuttings, seals it, and heats it in steps to 450 °C. The water and other gases that come off pass a mass spectrometer and freeze in a cold trap, so the water is both identified and measured. The cooked soil is then dumped and the chamber reused."
    parts: ["Crucible of about 250 cm³ with funnel inlet and dump door (plan design)", "Load cell to weigh each batch", "Lid seal and seal actuator", "Heaters and insulation for 150 °C, 350 °C and 450 °C steps (Resource Prospector steps)", "Known-volume gas manifold with pressure and temperature sensors", "Cold trap on a shaded radiator, warmed later to vent", "Valve to the mass spectrometer inlet"]
    tech: "NASA Resource Prospector OVEN (12 cm³, thermal-vacuum and vibration tested); Phoenix TEGA ovens (Mars, 2008)"
    trl: 4
  - name: Mass spectrometer
    desc: "A quadrupole mass spectrometer that identifies the gases released in the bake chamber, and from the soil under the rover while driving."
    parts: ["Ion source and quadrupole analyser", "Faraday cup and electron-multiplier detectors", "Inlet valve from the bake-chamber gas manifold", "Second inlet open to the ground for background readings", "Control electronics"]
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
  - {sev: High, title: "Icy samples lose water before they are sealed in: NASA vacuum tests lost about 30% from 4.5 wt% soil and about 80% from 0.8 wt% soil", fix: "Brush drill bites straight into the chamber and seal at once; keep the scoop, funnel and chamber cold until sealed; log time from ground to seal for every batch; calibrate losses on icy simulant in a cold vacuum chamber."}
  - {sev: High, title: "The bake chamber is about 20 times larger than any tested lunar oven, so it is not yet proven", fix: "Build a full-size chamber early and test it in thermal vacuum with icy simulant, including seal life and dumping, before the rover design is frozen."}
  - {sev: Medium, title: "Icy soil sticks in the scoop or clogs the inlet screen, as on Phoenix", fix: "Vibrate the scoop and screen with the rasp motor, use a coarse screen, keep the scoop cold so ice does not congeal, and pour slowly at an angle (Phoenix's fix)."}
  - {sev: Medium, title: "Dust on the chamber lid seal lets gas leak during heating", fix: "Use a replaceable seal and check each seal with a pressure-hold test before heating; the Resource Prospector prototype carried a store of spare seals."}
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
  - {title: "NASA NTRS: Colaprete et al., Resource Prospector instrumentation for lunar volatiles prospecting, sample acquisition and processing", url: "https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf", date: "Apr 2016"}
  - {title: "NASA NTRS: Kleinhenz et al., Volatiles loss from water bearing regolith simulant at lunar environments", url: "https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf", date: "Apr 2018"}
  - {title: "NASA NTRS: Paz, Environmental testing of the OVEN system for lunar water extraction and prospecting", url: "https://ntrs.nasa.gov/citations/20210013522", date: "2021"}
  - {title: "NASA NTRS: Paz & Oryshchyn, OVEN poster", url: "https://ntrs.nasa.gov/citations/20140017042", date: "Nov 2014"}
  - {title: "Captain (NASA KSC): Instrumentation for lunar volatile analysis (12th EuroHEMS workshop)", url: "https://www.hems-workshop.org/12thWS_EUROHEMS/Presentations/Captain.pdf", date: "2019"}
  - {title: "Bonitz et al.: NASA Mars 2007 Phoenix Lander Robotic Arm and Icy Soil Acquisition Device (JGR 113)", url: "https://www-robotics.jpl.nasa.gov/media/documents/2007JE003030.pdf", date: "Jun 2008"}
  - {title: "Bonitz et al.: The Phoenix Mars Lander Robotic Arm (IEEE Aerospace Conference)", url: "https://www-robotics.jpl.nasa.gov/media/documents/f1695_2.pdf", date: "Dec 2008"}
  - {title: "JPL: NASA's Phoenix lander has an oven full of Martian soil", url: "https://www.jpl.nasa.gov/news/nasas-phoenix-lander-has-an-oven-full-of-martian-soil/", date: "Jun 2008"}
  - {title: "JPL (archived): MSL Science Corner, sampling system", url: "https://webarchive.library.unt.edu/web/20130214054221/http://msl-scicorner.jpl.nasa.gov/samplingsystem", date: "2013"}
  - {title: "NASA Science: Preparing samples on Mars (PIA16691)", url: "https://science.nasa.gov/photojournal/preparing-samples-on-mars", date: ""}
  - {title: "Leshin et al.: Volatile, isotope and organic analysis of Martian fines with the Mars Curiosity rover (Science)", url: "https://mars.nasa.gov/files/msl/Science-2013-Leshin-.pdf", date: "Sep 2013"}
  - {title: "Hayne et al.: Global regolith thermophysical properties of the Moon from Diviner (JGR Planets)", url: "https://arxiv.org/pdf/1711.00977", date: "2017"}
  - {title: "Murphy & Koop: Review of the vapour pressures of ice and supercooled water (QJRMS 131)", url: "https://zenodo.org/records/1236243/files/article.pdf", date: "2005"}
  - {title: "Lunar Sourcebook, Chapter 9: Physical properties of the lunar surface (Carrier, Olhoeft & Mendell)", url: "https://www.lpi.usra.edu/publications/books/lunar_sourcebook/pdf/Chapter09.pdf", date: "1991"}
  - {title: "NASA: Technology Readiness Levels", url: "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels/", date: ""}
---

## What it does

The prospector rover answers one question for M01: **how much water can actually be got out of the ground, and from what depth?** It drives across a crater floor and maps hydrogen as it goes. Where the hydrogen signal is strongest, it stops. It scoops up loose soil and small debris, and drills the hard, ice-cemented ground below into cuttings down to 1 m. Both go into a sealed bake chamber on the rover. The chamber heats them and measures the water that comes off.

Measuring the water that a heated sample really gives up is the same job the M06 ice plant will do at full size, so the rover tests the plant's process as well as mapping the ice. That is why it bakes a much bigger sample than earlier prospecting instruments did (plan design).

## Heritage: the two closest designs

No flown rover does all of this on the Moon. The design combines two NASA rovers:

- **Resource Prospector (Moon, cancelled 2018) is the closest design.** It was a lunar polar rover with a 1 m drill whose cuttings were brushed "directly into a cup/oven"<sup class="r">[15](#s15)</sup>. Its OVEN accepted 12 cc of regolith from the drill, weighed it, sealed it, heated it to 150, 350 and 450 °C, passed the gases to an analyser, then discarded the sample so the crucible could be reused. It weighed about 12.5 kg and drew over 50 W steady<sup class="r">[15](#s15)</sup>. It survived two rounds of random vibration tests, one of them on the RP mobile platform, and worked in thermal vacuum from −50 to 75 °C. It is not part of any current mission<sup class="r">[17](#s17)</sup>.
- **Curiosity (Mars, landed 2012) is the closest that has flown.** A scoop and a drill both feed one processing device on its arm, which sieves the material and splits it into portions<sup class="r">[23](#s23)</sup>. The arm drops portions into ovens that heat most samples to about 1,000 °C<sup class="r">[24](#s24)</sup>. Heating scooped Martian soil released about 2 wt% water<sup class="r">[25](#s25)</sup>. Its samples are milligrams of dry, warm soil, not icy lunar soil.

The scoop itself follows **Phoenix** (Mars, 2008), a lander that dug icy soil. Its 2.4 m, 4-degree-of-freedom arm carried a scoop with a titanium front blade, a tungsten carbide secondary blade and a powered rasp for "indurated icy soils"<sup class="r">[20](#s20)</sup>.

## How it works

- **Chassis and mobility.** VIPER used four wheel modules, each steered independently. It drove at about 20 cm/s, or 10 cm/s while prospecting<sup class="r">[1](#s1)</sup>, and could climb slopes of up to 15°<sup class="r">[2](#s2)</sup>. VIPER's team tested crab-walking on a 15° upslope with a 45° cross slope<sup class="r">[1](#s1)</sup>. We copy that layout on a smaller frame.
- **Power and thermal.** The polar Sun is always low, so the solar panels stand vertically on the rover's sides. Crater floors can fall to about 25 K<sup class="r">[7](#s7)</sup>. A radioisotope heater unit gives about 1 W of heat with no power draw<sup class="r">[6](#s6)</sup>. NSPM-20 covers RHUs, so they need launch authorization<sup class="r">[12](#s12)</sup>. VIPER was designed to survive 96 h of darkness and to work for about 6 h inside a PSR<sup class="r">[1](#s1)</sup>. We use the same targets.
- **Drill: breaking hard ice into cuttings.** TRIDENT is a 1 m rotary-percussive drill. It lifts cuttings in 10 cm bites and has temperature sensors at the bit and 20 cm above it<sup class="r">[3](#s3)</sup>. The VIPER version weighs 18 kg, including launch locks. It draws under 5 W idle and about 20 W while augering, with peaks of 175 W, and it reaches 100 cm in under an hour<sup class="r">[1](#s1)</sup>. On IM-2 all its actuators, heaters and sensors worked, but the lander lay on its side<sup class="r">[4](#s4)</sup>. On VIPER the cuttings fall in a pile on the ground. Here, as on Resource Prospector, the brush sweeps each bite into the bake-chamber funnel instead<sup class="r">[15](#s15)</sup>. Resource Prospector's drill was rated TRL 6<sup class="r">[16](#s16)</sup>.
- **Scoop arm: loose soil and small debris.** The arm scoops loose surface soil and the floor of short trenches. Where the ground is too hard to scoop, the rasp chips it. On Phoenix, the scoop was pressed against the ground, the rasp bit was energised, and a plume of cuttings flew into the scoop's rear chamber. It took about 16 s in icy soil and 6 s in pure ice<sup class="r">[20](#s20)</sup>. On Mars, sixteen rasps in a 4 × 4 grid gave about 2.5 cc of material<sup class="r">[21](#s21)</sup>. Rasping is slow, so the drill is the main tool for hard ground and the rasp is for the surface (plan design). A vibrated screen keeps stones of more than about 10 mm out of the chamber (plan design).
- **Bake chamber: getting the water out.** Each batch is weighed, sealed and heated in Resource Prospector's three steps, 150, 350 and 450 °C<sup class="r">[15](#s15)</sup>. The released gas fills a known volume held warm, and the amount of gas is worked out from its pressure and temperature. That is how Resource Prospector's LAVA instrument quantified it<sup class="r">[19](#s19)</sup>. The mass spectrometer identifies which gases they are. The water vapour then freezes in a cold trap on a shaded radiator, and the chamber is dumped and reused (plan design). The chamber holds about 250 cm³, about 20 times Resource Prospector's 12 cc crucible (plan design). A bigger batch averages out patchy ice and gives grams of water rather than milligrams.
- **Mass spectrometer.** MSolo is a quadrupole instrument covering 2–100 amu. It weighs 6 kg and draws about 35 W while scanning<sup class="r">[1](#s1)</sup>. It worked on IM-2, but the gases it saw came from the lander or from Earth<sup class="r">[5](#s5)</sup>. Here it reads gas from the bake chamber, which is cleaner than sniffing an open cuttings pile.
- **Neutron spectrometer.** VIPER's NSS weighs 1.9 kg and draws 1.6 W. It detects 0.5 wt% water-equivalent hydrogen in the top metre while driving at 10 cm/s<sup class="r">[1](#s1)</sup>.
- **Communications.** VIPER's X-band link sent 256 kbps to Earth through its high-gain antenna (as high as 4 Mbps) and received 2 kbps on the omni antenna<sup class="r">[1](#s1)</sup>. We add a LunaNet S-band radio so the rover can use relays<sup class="r">[11](#s11)</sup>, plus a local wireless link. Astrobotic landers already offer 802.11n WLAN to deployed payloads<sup class="r">[9](#s9)</sup>. Nokia's LTE device module reached the Moon on IM-2. It was drawing power normally after landing, but it later got too cold to connect<sup class="r">[10](#s10)</sup>.
- **Navigation.** VIPER carried gimbaled stereo cameras on a 2 m mast, fixed rear stereo cameras, hazard cameras by each wheel, and LED lights<sup class="r">[3](#s3)</sup>. We keep the same layout.

### A sampling stop

1. Drive to the strongest hydrogen reading, then stop and record a background gas reading.
2. Scoop the surface soil into the chamber, seal it and bake it.
3. Dump the batch. Drill 10 cm and brush the bite into the chamber, seal and bake. Repeat bite by bite to 1 m, or join bites into one batch if they are small.
4. Move a few metres and repeat, to build a grid of holes in each PSR.

## Sizing

Mass budget (ESTIMATE, except where cited):

| Item | Mass (kg) | Basis |
|---|---|---|
| Drill (TRIDENT class) | 18 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Mass spectrometer | 6 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Neutron spectrometer | 1.9 | VIPER figure<sup class="r">[1](#s1)</sup> |
| Scoop arm with rasp and screen | 20 | ESTIMATE |
| Bake chamber, cold trap, valves and gas manifold | 25 | ESTIMATE; Resource Prospector's 12 cc OVEN was ~12.5 kg<sup class="r">[15](#s15)</sup> |
| Battery, 4 kWh | 25 | 4,000 Wh ÷ 160 Wh/kg<sup class="r">[8](#s8)</sup> |
| Cameras, lights, mast | 10 | ESTIMATE |
| Avionics and radios | 20 | ESTIMATE |
| Solar panels | 15 | ESTIMATE |
| Thermal (box, insulation, RHUs, radiator) | 15 | ESTIMATE |
| Chassis, wheels, motors | 90 | ESTIMATE |
| **Subtotal** | **~246** | |
| **With 30% margin** | **~320** | 246 × 1.3 |

That is about two-thirds of VIPER's ~475 kg<sup class="r">[1](#s1)</sup>. It is too heavy for Blue Ghost (up to 240 kg<sup class="r">[13](#s13)</sup>) but fits Griffin (625 kg<sup class="r">[9](#s9)</sup>).

**How much soil and water per batch** (this plan's arithmetic). Lunar soil in the top 30 cm has a bulk density of about 1.53–1.63 g/cm³<sup class="r">[28](#s28)</sup>, so a 250 cm³ chamber holds about 0.4 kg. At 0.5 wt% water that batch holds about 2 g of water. At 5 wt% it holds about 20 g.

**Energy per batch** (ESTIMATE). Regolith specific heat rises from about 0.28 J/(g·K) at 100 K to about 0.91 J/(g·K) at 400 K (from the Diviner team's fit<sup class="r">[26](#s26)</sup>; this plan's arithmetic). Heating 0.4 kg from 100 K to 450 °C (723 K) takes about 200 kJ, or about 56 Wh. The fit is stated as valid to just over 400 K<sup class="r">[26](#s26)</sup>, so the hotter part is extrapolated. Subliming 20 g of ice takes about 16 Wh more, at 51 kJ/mol<sup class="r">[27](#s27)</sup>. Doubling the total for heat leaks gives about 150 Wh a batch. A 150 W heater (plan design) does one batch in about an hour.

Energy for one sortie into a PSR (ESTIMATE): driving 100 W + avionics and radios 60 W + MSolo 35 W + lights 30 W + heaters 50 W + drill 20 W ≈ 300 W. Over 6 h that is 300 × 6 = 1.8 kWh. Two bake batches add about 0.3 kWh, so a sortie uses about 2.1 kWh, and the 4 kWh battery still has nearly 2× margin. A sealed batch keeps its water, so a batch can also be baked after driving back into sunlight, on solar power. For dark survival, 4,000 Wh ÷ 96 h ≈ 42 W on average for heaters and the computer. About 10 RHUs (≈ 10 W<sup class="r">[6](#s6)</sup>) cover a quarter of that.

## Readiness

NASA defines TRL 6 as a fully functional prototype or representative model, and TRL 7 as a demonstration in a space environment<sup class="r">[29](#s29)</sup>. The rover's parts are at different levels:

| Part | TRL | Why |
|---|---|---|
| Drill, mass spectrometer | 6–7 | Flown on IM-2 but never drilled lunar ground<sup class="r">[4](#s4)</sup>; Resource Prospector's drill was TRL 6<sup class="r">[16](#s16)</sup> |
| Mobility, power, neutron spectrometer, comms | 6 | Copied from VIPER designs<sup class="r">[1](#s1)</sup>, which have not yet flown |
| Scoop arm with rasp | 6 | Flew on Mars<sup class="r">[20](#s20)</sup>; not yet tested at lunar PSR cold (plan judgement) |
| Bake chamber | 4 | The 12 cc Resource Prospector OVEN passed vibration and thermal-vacuum tests<sup class="r">[17](#s17)</sup>; a 250 cm³ version has not been built (plan judgement) |

The rover as a whole is rated **TRL 4**, set by its least mature critical part, the bake chamber (plan design). Building the full-size chamber and testing it in thermal vacuum with icy simulant would bring it to about TRL 5–6.

## Testing and qualification

1. **Instruments.** Reuse flight designs (TRIDENT, MSolo, NSS) with only small changes, and re-run their acceptance tests.
2. **Bake chamber first.** Build a full-size chamber early. Test it in thermal vacuum with icy simulant at several known water contents: seal life, weighing, the 150/350/450 °C steps, cold-trap capture and dumping. Measure how much water is lost between the ground and the sealed lid. In Resource Prospector's vacuum tests it took about 5 minutes to brush a sample in and seal it, and samples lost about 30% of their water from 4.5 wt% soil and about 80% from 0.8 wt% soil<sup class="r">[16](#s16)</sup>.
3. **Scoop in icy soil.** Test scooping, rasping and pouring into the screen with cold icy simulant. On Phoenix, icy samples congealed in the scoop twice, most likely because sunlight warmed them, and a third sample scraped off the surface was delivered<sup class="r">[21](#s21)</sup>. Clumpy soil also stuck on the TEGA oven screen, and only a few particles got through when it was vibrated<sup class="r">[22](#s22)</sup>.
4. **Engineering model.** Build a full-size rover and drive it in soil simulant on 15° slopes, as VIPER did<sup class="r">[1](#s1)</sup>.
5. **Cryo and vacuum.** VIPER drilled 1 m into soil simulant doped with 5% water and chilled to −100 °C in a thermal-vacuum chamber, and tested its wheels and steering in thermal vacuum<sup class="r">[1](#s1)</sup>. We repeat this, colder, closer to PSR conditions, with the drill feeding the chamber. Run a full 6 h sortie and a 96 h dark-survival case on the whole rover in thermal vacuum.
6. **Dark field test.** Drive in the dark using only the rover's lights and cameras, as VIPER did at NASA Ames<sup class="r">[1](#s1)</sup>.
7. **Flight units.** Run vibration, shock and EMI tests to the environments in each lander's user guide.
8. **On the Moon.** First drive away from the lander and bake a "dry" batch in sunlight to record the contamination baseline. Then make short PSR sorties, longer each time.

## Open questions

- Can the rover drive off a lander that is leaning by 10–15°? What ramp design copes with that?
- How many RHUs can we get, and on what schedule, under NSPM-20 and the available Pu-238 supply?
- How many bake cycles can one crucible and seal survive? Resource Prospector's prototype could reuse its crucible<sup class="r">[18](#s18)</sup>, but no rated number of reuses was found.
- What chamber size is best? Bigger batches give more water to measure but cost mass and energy.
- Is a 6 h sortie enough for several holes plus bake batches, or should batches be baked back in sunlight?
- ShadowCam found that surface ice is patchy<sup class="r">[14](#s14)</sup>. How many holes and batches per PSR give a useful ice estimate?
- Should one rover carry a near-infrared spectrometer (NIRVSS class), as Resource Prospector did, to watch the cuttings and scoop?
