---
slug: kilopower-krusty-fission-test
title: "Kilopower / KRUSTY fission test"
alternatives:
  - {name: "US Lunar Reactor-1 (SPARC) / Fission Surface Power", compare: "The flight successor that Kilopower fed into. It aims much higher (at least 20 kWe for at least 5 years) and switches to HALEU fuel and closed Brayton conversion, so only part of the KRUSTY evidence carries over directly.", status: "Draft procurement Aug 2026; no contract awarded and no hardware tested yet", url: "https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/"}
  - {name: "Multi-Mission Radioisotope Thermoelectric Generator (MMRTG)", compare: "Flight-proven and needs no reactor control, but gives only about 125 W at the start of a mission and depends on scarce plutonium-238. Good for small loads, far too small to run a base.", status: "Flight proven on Mars rovers", url: "https://en.wikipedia.org/wiki/Multi-mission_radioisotope_thermoelectric_generator"}
  - {name: "Vertical solar arrays with regenerative fuel cells", compare: "No nuclear fuel or launch approval needed, and solar towers are simpler to build. But power stops in shadow and during lunar night, so large energy storage is needed, which adds mass and complexity.", status: "NASA-funded solar tower prototypes (2022); fuel cell storage tested as a lab breadboard (2026)", url: "https://www.nasa.gov/news-release/three-companies-to-help-nasa-advance-solar-array-technology-for-moon/"}
  - {name: "Russia-China lunar reactor (ILRS)", compare: "A planned reactor for the Russian-Chinese lunar base. It would do the same job, but no design details or test results are public, so it cannot be compared on numbers.", status: "Announced in 2024 with a target of 2035; no published test hardware", url: "https://en.wikipedia.org/wiki/Nuclear_power_in_space"}
links:
  - {title: "Poston et al.: Results of the KRUSTY Nuclear System Test (Nuclear Technology, NTRS 20205009351)", url: "https://ntrs.nasa.gov/citations/20205009351", kind: paper, date: "Jun 2020"}
  - {title: "Gibson et al.: KRUSTY Nuclear Ground Test Results and Lessons Learned (NTRS 20180005435)", url: "https://ntrs.nasa.gov/citations/20180005435", kind: paper, date: "Jul 2018"}
  - {title: "NASA Release 18-031: Demonstration Proves Nuclear Fission System Can Provide Space Exploration Power", url: "https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/", kind: official, date: "May 2018"}
  - {title: "NASA Space Technology: Kilopower project page", url: "https://www.nasa.gov/directorates/spacetech/kilopower", kind: official, date: "Dec 2017"}
  - {title: "Gibson et al.: Development of NASA's Small Fission Power System for Science and Human Exploration (NTRS 20150011642)", url: "https://ntrs.nasa.gov/citations/20150011642", kind: paper, date: "Jun 2015"}
  - {title: "NASA TechPort: Kilopower Small Fission Technology project record", url: "https://techport.nasa.gov/projects/14405", kind: data, date: "2018"}
  - {title: "Wikipedia: Kilopower", url: "https://en.wikipedia.org/wiki/Kilopower", kind: wiki, date: "2026"}
  - {title: "Csank and Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", kind: official, date: "Apr 2022"}
  - {title: "Wikipedia: Nuclear power in space (Fission Surface Power section)", url: "https://en.wikipedia.org/wiki/Nuclear_power_in_space", kind: wiki, date: "2026"}
  - {title: "NewSpace Economy: What NASA's SPARC procurement reveals about Lunar Reactor-1 (secondary)", url: "https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/", kind: press, date: "Sep 2026"}
  - {title: "Wikipedia: Multi-mission radioisotope thermoelectric generator", url: "https://en.wikipedia.org/wiki/Multi-mission_radioisotope_thermoelectric_generator", kind: wiki, date: "2026"}
  - {title: "NASA Release 22-090: Three Companies to Help NASA Advance Solar Array Technology for Moon", url: "https://www.nasa.gov/news-release/three-companies-to-help-nasa-advance-solar-array-technology-for-moon/", kind: official, date: "Aug 2022"}
  - {title: "NASA NTRS 20260002730: Performance of a Regenerative Fuel Cell System for the Lunar Surface", url: "https://ntrs.nasa.gov/citations/20260002730", kind: official, date: "Apr 2026"}
---

## What it is

