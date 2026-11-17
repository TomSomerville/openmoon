---
slug: msolo-mass-spectrometer
title: "MSolo mass spectrometer"
alternatives:
  - {name: "ProSPA (ESA PROSPECT package)", compare: "A sealed-oven lab that heats drill samples up to 950 °C and analyses the gas with an ion trap and a magnetic sector mass spectrometer, so it can measure isotope ratios precisely. It is far more capable than MSolo for science, but heavier and more complex, and it has not flown yet.", status: "Being prepared for flight on Intuitive Machines' Nova-C lander under NASA CLPS, flight opportunity in 2027", url: "https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full"}
  - {name: "PITMS ion trap mass spectrometer (NASA Goddard / Open University / ESA)", compare: "An ion trap mass spectrometer built to measure lunar exosphere gases and surface water. It sniffs the open environment rather than drill cuttings. Like MSolo it mostly saw its own lander's outgassing in flight.", status: "Flew on Astrobotic Peregrine (Jan 2024); worked in cislunar space but never reached the Moon", url: "https://iopscience.iop.org/article/10.3847/PSJ/ad9927"}
  - {name: "TRITON time-of-flight mass spectrometer (JAXA, LUPEX REIWA suite)", compare: "A triple-reflection time-of-flight mass spectrometer with a wider 1-200 amu range that analyses gas from heated regolith samples on the LUPEX rover. It works on sealed, heated samples rather than open cuttings, which should reduce contamination, but it is still in development.", status: "Engineering model stage; no flight yet", url: "https://space-plasma.exst.jaxa.jp/triton-en"}
links:
  - {title: "NASA NTRS: PRIME-1 MSolo overview and results (LSSW presentation)", url: "https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf", kind: official, date: "Apr 2026"}
  - {title: "NASA NTRS: VIPER's Mass Spectrometer observing lunar operations (MSolo)", url: "https://ntrs.nasa.gov/citations/20240015183", kind: official, date: "May 2025"}
  - {title: "NASA NTRS: Mass Spectrometer Observing Lunar Operations (MSoLo), ASMS 2023", url: "https://ntrs.nasa.gov/citations/20230007808", kind: official, date: "2023"}
  - {title: "NASA: NASA's lunar drill technology passes tests on the Moon", url: "https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/", kind: official, date: "Apr 2025"}
  - {title: "NASA Science: PRIME-1 (IM-2) CLPS delivery", url: "https://science.nasa.gov/lunar-science/clps-deliveries/prime-1-im", kind: official, date: ""}
  - {title: "NASA Images: Final assembly of the MSOLO-2 flight instrument at Kennedy", url: "https://images.nasa.gov/details/KSC-20230621-PH-KLS01_0034", kind: official, date: "Jun 2023"}
  - {title: "INFICON: INFICON technology returning to the Moon", url: "https://www.inficon.com/en/news/inficon-technology-returning-to-the-moon", kind: official, date: ""}
  - {title: "INFICON: Revisiting the historic southernmost lunar landing", url: "https://www.inficon.com/en/news/revisiting-the-historic-southernmost-lunar-landing", kind: official, date: "Mar 2026"}
  - {title: "NASA: NASA selects Blue Origin to deliver VIPER rover to Moon's south pole", url: "https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/", kind: official, date: "Sep 2025"}
  - {title: "Cohen et al.: The Peregrine Ion Trap Mass Spectrometer (PITMS), results from a CLPS-delivered mass spectrometer", url: "https://iopscience.iop.org/article/10.3847/PSJ/ad9927", kind: paper, date: "Jan 2025"}
  - {title: "Trautner et al.: PROSPECT, a sample acquisition and analysis package for lunar science and exploration", url: "https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full", kind: paper, date: "Apr 2024"}
  - {title: "ESA: European drill and mini lab secure ride to the Moon", url: "https://esa.int/Science_Exploration/Human_and_Robotic_Exploration/European_drill_and_mini_lab_secure_ride_to_the_Moon", kind: official, date: "Aug 2024"}
  - {title: "Wikipedia: IM-2", url: "https://en.wikipedia.org/wiki/IM-2", kind: wiki, date: ""}
  - {title: "Wikipedia: Residual gas analyzer", url: "https://en.wikipedia.org/wiki/Residual_gas_analyzer", kind: wiki, date: ""}
  - {title: "Wikipedia: Quadrupole mass analyzer", url: "https://en.wikipedia.org/wiki/Quadrupole_mass_analyzer", kind: wiki, date: ""}
---

## What it is

