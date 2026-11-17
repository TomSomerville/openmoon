---
slug: nokia-lunar-4g-lte-network
title: "Nokia lunar 4G/LTE network"
alternatives:
  - {name: "Wi-Fi (802.11) access points", compare: "NASA's baseline suit design sends non-critical video over 5 GHz Wi-Fi from an access point on the lander or rover. Wi-Fi is cheap and mature, but NASA expects it to reach only about 100-300 m, far short of the 2 km walking range.", status: "Baseline for video in Artemis suit designs; not yet flown on the lunar surface", url: "https://ntrs.nasa.gov/citations/20220015268"}
  - {name: "UHF TDMA suit radio (Space to Space Communication System)", compare: "The legacy UHF radio carries crew voice and limited telemetry and needs no central hub, so suits can talk directly. It supports only five users and low data rates, so it cannot carry HD video or a fleet of robots.", status: "Baseline for Artemis crew voice; flight heritage in low Earth orbit", url: "https://ntrs.nasa.gov/citations/20250001947"}
  - {name: "Mesh network radios (NASA JPL CADRE)", compare: "Small rovers relay data to each other and to a lander base station with no single hub, which suits robot swarms. Range and data rates are not published, and the system is a small technology demo, not a standards-based network.", status: "Built; JPL lists it as a future mission on Intuitive Machines IM-3", url: "https://www.jpl.nasa.gov/missions/cadre"}
  - {name: "Lunar relay satellites for surface-to-surface links", compare: "Surface users can reach each other through orbiting relays, which also covers areas with no local base station. NASA engineers note this does not scale well as the number of surface users grows, and it adds delay and depends on satellite passes.", status: "NASA relay services contract awarded to Intuitive Machines, Sep 2024", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services"}
links:
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", kind: official, date: "Mar 2025"}
  - {title: "Nokia: Nokia's cellular network ready for Moon as Intuitive Machines completes final lunar lander installation", url: "https://www.nokia.com/newsroom/nokias-cellular-network-ready-for-moon-as-intuitive-machines-completes-final-lunar-lander-installation/", kind: official, date: "Jan 2025"}
  - {title: "Nokia: How cellular networks will help us explore the Moon and Mars", url: "https://www.nokia.com/about-us/newsroom/articles/how-cellular-networks-will-help-us-explore-the-moon-and-mars/", kind: official, date: "Feb 2024"}
  - {title: "Nokia: Nokia and Axiom Space partner on cellular capabilities in next-gen lunar spacesuits", url: "https://www.nokia.com/newsroom/nokia-and-axiom-space-partner-to-enable-high-speed-cellular-network-capabilities-in-next-gen-lunar-spacesuits/", kind: official, date: "Aug 2024"}
  - {title: "NASA: Hello, Moon? It's NASA Calling (Tipping Point award to Nokia)", url: "https://www.nasa.gov/blogs/missions/2020/10/22/hello-moon-its-nasa-calling/", kind: official, date: "Oct 2020"}
  - {title: "NASA: NASA receives some data before Intuitive Machines ends lunar mission", url: "https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/", kind: official, date: "Mar 2025"}
  - {title: "Edwards et al.: 3GPP Telecommunications Technology on the Moon (IEEE Aerospace 2023, NTRS)", url: "https://ntrs.nasa.gov/citations/20220015268", kind: paper, date: "Mar 2023"}
  - {title: "Edwards et al.: Envisioned Lunar Surface Communications Using 3GPP Cellular and Wi-Fi Technologies (SpaceOps 2025, NTRS)", url: "https://ntrs.nasa.gov/citations/20250001947", kind: paper, date: "May 2025"}
  - {title: "NASA: NASA adds mission to Artemis lunar program, updates architecture", url: "https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/", kind: official, date: "Feb 2026"}
  - {title: "NASA JPL: CADRE (Cooperative Autonomous Distributed Robotic Exploration)", url: "https://www.jpl.nasa.gov/missions/cadre", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA: NASA selects lunar relay contractor for Near Space Network services", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services", kind: official, date: "Sep 2024"}
  - {title: "IM-2, Wikipedia", url: "https://en.wikipedia.org/wiki/IM-2", kind: wiki, date: "accessed Nov 2026"}
  - {title: "LTE (telecommunication), Wikipedia", url: "https://en.wikipedia.org/wiki/LTE_(telecommunication)", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

The Lunar Surface Communications System (LSCS) is a small 4G/LTE cellular network built by Nokia Bell Labs to work on the Moon. It uses the same [4G/LTE standard](https://en.wikipedia.org/wiki/LTE_(telecommunication)) as billions of phones, but Bell Labs [redesigned it](https://www.nokia.com/newsroom/nokias-cellular-network-ready-for-moon-as-intuitive-machines-completes-final-lunar-lander-installation/) for the lunar environment. NASA picked the project in October 2020 as a [Tipping Point award of about $14 million](https://www.nasa.gov/blogs/missions/2020/10/22/hello-moon-its-nasa-calling/). At the time, delivery was planned for late 2022.

The system flew on Intuitive Machines' IM-2 mission. The Athena lander touched down near the south pole on 6 March 2025, but [came to rest on its side in a crater](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/), and the mission ended early the next day. Because the solar panels pointed the wrong way, Nokia had power for only [a 25-minute window](https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/). In that window the network powered on, took commands from Nokia's control centre in Sunnyvale, California, and reported that its base station, radio and core were all working. It ran without interruption for the whole window. It could not make the first cellular call on the Moon, because the hopper carrying the user device had grown too cold by then.

Next, Nokia and Axiom Space plan to put the same technology into [Axiom's AxEMU spacesuits](https://www.nokia.com/newsroom/nokia-and-axiom-space-partner-to-enable-high-speed-cellular-network-capabilities-in-next-gen-lunar-spacesuits/). That demonstration was planned for the Artemis III landing. In February 2026 NASA [turned Artemis III into a low Earth orbit test in 2027](https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/) and moved the first landing to Artemis IV in 2028. When and where the suit demonstration will now fly has not been announced.

## Why Open Moon uses it

The base needs a local wireless network so that robots, sensors and later crew can talk to each other without going through Earth. A signal takes [about 1.5 seconds](https://www.nokia.com/about-us/newsroom/articles/how-cellular-networks-will-help-us-explore-the-moon-and-mars/) to reach Earth from the Moon. Coordinating a fleet of robots through Earth would be slow. Nokia argues a lunar base will look like an industrial site on Earth, with many machines and sensors on one network.

In the plan, an LTE base station at the habitat is the core of the M03 surface network. Mesh radios, relay masts on crater rims and fibre extend it. NASA engineers note that routing surface-to-surface traffic through relay satellites [does not scale well](https://ntrs.nasa.gov/citations/20220015268) as users multiply. A NASA working group has also recommended that NASA [baseline 3GPP cellular technology](https://ntrs.nasa.gov/citations/20250001947) for surfaces of the Moon and Mars. Without a cellular network, the base would rely on Wi-Fi with short range and UHF radios with low data rates.

## How it works

The LSCS has [three parts](https://ntrs.nasa.gov/citations/20250001947):

- **Network in a box (NIB):** a dual-redundant unit that combines the LTE base station and the core network, plus antennas, on the lander.
- **Device modules:** custom LTE modems tuned for extended coverage, fitted to the Lunar Outpost MAPP rover and the Intuitive Machines Micro-Nova "Grace" hopper.
- **Operations software:** mission control tools designed for slow, lossy direct-to-Earth links.

On Athena, the NIB sat on [an upper carbon-composite panel with 14 thermally isolated mounting points](https://www.nokia.com/newsroom/nokias-cellular-network-ready-for-moon-as-intuitive-machines-completes-final-lunar-lander-installation/). The lander's thermal system removed heat while it ran and warmed it while idle. Data was to go back to Earth through Intuitive Machines' direct-to-Earth service.

| Specification | IM-2 value |
|---|---|
| Standard | 4G/LTE, 3GPP Release 12 ([NASA](https://ntrs.nasa.gov/citations/20220015268)) |
| Band and channel | Band 3 (1710-1785 MHz up, 1805-1880 MHz down), 20 MHz channel ([NASA](https://ntrs.nasa.gov/citations/20220015268)) |
| Base station height | About 4 m, on the lander ([NASA](https://ntrs.nasa.gov/citations/20220015268)) |
| Planned range | 200-300 m short range, up to 2 km long range ([NASA](https://ntrs.nasa.gov/citations/20250001947)) |
| Operating time on the Moon | 25 minutes ([Nokia](https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/)) |
| Mass, power, data rate | Not published |

For the suit demonstration, Nokia plans to move to [3GPP Band 7](https://ntrs.nasa.gov/citations/20250001947), following lunar spectrum recommendations. The goal is HD video from each suit at 2 km or more.

## Limitations and open issues

- **No end-to-end test yet.** No device has connected to the network on the Moon, so range, throughput and lunar radio propagation are still unmeasured ([Nokia](https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/)).
- **Not radiation-hardened for critical use.** The IM-2 hardware was hardened but is not "rad hard" for high-criticality jobs such as crew voice ([NASA](https://ntrs.nasa.gov/citations/20220015268)).
- **No night survival.** The base station and devices were not designed to survive the lunar night ([NASA](https://ntrs.nasa.gov/citations/20220015268)). A base network needs a version that does.
- **Spectrum.** Long-term approval for Band 3 on the Moon is unlikely because of radio astronomy concerns below 2 GHz ([NASA](https://ntrs.nasa.gov/citations/20220015268)). The planned Band 7 also overlaps a radio astronomy band and a LunaNet navigation band, which leaves only part of it usable.
- **Single point of failure.** One base station gives coverage only near its site. When a lander leaves, [so does its network](https://ntrs.nasa.gov/citations/20250001947), so a permanent base needs fixed, maintained base stations.
- **Hub-dependent.** Unlike the UHF suit radio, standard LTE needs a base station. NASA wants suits to [talk directly](https://ntrs.nasa.gov/citations/20250001947) when no base station is in view.
- **Schedule.** The crewed suit demonstration was tied to Artemis III, which [no longer lands on the Moon](https://www.nasa.gov/news-release/nasa-adds-mission-to-artemis-lunar-program-updates-architecture/).
