---
id_code: M03
order: 3
title: Communications, navigation and time
phase: 0
window: "Years 0–4"
summary: Give the base an always-on link to Earth, a local network on the surface, and positioning and timing, mostly by buying services from relay networks already being built.
objective: "Provide at least 95% of the time link availability between the base and Earth, a high-bandwidth local surface network covering every work site including crater floors, and positioning and timing good enough for autonomous driving and landing."
trl_min: 6
depends_on: [M00, M02]
spec:
  - {k: "Earth link", v: "Commercial relay services + direct-to-Earth when Earth is in view"}
  - {k: "Surface network", v: "4G/LTE base station + mesh radios + fibre between fixed sites"}
  - {k: "Navigation", v: "Relay-based PNT, weak-signal GPS, surface beacons"}
  - {k: "Time", v: "Coordinated Lunar Time (in definition)"}
cost: {low: 0.72, high: 1.94, note: "service fees for 5 years plus own surface network and backup relay"}
cost_items:
  - {item: "Relay and ground-station service fees, 5 years", low: 0.15, high: 0.5, basis: "ESTIMATE. NASA's relay contract has a maximum potential value of $4.82B [src 1]"}
  - {item: "Backup relay smallsat ×1 (build + launch to lunar orbit)", low: 0.15, high: 0.4, basis: "ESTIMATE; ~300 kg at $300k/kg to lunar orbit ≈ $90M delivery [src 8] plus spacecraft"}
  - {item: "Surface LTE base station, mesh radios, rim relay masts", low: 0.05, high: 0.15, basis: "ESTIMATE hardware"}
  - {item: "Delivery of base comms node and rim relay masts (~400 kg)", low: 0.24, high: 0.48, basis: "~220 kg comms node (C03.1) + rim masts (C03.2), ESTIMATE × $0.6–1.2M/kg ($1.2M/kg published [src 8])"}
  - {item: "Optical terminal for the base (high-rate Earth link)", low: 0.08, high: 0.25, basis: "ESTIMATE; based on O2O/LCRD class terminals"}
  - {item: "Operations and network engineering, 5 years", low: 0.05, high: 0.16, basis: "ESTIMATE"}
exit_criteria:
  - "Base-to-Earth link available at least 95% of the time over three consecutive months, using relay services plus direct-to-Earth."
  - "Surface network covering the habitat zone, power sites, landing pads and at least one PSR worksite, with at least 10 Mbps to every robot."
  - "Rovers can drive autonomously using surface PNT with an accuracy good enough to follow a mapped road."
  - "Base clocks traceable to the agreed lunar time standard."
workstreams:
  - name: Earth link via relays
    desc: Buy relay service; don't build a constellation.
    items: ["Intuitive Machines NASA relay network", "ESA Moonlight (initial service end-2028)", "SSTL Lunar Pathfinder", "Own backup smallsat"]
  - name: Direct-to-Earth
    desc: Talk straight to Earth when Earth is above the horizon.
    items: ["High-gain antenna on a mast", "Optical terminal", "Commercial ground stations to relieve the DSN"]
  - name: Surface network
    desc: Local coverage for robots and crew.
    items: ["4G/LTE base station (Nokia IM-2 heritage)", "Mesh radios on rovers", "Relay masts on crater rims", "Fibre between fixed sites"]
  - name: Navigation
    desc: Know where every robot is.
    items: ["Relay-based PNT (LunaNet)", "Weak-signal GPS/Galileo receiver (LuGRE heritage)", "Surface beacons and visual landmarks"]
  - name: Time
    desc: One clock for the whole Moon.
    items: ["Coordinated Lunar Time adoption", "Atomic clock reference at the base", "Clock offset ~58.7 µs per Earth day vs Earth"]
technologies:
  - {name: "NASA commercial lunar relay (Intuitive Machines)", use: "Earth link and PNT", status: "Contract with a maximum potential value of $4.82B (Sep 2024)", trl: 7, src: 1}
  - {name: "ESA Moonlight", use: "Earth link and navigation", status: "5 satellites; initial operations by end 2028, full operations by 2030", trl: 6, src: 2}
  - {name: "SSTL Lunar Pathfinder", use: "Relay", status: "In final testing; launch NET 2027 on Blue Ghost M2", trl: 7, src: 3}
  - {name: "Nokia lunar 4G/LTE network", use: "Surface network", status: "Ran for its full ~25-minute power window on IM-2 (2025)", trl: 7, src: 13}
  - {name: "LuGRE GPS/Galileo receiver", use: "Navigation", status: "Got a position fix on the lunar surface, Mar 2025", trl: 7, src: 5}
  - {name: "Optical (laser) communications", use: "High-rate Earth link", status: "LCRD experimenting since 2022; O2O flew on Artemis II (2026) at up to 260 Mbps", trl: 7, src: 14}
  - {name: "LunaNet Interoperability Specification v5", use: "Standard so all networks work together", status: "Version 5 published Feb 2025; developed by NASA, ESA, JAXA", trl: 9, src: 7}
