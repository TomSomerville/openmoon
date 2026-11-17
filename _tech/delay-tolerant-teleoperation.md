---
slug: delay-tolerant-teleoperation
title: "Delay-tolerant teleoperation"
alternatives:
  - {name: "Onboard rover autonomy (Mars-style AutoNav)", compare: "The rover finds hazards and plans its own path, so Earth only sends goals. It is not slowed by the time delay and has flown for years on Mars, but it works best on simpler terrain and gives operators less moment-to-moment control than live driving.", status: "Flight proven: Perseverance uses AutoNav on Mars (since 2021)", url: "https://www.jpl.nasa.gov/news/nasas-perseverance-rover-hightails-it-to-martian-delta/"}
  - {name: "Cooperative multi-robot autonomy (NASA CADRE)", compare: "Small rovers share a goal and split the work among themselves with little human input. This scales to many robots without many drivers, but the rovers are small and it has not yet run on the Moon.", status: "Three rovers due on Intuitive Machines IM-3; NASA launch schedule lists IM-3 for early 2027", url: "https://jpl.nasa.gov/missions/cadre"}
  - {name: "Low-latency control by crew in orbit or at the base", compare: "An astronaut nearby drives the robot with well under a second of delay and can use force feedback. Control is much more direct, but it needs crew on site or in lunar orbit, which defeats the purpose of driving rovers between crew visits.", status: "Demonstrated from the ISS to a rover on Earth in ESA's Analog-1 test (Nov 2019), about 0.8 s lag", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Astronaut_Luca_feeling_the_force_to_advance_rover_control"}
  - {name: "Crew-driven rovers only (Apollo LRV model)", compare: "Astronauts drive the rover on site with no delay at all. This is simple and proven, but the rover sits idle whenever no crew is on the Moon.", status: "Flight proven on Apollo 15, 16 and 17 (1971-1972)", url: "https://en.wikipedia.org/wiki/Lunar_Roving_Vehicle"}
links:
  - {title: "NASA NTRS 20240001217: LTV remote teleoperation studies under four lunar communication latencies (technical memorandum)", url: "https://ntrs.nasa.gov/citations/20240001217", kind: official, date: "Jan 2024"}
  - {title: "NASA NTRS 20240011392: LTV remote teleoperation studies, IEEE Aerospace Conference paper", url: "https://ntrs.nasa.gov/citations/20240011392", kind: paper, date: "Mar 2025"}
  - {title: "NASA NTRS 20250004636: Lunar science real-time operations from NASA's VIPER mission (SpaceOps 2025)", url: "https://ntrs.nasa.gov/citations/20250004636", kind: paper, date: "May 2025"}
  - {title: "NASA NTRS 20240004286: Remote science work support on NASA's VIPER mission (LPSC)", url: "https://ntrs.nasa.gov/citations/20240004286", kind: paper, date: "Mar 2021"}
  - {title: "NASA: Lunar Terrain Vehicle", url: "https://www.nasa.gov/suits-and-rovers/lunar-terrain-vehicle/", kind: official, date: "2026"}
  - {title: "NASA: NASA provides update on Moon Base rovers, landers, missions", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/", kind: official, date: "May 2026"}
  - {title: "Wikipedia: Lunokhod 1", url: "https://en.wikipedia.org/wiki/Lunokhod_1", kind: wiki, date: "2026"}
  - {title: "Wikipedia: Lunokhod 2", url: "https://en.wikipedia.org/wiki/Lunokhod_2", kind: wiki, date: "2026"}
  - {title: "ESA: Astronaut Luca feeling the force to advance rover control (Analog-1)", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Astronaut_Luca_feeling_the_force_to_advance_rover_control", kind: official, date: "Nov 2019"}
  - {title: "DLR: An astronaut controls a rover on Earth", url: "https://www.dlr.de/en/latest/news/2019/04/20191125_astronaut-controls-rover-on-earth", kind: official, date: "Nov 2019"}
  - {title: "JPL: NASA's Perseverance rover hightails it to Martian delta (AutoNav)", url: "https://www.jpl.nasa.gov/news/nasas-perseverance-rover-hightails-it-to-martian-delta/", kind: official, date: "Mar 2022"}
  - {title: "JPL: CADRE mission page", url: "https://jpl.nasa.gov/missions/cadre", kind: official, date: "2026"}
  - {title: "NASA launch schedule (Intuitive Machines IM-3, early 2027)", url: "https://www.nasa.gov/event-type/launch-schedule/", kind: official, date: "Nov 2026"}
  - {title: "Wikipedia: Lunar Roving Vehicle", url: "https://en.wikipedia.org/wiki/Lunar_Roving_Vehicle", kind: wiki, date: "2026"}
---

## What it is

Delay-tolerant teleoperation means a person on Earth drives a rover on the Moon even though every command and every camera image arrives seconds late. The driver cannot react instantly, so the workstation, the rover and the driving style are all built around that lag. A NASA team at Johnson Space Center [tested this in 2023](https://ntrs.nasa.gov/citations/20240001217) with a simulated Artemis Lunar Terrain Vehicle (LTV) at the lunar south pole.

The idea is old. In the 1970s the Soviet Lunokhod rovers were driven from Earth by [a five-man team of controllers who sent commands in real time](https://en.wikipedia.org/wiki/Lunokhod_2). [Lunokhod 1 drove 10.54 km](https://en.wikipedia.org/wiki/Lunokhod_1) and [Lunokhod 2 about 39 km](https://en.wikipedia.org/wiki/Lunokhod_2). NASA's VIPER team planned to drive from Earth in the same way. Their papers give the round trip as [about 6 to 10 seconds](https://ntrs.nasa.gov/citations/20250004636). They also say the Deep Space Network link means [instant "joystick driving" with real-time visual or haptic feedback is not possible](https://ntrs.nasa.gov/citations/20240004286).

NASA's 2023 tests are the key evidence today. In April 2023 eight operators drove with 0 and 4 seconds of delay. In August 2023 two operators drove with 6 and 8 seconds. [All operators completed every terrain type and traverse at every delay](https://ntrs.nasa.gov/citations/20240001217). The work was also presented [at the 2025 IEEE Aerospace Conference](https://ntrs.nasa.gov/citations/20240011392).

## Why Open Moon uses it

Milestone M07 (surface mobility) plans to drive rovers from Earth between crew visits, so they keep hauling cargo and scouting instead of sitting idle. NASA wants the same thing. Its LTV [can be operated remotely to move cargo and science payloads between crew missions](https://www.nasa.gov/suits-and-rovers/lunar-terrain-vehicle/). In May 2026 NASA picked two LTVs. Astrolab's CLV-1 is [designed to support remote operations](https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/). Lunar Outpost's Pegasus is [capable of manual, autonomous, or teleoperated driving](https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/).

Open Moon does not build this technology. It runs an Earth-based teleoperation centre and trains drivers. Without remote driving, rovers could only move when crew are present, or would rely entirely on onboard autonomy.

## How it works

The driver sits at a console on Earth and watches video and telemetry from the rover. In NASA's tests the driver saw the terrain through [a single mast-mounted, high-resolution pan/tilt/zoom camera](https://ntrs.nasa.gov/citations/20240001217). In the August study the console added [a rate limiter for finer hand-controller control and a "predictive circle" showing where the vehicle could go](https://ntrs.nasa.gov/citations/20240001217). Drivers used the camera's 180-degree pan for [over 95% of their navigation](https://ntrs.nasa.gov/citations/20240001217), and leaned on cruise control at 6 and 8 seconds of delay.

The NASA requirement being checked was [6 km (threshold) to 8 km (goal) in one 24-hour period when operated remotely](https://ntrs.nasa.gov/citations/20240001217). Results, averaged over all operators and test conditions:

| Round-trip delay | Average speed (with stops) | Time to drive 6 km |
|---|---|---|
| 0 s | 3.24 km/h | 1 h 51 min |
| 4 s | 2.56 km/h | 2 h 21 min |
| 6 s | 2.03 km/h | 2 h 57 min |
| 8 s | 1.76 km/h | 3 h 25 min |

Source: [NASA NTRS 20240001217](https://ntrs.nasa.gov/citations/20240001217). The simulated rover could reach [12 km/h, turn in place and handle ±20° slopes](https://ntrs.nasa.gov/citations/20240001217). Drivers went slower and braked more with any delay, and [workload rose significantly](https://ntrs.nasa.gov/citations/20240001217). The study chose 6 to 8 seconds [based on an analysis of Deep Space Network capabilities](https://ntrs.nasa.gov/citations/20240001217).

## Limitations and open issues

- **Small, simulated tests.** The August 6 and 8 second study used [only two operators](https://ntrs.nasa.gov/citations/20240001217). All runs were in a simulator, with [a high-bandwidth, flawless communication link and faultless navigation](https://ntrs.nasa.gov/citations/20240001217). Dropouts and real lunar lighting have not been tested this way.
- **Rock strikes.** In the April study the vehicle had [861 rock contacts at 0 s and 959 at 4 s](https://ntrs.nasa.gov/citations/20240001217) across all runs. Rock contacts were not analysed for the 6 and 8 second runs.
- **Training.** Test operators had 15 minutes to 3 hours of practice. They estimated [20 to 100 hours to reach about 60% proficiency, and up to a year for full proficiency](https://ntrs.nasa.gov/citations/20240001217).
- **Line of sight.** Driving from Earth needs a radio path to Earth. Near the south pole, terrain can block it. How often this would stop driving at Open Moon's sites is not published.
- **Not yet flown for LTVs.** No LTV has reached the Moon. NASA aims to deploy them [by 2028](https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/), and how remote driving performs there is still to be proven.
