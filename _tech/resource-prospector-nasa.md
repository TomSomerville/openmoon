---
slug: resource-prospector-nasa
title: "Resource Prospector drill-to-oven system (NASA)"
alternatives:
  - {name: "Curiosity sampling system and SAM (NASA, Mars)", compare: "A scoop and a drill both feed one handling device on the arm, which sieves and portions the sample and drops it into ovens that heat to about 1,000 °C. It is the only flown rover with both a scoop and a drill feeding ovens, but its samples are milligrams of warm, dry Martian soil.", url: "https://webarchive.library.unt.edu/web/20130214054221/http://msl-scicorner.jpl.nasa.gov/samplingsystem"}
  - {name: "Phoenix Robotic Arm and TEGA ovens (NASA, Mars)", compare: "A lander arm with a bladed scoop and a powered rasp for icy soil, feeding eight small ovens. It flew in 2008, but icy samples congealed in the scoop and clumpy soil stuck on the oven screens.", url: "https://www-robotics.jpl.nasa.gov/media/documents/2007JE003030.pdf"}
  - {name: "ProSEED drill and ProSPA lab (ESA PROSPECT)", compare: "A 1 m drill that hands small samples to up to 25 single-use ovens heated to 950 °C, with two mass spectrometers. More precise, but it heats tiny samples and is fixed to a lander. Booked on IM-4 in 2027.", url: "https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full"}
  - {name: "LUWEX extraction test rig (DLR-led, EU-funded)", compare: "A stirred crucible that took almost 65% of the water out of icy simulant at about 110 K in vacuum. It handles bulk soil for water production rather than prospecting, and it is a lab rig (TRL 4–5).", url: "https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions"}
links:
  - {title: "NASA NTRS: Colaprete et al., Resource Prospector instrumentation for lunar volatiles prospecting, sample acquisition and processing", url: "https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf", kind: official, date: "Apr 2016"}
  - {title: "NASA NTRS: Paz, Environmental testing of the OVEN system for lunar water extraction and prospecting", url: "https://ntrs.nasa.gov/citations/20210013522", kind: official, date: "2021"}
  - {title: "NASA NTRS: Kleinhenz et al., Volatiles loss from water bearing regolith simulant at lunar environments", url: "https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf", kind: official, date: "Apr 2018"}
  - {title: "NASA NTRS: Paz & Oryshchyn, OVEN poster", url: "https://ntrs.nasa.gov/citations/20140017042", kind: official, date: "Nov 2014"}
  - {title: "NASA NTRS: Paz et al., RESOLVE OVEN field demonstration unit for lunar resource extraction", url: "https://ntrs.nasa.gov/api/citations/20130000835/downloads/20130000835.pdf", kind: official, date: "2012"}
  - {title: "Captain (NASA KSC): Instrumentation for lunar volatile analysis (12th EuroHEMS workshop)", url: "https://www.hems-workshop.org/12thWS_EUROHEMS/Presentations/Captain.pdf", kind: official, date: "2019"}
  - {title: "Spaceflight Now: NASA cancels lunar rover, shifts focus to commercial Moon landers", url: "https://spaceflightnow.com/2018/05/01/nasa-cancels-lunar-rover-shifts-focus-to-commercial-moon-landers/", kind: press, date: "May 2018"}
  - {title: "NASA Images: Resource Prospector mobility test at Kennedy", url: "https://images.nasa.gov/details/KSC-20170628-PH_KLS01_0073", kind: official, date: "Jun 2017"}
---

## What it is

Resource Prospector (RP) was a NASA rover meant to prospect for water ice at a lunar pole. Its chain went from drill to oven to gas analyser. A 1 m drill lifted soil and brushed it ["directly into a cup/oven"](https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf). The OVEN (Oxygen and Volatile Extraction Node) weighed and sealed the sample and heated it. The LAVA instrument then identified and measured the gases.

NASA headquarters told the mission's managers on 23 April 2018 to end development of the rover by the end of May. NASA said selected instruments would continue toward [commercial landers](https://spaceflightnow.com/2018/05/01/nasa-cancels-lunar-rover-shifts-focus-to-commercial-moon-landers/). The OVEN is [not part of any current prospecting mission](https://ntrs.nasa.gov/citations/20210013522).

## Why Open Moon uses it

Open Moon's prospector rover (C01.1) scoops loose soil, drills ice-cemented ground into cuttings, and bakes both in a sealed chamber to measure the water that comes out. RP is the closest lunar design to that. It is the only lunar polar rover designed to feed drill cuttings straight into a sealed oven, and it was built and tested as hardware. Open Moon copies its delivery method, its weigh-seal-heat sequence and its heating steps, and scales up the crucible.

## How it works

The [OVEN](https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf):

| Specification | Value |
|---|---|
| Sample | 12 cc of regolith from the drill |
| Steps | Weighs the sample, seals it in the reactor, heats it, passes the gases to LAVA, discards the sample |
| Heating | 150 °C, 350 °C and 450 °C |
| Reuse | The crucible is reused after the sample is discarded |
| Mass | About 12.5 kg |
| Power | More than 50 W steady state |

An earlier NASA poster says the OVEN heats to [at least 150 °C for volatile analysis and as high as 900 °C](https://ntrs.nasa.gov/citations/20140017042) for hydrogen reduction. It says the crucible can be used more than once.

LAVA measured the gas by sending it to a [known volume held warm to stop condensation](https://www.hems-workshop.org/12thWS_EUROHEMS/Presentations/Captain.pdf) and working out the amount from the ideal gas law. It then diluted a gas sample and analysed it by GC-MS. Evolved water was also to be [condensed and photographed](https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf).

The OVEN went through two rounds of random vibration tests. One was stand-alone at NASA Johnson, and one was mounted on RP's mobile platform. It survived both without damage. It also [worked in thermal vacuum from −50 to 75 °C](https://ntrs.nasa.gov/citations/20210013522).

## Limitations and open issues

- **Never flew.** The rover was cancelled in 2018, so no part of this chain has worked on the Moon.
- **Water is lost before sealing.** In NASA Glenn vacuum tests it took [about 5 minutes to brush a sample into the crucible and seal it](https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf). Samples from 4.5 wt% soil lost about 30% of their water, and samples from 0.8 wt% soil about 80%. The authors found that agitating the sample during delivery has a significant impact.
- **Small samples.** 12 cc gives milligrams to a few grams of water. Open Moon's 250 cm³ chamber is about 20 times larger and has not been built (plan design).
- **Reuse limits not published.** No rated number of crucible or seal reuses was found. The 2012 field prototype carried [up to 50 disposable seals](https://ntrs.nasa.gov/api/citations/20130000835/downloads/20130000835.pdf).
- **Not tested at PSR cold.** The thermal-vacuum demonstration covered −50 to 75 °C. Permanently shadowed crater floors are much colder.
