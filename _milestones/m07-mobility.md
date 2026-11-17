---
id_code: M07
order: 7
title: Surface mobility
phase: 2
window: "2028–2033"
summary: Get unpressurised rovers, a pressurised rover and utility robots working on the surface, so crews and cargo can move between every site.
objective: "Have at least two unpressurised crew rovers that can also drive themselves, one pressurised rover for multi-week trips, and a fleet of utility robots for hauling and inspection, all driven remotely from Earth between crew visits."
trl_min: 6
depends_on: [M02, M03, M05]
spec:
  - {k: "Unpressurised", v: "2 × LTV-class (Astrolab CLV-1, Lunar Outpost Pegasus)"}
  - {k: "Pressurised", v: "1 × 2-crew rover, ~28–30-day trips (JAXA/Toyota class)"}
  - {k: "Utility", v: "Carts and small robots for hauling and inspection"}
  - {k: "Teleoperation", v: "Earth-driven with 6–8 s delay tolerance"}
cost: {low: 1.2, high: 3.3, note: "rover services leased or shared through partners"}
cost_items:
  - {item: "LTV services (2 rovers)", low: 0.45, high: 1.0, basis: "NASA's 2026 LTV task orders: $219M (Astrolab) + $220M (Lunar Outpost) [src 1]; high side adds services growth"}
  - {item: "Pressurised rover: partnership share", low: 0.5, high: 1.5, basis: "ESTIMATE; cost share in a JAXA-led programme"}
  - {item: "Utility robots, carts and spares, including delivery (~250 kg)", low: 0.2, high: 0.6, basis: "ESTIMATE; 250 kg × $0.6–1.2M/kg delivery plus hardware"}
  - {item: "Teleoperation centre and driver training", low: 0.05, high: 0.2, basis: "ESTIMATE"}
exit_criteria:
  - "Two LTVs operating at the base, each having driven at least 100 km, including driverless traverses commanded from Earth."
  - "Pressurised rover completes a crewed 14-day trip with resupply."
  - "Utility robots haul cargo from pads to sites without crew help."
workstreams:
  - name: Unpressurised rovers (LTV)
    desc: Lease rovers that carry suited crew and drive themselves when no one is there.
    items: ["Astrolab CLV-1 (~2,000 lb, >6 mph)", "Lunar Outpost Pegasus (up to 1 year, >9 mph)", "Delivery by Blue Origin in 2028"]
  - name: Pressurised rover
    desc: A mobile habitat for long trips.
    items: ["JAXA/Toyota Lunar Cruiser class", "2 crew, ~28–30-day trips", "Suitports or airlock"]
  - name: Utility robots
    desc: Do the hauling so crews don't have to.
    items: ["Payload carts towed by LTVs", "Small inspection rovers", "Cable inspection along M04 routes"]
  - name: Teleoperation
    desc: Drive rovers from Earth between crew visits.
    items: ["Delay-tolerant driving at 6–8 s", "Autonomous hazard avoidance", "Driver training on simulators"]
technologies:
  - {name: "Astrolab CLV-1 (LTV)", use: "Crew and cargo rover", status: "NASA task order $219M (May 2026); flight hardware due end 2027; delivery 2028", trl: 6, src: 1}
  - {name: "Lunar Outpost Pegasus (LTV)", use: "Crew and cargo rover", status: "NASA task order $220M (May 2026); delivery 2028", trl: 6, src: 1}
  - {name: "JAXA/Toyota pressurised rover (Lunar Cruiser)", use: "Long crewed trips", status: "2024 agreement: 2 crew up to 30 days, ~10-year life; NASA lists 28 days; cargo delivery NET FY2032", trl: 5, src: 3}
  - {name: "Delay-tolerant teleoperation", use: "Earth-driven rovers", status: "NASA LTV studies: operators completed traverses at 4, 6 and 8 s delay (2023)", trl: 6, src: 5}
  - {name: "NASA CADRE autonomous rovers", use: "Multi-robot autonomy heritage", status: "Delivered for IM-3, NET Q1 2027", trl: 6, src: 6}
