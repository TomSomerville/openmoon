---
slug: viper-rover-nasa
title: "VIPER rover (NASA)"
alternatives:
  - {name: "LUPEX lander and rover (JAXA/ISRO)", compare: "A Japan-India lander with a rover of over 350 kg, aimed at measuring the quantity and form of water near the south pole. It has a longer target operating period (over 3 months) but has not been built yet, while VIPER is already assembled and tested.", status: "In development; JAXA lists launch no earlier than 2028 on an H3 rocket", url: "https://www.exploration.jaxa.jp/e/program/lunarpolar/"}
  - {name: "Chang'e 7 (CNSA)", compare: "An orbiter, lander, rover and rocket-powered hopping probe aimed at the rim of Shackleton crater. Its hopper can reach places no rover can, and it targets a different site, so its data would complement VIPER's.", status: "Planned launch in 2027 on a Long March 5", url: "https://en.wikipedia.org/wiki/Chang%27e_7"}
  - {name: "Stationary lander drill, PRIME-1 style (TRIDENT + MSolo)", compare: "Uses the same drill and mass spectrometer as VIPER but bolted to a lander, so it samples one spot only. Far cheaper and simpler, but gives no map of how ice varies across terrain.", status: "Flew on Intuitive Machines IM-2 in March 2025; the lander ended up on its side and lost power the next day", url: "https://en.wikipedia.org/wiki/IM-2"}
  - {name: "Commercial lunar terrain vehicles (Astrolab CLV-1, Lunar Outpost Pegasus)", compare: "Crew-capable rovers that will be driven remotely from Earth before crews arrive, mapping the south pole region. They will map the region and gather lighting and terrain data, but they are crew vehicles, not dedicated ice prospectors.", status: "Flight hardware due to NASA end of 2027; Blue Origin task order to deliver them by 2028", url: "https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/"}
links:
  - {title: "NASA: NASA selects Blue Origin to deliver VIPER rover to Moon's south pole (CS-7)", url: "https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/", kind: official, date: "Sep 2025"}
  - {title: "NASA: NASA provides progress update on Moon Base rovers", url: "https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/", kind: official, date: "Oct 2026"}
  - {title: "NASA: NASA ends VIPER project, continues Moon exploration", url: "https://www.nasa.gov/news-release/nasa-ends-viper-project-continues-moon-exploration/", kind: official, date: "Jul 2024"}
  - {title: "NASA: NASA presses forward search for VIPER Moon rover partner", url: "https://www.nasa.gov/news-release/nasa-presses-forward-search-for-viper-moon-rover-partner/", kind: official, date: "Feb 2025"}
  - {title: "NASA CLPS blog: NASA to explore additional methods to send VIPER to Moon", url: "https://www.nasa.gov/blogs/clps/2025/05/07/nasa-to-explore-additional-methods-to-send-viper-to-moon/", kind: official, date: "May 2025"}
  - {title: "NASA Science: VIPER mission overview", url: "https://science.nasa.gov/mission/viper/", kind: official, date: "Sep 2026"}
  - {title: "NASA Science: VIPER in depth (key facts)", url: "https://science.nasa.gov/mission/viper/in-depth/", kind: official, date: ""}
  - {title: "NASA Science: VIPER rover and instruments", url: "https://science.nasa.gov/mission/viper/rover-and-instruments/", kind: official, date: ""}
  - {title: "NASA Science: VIPER lunar operations", url: "https://science.nasa.gov/mission/viper/lunar-operations/", kind: official, date: ""}
  - {title: "NASA NTRS: Fong, Volatiles Investigating Polar Exploration Rover (robotics seminar slides)", url: "https://ntrs.nasa.gov/citations/20260000802", kind: official, date: "Jan 2026"}
  - {title: "NASA NTRS: VIPER system integrated thermal vacuum test planning and preparation (TFAWS)", url: "https://ntrs.nasa.gov/citations/20250007124", kind: official, date: "Aug 2025"}
  - {title: "NASA NTRS: VIPER rover flight build and environmental test status (IAC 2024)", url: "https://ntrs.nasa.gov/citations/20240002248", kind: paper, date: "Oct 2024"}
  - {title: "Wikipedia: VIPER (rover)", url: "https://en.wikipedia.org/wiki/VIPER_(rover)", kind: wiki, date: ""}
  - {title: "Wikipedia: Blue Moon Pathfinder (first Blue Moon MK1 flight)", url: "https://en.wikipedia.org/wiki/Blue_Moon_Pathfinder", kind: wiki, date: ""}
  - {title: "Open MCT, NASA's open-source mission control software used by VIPER", url: "https://nasa.github.io/openmct/", kind: repo, date: ""}
