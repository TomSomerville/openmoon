---
slug: nasa-isru-pilot-excavator-ipex
title: "NASA ISRU Pilot Excavator (IPEx)"
alternatives:
  - {name: "RASSOR 2.0", compare: "The direct predecessor of IPEx, also built at NASA Kennedy, using the same counter-rotating bucket drums. It is larger (65 kg dry against a 30 kg target for IPEx) and is a TRL 4 breadboard, so it is a fallback design rather than a better one.", status: "TRL 4 breadboard; ground-tested for hundreds of hours; no flight plan", url: "https://ntrs.nasa.gov/citations/20150022134"}
  - {name: "Interlune / Vermeer excavator and site-preparation tool", compare: "A commercial continuous-motion excavator built for very large throughput to harvest helium-3, with a rover-mounted site-preparation tool planned. Much bigger in scale than IPEx, but younger, with little published engineering data.", status: "Full-scale ground prototype unveiled May 2025; NASA STTR Phase I ($150,000) in 2026; mission-ready site-preparation tool targeted for 2028", url: "https://www.interlune.space/press-release/interlune-and-vermeer-expand-strategic-partnership-to-build-essential-moon-base-infrastructure"}
  - {name: "Starpath Robotics excavation rover", compare: "A four-wheeled commercial rover with a dual drum-barrel scraper that mines and hauls regolith, similar in concept to IPEx. It is aimed at ice mining for propellant; performance figures are not published.", status: "Second place in NASA's Break the Ice Lunar Challenge (June 2024); tested in a NASA Marshall thermal vacuum chamber in 2025", url: "https://www.nasa.gov/centers-and-facilities/marshall/california-teams-win-1-5-million-in-nasas-break-the-ice-lunar-challenge"}
  - {name: "Terra Engineering Fracture rover", compare: "Winner of NASA's Break the Ice Lunar Challenge, designed to cross rocky terrain and survive south-pole conditions. NASA has not published its excavation method or rates, so it cannot yet be compared on numbers.", status: "Challenge winner (June 2024); no flight plan announced", url: "https://www.nasa.gov/centers-and-facilities/marshall/california-teams-win-1-5-million-in-nasas-break-the-ice-lunar-challenge"}
links:
  - {title: "NASA: ISRU Pilot Excavator (IPEx) project page", url: "https://www.nasa.gov/isru-pilot-excavator/", kind: official, date: "Nov 2026"}
  - {title: "Schuler et al., ISRU Pilot Excavator (IPEx) TRL 5 Design Overview (ASCEND 2024), NTRS", url: "https://ntrs.nasa.gov/citations/20240008162", kind: paper, date: "Aug 2024"}
  - {title: "IPEx TRL 5 Design Overview, full paper (PDF)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", kind: paper, date: "Aug 2024"}
  - {title: "Schuler et al., ISRU Pilot Excavator: Bucket Drum Scaling Experimental Results (ASCE Earth and Space 2022)", url: "https://ntrs.nasa.gov/citations/20210025846", kind: paper, date: "Apr 2022"}
  - {title: "Design and Testing of TRL5 IPEx Actuators (IEEE Aerospace 2025), NTRS", url: "https://ntrs.nasa.gov/citations/20250000003", kind: paper, date: "Mar 2025"}
  - {title: "The IPEx Autonomy Test-Site: Terrestrial Testing of Autonomous Excavation in Lunar South Pole Conditions (IEEE Aerospace 2025), NTRS", url: "https://ntrs.nasa.gov/citations/20250000128", kind: paper, date: "Mar 2025"}
  - {title: "ISRU Pilot Excavator Wheel Testing in Lunar Regolith Simulant (ASCE Earth and Space 2024), NTRS", url: "https://ntrs.nasa.gov/citations/20240001016", kind: paper, date: "Apr 2024"}
  - {title: "ISRU Pilot Excavator: Development of Autonomous Excavation Algorithms (Space Resources Roundtable 2022), NTRS", url: "https://ntrs.nasa.gov/citations/20220005125", kind: paper, date: "2022"}
  - {title: "NASA: IPEx autonomy testing in a blacked-out facility", url: "https://www.nasa.gov/image-article/ipex-autonomy-testing/", kind: official, date: "Mar 2024"}
  - {title: "NASA Image Library: IPEx simulated lunar mission at Kennedy Space Center", url: "https://images.nasa.gov/details/KSC-20240830-PH-FMX01_0147", kind: official, date: "Aug 2024"}
  - {title: "NASA: IPEx TRL 5 demonstration, narrated video", url: "https://images-assets.nasa.gov/video/IPEx%20TRL%205%20Demo%20Narrated/IPEx%20TRL%205%20Demo%20Narrated~large.mp4", kind: video, date: "2024"}
  - {title: "NASA: Lunar Autonomy Challenge (digital twin of IPEx)", url: "https://www.nasa.gov/directorates/stmd/student-lunar-autonomy-challenge/", kind: official, date: "Nov 2024"}
  - {title: "NASA NTRS 20150022134: RASSOR 2.0", url: "https://ntrs.nasa.gov/citations/20150022134", kind: paper, date: "2015"}
  - {title: "Military and Aerospace Electronics: Starpath tests lunar excavation rover at NASA Marshall", url: "https://www.militaryaerospace.com/home/news/55319890/starpath-tests-lunar-excavation-rover-at-nasa-marshall", kind: press, date: "Sep 2025"}
  - {title: "Interlune: NASA STTR project for lunar trenching and excavation technology", url: "https://www.interlune.space/press-release/interlune-announces-details-of-nasa-sttr-project-to-advance-scalable-multipurpose-lunar-trenching-and-excavation-technology", kind: official, date: "Feb 2026"}
---

## What it is

