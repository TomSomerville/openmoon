---
slug: rassor-2-0
title: "RASSOR 2.0"
alternatives:
  - {name: "NASA ISRU Pilot Excavator (IPEx)", compare: "The direct successor to RASSOR 2.0, using the same counter-rotating bucket drums at 50-70% of the volume and a 30 kg dry mass target. It is lighter and is being built with flight in mind, but it digs less per trip and is still a ground prototype.", status: "TRL-5 version about 95% designed and 90% fabricated as of June 2024; targets 10,000 kg at 42 kg/h over an 11-day mission; no flight booked", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf"}
  - {name: "Interlune / Vermeer helium-3 excavator", compare: "A much larger continuous excavator built to process regolith for helium-3. It is designed for far higher throughput, but it is a heavy industrial machine aimed at shallow harvesting, not a small robot for trenching, berms and feedstock delivery.", status: "Full-scale ground prototype unveiled May 2025; designed for 100 t of regolith per hour; not flown", url: "https://www.interlune.space/press-release/space-resources-company-interlune-unveils-full-scale-prototype-of-excavator-for-harvesting-helium-3-from-the-moon"}
  - {name: "Komatsu lunar construction machine (Japan Space Construction Innovation Project)", compare: "A lunar version of a conventional construction excavator, designed with digital-twin simulation. It would offer familiar earthmoving tools, but it relies on machine weight and ground contact for digging force, which RASSOR's opposed drums avoid.", status: "Research and simulation stage; Komatsu aims to complete project goals by the early 2030s", url: "https://komatsu.eu/en/campaign/lunar-excavator"}
links:
  - {title: "NASA KSC fact sheet: Regolith Advanced Surface Systems Operations Robot (RASSOR), NTRS 20150022134", url: "https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf", kind: official, date: "2015"}
  - {title: "Mueller et al., Design of an Excavation Robot: RASSOR 2.0 (ASCE Earth and Space 2016)", url: "https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf", kind: paper, date: "Apr 2016"}
  - {title: "NTRS record 20210011366: Design of an Excavation Robot: RASSOR 2.0", url: "https://ntrs.nasa.gov/citations/20210011366", kind: official, date: "Apr 2016"}
  - {title: "Mueller et al., Regolith Advanced Surface Systems Operations Robot (RASSOR), IEEE Aerospace Conference (first generation)", url: "https://ntrs.nasa.gov/citations/20130008972", kind: paper, date: "2013"}
  - {title: "US Patent 9,027,265: Zero horizontal reaction force excavator", url: "https://patents.google.com/patent/US9027265B1/en", kind: data, date: "May 2015"}
  - {title: "ICE-RASSOR: Intelligent Capabilities Enhanced RASSOR (NTRS 20205007299)", url: "https://ntrs.nasa.gov/citations/20205007299", kind: paper, date: "Sep 2020"}
  - {title: "Mass inferencing model creation and deployment to the RASSOR lunar excavation robot (NTRS 20210022473)", url: "https://ntrs.nasa.gov/citations/20210022473", kind: paper, date: "Oct 2021"}
  - {title: "ISRU Pilot Excavator bucket drum scaling (ASCE Earth and Space 2022)", url: "https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf", kind: paper, date: "2022"}
  - {title: "IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", kind: paper, date: "2024"}
  - {title: "NASA: NASA Kennedy digs latest robot test (RASSOR berm test)", url: "https://www.nasa.gov/image-article/nasa-kennedy-digs-latest-robot-test", kind: official, date: "Jun 2025"}
  - {title: "NASA Image Library: RASSOR builds a berm during a site preparation test, KSC-20250603-PH-FMX01_0086", url: "https://images.nasa.gov/details/KSC-20250603-PH-FMX01_0086", kind: data, date: "Jun 2025"}
  - {title: "NASA Kennedy Space Center video: NASA Developing Mining Robot for Moon, Mars", url: "https://www.youtube.com/watch?v=YWiRuyhjEZ8", kind: video, date: ""}
  - {title: "Wikipedia: Swamp Works", url: "https://en.wikipedia.org/wiki/Swamp_Works", kind: wiki, date: "2026"}
---

## What it is

RASSOR (Regolith Advanced Surface Systems Operations Robot) is a small digging robot built by [NASA Kennedy Space Center's Swamp Works](https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf). It was designed to answer one problem: on the Moon or Mars, a light robot does not weigh enough to push a blade or bucket into the ground. RASSOR gets around this with two opposing rotating drums that cancel out each other's digging forces. NASA patented the idea in May 2015 as a ["zero horizontal reaction force excavator"](https://patents.google.com/patent/US9027265B1/en).

The [first generation](https://ntrs.nasa.gov/citations/20130008972) was a lightweight proof-of-concept tested in lunar regolith simulant. RASSOR 2.0, described in a [2016 design paper](https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf), cut system mass by about 50% to 66 kg and doubled the regolith it can carry to 80 kg. The paper says a single unit can dig at least 2.7 t of regolith per day. A later NASA paper gives its [dry mass as 65 kg](https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf) and calls it a breadboard built from parts with proven paths to flight.

RASSOR 2.0 is a ground prototype. Its designers rated it [TRL 4](https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf), and NASA's [IPEx design paper](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf) also calls it the TRL-4 version of the concept. It has since been used for [machine-learning research](https://ntrs.nasa.gov/citations/20205007299) and, in May 2025, a [site preparation test](https://www.nasa.gov/image-article/nasa-kennedy-digs-latest-robot-test) where it built a three-foot berm of simulant to prove that a bucket-drum excavator can shape surface features.

## Why Open Moon uses it

Open Moon lists RASSOR 2.0 for light excavation in **M02 (site preparation)**: grading pads and roads, digging trenches and piling up berms that shield equipment from landing blast. It sits beside NASA's IPEx in the plan. RASSOR 2.0 is the larger, heavier, older design; IPEx is its [30 kg-class successor](https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf) built on the same drums.

NASA's original mission concept was to send RASSOR to the Moon for five years to [feed regolith to an oxygen plant](https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf). The fact sheet describes 35 trips with 20 kg loads every 24 hours, and says four units together could support 10 t of oxygen a year. That same job, delivering feedstock, matters for later Open Moon oxygen production.

Without a low-mass excavator, the base would have to land heavy Earth-style machines, which cost far more to deliver, or skip pads and berms. That would leave equipment exposed to rocket exhaust spray.

## How it works

RASSOR 2.0 has a compact wheeled chassis with two arms, one at each end. Each arm carries [two bucket drums](https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf), which are hollow cylinders with scoops around the outside. The front and rear drums spin in opposite directions, so their horizontal pushes cancel. Internal baffles keep soil inside the drum while it turns. When the drums are full, the robot drives back and dumps them into a hopper by spinning them the other way.

The design paper's concept of operations has the robot working 100 m from a lander. It mines for 16 hours, then recharges for 8. It can trench deeper than 1.0 m. The team chose wheels over the tracks used on RASSOR 1.5, because the drums cancel digging forces and remove the need for strong traction. If it gets stuck in loose soil, it can lower its arms so the drums share its weight, and it can use its arms and drums to right itself if it tips over.

| Specification | Value |
|---|---|
| Total mass | [66 kg](https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf) (65 kg dry in [a 2022 paper](https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf)) |
| Regolith payload | 80 kg across four drums |
| Excavation rate | At least 2.7 t per day |
| Energy use | 4 W per kg/h of excavation rate |
| Speed | 27 cm/s average, 56.5 cm/s maximum |
| Drums | 4, each with 8 scoops |
| Actuators | 10; shoulder actuator 644 N·m peak, 3.58 kg |
| Power bus | 48 V DC |
| Control | Teleoperated, with semi-autonomous "Auto Dig" and simulated autonomy (ROS, Gazebo) |

Later NASA work taught RASSOR to [estimate the mass in its drums](https://ntrs.nasa.gov/citations/20210022473) from motor data, with mean error under 7.5%, so it knows when to return and unload.

## Limitations and open issues

- **Never tested in vacuum or low gravity as a full system.** The 2016 paper rated it TRL 4. The planned [RASSOR 3.0](https://ntrs.nasa.gov/api/citations/20210011366/downloads/ASCE%202016%20RASSOR%202%20Final%20%206_8_2016.pdf) step to TRL 5 has instead been taken up by [IPEx](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf).
- **No flight version.** No lunar mission has been announced for RASSOR 2.0, and flight-qualified mass and power are not published.
- **Inconsistent figures.** Published mass is 65 or 66 kg. The fact sheet's 20 kg loads differ from the 2016 paper's 80 kg drum capacity.
- **Dust and thermal survival.** The design paper does not report testing of seals, actuators or electronics against lunar dust, vacuum or extreme cold.
- **Prototype shortcuts.** The team reported trouble with small electrical connectors, budget-limited stereo cameras and a 48 V bus that forced motor trade-offs.
- **Throughput.** At a few tonnes per day, it suits light site work. Large berms and pads would need several units working for a long time.