---

## What it is

VIPER (Volatiles Investigating Polar Exploration Rover) is a solar-powered NASA rover built to map water ice at the Moon's south pole. NASA's Ames Research Center leads the mission. Johnson Space Center designed the rover hardware, and the instruments come from Ames, Kennedy and Honeybee Robotics ([Wikipedia](https://en.wikipedia.org/wiki/VIPER_(rover))). It grew out of the Resource Prospector concept, which was cancelled in 2018. VIPER was developed from 2019 to 2024 ([NTRS, Fong 2026](https://ntrs.nasa.gov/citations/20260000802)). Flight rover assembly was finished on 4 June 2024 ([NTRS](https://ntrs.nasa.gov/citations/20260000802)). The rover then completed thermal vacuum testing in the fall of 2024 ([NASA](https://www.nasa.gov/news-release/nasa-presses-forward-search-for-viper-moon-rover-partner/)).

NASA cancelled VIPER in July 2024, citing cost growth and delays to both the rover and Astrobotic's Griffin lander ([NASA](https://www.nasa.gov/news-release/nasa-ends-viper-project-continues-moon-exploration/)). The lifecycle cost had been put at $433.5 million, and about $450 million had been spent when it was cancelled ([Wikipedia](https://en.wikipedia.org/wiki/VIPER_(rover))). In 2025 NASA asked for no-cost partners and then dropped that call ([NASA](https://www.nasa.gov/blogs/clps/2025/05/07/nasa-to-explore-additional-methods-to-send-viper-to-moon/)). In September 2025 it gave Blue Origin a CLPS task order, CS-7, worth up to $190 million. The plan is to land VIPER in late 2027 on a second Blue Moon MK1 lander ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/)). As of October 2026, the rover is fully built and in final testing at Johnson ([NASA](https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/)).

## Why Open Moon uses it

VIPER is a **partner data source** for milestone M01 (prospecting). Open Moon does not buy or run it. The M01 plan says to use results from missions that are already planned first, and VIPER is the most capable of these. It is built to show where ice is most likely to be found and easiest to reach ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/)). It works in a planned 100-day window ([NASA](https://science.nasa.gov/mission/viper/)) and drills at four kinds of "ice stability region": dry, deep, shallow and surface ([NTRS](https://ntrs.nasa.gov/citations/20260000802)). That ground truth would help Open Moon choose where to send its own prospector rovers, and later where to mine.

The CS-7 delivery price (up to $190 million) is also the cost benchmark M01 uses for each of its own polar deliveries ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/)). Without VIPER, M01 still works. Its two prospector rovers would have to cover more ground alone, with less earlier data to guide their routes.

## How it works

