---
id_code: "C02.1"
milestone: M02
order: 1
title: Common payload interface
summary: "One published standard for how every Open Moon payload bolts down, plugs in, stays warm and gets lifted, so the same payload can fly on any selected lander without a redesign."
trl: 6
spec:
  - {k: "Scope", v: "Mechanical, electrical, data, thermal, dust and lifting interfaces"}
  - {k: "Mechanical (small)", v: "Adapter plate onto M5 inserts on a 75 mm grid (matches Astrobotic decks)"}
  - {k: "Mechanical (medium/heavy)", v: "Standard pallet with four hard points, four lifting lugs and forklift pockets (design choice)"}
  - {k: "Power", v: "28 V DC ±5%, two circuits: operations/heaters and actuation"}
  - {k: "Data", v: "RS-422 and SpaceWire, plus Ethernet/IP on the pallet class (design choice); time-at-tone sync"}
  - {k: "Connector", v: "MIL-DTL-38999 Series III, regular and small sizes"}
  - {k: "Thermal", v: "Payload isolated from lander, conductance below 0.1 W/K"}
  - {k: "Release", v: "Non-pyrotechnic, shock below 300 g into the lander"}
  - {k: "Landers covered", v: "Blue Ghost, Griffin, Nova-C, Blue Moon Mk1, Starship and Blue Moon Mk2 cargo"}
  - {k: "Deliverable", v: "Open interface control document, CAD, connector pinouts and test plan"}
subcomponents:
  - name: Mechanical mount and adapter plate
    desc: "Each payload bolts to its own adapter plate, and the plate bolts to the lander, so payload design does not wait for bolt-hole assignment."
    parts: ["Adapter plate (part of payload mass)", "M5 bolts into lander helicoil inserts, 75 mm grid", "Thermal and vibration isolators", "Grounding and bonding strap", "Per-lander adapter drawings"]
    tech: "Astrobotic adapter-plate practice"
    trl: 8
  - name: Pallet and load paths
    desc: "For payloads from about 100 kg up to several tonnes, a standard pallet carries loads into four lander hard points."
    parts: ["Machined aluminium pallet frame", "Four hard-point fittings with shear cones", "Hold-down and release mechanisms", "Forklift tine pockets", "Kinematic seats for reattaching on the surface"]
    tech: "Design choice; release rules from lander user guides"
    trl: 5
  - name: Electrical interface
    desc: "One connector family and one voltage for every lander, with switched, current-limited circuits."
    parts: ["MIL-DTL-38999 Series III connector (regular and small)", "28 V operations and heater circuit", "28 V actuation circuit", "Release-signal lines", "Single-point ground return"]
    tech: "Astrobotic Standard Electrical Connector"
    trl: 8
  - name: Data and timing interface
    desc: "Standard serial links for small payloads, Ethernet/IP for larger ones, and a time pulse so every payload logs the same time."
    parts: ["RS-422 with SLIP/UDP", "SpaceWire for high-rate payloads", "Ethernet/IP (pallet class)", "Time-at-tone sync", "Wireless fallback after deployment (WLAN or LTE)"]
    tech: "Astrobotic data services; LunaNet IP-based architecture"
    trl: 7
  - name: Thermal and dust covers
    desc: "Payloads look after their own temperature and keep their optics and connectors covered until they are clear of landing dust."
    parts: ["Low-conductance standoffs (below 0.1 W/K)", "Payload-owned heaters and radiators", "Multi-layer insulation blankets", "Hinged dust covers released after landing", "Connector dust caps"]
    tech: "Lander user-guide practice; dust covers are a design choice"
    trl: 6
  - name: Lifting points
    desc: "Every payload heavier than a person can lift carries standard lugs and pockets that the offloading crane (C02.2) can grab."
    parts: ["Four lifting lugs on the pallet corners", "Forklift tine pockets", "Hoist spreader bar", "Centre-of-mass marking", "Fiducial targets for crane cameras"]
    tech: "Matches LSMS hoist and forklift tools"
    trl: 5
