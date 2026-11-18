---
id_code: "C07.1"
milestone: M07
order: 1
title: Utility robots and payload carts
summary: "Unpowered carts that LTVs tow between pads and sites, plus small inspection rovers that patrol power cables, so cargo moves and checks happen without crew."
trl: 5
spec:
  - {k: "Fleet", v: "2 payload carts + 2 inspection rovers (design choice)"}
  - {k: "Total delivered mass", v: "~250 kg including spares (M07 budget)"}
  - {k: "Cart mass", v: "~50 kg each (ESTIMATE)"}
  - {k: "Cart payload", v: "500 kg rated (design choice; must match LTV tow limit, not yet published)"}
  - {k: "Payload deck", v: "Open Moon payload interface (C02.1)"}
  - {k: "Inspection rover", v: "~25 kg, carry-on-bag scale, solar and battery (ESTIMATE)"}
  - {k: "Patrol", v: "M04 cable routes, each 3 km or less (DD-010)"}
  - {k: "Control", v: "Autonomous with Earth supervision at 6–8 s delay"}
  - {k: "Life", v: "5 years (design goal)"}
subcomponents:
  - name: Cart chassis
    desc: "A light, unpowered two-axle frame with large wheels that rolls behind an LTV."
    parts: ["Aluminium frame", "Four rigid wire-mesh or grousered wheels", "Sealed wheel bearings with dust covers", "Parking brake", "Tie-down points"]
    tech: "Apollo 14 MET (hand-pulled cart); LRV wheel heritage"
    trl: 6
  - name: Hitch
    desc: "A tow bar and coupling that an LTV can pick up and drop without crew."
    parts: ["Rigid tow bar with self-aligning coupler", "Remote release latch", "Fiducial marker for automatic docking", "Load and angle sensor"]
    tech: "Plan design choice; LTV tow interface not yet published"
    trl: 4
  - name: Payload deck
    desc: "A flat deck with the standard C02.1 bolt pattern and connectors, so any Open Moon payload can ride on it."
    parts: ["C02.1 mechanical bolt pattern", "C02.1 power and data pass-through", "Crane lift points (LSMS-class)", "Dust cover"]
    tech: "Open Moon payload interface standard (C02.1)"
    trl: 4
  - name: Inspection rover
    desc: "A small solar-powered rover that drives along cable routes and around the base, looking for damage."
    parts: ["Stereo cameras and lights", "Thermal camera to spot hot joints", "Mesh radio", "Solar panel and battery", "Four-wheel chassis"]
    tech: "NASA/JPL CADRE rovers"
    trl: 6
  - name: Teleoperation and autonomy
    desc: "Robots run set routes on their own; drivers on Earth step in for hitching and unusual events."
    parts: ["Route maps from M05 road survey", "Onboard hazard detection", "Earth control station with delay simulator", "Fault reports to the base network"]
    tech: "NASA LTV delay tests; CADRE autonomy"
    trl: 6
risks:
  - {sev: High, title: "Neither selected LTV has published a towing capacity or hitch interface", fix: "Agree a tow interface with Astrolab and Lunar Outpost early; size cart payload to the lower tow limit."}
  - {sev: High, title: "Carts can get stuck on rough ground; Apollo 14 crew had to carry the MET over rough terrain", fix: "Use graded M05 roads; large wheels; carts stay on mapped routes."}
  - {sev: Medium, title: "Small rovers like CADRE are built to work for one lunar day, about 14 Earth days", fix: "Add batteries and heaters for night survival, or park the rovers in a heated shelter at night."}
  - {sev: Medium, title: "Automatic hitching has never been done on the Moon", fix: "Test on Earth with real LTV prototypes; fall back to Earth-driven hitching or crew help."}
  - {sev: Medium, title: "Dust wears wheel bearings over long distances", fix: "Sealed, covered bearings; spare wheels in the 250 kg budget; sintered road sections (M05)."}
  - {sev: Medium, title: "Inspection rover near 3 kV AC grid cables could short or be damaged", fix: "Keep a set distance from cables; inspect by camera only; never touch the cable."}