sources:
  - {title: "NASA: NASA selects lunar relay contractor for Near Space Network services", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services", date: "Sep 2024"}
  - {title: "ESA: Moonlight programme", url: "https://www.esa.int/articles/esa-s-moonlight-programme-pioneering-the-path-for-lunar-exploration", date: "Oct 2024"}
  - {title: "Lunar Pathfinder, Wikipedia", url: "https://en.wikipedia.org/wiki/Lunar_Pathfinder", date: "accessed Nov 2026"}
  - {title: "Fierce Network: Nokia's lunar network on IM-2", url: "https://www.fierce-network.com/wireless/nokias-not-getting-hung-missed-lunar-phone-call", date: "Mar 2025"}
  - {title: "NASA: NASA successfully acquires GPS signals on Moon", url: "https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/", date: "Mar 2025"}
  - {title: "NASA: Laser Communications Relay Demonstration, a year of experimentation", url: "https://www.nasa.gov/missions/tech-demonstration/nasas-laser-communications-relay-a-year-of-experimentation/", date: "2023"}
  - {title: "NASA: LunaNet Interoperability Specification", url: "https://www.nasa.gov/communicating-with-missions/scan/lcrns/lunanet-interoperability-specification/", date: "Feb 2025"}
  - {title: "Astrobotic Payload User's Guide ($300k/kg to lunar orbit, $1.2M/kg to surface)", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "NASA OIG IG-23-016: Deep Space Network", url: "https://oig.nasa.gov/docs/IG-23-016.pdf", date: "Jul 2023"}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region (Earth visibility)", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "White House OSTP: celestial time standardization policy", url: "https://bidenwhitehouse.archives.gov/ostp/news-updates/2024/04/02/white-house-office-of-science-and-technology-policy-releases-celestial-time-standardization-policy", date: "Apr 2024"}
  - {title: "collectSPACE: Artemis II flyby video and Intuitive Machines lunar relays", url: "https://www.collectspace.com/news/news-040626a-artemis-ii-moon-flyby-video-intuitive-machines-lunar-relays.html", date: "Apr 2026"}
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", date: "Mar 2025"}
  - {title: "NASA: Laser Communications Relay Demonstration (LCRD) overview", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/laser-communications-relay-demonstration-lcrd-overview/", date: "2026"}
  - {title: "OSTP: Policy on Celestial Time Standardization (memorandum)", url: "https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/04/Celestial-Time-Standardization-Policy.pdf", date: "Apr 2024"}
  - {title: "JPL IPN Progress Report 42-176: Lunar pole illumination and communications maps (Bryant)", url: "https://ipnpr.jpl.nasa.gov/progress_report/42-176/176C.html", date: "Feb 2009"}
risks:
  - {sev: High, title: "Even at the best base site studied by JPL, Earth is in direct view only about half the time", fix: "Relays are mandatory; contract two independent relay networks; own one backup smallsat"}
  - {sev: High, title: "Relay launches keep slipping (Lunar Pathfinder, IM-3)", fix: "Don't schedule crew activity until two relays are operating; store-and-forward for robots meanwhile"}
  - {sev: High, title: "NASA's Deep Space Network is oversubscribed by up to 40%, rising to ~50% in the 2030s", fix: "Use commercial ground stations; optical links for bulk data"}
  - {sev: Medium, title: "No radio line of sight into crater floors", fix: "Relay masts on rims; tethered or mesh radios on rovers"}
  - {sev: Medium, title: "Optical terminals can't always point at Earth (seen on Artemis II)", fix: "Keep RF as primary for commanding; optical for bulk data only"}
---

## The problem

Earth visibility near the south pole varies by site: some Earth-facing areas see Earth almost all the time, others never do<sup class="r">[10](#s10)</sup>. At the best proposed base site in a JPL study, Earth was in direct view only about 51% of the time<sup class="r">[16](#s16)</sup>. NASA's own Deep Space Network is already oversubscribed by up to 40%, and that's projected to reach about 50% in the 2030s<sup class="r">[9](#s9)</sup>. A permanent base needs a link that never drops, and it can't depend on spare DSN time.

## The answer: buy, don't build

Lunar relay networks are already funded:

- **NASA's commercial relay network.** Intuitive Machines holds a contract worth up to $4.82B<sup class="r">[1](#s1)</sup>. Its first relay satellite launches with IM-3, and it plans five relays in total<sup class="r">[12](#s12)</sup>.
- **ESA Moonlight.** Five satellites focused on the south pole, with initial service by the end of 2028 and full operations in 2030<sup class="r">[2](#s2)</sup>.
- **SSTL Lunar Pathfinder.** In final testing; it launches no earlier than 2027<sup class="r">[3](#s3)</sup>.

NASA, ESA and JAXA develop a shared LunaNet interoperability specification<sup class="r">[7](#s7)</sup>, so one radio at the base should be able to use any network that follows it. Open Moon buys service from at least two networks and keeps one small backup relay of its own.

## On the surface

Nokia's 4G/LTE network ran without interruption for its whole ~25-minute power window on IM-2 in 2025, even though the lander's solar panels were badly oriented after landing<sup class="r">[13](#s13)</sup>. The base uses the same approach:

- an LTE base station at the habitat
- mesh radios on every rover
- relay masts on crater rims so robots in shadowed craters stay connected
- fibre between fixed sites such as the reactor, the solar towers and the oxygen plant

## Knowing where you are, and what time it is

- **Positioning.** LuGRE picked up GPS and Galileo signals on the lunar surface and computed a position fix in March 2025<sup class="r">[5](#s5)</sup>. Combined with relay-based positioning and visual landmarks, that's enough for rovers to drive mapped roads.
- **Time.** Seen from the Moon, an Earth clock appears to lose about 58.7 µs per Earth day<sup class="r">[15](#s15)</sup>. The White House asked NASA for a Coordinated Lunar Time strategy by the end of 2026<sup class="r">[11](#s11)</sup>. The base adopts whatever standard is agreed.

## Step-by-step

1. Sign service agreements with two relay networks.
2. Land the surface network kit with the first M04 power delivery: LTE base station, mast antennas, mesh radios.
3. Put relay masts on the rims of the PSRs chosen in M01.
4. Install the optical terminal for bulk data, such as video and science.
5. Prove at least 95% link availability for three months before any crew arrives.
