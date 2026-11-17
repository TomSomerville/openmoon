---
slug: lunar-surface-manipulation-system-lsms
title: "Lunar Surface Manipulation System (LSMS)"
alternatives:
  - {name: "Davit or pulley-and-reel lowering", compare: "A fixed boom or a set of pulleys and reels lowers one payload from the lander. Simple and flight-proven on Apollo, but each unit is built for a single payload, cannot place cargo precisely and is usually left behind after one use.", status: "Flown: Apollo 15-17 lowered the 210 kg rover with pulleys and braked reels; telescoping davit cranes studied by NASA in 2020-22", url: "https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_lrv.html"}
  - {name: "Deployable ramps with a winch", compare: "Inflatable or folding metal ramps give wheeled cargo a path from the deck to the ground. Light and mechanically simple, but only work for payloads that can drive or be skidded down, and a rock or slope at the ramp foot can block them.", status: "Concept studies by NASA (ICES 2022 trade); no lunar ramp offload flown yet", url: "https://ntrs.nasa.gov/citations/20220005086"}
  - {name: "ATHLETE wheel-on-leg robot", compare: "A six-legged JPL rover whose limbs double as arms, so it can both carry and lift cargo. More mobile and dexterous than LSMS, but much heavier and more complex for the load it lifts.", status: "Ground prototypes tested by JPL; not funded for flight", url: "https://en.wikipedia.org/wiki/ATHLETE"}
  - {name: "Serial robotic arm (InSight-style)", compare: "A conventional arm with a motor at every joint. Proven on the Moon and Mars and precise, but flown arms reach only 0.75-2.2 m and lift at most 45 kg, so they do not scale to tonne-class cargo.", status: "Flight-proven at small scale (InSight arm placed a 29 kg seismometer on Mars)", url: "https://ntrs.nasa.gov/citations/20210022100"}