IPEx is a small robotic excavator that NASA's Kennedy Space Center is developing to dig large amounts of lunar regolith. NASA calls it both a bulldozer and a dump truck. It is funded by NASA's Space Technology Mission Directorate through the Game Changing Development program ([ASCEND 2024 paper](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf)). On its current project page NASA now calls it the "Infrastructure Pilot Excavator" ([NASA](https://www.nasa.gov/isru-pilot-excavator/)).

IPEx grew out of RASSOR, an earlier Kennedy robot that proved the bucket-drum idea at TRL 4. RASSOR 2.0 weighs 65 kg dry. IPEx targets 30 kg dry, scaled to roughly 50–70% of RASSOR's size ([bucket drum scaling paper](https://ntrs.nasa.gov/citations/20210025846)). The goal is to dig 10,000 kg of regolith at 42 kg/h and drive a total of 70 km over an 11-day mission at the lunar south pole ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)). For comparison, NASA missions so far have excavated only tens of kilograms.

By June 2024 the TRL 5 version was about 95% designed and 90% built. It is being taken toward a TRL 6 "flight-ready" state for a demonstration mission that is "currently unmanifested" ([ASCEND 2024](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf)). The TRL 5 robot ran a simulated lunar mission in a Kennedy testbed in August 2024 ([NASA Image Library](https://images.nasa.gov/details/KSC-20240830-PH-FMX01_0147), [video](https://images-assets.nasa.gov/video/IPEx%20TRL%205%20Demo%20Narrated/IPEx%20TRL%205%20Demo%20Narrated~large.mp4)). NASA has announced no launch date ([NASA](https://www.nasa.gov/isru-pilot-excavator/)).

## Why Open Moon uses it

Open Moon uses IPEx-class excavators as the main diggers in [M05, site preparation](/milestones/m05-site-prep/). They grade roads, build berms around landing pads and the reactor, and stockpile regolith for oxygen extraction and sintered pads. M05 plans a fleet of four excavators.

The digging rate matters beyond M05. NASA designed IPEx to feed a follow-on "ISRU Pilot Plant": making 1,000 kg of oxygen needs 10,000 kg of regolith ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)). Without a light, reliable excavator, pads, berms and oxygen production would have to wait for heavier machines that cost much more to land.

## How it works

A normal Earth excavator uses its own weight to push against the soil. On the Moon, a light robot has too little weight for that. IPEx instead uses bucket drums: hollow cylinders with scoops around the outside. Two pairs of drums dig at the same time in opposite directions, so their digging forces mostly cancel out. Regolith falls into the drum and is held by internal baffles. Running the drum backwards dumps it ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)).

The robot has four subsystems ([ASCEND 2024](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf)):

- **Regolith delivery:** drums, arms and their actuators. Each dig cycle carries up to 30 kg, with 15 kg as the minimum for success.
- **Mobility:** four wheels with skid steering and no suspension, using rigid aluminium wheels after testing ten wheel designs on simulant ([wheel tests](https://ntrs.nasa.gov/citations/20240001016)).
- **Cameras and dust mitigation:** cameras for visual navigation, with electrodynamic dust shields on the lenses that can be jettisoned if they fail.
- **Thermal control:** while digging, a cover protects the radiator from dust and waste heat melts a 2.5 kg phase-change pack. IPEx then stops, opens the cover and radiates the heat away.

| Specification | Value |
|---|---|
| Dry mass (target) | 30 kg class |
| Mission excavation target | 10,000 kg in 11 days |
| Excavation rate (target) | 42 kg/h |
| Load per dig cycle | Up to 30 kg (15 kg minimum) |
| Driving speed | 30 cm/s nominal |
| Total drive distance | Up to 70 km |
| Obstacles and slopes | Rocks up to 7.5 cm; slopes up to 15° |
| Phase-change heat store | 300.5 kJ, n-hexadecane, melts at 18 °C |

Source for the table: [ASCEND 2024](https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf). Its actuators use frameless motors and harmonic gears shared across the wheels, arms and drums, built strong enough to work in Earth gravity during testing.

Autonomy is tested in a 21.3 × 33.5 m enclosed site at Kennedy that copies the low sun and long shadows of the south pole ([autonomy test-site paper](https://ntrs.nasa.gov/citations/20250000128), [NASA](https://www.nasa.gov/image-article/ipex-autonomy-testing/)). Student teams also wrote navigation software for a digital twin of IPEx in NASA's [Lunar Autonomy Challenge](https://www.nasa.gov/directorates/stmd/student-lunar-autonomy-challenge/).

## Limitations and open issues

- **No flight.** The demonstration mission is unmanifested and has no launch date ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162), [NASA](https://www.nasa.gov/isru-pilot-excavator/)).
- **Rates are design targets.** The 42 kg/h and 10 t figures are goals for a notional mission, not measurements on the Moon ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)). NASA's project page describes the 10,000 kg as "in a single lunar day", which is not the same framing as the paper's 11 days ([NASA](https://www.nasa.gov/isru-pilot-excavator/)).
- **Actuator reliability.** All three actuator types passed accelerated life testing, but only the bucket drum actuator finished the mission-sequence test without a restart. The tests found several failure modes that led to design changes ([actuator paper](https://ntrs.nasa.gov/citations/20250000003)).
- **Dust.** Cameras and radiator depend on dust shields and covers that have been tested only on the ground.
- **Scale.** A 30 kg robot moving about 10 t per mission is far below what full-scale ISRU and construction will need: thousands of tonnes per year ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)).
- **Avionics and software** are not covered in the TRL 5 paper and were left for a separate publication ([ASCEND 2024](https://ntrs.nasa.gov/citations/20240008162)).
- **Not published:** a final as-built mass, power use, and unit cost.
