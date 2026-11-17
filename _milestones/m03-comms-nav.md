---
id_code: M03
order: 3
title: Communications, navigation and time
phase: 1
window: "2027–2031"
summary: Give the base an always-on link to Earth, a local network on the surface, and positioning and timing, mostly by buying services from relay networks already being built.
objective: "Provide at least 95% of the time link availability between the base and Earth, a high-bandwidth local surface network covering every work site including crater floors, and positioning and timing good enough for autonomous driving and landing."
trl_min: 6
depends_on: [M00, M02]
spec:
  - {k: "Earth link", v: "Commercial relay services + direct-to-Earth when Earth is in view"}
  - {k: "Surface network", v: "4G/LTE base station + mesh radios + fibre between fixed sites"}
  - {k: "Navigation", v: "Relay-based PNT, weak-signal GPS, surface beacons"}
  - {k: "Time", v: "Coordinated Lunar Time (in definition)"}
cost: {low: 0.6, high: 1.7, note: "service fees for 5 years plus own surface network and backup relay"}
cost_items:
  - {item: "Relay and ground-station service fees, 5 years", low: 0.15, high: 0.5, basis: "ESTIMATE. NASA's relay contract has a $4.82B ceiling shared across all NASA users [src 1]"}
  - {item: "Backup relay smallsat ×1 (build + launch to lunar orbit)", low: 0.15, high: 0.4, basis: "ESTIMATE; ~300 kg at $300k/kg to lunar orbit ≈ $90M delivery [src 8] plus spacecraft"}
  - {item: "Surface LTE base station, mesh radios, rim relay masts", low: 0.05, high: 0.15, basis: "ESTIMATE hardware"}
  - {item: "Delivery of surface network kit (~200 kg)", low: 0.12, high: 0.24, basis: "200 kg × $0.6–1.2M/kg (ESTIMATE; $1.2M/kg published [src 8])"}
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
  - {name: "NASA commercial lunar relay (Intuitive Machines)", use: "Earth link and PNT", status: "Contract up to $4.82B (2024); first relay satellite flies on IM-3, NET early 2027", trl: 7, src: 1}
  - {name: "ESA Moonlight", use: "Earth link and navigation", status: "€123M phase 1; 5 satellites; initial service end 2028, full 2030", trl: 6, src: 2}
  - {name: "SSTL Lunar Pathfinder", use: "Relay", status: "In final testing; launch NET 2027 on Blue Ghost M2", trl: 7, src: 3}
  - {name: "Nokia lunar 4G/LTE network", use: "Surface network", status: "Ran for its full ~25-minute window on IM-2 (2025)", trl: 7, src: 4}
  - {name: "LuGRE GPS/Galileo receiver", use: "Navigation", status: "Got a position fix on the lunar surface, Mar 2025", trl: 7, src: 5}
  - {name: "Optical (laser) communications", use: "High-rate Earth link", status: "LCRD demo complete 2024; O2O flew on Artemis II (2026)", trl: 7, src: 6}
  - {name: "LunaNet Interoperability Specification v5", use: "Standard so all networks work together", status: "Published Jan 2025 by NASA, ESA, JAXA", trl: 9, src: 7}
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
risks:
  - {sev: High, title: "Earth is below the horizon from the south pole for about half of each month", fix: "Relays are mandatory; contract two independent relay networks; own one backup smallsat"}
  - {sev: High, title: "Relay launches keep slipping (Lunar Pathfinder, IM-3)", fix: "Don't schedule crew activity until two relays are operating; store-and-forward for robots meanwhile"}
  - {sev: High, title: "NASA's Deep Space Network is oversubscribed by up to 40%, rising to ~50% in the 2030s", fix: "Use commercial ground stations; optical links for bulk data"}
  - {sev: Medium, title: "No radio line of sight into crater floors", fix: "Relay masts on rims; tethered or mesh radios on rovers"}
  - {sev: Medium, title: "Optical terminals can't always point at Earth (seen on Artemis II)", fix: "Keep RF as primary for commanding; optical for bulk data only"}
---

## The problem

Earth is visible from the south pole for only about half of each month<sup class="r">[10](#s10)</sup>. NASA's own Deep Space Network is already oversubscribed by up to 40%, and that's projected to reach about 50% in the 2030s<sup class="r">[9](#s9)</sup>. A permanent base needs a link that never drops, and it can't depend on spare DSN time.

## The answer: buy, don't build

Lunar relay networks are already funded:

- **NASA's commercial relay network.** Intuitive Machines holds a contract worth up to $4.82B<sup class="r">[1](#s1)</sup>. Its first relay satellite flies on IM-3 and two more on IM-4<sup class="r">[12](#s12)</sup>.
- **ESA Moonlight.** Five satellites focused on the south pole, with initial service by the end of 2028 and full operations in 2030<sup class="r">[2](#s2)</sup>.
- **SSTL Lunar Pathfinder.** In final testing; it launches no earlier than 2027<sup class="r">[3](#s3)</sup>.

All of them follow the shared LunaNet specification<sup class="r">[7](#s7)</sup>, so one radio at the base can use any of them. Open Moon buys service from at least two networks and keeps one small backup relay of its own.

## On the surface

Nokia's 4G/LTE network ran for its whole ~25-minute power window on IM-2 in 2025, even though the lander had tipped over<sup class="r">[4](#s4)</sup>. The base uses the same approach:

- an LTE base station at the habitat
- mesh radios on every rover
- relay masts on crater rims so robots in shadowed craters stay connected
- fibre between fixed sites such as the reactor, the solar towers and the oxygen plant

## Knowing where you are, and what time it is

- **Positioning.** LuGRE picked up GPS and Galileo signals on the lunar surface and computed a position fix in March 2025<sup class="r">[5](#s5)</sup>. Combined with relay-based positioning and visual landmarks, that's enough for rovers to drive mapped roads.
- **Time.** A clock on the Moon gains about 58.7 µs per Earth day. The White House asked NASA for a Coordinated Lunar Time strategy by the end of 2026<sup class="r">[11](#s11)</sup>. The base adopts whatever standard is agreed.

## Step-by-step

1. Sign service agreements with two relay networks.
2. Land the surface network kit with the first M04 power delivery: LTE base station, mast antennas, mesh radios.
3. Put relay masts on the rims of the PSRs chosen in M01.
4. Install the optical terminal for bulk data, such as video and science.
5. Prove at least 95% link availability for three months before any crew arrives.