MSolo (Mass Spectrometer Observing Lunar Operations) is a small gas analyser built to tell which gases come off lunar soil. It was developed at [NASA Kennedy Space Center](https://ntrs.nasa.gov/citations/20240015183). It is a modified commercial off-the-shelf (COTS) instrument. The core is INFICON's [Transpector MPH residual gas analyzer](https://www.inficon.com/en/news/inficon-technology-returning-to-the-moon), ruggedized for launch, vacuum and lunar temperatures. INFICON says the work builds on [more than 14 years of collaboration](https://www.inficon.com/en/news/inficon-technology-returning-to-the-moon) with Kennedy.

MSolo first reached the Moon on the PRIME-1 payload aboard Intuitive Machines' Athena lander (IM-2). Athena landed on [6 March 2025 about 500 m from its target near Mons Mouton](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). It came to rest [on its side inside a crater](https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/), so a planned 10-day mission became about 10 to 12 hours. MSolo [started right up and performed well](https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/). On the surface it was powered on 3 times and captured [43 scans (40 complete)](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). INFICON counts [136 full spectra](https://www.inficon.com/en/news/revisiting-the-historic-southernmost-lunar-landing) across transit and surface. But the gases it saw were all [anthropogenic](https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/): Earth air, Earth water and lander propellant vents. NASA states PRIME-1 [could not meet its science goals](https://science.nasa.gov/lunar-science/clps-deliveries/prime-1-im).

A second unit flies on NASA's VIPER rover. NASA's MSolo team describes it as [one of VIPER's analytical instruments](https://ntrs.nasa.gov/citations/20240015183). A photo shows the [MSOLO-2 flight instrument in final assembly in June 2023](https://images.nasa.gov/details/KSC-20230621-PH-KLS01_0034). VIPER now has a delivery option on Blue Origin's Blue Moon MK1, [in late 2027](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/). INFICON also says an MSolo will fly on [Intuitive Machines' IM-5 to Mons Malapert](https://www.inficon.com/en/news/inficon-technology-returning-to-the-moon). It did not give a firm date.

## Why Open Moon uses it

Milestone M01 (prospecting) has to find out how much water ice lies in the polar soil, and in what form. Neutron spectrometers only show hydrogen. A mass spectrometer shows which molecules are actually there: water, CO2, methane and others. On a drill, MSolo was set up to [examine drill cuttings for subsurface volatiles](https://science.nasa.gov/lunar-science/clps-deliveries/prime-1-im). Open Moon's prospector rover carries an MSolo-class instrument beside a 1 m drill.

It is a good fit because it is cheap and already flown. The team's main conclusion from IM-2 is that a [space-hardened COTS instrument can work well in space and on the lunar surface](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). It also says development can use flight-like hardware at commercial-level costs. Its interface plugs into [practically any CLPS host with a 28 V bus and an RS-422 serial link](https://ntrs.nasa.gov/citations/20240015183). Without it, prospecting would measure hydrogen but not identify the gases, and the plan's water-processing design would rest on guesses.

## How it works

MSolo has three main parts: the sensor, the avionics, and a [calibration gas system](https://ntrs.nasa.gov/citations/20240015183). In the sensor, electrons ionize gas molecules. A [quadrupole mass filter](https://en.wikipedia.org/wiki/Quadrupole_mass_analyzer) then lets through only ions of one mass-to-charge ratio at a time. A detector counts them. Sweeping the filter gives a spectrum, which works the same way as an industrial [residual gas analyzer](https://en.wikipedia.org/wiki/Residual_gas_analyzer). A radiation-tolerant computer running Linux controls the instrument. The calibration tank holds [3% hydrogen, 10% krypton, 10% xenon and nitrogen](https://ntrs.nasa.gov/citations/20240015183), released on demand to check tuning.

On a drill mission, the drill brings cuttings to the surface. Ice in the cuttings warms and releases gas, and MSolo [detects and quantifies those gases](https://ntrs.nasa.gov/citations/20240015183). Targets include water and hydrogen and oxygen isotope ratios (D/H, 18O/16O).

| Specification | Value |
|---|---|
| Base instrument | INFICON Transpector MPH (COTS) |
| Ionization | Electron impact, 70 eV (40 eV low mode) |
| Mass range | m/z 1 to 100, unit mass resolution |
| Detectors | Faraday cup or continuous dynode electron multiplier |
| Sensitivity | about 4E-5 A/Torr for nitrogen (Faraday cup) |
| Size | 18 x 21 x 48 cm |
| Mass | 4.8 kg |
| Power | 30 W nominal, 40 W peak, at 28 V |
| Input voltage | 22 to 33.6 V |

Source: [NASA MSolo VIPER paper, Table 1](https://ntrs.nasa.gov/citations/20240015183).

## Limitations and open issues

- **Contamination from home.** On IM-2, Earth air was still in the spectra [days after launch because the sensor was not hermetically sealed](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). The team says baking out the instrument or running it long enough is needed for best sensitivity.
- **Lander outgassing.** Athena vented its methane and oxygen tanks [while MSolo was on](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). PITMS on Peregrine also saw [water outgassing much higher than other planetary spacecraft](https://iopscience.iop.org/article/10.3847/PSJ/ad9927). Open Moon's answer is to sample away from the lander.
- **Never measured lunar ice.** No MSolo has yet analysed drill cuttings from an icy site. The team believes it [would have seen water above background](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf) in an icy region, but this is based on lab results.
- **Sensitivity loss after landing.** Surface sensitivity was lower than in transit, [possibly from dust](https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf). The cause is not known.
- **Limited range and resolution.** Mass range stops at m/z 100 with unit resolution. It cannot match the isotope precision of a lab like [ProSPA](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full).
- **Cold operation.** Before the build, little was known about how a COTS system would behave at lunar-like [temperatures from 70 to -45 °C](https://ntrs.nasa.gov/citations/20230007808). Survival inside permanently shadowed regions has not been tested. The extra heating it would need there is not published.
- **Schedule.** The next flights depend on VIPER's [optional delivery](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/) and on IM-5, which has no firm public date.
