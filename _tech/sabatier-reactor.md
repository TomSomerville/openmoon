---
slug: sabatier-reactor
title: "Sabatier reactor"
alternatives:
  - {name: "Sabatier plus methane post-processing (Plasma Pyrolysis Assembly or Honeywell carbon vapor deposition)", compare: "Keeps the flight-proven Sabatier reactor but adds a second stage that pulls hydrogen back out of the methane, raising oxygen recovery from about 50% to a theoretical 75% (plasma) or nearly 100% (carbon deposition). The cost is a hot, power-hungry extra unit and a carbon or acetylene by-product to manage.", status: "Plasma Pyrolysis Assembly rated overall TRL 3 and Honeywell CVD TRL 4 in NASA's 2020 trade", url: "https://ntrs.nasa.gov/citations/20205004679"}
  - {name: "Bosch and Series-Bosch reactors", compare: "Reduce CO2 all the way to solid carbon and water, so in theory all the oxygen is recovered and no gas is vented. Solid carbon fouls the catalyst and must be removed; in the 1990s head-to-head test the Bosch weighed and used several times more than the Sabatier.", status: "Series-Bosch at about TRL 3-4; still in modelling and lab testing at NASA Marshall", url: "https://ntrs.nasa.gov/citations/20250001963"}
  - {name: "Solid oxide co-electrolyzer with carbon formation reactor", compare: "Electrolyzes CO2 and water together at high temperature, giving pure oxygen directly plus a CO/H2 gas that a second reactor turns into solid carbon. It could replace both the Sabatier and the oxygen generator, but it is far less mature.", status: "Phase I prototype development at NASA Glenn and pH Matter (2017)", url: "https://ntrs.nasa.gov/citations/20170001404"}
  - {name: "Macrofluidic electrochemical reactor (MFECR)", compare: "Turns CO2 into ethylene and CO at room temperature while making oxygen, aiming at 75% or more recovery and replacing the Sabatier, oxygen generator and pyrolysis unit with one box. Only a single test cell exists so far.", status: "Single-cell laboratory testing at NASA Marshall and UT Arlington (2024)", url: "https://ntrs.nasa.gov/citations/20240002161"}
links:
  - {title: "NASA NTRS 20190030371: Hydrogen Recovery by Methane Pyrolysis to Elemental Carbon (ICES-2019-103)", url: "https://ntrs.nasa.gov/citations/20190030371", kind: paper, date: "Jul 2019"}
  - {title: "NASA NTRS 20205004679: Comparison of Exploration Oxygen Recovery Technology Options Using ESM and LSMAC (ICES-2020-108)", url: "https://ntrs.nasa.gov/citations/20205004679", kind: paper, date: "Jul 2020"}
  - {title: "NASA NTRS 20100033195: Sabatier Carbon Dioxide Reduction Assembly Development for Closed Loop Water Recovery", url: "https://ntrs.nasa.gov/citations/20100033195", kind: official, date: "Jan 2004"}
  - {title: "NASA NTRS 20050110128: Sabatier Methanation Reactor for Space Exploration", url: "https://ntrs.nasa.gov/citations/20050110128", kind: official, date: "2005"}
  - {title: "NASA image ISS025-E-007248: Doug Wheelock installs the Sabatier system in Tranquility", url: "https://images.nasa.gov/details/iss025e007248", kind: official, date: "Oct 2010"}
  - {title: "NASA NTRS 20140002591: Sabatier Catalyst Poisoning Investigation", url: "https://ntrs.nasa.gov/citations/20140002591", kind: paper, date: "Jul 2013"}
  - {title: "NASA NTRS 20120004277: Models for Carbon Dioxide Reduction Technologies for Spacecraft Air Revitalization", url: "https://ntrs.nasa.gov/citations/20120004277", kind: paper, date: "2012"}
  - {title: "NASA NTRS 20100036570: Sabatier Reactor Integration with Microwave Plasma Methane Pyrolysis Post-Processor", url: "https://ntrs.nasa.gov/citations/20100036570", kind: paper, date: "Jul 2010"}
  - {title: "NASA NTRS 20150016512: Advanced Oxygen Recovery via Series-Bosch Technology", url: "https://ntrs.nasa.gov/citations/20150016512", kind: paper, date: "Jul 2015"}
  - {title: "NASA NTRS 20170001404: Solid Oxide Co-Electrolyzer and Carbon Formation Reactor for Oxygen Regeneration", url: "https://ntrs.nasa.gov/citations/20170001404", kind: paper, date: "2017"}
  - {title: "NASA NTRS 20240002161: Electrochemical Recovery of O2 from Metabolic CO2 at the ISS (ICES-2024-168)", url: "https://ntrs.nasa.gov/citations/20240002161", kind: paper, date: "Jul 2024"}
  - {title: "NASA NTRS 20250001963: Parametric Study on the S-Bosch Process (ICES-2025-74)", url: "https://ntrs.nasa.gov/citations/20250001963", kind: paper, date: "Jul 2025"}
  - {title: "ESA: Advanced Closed Loop System (Airbus Sabatier-based CO2 recycling rack on ISS)", url: "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Research/Advanced_Closed_Loop_System", kind: official, date: "Sep 2018"}
  - {title: "Wikipedia: Sabatier reaction", url: "https://en.wikipedia.org/wiki/Sabatier_reaction", kind: wiki, date: "2026"}
---

## What it is