VIPER is about the size of a golf cart. It has four wheel modules with active suspension and independent steering, so it can drive sideways or spin in place. In very soft soil it can lift each wheel and "walk" itself free ([NASA](https://science.nasa.gov/mission/viper/rover-and-instruments/)). It is the first NASA rover with headlights, which it needs inside dark craters ([NASA](https://science.nasa.gov/mission/viper/rover-and-instruments/)).

Prospecting is done in stages:

1. While driving, the **Neutron Spectrometer System (NSS)** senses hydrogen up to about 1 m (3 ft) down.
2. At promising spots, the **TRIDENT** rotary-percussive drill brings up soil from as deep as 1 m.
3. **NIRVSS** (infrared) tells water apart from hydroxyl and identifies minerals.
4. **MSolo**, a modified commercial mass spectrometer, measures the gases that come off the soil.

All four instruments are described by [NASA](https://science.nasa.gov/mission/viper/rover-and-instruments/).

Drivers on Earth steer it from waypoint to waypoint, about every 4.5 m. The signal delay is only 6 to 10 seconds. Mission control at Ames uses NASA's open-source [Open MCT](https://nasa.github.io/openmct/) software ([NASA](https://science.nasa.gov/mission/viper/lunar-operations/)).

| Specification | Value |
|---|---|
| Size | 1.5 m × 1.5 m × 2.5 m ([NASA](https://science.nasa.gov/mission/viper/in-depth/)) |
| Mass | 450 kg ([NASA](https://science.nasa.gov/mission/viper/in-depth/)); 430 kg dry ([Wikipedia](https://en.wikipedia.org/wiki/VIPER_(rover))) |
| Power | Solar-charged battery, 450 W peak ([NASA](https://science.nasa.gov/mission/viper/in-depth/)); no radioisotope heaters ([NTRS](https://ntrs.nasa.gov/citations/20260000802)) |
| Top speed | 20 cm/s; 10 cm/s limit while prospecting ([NTRS](https://ntrs.nasa.gov/citations/20260000802)) |
| Wheels | 4 × 50 cm diameter, 20 cm wide ([NTRS](https://ntrs.nasa.gov/citations/20260000802)) |
| Slopes | 15° normally, 25–30° when needed ([NASA](https://science.nasa.gov/mission/viper/lunar-operations/)) |
| Planned traverse | 20 km design limit, potential for 30+ km ([NTRS](https://ntrs.nasa.gov/citations/20260000802)); NASA now says more than 30 km ([NASA](https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/)) |
| Drilling goal | 50 holes of 1 m, 5 of them in permanently shadowed regions (PSRs); 1.7 km of driving in PSRs ([NTRS](https://ntrs.nasa.gov/citations/20260000802)) |
| Communications | X-band direct to Earth over the Deep Space Network, with no relay ([NASA](https://science.nasa.gov/mission/viper/in-depth/)) |
| Target site | Mons Mouton, west of Nobile crater, about 84.6°S ([NTRS](https://ntrs.nasa.gov/citations/20260000802)) |

## Limitations and open issues

- **The delivery is not yet certain.** CS-7 only pays for design and an off-loading demonstration up front. NASA will decide whether to fund the landing after Blue Origin's first MK1 flight ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/)). That first flight was planned for 2025 ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/)) and is now no earlier than Q1 2027 ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_Pathfinder)). The science window requires landing by late 2027, which leaves little margin.
- **It cannot spend long in the dark.** The rover is solar-only and cannot survive more than 50 hours of continuous darkness ([NASA](https://science.nasa.gov/mission/viper/lunar-operations/)). Trips into PSRs are short, and only 5 of the 50 planned drill holes are in PSRs ([NTRS](https://ntrs.nasa.gov/citations/20260000802)).
- **There are communication blackouts.** Earth is out of view for about two weeks each month, so the rover must hibernate at "safe havens" during those periods ([NASA](https://science.nasa.gov/mission/viper/lunar-operations/)).
- **It covers one small area.** It explores one region near Nobile crater over about 100 days. That data may not represent ice at other sites.
- **The instruments have little lunar heritage.** TRIDENT and MSolo flew on PRIME-1, but the IM-2 lander tipped over and lost power within a day ([Wikipedia](https://en.wikipedia.org/wiki/IM-2)).
- **NASA's public pages are out of date.** Some still list the old 2024 launch and a 20 km goal ([NASA](https://science.nasa.gov/mission/viper/in-depth/)), so check numbers against newer releases.
- **Data access is unclear.** NASA plans to release the rover software after the mission ([NASA](https://science.nasa.gov/mission/viper/lunar-operations/)). No public timeline for releasing the science data was found.