risks:
  - {sev: High, title: "Lander providers do not publish full interface documents; deck layouts and loads arrive late and change", fix: "Keep payloads independent of bolt holes by using adapter plates. Sign interface agreements early and fund per-lander adapter drawings."}
  - {sev: High, title: "One standard may not fit both 240 kg small landers and 15 t cargo landers", fix: "Define three classes (plate, pallet, heavy pallet) that share the same connector, voltage and data protocols."}
  - {sev: High, title: "Heavy landers put cargo high above the ground (Starship is 52 m tall)", fix: "Put lifting lugs and forklift pockets on every pallet so a lander elevator or the C02.2 crane can handle it."}
  - {sev: Medium, title: "Launch and landing loads differ between landers and launch vehicles", fix: "Qualify each payload to an envelope of all selected landers' environments, using GEVS-style tests."}
  - {sev: Medium, title: "Landing plume dust coats optics, radiators and connectors", fix: "Covers stay closed until after landing and are released only after any nearby landing. Connectors carry dust caps."}
  - {sev: Medium, title: "Power and data per kilogram differ widely between landers", fix: "Design payloads to the lowest common level (1 W/kg, 10 kbps/kg) and buy extra where needed."}
  - {sev: Medium, title: "A release mechanism fails and the payload is stuck on the deck", fix: "Use dual-wound non-pyrotechnic release devices, and allow the crane to free a stuck payload by lifting."}
sources:
  - {title: "Astrobotic Lunar Landers Payload User's Guide", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "Firefly: Blue Ghost lunar lander", url: "https://fireflyspace.com/blue-ghost", date: "accessed Nov 2026"}
  - {title: "Intuitive Machines and Space Applications Services: lunar delivery services (ESA BSGN)", url: "https://bsgn.esa.int/wp-content/uploads/2024/02/02-INTUITIVE-MACHINES-AND-SPACE-APPS-Richard-A.-Trent-M.pdf", date: "Feb 2024"}
  - {title: "Blue Moon (spacecraft), Wikipedia", url: "https://en.wikipedia.org/wiki/Blue_Moon_(spacecraft)", date: "accessed Nov 2026"}
  - {title: "NASA HLS IAC 2026 presentation", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "NASA: Lightweight crane technology could find a home on the Moon (LSMS)", url: "https://www.nasa.gov/centers-and-facilities/langley/lightweight-crane-technology-could-find-a-home-on-the-moon/", date: "Feb 2021"}
  - {title: "NASA: LunaNet Interoperability Specification v5", url: "https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf", date: "Jan 2025"}
  - {title: "Blue Origin: Blue Moon Mark 1", url: "https://www.blueorigin.com/blue-moon/mark-1", date: "accessed Nov 2026"}
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", date: "Mar 2025"}
---

## What it does

Open Moon buys rides on several landers (M02). Each lander company publishes its own payload rules, and no two are the same. The common payload interface is **one Open Moon standard** that sits between our payloads and every lander. A payload built to it needs only a small adapter, not a redesign, to move from one lander to another. That matters because M02 plans to fly critical items twice, on different providers.

## How it works

