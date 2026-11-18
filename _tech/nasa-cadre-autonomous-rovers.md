---
slug: nasa-cadre-autonomous-rovers
title: "NASA CADRE autonomous rovers"
alternatives:
  - {name: "Delay-tolerant teleoperation from Earth", compare: "People on Earth drive each rover through a 4-8 second delay instead of robots planning together on the Moon. It needs no new autonomy software, but it is slower, tiring for operators and needs one driver per vehicle.", status: "NASA simulator studies in 2023 had operators finish traverses at 0, 4, 6 and 8 s delay; not yet flown on a lunar rover.", url: "https://ntrs.nasa.gov/citations/20240001217"}
  - {name: "Lunar Outpost Pegasus LTV (autonomous driving mode)", compare: "One large crew rover that can drive itself, rather than a team of small cooperating robots. It can carry people and cargo, but it does not show many robots sharing maps and splitting up tasks.", status: "NASA LTV award in 2026; flight units to be qualified over the next 18 months.", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/"}
  - {name: "NASA VIPER", compare: "A single, much larger science rover with a 1 m drill, planned for a 100-day mission. It has more capable instruments but no multi-robot teamwork, and it is operated closely from the ground.", status: "To be delivered to Mons Mouton by a Blue Origin Blue Moon MK-1 lander (announced Sep 2025).", url: "https://science.nasa.gov/mission/viper/"}
  - {name: "Lunar Outpost MAPP rover", compare: "A commercial small rover offered as a service to carry customer payloads. It is a single vehicle, not a cooperating team, but it can be bought rather than built.", status: "Commercial product; a Lunar Outpost rover carries Lunar Vertex instruments on the same IM-3 flight.", url: "https://www.lunaroutpost.com/mapp"}
links:
  - {title: "NASA: Cooperative Autonomous Distributed Robotic Exploration (CADRE) project page", url: "https://www.nasa.gov/cooperative-autonomous-distributed-robotic-exploration-cadre", kind: official, date: "Jul 2025"}
  - {title: "NASA/JPL: NASA's mini rover team is packed for lunar journey", url: "https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey", kind: official, date: "Feb 2025"}
  - {title: "JPL Robotics: CADRE flight project page", url: "https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/", kind: official, date: "2024"}
  - {title: "JPL Robotics: CADRE mission overview", url: "https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/cadre-mission-overview/", kind: official, date: "2024"}
  - {title: "NASA Photojournal PIA26164: NASA's CADRE rovers take first autonomous drive", url: "https://science.nasa.gov/photojournal/nasas-cadre-rovers-take-first-autonomous-drive/", kind: official, date: "Mar 2024"}
  - {title: "Rabideau et al.: Planning, scheduling, and execution on the Moon: the CADRE technology demonstration mission (AAMAS 2025)", url: "https://arxiv.org/abs/2502.14803", kind: paper, date: "Feb 2025"}
  - {title: "JPL AI group: CADRE slides, MASSpace '24 workshop", url: "https://ai.jpl.nasa.gov/public/documents/presentations/CADRE-AAMAS-Slides.pdf", kind: paper, date: "2024"}
  - {title: "NASA launch schedule (Moon Base: Intuitive Machines IM-3, early 2027)", url: "https://www.nasa.gov/event-type/launch-schedule/", kind: official, date: "Nov 2026"}
  - {title: "Wikipedia: IM-3", url: "https://en.wikipedia.org/wiki/IM-3", kind: wiki, date: "Nov 2026"}
  - {title: "Wikipedia: Reiner Gamma", url: "https://en.wikipedia.org/wiki/Reiner_Gamma", kind: wiki, date: "2026"}
  - {title: "NTRS 20230000531: Selection and characterization of the landing site for CLPS mission CP-11 (LPSC 2023)", url: "https://ntrs.nasa.gov/citations/20230000531", kind: paper, date: "Mar 2023"}
  - {title: "NASA: Commercial Lunar Payload Services (CLPS)", url: "https://www.nasa.gov/commercial-lunar-payload-services/", kind: official, date: "Nov 2026"}
  - {title: "NTRS 20240001217: LTV remote teleoperation studies under four lunar communication latencies", url: "https://ntrs.nasa.gov/citations/20240001217", kind: official, date: "2024"}
---

## What it is

CADRE (Cooperative Autonomous Distributed Robotic Exploration) is a NASA technology demonstration of three small rovers that work as a team. The goal is to show that a group of robots can [collaborate to gather data without direct commands from mission controllers on Earth](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey). NASA describes the rovers as "suitcase-size". Each has an [onboard computer, a wireless radio and a stereo camera](https://www.nasa.gov/cooperative-autonomous-distributed-robotic-exploration-cadre). NASA calls them [the latest version of its A-PUFFER technology](https://www.nasa.gov/cooperative-autonomous-distributed-robotic-exploration-cadre). NASA has not published a mass or exact dimensions on the pages cited here.

JPL manages CADRE for NASA's Game Changing Development program. [Motiv Space Systems built key hardware, Clemson University contributed research, and NASA Glenn and Ames supported the project](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey). The rovers completed their [first autonomous team drive in a JPL clean room in December 2023](https://science.nasa.gov/photojournal/nasas-cadre-rovers-take-first-autonomous-drive/). Hardware build and testing ended in February 2024. The rovers were [shipped to Intuitive Machines in Houston and arrived on 9 February 2025](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey).

CADRE will fly on Intuitive Machines' IM-3 Nova-C lander under NASA's [CLPS](https://www.nasa.gov/commercial-lunar-payload-services/) program. It will land at [Reiner Gamma](https://en.wikipedia.org/wiki/Reiner_Gamma), a lunar swirl on the western near side. IM-3 has slipped several times. NASA's [launch schedule now lists it for early 2027](https://www.nasa.gov/event-type/launch-schedule/), and [Wikipedia gives NET Q1 2027 on a Falcon 9](https://en.wikipedia.org/wiki/IM-3).

## Why Open Moon uses it

Open Moon lists CADRE in milestone M07 (surface mobility) as heritage for multi-robot autonomy. M07 expects rovers and utility robots to build the base before any crew arrives (Phase 1). CADRE is the first flight test of robots that [share maps, split up work and decide what to do as a team](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/). NASA says success [could lead to teams of robots supporting astronauts and taking distributed measurements](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey).

Open Moon does not plan to buy CADRE rovers. It uses the software ideas and flight data. Without CADRE, fleets of utility robots would rely on [Earth teleoperation through a 4-8 second delay](https://ntrs.nasa.gov/citations/20240001217), with one operator per vehicle. NASA's own project page notes that [waiting for ground control "eats up precious time"](https://www.nasa.gov/cooperative-autonomous-distributed-robotic-exploration-cadre).

## How it works

The team is three rovers plus a base station on the lander. Each rover is lowered [by tether from the lander to the surface](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey). The base station is [powered by the lander and has no battery](https://arxiv.org/abs/2502.14803). It acts as the link to Earth and helps with computing.

CADRE runs [two experiments](https://arxiv.org/abs/2502.14803):

1. **Exploration.** The leader splits an unknown area into one sub-region per rover. Each rover maps its part with its stereo cameras. The result is a [digital elevation map](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/).
2. **Distributed sensing.** The rovers drive in formation to a waypoint tens of metres away. They take coordinated multi-static ground-penetrating radar soundings to [map the subsurface](https://arxiv.org/abs/2502.14803).

The software plans centrally and executes in a distributed way. A [leader election mechanism](https://arxiv.org/abs/2502.14803) picks a new leader if one rover fails, and a "designated survivor" keeps a backup of every agent's data.

| Item | Value |
|---|---|
| Robots | 3 rovers + 1 lander base station ([JPL](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/cadre-mission-overview/)) |
| Sensors | Stereo cameras, ground-penetrating radar ([JPL](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/cadre-mission-overview/)) |
| Power | Solar arrays and battery; minimum charge about 20% ([paper](https://arxiv.org/abs/2502.14803)) |
| Duty cycle | 25-minute work cycles; an FPGA timer shuts all agents down at 25 and 55 min past the hour ([paper](https://arxiv.org/abs/2502.14803)) |
| CPU limit | 65 °C; only a few minutes of driving near lunar noon ([paper](https://arxiv.org/abs/2502.14803)) |
| Mission length | Daylight of one lunar day, about 14 Earth days ([NASA](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey)) |
| Wheels | Ultralight aluminium with grousers ([NASA](https://science.nasa.gov/photojournal/nasas-cadre-rovers-take-first-autonomous-drive/)) |
| Mass, size, speed | Not published in the sources cited here |

## Limitations and open issues

- **Not flown yet.** CADRE has only been tested on Earth. JPL once [targeted a late 2023 launch](https://robotics.jpl.nasa.gov/what-we-do/flight-projects/cooperative-autonomous-distributed-robotic-exploration-cadre/); IM-3 is now [listed for early 2027](https://www.nasa.gov/event-type/launch-schedule/).
- **Lander risk.** [IM-1 and IM-2 both tipped over after hard landings](https://en.wikipedia.org/wiki/IM-3). CADRE depends on IM-3 landing upright and deploying it.
- **Short mission.** The rovers only work through [one lunar day](https://www.nasa.gov/technology/nasas-mini-rover-team-is-packed-for-lunar-journey). They do not show night survival, which a base fleet would need.
- **Heat limits.** Near lunar noon the [CPU overheats after a few minutes of driving](https://arxiv.org/abs/2502.14803). Larger, longer-lived robots will need better thermal design.
- **Small scale.** The demo covers [a region near the lander](https://arxiv.org/abs/2502.14803), with waypoints tens of metres away. It does not prove kilometre-scale teamwork.
- **Ground-tested software.** Planner tests ran on [stationary flight rovers in a clean room for over 9 hours](https://arxiv.org/abs/2502.14803), not on lunar terrain.
- **Missing public specs.** Mass, size, speed and radio range are not in the sources used here.
