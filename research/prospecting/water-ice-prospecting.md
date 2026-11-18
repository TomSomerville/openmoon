# Prospecting for water ice: past missions, extraction hardware and 1–3 m drills

Researched 18 Nov 2026. Every claim below links to a source that was opened during this research. Where a value is not published, the text says so. Anything that is this note's own arithmetic is marked "this note's arithmetic". Numbers in square brackets point to the [Sources](#sources) list. For where the ice is and how much there may be, see the companion note `research/ice/south-pole-water-ice.md`.

## Summary

- **No mission has yet measured ice in place in a lunar permanently shadowed region (PSR).** LCROSS hit Cabeus in 2009 and measured 5.6 ± 2.9 wt% water in the ejecta, but it was an impactor, not a lander ([AAAS](https://www.aaas.org/news/science-lcross-impact-ejects-minerals-and-frozen-water-crater-moon) [8]). PRIME-1 (TRIDENT drill + MSolo) landed on its side in March 2025 and "did not penetrate the ground" ([Zacny et al. 2025](https://iopscience.iop.org/article/10.3847/PSJ/ae0b51) [14]). Luna-25 crashed in August 2023 ([Wikipedia](https://en.wikipedia.org/wiki/Luna_25) [20]).
- **Phoenix (Mars, 2008) is the closest real example of "scrape ice, heat it in an oven, measure the water".** It is also a warning. The team wrote that "attempts to collect and to deliver ice-cemented soil materials to the TEGA ovens were not successful". They measured a sublimated lag instead, which held ~2% ice ([Smith et al. 2009](https://planetary.chem.tufts.edu/Boynton%20etal%20Science%202009v325p61.pdf) [1]).
- **The flight-ready lunar pattern is "drill, then heat the cuttings, then measure the gas".** TRIDENT (1 m, 26.5 kg) leaves a cuttings pile that MSolo and NIRVSS read ([NASA VIPER](https://science.nasa.gov/mission/viper/rover-and-instruments/) [15]; [14]). ESA's PROSPECT drills to 1 m and seals samples in up to 25 single-use ovens heated to 950 °C. Its stated water detection limit is 414 µg/g ([Trautner et al. 2024](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full) [27]). It is booked on Intuitive Machines IM-4 to Mons Mouton in 2027 ([ESA](https://www.esa.int/Newsroom/Press_Releases/European_drill_and_mini_lab_secure_ride_to_the_Moon) [28]; [NASA](https://www.nasa.gov/event/clps-flight-intuitive-machines-im-4-2/) [31]).
- **Upcoming ice measurements (as of 18 Nov 2026):**
  - VIPER: fully built and in final testing. It is due to fly in 2027 on a Blue Moon Mark 1 ([NASA, 20 Oct 2026](https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/) [16]).
  - Chang'e-7: missed its Aug 2026 window and is listed for 2027 ([Wikipedia](https://en.wikipedia.org/wiki/Chang'e_7) [17]).
  - LUPEX: launch no earlier than 2028. It observes down to 1.5 m ([JAXA](https://www.exploration.jaxa.jp/e/program/lunarpolar/) [18]).
  - ExoMars Rosalind Franklin (Mars): carries a 2 m drill. It is "on schedule for launch in the latter part of 2028" ([Sefton-Nash et al., EPSC 2026](https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-411.html) [21]).
- **Bulk water extraction from icy regolith is still lab hardware (TRL 4–5 at best).**
  - LUWEX (DLR-led) took almost 65% of the water out of an icy simulant at ~110 K and 5×10⁻⁶ mbar. The integrated system reached TRL 4, and the extraction subsystem TRL 5 ([DLR](https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions) [39]; [Imhof et al. 2024](https://liquifer.com/wp-content/uploads/2024/11/IAC-2024-LUWEX-paper_19092024.pdf) [40]).
  - NASA's LADI auger dryer reached TRL 4 ([NTRS](https://ntrs.nasa.gov/citations/20230013485) [38]).
  - NASA MSFC microwaved 0.5–2% ice simulant in cryo-vacuum. It removed at least 85% of the water in 5 minutes ([Ethridge & Kaukler 2007](https://ntrs.nasa.gov/api/citations/20070018802/downloads/20070018802.pdf) [33]).
- **The only published energy figure per gram of water is 1.7 Wh/g, for Honeybee's PVEx.** It comes from 2016 analog tests, as reported by Wikipedia ([Wikipedia](https://en.wikipedia.org/wiki/World_Is_Not_Enough_(spacecraft_propulsion)) [35]). That equals 1,700 Wh per kg of water (this note's arithmetic). The primary 2016 LEAG abstract was not found.
- **Low ice content makes sampling losses worse.** In NASA Glenn thermal-vacuum tests, drilled samples from a 4.5 wt% bed lost ~30% of their water during sampling. Samples from a 0.8 wt% bed lost ~80% ([Kleinhenz et al. 2018](https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf) [46]).
- **Ice cements regolith.** Simulant with ~0.6–1.5% ice "behaves like weak shale or mudstone". At ~10.6% ice it behaves like "strong limestone or sandstone" ([NASA KSC, Mantovani et al. 2014, citing Gertsch 2006](https://ntrs.nasa.gov/api/citations/20140017852/downloads/20140017852.pdf) [48]). Strength rises as temperature falls from −130 °C to −190 °C ([Liu et al. 2019](https://iafastro.directory/iac/archive/browse/IAC-19/D4/5/54517/) [49]).
- **No drill test at true PSR temperatures (25–40 K) was found.** Published drill tests went down to below −100 °C (TRIDENT, [14]) and below −150 °C (ProSEED, [27]). Test beds at NASA Glenn reached an average of 140 K ([Kleinhenz 2014](https://ntrs.nasa.gov/citations/20140012567) [47]).

## 1. Missions that sampled or detected water in place (Moon and Mars)

### 1a. Table

| Mission (body) | Instrument | What it measured | Depth | Result | Date | Status |
|---|---|---|---|---|---|---|
| Viking 1 & 2 (Mars) | GCMS (gas chromatograph–mass spectrometer) | Gases released when soil was heated up to 500 °C | Surface and subsurface samples at both sites | Water and CO₂ were released; no other inorganic gases; no martian organics ([NTRS, Biemann et al. 1977](https://ntrs.nasa.gov/citations/19780027538) [6]) | Landed 1976; paper 30 Sep 1977 | Ended |
| Apollo 15–17 (Moon) | Apollo Lunar Surface Drill | Returned deep core | 3 m length (Apollo 17 deep drill) | Six 3 g frozen subsamples from 94.5–292 cm depth have been kept at ~250–260 K since 1973. On the Moon they were below 250 K. "Drilling and extraction on the moon was very difficult" ([Lunar Sample Compendium, 70001–70006](https://curator.jsc.nasa.gov/lunar/lsc/a17drill.pdf) [24]) | Dec 1972 | Samples in curation |
| Apollo 17 ANGSA 73001 (Moon) | Drive tube, vacuum-sealed on the Moon | Volatiles in a sealed core | Lower half of a drive tube | Opened in Feb 2022 to study volatiles and prepare for cold, sealed Artemis samples. No gas results were found in this research ([NASA](https://www.nasa.gov/feature/nasa-studies-new-50-year-old-lunar-sample-to-prep-for-return-to-moon) [25]) | Collected Dec 1972; opened Feb 2022 | Analysis published in parts |
| Mars Odyssey GRS (Mars, orbit – context only) | Gamma-ray / neutron | Hydrogen | Upper ~1 m | 20–50% ice by mass in a lower layer. It lies ~60 cm down at 60°S and ~30 cm down near 75°S ([NASA JPL, 28 May 2002](https://www.jpl.nasa.gov/news/odyssey-finds-water-ice-in-abundance-under-mars-surface/) [7]) | 2002 | Orbital context |
| Phoenix (Mars) | TEGA: 8 single-use ovens, up to 1000 °C, with an evolved-gas mass spectrometer ([Boynton et al. 2009](https://planetary.chem.tufts.edu/Boynton%20etal%20Science%202009v325p61.pdf) [1]) | Melting endotherm and evolved H₂O | Ice table at ~5 cm under the lander; arm scraped ~2 mm-deep grids in the icy layer ([1]; [NASA JPL](https://www.jpl.nasa.gov/news/phoenix-scrapes-almost-perfect-icy-soil-for-analysis/) [2]) | Melting onset −2 °C; 1.0 mg ice; "~2% ice" if the oven was full. This was a sublimated lag, not the ice layer. Ice-cemented samples could not be delivered to the ovens ([Smith et al. 2009, in [1]]) | Landed May 2008 | Ended Nov 2008 |
| Curiosity (Mars) | SAM evolved-gas analysis (heated to ~835 °C) | H₂O, SO₂, CO₂, O₂ | Scooped surface fines (Rocknest) | 1.5–3 wt% water, bound in an amorphous component ([Leshin et al. 2013](https://mars.nasa.gov/files/msl/Science-2013-Leshin-.pdf) [3]) | 2012–13 | Operating |
| Curiosity (Mars) | DAN (pulsed neutron, IKI) | Hydrogen | Down to ~60 cm | Up to ~4% water along the early traverse ([Wikipedia, DAN](https://en.wikipedia.org/wiki/Dynamic_Albedo_of_Neutrons) [4]) | 2012 onward | Operating |
| Perseverance (Mars) | RIMFAX (radar), SHERLOC, SuperCam | Buried structure; minerals "altered by watery environments" (SHERLOC) | RIMFAX: "greater than 30 feet (10 meters)", depending on material | NASA's instrument page lists no ice measurement for these instruments ([NASA](https://science.nasa.gov/mission/mars-2020-perseverance/science-instruments/) [5]) | 2021 onward | Operating |
| LCROSS (Moon) | Impactor + NIR / UV-vis spectrometers | Water in the ejecta | Ejecta from the impact crater | 5.6 ± 2.9 wt% water; ~155 kg of vapour and ice in view ([AAAS](https://www.aaas.org/news/science-lcross-impact-ejects-minerals-and-frozen-water-crater-moon) [8]) | 9 Oct 2009 | Ended |
| Chang'e-5 (Moon) | Lunar Mineralogical Spectrometer on the lander | Water in regolith and in one rock | Surface, before sampling | Regolith < 120 ppm (mostly solar wind); a vesicular rock ~180 ppm ([CAS, Jan 2022](https://english.cas.cn/head/202201/t20220108_295734.shtml) [9]). Drill core ~1 m deep; 1,731 g returned ([Wikipedia](https://en.wikipedia.org/wiki/Chang%27e_5) [55]) | Dec 2020; paper 7 Jan 2022 | Complete |
| Chang'e-6 (Moon, far side) | Returned basalt, lab analysis | Water in the mantle source | Returned samples | 1–1.5 ppm (µg/g) in the mantle source, the lowest ever reported. Near-side samples reach up to 200 µg/g ([China Aerospace, Apr 2025](https://english.spacechina.com/n17212/c4305200/content.html) [10]) | Published Apr 2025 (*Nature*) | Complete |
| Chandrayaan-3 (Moon, 69.37°S) | ChaSTE thermal probe | Temperature profile | Top 10 cm | Peak 355 K on a 6° sun-facing slope. Modelling suggests that pole-facing slopes > 14° could hold ice "at depths of a few tens of centimetres". No water measurement ([ISRO, 6 Mar 2025](https://www.isro.gov.in/India_Bags_Credit_First-Ever_In-Situ_Measurement.html) [11]) | 24 Aug–2 Sep 2023 | Ended |
| Luna-25 (Moon) | ADRON-LR (active neutron/gamma), LIS-TV-RPM (IR spectrometer), LASMA-LR (laser mass spectrometer), arm for soil samples | Was to search for water ice | — | Crashed 19 Aug 2023. An engine ran 127 s instead of 84 s ([Wikipedia](https://en.wikipedia.org/wiki/Luna_25) [20]) | Aug 2023 | Failed |
| IM-2 PRIME-1 (Moon, 84.79°S) | TRIDENT drill + MSolo mass spectrometer | Was to drill and analyse cuttings | Planned 1 m | Lander on its side. In ~20 min, the drill extended to 35 cm and 100 cm, but "did not penetrate the ground" ([Zacny et al. 2025](https://iopscience.iop.org/article/10.3847/PSJ/ae0b51) [14]). NASA says "100% of the instruments worked" ([NASA](https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/) [12]). MSolo took 43 scans, dominated by Earth air and lander venting ([NTRS, Apr 2026](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf) [13]) | Landed 6 Mar 2025; ~12 h | Ended |
| VIPER (Moon) | NSS, TRIDENT, NIRVSS, MSolo | Hydrogen to ~1 m; cuttings | 1 m drill | Not flown ([NASA](https://science.nasa.gov/mission/viper/rover-and-instruments/) [15]) | Cancelled Jul 2024, then revived | Fully built, final testing; to fly in 2027 on Blue Moon Mk1 ([NASA, 20 Oct 2026](https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/) [16]) |
| Chang'e-7 (Moon) | Hopper: "Water Molecule and Hydrogen Isotope Analyzer" for a PSR. Rover: volatiles/isotopes system and penetrating radar | PSR in-situ | Not published | Not flown ([Wikipedia](https://en.wikipedia.org/wiki/Chang'e_7) [17]) | Aug 2026 window cancelled | Planned 2027; target 88°48′S 123°24′E near Shackleton |
| LUPEX (Moon) | REIWA (LTGA, TRITON, ADORE, ISRO's ISAP), NASA NS, ISRO GPR, ESA EMS-L | Water quantity, distribution, form | "Up to 1.5 m underground" | Not flown ([JAXA](https://www.exploration.jaxa.jp/e/program/lunarpolar/) [18]); "1.5m earth auger" ([JAXA tech page](https://humans-in-space.jaxa.jp/en/biz-lab/tech/lupex/) [19]) | — | NET 2028 on H3 |
| ExoMars Rosalind Franklin (Mars) | 2 m drill with Ma_MISS IR spectrometer; WISDOM radar (~3 m); Adron (neutrons) | Ice or water and hydrated minerals in the borehole wall ([ESA](https://exploration.esa.int/web/mars/-/45103-rover-instruments) [23]) | 2 m | Not flown | — | Launch in late 2028, landing at Oxia Planum in 2030 ([EPSC 2026](https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-411.html) [21]). ESA's instrument page lists Adron. Whether Adron is still on board after Russia's exit was not checked. |

### 1b. Lessons the sources state

- **Icy material is hard to deliver.** At Phoenix, ice-cemented soil could not be delivered to the TEGA ovens. The team analysed a sublimated lag instead ([1]). Before that, the arm made 50 scrapes in the icy layer to collect 10–20 cm³ piles ([NASA JPL](https://www.jpl.nasa.gov/news/phoenix-scrapes-almost-perfect-icy-soil-for-analysis/) [2]).
- **Contamination from the lander.** On PRIME-1 the spectra "were dominated by what we brought with us". The team says that baking out the mass spectrometer is necessary. They also say that "had we landed in an icy region, we would have seen H2O above the post-landing background" ([13]).
- **Apollo core heating.** The curators note that extraction "must have caused significant heating", and that dark drill segments "would have been substantially heated" unless they were shaded at once ([24]).

## 2. Hardware that takes regolith and extracts its water

Two classes exist. **Analytical ovens** heat milligrams to grams so that the water can be measured. **Extraction systems** heat kilograms or more to collect the water.

### 2a. Analytical ovens (prospecting instruments)

| System | How it works | Sample size | Heating | Detection | Mass / power | Status / TRL | Source |
|---|---|---|---|---|---|---|---|
| Phoenix TEGA (NASA/Univ. Arizona) | Sample dropped through a screen into one of 8 ovens. Calorimetry plus evolved gas carried by N₂ at 12 mbar to an analyser | Oven volume 0.052 cm³ | Up to 1000 °C at a controlled ramp | Mass spectrometer | Not published in the source | Flew in 2008 | [Boynton et al. 2009](https://planetary.chem.tufts.edu/Boynton%20etal%20Science%202009v325p61.pdf) [1] |
| Curiosity SAM | Evolved gas under helium flow | Scooped fines | ~835 °C | QMS and other analysers | Not opened in this research | Operating | [Leshin et al. 2013](https://mars.nasa.gov/files/msl/Science-2013-Leshin-.pdf) [3] |
| Resource Prospector OVEN + LAVA (NASA, cancelled 2018) | Drill delivers 12 cc. OVEN weighs it, seals it and heats it. LAVA identifies gases by GC-MS and photographs condensed water | 12 cc | 150 °C, 350 °C, 450 °C | GC-MS; water ≥ 0.5 wt% goal | OVEN ~12.5 kg, > 50 W steady | Not flown (programme ended) | [NTRS, Colaprete et al. 2016](https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf) [32] |
| ESA PROSPECT: ProSPA mini-lab (Open University) | Up to 25 single-use ovens on a carousel. Sample imaged, sealed, then heated. Two mass spectrometers: an ion trap (m/z 2–200) and a magnetic sector for isotopes | Push-tube ~45 mm³; auger ~5,000 mm³ ([27]); imaged volume 10–60 mm³ ([26]) | Up to 950 °C ([27]); 6 °C/min ramp for evolved-gas analysis; 900–1000 °C ISRU demos with H₂ or CH₄ ([26]) | H₂O minimum 414 µg/g, i.e. ~20.7 µg in 50 mg ([27]) | ProSPA 13 kg. Whole package averages 85.6 W, peaking at 200 W ([27]) | A Bench Development Model and a flight-like Solids Inlet System EM exist ([27]). To fly on IM-4 in 2027 ([28]; [30]; [31]) | [Barber et al. 2018](https://www.cosmos.esa.int/documents/1568476/1766000/RD5_2018_LPSC_PROSPECT_ProSPA_Poster_Abstract2172.pdf) [26]; [Trautner et al. 2024](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full) [27] |
| MSolo (NASA KSC, COTS-based) | Reads gases from the cuttings pile and the surroundings; no oven | — | None (relies on the warm cuttings) | Quadrupole mass spectrometer, 0–90 m/z scans | See the existing tech card | Flew on PRIME-1; also on VIPER | [13]; [15] |
| LUPEX REIWA (JAXA + ISRO) | Includes a thermogravimetric analyser (LTGA), TRITON, ADORE and ISRO's ISAP | Not published | Not published | Not published | Not published | In development, NET 2028 | [18]; [19] |

### 2b. Bulk water extraction (ISRU)

| System | How it works | Ice content tested | Test conditions | Result | Energy per kg water | TRL | Source |
|---|---|---|---|---|---|---|---|
| Microwave extraction (Ethridge & Kaukler, NASA MSFC) | 2.45 GHz microwaves heat regolith from within; vapour is caught in a liquid-nitrogen cold trap. The aim is to avoid digging | 0.5–2% water ice in JSC-1 simulant | Cryo (−196 °C) and vacuum (10⁻⁶ torr) test bed. A consumer kitchen microwave oven was used (1100–1200 W in the paper) | After 5 min of heating, ≥ 85% of the water was removed and 99% of that was captured | Not published | Not stated. The authors call it a "proof of principal demonstration" | [NTRS 2007](https://ntrs.nasa.gov/api/citations/20070018802/downloads/20070018802.pdf) [33]; [NTRS 2011](https://ntrs.nasa.gov/citations/20110008785) [34] |
| PVEx – Planetary Volatiles Extractor (Honeybee Robotics) | A double-wall coring drill goes into icy ground and heats the core. Vapour flows to a cold trap | Not given in the source opened | "Space analog conditions" | 87% extraction efficiency | 1.7 Wh/g, from 60 W for 40 min ([35]); = 1,700 Wh/kg (this note's arithmetic) | Not stated | [Wikipedia, citing Zacny et al. 2016 (LEAG)](https://en.wikipedia.org/wiki/World_Is_Not_Enough_(spacecraft_propulsion)) [35] |
| Thermal corer + VCHP cold trap (Advanced Cooling Technologies + Honeybee; NASA SBIR Ph II) | 3D-printed steel corer (17.3 cm long, 5 cm ID). Heat-transfer fluid flows in mini-channels; vapour goes to a cold-trap tank | 5 wt% | Regolith chamber at −30 °C to 20 °C, ~7×10⁻³ Torr; cold trap at −50 °C | ~32 g of water collected (> 100% apparent efficiency, attributed to errors). A 2-inch corer modelled 100% sublimation in 11 min | Preliminary estimate: "about 2.3 kWh of thermal energy is required to sublimate ice at a target rate of 0.278 kg/hr" | Not stated | [Lee et al., ICES-2023-337](https://www.1-act.com/wp-content/uploads/2023/07/ICES-2023-337-Ice-Extraction-and-Collection-System-of-Ice-Miner.pdf) [36] |
| LADI – Lunar Auger Dryer ISRU (NASA JSC) | Excavator feeds a hopper, then a variable-pitch heated screw conveyor. It runs below water's triple point, with regolith plugs as seals (no valves). Vapour goes to a cold trap | Planned 5–8.5 wt% | Lab breadboard (LHS-1 simulant) | Models validated by tests | Not published | TRL 4 (2023); GCD target TRL 5 | [NTRS abstract](https://ntrs.nasa.gov/api/citations/20210013233/downloads/PTMSS-SRR_LADI%20Abstract.doc.pdf) [37]; [NTRS 2023](https://ntrs.nasa.gov/citations/20230013485) [38] |
| LUWEX (DLR, TU Braunschweig, LIQUIFER, Thales Alenia, others; EU-funded) | Stirred crucible with rotating heating rods; ice sublimes. Cold trap at −150 °C; ice dropped into a liquefaction chamber, then purified | Several mixing ratios (exact values not given). Ice grains 2.4 µm radius | ~110 K, ~5×10⁻⁶ mbar (CoPhyLab L-Chamber) | Almost 65% extracted; > 3 L of clean water in total; ≥ 0.5 L per run | Not published | Integrated system TRL 4; extraction and capture TRL 5 | [DLR, 28 Oct 2024](https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions) [39]; [Imhof et al. IAC-2024](https://liquifer.com/wp-content/uploads/2024/11/IAC-2024-LUWEX-paper_19092024.pdf) [40] |
| Thermal Mining (Sowers, Colorado School of Mines; NASA NIAC 2019) | Heat ice in place with redirected sunlight, or with heaters or rods in boreholes. Vapour is caught under a dome-like tent and refrozen in cold traps | — | Concept study | NASA page: "60% less mass and energy than excavation" (project estimate) | Not published on the page | Concept (NIAC) | [NASA NIAC](https://www.nasa.gov/general/thermal-mining-of-ices-on-cold-solar-system-bodies/) [41] |
| WIEVR – Wells for In Situ Extraction of Volatiles (Grainflow Dynamics) | Solar heat vaporises subsurface ice; vapour rises up a well bore to a surface condenser. No pumps in the simplest form | — | — | No test data in the abstract | Not published | Concept | [NTRS 2013](https://ntrs.nasa.gov/citations/20130014116) [42] |
| NASA Break the Ice Lunar Challenge | Excavation and transport of icy regolith to a "hypothetical" processing plant. **Water extraction was not part of it.** | Not covered here | — | $1.5 M awarded | — | — | [NASA](https://www.nasa.gov/prizes-challenges-and-crowdsourcing/centennial-challenges/break-the-ice-challenge) [43] |
| Interlune excavator (with Vermeer) | Continuous excavator designed for 100 t/h of regolith. It is for **helium-3**; the release does not mention water | — | Full-scale prototype, May 2025 | — | — | Prototype | [Interlune](https://www.interlune.space/press-release/space-resources-company-interlune-unveils-full-scale-prototype-of-excavator-for-harvesting-helium-3-from-the-moon) [44] |

**Not found.** This research found no published source for "L-VRAP", "Water Walker" or a "Mobile In-Situ Water Extractor (MISWE)", so nothing is reported for them. No primary energy-per-kg figure was found for LUWEX, LADI or the microwave work.

**What sets the energy.** The LUWEX team writes that regolith's "extremely low thermal conductivity" means "it will take a lot of time and energy for the ice to reach a temperature where it could sublimate". This is why they stir it ([40]). The MSFC team gives the same reason for using microwaves, which heat "from within" ([34]).

## 3. Drilling 1–3 m into a PSR and checking for ice

### 3a. Drills and probes

| Hardware | Max depth | Mass | Power | How samples are analysed | Cold / ice tests | Status | Source |
|---|---|---|---|---|---|---|---|
| **TRIDENT** (Honeybee Robotics) – rotary-percussive | 1 m. Takes 10 cm "bites"; feed 1.25 mm/s | 26.5 kg (drill 19.5 kg + avionics 7 kg) | 50 W rotary (nominal); 2 J per blow at up to 972 blows/min | Cuttings are brushed into a pile; MSolo and NIRVSS read it (VIPER). A bit temperature sensor and heater are also fitted | Below −100 °C and < 10⁻⁴ Torr in LSP-2 simulant with up to 8.5 wt% ice. A 1 m hole in limestone in vacuum. Its parent design, the RP drill, was TRL 6 | Flew on PRIME-1 (did not drill); on VIPER for 2027 | [Zacny et al. 2025](https://iopscience.iop.org/article/10.3847/PSJ/ae0b51) [14]; [15] |
| **ProSEED** (ESA PROSPECT, Leonardo) | 1 m (ProSPA aims to analyse samples "from up to 1.2 m", per the 2018 abstract [26]) | 31.8 kg (CEU 5.3 kg, drill + positioner 23.4 kg, harness 3.1 kg) | Package averages 85.6 W, peaking at 200 W | Push tube and auger deliver into ProSPA ovens; a permittivity sensor is aimed at < 1 wt% ice (expected, not yet shown) | Demonstration model drilled NU-LHT-2M with up to ~10 wt% ice to 1 m, below −150 °C | To fly on IM-4 to Mons Mouton in 2027, operating ~1 lunar day | [Trautner et al. 2024](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full) [27]; [28]; [29]; [30]; [31] |
| **LUPEX auger** (JAXA/ISRO) | ~1.5 m | Not published (rover payload > 350 kg) | Not published | Samples go to REIWA | Not published | NET 2028 | [18]; [19] |
| **ExoMars drill** (ESA, Mars) | 2 m (drill tool ~700 mm + three ~500 mm rods) | Not published on the ESA page | Not published | 1 cm × 3 cm core goes to the onboard lab; Ma_MISS reads the borehole wall | Not published on the pages opened | Launch late 2028 | [ESA drill page](https://exploration.esa.int/web/mars/-/43611-rover-drill) [22]; [21] |
| **Chang'e-5 lander drill** | ~1 m core | Not published | Not published | Core returned to Earth | Mid-latitude, no ice | Flew 2020 | [Wikipedia](https://en.wikipedia.org/wiki/Chang%27e_5) [55] |
| **Apollo Lunar Surface Drill** (crew-operated) | 3 m (Apollo 17 deep drill) | Not published in the source | Not published | Core returned | — | Flew 1971–72 | [24] |
| **LISTER** (Texas Tech + Honeybee) – pneumatic | 1 m (≈ 98 cm in the first three days) | 12.9 kg incl. avionics | Not published (50 mW heater during measurements) | No sample return; thermal probe only. Two tanks of ~130 g N₂ each | Mare Crisium, not a PSR | Flew on Blue Ghost 1 (Mar 2025) | [Nagihara et al. 2025](https://iopscience.iop.org/article/10.3847/PSJ/ae0465) [50] |
| **Icebreaker drill** (Honeybee, for the Icebreaker Life Mars proposal) – rotary-percussive | Designed for 1 m; 2.08 m reached in a field test at Haughton Crater | 10 kg (2nd generation) | Not published | Cuttings for life-detection instruments | Arctic and Antarctic ice-cemented ground. It got stuck at 1 m in one Antarctic hole; refrozen cuttings cross-contaminated samples. Vacuum-chamber holes reached 30 cm | Proposal not selected; "ready for flight" pending more tests (2014) | [NASA Astrobiology, Apr 2014](https://astrobiology.nasa.gov/news/icebreaking-mars/) [53] |
| **Planetary Deep Drill** (Honeybee) – wireline | Designed for tens of metres; depth reached not stated | Prototype 4 m long | ~100 W on average (50–250 W) in gypsum | Auger reeled up to empty | Gypsum quarry, Nov–Dec 2015 | Prototype | [Planetary Society, Jan 2016](https://www.planetary.org/articles/20160119-planetary-deep-drill-field-test) [51] |
| **Auto-Gopher / Auto-Gopher-2** (Honeybee + JPL) – wireline, piezo-percussive | "Limited only by the length of the tether" | Not published | Not published | Core breaker and retaining mechanism | Ice drilling at about −100 °C was planned, not reported as done | MatISSE development (2015) | [NASA Science](https://science.nasa.gov/?p=37083) [52] |
| **Honeybee Lunar Prospecting Drill** (Resource Prospector tests) | 40–50 cm sampling in the tests | Not published | ~20 W at ~30 N weight-on-bit | Samples brushed into a crucible (~5–10 min) | 10⁻⁵ Torr, −80 °C to −20 °C, 5 wt% water in NU-LHT-3M | Test hardware | [Kleinhenz et al. 2015](https://ntrs.nasa.gov/citations/20150011440) [45]; [46] |

### 3b. Non-drilling ways to check for ice

| Method | Example | Depth sensed | What it gives | Source |
|---|---|---|---|---|
| Rover neutron spectrometer | VIPER NSS | Up to ~1 m | Hydrogen; flags where to drill | [15] |
| Same, earlier design goal | Resource Prospector NSS | Down to 1 m | Water-equivalent hydrogen > 0.5 wt% | [32] |
| Active neutron | Curiosity DAN | ~60 cm | Up to ~4% water (Mars) | [4] |
| NIR spectrometer on cuttings | VIPER NIRVSS | Surface of the cuttings pile | Tells water from hydroxyl; CO₂, NH₃, CH₄ ices; surface temperature | [15] |
| Ground-penetrating radar | Chang'e-4 LPR (500 MHz) | ~40 m | Layering and boulders; the paper does not discuss ice | [Li et al. 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7043921) [54] |
| Ground-penetrating radar | Perseverance RIMFAX | > 10 m | Buried structure | [5] |
| Ground-penetrating radar | ExoMars WISDOM | ~3 m, cm-scale resolution | Picks drill sites | [23] |
| Ground-penetrating radar | LUPEX GPR (ISRO); Chang'e-7 rover radar | Not published | — | [18]; [17] |

### 3c. How PSR cold affects drilling and sampling

- **Temperatures.** A NASA-funded team gives a mean PSR temperature of about 85 K, ranging from 40 K to 120 K ([36]). The companion ice note gives 38 K at the LCROSS site and ~25 K in doubly shadowed craters.
- **Strength rises with ice content.** Load-penetration tests on JSC-1 compacted and cooled to cold-trap conditions found:

  | Ice content | Behaves like |
  |---|---|
  | 0.6–1.5% | "weak shale or mudstone… readily excavated" |
  | ~8.4% | "moderate-strength limestones, sandstones, and shales" |
  | ~10.6% | "strong limestone or sandstone and requires massive excavators" |

  ([NASA KSC, Mantovani et al. 2014](https://ntrs.nasa.gov/api/citations/20140017852/downloads/20140017852.pdf) [48], citing Gertsch et al. 2006.) Note: the Missouri S&T repository page for Gertsch et al. says "This paper has been withdrawn" ([Scholars' Mine](https://scholarsmine.mst.edu/faculty_work/2044) [57]). The reason is not given there.
- **Strength rises as it gets colder.** Colorado School of Mines tested a basaltic simulant with 6% water by mass. Compressive and tensile strength both correlate with falling temperature from −130 °C to −190 °C, and the material "behaves similarly to soft rock" ([Liu et al. IAC-19](https://iafastro.directory/iac/archive/browse/IAC-19/D4/5/54517/) [49]).
- **Water is lost while sampling.** In NASA Glenn tests at 10⁻⁵ Torr and −80 °C to −20 °C, properly sealed samples lost on average 30% of their water during drilling and transfer. Losses were lower at colder temperatures and for bigger samples ([45]). Over 43 samples, "agitating the sample during delivery has a significant impact" ([46]). Samples from a 4.5 wt% bed lost ~30%, and samples from a 0.8 wt% bed lost ~80% ([46]).
- **Test beds are warmer than PSRs.** NASA Glenn's frozen simulant bed, used to make cuttings piles for the RESOLVE spectrometer, averaged 140 K in vacuum ([47]).
- **Getting stuck.** TRIDENT carries an embedded heater and temperature sensors; both were run on PRIME-1 ([14]; [NASA](https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/) [12]). The Icebreaker drill stuck at 1 m in one Antarctic hole and could not retract ([53]).
- **Gap.** No drilling test at 25–40 K was found. The coldest drill tests reported were "below −100 °C" (~173 K) for TRIDENT ([14]) and "below −150 °C" (~123 K) for ProSEED ([27]). (The kelvin values are this note's arithmetic.)

## Photos

All of these show real hardware or real mission images unless the caption says otherwise.

| Subject | Page | Credit | Note |
|---|---|---|---|
| Phoenix: ice sublimating in the Dodo-Goldilocks trench (Mars) | https://images.nasa.gov/details/PIA10906 | NASA/JPL-Caltech/University of Arizona/Texas A&M University | Real image from Mars |
| Phoenix: soil on the TEGA oven screen (Mars) | https://images.nasa.gov/details/PIA11128 | NASA/JPL-Caltech/University of Arizona/Max Planck Institute | Real image from Mars |
| SAM being installed in Curiosity | https://images.nasa.gov/details/PIA13792 | NASA/JPL-Caltech | Flight hardware |
| TRIDENT flight drill inspected in a clean room (VIPER) | https://www.nasa.gov/general/all-together-now-drill-joins-other-moon-rover-science-instruments | NASA/Robert Markowitz | Flight hardware, Oct 2023 [56] |
| LISTER on Blue Ghost 1 | https://images.nasa.gov/details/IMG_4939 | NASA/Firefly Aerospace | Flight payload (Dec 2024) |
| Apollo 15 commander setting up the deep drill | AS15-87-11847, shown as Fig. 1 in the Lunar Sample Compendium [24] | NASA | Real lunar surface photo |
| LUWEX extraction set-up | https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions | DLR (CC BY-NC-ND 3.0) | Lab hardware [39] |
| Honeybee Planetary Deep Drill field test | https://www.planetary.org/articles/20160119-planetary-deep-drill-field-test | Credit not checked | Prototype [51] |
| ExoMars drill (deployed) | https://planetary.org/space-images/rosalind-franklin-drill-deployed | ESA/ATG medialab | **Artwork, not a photo.** ESA has hardware photos (e.g. "Deep drilling for Mars", 2023). Those pages did not load in this research, so they are not listed. |
| ProSEED drill | ESA image pages exist (e.g. "Lunar drill in action", 2020) | — | Pages did not load in this research (they redirected to ESA's homepage). Check the credit before use. |

## Already in the repo (tech cards)

- `_tech/trident-drill-honeybee-robotics.md` – TRIDENT (it already lists ProSEED, the LUPEX drill, LISTER and the Chang'e-5 drill as alternatives)
- `_tech/msolo-mass-spectrometer.md` – MSolo
- `_tech/viper-rover-nasa.md` – VIPER (lists LUPEX and Chang'e-7 as alternatives)
- `_tech/ice-excavation-nasa-break-the-ice.md` – excavation only, no extraction
- `_tech/nasa-isru-pilot-excavator-ipex.md`, `_tech/rassor-2-0.md` – excavators
- `_tech/shadowcam-on-kplo-danuri.md`, `_tech/chandrayaan-2-orbiter-dfsar-radar.md`, `_tech/lunar-reconnaissance-orbiter-lro.md` – orbital remote sensing

## Possible tech cards

Listed only; none were created.

1. ESA PROSPECT (ProSEED drill + ProSPA oven lab)
2. LUPEX rover and REIWA water analysers (JAXA/ISRO)
3. VIPER Neutron Spectrometer System (NSS) as a pre-drill hydrogen survey
4. NIRVSS near-infrared volatiles spectrometer
5. LISTER pneumatic excavation probe
6. Microwave volatile extraction (NASA MSFC)
7. LADI lunar auger dryer (NASA JSC)
8. Thermal corer / PVEx (Honeybee + ACT)
9. LUWEX extraction-and-purification chain (DLR-led)
10. Thermal Mining (Colorado School of Mines, NIAC)
11. Chang'e-7 hopper and its water-molecule analyser
12. Lunar ground-penetrating radar (Chang'e-4 LPR / LUPEX GPR)
13. Deep wireline drills (Honeybee Planetary Deep Drill / Auto-Gopher) for > 1 m holes

## Sources

1. Boynton, W. V. et al., "Evidence for calcium carbonate at the Mars Phoenix landing site", *Science* 325, 61 (2009). The PDF also holds the end of Smith, P. H. et al., "H2O at the Phoenix landing site", *Science* 325, 58–61. Tufts copy. https://planetary.chem.tufts.edu/Boynton%20etal%20Science%202009v325p61.pdf
2. NASA JPL: "Phoenix scrapes almost perfect icy soil for analysis". 1 Jul 2008. https://www.jpl.nasa.gov/news/phoenix-scrapes-almost-perfect-icy-soil-for-analysis/
3. Leshin, L. A. et al., "Volatile, isotope, and organic analysis of martian fines with the Mars Curiosity rover", *Science* 341 (2013). https://mars.nasa.gov/files/msl/Science-2013-Leshin-.pdf
4. Wikipedia: "Dynamic Albedo of Neutrons". Accessed Nov 2026. https://en.wikipedia.org/wiki/Dynamic_Albedo_of_Neutrons
5. NASA Science: Mars 2020 Perseverance science instruments. Accessed Nov 2026. https://science.nasa.gov/mission/mars-2020-perseverance/science-instruments/
6. NASA NTRS: Biemann, K. et al., "The search for organic substances and inorganic volatile compounds in the surface of Mars", *JGR* 82. 30 Sep 1977. https://ntrs.nasa.gov/citations/19780027538
7. NASA JPL: "Odyssey finds water ice in abundance under Mars' surface". 28 May 2002. https://www.jpl.nasa.gov/news/odyssey-finds-water-ice-in-abundance-under-mars-surface/
8. AAAS / *Science*: "LCROSS impact ejects minerals and frozen water" (Colaprete et al. 2010). Oct 2010. https://www.aaas.org/news/science-lcross-impact-ejects-minerals-and-frozen-water-crater-moon
9. Chinese Academy of Sciences: Chang'E-5 lander in-situ water detection (Lin et al., *Science Advances*). Jan 2022. https://english.cas.cn/head/202201/t20220108_295734.shtml
10. China Aerospace Science and Technology Corp.: Chang'e-6 far-side water finding (Hu Sen et al., *Nature*). Apr 2025. https://english.spacechina.com/n17212/c4305200/content.html
11. ISRO: "India bags credit of first-ever in-situ measurement…" (ChaSTE; *Commun. Earth Environ.*, doi:10.1038/s43247-025-02114-6). 6 Mar 2025. https://www.isro.gov.in/India_Bags_Credit_First-Ever_In-Situ_Measurement.html
12. NASA: "NASA's lunar drill technology passes tests on the Moon" (PRIME-1). 2025. https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/
13. NASA NTRS: Captain, J. et al., "PRIME-1: MSolo overview and results". Apr 2026. https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf
14. Zacny, K. et al., "TRIDENT ice mining drill for lunar volatile prospecting for PRIME-1 and VIPER missions", *Planet. Sci. J.* 6(12). 22 Dec 2025. https://iopscience.iop.org/article/10.3847/PSJ/ae0b51
15. NASA Science: VIPER rover and instruments. Accessed Nov 2026. https://science.nasa.gov/mission/viper/rover-and-instruments/
16. NASA: "NASA provides progress update on Moon Base rovers". 20 Oct 2026. https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/
17. Wikipedia: "Chang'e 7". Accessed Nov 2026. https://en.wikipedia.org/wiki/Chang'e_7
18. JAXA Space Exploration Center: Lunar Polar Exploration Mission (LUPEX). Accessed Nov 2026. https://www.exploration.jaxa.jp/e/program/lunarpolar/
19. JAXA Humans in Space: LUPEX technology page. Accessed Nov 2026. https://humans-in-space.jaxa.jp/en/biz-lab/tech/lupex/
20. Wikipedia: "Luna 25". Accessed Nov 2026. https://en.wikipedia.org/wiki/Luna_25
21. Sefton-Nash, E., Vago, J. L. et al., Rosalind Franklin mission status, EPSC 2026 abstract EPSC2026-411. 2026. https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-411.html
22. ESA Exploration: "The ExoMars drill unit". Accessed Nov 2026. https://exploration.esa.int/web/mars/-/43611-rover-drill
23. ESA Exploration: "The ExoMars rover instrument suite". Accessed Nov 2026. https://exploration.esa.int/web/mars/-/45103-rover-instruments
24. NASA JSC Lunar Sample Compendium (C. Meyer 2007, draft): Apollo 17 deep drill core, frozen samples 70001–70006. https://curator.jsc.nasa.gov/lunar/lsc/a17drill.pdf
25. NASA: "NASA studies new 50-year-old lunar sample to prep for return to Moon" (ANGSA 73001). Mar 2022. https://www.nasa.gov/feature/nasa-studies-new-50-year-old-lunar-sample-to-prep-for-return-to-moon
26. Barber, S. J. et al., "ProSPA: Analysis of lunar polar volatiles and ISRU demonstration on the Moon", LPSC 49, abstract 2172 (ESA-hosted). 2018. https://www.cosmos.esa.int/documents/1568476/1766000/RD5_2018_LPSC_PROSPECT_ProSPA_Poster_Abstract2172.pdf
27. Trautner, R. et al., "PROSPECT: A comprehensive sample acquisition and analysis package for lunar science and exploration", *Frontiers in Space Technologies* 5:1331828. 2024. https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full
28. ESA press release N° 46-2024: "European drill and mini lab secure ride to the Moon". 29 Aug 2024. https://www.esa.int/Newsroom/Press_Releases/European_drill_and_mini_lab_secure_ride_to_the_Moon
29. ESA Exploration: PROSPECT operations. Accessed Nov 2026. https://exploration.esa.int/web/moon/-/59105-operations
30. NASA Science: CP-22 science payloads (IM-4 to Mons Mouton). Accessed Nov 2026. https://science.nasa.gov/lunar-science/clps-deliveries/cp-22-science
31. NASA: CLPS flight Intuitive Machines IM-4 (event page, updated 21 Oct 2026). https://www.nasa.gov/event/clps-flight-intuitive-machines-im-4-2/
32. NASA NTRS: Colaprete, A. et al., "Resource Prospector instrumentation for lunar volatiles prospecting, sample acquisition and processing". Apr 2016. https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf
33. NASA NTRS: Ethridge, E. C. & Kaukler, W., "Microwave extraction of water from lunar regolith simulant", STAIF-2007. 2007. https://ntrs.nasa.gov/api/citations/20070018802/downloads/20070018802.pdf
34. NASA NTRS: Ethridge, E. C. & Kaukler, W., "Microwave processing of planetary surfaces for volatile extraction", AIAA ASM. Jan 2011. https://ntrs.nasa.gov/citations/20110008785
35. Wikipedia: "World Is Not Enough (spacecraft propulsion)" (PVEx test figures, citing Zacny et al. 2016, LEAG). Accessed Nov 2026. https://en.wikipedia.org/wiki/World_Is_Not_Enough_(spacecraft_propulsion)
36. Lee, K.-L. et al. (Advanced Cooling Technologies) and Zacny, K. (Honeybee), "Demonstration of ice extraction and ice collection system for lunar ice miners", ICES-2023-337. Jul 2023. https://www.1-act.com/wp-content/uploads/2023/07/ICES-2023-337-Ice-Extraction-and-Collection-System-of-Ice-Miner.pdf
37. NASA NTRS: Collins, J. A., Erickson, L. R., Walton, O., "Lunar Auger Dryer ISRU (LADI) breadboard testing and model validation" (abstract). 2021. https://ntrs.nasa.gov/api/citations/20210013233/downloads/PTMSS-SRR_LADI%20Abstract.doc.pdf
38. NASA NTRS: Collins, J. A., Michel, J., Araghi, K., "Lunar water extraction via Lunar Auger Dryer ISRU (LADI)", AIAA ASCEND. Oct 2023. https://ntrs.nasa.gov/citations/20230013485
39. DLR: "Water from Moon rock for future astronaut missions" (LUWEX). 28 Oct 2024. https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions
40. Imhof, B. et al., "LUWEX: Validation of lunar water extraction and purification technologies…", IAC-24,A3,2B,6. Oct 2024. https://liquifer.com/wp-content/uploads/2024/11/IAC-2024-LUWEX-paper_19092024.pdf
41. NASA NIAC: "Thermal Mining of Ices on Cold Solar System Bodies" (G. Sowers, Colorado School of Mines). 10 Apr 2019. https://www.nasa.gov/general/thermal-mining-of-ices-on-cold-solar-system-bodies/
42. NASA NTRS: Walton, O. R., "Wells for In Situ Extraction of Volatiles from Regolith (WIEVR)", NASA Tech Briefs. Jul 2013. https://ntrs.nasa.gov/citations/20130014116
43. NASA: Break the Ice Lunar Challenge (archived page). Accessed Nov 2026. https://www.nasa.gov/prizes-challenges-and-crowdsourcing/centennial-challenges/break-the-ice-challenge
44. Interlune press release: full-scale excavator prototype for helium-3. 7 May 2025. https://www.interlune.space/press-release/space-resources-company-interlune-unveils-full-scale-prototype-of-excavator-for-harvesting-helium-3-from-the-moon
45. NASA NTRS: Kleinhenz, J. E., Paulsen, G., Zacny, K., Smith, J., "Impact of drilling operations on lunar volatiles capture: thermal vacuum tests", AIAA 2015-1177. Jan 2015. https://ntrs.nasa.gov/citations/20150011440
46. NASA NTRS: Kleinhenz, J. et al., "Volatiles loss from water bearing regolith simulant at lunar environments". 2018. https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf
47. NASA NTRS: Kleinhenz, J., "Lunar polar environmental testing: regolith simulant conditioning", AIAA 2014-0689. Jan 2014. https://ntrs.nasa.gov/citations/20140012567
48. NASA NTRS: Mantovani, J. G. et al., "Characterizing the physical and thermal properties of planetary regolith at low temperatures" (cites Gertsch et al. 2006). 2014. https://ntrs.nasa.gov/api/citations/20140017852/downloads/20140017852.pdf
49. Liu, W., Zody, Z., Bottini, C., Rostami, J., Dreyer, C., "Estimation of geotechnical properties of icy lunar regolith in cryogenic environments", IAC-19 (abstract). 2019. https://iafastro.directory/iac/archive/browse/IAC-19/D4/5/54517/
50. Nagihara, S. et al., "LISTER on Blue Ghost Mission 1 to Mare Crisium. I. Pneumatic excavation of regolith", *Planet. Sci. J.* 6(10). 8 Oct 2025. https://iopscience.iop.org/article/10.3847/PSJ/ae0465
51. The Planetary Society: "Planetary Deep Drill field test" (J. Davis). 20 Jan 2016. https://www.planetary.org/articles/20160119-planetary-deep-drill-field-test
52. NASA Science: "Auto-Gopher: Drilling deep to explore the solar system". Accessed Nov 2026. https://science.nasa.gov/?p=37083
53. NASA Astrobiology: "Icebreaking Mars" (Icebreaker drill). 18 Apr 2014. https://astrobiology.nasa.gov/news/icebreaking-mars/
54. Li, C. et al., "The Moon's farside shallow subsurface structure unveiled by Chang'E-4 Lunar Penetrating Radar", *Science Advances* 6, eaay6898 (PMC). Feb 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7043921
55. Wikipedia: "Chang'e 5". Accessed Nov 2026. https://en.wikipedia.org/wiki/Chang%27e_5
56. NASA: "All together now: drill joins other Moon rover science instruments". 18 Oct 2023. https://www.nasa.gov/general/all-together-now-drill-joins-other-moon-rover-science-instruments
57. Missouri S&T Scholars' Mine: Gertsch, L. S., Gustafson, R., Gertsch, R. E., "Effect of water ice content on excavatability of lunar regolith" (record marked "withdrawn"). https://scholarsmine.mst.edu/faculty_work/2044
