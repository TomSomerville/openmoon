---
id_code: M02
order: 2
title: Transport to the surface
phase: 0
window: "Years 0–4"
summary: Secure reliable rides for cargo of every size and for crews. Open Moon buys transport; it does not build rockets.
objective: "Establish contracts and interfaces for three cargo classes (under 1 t, about 3 t, about 15 t) and for crew seats, so every later milestone can count on a delivery schedule. Build the equipment to offload cargo on the surface."
trl_min: 6
depends_on: [M00]
spec:
  - {k: "Small cargo", v: "Under 1 t: commercial landers (Blue Ghost, Griffin, Nova-C)"}
  - {k: "Medium cargo", v: "About 3 t: Blue Moon Mark 1"}
  - {k: "Heavy cargo", v: "About 15 t: Starship and Blue Moon Mk2 cargo variants"}
  - {k: Crew, v: "Government crew flights (such as NASA Artemis) or commercial HLS seats"}
  - {k: "Crew cadence", v: "From Phase 2: crews of 3, 4 landings and 4 departures a year (DD-006)"}
cost: {low: 0.95, high: 2.2, note: "interfaces, offloading and integration only; each delivery is costed in the milestone that uses it"}
cost_items:
  - {item: "Common payload interface and integration team (5 years)", low: 0.15, high: 0.4, basis: "ESTIMATE"}
  - {item: "Surface offloading crane ×2 (LSMS-class)", low: 0.1, high: 0.3, basis: "NASA proposed a $22M Phase I to reach a TRL 6 proto-flight LSMS [src 7]; flight units and delivery added (ESTIMATE)"}
  - {item: "Delivery of 2 cranes (~1 t total) on small/medium landers", low: 0.6, high: 1.2, basis: "1 t × $0.6–1.2M/kg (ESTIMATE; $1.2M/kg is Astrobotic's published price)"}
  - {item: "Schedule and cost-growth reserve (30%)", low: 0.1, high: 0.3, basis: "Total value of NASA's first eight CLPS task orders grew nearly 26% [src 9]"}
exit_criteria:
  - "Firm delivery contracts or reservations for at least two independent providers in each cargo class."
  - "A published Open Moon payload interface standard (mechanical, electrical, data) that fits all selected landers."
  - "An offloading crane delivered and tested on the surface, able to lift cargo from a lander deck to the ground."
  - "Crew transport agreement in place for Phase 2: 4 crew landings and 4 departures a year, crews of 3, each crew's vehicle able to wait about 6.5 months on the surface."
workstreams:
  - name: Small cargo (under 1 t)
    desc: Buy rides on commercial landers for instruments and small robots.
    items: ["Firefly Blue Ghost", "Astrobotic Griffin", "Intuitive Machines Nova-C", "Two providers per payload where possible"]
  - name: Medium cargo (about 3 t)
    desc: Rovers, power units and pilot plants.
    items: ["Blue Origin Blue Moon Mark 1 (up to 3 t)", "Track Pathfinder flight (NET Q1 2027)"]
  - name: Heavy cargo (about 15 t)
    desc: Habitats, reactors and large ISRU plants.
    items: ["Starship cargo variant", "Blue Moon Mk2 cargo variant", "NASA states ~15 t per cargo landing"]
  - name: Crew access
    desc: Seats for Open Moon crews.
    items: ["NASA Artemis crew flights (Orion and HLS)", "Commercial HLS seats once offered", "4 crew landings and 4 departures a year from Phase 2 (DD-006)", "Return vehicle that can wait ~6.5 months on the surface", "Crew training and medical certification"]
  - name: Offloading and handling
    desc: Getting cargo off tall landers safely.
    items: ["Cable-driven crane (LSMS heritage)", "Ramps and winches", "Payload carts towed by LTVs"]
  - name: Interfaces
    desc: One standard so payloads fit any lander.
    items: ["Mechanical bolt pattern and loads", "Power and data connectors", "Thermal and dust covers"]
