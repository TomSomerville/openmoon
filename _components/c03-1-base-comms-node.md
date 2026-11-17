---
id_code: "C03.1"
milestone: M03
order: 1
title: Base communications node
summary: "The base's central radio station: it links the base to Earth (direct and through relays), runs the local LTE network, keeps the base clock, and routes every robot's and crew member's data."
trl: 6
spec:
  - {k: "Relay link", v: "LunaNet S-band (2025–2110 / 2200–2290 MHz) and K-band (23.15–23.55 / 27.0–27.5 GHz)"}
  - {k: "Direct-to-Earth", v: "X-band (7190–7235 MHz up, 8450–8500 MHz down) via high-gain antenna on a mast"}
  - {k: "Optical link", v: "Laser terminal, up to 260 Mbps class (O2O heritage), for bulk data"}
  - {k: "Surface network", v: "4G/LTE network-in-a-box (base station, radio, core) plus Ethernet/fibre to fixed sites"}
  - {k: "Timing", v: "Atomic clock reference, traceable to the lunar time standard"}
  - {k: "Mast", v: "~10 m (design choice; NASA VSAT goal height)"}
  - {k: "Power", v: "~300 W average, ~550 W peak, from base grid plus 8 h battery (ESTIMATE)"}
  - {k: "Mass", v: "~190 kg excl. optical terminal, ~220 kg incl. (ESTIMATE, with 30% margin)"}
  - {k: "Quantity", v: "1 primary + 1 backup node at a second site (design choice)"}
  - {k: "Delivery class", v: "Medium lander (Blue Moon Mk1) with first M04 power delivery"}
subcomponents:
  - name: LunaNet relay radio
    desc: "Talks to lunar relay satellites from any LunaNet provider, so the base keeps its Earth link when Earth is below the horizon."
    parts: ["S-band proximity transceiver", "K-band proximity transceiver", "Wide-beam and steerable antennas", "LANS Augmented Forward Signal receiver (2483.5–2500 MHz)", "LunaNet IP / DTN router"]
    tech: "LunaNet Interoperability Specification v5"
    trl: 6
  - name: Direct-to-Earth high-gain antenna on mast
    desc: "A gimbaled dish on a mast talks straight to Earth ground stations whenever Earth is above the horizon."
    parts: ["~1 m X-band dish (ESTIMATE)", "Two-axis gimbal", "X-band transponder and power amplifier", "Deployable mast, ~10 m", "Omni antenna for safe mode"]
    tech: "VIPER X-band DTE; NASA VSAT mast development"
    trl: 6
  - name: Optical terminal
    desc: "A laser terminal sends large volumes of data (video, science, maps) to optical ground stations when Earth is in view."
    parts: ["Telescope and gimbal", "Fine-pointing and tracking sensor", "Laser transmitter and receiver", "Modem and data buffer", "Dust cover"]
    tech: "Artemis II O2O; LCRD"
    trl: 7
  - name: LTE base station
    desc: "A hardened cellular network-in-a-box gives robots, suits and the habitat a high-rate local link."
    parts: ["eNodeB base station", "Radio unit and sector antennas on the mast", "Network core (EPC) on the node computer", "Device modules for rovers and suits", "Operations and management software"]
    tech: "Nokia Bell Labs LSCS (IM-2, 2025)"
    trl: 7
  - name: Timing and navigation reference
    desc: "An atomic clock gives the whole base one time, steered to the lunar time standard, and anchors local positioning."
    parts: ["Primary atomic clock (DSAC heritage)", "Backup chip-scale atomic clock", "Weak-signal GNSS receiver (LuGRE heritage)", "Time distribution over LTE and Ethernet", "Surveyed antenna position (base geodetic marker)"]
    tech: "NASA DSAC; LuGRE"
    trl: 6
  - name: Power, thermal and housing
    desc: "Takes power from the base grid, rides through short outages on a battery, and keeps the electronics in a stable temperature range."
    parts: ["Grid power converter (from M04 bus)", "~2.4 kWh Li-ion battery (ESTIMATE)", "Insulated electronics vault with radiator", "Survival heaters", "Mast base, leveling feet and regolith ballast"]
    tech: "Standard spacecraft practice"
    trl: 7
