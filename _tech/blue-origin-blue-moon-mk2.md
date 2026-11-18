---
slug: blue-origin-blue-moon-mk2
title: "Blue Origin Blue Moon Mk2"
alternatives:
  - {name: "SpaceX Starship HLS (and cargo variant)", compare: "The other NASA crew lander. Much larger (52 m tall versus 16 m) and burns methane and oxygen instead of hydrogen and oxygen. It can carry more mass, but crew and cargo sit far above the ground and reach the surface by elevator, which NASA tracks as a top risk.", status: "In development under NASA contract; ship-to-ship propellant transfer not yet demonstrated as of late 2026", url: "https://en.wikipedia.org/wiki/Starship_HLS"}
  - {name: "Blue Origin Blue Moon Mark 1", compare: "Smaller, uncrewed cargo lander from the same company, with one BE-7 engine and up to about 3 t of payload. It is closer to flight and shares avionics and power systems with Mk2, but it cannot carry crew or habitat-sized loads.", status: "Pathfinder flight planned; two Mark 1 missions are meant to fly before the Mk2 demo", url: "https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29"}
  - {name: "CAST Lanyue (China)", compare: "Two-crew lander for China's crewed lunar programme. It drops its propulsion stage before landing and is far smaller than Mk2. Not available to outside programmes today.", status: "Integrated landing and ascent tests done in Aug 2025; first crewed landing targeted before 2030", url: "https://en.wikipedia.org/wiki/Lanyue"}
  - {name: "ESA Argonaut", compare: "European uncrewed cargo lander carrying up to about 1.5 t. It covers medium cargo only, so it cannot replace Mk2 for crew or heavy items, but it adds a non-US supplier.", status: "In development; first launch planned for 2030 on Ariane 6", url: "https://en.wikipedia.org/wiki/Argonaut_%28lunar_lander%29"}
links:
  - {title: "NASA OIG IG-26-004: NASA's management of the Human Landing System contracts", url: "https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf", kind: official, date: "Mar 2026"}
  - {title: "NASA HLS program, IAC 2026 presentation (Blue Moon specs, cargo variants, habitat delivery)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", kind: official, date: "Oct 2026"}
  - {title: "NASA selects Blue Origin as second Artemis lunar lander provider", url: "https://www.nasa.gov/news-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/", kind: official, date: "May 2023"}
  - {title: "NASA shares plans to accelerate Artemis, return to Moon", url: "https://www.nasa.gov/missions/artemis/nasa-shares-plans-to-accelerate-artemis-return-to-moon/", kind: official, date: "Nov 2026"}
  - {title: "NASA: Human Landing System program page", url: "https://www.nasa.gov/humans-in-space/human-landing-system/", kind: official, date: "accessed Nov 2026"}
  - {title: "Blue Moon (spacecraft), Wikipedia", url: "https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29", kind: wiki, date: "accessed Nov 2026"}
  - {title: "BE-7 engine, Wikipedia", url: "https://en.wikipedia.org/wiki/BE-7", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Human Landing System, Wikipedia", url: "https://en.wikipedia.org/wiki/Human_Landing_System", kind: wiki, date: "accessed Nov 2026"}
  - {title: "New Glenn launch vehicle, Wikipedia", url: "https://en.wikipedia.org/wiki/New_Glenn", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Starship HLS, Wikipedia", url: "https://en.wikipedia.org/wiki/Starship_HLS", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

Blue Moon Mk2 (Mark 2) is Blue Origin's crewed lunar lander. NASA picked it in May 2023 as its second Human Landing System, after SpaceX's Starship. The deal is a firm-fixed-price contract that NASA [announced at $3.4 billion](https://www.nasa.gov/news-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/). It includes one uncrewed demonstration landing before a crewed mission. The [NASA Inspector General](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) counts it as about $3.1 billion because it leaves out the cargo-lander line items. By December 2025 that value had grown by only $13 million, less than 1 percent.

Blue Origin leads a "National Team". It first included Astrobotic, Boeing, Draper, Honeybee Robotics and Lockheed Martin. Blue Origin later took some of the transporter tank work in-house ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). The company adds capability step by step. Two flights of the smaller [Blue Moon Mark 1](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29) cargo lander are meant to test propulsion, cryogenic fluid management and precision landing before the Mk2 demo ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).

Status in late 2026: the critical design review has slipped several times. The uncrewed demo is expected in **February 2029** ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). NASA's newer plan has a Blue Moon test article dock with Orion in Earth orbit on Artemis III in 2027. Both lander providers are aiming to support a crewed landing in 2028 ([NASA](https://www.nasa.gov/missions/artemis/nasa-shares-plans-to-accelerate-artemis-return-to-moon/)).