technologies:
  - {name: "Firefly Blue Ghost lander", use: "Small cargo", status: "Fully successful landing Mar 2025; 14 days of operations", trl: 9, src: 1}
  - {name: "Intuitive Machines Nova-C", use: "Small cargo", status: "Landed twice (2024, 2025); both times ended on its side", trl: 7, src: 2}
  - {name: "Astrobotic Griffin", use: "Small cargo", status: "First flight planned January 2027", trl: 6, src: 2}
  - {name: "Blue Origin Blue Moon Mark 1", use: "Medium cargo (up to 3 t)", status: "Pathfinder to Shackleton connecting ridge NET Q1 2027", trl: 6, src: 3}
  - {name: "SpaceX Starship HLS / cargo", use: "Heavy cargo and crew", status: "Starship reached orbit on flights 14 and 15 (2026); ship caught by the tower after flight 15", trl: 6, src: 4}
  - {name: "Blue Origin Blue Moon Mk2", use: "Crew; cargo variant", status: "~$3.1B NASA contract; uncrewed demo expected Feb 2029", trl: 5, src: 5}
  - {name: "Lunar Surface Manipulation System (LSMS)", use: "Offloading crane", status: "Ground prototypes tested; NASA proposed path to TRL 6", trl: 4, new: true, src: 7}
