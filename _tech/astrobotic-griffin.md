---
slug: astrobotic-griffin
title: "Astrobotic Griffin"
alternatives:
  - {name: "Firefly Blue Ghost", compare: "Smaller lander that carried about 94 kg of NASA payloads on its first flight. It has the best record of any commercial lander, but it cannot carry a 500 kg rover the way Griffin is meant to.", status: "Flown: fully successful soft landing in Mare Crisium on 2 March 2025", url: "https://en.wikipedia.org/wiki/Blue_Ghost_Mission_1"}
  - {name: "Intuitive Machines Nova-C", compare: "Methane/oxygen lander for about 100-130 kg of payload, much less than Griffin. It has reached the surface twice, but both landers ended up on their sides.", status: "Flown twice (IM-1 Feb 2024, IM-2 Mar 2025); IM-3 planned", url: "https://en.wikipedia.org/wiki/Nova-C"}
  - {name: "Blue Origin Blue Moon Mark 1", compare: "Hydrogen/oxygen lander for up to 3,000 kg, about five times Griffin's capacity. It suits larger cargo but needs a New Glenn launch and has not flown yet.", status: "Pathfinder flight planned for 2027", url: "https://en.wikipedia.org/wiki/Blue_Moon_(spacecraft)"}
links:
  - {title: "Astrobotic: Griffin Lander (product page and specifications)", url: "https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/", kind: official, date: "accessed Nov 2026"}
  - {title: "Astrobotic Lunar Landers Payload User's Guide (Peregrine and Griffin)", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", kind: data, date: "Aug 2021"}
  - {title: "NASA: Moon Base, Voyager Griffin-1 mission page", url: "https://www.nasa.gov/event/clps-flight-astrobotics-griffin-mission-one/", kind: official, date: "Oct 2026"}
  - {title: "NASA: NASA Ends VIPER Project, Continues Moon Exploration", url: "https://www.nasa.gov/news-release/nasa-ends-viper-project-continues-moon-exploration/", kind: official, date: "Jul 2024"}
  - {title: "NASA OIG IG-24-013: NASA's Commercial Lunar Payload Services Initiative", url: "https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf", kind: official, date: "Jun 2024"}
  - {title: "Griffin Mission One, Wikipedia", url: "https://en.wikipedia.org/wiki/Griffin_Mission_One", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Astrobotic Technology, Wikipedia", url: "https://en.wikipedia.org/wiki/Astrobotic_Technology", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Peregrine Mission One, Wikipedia", url: "https://en.wikipedia.org/wiki/Peregrine_Mission_One", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Commercial Lunar Payload Services, Wikipedia", url: "https://en.wikipedia.org/wiki/Commercial_Lunar_Payload_Services", kind: wiki, date: "accessed Nov 2026"}
  - {title: "SpacePolicyOnline: Astrobotic Unveils Griffin Moon Base II Lander", url: "https://spacepolicyonline.com/news/astrobotic-unveils-griffin-moon-base-ii-lander/", kind: press, date: "Jun 2026"}
---

## What it is

Griffin is a four-legged robotic cargo lander built by [Astrobotic](https://en.wikipedia.org/wiki/Astrobotic_Technology), a company founded in Pittsburgh in 2007. Voyager Technologies announced in June 2026 that it was buying Astrobotic ([SpacePolicyOnline](https://spacepolicyonline.com/news/astrobotic-unveils-griffin-moon-base-ii-lander/)). Griffin is the larger sibling of Astrobotic's Peregrine lander and shares its core spacecraft bus ([Astrobotic PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)). Astrobotic rates it at [625 kg of payload](https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/) to the lunar surface, with 100 m landing accuracy. NASA buys deliveries on landers like Griffin through its [Commercial Lunar Payload Services (CLPS)](https://en.wikipedia.org/wiki/Commercial_Lunar_Payload_Services) program.

NASA picked Griffin in June 2020 to deliver the VIPER rover. The task order started at $199.5 million and had grown to $322.8 million by February 2024 ([NASA OIG](https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf)). In July 2024 NASA [ended VIPER](https://www.nasa.gov/news-release/nasa-ends-viper-project-continues-moon-exploration/), but it kept the Griffin contract as a flight demonstration of the lander and its engines. Griffin's predecessor, Peregrine, launched in January 2024 but never reached the Moon because of a [propellant leak](https://en.wikipedia.org/wiki/Peregrine_Mission_One).

The first flight, Griffin Mission One, will carry Astrolab's 500 kg FLIP rover and smaller payloads to Nobile Crater near the south pole ([Wikipedia](https://en.wikipedia.org/wiki/Griffin_Mission_One)). NASA named it "Moon Base II" in May 2026. The lander finished environmental testing at JPL on 13 October 2026, and launch on a SpaceX Falcon Heavy is planned for no earlier than January 2027 ([Wikipedia](https://en.wikipedia.org/wiki/Griffin_Mission_One); [NASA](https://www.nasa.gov/event/clps-flight-astrobotics-griffin-mission-one/)).

## Why Open Moon uses it

Griffin is one of three small-cargo landers in milestone M02 (Transport), next to Firefly Blue Ghost and Intuitive Machines Nova-C. It fills the gap between landers that carry about 100 kg and Blue Moon Mark 1's 3 t. That size suits single rovers, science packages and small power or communications units. Its optional [egress ramps](https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/) let a rover drive off without a crane.

Open Moon's rule is to fly each payload class with two providers where possible. Without Griffin, the only flown landers in the plan carry much less than a 500 kg rover. Payloads of that size would wait for the first Blue Moon Mark 1 flights, which are larger, costlier and also not yet flown.

## How it works

Griffin uses an aluminum structure with a launch adapter cone, deck panels and four radiator panels. Payloads mount on the deck, below it or on rover ramps ([PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)). Four landing legs absorb the touchdown shock.

The propulsion system burns a hypergolic bipropellant (M20, a hydrazine derivative, with MON-3 oxidizer) that ignites on contact. The 2021 user's guide lists five 700 lbf main engines and twelve 25 lbf attitude thrusters ([PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)). Astrobotic's current page lists [seven main engines](https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/) and four thruster clusters. The engines pulse on and off to throttle.

For landing, Griffin uses a star tracker, sun sensors, an inertial unit, a Doppler LiDAR and terrain-relative navigation, with an optional scanning LiDAR to spot hazards down to 15 cm ([Astrobotic](https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/)). Power comes from triple-junction solar cells and a lithium-ion battery on a 28 V bus. Polar missions use side-mounted panels. The lander talks to Earth on X-band and to deployed rovers over a 2.4 GHz WLAN link ([PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)).

| Specification | Value |
|---|---|
| Payload to surface | 625 kg ([Astrobotic](https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/)) |
| Lander mass (Mission One) | 1,265 kg ([Wikipedia](https://en.wikipedia.org/wiki/Griffin_Mission_One)) |
| Landing accuracy | 100 m |
| Surface operations (polar) | Up to 14 days ([PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)) |
| Payload power | 1.0 W/kg nominal, 2.5 W/kg peak |
| Launch vehicle | SpaceX Falcon Heavy |
| Published surface price (2021) | $1.2 million per kg ([PUG](https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf)) |

Astrobotic does not publish Griffin's dimensions or its propellant load.

## Limitations and open issues

- **No flight heritage.** Griffin has never flown. Its only sibling, Peregrine, failed in space after a [valve problem](https://en.wikipedia.org/wiki/Peregrine_Mission_One).
- **New engines.** NASA's Inspector General noted Griffin uses a scaled-up version of Peregrine's engine, and that Peregrine's engines were never qualification-tested or fired for full duration before flight ([OIG](https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf)).
- **Schedule slips.** The first launch was set for November 2023 and has slipped many times. It is now planned for January 2027 ([OIG](https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf); [Wikipedia](https://en.wikipedia.org/wiki/Griffin_Mission_One)).
- **Cost growth.** The VIPER task order rose 62% before the rover was cancelled ([OIG](https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf)).
- **Short surface life.** The polar configuration is rated for up to 14 days, so Griffin delivers payloads but cannot serve as long-term infrastructure.
- **Unclear specs.** The published main-engine count differs between the 2021 guide (five) and the current product page (seven).
- **Follow-on flights.** No dates have been published for later Griffin missions ([Wikipedia](https://en.wikipedia.org/wiki/Astrobotic_Technology)).
