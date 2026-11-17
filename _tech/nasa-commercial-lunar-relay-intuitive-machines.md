---
slug: nasa-commercial-lunar-relay-intuitive-machines
title: "NASA commercial lunar relay (Intuitive Machines)"
alternatives:
  - {name: "ESA Moonlight", compare: "European relay and navigation service, also aimed at the south pole: one communications satellite and four navigation satellites. It adds a second, independent network, but starts later than the planned US service.", status: "In development; initial operations by end 2028, full operations by 2030", url: "https://www.esa.int/articles/esa-s-moonlight-programme-pioneering-the-path-for-lunar-exploration"}
  - {name: "SSTL Lunar Pathfinder", compare: "A single relay satellite built by SSTL and operated by ESA. Much smaller in scope than a five-satellite constellation, so coverage is limited, but it is close to flight.", status: "Final environmental testing (Oct 2026); launch NET 2027 on Firefly Blue Ghost Mission 2", url: "https://en.wikipedia.org/wiki/Lunar_Pathfinder"}
  - {name: "Direct-to-Earth via NASA's Deep Space Network", compare: "No relay needed when Earth is above the horizon. But at south pole sites Earth is often out of view, and the DSN is already oversubscribed.", status: "Operational, but demand exceeds capacity by up to 40%", url: "https://oig.nasa.gov/docs/IG-23-016.pdf"}
  - {name: "JAXA Lunar Navigation Satellite System (LNSS)", compare: "Japan's planned lunar navigation service, meant to be interoperable with NASA's relays and Moonlight. Would add navigation coverage rather than replace the Earth link.", status: "Planned; no public launch date found", url: "https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf"}