sources:
  - {title: "Firefly: Blue Ghost completes 14 days of surface operations", url: "https://fireflyspace.com/news/firefly-aerospace-successfully-completes-14-days-of-surface-operations-on-the-moon", date: "Mar 2025"}
  - {title: "Commercial Lunar Payload Services, Wikipedia", url: "https://en.wikipedia.org/wiki/Commercial_Lunar_Payload_Services", date: "accessed Nov 2026"}
  - {title: "Blue Origin: Blue Moon Mark 1", url: "https://www.blueorigin.com/blue-moon/mark-1", date: "accessed Nov 2026"}
  - {title: "Starship flight 15, Wikipedia", url: "https://en.wikipedia.org/wiki/Starship_flight_15", date: "Nov 2026"}
  - {title: "NASA OIG IG-26-004: Management of the Human Landing System contracts", url: "https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf", date: "Mar 2026"}
  - {title: "NASA HLS IAC 2026 presentation (cargo landers ~15 t)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "NASA NTRS: LSMS technology overview", url: "https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf", date: "2020"}
  - {title: "Astrobotic Lunar Landers Payload User's Guide ($1.2M/kg)", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "NASA OIG IG-24-013: CLPS initiative", url: "https://oig.nasa.gov/wp-content/uploads/2024/06/final-report-ig-24-013-nasas-commercial-lunar-payload-services-initiative.pdf", date: "Jun 2024"}
  - {title: "NASA: NASA Shares Plans to Accelerate Artemis, Return to Moon", url: "https://www.nasa.gov/missions/artemis/nasa-shares-plans-to-accelerate-artemis-return-to-moon/", date: "Nov 2026"}
  - {title: "NASA: NASA Awards Moon Base Transportation, Technology, Science Projects (CLPS 2)", url: "https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/", date: "Nov 2026"}
  - {title: "NASA: NASA Unveils Initiatives to Achieve America's National Space Policy", url: "https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/", date: "Mar 2026"}
  - {title: "NASA: Artemis II mission milestones, an image and video recap", url: "https://www.nasa.gov/centers-and-facilities/johnson/artemis-ii-mission-milestones-an-image-and-video-recap/", date: "Apr 2026"}
risks:
  - {sev: Critical, title: "Heavy cargo landers are not yet proven: Starship has not demonstrated orbital refuelling, and Blue Moon Mk2's demo is expected in 2029", fix: "Keep everything in Phase 0 within small and medium lander sizes, and plan heavy landers only from Phase 1 (habitats); design heavy items to split across two providers; set schedule margin of 2+ years"}
  - {sev: High, title: "Landing reliability: of four CLPS missions in 2024–25, two landers tipped over and one never attempted a landing", fix: "Fly critical items twice; prefer providers with upright landings; insure or hold spares"}
  - {sev: High, title: "Cost and schedule growth: CLPS orders grew nearly 26% in total value and slipped 14 months on average", fix: "Budget 30% growth on every delivery; plan for slips in the schedule"}
  - {sev: Medium, title: "Tall landers (Starship) put cargo many metres above the ground", fix: "Crane or elevator on the lander; LSMS-style cable crane on the surface"}
  - {sev: High, title: "Crew seats depend on government programmes, and this plan needs a crewed landing every 3 months, twice NASA's planned rate of one every six months after Artemis V", fix: "Plan crew flights at this cadence from the start; contract two crew transport providers; keep commercial-seat option open; let a tour stretch by one cycle if a landing slips"}
  - {sev: High, title: "Each crew's vehicle must wait about 6.5 months on the surface as its way home, with up to three parked at once at handovers; no crewed lander has published a stay that long", fix: "Make surface wait time a contract requirement; power, shade and inspect parked vehicles; keep a rescue option"}
---

## Where transport stands (November 2026)

- **Artemis II** flew four astronauts around the Moon on 1–10 April 2026<sup class="r">[13](#s13)</sup>.
- **Artemis III** is now a 2027 test in Earth orbit. Orion will dock with Starship and Blue Moon test articles there. **The first crewed landing is Artemis IV, planned for 2028**<sup class="r">[10](#s10)</sup>.
- **NASA plans** at least one landing a year after Artemis III, then a crewed landing every six months after Artemis V<sup class="r">[12](#s12)</sup>.
- **CLPS 2**, a 10-year contract worth up to $10B in total, was awarded to eight companies in November 2026<sup class="r">[11](#s11)</sup>.
- **Bottom line:** there is a growing commercial market to buy rides from.

{% include decision-note.html id="DD-011" extra="See Lander candidates for each lander's published slope limit and payload." %}

- **Landing rule:** every Open Moon delivery lands on ground of 8° or less. Slope limits and payloads for ten landers are compared on the [Lander candidates]({{ '/landers/' | relative_url }}) page.
- **Same ground as NASA:** Blue Moon Mark 1's Pathfinder targets the Shackleton connecting ridge, inside Open Moon's focus area (DD-010).

## How much does it cost to land a kilogram?

- **Published price:** Astrobotic lists **$1.2M per kg** to the surface<sup class="r">[8](#s8)</sup>.
- **Cost growth:** NASA's first eight CLPS delivery orders grew nearly **26%** in total value and slipped **14 months** on average<sup class="r">[9](#s9)</sup>.
- **Heavy landers:** NASA expects cargo landers to carry about 15 t each<sup class="r">[6](#s6)</sup>. We found no published price for them. This plan assumes **$0.2–0.6M per kg** (ESTIMATE) and shows that assumption wherever it's used.

This is the single most important number in the plan. Every kilogram made on the Moon instead of shipped saves hundreds of thousands of dollars, which is why ISRU (M06, M11, M12) gets priority.

## Step-by-step

1. **Publish the payload interface standard:** bolt pattern, loads, power and data connectors. Every Open Moon payload uses it.
2. **Reserve small-lander rides** for M01 and M03 payloads, with two providers per critical payload.
3. **Book medium-lander slots** on Blue Moon Mark 1 (up to 3 t<sup class="r">[3](#s3)</sup>) for rovers, pilot plants and the first power units. Watch the Pathfinder flight, planned no earlier than Q1 2027.
4. **Negotiate heavy-cargo slots** for habitats and the reactor. Starship reached orbit on flights 14 and 15 in 2026<sup class="r">[4](#s4)</sup>, but ship-to-ship propellant transfer has never been done<sup class="r">[5](#s5)</sup> and was still listed as an upcoming test in October 2026<sup class="r">[6](#s6)</sup>. Every heavy item has a fallback design that splits into medium-lander pieces.
5. **Build and land the offloading crane.** It's based on NASA's LSMS cable-driven crane, which has been tested on the ground<sup class="r">[7](#s7)</sup>.
6. **Sign a crew transport agreement** for Phase 2.

## Crew cadence for Phase 2

{% include decision-note.html id="DD-006" extra="Crew transport was booked for four short sorties and then two rotations a year. It is now 4 crew landings and 4 departures a year." %}

- **Crews of 3.** A new crew lands every 3 months and stays about 6.5 months (DD-006).
- **This plan's arithmetic.** 12 months ÷ 3 months = **4 arrivals a year**, and in steady state **4 departures a year**.
- **Against NASA's plan.** NASA plans a crewed landing every six months after Artemis V<sup class="r">[12](#s12)</sup>. This plan needs twice that rate, so it needs more than one provider.
- **Waiting vehicles.** Each crew's vehicle is its way home, so it waits on the surface for the whole tour. At a handover up to three may be on site at once (plan design; open question).
- **Spare seat.** Artemis II flew four astronauts<sup class="r">[13](#s13)</sup>. If crew vehicles keep four seats, a crew of 3 leaves one free for cargo, a visitor or a medical return (plan design).