links:
  - {title: "NASA NTRS: LSMS Overview for Blue Origin (proposal slides)", url: "https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf", kind: official, date: "Aug 2020"}
  - {title: "Doggett et al.: Design and Field Test of a Mass Efficient Crane for Lunar Payload Handling (AIAA SPACE 2008)", url: "https://ntrs.nasa.gov/citations/20080040185", kind: paper, date: "Sep 2008"}
  - {title: "Dorsey et al.: Developments to Increase the Performance, Versatility and Automation of the LSMS (AIAA SPACE 2009)", url: "https://ntrs.nasa.gov/citations/20090034163", kind: paper, date: "Sep 2009"}
  - {title: "Jones: A Protoflight LSMS to Enable High-Load, Long-Reach Lunar Surface Operations (ASCEND 2021)", url: "https://ntrs.nasa.gov/citations/20210022100", kind: paper, date: "Nov 2021"}
  - {title: "NASA: LSMS, a Versatile Lifting Device for Planetary Surface Payload Handling (Excavation and Construction review)", url: "https://ntrs.nasa.gov/citations/20210020847", kind: official, date: "Aug 2021"}
  - {title: "Wong and Cline: LSMS-L35, Miniature Crane for Payload Offloading (ASCEND 2022)", url: "https://ntrs.nasa.gov/citations/20220013968", kind: paper, date: "Oct 2022"}
  - {title: "NASA: LANDO, Developing Autonomous Payload Offloading for Lunar Surface Operations (LSIC poster)", url: "https://ntrs.nasa.gov/citations/20230004222", kind: official, date: "Apr 2023"}
  - {title: "Puig-Navarro et al.: Safe Operational Envelope for the LSMS Family of Cable-Driven Cranes (ASCEND 2024)", url: "https://ntrs.nasa.gov/citations/20240008266", kind: paper, date: "Jul 2024"}
  - {title: "NASA: The Potential for Offloading of Fission Surface Power Systems (NETS 2025)", url: "https://ntrs.nasa.gov/citations/20250004365", kind: official, date: "May 2025"}
  - {title: "Seubert, Martin and Doggett: Structural Sizing for the LSMS Architecture (AIAA SciTech 2026)", url: "https://ntrs.nasa.gov/citations/20250011487", kind: paper, date: "Jan 2026"}
  - {title: "Gill et al.: Lunar Surface Cargo Offloading Concepts (ICES 2022)", url: "https://ntrs.nasa.gov/citations/20220005086", kind: paper, date: "Jul 2022"}
  - {title: "NASA Technology Transfer: Lunar Surface Manipulation System (LAR-TOPS-73)", url: "https://technology.nasa.gov/patent/LAR-TOPS-73", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA NSSDC: The Apollo Lunar Roving Vehicle (deployment by pulleys and reels)", url: "https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_lrv.html", kind: official, date: "accessed Nov 2026"}
  - {title: "ATHLETE, Wikipedia", url: "https://en.wikipedia.org/wiki/ATHLETE", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

The LSMS is a lightweight, cable-driven crane-arm for unloading cargo from lunar landers. It was designed at NASA Langley Research Center. It looks like a small tower crane but moves like a robot arm. Most recent NASA papers call it the *Lightweight* Surface Manipulation System. It can hang a load from a hoist like a crane. It can also grip a payload rigidly with a tool at its tip and place it precisely ([Doggett et al. 2008](https://ntrs.nasa.gov/citations/20080040185)). NASA offers the design for licensing ([NASA Technology Transfer](https://technology.nasa.gov/patent/LAR-TOPS-73)).

The first test-bed was built to lift one metric ton at its tip on the Moon. It had a 7.5 m reach and stood 3.8 m tall at the shoulder, so it could unload landers with 5-6 m deck heights. It was field tested at Moses Lake, Washington, in 2008 ([Doggett et al. 2008](https://ntrs.nasa.gov/citations/20080040185)). Later work added a forklift mode, regolith digging and quick-change tools. A second-generation design aimed for three times the payload at about the same mass ([Dorsey et al. 2009](https://ntrs.nasa.gov/citations/20090034163)). In 2020 NASA proposed a 3-year, $22M project to build an engineering unit and a proto-flight unit, taking the LSMS from TRL 4 to TRL 6 ([NASA 2020](https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf)). A 4-year protoflight project then started under NASA's Space Technology Mission Directorate. Its target was 1,000 kg at 8 m reach on the Moon, flying as a demo on a large cargo lander ([Jones 2021](https://ntrs.nasa.gov/citations/20210022100)).

Two lab prototypes exist at Langley: the LSMS-L1000 (1,000 kg) and the small LSMS-L35 (35 kg) ([Seubert et al. 2026](https://ntrs.nasa.gov/citations/20250011487)). The L35 has a 2.25 m reach and is sized for small commercial (CLPS) landers ([Wong and Cline 2022](https://ntrs.nasa.gov/citations/20220013968)). The LANDO project is building autonomy software for it ([NASA 2023](https://ntrs.nasa.gov/citations/20230004222)). No LSMS has flown. We found no public record that the protoflight unit was finished or given a flight.

## Why Open Moon uses it

Milestone M02 (Transport) must deliver cargo to the surface, not just to a lander deck. Its exit criteria include an offloading crane tested on the Moon. Tall landers put cargo several metres above the ground. NASA's own study found that cargo height and whether cargo can move itself matter most when choosing how to offload ([Gill et al. 2022](https://ntrs.nasa.gov/citations/20220005086)). In 2023, CLPS missions had no general offloading capability: payloads other than rovers stayed on the lander ([NASA 2023](https://ntrs.nasa.gov/citations/20230004222)).

LSMS fills that gap with one reusable machine. A davit or ramp is built for one payload. An LSMS can unload many payloads and, with self-offloading, serve many landers ([Seubert et al. 2026](https://ntrs.nasa.gov/citations/20250011487)). NASA has sized one for a 7-tonne, 40 kWe fission reactor, with members of about 146 kg, or 2% of the payload mass ([Seubert et al. 2026](https://ntrs.nasa.gov/citations/20250011487)). Without such a crane, every later milestone would need its own custom offloading hardware, adding mass to every delivery.

## How it works

The LSMS is a truss. Rigid members (kingpost, arm, forearm) carry compression. Cables and rods carry tension. The motors do not sit at the joints. They sit at the base and pull cables over lever arms called spreaders, which gives mechanical advantage and allows small motors ([Doggett et al. 2008](https://ntrs.nasa.gov/citations/20080040185)). Because members work in tension and compression rather than bending, it is far lighter than a serial arm for the same load ([NASA 2020](https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf)). It has three main joints: waist, shoulder and elbow. It can lift about twice as much at the elbow as at the wrist ([Puig-Navarro et al. 2024](https://ntrs.nasa.gov/citations/20240008266)). The protoflight design replaces steel cable with Vectran webbing and adds a base that self-levels up to ±15° on a tilted lander ([Jones 2021](https://ntrs.nasa.gov/citations/20210022100)).

| Version | Lunar lift (wrist) | Reach | Source |
|---|---|---|---|
| 2008 test-bed | 1,000 kg | 7.5 m | [Doggett 2008](https://ntrs.nasa.gov/citations/20080040185) |
| Protoflight target (L1000) | 1,000 kg | 8 m | [Jones 2021](https://ntrs.nasa.gov/citations/20210022100) |
| LSMS-L35 | 35 kg | 2.25 m | [Wong and Cline 2022](https://ntrs.nasa.gov/citations/20220013968) |
| 2020 HLS-class concept | 5,000 kg (10,000 kg near base) | three 4 m links | [NASA 2020](https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf) |
| HLS-class mass goal | 500 kg system mass | | [NASA 2020](https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf) |

NASA says the design scales from about 2 m and 100 kg to about 15 m and 10,000 kg ([Jones 2021](https://ntrs.nasa.gov/citations/20210022100)).

## Limitations and open issues

- **Never flown.** All testing is on Earth. The planned demo assumed a Class-D, two-week mission and did not include lander integration or system tests ([NASA 2020](https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf)).
- **Limited environment testing.** Thermal vacuum testing was planned only at subsystem level, not on the whole unit ([Jones 2021](https://ntrs.nasa.gov/citations/20210022100)).
- **Unclear status.** Public papers do not say whether the protoflight unit was completed, or whether a flight has been booked.
- **Dust and long life.** The demo was sized for one lunar day, where dust impact was expected to be minimal ([Jones 2021](https://ntrs.nasa.gov/citations/20210022100)). A base crane must survive many lunar nights and years of dust. That is unproven.
- **Cable dynamics.** In low gravity, a cable can lose tension during fast moves, so safe speed limits must be enforced ([Puig-Navarro et al. 2024](https://ntrs.nasa.gov/citations/20240008266)).
- **Autonomy still in development.** Unloading from a tilted deck and judging whether a payload is safe to lift are still being developed ([NASA 2023](https://ntrs.nasa.gov/citations/20230004222)).
- **Heavy cargo.** The largest built prototype is 1,000 kg class. Multi-tonne versions exist only as sizing studies ([Seubert et al. 2026](https://ntrs.nasa.gov/citations/20250011487)).
