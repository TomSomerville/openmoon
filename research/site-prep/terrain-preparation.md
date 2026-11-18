# Site and terrain preparation: clearing rocks, grading, and fusing regolith into hard surfaces

Researched 18 Nov 2026. Every claim below links to a source that was opened during this research. Where a value is not published, the text says so. This note's own arithmetic is marked **ESTIMATE** and shows its working. Numbers in square brackets point to the [Sources](#sources) list.

## Summary

- **The "ESA rover that microwaves regolith" does not match one single project.** ESA's paving project is **PAVER** ("Paving the road for large area sintering of regolith", Jun 2021 – Dec 2022). It melts regolith with a **12 kW CO2 laser** that stands in for **concentrated sunlight**, not microwaves ([ESA, 12 Oct 2023](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon) [1]; [LIQUIFER](https://liquifer.com/?p=1932) [4]). PAVER's roadmap lists a **mobile, in-place paving setup** as one of two strategies, and proposes a rover or a lander arm for a flight demo ([Brandić Lipińska et al., IAC 2022](https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf) [3]). The **microwave paver vehicle** is a **NASA** concept: Marshall's MMPACT microwave team set a goal of a "2mT microwave paver vehicle" for landing pads and roads ([Effinger, NASA MSFC, Dec 2020](https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf) [12]). ESA's own microwave work found here is lab-scale: an antenna applicator at EAC ([ESA blog, Aug 2021](https://blogs.esa.int/exploration/spaceship-eac-turning-up-the-heat-on-lunar-dust/) [5]) and the MARVEL payload study ([Univ. Surrey](https://www.surrey.ac.uk/research-projects/microwave-heating-apparatus-lunar-regolith-variant-experiments-lunar-isru-missions-marvel) [6]). Neither is a rover.
- **PAVER results.** It made interlocking glassy tiles ~220–250 mm across from EAC-1A simulant. One melt layer is ~18–20 mm deep. Mean compressive strength was **94 MPa**, but with a large spread (56–216 MPa). Density was **2.76 g/cm³** (~4.8% porosity). **Reheating a cooled track cracked it.** A three-layer build also cracked ([Ginés-Palomares et al. 2023](https://www.nature.com/articles/s41598-023-42008-1.pdf) [2]). ESA's own estimate is **115 days** for a 100 m², 2 cm thick pad ([ESA](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon) [1]). Tests were in air, not in vacuum ([2]).
- **NASA picked laser over microwave for its landing-pad material.** MMPACT's 2022–23 down-select tested three materials. Only ICON's laser VMX passed the full suite. Microwave sintering was not one of the three tested ([MMPACT poster 2023](https://ntrs.nasa.gov/api/citations/20230008890/downloads/MMPACT%20Jamboree%20Poster%202023%20-%20final.pdf) [14]). Microwave stays in the MMPACT "toolbox" ([14]; [MMPACT to JAXA, Apr 2024](https://ntrs.nasa.gov/api/citations/20240004549/downloads/20240422%20JAXA%20Presentation.pdf) [15]).
- **An economic trade study favours microwave sintering for the hot inner zone of a pad.** It found microwave sintering "currently the most favorable method" for the inner zone, "although other methods are within the range of uncertainty" ([Metzger & Autry 2022](https://arxiv.org/pdf/2205.00378) [18]). Its model needs **21.73 kWh/m²** of microwave energy for a sintered layer ([18]). This is a model, not a measurement.
- **Fused regolith suits pads, roads and berm crests, with caveats.** Sources name roads and landing pads as the main goal (PAVER [1][3], MMPACT [12][15], ICON [16]). The caveats are cracking under reheating and thermal shock [2], glass that may shatter into sharp fragments under a rocket plume [2], high power and long build times [1][18], and no test anywhere under a real lander engine on a fused-in-place surface.
- **Berms are cheap and well studied on paper.** Apollo plume ejecta blew out at about 1–3° above horizontal at ~1 km/s ([Metzger et al.](https://arxiv.org/pdf/2104.06248) [21]). NASA KSC's 2026 Lunar Innovation Park design uses a **2.5 m berm**, a 1 m crest and an 8 m standoff ([Gelino, Earth & Space 2026](https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf) [23]). RASSOR 2.0 has built a test berm ([23]).
- **Blade grading works on Earth. Lunar traction is the limit.** NASA's LANCE blade on the Chariot rover cleared a 25 × 25 m area in ~2.5 h and built a 1.3 m berm in ~4 h, in Earth gravity ([Mueller et al.](https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf) [26]). The ~700 kg Apollo rover's usable traction on the Moon was calculated at only **239 N** ([Just et al. 2024](https://link.springer.com/content/pdf/10.1007/s11440-023-01914-4.pdf) [27]).
- **Our site has some boulder data.** On the de Gerlache rim area "GR1" (~1.5 km²), Boazman et al. mapped 48 boulders (1.2–19.4 m²) and slopes under 6° on the rim ([Boazman et al. 2024](https://iopscience.iop.org/article/10.3847/PSJ/ad8fb0) [32]). Rocks smaller than ~1–4 m cannot be seen from orbit ([Boazman et al. 2022](https://iopscience.iop.org/article/10.3847/PSJ/aca590) [31]). Diviner's standard rock-abundance maps stop at 60°S ([ODE](https://ode.rsl.wustl.edu/moon/pagehelp/Content/Missions_Instruments/LRO/DIVINER/GDR_L3.htm) [34]). **Small-rock counts for our site are not published.**

## 1. Clearing rocks

### What has to be cleared: rock data near our site

| Data set | What it says | Where | Source |
|---|---|---|---|
| LROC NAC boulder map (Boazman et al. 2022) | 86,896 isolated boulders mapped. Smallest mapped size is 2×2 pixels, about 1–4 m. Up to 1,800 boulders/km² on the Shackleton rim. About 3,000/km² at the base of the connecting-ridge slope. About 0–300/km² around ridge PSRs. About 300–600/km² near the Spudis PSR. | Artemis sites 001 (89.45°S, 137.31°W) and 004 (89.78°S, 155.73°W), Shackleton–de Gerlache ridge | [Boazman et al. 2022, PSJ 3:275](https://iopscience.iop.org/article/10.3847/PSJ/aca590) [31] |
| LROC NAC hazard map (Boazman et al. 2024) | GR1 on the de Gerlache rim: ~1.5 km², 48 boulders, 1.2–19.4 m² in area (median 3.5 m²). 4,249 craters, smallest 1.5 m. Rim slopes under 6°. Boulders and craters over 5 m, and slopes over 10°, are treated as landing hazards. Some parts were in darkness and could not be mapped. | de Gerlache rim (GR1); connecting ridge (CR1) | [Boazman et al. 2024, PSJ](https://iopscience.iop.org/article/10.3847/PSJ/ad8fb0) [32] |
| Boulder slopes (Lamantia et al., abstract) | More than 10,000 boulders mapped around de Gerlache. 94.91% rest on slopes under 30°; 57.02% on slopes of 20° or less. Sizes and densities are not given in the abstract. | de Gerlache area | [GSA 2023 abstract](https://studio.m-anage.com/gsa/2023AM/webprogram/Paper392864.html) [33] |
| Diviner rock abundance | Standard gridded maps cover only −60° to +60° latitude. | Not our site | [WUSTL ODE, Diviner GDR L3](https://ode.rsl.wustl.edu/moon/pagehelp/Content/Missions_Instruments/LRO/DIVINER/GDR_L3.htm) [34] |
| Rocks under ~1 m | **Not published for our site.** No lander or rover has imaged it. | — | — |

**For plan use:** Orbital data show where large boulders are. They do not show the cobbles and small rocks a blade, sieve or fusing robot will meet. Those need surface imaging first (M01 prospecting).

### Robots and concepts for moving rocks

| Concept | How it handles rocks | Status | Source |
|---|---|---|---|
| NASA LANCE blade on Chariot | The blade is meant for "area clearing of rocks, leveling, dozing, grading, and berm construction". Its structure was analysed for a 5,000 lbf load from hitting a buried rock. | Field test, Moses Lake, Jun 2008 | [Mueller et al.](https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf) [26] |
| ASPECT (Colorado School of Mines, Lunar Outpost, Michigan Tech) | NASA describes ASPECT as "a fully autonomous rover" for excavation, **boulder moving** and compaction. The system pairs a Lunar Outpost Hound rover with a "rock and regolith grader" and a compactor. It was tested in a >100 m² regolith bed on a 10 m diameter site. The paper reports power, time and energy, but the values are not on the public abstract page. | NASA LuSTR 2021 grant; Ascend 2026 paper | [NASA STRG](https://www.nasa.gov/directorates/stmd/space-tech-research-grants/aspect-autonomous-site-preparation-excavation-compaction-and-testing) [29]; [Dreyer et al. 2026](https://digitalcommons.mtu.edu/michigantech-p2/2839) [30] |
| Rock rake + trommel "breakwater" pad (van Susante) | Rocks are raked out of regolith, sorted by size in a trommel and laid smallest-first, largest on top. The trade study found raking energy "highly dependent on the rock abundance". | Concept in a trade study | [Metzger & Autry 2022](https://arxiv.org/pdf/2205.00378) [18] |
| Astrobotic / Carnegie Mellon rock-gathering rovers | Small rovers "the size of riding mowers" would comb the soil for rocks and gather them to pave a grit-free pad. The berm option was 8.5 ft tall in a 160 ft semicircle, built by two 330 lb rovers in under six months. | NASA-sponsored study, 2009 (press) | [ScienceDaily, Mar 2009](https://www.sciencedaily.com/releases/2009/02/090225132353.htm) [35] |
| CMU CraterGrader | A <25 kg robot with a 250 mm blade. It did not handle rocks; the paper lists rock picking as future work. | Lab sandbox, 2023 | [Lee et al., arXiv](https://ar5iv.labs.arxiv.org/html/2311.01697) [28] |
| Astroport (STTR Phase II) | Contract title: "bulk regolith handling technologies for landing/launch pad site preparation and blast shield construction". Its abstract includes regolith hauling and **sieving** and berm construction. | Contract to Sep 2027, up to $1.22M | [HigherGov contract record](https://www.highergov.com/contract/80NSSC24CA021/) [37] |
| LSMS crane | Built to offload cargo. **No source found that tests it for rock picking.** | — | Plan card `_tech/lunar-surface-manipulation-system-lsms.md` |
| NASA MMPACT forward work | Lists a "Flight site preparation vehicle (rock removal, leveling, etc.)" as work it plans to leverage. | Plan item, 2020 | [Effinger 2020](https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf) [12] |

**Terrestrial analogue.** TerraClear's farm rock picker mounts on a skid steer or track loader. It picks rocks up to 300 lb and averages **400 rocks per hour**. It is operator-driven; full autonomy was described as a "multi-year project" ([The Robot Report, May 2021](https://www.therobotreport.com/terraclear-picks-up-25-million-to-build-a-robotic-rock-picker/) [36]). It is a press source only.

## 2. Grading and levelling with a blade

| Study | Machine / blade | Test conditions | Result | Source |
|---|---|---|---|---|
| NASA LANCE + Chariot (KSC, JSC, GRC, CSM) | 4.1 m blade, aluminium frame and composite moldboard, 70% lighter than a commercial steel blade | Moses Lake, WA, Jun 2008; volcanic silt; Earth gravity; teleoperated | Cleared a 25 × 25 m area in ~2.5 h; grading estimated at a further 2 h. Built a 1.3 m ramp berm in ~4 h. Chariot gave ~5,000 lbf drawbar pull at wheel slip on firm ground. Work was "highly operator dependent". Behaviour in 1/6 g, vacuum and real regolith still needs study. | [Mueller et al.](https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf) [26] |
| Blade-force models (same paper) | Balovnev and Luth-Wismer equations versus measured forces | Moses Lake data | Balovnev bucket equations matched best. Luth-Wismer gave about 10× the measured horizontal force. | [26] |
| CMU CraterGrader | <25 kg robot, 250 × 50 mm blade, chain-mail drag mat, 100 W max load, 138 N drawbar pull | 5 × 5 m site in quartz sand, Earth gravity | Final grade 0.11°, smoothness 0.7 cm, against NASA LuSTR targets of ±1° and 1 cm. Each run took about 30 min. | [Lee et al.](https://ar5iv.labs.arxiv.org/html/2311.01697) [28] |
| ASPECT | Hound rover + CSM grader + MTU compactor | >100 m² regolith bed with lunar-like topography and density | Power, time and energy measured for a 10 m site. **Values not public on the page opened.** | [Dreyer et al. 2026](https://digitalcommons.mtu.edu/michigantech-p2/2839) [30] |
| Metzger & Autry trade-study inputs (assumed, not measured) | 300 kg rover, 1.5 m grader blade | Model | Assumed grading rate 0.1 m²/s and compacting rate 0.05 m²/s. Blade force from Gallo et al. at 6 cm depth, divided by 6 for gravity, which the authors say is wrong where cohesion dominates. | [Metzger & Autry 2022](https://arxiv.org/pdf/2205.00378) [18] |
| RASSOR 2.0 berm test | Counter-rotating drums | Earth ambient, Black Point-1 simulant, teleoperated | Built a berm; average relative density 61% from repeated driving over it. | [Gelino 2026](https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf) [23] |

**Traction in low gravity.**
- On Earth, heavy machines use their weight to resist the blade's push. On the Moon a light vehicle slips or lifts instead ([Just et al. 2024](https://link.springer.com/content/pdf/10.1007/s11440-023-01914-4.pdf) [27]).
- Wilkinson and DeGennaro calculated the ~700 kg Apollo LRV's maximum effective tractive force on the Moon as "a mere 239 N" (as cited by [27]).
- Available traction "has to be multiple times larger than the necessary excavation force" ([27]).
- Vibrating the cutting edge cut forces by **up to 50%** in tests. Other studies cited there report up to 40× reductions with vibration or percussion ([27]).
- This is why IPEx and RASSOR use counter-rotating drums (see the plan's IPEx and RASSOR cards).

**Rates in m³/h and blade power.** No measured lunar-relevant m³/h or kW figure for blade grading was found. LANCE's figures are area and time on Earth. ASPECT's measured power figures are in the paywalled Ascend paper.

**ESTIMATE (this note's arithmetic, Earth test only):** LANCE cleared 625 m² in ~2.5 h, so about 250 m²/h. Including the further 2 h of grading, about 140 m²/h. In lunar gravity the same machine would have far less traction ([27]), so this is an upper bound, not a lunar rate.

**Compaction.** NASA MSFC lists that "lunar regolith typically compacts less than terrestrial simulants, with larger void ratios" ([Effinger 2020](https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf) [12]). The 2026 KSC design compacts pad and shelter foundations to 80% relative density, and assumes berms at 50% (1.4 g/cm³) ([Gelino 2026](https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf) [23]).

## 3. Fusing regolith into a hard surface: the projects

### Which project is the "ESA rover that microwaves regolith"?

- **ESA PAVER** is the ESA project about paving roads and landing pads. It uses **light** (a laser standing in for sunlight), not microwaves. "In practice we would not bring a carbon dioxide laser on the Moon," says ESA's Advenit Makaya. A Fresnel lens "a couple of metres across" would concentrate sunlight instead ([ESA](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon) [1]).
- PAVER has two strategies: tiles made at a fixed station and laid by a rover, or a **mobile sintering setup** that melts tiles in place. No choice between them had been made in 2022 ([IAC 2022](https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf) [3]). A demo could use "a robotic arm on the lander vehicle or ... a rover". The site must first be raked and graded "to remove larger rocks" ([3]).
- **The microwave paver vehicle is NASA's.** NASA MSFC's Microwave Structure Construction Capability (MSCC, part of MMPACT) aimed at "a mid-sized payload (e.g., 2mT microwave paver vehicle)" for landing pads and roads ([Effinger 2020](https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf) [12]). The NTRS file for that briefing is named "Moon Village-MSCC". The slides themselves do not say where they were shown.
- An early NASA KSC paper also suggested an excavator "equipped with a microwave transmitter to glassify the surface of the soil" ([Metzger et al.](https://arxiv.org/pdf/2104.06248) [21]).
- **ESA microwave work** found in this research is lab-scale and not on a rover. One is EAC's antenna applicator ([ESA blog](https://blogs.esa.int/exploration/spaceship-eac-turning-up-the-heat-on-lunar-dust/) [5]). The other is the MARVEL payload study at Surrey ([6]).
- **Conclusion:** No source found describes an ESA rover that microwaves regolith. The owner's description most likely mixes ESA PAVER (roads and pads, mobile paving) with NASA's microwave paver concept. This note cannot tell which one the owner saw.

### Project-by-project facts

| Project | Agency / funder | Method | Power | Rate | Layer / product | Test conditions | TRL / status | Sources |
|---|---|---|---|---|---|---|---|---|
| **PAVER** (BAM lead; Aalen Univ.; TU Clausthal; LIQUIFER; DLR support) | ESA OSIP, Off-Earth Manufacturing Campaign; Jun 2021 – Dec 2022 | 12 kW CO2 laser as a stand-in for concentrated sunlight; spot up to 100 mm | 10 kW (95 mm spot) for tracks; 3 kW (45 mm spot, 188 W/cm²) for interlocking tiles | Bed moved at 5 mm/min. ESA estimate: 100 m² × 2 cm pad in 115 days. A Fresnel lens of ~2.37 m² would replace the laser (paper's figure). | Melt depth 20 mm at 1,200 s, max 25 mm at 2,400 s. Glassy top, crystalline below. 94 MPa mean (56–216 MPa). 2.76 g/cm³, ~4.8% porosity. Surface roughness Ra 43.6 µm. | Single tracks and tiles in air. A vacuum crucible (~10⁻² mbar) was used only for the melt-depth study. EAC-1A simulant, dried at 180 °C. | TRL 3 → 4 during the project, aiming at TRL 5 (2022 paper). No flight demo booked. | [1] [2] [3] [4] |
| **NASA MSCC (microwave, MMPACT)** (MSFC with Alfred Univ., JPL, Radiance Technologies) | NASA Game Changing Development | Microwave sintering with horns/applicators | Not published (a 2006 1 kW microwave heater is shown) | Not published. "Mass sintered ... per hour" is listed as a challenge to determine. | Bricks of three simulants sintered in inert gas; sample ~5 cm × 2 cm. Near-field coupler shown on a benchtop in air. | Bench tests; 4 ft TVAC chamber with microwave system | Goal TRL 6. Not in the 2022–23 landing-pad down-select. | [12] [13] [14] |
| **ICON Olympus laser VMX** | NASA SBIR Phase III ($57.2M); MMPACT | Laser powder-bed fusion of regolith layers | Not published | Not published | ~50,000 psi compressive at 25 °C; ~36,500 psi after 1 year of lunar TVAC cycles; layer adhesion ~1,260 psi; 2.7 g/cm³ | Made in vacuum; arm working in TVAC at subsystem scale | Selected in MMPACT landing-pad down-select (2022–23). No lunar demo date listed. | [14] [16] [17] |
| **Metzger & Autry microwave model** | UCF / ASU study | Microwave at 2.45 GHz, 200 kW/m² baseline flux | Assumes 200 kW at the outpost, magnetron efficiency 0.5 | Modelled, not measured | 21.73 kWh/m² for a 3 cm layer; 18.45 kWh/m² for 1 cm (text). Inner pad 7.62 cm, outer 2.54 cm (inputs). | Finite-difference model using measured simulant dielectric data | Trade study only | [18] |
| **MOONRISE** (TU Braunschweig IRAS, LZH, Leibniz Univ. Hannover) | Volkswagen Foundation (**not ESA**) | Laser head (~3 kg) on the MIRA3D rover's arm | Not published | Not published | Melted "joint lanes"; spheres melted in the Einstein Elevator in lunar gravity and weightlessness | Laser head passed TVAC and vibration; regolith melted in a vacuum chamber | Project ended (2-year project, reported Jan 2021). Flight model was the next goal. | [8] |
| **RegoLight** (DLR lead; Space Applications Services; LIQUIFER; COMEX; Bollinger Grohmann) | EU Horizon 2020 (**not ESA**), Nov 2015 – Apr 2018 | Concentrated sunlight (DLR solar furnace, or xenon lamps) | Not published | About 1 layer per minute; regolith passed under the beam at 48 mm/s | Interlocking bricks with rounded edges; resolution 20–30 mm | Vacuum test at ~150 mbar only | TRL 3 → 5 claimed | [9] [10] |
| **ESA/DLR solar 3D-printed brick (2017)** | ESA | Concentrated sunlight, 0.1 mm layers at 1,000 °C | Not published | One 20 × 10 × 3 cm brick in ~5 h | Strength of gypsum; edges warped | Normal air pressure | Lab demo | [11] |
| **ESA EAC microwave (Spaceship EAC)** | ESA | Antenna-like applicator for local sintering and melting; semi-open cavity for bulk heating | "High-power"; value not published | Not published | Cavity made "a continuous line of molten regolith for the first time". Antenna made spots of melt. | Lab; plasma seen during cavity heating in vacuum | Lab | [5] |
| **MARVEL** (Univ. Surrey) | ESA OSIP, €175,000, Apr 2021 – Dec 2022 | Microwave heating; aims at flight hardware for an ESA ISRU payload | Not published on the page | — | — | Modelling and fabrication criteria | Ended per dates; outcome not on the page | [6] [7] |

**Microwave physics, from sources:**
- Taylor and Meek proposed that the nanophase iron in lunar soil makes it couple strongly to microwaves ([Crossref record](https://api.crossref.org/works/10.1061/(ASCE)0893-1321(2005)18:3(188)) [20]; hypothesis as described in [Metzger & Autry 2022](https://arxiv.org/pdf/2205.00378) [18]). The original abstract could not be retrieved.
- Recent NASA work, reported as a personal communication, "indicates that lunar soil with np-Fe0 absorbs microwaves only marginally better" than suitable simulants without it ([18]).
- For JSC-1AC simulant at 2.45 GHz, the loss tangent rises from 0.02 at 25 °C to 0.31 at 1,100 °C. The half-power depth falls from 286 mm at 110 °C to 13 mm at 1,100 °C. So the soil heats sluggishly below 200 °C and fast above it ([Allan et al., NTRS](https://ntrs.nasa.gov/api/citations/20110007089/downloads/20110007089.pdf) [19]).
- MSFC calls regolith "a super insulator". Its applicator must survive "an 1100C radiant surface and volatiles" ([12]).

### Energy comparison (this note's arithmetic)

| Case | Working | Result | Label |
|---|---|---|---|
| PAVER lab, 10 kW track | 0.095 m spot × 0.005 m/min = 0.0285 m²/h. 10 kW ÷ 0.0285 m²/h. Depth ~20 mm × 2.76 t/m³ = ~55 kg/m². | ~350 kWh/m², ~6.4 kWh/kg (~23 MJ/kg) of laser energy, in air | ESTIMATE |
| ESA PAVER pad estimate | 100 m² × 0.02 m × 2.76 t/m³ = 5.5 t over 115 days | ~2 kg/h | ESTIMATE from [1] |
| Metzger & Autry microwave model | 21.73 kWh/m² ÷ (0.03 m × 2,200 kg/m³ = 66 kg/m²) | ~0.33 kWh/kg (~1.2 MJ/kg) of microwave energy; ~2.4 MJ/kg electric at 0.5 magnetron efficiency | ESTIMATE from [18] |
| Cardiff & Hall solar sintering (2008, as cited) | 13 cm²/min | 100 m² pad in 55 days | as cited in [2] |

The lab laser figure is about 20× the microwave model. The two are not like for like: one is an unoptimised lab melt in air, the other a model that ignores heat conduction ([18]).

## 4. Applications: roads, pads, berms, dust-free surfaces

### Why pads and berms matter (plume ejecta)

- Apollo 12 landed **155 m** from Surveyor III ([Metzger et al., NTRS 2011/12](https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf) [22]). Surveyor's surface had "hundreds of pits" from soil particles. The particles struck at **300 m/s to 2 km/s** ([Metzger et al.](https://arxiv.org/pdf/2104.06248) [21]).
- The Surveyor dust paper modelled particles under 13 µm reaching Surveyor at up to 130 m/s ([22]).
- In Apollo landing videos, dust blew out at 1–3° above horizontal at ~1 km/s. Over a shallow crater on Apollo 15 the angle was 7–11°, and briefly over 22° ([21]).
- Because the spray is low, a berm may block most of it ([21]). But if a scour hole forms, larger, slower ejecta "will rain down upon the outpost, rendering berms or screens ineffective". So "a complete solution ... probably requires surface stabilization" ([21]).
- Even with a hard pad, the authors argue for berms too, because a failed pad would make "platy-shaped ejecta" that blows more easily ([21]).
- NASA KSC splits a pad into a central zone, an outer perimeter for off-nominal landings and dust, and blast barriers ([Gelino et al. 2020](https://ntrs.nasa.gov/api/citations/20205008550/downloads/Landing%20Launch%20Pads%20Concepts%20v3%20Poster.pdf) [24]).
- PAVER's paper cites the Surveyor III sandblasting and lunar rover dust as its reason for paving ([2]).

### What the sources say about each use

| Use | What sources say | Issues raised | Sources |
|---|---|---|---|
| **Landing pad, inner (hot) zone** | Metzger & Autry favour microwave sintering here. Inner zone radius 12 m, 7.62 cm thick in their model. MMPACT chose laser VMX for its landing-pad material. | Glass may fail under thermal shock "during rocket lift-off", making "sharp fragments" ([2]). No fused-in-place surface has been hot-fire tested. Pavers need grout so plume gas cannot get under the pad ([18]). | [2] [14] [18] |
| **Landing pad, outer zone** | Sintering wins when transport is costly; polymer infusion wins below ~$110K/kg delivered ([18]). Thinner layer (2.54 cm) is enough ([18]). | — | [18] |
| **Pavers vs in-place fusing** | NASA/Masten hot-fire tested sintered basalt pavers and blankets in 2021 ([25]). Pavers need ovens, mould handling and grout. In the model, grouting took about 2/3 of construction time ([18]). | Oven pavers lost more energy than microwaves for the thick inner pad ([18]). | [18] [25] |
| **Roads** | PAVER aims at "efficient transport routes that are less dusty" ([4]). Metzger & Autry suggest thicker roads across the outer pad so traffic does not fracture it ([18]). | PAVER's glassy surface roughness "could negatively influence the driving performance". Wheel friction has not been tested ([2]). | [2] [4] [18] |
| **Berms** | KSC 2026: 2.5 m high (lander height with solar array stowed), 1 m crest so IPEx tracks overlap, 52° side walls, 8 m standoff from berm face to lander, 4.9 m base width. Design uses ejecta at 1 km/s and 3°. On a 4° slope the berm volume rose 2.6×. | "No safe scientific or operational standoff distances have been defined." Ejecta erosion of berms still needs study. | [23] |
| **Berm crest / blast shield** | ICON says Olympus will inform landing pads, blast shields and roads ([16]). MMPACT lists berms and blast shields as targets ([15]). | No fused berm crest test found. | [15] [16] |
| **Dust-free surfaces** | PAVER and RegoLight both aim at dust mitigation ([3], [10]). | Durability under many thermal cycles: ICON's strength fell from ~50,000 to ~36,500 psi after 1 year of TVAC cycling ([16]), about 27% lower (this note's arithmetic); PAVER calls for thermal shock tests ([2]). | [2] [3] [10] [16] |

**Power and time (modelled).** With 200 kW for sintering, the model needs 3.5 t of microwave hardware plus 4 rovers to carry it ([18]). In one cost-optimised scenario, grading and compacting took 1.0 day, sintering the inner pad 5.0 days and the outer pad 17.3 days. In a slower scenario they took 4.3, 22.2 and 76.4 days ([18]).

## Fit with the current plan

This section only flags agreement and disagreement. It changes nothing.

| Plan item (current) | What the sources say | Fit |
|---|---|---|
| C05.3 product "~2.7 g/cm³, ~50,000 psi (ICON lab data)" | ICON slides give the same values ([16]). PAVER's laser-melt glass was 2.76 g/cm³ but only 94 MPa mean (~13,600 psi, this note's conversion), with a wide spread ([2]). | Agrees with ICON; PAVER shows a solar or broad-beam process may give a much weaker, more variable product. |
| C05.3 "Energy to fuse 1 kg: 1.5 MJ (ASSUMPTION, unsourced)" → 30 kW gives ~72 kg/h | Microwave model: ~1.2 MJ/kg delivered, ~2.4 MJ/kg electric (ESTIMATE from [18]). PAVER lab laser: ~23 MJ/kg (ESTIMATE from [2]). | The assumption sits near the microwave model. It is about 15× better than the only measured lab-laser data found. At PAVER-lab energy, 30 kW would give about 4.7 kg/h (ESTIMATE: 30 kWh/h ÷ 6.4 kWh/kg). The plan's own risk "fusing rate ... not published" is confirmed: no measured rate for VMX or MSCC was found. |
| C05.3 "Heritage: ... NASA MMPACT microwave sintering" | MMPACT's microwave work was not in its 2022–23 landing-pad down-select; laser VMX was selected ([14]). | Laser baseline agrees with NASA's choice. Microwave heritage is weaker than the card implies. |
| C05.3 "Layer: thin layers built up to 50 mm" | PAVER multi-layer builds cracked when the next layer was melted ([2]). Metzger & Autry say single-pass microwave depth "eliminates problems of delamination" ([18]). | Disagrees in part: layering is a known crack risk. |
| C05.2 "Surface thickness 50 mm, within NASA 25–50 mm range" | Metzger & Autry use 76.2 mm inner and 25.4 mm outer ([18]). PAVER single layer ~18–20 mm ([2]). | Inside the published spread. The inner zone may need to be thicker. |
| C05.2 "Berm ~2 m high (ESTIMATE)" | KSC 2026 design: 2.5 m, 1 m crest, 8 m standoff, for ~625 kg CLPS landers ([23]). | Plan is lower than KSC's design for much smaller landers. |
| C05.2 "Thermal cycling may crack a large slab → pavers or panels" | PAVER chose hollow interlocking tiles with no crossovers because reheated tracks cracked ([1][2]). | Agrees. |
| C05.2 sub-grade "clear rocks, level, compact" | PAVER and MMPACT both require rock removal and grading first ([3][12]). KSC compacts pad foundations to 80% RD ([23]). | Agrees. No compaction target is stated in the plan. |
| C05.1 "200 kg/h per unit (ESTIMATE)", grading blade add-on | No measured lunar blade rate found. Lunar traction is very limited ([27]). LANCE Earth rates exist but are not lunar ([26]). | Not contradicted, not supported. Blade work on a light robot is traction-limited. |
| C05.3 open question "laser or microwave?" | Sources split: the NASA down-select chose laser VMX [14]; the economic trade chose microwave [18]; ESA PAVER uses light (solar) [1]. | Still open. |
| Site rocks | GR1 on de Gerlache rim: 48 boulders in ~1.5 km², slopes <6° ([32]). Small rocks are not mapped. | Supports a rim pad site; rock clearing load is unknown. |

## Possible tech cards

Candidates only. None created.

- **ESA PAVER (solar/laser paving)** — already an alternative inside the pavers card; could become its own card.
- **NASA MMPACT microwave sintering (MSCC)** — microwave paver vehicle concept.
- **NASA LANCE lunar bulldozer blade** — field-tested blade with Chariot.
- **ASPECT autonomous site preparation (Colorado School of Mines / Lunar Outpost / Michigan Tech)**.
- **Regolith berms and blast barriers (NASA KSC Lunar Innovation Park design)**.
- **Rock rake and trommel gravel pad (van Susante)**.
- **MOONRISE rover-mounted laser (LZH / TU Braunschweig)**.
- **RegoLight solar sintering** — already an alternative on the ICON card.
- **Astroport BrickBot / molten-regolith bricks**.
- **Vibration-assisted excavation blades** ([27]).

## Photos

Not downloaded. Credits are as given on each source page.

| What it shows | Real hardware? | Page | Credit |
|---|---|---|---|
| PAVER laser tracks, interlocking tiles, cross-sections | Yes (lab samples) | [Ginés-Palomares et al. 2023, Figs 1–4](https://www.nature.com/articles/s41598-023-42008-1) [2] | Ginés-Palomares et al., *Scientific Reports* (open access, CC BY) |
| PAVER lab images: laser, triangular melt pattern, 1.8 cm melt layer | Yes (lab) | [ESA "How to make roads on the Moon"](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon) [1] | ESA page; per-image credit not captured in text retrieved |
| PAVER artist's scene: lander on a tiled pad, robot arm in foreground | No (artwork) | [LIQUIFER "Paving the Road"](https://liquifer.com/?p=1932) [4] | LIQUIFER |
| PAVER 12 kW laser, KUKA arm, X-Y unit, recoater (Fig. 1) | Yes (lab) | [IAC 2022 paper](https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf) [3] | PAVER consortium |
| EAC microwave antenna applicator and molten spots | Yes (lab) | [ESA blog](https://blogs.esa.int/exploration/spaceship-eac-turning-up-the-heat-on-lunar-dust/) [5] | ESA–T. Schild; portrait ESA–E. Tuohy |
| MOONRISE melted lanes | Yes (lab) | [LZH press release](https://www.lzh.de/en/node/22569) [8] | Photo: LZH |
| RegoLight solar-printed parts, mobile printing head, vacuum setup | Yes (lab) | [IAC 2018 paper](https://liquifer.com/wp-content/uploads/2020/03/2018_Using_IAC-18E516x477461.pdf) [10] | RegoLight consortium; photos DLR and Space Applications Services |
| MSFC 20 ft vacuum chamber; 1 kW microwave heater; 4 ft TVAC with microwave system | Yes (facilities) | [Effinger 2020](https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf) [12] | NASA |
| MSCC microwave-sintered brick; near-field coupler | Yes (lab) | [Edmunson 2022](https://ntrs.nasa.gov/api/citations/20220012533/downloads/ISRU%20Tech%20Review%202022%20Edmunson%20v2.pdf) [13] | Dr Holly Shulman and Radiance Technology / Quinn Otte |
| ICON laser-melted 1.3 kg sample; TVAC robot | Yes (lab) | [Edmunson 2022](https://ntrs.nasa.gov/api/citations/20220012533/downloads/ISRU%20Tech%20Review%202022%20Edmunson%20v2.pdf) [13]; [ICON LSIC slides](https://lsic.jhuapl.edu/uploadedDocs/focus-files/2291-ICON%20Olympus%20LSIC%20Slides%2031JAN2024.pdf) [16] | ICON (used with permission) |
| LANCE blade grading and building a berm at Moses Lake | Yes (field test) | [Mueller et al.](https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf) [26] | NASA |
| CraterGrader robot in MoonYard | Yes (lab) | [Lee et al.](https://ar5iv.labs.arxiv.org/html/2311.01697) [28] | Carnegie Mellon University authors |
| Surveyor III with Apollo 12 LM on horizon | Yes (Moon) | [Metzger et al.](https://arxiv.org/pdf/2104.06248) [21] (Fig. 5) | NASA |

## Not verified (leads only)

- **ESA MICROLITH** ("MICROwaves heating for sintering of regoLITH", RINA, EXPRO+). Search results list it on ESA Nebula, but `nebula.esa.int` could not be reached from this session, so no facts are given here. The host must be allowed in the session's network settings to check it.
- **Caterpillar–NASA lunar work.** Only press coverage from 2008–2019 was found. Not used.
- **NASA FLEET ultrasonic blade on parabolic flights (2024).** Force results not found.
- **Taylor & Meek 2005 abstract.** Paywalled; only the bibliographic record was opened [20].

## Sources

1. ESA: "How to make roads on the Moon" (PAVER project). 12 Oct 2023. https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon
2. Ginés-Palomares, J.-C., Fateri, M., Kalhöfer, E., Schubert, T., Meyer, L., Kolsch, N., Brandić Lipińska, M., Davenport, R., Imhof, B., Waclavicek, R., Sperl, M., Makaya, A., Günster, J., "Laser melting manufacturing of large elements of lunar regolith simulant for paving on the Moon", *Scientific Reports* 13:15593 (PDF). Oct 2023. https://www.nature.com/articles/s41598-023-42008-1.pdf
3. Brandić Lipińska, M. et al., "PAVER – Contextualizing laser sintering within a lunar technology roadmap", IAC-22,A3,2C (LIQUIFER-hosted PDF). Sep 2022. https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf
4. LIQUIFER Systems Group: "Paving the Road" project page. Accessed 18 Nov 2026. https://liquifer.com/?p=1932
5. ESA Exploration blog: "Spaceship EAC: turning up the heat on lunar dust". 12 Aug 2021. https://blogs.esa.int/exploration/spaceship-eac-turning-up-the-heat-on-lunar-dust/
6. University of Surrey: "Microwave heating apparatus of lunar regolith for variant experiments of lunar ISRU missions (MARVEL)" (ESA OSIP). Accessed 18 Nov 2026. https://www.surrey.ac.uk/research-projects/microwave-heating-apparatus-lunar-regolith-variant-experiments-lunar-isru-missions-marvel
7. University of Surrey: "Microwave heating demonstrator payload" (UKSA). Accessed 18 Nov 2026. https://www.surrey.ac.uk/research-projects/microwave-heating-demonstrator-payload
8. Laser Zentrum Hannover: "MOONRISE: Step by step towards a village made of moon dust". 7 Jan 2021. https://www.lzh.de/en/node/22569
9. CORDIS (European Commission): RegoLight, "Sintering Regolith with Solar Light", grant 686202. Accessed 18 Nov 2026. https://cordis.europa.eu/project/id/686202
10. Imhof, B. et al., "Using solar sintering to build infrastructure on the Moon – latest advancements in the RegoLight project", IAC-18.E5.1 (LIQUIFER-hosted PDF). Oct 2018. https://liquifer.com/wp-content/uploads/2020/03/2018_Using_IAC-18E516x477461.pdf
11. ESA: "Printing bricks from moondust using the Sun's heat". 3 May 2017. https://www.esa.int/articles/printing-bricks-from-moondust-using-the-sun-s-heat
12. Effinger, M., NASA MSFC: "Microwave Sintering Lunar Landing Pads & Horizontal Infrastructure" (MMPACT MSCC), NTRS 20205010871. Dec 2020. https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf
13. Edmunson, J., NASA MSFC: "MMPACT", ISRU Technology Review, NTRS 20220012533. Aug 2022. https://ntrs.nasa.gov/api/citations/20220012533/downloads/ISRU%20Tech%20Review%202022%20Edmunson%20v2.pdf
14. NASA MSFC: "MMPACT Material Screening" poster, NTRS 20230008890. 2023. https://ntrs.nasa.gov/api/citations/20230008890/downloads/MMPACT%20Jamboree%20Poster%202023%20-%20final.pdf
15. NASA MSFC: MMPACT presentation to JAXA, NTRS 20240004549. Apr 2024. https://ntrs.nasa.gov/api/citations/20240004549/downloads/20240422%20JAXA%20Presentation.pdf
16. ICON: "Project Olympus" LSIC slides. 31 Jan 2024. https://lsic.jhuapl.edu/uploadedDocs/focus-files/2291-ICON%20Olympus%20LSIC%20Slides%2031JAN2024.pdf
17. NASA: "NASA enables construction technology for Moon and Mars exploration". 13 May 2025, updated 22 Jun 2026. https://www.nasa.gov/directorates/stmd/nasa-enables-construction-technology-for-moon-and-mars-exploration/
18. Metzger, P. T. and Autry, G. W., "The Cost of Lunar Landing Pads with a Trade Study of Construction Methods" (arXiv 2205.00378). May 2022. https://arxiv.org/pdf/2205.00378
19. Allan, S. M. et al., "High Temperature Microwave Dielectric Properties of JSC-1AC Lunar Simulant", NTRS 20110007089 (manuscript). 2011. https://ntrs.nasa.gov/api/citations/20110007089/downloads/20110007089.pdf
20. Crossref record: Taylor, L. A. and Meek, T. T., "Microwave Sintering of Lunar Soil: Properties, Theory, and Practice", *J. Aerospace Engineering* 18(3), 188–196, DOI 10.1061/(ASCE)0893-1321(2005)18:3(188). 2005. https://api.crossref.org/works/10.1061/(ASCE)0893-1321(2005)18:3(188)
21. Metzger, P. T., Li, X., Immer, C. D., Lane, J. E., NASA KSC: "ISRU Implications for Lunar and Martian Plume Effects" (arXiv 2104.06248). Posted Apr 2021. https://arxiv.org/pdf/2104.06248
22. Metzger, P., Hintze, P., Trigwell, S., Lane, J., NASA KSC: "Further Analysis on the Mystery of the Surveyor III Dust Deposits", NTRS 20120000029. 2012. https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf
23. Gelino, N., NASA KSC Swamp Works: "Lunar Innovation Park: Site Plan & Bulk Regolith Feature Design", Earth & Space 2026, NTRS 20260002816. Apr 2026. https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf
24. Gelino, N. et al., NASA KSC: "Lunar Landing and Launch Pad Construction – Concepts and Criteria" poster, NTRS 20205008550. 2020. https://ntrs.nasa.gov/api/citations/20205008550/downloads/Landing%20Launch%20Pads%20Concepts%20v3%20Poster.pdf
25. NASA: "NASA Tests Landing Pad Materials for Future Lunar Missions". 21 Oct 2021. https://www.nasa.gov/centers-and-facilities/kennedy/nasa-tests-landing-pad-materials-for-future-lunar-missions
26. Mueller, R. P., Wilkinson, R. A., Gallo, C. A., Nick, A. J., Schuler, J. M., King, R. H.: "Lightweight Bulldozer Attachment for Construction and Excavation on the Lunar Surface" (LANCE), AIAA Space 2009, NTRS 20130012987. 2009. https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf
27. Just, G. H., Roy, M. J., Joy, K. H., Smith, K. L., "Experimental proof-of-concept of the effect of inlet geometry on excavation forces and their reduction for small-scale continuous excavators", *Acta Geotechnica* 19, 55–70 (open access PDF). Jun 2023. https://link.springer.com/content/pdf/10.1007/s11440-023-01914-4.pdf
28. Lee, R., Younes, B., Pletta, A., Harrington, J., Wong, R. Q., Whittaker, W., "CraterGrader: Autonomous Robotic Terrain Manipulation for Lunar Site Preparation and Earthmoving" (arXiv 2311.01697, ar5iv). 2023. https://ar5iv.labs.arxiv.org/html/2311.01697
29. NASA Space Technology Research Grants: "ASPECT: Autonomous Site Preparation, Excavation, Compaction, and Testing". 1 Apr 2022. https://www.nasa.gov/directorates/stmd/space-tech-research-grants/aspect-autonomous-site-preparation-excavation-compaction-and-testing
30. Dreyer, C. B., van Susante, P., Wagner, V. et al., "Lunar Site Preparation Technology Development from ASPECT", Ascend 2026 (Michigan Tech record; DOI 10.2514/6.2026-3026). 13 May 2026. https://digitalcommons.mtu.edu/michigantech-p2/2839
31. Boazman, S. J. et al., "The Distribution and Accessibility of Geologic Targets near the Lunar South Pole and Candidate Artemis Landing Sites", *Planet. Sci. J.* 3:275. Dec 2022. https://iopscience.iop.org/article/10.3847/PSJ/aca590
32. Boazman, S. J., Heather, D., Inoue, H., Ohtake, M., "Mapping Potential Hazards and Identifying Sampling Points within Lunar South Polar Region Areas of Interest", *Planet. Sci. J.* 2024. https://iopscience.iop.org/article/10.3847/PSJ/ad8fb0
33. Lamantia, A., Hollingsworth, I. L., Luna, J., Roberson, P., "Distribution of boulders around de Gerlache crater and lunar south pole candidate landing regions", GSA Connects 2023 abstract. Oct 2023. https://studio.m-anage.com/gsa/2023AM/webprogram/Paper392864.html
34. Washington University ODE: "LRO Diviner Gridded Data Record Level 3 (GDR_L3)" help page. Accessed 18 Nov 2026. https://ode.rsl.wustl.edu/moon/pagehelp/Content/Missions_Instruments/LRO/DIVINER/GDR_L3.htm
35. ScienceDaily (Carnegie Mellon / Astrobotic release): "Researchers show small robots can prepare lunar surface for NASA outpost". 2 Mar 2009. https://www.sciencedaily.com/releases/2009/02/090225132353.htm
36. The Robot Report: "TerraClear picks up $25 million to build a robotic rock picker". 27 May 2021. https://www.therobotreport.com/terraclear-picks-up-25-million-to-build-a-robotic-rock-picker/
37. HigherGov contract record 80NSSC24CA021: Astroport Space Technologies, STTR Phase II, "Bulk regolith handling technologies for landing/launch pad site preparation and blast shield construction". Accessed 18 Nov 2026. https://www.highergov.com/contract/80NSSC24CA021/