Kilopower was a NASA project to build a small, simple fission reactor for space. It aimed at systems that could scale from 1 to 10 kWe ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)). The project started in 2015. NASA's Glenn Research Center led it, with Marshall, the Department of Energy's NNSA, Los Alamos National Laboratory, the Y-12 National Security Complex and the Nevada National Security Site ([NASA](https://www.nasa.gov/directorates/spacetech/kilopower)). Before Kilopower, NASA saw a gap between radioisotope generators, which serve loads below about 1 kWe, and the larger power that future missions would need ([Gibson et al. 2015](https://ntrs.nasa.gov/citations/20150011642)).

KRUSTY (Kilopower Reactor Using Stirling TechnologY) was the project's nuclear ground test. It ran from November 2017 to March 2018 at the Device Assembly Facility in Nevada ([NASA](https://www.nasa.gov/directorates/spacetech/kilopower)). It ended with a 28-hour full-power run that simulated a mission: startup, ramp to full power, steady running and shutdown ([NASA release 18-031](https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/)). It was the first space fission reactor test in over 50 years ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)). The whole test was designed, built and run for less than $20 million ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)).

Kilopower itself has now ended. NASA's Fission Surface Power work builds on its results ([NASA](https://www.nasa.gov/directorates/spacetech/kilopower)). In 2026 that work became the "Lunar Reactor-1" procurement, which targets at least 20 kWe ([NewSpace Economy](https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/)).

## Why Open Moon uses it

Open Moon's power plan (milestone M04) needs steady power through the two-week lunar night and in shadowed craters, where solar power is hard to get ([NASA release 18-031](https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/)). Open Moon does not fly KRUSTY hardware. It uses KRUSTY as heritage: proof that a compact fission reactor with heat pipes and Stirling engines really works, behaves as predicted, and survives failures.

NASA's 2022 lunar reference design kept the same building blocks: sodium heat pipes and Stirling converters, in a 40 kWe system of about 10,000 kg ([Csank and Scott](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf)). Without KRUSTY, any lunar reactor would rest on paper studies alone. The base would then have to rely on solar arrays plus very large night-time storage.

## How it works

The core is a solid cast cylinder of highly enriched uranium alloyed with molybdenum, made in three sections ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)). The fuel is 93% uranium-235 and 7% molybdenum ([Wikipedia](https://en.wikipedia.org/wiki/Kilopower)). NASA describes it as about the size of a paper towel roll ([NASA release 18-031](https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/)). Beryllium oxide reflectors around it bounce neutrons back into the core. A flight unit would use a boron carbide rod in the centre to start, stop and set the temperature. In the test, the team moved the reflectors instead ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)).

Eight sodium heat pipes sit in grooves on the core. They carry heat to the power converters with no pumps. KRUSTY had two real Sunpower 80 W Stirling converters and six thermal simulators ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)). The reactor follows the load by itself, like a thermostat. If the engines draw more heat, the fuel cools and shrinks, and fission power rises ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)). During load swings of over 175%, the core temperature stayed within 4% of its 800 °C setpoint. Even a full shutdown of the converters caused only a 14 °C overshoot ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)).

| Specification | KRUSTY value |
|---|---|
| Thermal power | 1.5 to 5.0 kWt; design point 4 kWt at 800 °C ([Poston](https://ntrs.nasa.gov/citations/20205009351)) |
| Peak fuel temperature | about 880 °C ([Poston](https://ntrs.nasa.gov/citations/20205009351)) |
| Stirling output | about 90 We per converter; 183 We combined at most ([Poston](https://ntrs.nasa.gov/citations/20205009351), [Gibson](https://ntrs.nasa.gov/citations/20180005435)) |
| Efficiency | about 35% converter, about 25% system ([Poston](https://ntrs.nasa.gov/citations/20205009351)) |
| Startup to 800 °C | about 1.5 hours ([Gibson](https://ntrs.nasa.gov/citations/20180005435)) |
| Mass / fuel | 134 kg prototype with 28 kg of U-235 ([Wikipedia](https://en.wikipedia.org/wiki/Kilopower)) |
| Full-power run | 28 continuous hours ([Gibson](https://ntrs.nasa.gov/citations/20180005435)) |

The planned flight family ranged up to 10 kWe, running for at least 10 years ([NASA release 18-031](https://www.nasa.gov/news-release/demonstration-proves-nuclear-fission-system-can-provide-space-exploration-power/)).

## Limitations and open issues

- **Not a life test.** KRUSTY ran for only 28 hours. Long-term effects such as material creep and diffusion between metals still need study ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)).
- **Control rod never moved.** The flight design's boron carbide rod was not tested. Its long-term operation under radiation and protection against accidental movement still need proving ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)).
- **Low electrical output.** Only two small converters made about 180 We in total. A full 1 kWe system was never run on nuclear heat ([Gibson et al. 2018](https://ntrs.nasa.gov/citations/20180005435)).
- **Gravity and heat pipes.** The test heat pipes partly worked as thermosiphons in Earth gravity, and they struggled during startup. Flight heat pipes must be qualified for low gravity ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)).
- **Flight parts differ.** Flight conversion, heat rejection and shielding will be quite different. Launch and landing loads were only roughly considered ([Poston et al. 2020](https://ntrs.nasa.gov/citations/20205009351)).
- **Design has moved on.** KRUSTY used highly enriched uranium and Stirling engines. Lunar Reactor-1 now calls for HALEU fuel and closed Brayton conversion, so new testing will be needed ([NewSpace Economy](https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/)).
- **Cost of a flight unit not published.** Only the test cost (under $20 million) is public. No figure for a flight Kilopower unit has been published.