A Sabatier reactor combines carbon dioxide with hydrogen over a catalyst to make water and methane. French chemists Paul Sabatier and Jean-Baptiste Senderens discovered the reaction in 1897 ([Wikipedia](https://en.wikipedia.org/wiki/Sabatier_reaction)). In a spacecraft, both inputs are waste: CO2 that the crew breathes out, and hydrogen left over when water is split to make oxygen ([NASA NTRS](https://ntrs.nasa.gov/citations/20100033195)).

NASA picked Sabatier over the rival Bosch process for Space Station Freedom in 1992, and kept it for the ISS ([ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679)). Hamilton Sundstrand (now Collins Aerospace) built the ISS Carbon Dioxide Reduction Assembly, with NASA Johnson, NASA Marshall and Southwest Research Institute ([NASA NTRS](https://ntrs.nasa.gov/citations/20100033195); [ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679)). Astronaut Doug Wheelock installed it in the Tranquility node in October 2010 ([NASA](https://images.nasa.gov/details/iss025e007248)). It has run on the station since 2010 ([NASA NTRS](https://ntrs.nasa.gov/citations/20140002591)). NASA's 2020 trade study rates the ISS Sabatier at TRL 9 ([ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679)). Open Moon's table lists it more cautiously at TRL 8, because a lunar version has not flown.

ESA later sent a second Sabatier system, Airbus's Advanced Closed Loop System, to the ISS on Japan's HTV-7 cargo ship. ESA says it recycles about half the CO2, makes oxygen for three astronauts and saves about 400 litres of launched water a year ([ESA](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Research/Advanced_Closed_Loop_System)).

## Why Open Moon uses it

In the base life support, installed before the first crew (M08) and run by the crewed base (M09), the Sabatier reactor closes part of the oxygen loop. A CO2 scrubber removes CO2 from cabin air. The Sabatier turns it into water. The oxygen generator then splits that water into oxygen to breathe and hydrogen, which goes back to the Sabatier ([ICES-2019-103](https://ntrs.nasa.gov/citations/20190030371)). Without it, all the oxygen for breathing would have to come from shipped or mined water and from regolith processing.

Its known weakness is acceptable on the Moon. The reaction locks half the hydrogen into methane, which is vented. That caps oxygen recovery from CO2 at about 50% ([ICES-2019-103](https://ntrs.nasa.gov/citations/20190030371)), or about 54% as operated on ISS ([ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679)). Open Moon covers the gap with oxygen made from regolith (M06). The methane need not be wasted: NASA has long noted it could be used for propulsion or broken down to recover hydrogen ([NASA NTRS](https://ntrs.nasa.gov/citations/20050110128)).

## How it works

The core reaction is CO2 + 4 H2 → CH4 + 2 H2O ([ICES-2019-103](https://ntrs.nasa.gov/citations/20190030371)). It gives off a lot of heat (ΔH about -165 kJ/mol), so the reactor may need active cooling. It typically runs at 150-350 °C, depending on the catalyst ([NASA NTRS](https://ntrs.nasa.gov/citations/20120004277)). Nickel or ruthenium-on-alumina catalysts are common ([Wikipedia](https://en.wikipedia.org/wiki/Sabatier_reaction)). Because no solid carbon forms, the reactor needs little maintenance ([NASA NTRS](https://ntrs.nasa.gov/citations/20120004277)).

The ISS assembly has a catalyst bed, a condensing heat exchanger, a phase separator to pull the liquid water out of the gas, and a piston compressor that stores CO2 from the scrubber ([NASA NTRS](https://ntrs.nasa.gov/citations/20100033195)). The water is cleaned by the station's water processor and sent to the oxygen generator; the methane is vented overboard ([NASA NTRS](https://ntrs.nasa.gov/citations/20150016512)).

| Parameter | Value | Source |
|---|---|---|
| Reaction | CO2 + 4 H2 → CH4 + 2 H2O | [ICES-2019-103](https://ntrs.nasa.gov/citations/20190030371) |
| Heat released | about 165 kJ/mol | [NTRS](https://ntrs.nasa.gov/citations/20120004277) |
| Typical temperature | 150-350 °C | [NTRS](https://ntrs.nasa.gov/citations/20120004277) |
| O2 recovery from CO2 | about 50% theoretical, ~54% as run on ISS | [ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679) |
| Design water output | up to 2,000 lb (about 900 kg) a year, 7-person-equivalent crew | [NTRS](https://ntrs.nasa.gov/citations/20100033195) |
| 1990s test unit (8 crew, with system impacts) | 497 kg, 395 W average | [ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679) |

The mass and power of the ISS flight unit itself are not given in these sources.

## Limitations and open issues

- **Half the hydrogen is lost.** Venting methane limits oxygen recovery to about 50%. Hydrogen is scarce on the Moon, so every vent is a real loss ([ICES-2019-103](https://ntrs.nasa.gov/citations/20190030371)).
- **Getting beyond 50% needs unproven hardware.** Methane post-processors, Bosch variants and electrolysis options were all rated TRL 3-5 in 2020 ([ICES-2020-108](https://ntrs.nasa.gov/citations/20205004679)). A plasma pyrolysis unit reaches only 75% theoretical hydrogen recovery ([NASA NTRS](https://ntrs.nasa.gov/citations/20100036570)).
- **Catalyst poisoning.** The CO2 feed comes straight from the scrubber with no contaminant removal, so trace organics concentrated in the sieve could degrade the catalyst ([NASA NTRS](https://ntrs.nasa.gov/citations/20140002591)).
- **Wearing parts.** NASA flagged CO2 compressor seal life, and the separator's tolerance to freezing and catalyst fines, as development risks ([NASA NTRS](https://ntrs.nasa.gov/citations/20100033195)).
- **Not tested in lunar conditions.** All flight experience is in microgravity on ISS. How the water separator and long dormant periods between crews behave on the Moon is not published.
- **No lunar mass or power figure.** No published value exists for a Sabatier sized for an Open Moon crew.
