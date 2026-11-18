---
slug: astrobotic-lunagrid-lite
title: "Astrobotic LunaGrid-Lite"
alternatives:
  - {name: "High-voltage DC cable (NASA Glenn concept)", compare: "Uses DC instead of LunaGrid-Lite's 1 kHz AC. NASA Glenn found a DC cable lighter than an AC cable for a 40 kW, 3 km link, but stepping DC voltage up and down needs stacked converters that lack high-voltage radiation-tolerant parts.", status: "Paper study for fission surface power (NETS-2022); step-down approach shown at Glenn only up to 600 V", url: "https://ntrs.nasa.gov/citations/20220002315"}
  - {name: "Wireless power beaming (laser or microwave)", compare: "No cable to lay or damage, and it can reach moving rovers. But it is far less efficient: a 2019 Navy laser test reached 20% for 400 W over 330 m with a receiver and transmitter of more than 2,500 kg.", status: "Ground demonstrations only; NASA Glenn judged it not mass-competitive for bulk power, but worth study for small mobile loads", url: "https://ntrs.nasa.gov/citations/20220002315"}
  - {name: "Superconducting cable", compare: "Near-zero resistance loss, but needs cryocoolers drawing about 18.4 kW and a radiator over 750 kg for a 40 kW link, which NASA Glenn judged not feasible.", status: "Rejected in NASA Glenn's lunar transmission review", url: "https://ntrs.nasa.gov/citations/20220002315"}
  - {name: "Generation next to each user (e.g. a VSAT solar tower per site)", compare: "Avoids long cables by putting a solar tower beside each load. Simpler, but each site then needs its own good sunlight and storage, and loads in shadow cannot be served.", status: "NASA funded three vertical solar array prototypes in 2022 (up to 32 ft tall)", url: "https://www.nasa.gov/news-release/three-companies-to-help-nasa-advance-solar-array-technology-for-moon/"}
links:
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review, flight model underway", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", kind: official, date: "Aug 2025"}
  - {title: "Astrobotic: Astrobotic wins $34.6M for power demo mission on the Moon", url: "https://www.astrobotic.com/astrobotic-wins-34-6m-for-power-demo-mission-on-the-moon/", kind: official, date: "Jul 2023"}
  - {title: "NASA: 2023 NASA Tipping Point selections", url: "https://www.nasa.gov/general/2023-nasa-tipping-point-selections/", kind: official, date: "Jul 2023"}
  - {title: "Astrobotic: Lunar-optimized, ultra-light cable transmits power (lab test)", url: "https://www.astrobotic.com/lunar-optimized-ultra-light-cable-transmits-power/", kind: official, date: "Jul 2024"}
  - {title: "Canonge & Zamborsky (Astrobotic): LunaGrid-Lite overview, LSIC presentation", url: "https://lsic.jhuapl.edu/uploadedDocs/focus-files/2531-2024-06-27%20-%20LunaGrid-Lite%20Overview%20LSIC%20Presentation%20-%20TO%20LSIC.pdf", kind: official, date: "Jun 2024"}
  - {title: "Astrobotic: LunaGrid lunar surface power service", url: "https://www.astrobotic.com/lunar-delivery/lunar-surface-power/", kind: official, date: "2026"}
  - {title: "Astrobotic: CubeRover and other Moon rovers", url: "https://www.astrobotic.com/lunar-delivery/rovers/", kind: official, date: "2026"}
  - {title: "Barth & Pike, NASA Glenn: Lunar power transmission for fission surface power (NETS-2022)", url: "https://ntrs.nasa.gov/citations/20220002315", kind: paper, date: "2022"}
  - {title: "NASA RELEASE 22-090: Three companies to help NASA advance solar array technology for Moon", url: "https://www.nasa.gov/news-release/three-companies-to-help-nasa-advance-solar-array-technology-for-moon/", kind: official, date: "Aug 2022"}
  - {title: "Wikipedia: Astrobotic Technology", url: "https://en.wikipedia.org/wiki/Astrobotic_Technology", kind: wiki, date: "2026"}
  - {title: "Space.com: Falcon Heavy launch of Griffin moon lander delayed to 2026", url: "https://www.space.com/space-exploration/spacex-falcon-heavy-launch-of-private-griffin-moon-lander-now-targeting-mid-2026", kind: press, date: "Oct 2025"}
  - {title: "SpacePolicyOnline: Astrobotic unveils Griffin Moon Base II lander", url: "https://spacepolicyonline.com/news/astrobotic-unveils-griffin-moon-base-ii-lander/", kind: press, date: "Jun 2026"}
---

## What it is

LunaGrid-Lite is a small lunar power-transmission demonstration built by Astrobotic of Pittsburgh. A tiny CubeRover drives away from a lander, unreeling a thin power cable behind it, and then receives power sent down that cable. The goal is to show for the first time that power can be moved between assets on the Moon by wire. The current design lays [500 m of ultra-light cable and transmits 1 kW](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/).