sources:
  - {title: "NASA RELEASE26-046: NASA provides update on Moon Base rovers, landers, missions", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/", date: "May 2026"}
  - {title: "NASA: NASA selects companies to advance Moon mobility for Artemis missions (LTV $4.6B IDIQ)", url: "https://www.nasa.gov/news-release/nasa-selects-companies-to-advance-moon-mobility-for-artemis-missions/", date: "Apr 2024"}
  - {title: "NASA: NASA, Japan advance space cooperation, sign agreement for lunar rover", url: "https://www.nasa.gov/news-release/nasa-japan-advance-space-cooperation-sign-agreement-for-lunar-rover/", date: "Apr 2024"}
  - {title: "NASA Moon Base – Phases", url: "https://www.nasa.gov/moonbase-phases/", date: "2026"}
  - {title: "NASA NTRS 20240001217: LTV remote driving with time delay", url: "https://ntrs.nasa.gov/citations/20240001217", date: "2024"}
  - {title: "JPL: CADRE", url: "https://jpl.nasa.gov/missions/cadre", date: ""}
  - {title: "NASA HLS IAC 2026 presentation (pressurised rover cargo delivery NET FY2032)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "Toyota: Lunar Cruiser", url: "https://global.toyota/en/mobility/technology/lunarcruiser/index.html", date: "2026"}
risks:
  - {sev: High, title: "Rovers are scheduled to arrive on a lander (Blue Moon Mk1) that hasn't flown yet", fix: "Keep a second delivery option; don't schedule crew sorties until at least one LTV is on the surface"}
  - {sev: High, title: "The pressurised rover's date is unclear (Artemis VII tie, NET FY2032 delivery)", fix: "Plan Phase 2 sorties to work without it, within walking/LTV range of the habitat"}
  - {sev: Medium, title: "Dust wear on wheels, seals and joints over long distances", fix: "Sintered roads (M05); scheduled maintenance; dust-tolerant designs"}
  - {sev: Medium, title: "Driving in long shadows and low sun angles at the pole", fix: "Lidar and headlights; mapped roads with beacons"}
---

## What's real

- **LTVs.** In May 2026 NASA picked two lunar terrain vehicles:
  - Astrolab **CLV-1**, $219M
  - Lunar Outpost **Pegasus**, $220M
  - Blue Origin is paid $188M to deliver both to the south pole in 2028<sup class="r">[1](#s1)</sup>.
- **Pressurised rover.** The JAXA/Toyota rover is planned to carry 2 crew for up to 30 days<sup class="r">[3](#s3)</sup>. NASA's 2026 page says 28 days, deployed in Phase 2 (2029–2032)<sup class="r">[4](#s4)</sup>, and the cargo delivery is listed as no earlier than FY2032<sup class="r">[7](#s7)</sup>.
- **Remote driving.** NASA tests had operators drive LTVs with 4-, 6- and 8-second delays, and every operator completed the traverses<sup class="r">[5](#s5)</sup>.

## How Open Moon uses them

Open Moon doesn't develop its own crew rovers. It leases LTV services and joins the pressurised-rover programme as a partner. Its own spending goes on:

- utility carts and small robots for hauling, inspection and cable patrol
- the teleoperation centre on Earth

Between crew visits, rovers are driven from Earth to keep them productive.

## Step-by-step

1. **Agree LTV service terms** for Open Moon use at the base site.
2. **Build a teleoperation centre** and train drivers on delay simulators.
3. **When the LTVs land in 2028:** commission them, map the roads, and start hauling for M05 and M06.
4. **Deliver the utility carts and robots** on small landers.
5. **Pressurised rover:** join as a partner; prepare its charging station and a dock at the habitat.
