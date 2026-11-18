---
slug: molten-regolith-electrolysis-nasa-lunar-resource
title: "Molten regolith electrolysis (NASA + Lunar Resources)"
alternatives:
  - {name: "Carbothermal reduction (Sierra Space + NASA)", compare: "Melts a small spot of regolith with concentrated sunlight at about 1,800 °C and reduces it with carbon, producing carbon monoxide that must then be processed into oxygen. It is further along in testing than MRE and keeps the melt off the walls passively, but it adds gas-processing steps and leaves reduced slag rather than separated molten metals.", status: "Flight-like reactor ran automated in NASA JSC's dirty thermal-vacuum chamber in 2024; key hardware rated TRL 6", url: "https://ntrs.nasa.gov/citations/20250004151"}
  - {name: "Blue Origin Blue Alchemist", compare: "Blue Origin's own molten regolith electrolysis system, aimed at oxygen plus silicon, iron and aluminium for solar cells and other products. Same basic chemistry, but a separate, privately run design with less published test data.", status: "Passed critical design review Sep 2025; autonomous demo in a simulated lunar environment planned for 2026", url: "https://www.blueorigin.com/news/blue-alchemist-hits-major-milestone-toward-permanent-sustainable-lunar-infrastructure"}
  - {name: "Molten salt electrolysis (Metalysis process, ESA)", compare: "Keeps regolith solid in molten calcium chloride at 950 °C and pulls the oxygen out electrically. The lower temperature eases materials problems, but the salt is a consumable that must be recovered, and the metals come out as a mixed alloy.", status: "ESA prototype plant opened at ESTEC in Jan 2020; oxygen was vented, not stored", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust"}
  - {name: "Hydrogen reduction of iron oxide", compare: "Heats regolith above 900 °C in hydrogen so iron oxide gives up oxygen as water, which is then split. It runs much cooler than MRE, but it only reaches the oxygen bound in iron oxide, a small part of most regolith, so yield per kilogram is lower.", status: "Studied and lab-tested for decades; no lunar flight", url: "https://en.wikipedia.org/wiki/In_situ_resource_utilization"}
links:
  - {title: "NASA KSC: Large-scale demonstration of MRE for oxygen production in a relevant environment (ICES 2026 slides)", url: "https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf", kind: official, date: "Jul 2026"}
  - {title: "NASA NTRS 20260003760: Large-scale demonstration of MRE (ICES 2026 abstract)", url: "https://ntrs.nasa.gov/citations/20260003760", kind: official, date: "May 2026"}
  - {title: "NASA Kennedy breathes life into Moon soil testing", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing", kind: official, date: "May 2025"}
  - {title: "NASA NTRS 20250003220: MRE vacuum testing at KSC, analysis of the retrieved core sample", url: "https://ntrs.nasa.gov/citations/20250003220", kind: official, date: "May 2025"}
  - {title: "NASA KSC + Lunar Resources: MRE core sample analysis (LSIC slides)", url: "https://ntrs.nasa.gov/api/citations/20250005608/downloads/MRE_SRR_Core_presentation.pdf", kind: official, date: "May 2025"}
  - {title: "Grossman et al.: Development of a cold-walled MRE reactor (GaLORE)", url: "https://ntrs.nasa.gov/api/citations/20205007780/downloads/LSIC-Fall2020-abstract-MRE.pdf", kind: official, date: "Sep 2020"}
  - {title: "Sibille & Grossman: MRE system design and vacuum component testing (IAC-22)", url: "https://iafastro.directory/iac/archive/browse/IAC-22/D3/2B/72009/", kind: paper, date: "Sep 2022"}
  - {title: "Sibille & Dominguez: Joule-heated MRE reactor concepts for the Moon and Mars (ICES 2012)", url: "https://ntrs.nasa.gov/citations/20120003037", kind: paper, date: "Jul 2012"}
  - {title: "Sibille et al.: Performance testing of MRE with transfer of molten material (AIAA 2010)", url: "https://ntrs.nasa.gov/citations/20110008524", kind: paper, date: "Jan 2010"}
  - {title: "Schreiner et al.: A parametric sizing model for MRE reactors (Advances in Space Research)", url: "https://doi.org/10.1016/j.asr.2016.01.006", kind: paper, date: "Apr 2016"}
  - {title: "Lunar Resources: Resource extraction", url: "https://www.lunarresources.space/resource-extraction", kind: official, date: ""}
  - {title: "Colorado School of Mines: $2M from NASA to extract aluminium from an MRE reactor", url: "https://www.mines.edu/news/all-news/2023/mines-researchers-get-2m-from-nasa-to-advance-technology-for-extracting-aluminum-from-lunar-soil.html", kind: official, date: "Oct 2023"}
  - {title: "NASA Image Library: MRE testing on simulated regolith at Kennedy", url: "https://images.nasa.gov/details/KSC-20220913-PH-CSH01_0001", kind: official, date: "Sep 2022"}
  - {title: "Wikipedia: In situ resource utilization", url: "https://en.wikipedia.org/wiki/In_situ_resource_utilization", kind: wiki, date: ""}
---

## What it is

Molten regolith electrolysis (MRE) makes oxygen straight from Moon dirt. The regolith is melted at about 1,600 °C and an electric current is passed through the melt. Oxygen gas bubbles off at one electrode and molten metal collects at the other ([NASA NTRS](https://ntrs.nasa.gov/citations/20110008524)). It needs no chemical reagents, and it is the only single-step process that also gives raw molten metals ([IAC-22](https://iafastro.directory/iac/archive/browse/IAC-22/D3/2B/72009/)).

The idea is old. A case for it was published in 1990, electrode materials were shown in the lab by 2009, and a sizing model followed in 2015-2016 ([NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf); [Schreiner et al.](https://doi.org/10.1016/j.asr.2016.01.006)). Early lab cells used only 20-200 g batches; by 2010 tests ran at up to 10 A with 0.5-1 kg of simulant ([Sibille et al.](https://ntrs.nasa.gov/citations/20110008524)). From 2019 to 2023 NASA Kennedy's Swamp Works built an early reactor called GaLORE ([NASA](https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing); [image](https://images.nasa.gov/details/KSC-20220913-PH-CSH01_0001)).

In December 2024, Kennedy and Lunar Resources, Inc. of Houston tested the company's LR-1 reactor in a vacuum chamber, funded by NASA's Game Changing Development program through an SBIR Phase III contract ([NTRS](https://ntrs.nasa.gov/citations/20250003220)). It melted 25 kg of simulant and made about 0.07 kg of oxygen per hour for 9 hours ([NTRS](https://ntrs.nasa.gov/citations/20260003760)). NASA called it the first time it had made molecular oxygen with this process ([NASA](https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing)). Open Moon rates it TRL 4.

## Why Open Moon uses it

Regolith is more than 42% oxygen by mass ([NASA KSC](https://ntrs.nasa.gov/api/citations/20205007780/downloads/LSIC-Fall2020-abstract-MRE.pdf)), and it is everywhere. MRE is the main oxygen plant in [M06, ISRU pilot](/plan/m06-isru-pilot/), which targets at least 10 t of oxygen a year. That is about 1.1 kg an hour, or roughly 16 times the 2024 demo rate (this plan's arithmetic). Unlike ice mining, it does not depend on finding water in shadowed craters.

The oxygen feeds breathing air and, later, the oxidiser half of rocket propellant in [M11](/plan/m11-propellant/) ([NASA](https://www.nasa.gov/centers-and-facilities/kennedy/nasa-kennedy-breathes-life-into-moon-soil-testing)). The metal by-product (iron, silicon and others) feeds [M12, manufacturing](/plan/m12-manufacturing/). Lunar Resources says its process has extracted iron, aluminium, silicon and magnesium ([Lunar Resources](https://www.lunarresources.space/resource-extraction)), and a $2M NASA grant to Colorado School of Mines is building a system to tap molten aluminium from its MRE reactors and cast it into wire ([Mines](https://www.mines.edu/news/all-news/2023/mines-researchers-get-2m-from-nasa-to-advance-technology-for-extracting-aluminum-from-lunar-soil.html)). Without MRE, the base would rely on carbothermal reduction alone, or keep shipping oxygen from Earth.

## How it works

A run has three phases ([NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf)):

1. **Heat.** Heaters bring the regolith to about 1,400 °C.
2. **Electrolyse.** Current flows through the melt. The current itself heats it (Joule heating), so heater power can drop. At the anode, oxide ions give up electrons and form O₂. At the cathode, metal ions such as silicon are reduced to liquid metal.
3. **Cool.** The melt solidifies.

Each O₂ molecule needs 4 electrons, so the total current sets the maximum oxygen rate ([NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf)).

The key design idea is the "cold wall". Molten oxides and metals at 1,600 °C eat through containers. Heating only a pool between the electrodes leaves a shell of solid regolith that protects the vessel ([Sibille & Dominguez](https://ntrs.nasa.gov/citations/20120003037); [Grossman et al.](https://ntrs.nasa.gov/api/citations/20205007780/downloads/LSIC-Fall2020-abstract-MRE.pdf)).

| 2024 LR-1 test | Value |
|---|---|
| Feedstock | 25 kg ICN-LHT-1G highland simulant ([NASA](https://ntrs.nasa.gov/api/citations/20250005608/downloads/MRE_SRR_Core_presentation.pdf)) |
| Peak melt temperature | above 1,700 °C |
| Electrolysis | 9 h at 45 V, 210 A |
| Peak power | about 9 kW |
| Oxygen rate | 0.07 kg/h average |
| Oxygen produced | 2.3% of feed by weight |
| Efficiency | 0.3 mol O₂ per kWh |
| Gas purity | up to 80% O₂ by volume at some data points |

Values from [NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf) unless marked. 0.3 mol/kWh is about 100 kWh per kg of oxygen (this plan's arithmetic). The reactor sat in Kennedy's ASSIST chamber, which reaches 3×10⁻⁶ torr. Gas was tracked with a residual gas analyser, oxygen sensors and a gas chromatograph ([NTRS](https://ntrs.nasa.gov/citations/20250003220)).

## Limitations and open issues

- **Energy use.** About 100 kWh per kg in the demo. At that rate, 10 t a year needs about 120 kW (this plan's arithmetic). Bigger reactors should lose less heat, but no published test shows how much better they get.
- **Batch, not continuous.** The 2024 reactor ran one batch. Reusability, continuous feed and removal of spent melt, gas clean-up, compression and storage are all listed as future work ([NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf)).
- **Materials at 1,600-1,700 °C.** Melts are chemically aggressive and limit reactor life ([Sibille & Dominguez](https://ntrs.nasa.gov/citations/20120003037)). Anode and crucible wear rates over long runs are not yet published.
- **Gas purity.** Product gas reached up to 80% O₂ by volume, so other gases must be removed before use ([NASA KSC](https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf)).
- **Earth gravity, simulant only.** All tests used simulant at 1 g. Bubble release and melt flow in 1/6 g are untested.
- **No flight plan.** The NASA sources found here give no date for a lunar MRE demonstration.
- **Little company detail.** Lunar Resources' own pages do not publish reactor specifications ([Lunar Resources](https://www.lunarresources.space/resource-extraction)).