sources:
  - {title: "Wikipedia: Modular Equipment Transporter", url: "https://en.wikipedia.org/wiki/Modular_Equipment_Transporter", date: "accessed Nov 2026"}
  - {title: "NASA RELEASE26-046: NASA provides update on Moon Base rovers, landers, missions", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/", date: "May 2026"}
  - {title: "Astrolab: FLEX services", url: "https://astrolab.space/flex-services", date: "accessed Nov 2026"}
  - {title: "JPL: CADRE", url: "https://jpl.nasa.gov/missions/cadre", date: ""}
  - {title: "NASA NTRS 20240001217: LTV remote driving with time delay", url: "https://ntrs.nasa.gov/citations/20240001217", date: "2024"}
  - {title: "NASA NTRS 20220002315: Lunar power transmission for fission surface power", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", date: "2022"}
---

## What it does

Crews should not spend surface time moving boxes. Utility robots do the hauling and routine checks. Payload carts carry cargo from the landing pads to the habitat, the ISRU plant and the power sites. An LTV tows them, with or without crew. Small inspection rovers drive the M04 cable routes and look for damage.

## How it works

**Cart chassis.** The idea is old. On Apollo 14 the crew pulled a two-wheeled cart, the Modular Equipment Transporter (MET). It weighed at most 30 lb empty and carried up to 340 lb. It used the first tyres on the Moon. On rough ground the crew had to lift and carry it<sup class="r">[1](#s1)</sup>. Open Moon's cart has four wheels, so it stands on its own. It runs on graded M05 roads.

**Hitch.** NASA chose two LTVs in May 2026: Astrolab CLV-1 (about 2,000 lb, over 6 mph) and Lunar Outpost Pegasus (over 9 mph, manual, autonomous or teleoperated)<sup class="r">[2](#s2)</sup>. CLV-1 is adapted from Astrolab's FLEX. Astrolab says FLEX carries up to 2,000 kg on a modular payload interface<sup class="r">[2](#s2)</sup><sup class="r">[3](#s3)</sup>. Neither company has published a towing rating. So the hitch is an Open Moon design that must be agreed with both providers. A fiducial marker on the tow bar lets the LTV line up by itself.

**Payload deck.** The deck uses the C02.1 payload interface. A crate that rode on a lander bolts straight onto a cart, with no adapter.

**Inspection rover.** NASA/JPL's CADRE rovers are about the size of a carry-on bag. Each has two stereo cameras and mesh radios, and runs on solar power. They work as a team, mostly without human input, for one lunar day (about 14 Earth days)<sup class="r">[4](#s4)</sup>. Open Moon's inspection rover is a CADRE-class design with a thermal camera added. It drives beside the ±4 kVDC cables that M04 lays<sup class="r">[6](#s6)</sup>, looking for cuts, burial loss and hot joints.

**Teleoperation.** In NASA tests, operators drove an LTV with 4, 6 and 8 s delays, and every operator completed the traverses<sup class="r">[5](#s5)</sup>. Open Moon robots run mapped routes on their own. Earth drivers take over for hitching and for anything unusual.

## Sizing

| Item | Qty | Mass each | Total | Basis |
|---|---|---|---|---|
| Payload cart | 2 | 50 kg | 100 kg | ESTIMATE |
| Inspection rover | 2 | 25 kg | 50 kg | ESTIMATE |
| Hitch kits for LTVs | 2 | 10 kg | 20 kg | ESTIMATE |
| Spares (wheels, bearings, batteries) | — | — | 50 kg | ESTIMATE |
| Charging and shelter kit | 1 | 30 kg | 30 kg | ESTIMATE |
| **Total** | | | **250 kg** | matches M07 budget |

The MET carried about 11 times its own empty mass (340 ÷ 30)<sup class="r">[1](#s1)</sup>. A 50 kg cart rated for 500 kg is a ratio of 10. That is in the same range, on a stronger four-wheel frame.

## Testing and qualification

1. **Cart drop and fatigue tests** with a full load, on rough simulant ground.
2. **Hitch trials** with LTV ground prototypes from both providers, including automatic coupling.
3. **Inspection rover field test** along a real 1 km cable run on Earth, with planted faults.
4. **Thermal vacuum test** of the rover, including a simulated lunar night.
5. **On the Moon:** first cart haul from pad 1 to the power site. Then the first full patrol of a cable route.

## Open questions

- What tow load and hitch will CLV-1 and Pegasus accept?
- Should carts have their own motors so they can move without an LTV?
- Can inspection rovers survive the night, or do they need a heated garage?
- Which faults can a camera find on a buried cable, and which need electrical testing?