risks:
  - {sev: High, title: "Earth is below the horizon from the south pole for about half of each month", fix: "Use at least two independent relay networks through the LunaNet radio, plus the backup relay smallsat from M03."}
  - {sev: High, title: "Frequencies for lunar surface cellular networks are not yet approved", fix: "Take part in the SFCG/ITU process. Keep LTE equipment able to retune, and keep Wi-Fi mesh as a fallback."}
  - {sev: High, title: "Relay launches keep slipping, so the node may arrive before any relay is working", fix: "The node works direct-to-Earth from day one. Robots use store-and-forward until relays are up."}
  - {sev: Medium, title: "Optical links need clear weather at the ground station and precise pointing", fix: "Use optical only for bulk data. Keep RF as the command link and use several optical ground stations."}
  - {sev: Medium, title: "The node is a single point of failure for the whole base", fix: "Install a second, smaller node at another site. Every rover can also talk direct-to-Earth or through relays."}
  - {sev: Medium, title: "Landing plume dust sandblasts antennas and the optical window", fix: "Site the node at least ~1 km from the landing pad (design target), with berms. Keep a dust cover on the optics."}
  - {sev: Medium, title: "The node is heavier than the ~200 kg network kit assumed in the M03 budget", fix: "Deliver the optical terminal separately (as M03 already costs it). Re-check the M03 delivery budget."}