links:
  - {title: "NASA: NASA selects lunar relay contractor for Near Space Network services", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services", kind: official, date: "Sep 2024"}
  - {title: "Esper et al., NASA's Lunar Communications Relay and Navigation Systems (LCRNS), SpaceOps 2025 (NTRS)", url: "https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf", kind: paper, date: "May 2025"}
  - {title: "NASA: NASA delivers navigation system for commercial lunar relay (NavCube3-mini on Altus-1)", url: "https://www.nasa.gov/technology/space-comms/nasa-delivers-navigation-system-for-commercial-lunar-relay/", kind: official, date: "Aug 2026"}
  - {title: "NASA: LunaNet Interoperability Specification", url: "https://www.nasa.gov/communicating-with-missions/scan/lcrns/lunanet-interoperability-specification/", kind: data, date: "Feb 2025"}
  - {title: "NASA OIG: active audits, incl. A-26-05-00-HED on SCaN for Artemis", url: "https://oig.nasa.gov/active-projects/", kind: official, date: "Nov 2026"}
  - {title: "NASA OIG IG-23-016: NASA's Management of the Deep Space Network", url: "https://oig.nasa.gov/docs/IG-23-016.pdf", kind: official, date: "Jul 2023"}
  - {title: "IM-3, Wikipedia", url: "https://en.wikipedia.org/wiki/IM-3", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Intuitive Machines, Wikipedia", url: "https://en.wikipedia.org/wiki/Intuitive_Machines", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Gunter's Space Page: Altus 1-5", url: "https://space.skyrocket.de/doc_sdat/altus-1.htm", kind: data, date: "accessed Nov 2026"}
  - {title: "collectSPACE: Artemis II flyby video and Intuitive Machines lunar relays", url: "https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html", kind: press, date: "Apr 2026"}
  - {title: "Aviation Week: Intuitive Machines lunar communication satellite launch plans change", url: "https://aviationweek.com/space/space-exploration/intuitive-machines-lunar-communication-satellite-launch-plans-change", kind: press, date: "Aug 2026"}
  - {title: "ESA: Moonlight programme", url: "https://www.esa.int/articles/esa-s-moonlight-programme-pioneering-the-path-for-lunar-exploration", kind: official, date: "Oct 2024"}
---

## What it is

NASA is buying lunar relay service instead of building its own relay satellites. In September 2024 it awarded Intuitive Machines of Houston a firm-fixed-price contract for "GEO to Cislunar Relay Services" under its Near Space Network, with a maximum potential value of $4.82 billion. The base period runs from October 2024 to September 2029, with options to September 2034 ([NASA](https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services)). The service covers communications plus position, navigation and timing (PNT) for the lunar south pole region.

NASA's project behind this is called Lunar Communications Relay and Navigation Systems (LCRNS). Intuitive Machines is its first commercial provider, and its satellites and ground stations form the Lunar Data Network, which the company runs independently of NASA ([Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf)). The company plans five relay satellites ([collectSPACE](https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html)), named Altus 1 to 5 ([Gunter's Space Page](https://space.skyrocket.de/doc_sdat/altus-1.htm)).

None has flown yet. Altus-1 is to ride with the IM-3 lander, now listed as no earlier than the first quarter of 2027 ([Wikipedia](https://en.wikipedia.org/wiki/IM-3)). The company had earlier forecast 2026 ([Aviation Week](https://aviationweek.com/space/space-exploration/intuitive-machines-lunar-communication-satellite-launch-plans-change)). NASA delivered a GPS/Galileo navigation receiver, NavCube3-mini, for Altus-1 in July 2026 ([NASA](https://www.nasa.gov/technology/space-comms/nasa-delivers-navigation-system-for-commercial-lunar-relay/)).

## Why Open Moon uses it

This is the base's main link to Earth in [M03](/plan/m03-comms-nav/). Near the south pole, Earth is often below the horizon. In NASA's analysis, direct-to-Earth links give only 17% to 43% yearly coverage at candidate landing sites. One relay raises that to 80-86%, and NASA says two more relays remove the remaining gaps ([Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf)). The other option, NASA's Deep Space Network, is already oversubscribed by up to 40%, rising to about 50% by the 2030s ([NASA OIG](https://oig.nasa.gov/docs/IG-23-016.pdf)).

NASA expects the relays to serve human landers, the Lunar Terrain Vehicle and CLPS landers ([NASA](https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services)). Open Moon's robots and crew would use the same service. Without it, the base would be cut off for much of each month, and rovers in shadowed craters would have no link at all. Because it follows the shared LunaNet specification, a single radio should also work with ESA's Moonlight ([NASA](https://www.nasa.gov/communicating-with-missions/scan/lcrns/lunanet-interoperability-specification/)).

## How it works

Relay satellites in lunar orbit talk to users on the surface over short "proximity" links, then pass the data to Earth over a "trunk" link. Satellites close to the Moon make it easier to connect, so surface systems can carry smaller radios ([collectSPACE](https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html)). NASA's reference design also asks the satellites to store data and forward it later, using delay-tolerant networking ([Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf)).

For navigation, each relay carries a GPS receiver and a stable clock. It works out its own position and broadcasts it, like a GPS satellite. With four relays in view, a user receiver can compute its position. NASA calls this the Lunar Augmented Navigation Service ([Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf)).

Intuitive Machines has not published Altus specifications. The numbers below are NASA's early reference design (DRM-0), not the flight hardware:

| Item | NASA reference design (DRM-0) |
|---|---|
| Ka-band link, surface to relay | 50 Mbps |
| Ka-band link, relay to surface | 10 Mbps |
| S-band low-rate link | 50 bps to 100 kbps |
| Orbit | 6,500 km circular polar, 13.1 h period |
| Coverage of south pole, 1 satellite | 41% |
| Design life | 8+ years |

Source: [Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf). The same paper says the chosen constellation orbit differs from DRM-0.

## Limitations and open issues

- **Nothing in orbit yet.** Altus-1 has slipped from 2026 to early 2027 ([Aviation Week](https://aviationweek.com/space/space-exploration/intuitive-machines-lunar-communication-satellite-launch-plans-change)), and its ride depends on the IM-3 lander schedule ([Wikipedia](https://en.wikipedia.org/wiki/IM-3)).
- **Launch plan changing.** Earlier plans put two relays on IM-4 ([Wikipedia](https://en.wikipedia.org/wiki/Intuitive_Machines)); a later listing has Altus 2-5 on one dedicated launch in 2028 ([Gunter's Space Page](https://space.skyrocket.de/doc_sdat/altus-1.htm)).
- **No published specs.** Data rates, orbits and PNT accuracy of the real constellation are not public.
- **Full navigation needs four satellites in view**, so PNT will be partial until the constellation is complete ([Esper et al.](https://ntrs.nasa.gov/api/citations/20250003321/downloads/LCRNS_Esper_257.pdf)).
- **Antenna pointing.** Live high-resolution video depends on the antennas deploying and pointing at Earth ([collectSPACE](https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html)).
- **Oversight pending.** NASA's Inspector General is auditing whether the SCaN program can meet Artemis communication needs ([NASA OIG](https://oig.nasa.gov/active-projects/)).
- **Single supplier.** The contract has one awardee ([Wikipedia](https://en.wikipedia.org/wiki/Intuitive_Machines)), so Open Moon also buys service from a second network.