## Why Open Moon uses it

Open Moon needs two things it cannot build itself: **crew transport** and **heavy cargo** (about 15 t per landing). Both are part of Open Moon's transport plan. NASA says cargo versions of both crew landers will deliver about [15 t (33,000 lb) each](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf). NASA also intends to give Blue Origin the job of landing a lunar surface habitat [no earlier than FY2033](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf). That ties Mk2 cargo directly to the plan's first habitat (M08).

Mk2 is Open Moon's second heavy lander, after Starship. Having two suppliers means one failure or delay does not ground the base. Mk2 also has a practical edge: crew use stairs about [6 feet (1.8 m) off the ground](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf), not an elevator high above the surface. Without Mk2, every habitat, reactor and large ISRU plant would depend on one vehicle. The alternative is to split them into pieces small enough for medium landers.

## How it works

The lander is [16 m (52 ft) tall](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf). It has three BE-7 engines that burn liquid hydrogen and liquid oxygen, and it launches inside the payload fairing of a New Glenn rocket. The crew cabin sits at the bottom of the vehicle. The [BE-7](https://en.wikipedia.org/wiki/BE-7) is a dual-expander engine rated at up to 44 kN, and it can throttle down to 8.9 kN ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29)).

Hydrogen and oxygen give high performance, but hydrogen boils off at about 20 K. Blue Origin is developing a solar-powered system to reduce boiloff for long storage ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29)). NASA has stepped up its oversight of the lander's cryocoolers ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).

The mission depends on refuelling. In the contract plan, a transporter goes up to low Earth orbit first and works as a propellant depot. Several refuelling flights then fill the transporter, and it hands propellant to the lander in stages on the way to lunar orbit ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). In the 2026 redesign, transfer stages in Earth orbit push Mk2 toward the Moon. There it meets Orion in a closer lunar orbit ([NASA](https://www.nasa.gov/missions/artemis/nasa-shares-plans-to-accelerate-artemis-return-to-moon/)).

| Specification | Value |
|---|---|
| Height | 16 m (52 ft) ([NASA](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf)) |
| Engines | 3 × BE-7, LH2/LOX ([NASA](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf)) |
| Launcher | New Glenn, from LC-36, Florida ([NASA](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf)) |
| Crew to surface | 2, about one week, on the original Artemis V plan ([NASA](https://www.nasa.gov/news-release/nasa-selects-blue-origin-as-second-artemis-lunar-lander-provider/)) |
| Surface stay (design) | Up to 30 days ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29)) |
| Cargo variant | About 15 t ([NASA](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf)); Wikipedia lists 20 t reusable or 30 t one-way ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29)) |
| Launch / dry mass | Over 45 t / 16 t ([Wikipedia](https://en.wikipedia.org/wiki/Blue_Moon_%28spacecraft%29)); NASA has not published an official figure |
| Tilt limit after landing | 8° or less, set by NASA ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)) |

## Limitations and open issues

- **Refuelling is unproven.** The architecture depends on storing hydrogen and oxygen in space and transferring them between vehicles several times. The OIG calls cryogenic fluid management one of Blue Origin's most significant challenges ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).
- **Schedule slips.** The critical design review moved from December 2024 to August 2025, and a further slip to July 2026 was expected. As of August 2025, nearly half of the requests for action from the preliminary design review were still open. Blue Origin had to mature its propulsion, cut mass and improve propellant margins ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).
- **No flight yet.** The uncrewed demo is expected in February 2029 ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). The cargo variant has no published flight date. Habitat delivery is no earlier than FY2033 ([NASA](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf)).
- **Spacesuit interface.** A mismatch in the don/doff station means Blue Origin may need to redesign the airlock or build its own hardware. That could add time and cost ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).
- **Landing risk.** Uneven south-pole terrain could exceed the 8° tilt limit. Decisions on manual control had not yet been made as of November 2025 ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).
- **Depends on New Glenn.** New Glenn reached orbit in January 2025 and landed its booster in November 2025 ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). The refuelling plan still needs a fleet of tanker launches for each mission ([OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)).
- **Commercial access is unclear.** No price per cargo landing or per crew seat for non-NASA customers has been published.