- **Mechanical.** Astrobotic's decks give about 0.5 m² per side, with locking helicoil inserts for M5 bolts on a 75 mm grid. Astrobotic recommends an adapter plate between payload and deck. The plate counts as payload mass<sup class="r">[1](#s1)</sup>. We adopt the same grid and the adapter-plate rule for small payloads. Larger payloads ride on a standard pallet (our design) that bolts to four lander hard points.
- **Loads.** Astrobotic quotes a random-vibration limit of 14.1 Grms for 2 minutes per axis. It points payloads to NASA's GEVS standard for random, shock and acoustic tests<sup class="r">[1](#s1)</sup>. We qualify every payload to an envelope covering all selected landers.
- **Electrical.** Power comes through a Glenair MIL-DTL-38999 Series III connector. Each payload gets two 28 ± 5% V DC circuits, one for operations and heaters and one for deployments. Both are current-regulated and protected<sup class="r">[1](#s1)</sup>. We adopt the same connector family, voltage and two-circuit split.
- **Data and time.** RS-422 (with SLIP/UDP) or SpaceWire, both carrying "time at the tone" so payload clocks match the lander. After deployment the payload can switch to 802.11n WLAN<sup class="r">[1](#s1)</sup>. LunaNet uses IP networking and expects surface links built on IETF and 3GPP standards<sup class="r">[7](#s7)</sup>, so the pallet class adds Ethernet/IP. Nokia's IM-2 network showed that 3GPP cellular equipment can run on a lander<sup class="r">[9](#s9)</sup>.
- **Thermal and dust.** The payload must be thermally isolated from the lander, with a conductance below 0.1 W/K, and must control its own temperature<sup class="r">[1](#s1)</sup>. We add dust covers on optics and connectors, released after landing.
- **Release.** Surface release devices must be non-pyrotechnic, make little debris and put no more than 300 g of shock into the lander<sup class="r">[1](#s1)</sup>.
- **Lifting.** The LSMS crane has hoist and forklift-tine tools<sup class="r">[6](#s6)</sup>. Every pallet therefore carries four lifting lugs and two tine pockets, so the C02.2 crane can grab it.

## How it maps to each lander

| Lander | Surface payload | Payload power / data | Fit |
|---|---|---|---|
| Firefly Blue Ghost | up to 240 kg<sup class="r">[2](#s2)</sup> | over 400 W; DTE or relay<sup class="r">[2](#s2)</sup> | Plate class on above-deck, interior, inter-deck or below-deck positions<sup class="r">[2](#s2)</sup> |
| Astrobotic Griffin | 625 kg<sup class="r">[1](#s1)</sup> | 1 W and 10 kbps per kg as standard<sup class="r">[1](#s1)</sup> | Plate class, native grid; pallet on request |
| Intuitive Machines Nova-C | 130–150 kg<sup class="r">[3](#s3)</sup> | 300–400 W; up to 8 Mbps<sup class="r">[3](#s3)</sup> | Plate class via per-lander adapter |
| Blue Moon Mk1 | up to 3,000 kg<sup class="r">[4](#s4)</sup><sup class="r">[8](#s8)</sup> | not published | Pallet class; lander is 8.05 m tall, 3.08 m wide<sup class="r">[4](#s4)</sup> |
| Starship / Blue Moon Mk2 cargo | ~15 t<sup class="r">[5](#s5)</sup> | not published | Heavy pallet; Starship is 52 m tall, with crew compartment at the top and an elevator<sup class="r">[5](#s5)</sup>; Mk2 is 16 m<sup class="r">[5](#s5)</sup> |

## Sizing

Power and data budgets per kilogram (arithmetic from the figures above):

- Griffin standard: 1 W/kg, so a 100 kg payload gets 100 W and 100 × 10 = 1,000 kbps.
- Blue Ghost: 400 W ÷ 240 kg ≈ 1.7 W/kg at full load.
- Nova-C: 300–400 W ÷ 130–150 kg ≈ 2.0–3.1 W/kg.

**Design rule (Open Moon choice):** every payload must survive and do its minimum mission on **1 W/kg and 10 kbps/kg**, the lowest common level. Extra power and data are bought per mission.

Pallet classes (design choice, ESTIMATE):

| Class | Payload mass | Mount | Lifting |
|---|---|---|---|
| Plate | up to ~100 kg | Adapter plate, M5 on 75 mm grid | Hand or crane hook |
| Pallet | ~100 kg – 3 t | 4 hard points | 4 lugs + tine pockets |
| Heavy pallet | 3 – 15 t | 4–8 hard points, set per lander | Spreader bar + lander elevator or crane |

## Testing and qualification

1. **Write the standard.** Publish an open interface control document, CAD files and pinouts. Review it with each lander provider.
2. **Fit checks.** Build a mass-and-connector dummy for each class and fit-check it at each provider's integration facility.
3. **Environment tests.** Shake, shock and acoustic-test the dummy pallet to the envelope of all landers' environments (GEVS-style<sup class="r">[1](#s1)</sup>).
4. **Thermal-vacuum test.** Measure the plate's conductance to confirm it stays below 0.1 W/K. Cycle the dust covers in vacuum and cold.
5. **Crane interface test.** Lift dummy pallets with the C02.2 crane's hoist and tines on Earth.
6. **First flight.** The first small payloads (M01, M03) fly on the plate class. The crane's own delivery tests the pallet class on the Moon.

## Open questions

- Will Blue Origin and SpaceX publish payload user guides for Blue Moon Mk1 and Starship cargo? What hard-point spacing do they use?
- Is 28 V enough for payloads above 1 kW, or does the heavy pallet need a higher-voltage bus to match M04's grid?
- Which Ethernet variant survives lunar thermal cycling best: copper SpaceWire-style links or fibre?
- Can an existing industry standard (for example a CubeSat-style rail or an ISS-style connector) replace parts of this one?
