---
slug: optical-laser-communications
title: "Optical (laser) communications"
alternatives:
  - {name: "Ka-band radio direct-to-Earth", compare: "Uses radio dishes instead of a laser. It works through clouds and is mature, but needs a bigger, heavier antenna for less data: LRO's Ka-band system sent 100 Mb/s with a 0.75 m antenna, versus 622 Mb/s for the lighter LLCD laser terminal.", status: "Flight proven at the Moon since LRO (2009); supported by NASA's Deep Space Network, which is oversubscribed", url: "https://www.nasa.gov/wp-content/uploads/2025/09/optical-communications-systems-for-nasas-human-space-flight-missions.pdf"}
  - {name: "S-band radio (low-rate link)", compare: "The standard low-rate radio link for commanding and voice. Very robust and needs little pointing, but Orion's S-band link runs at only up to a few Mbps, far too slow for bulk video and science data.", status: "Operational; Orion's primary communications link", url: "https://www.nasa.gov/wp-content/uploads/2025/09/optical-communications-systems-for-nasas-human-space-flight-missions.pdf"}
  - {name: "NASA commercial lunar relay (Intuitive Machines)", compare: "Radio relay satellites in lunar orbit, so sites with no view of Earth can still talk home and surface terminals can be smaller. It adds coverage, not raw speed, and depends on a service contract and on relay launches.", status: "Contract with a maximum potential value of $4.82B awarded Sep 2024; relays not yet operating", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services"}
  - {name: "ESA Moonlight", compare: "A European relay constellation: one high data rate communications satellite and four navigation satellites, linked to Earth through three ground stations. Like other relays it fixes coverage gaps at the south pole rather than replacing a high-rate optical pipe.", status: "Initial operations planned by end of 2028, full operations by 2030", url: "https://www.esa.int/articles/esa-s-moonlight-programme-pioneering-the-path-for-lunar-exploration"}
links:
  - {title: "NASA: Laser Communications Relay Demonstration (LCRD) overview", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/", kind: official, date: "2026"}
  - {title: "NASA Goddard ESC: Orion Artemis II Optical Communications System (O2O)", url: "https://www.nasa.gov/goddard/esc/o2o/", kind: official, date: "May 2026"}
  - {title: "NASA: Laser communications terminal delivered for Artemis II Moon mission", url: "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/nasa-laser-communications-terminal-delivered-for-artemis-ii-moon-mission/", kind: official, date: "Jun 2023"}
  - {title: "NASA: Historic demonstration proves laser communication possible (LLCD, 622 Mbps from lunar orbit)", url: "https://www.nasa.gov/missions/tech-demonstration/laser-communications-relay/historic-demonstration-proves-laser-communication-possible/", kind: official, date: "Oct 2013"}
  - {title: "Seas et al. (NASA GSFC, MIT Lincoln Laboratory): Optical communications systems for NASA's human space flight missions", url: "https://www.nasa.gov/wp-content/uploads/2025/09/optical-communications-systems-for-nasas-human-space-flight-missions.pdf", kind: paper, date: "Sep 2025"}
  - {title: "NASA: Record-breaking laser demo (TBIRD) completes mission", url: "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/nasas-record-breaking-laser-demo-completes-mission/", kind: official, date: "Sep 2024"}
  - {title: "NASA: Deep space communications demo (DSOC) exceeds project expectations", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/deep-space-optical-communications-dsoc/nasas-deep-space-communications-demo-exceeds-project-expectations/", kind: official, date: "Sep 2025"}
  - {title: "NASA OIG IG-23-016: NASA's management of the Deep Space Network", url: "https://oig.nasa.gov/docs/IG-23-016.pdf", kind: official, date: "Jul 2023"}
  - {title: "collectSPACE: Artemis II flyby video and Intuitive Machines lunar relays", url: "https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html", kind: press, date: "Apr 2026"}
  - {title: "NASA Image Library: O2O hardware at Kennedy Space Center", url: "https://images.nasa.gov/details/KSC-20230602-PH-GEB01-0010", kind: official, date: "Jun 2023"}
  - {title: "Laser communication in space, Wikipedia", url: "https://en.wikipedia.org/wiki/Laser_communication_in_space", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Laser Communications Relay Demonstration, Wikipedia", url: "https://en.wikipedia.org/wiki/Laser_Communications_Relay_Demonstration", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

Optical communications send data on a beam of infrared laser light instead of radio waves. The higher frequency of light lets far more data fit into one link, and the hardware can be smaller, lighter and use less power than a radio system with similar performance. NASA says optical links can offer a [10- to 100-fold increase in data rate](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/) over radio for comparable mass and power.

NASA has built this up step by step, mostly with [MIT Lincoln Laboratory](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/nasa-laser-communications-terminal-delivered-for-artemis-ii-moon-mission/). In 2013 the Lunar Laser Communication Demonstration (LLCD) on LADEE sent data from lunar orbit at [622 Mbps, with a 20 Mbps uplink](https://www.nasa.gov/missions/tech-demonstration/laser-communications-relay/historic-demonstration-proves-laser-communication-possible/). The Laser Communications Relay Demonstration (LCRD) launched to geosynchronous orbit in December 2021 and has run [31 experiments and more than 3,400 test sessions](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/) since June 2022. The TBIRD CubeSat reached [200 Gbps](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/nasas-record-breaking-laser-demo-completes-mission/) to the ground, and DSOC on Psyche streamed video at [267 Mbps from 19 million miles away](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/deep-space-optical-communications-dsoc/nasas-deep-space-communications-demo-exceeds-project-expectations/).

The closest match to what a Moon base needs is O2O, the [Orion Artemis II Optical Communications System](https://www.nasa.gov/goddard/esc/o2o/), designed to send 4K video from the Moon. It launched on Artemis II on 1 April 2026. It was the first laser system on a crewed deep-space mission, linked Orion and Earth at up to 260 Mbps and [sent over 484 gigabytes](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/) of data.

## Why Open Moon uses it

In milestone M03 (Communications, navigation and time), the optical terminal is the base's high-rate pipe to Earth. It carries bulk data such as video, science and mapping data, while radio relays and radio direct-to-Earth links handle commanding. The plan budgets an estimated $0.08–0.25 billion for a base terminal of the O2O/LCRD class. That figure is an Open Moon estimate, not a published price.

Without optical links, all bulk data would have to go over radio. That means larger antennas and more power at the base, and more load on NASA's Deep Space Network. The network is already oversubscribed, with demand [exceeding supply by as much as 40 percent](https://oig.nasa.gov/docs/IG-23-016.pdf) at times. The same report says the DSN is [expected to support optical communication](https://oig.nasa.gov/docs/IG-23-016.pdf) in future, using less power for faster downloads.

## How it works

A terminal has three main parts: an optical module (a small telescope on a gimbal) that points the beam, a modem that turns data into light pulses, and control electronics. On Orion, the optical module and controller sat outside on the crew module adapter, and the modem sat inside on a vibration-isolated pallet. O2O uses a 10 cm telescope design called MAScOT with a field of regard of 90° to −30° in elevation and 360° in azimuth. In the published design it is paired with a [1 W, 1550 nm pulse-position modulation modem](https://www.nasa.gov/wp-content/uploads/2025/09/optical-communications-systems-for-nasas-human-space-flight-missions.pdf). The laser beam is very narrow, so precise pointing is the hardest part. LLCD calibrated its pointing on the way to the Moon so it could [lock on almost instantly](https://www.nasa.gov/missions/tech-demonstration/laser-communications-relay/historic-demonstration-proves-laser-communication-possible/).

On Earth, ground telescopes sit at high, dry sites. O2O sent data to [Las Cruces, New Mexico, or Table Mountain, California](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/nasa-laser-communications-terminal-delivered-for-artemis-ii-moon-mission/). LCRD uses [Table Mountain and Haleakalā, Hawaii](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/).

| Item | LLCD (2013) | O2O (2026) |
|---|---|---|
| Downlink | 622 Mbps | up to 260 Mbps |
| Uplink | 20 Mbps | up to 20 Mbps (design) |
| Telescope aperture | not stated here | 10 cm |
| Wavelength | not stated here | 1550 nm |
| Terminal mass / power | 30.7 kg / 90 W | not published |
| Comparable Ka-band radio | 61 kg / 120 W, 100 Mb/s (LRO) | — |

Sources: [Seas et al.](https://www.nasa.gov/wp-content/uploads/2025/09/optical-communications-systems-for-nasas-human-space-flight-missions.pdf), [NASA LCRD](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/).

## Limitations and open issues

- **Clouds and weather.** Infrared links are [highly sensitive to clouds](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/). LCRD showed links can survive some thin high clouds, but NASA stresses the need for more ground stations for redundancy.
- **Pointing.** On Artemis II the terminal could not always point at Earth, for example while the spacecraft's windows faced the Moon during the flyby, so live video had to [go over radio](https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html). Open Moon keeps radio as the primary command link.
- **Earth must be in view.** A direct laser link only works when Earth is above the horizon. No operational lunar optical relay has been funded or announced in the sources used here.
- **Not yet proven on the surface.** Every flight so far has been in orbit or in flight. How a terminal copes with lunar dust and the cold lunar night on the surface has not been demonstrated.
- **Mass, power and price of a surface terminal are not published.** The plan's budget line is an estimate.
- **Ground network is small.** NASA's laser demonstrations have relied on a handful of ground stations (Table Mountain, Haleakalā, Las Cruces). Capacity will need to grow if many lunar users depend on laser links.