NASA picked the project in July 2023 as a [$34.6 million Tipping Point award](https://www.nasa.gov/general/2023-nasa-tipping-point-selections/), a milestone-based Space Act Agreement. The original plan was for a [6U CubeRover to unreel 1 km of cable](https://www.astrobotic.com/astrobotic-wins-34-6m-for-power-demo-mission-on-the-moon/), with the lander's solar arrays standing in for a future solar tower. By mid-2024 the planned length had dropped to [500 m](https://lsic.jhuapl.edu/uploadedDocs/focus-files/2531-2024-06-27%20-%20LunaGrid-Lite%20Overview%20LSIC%20Presentation%20-%20TO%20LSIC.pdf), mainly because of a 20 kg mass cap. In July 2024 the team sent [1 kW of AC power through 1,000 ft of lunar-designed cable](https://www.astrobotic.com/lunar-optimized-ultra-light-cable-transmits-power/) in the lab, both spooled and unspooled.

LunaGrid-Lite passed its Critical Design Review in [August 2025](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/) and moved into flight hardware build. Astrobotic aimed for a flight-ready system by Q2 2026 and a System Integration Review in Q4 2025. NASA says the rover will be [delivered by an Astrobotic Griffin lander](https://www.nasa.gov/general/2023-nasa-tipping-point-selections/). Its flight is not listed on the [Griffin Mission One](https://en.wikipedia.org/wiki/Astrobotic_Technology) payload set, and no launch date had been published as of this writing. In June 2026 Voyager [announced it is acquiring Astrobotic](https://spacepolicyonline.com/news/astrobotic-unveils-griffin-moon-base-ii-lander/).

## Why Open Moon uses it

In [M04 Surface power grid](/plan/m04-power/), electricity has to travel from solar towers on sunlit ridges, and later a reactor kept far from the crew, to habitats and ISRU plants. That means cables, and robots that can lay them. Astrobotic says its rover will be [the first ever to deliver near-permanent infrastructure](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/) to another world. It is also the first flight test of the cable, reel and high-voltage converter that Astrobotic's full [LunaGrid service](https://www.astrobotic.com/lunar-delivery/lunar-surface-power/) would use.

Open Moon's first power landing pairs a 10 kW solar tower with a LunaGrid-Lite-class cable rover. The flight data on cable heating, regolith wear and rover driving with a tether will shape how later, longer and higher-power lines are laid. Under design change DD-013 the standard Open Moon power run is 3 km or less, about six times LunaGrid-Lite's 500 m, or three 1 km reels spliced together (this plan's arithmetic). DD-014 also allows extended runs of up to 10 km, at about 10–15% loss: that is twenty times LunaGrid-Lite's 500 m, or ten 1 km reels (this plan's arithmetic). Without such a test, the base would have to lay kilometres of cable using methods never tried in lunar vacuum, dust and cold. The alternative, beaming power wirelessly, is [an order of magnitude heavier](https://ntrs.nasa.gov/citations/20220002315) for bulk power.

## How it works

The [system has four parts](https://lsic.jhuapl.edu/uploadedDocs/focus-files/2531-2024-06-27%20-%20LunaGrid-Lite%20Overview%20LSIC%20Presentation%20-%20TO%20LSIC.pdf): a DC-to-AC power converter on the lander, the cable, a cable deployment system, and the CubeRover. The converter raises the lander's power to 1 kV, single-phase AC at 1 kHz. Astrobotic says the converter was [co-created with NASA Glenn](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/). High voltage keeps current low, so a thin, light cable can carry the power.

The rover carries a reel with a tensioning and reverse mechanism, plus a motorised feeder whose splined cogs grip the cable, a design borrowed from 3D-printer filament feeders. The test load sits back at the lander in a "there and back" layout, so power flows out along the cable and back again. Sensors measure efficiency, voltage drop and power factor. The rover is Astrobotic's first [4U CubeRover](https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/), with WiFi for local links and cameras chosen for low south-polar sunlight.

| Specification | Value |
|---|---|
| Power transmitted | 1 kW |
| Transmission | 1 kV, 1 kHz, single-phase AC |
| Cable laid | 500 m (1 km in the 2023 plan) |
| Total system mass cap | 20 kg |
| Planned surface operations | up to 200 hours; no night survival |
| Lab test (2024) | 1 kW through 1,000 ft of cable |
| NASA funding | $34.6 million (Tipping Point) |

Cable mass, insulation thickness and efficiency figures for the flight cable have not been published.

## Limitations and open issues

- **Not yet flown.** All results so far are from lab tests. Astrobotic's Griffin landings have slipped before; Griffin-1 moved to [no earlier than July 2026](https://www.space.com/space-exploration/spacex-falcon-heavy-launch-of-private-griffin-moon-lander-now-targeting-mid-2026). No public flight date for LunaGrid-Lite exists.
- **Small scale.** 1 kW over 500 m is far below the tens of kilowatts over 1-3 km that a base needs, or up to 10 km on an Open Moon extended run (DD-014). NASA Glenn's [study of a 40 kW, 3 km line](https://ntrs.nasa.gov/citations/20220002315) points to several kV, so the flight design will not carry over directly.
- **Different voltage from the base grid.** NASA Glenn found [AC cable heavier than DC](https://ntrs.nasa.gov/citations/20220002315) for the same job, but DC needs high-voltage radiation-tolerant switches that are hard to get. NASA's later [grid trade study chose 3 kV AC at 1 kHz](https://ntrs.nasa.gov/citations/20220011587), and Open Moon follows it (design change DD-001). LunaGrid-Lite runs at 1 kV, so the base's source lines and distribution grid need higher-voltage cable than this demo.
- **Cable risks.** Astrobotic lists [breaking, tangling, regolith in the deployer, heating of the thin cable, jacket strength and magnetic interaction with regolith](https://lsic.jhuapl.edu/uploadedDocs/focus-files/2531-2024-06-27%20-%20LunaGrid-Lite%20Overview%20LSIC%20Presentation%20-%20TO%20LSIC.pdf) as key risks.
- **Short mission.** Up to 200 hours, with no night survival, so long-term cable ageing and thermal cycling will not be tested.
- **Programme change.** The [Voyager acquisition](https://spacepolicyonline.com/news/astrobotic-unveils-griffin-moon-base-ii-lander/) may change priorities and schedules; its effect on LunaGrid-Lite is not public.