sources:
  - {title: "NASA: LunaNet Interoperability Specification v5", url: "https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf", date: "Jan 2025"}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region (Earth visibility)", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "NASA OIG IG-23-016: Deep Space Network", url: "https://oig.nasa.gov/docs/IG-23-016.pdf", date: "Jul 2023"}
  - {title: "NASA NTRS: VIPER Mission Overview (Andrews)", url: "https://ntrs.nasa.gov/api/citations/20205000864/downloads/2020-04-14%2C%20VIPER%20Mission%20Overview%20(Andrews).pdf", date: "Apr 2020"}
  - {title: "NASA: NASA laser terminal enhances views during Artemis II mission", url: "https://www.nasa.gov/missions/artemis/artemis-2/nasa-laser-terminal-enhances-views-during-artemis-ii-mission/", date: "Apr 2026"}
  - {title: "NASA: Laser Communications Relay Demonstration, a year of experimentation", url: "https://www.nasa.gov/missions/tech-demonstration/nasas-laser-communications-relay-a-year-of-experimentation/", date: "2023"}
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", date: "Mar 2025"}
  - {title: "NASA: Deep Space Atomic Clock (DSAC) overview", url: "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/deep-space-atomic-clock-dsac-overview/", date: "accessed Nov 2026"}
  - {title: "White House OSTP: celestial time standardization policy", url: "https://bidenwhitehouse.archives.gov/ostp/news-updates/2024/04/02/white-house-office-of-science-and-technology-policy-releases-celestial-time-standardization-policy", date: "Apr 2024"}
  - {title: "NASA: NASA successfully acquires GPS signals on Moon (LuGRE)", url: "https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/", date: "Mar 2025"}
  - {title: "NASA NTRS: Vertical Solar Array Technology annual review", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
  - {title: "Gläser et al. 2014, Icarus: Illumination at the lunar south pole", url: "https://ui.adsabs.harvard.edu/abs/2014Icar..243...78G", date: "2014"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "NASA: NASA selects lunar relay contractor for Near Space Network services", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services", date: "Sep 2024"}
  - {title: "ESA: Moonlight programme", url: "https://www.esa.int/articles/esa-s-moonlight-programme-pioneering-the-path-for-lunar-exploration", date: "Oct 2024"}
---

## What it does

The node is the base's telephone exchange. It does four jobs:

1. It sends base data to Earth, either straight to Earth or through relay satellites.
2. It runs the local wireless network that every rover, suit and building joins.
3. It keeps the master clock.
4. It routes data between all of them.

M03's exit criterion is a link to Earth at least 95% of the time. This node is the hardware that delivers it.

## How it works

- **Relay radio.** All of the lunar relay networks follow the LunaNet Interoperability Specification<sup class="r">[1](#s1)</sup>. That includes NASA's commercial relay network, a contract worth up to $4.82B<sup class="r">[14](#s14)</sup>, and ESA's Moonlight<sup class="r">[15](#s15)</sup>. LunaNet uses S-band (2025–2110 MHz forward, 2200–2290 MHz return) and K-band (23.15–23.55 GHz forward, 27.0–27.5 GHz return) for links between relays and surface users. Its navigation signal sits at 2483.5–2500 MHz<sup class="r">[1](#s1)</sup>. One radio built to this spec can use any provider.
- **Direct-to-Earth.** LunaNet keeps S-band for local links and uses X-band (7190–7235 MHz up, 8450–8500 MHz down) for direct-with-Earth links<sup class="r">[1](#s1)</sup>. From the south pole, Earth is in view for only about half of each month<sup class="r">[2](#s2)</sup>, so this link covers half the time and relays cover the rest. For scale, VIPER's small rover antenna sent 256 kbps, and up to 4 Mbps, over X-band<sup class="r">[4](#s4)</sup>. The node's larger dish should do better. NASA's Deep Space Network is oversubscribed by up to 40%<sup class="r">[3](#s3)</sup>, so we plan to use commercial ground stations as well.
- **Optical terminal.** On Artemis II, O2O made multiple 260 Mbps downlinks and moved about 484 GB in about 10 days. At the same distance, the radio links were limited to single-digit Mbps<sup class="r">[5](#s5)</sup>. NASA's LCRD relay ran a year of laser-communication experiments<sup class="r">[6](#s6)</sup>. LunaNet v5 does not yet cover optical links<sup class="r">[1](#s1)</sup>, so the terminal speaks directly to optical ground stations.
- **LTE base station.** On IM-2, Nokia's "network in a box" powered on and reached an "on-air" state with its base station, radio and network core all working. It ran without interruption for the whole 25-minute power window<sup class="r">[7](#s7)</sup>. LunaNet expects surface users to connect through UHF, Wi-Fi or 3GPP (cellular) links, but the frequency bands for lunar cellular service are still under study<sup class="r">[1](#s1)</sup>.
- **Timing.** A clock on the Moon gains about 58.7 µs per Earth day relative to Earth<sup class="r">[9](#s9)</sup>. NASA's Deep Space Atomic Clock loses about one second in 10 million years and is up to 50 times more stable than GPS satellite clocks<sup class="r">[8](#s8)</sup>. LuGRE got a GPS/Galileo position fix on the lunar surface<sup class="r">[10](#s10)</sup>, so a GNSS receiver gives a second, independent time and position check.
- **Mast.** NASA's VSAT project set a 10 m mast-height goal (5 m threshold) on slopes of up to 15°<sup class="r">[11](#s11)</sup>. We use a mast of that class. Height matters: at the best ridge point near Shackleton, sunlight rises from 92% at 2 m to 96% at 10 m<sup class="r">[12](#s12)</sup>. Line of sight for radio improves with height in the same way.

## Sizing

Power (ESTIMATE):

| Load | Average (W) | Peak (W) |
|---|---|---|
| Relay radio (S + K) | 60 | 120 |
| X-band DTE transponder and amplifier | 60 | 150 |
| Optical terminal | 40 | 100 |
| LTE network-in-a-box | 60 | 80 |
| Clocks, router, computer | 30 | 30 |
| Heaters and gimbals | 50 | 70 |
| **Total** | **~300** | **~550** |

Battery to ride through 8 h of grid outage: 300 W × 8 h = 2.4 kWh. At 160 Wh/kg for Li-ion<sup class="r">[13](#s13)</sup>, that is 2,400 ÷ 160 = 15 kg. Longer darkness (up to ~100 h at the pole<sup class="r">[13](#s13)</sup>) is covered by the base grid (M04), not by the node.

Mass (ESTIMATE): mast 40 kg + dish and gimbal 20 + radios 20 + LTE 15 + clocks and computer 10 + battery 15 + vault, thermal and harness 25 = **145 kg**. With 30% margin that is **~190 kg**. Adding a 25 kg optical terminal gives (145 + 25) × 1.3 ≈ **220 kg**.

## Testing and qualification

1. **Interoperability tests.** Test the relay radio against each provider's LunaNet test set and against NASA's published AFS signal specification<sup class="r">[1](#s1)</sup>.
2. **End-to-end ground test.** Run the whole node in a thermal-vacuum chamber, linked to a real ground station through a channel simulator that adds the Earth–Moon signal delay.
3. **LTE field test.** Run a Nokia-class network in a desert analogue site with rovers at 1–5 km to measure range and throughput.
4. **Mast test.** Deploy and retract the mast on a 15° slope. Measure dish pointing while the mast is loaded.
5. **On the Moon.** Commission DTE first, then relays, then LTE, then optical. Count availability daily until it is at or above 95% for three months (M03 exit criterion).

## Open questions

- Which frequency band will lunar 3GPP networks get, and when? Can our LTE hardware retune if the band changes?
- What X-band data rate can a ~1 m dish reach to a commercial 13 m ground antenna? Should we go to Ka-band for direct-to-Earth?
- Is a DSAC-class mercury-ion clock worth its mass and power at the base, or does a chip-scale clock steered by relay time suffice?
- How far from the landing pad must the node be to avoid plume damage?
- Should Open Moon buy a node as a service from a lander or relay company instead of owning it?
