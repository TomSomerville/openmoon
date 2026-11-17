---
id_code: M08
order: 8
title: First habitat and crewed sorties
phase: 2
window: "2031–2035"
summary: Land the first surface habitat and fly crews for stays of two to four weeks, leaving more infrastructure behind on every visit.
objective: "Land a habitat for two to four crew, fly four crewed sorties of 14–30 days, and use them to commission the power, ISRU and mobility systems with people on site."
trl_min: 5
depends_on: [M02, M03, M04, M05, M07]
spec:
  - {k: Habitat, v: "1 rigid module, ~15 t class (e.g. Thales Alenia MPH: ~3 m × 6 m, 10-year life)"}
  - {k: Crew, v: "2 per sortie at first (MPH is reported as a 2-crew module), 4 once a second module or the pressurised rover is docked"}
  - {k: Stays, v: "14–30 days"}
  - {k: Sorties, v: "4"}
  - {k: Suits, v: "Axiom AxEMU class"}
cost: {low: 10.6, high: 30.2, note: "crew transport dominates"}
cost_items:
  - {item: "Habitat module (build, test)", low: 1.0, high: 3.0, basis: "ESTIMATE"}
  - {item: "Habitat delivery (~15 t, heavy cargo lander)", low: 3.0, high: 9.0, basis: "15 t [src 11] × $0.2–0.6M/kg (ESTIMATE)"}
  - {item: "4 crewed sorties (crew launch + landing)", low: 6.0, high: 16.4, basis: "High: $4.1B per SLS/Orion launch (OIG) [src 6]; low assumes commercial crew transport at ~$1.5B per mission (ESTIMATE)"}
  - {item: "Spacesuits, EVA tools, airlock/dust lock", low: 0.3, high: 0.8, basis: "ESTIMATE"}
  - {item: "Mission operations and crew training", low: 0.3, high: 1.0, basis: "ESTIMATE"}
exit_criteria:
  - "Habitat landed, deployed and powered from the M04 grid, with life support running uncrewed for at least 3 months before the first crew."
  - "Four sorties of 14–30 days flown with no serious injury."
  - "Each crew completes a planned list of maintenance, installation and science tasks."
  - "Dust kept out of the habitat to a measured standard."
workstreams:
  - name: Habitat
    desc: A rigid, wheeled module that can be moved and later buried.
    items: ["~15 t class pressurised module", "Delivered on a heavy cargo lander", "Moved by LTVs to the habitat zone"]
  - name: Life support (open loop + recycling)
    desc: ISS-derived systems.
    items: ["Water recovery", "Oxygen generation", "CO₂ removal", "Top-up from M06 water and oxygen"]
  - name: Dust control
    desc: Keep dust out of the cabin.
    items: ["Dust lock / suitport", "Brushes and electrostatic cleaning", "Sintered ground around the hatch"]
  - name: EVA
    desc: Working outside.
    items: ["AxEMU-class suits", "Tools for maintenance", "LTV range limits for walk-back safety"]
  - name: Crew transport
    desc: Seats to and from the surface.
    items: ["NASA Artemis / Moon Base partnership", "Commercial landers when certified"]
  - name: Medical
    desc: Treat what can be treated, evacuate what can't.
    items: ["Medical kit and ultrasound", "Telemedicine with 5–12 s delay", "Evacuation plan"]
technologies:
  - {name: "Thales Alenia Space Multi-Purpose Habitation (MPH)", use: "Surface habitat", status: "Preliminary design contract with ASI (Jul 2025); ~15 t, ~3 m × 6 m, 10-yr life; launch planned 2033", trl: 5, src: 11}
  - {name: "Sierra Space LIFE inflatable", use: "Alternative expandable habitat", status: "Full-scale burst test reached 77 psi before bursting (reported Jan 2024), 27% above NASA's recommended 60.8 psi", trl: 5, src: 2}
  - {name: "ISS life support (ECLSS)", use: "Air and water recycling", status: "Flight-proven; 98% water recovery demonstrated 2023", trl: 9, src: 3}
  - {name: "Axiom AxEMU spacesuit", use: "Moonwalks", status: "Critical design review closed 13 Nov 2026; qualification next", trl: 6, src: 4}
  - {name: "Heavy cargo lander (Starship / Blue Moon Mk2 cargo)", use: "Habitat delivery", status: "~15 t class; habitat delivery NET FY2033 per NASA", trl: 6, src: 5}
sources:
  - {title: "Thales Alenia Space: contract with ASI to develop lunar Multi-Purpose Habitation module", url: "https://www.thalesgroup.com/en/worldwide/space/press_release/thales-alenia-space-signs-contract-italian-space-agency-asi-develop", date: "Jul 2025"}
  - {title: "TechCrunch: Sierra Space's inflatable habitat blows up as planned", url: "https://techcrunch.com/2024/01/22/successful-failure-sierra-spaces-inflatable-habitat-blows-up-as-planned", date: "Jan 2024"}
  - {title: "Space.com: ISS hits 98% water recycling milestone", url: "https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone", date: "Jun 2023"}
  - {title: "Axiom Space: completes NASA's critical design review for next-generation spacesuit", url: "https://www.axiomspace.com/release/axiom-space-completes-nasas-critical-design-review-for-next-generation-spacesuit", date: "Nov 2026"}
  - {title: "NASA HLS IAC 2026 presentation (cargo landers, habitat delivery NET FY2033)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "NASA OIG IG-22-003: NASA's management of the Artemis missions ($4.1B per launch)", url: "https://www.oversight.gov/sites/default/files/oig-reports/NASA/Final-Report-IG-22-003-NASAs-Management-Artemis-Missions.pdf", date: "Nov 2021"}
  - {title: "NASA NTRS: Holden et al. 2026, communication delay study methods (5–12 s)", url: "https://ntrs.nasa.gov/api/citations/20260002621/downloads/Holden%20et%20al%202026%20-%20comm%20delay%20study%20methodsa.pdf", date: "2026"}
  - {title: "Gaier, NASA/TM-2005-213610: Effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "NASA: Environmental Control and Life Support Systems reference", url: "https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss", date: "Apr 2025"}
  - {title: "NASA Moon Base – Phases", url: "https://www.nasa.gov/moonbase-phases/", date: "2026"}
  - {title: "European Spaceflight: ASI awards new lunar habitat contract to Thales Alenia Space (MPH: 3 m × 6 m, ~15 t, 2 crew, 7–30 days a year)", url: "https://europeanspaceflight.com/asi-awards-new-lunar-habitat-contract-to-thales-alenia-space/", date: "Jul 2025"}
  - {title: "NASA OIG: Spacesuit development delays could impact Artemis timeline and ISS operations (demonstrations could slip to 2031)", url: "https://oig.nasa.gov/news/spacesuit-development-delays-could-impact-artemis-timeline-and-iss-operations/", date: "Apr 2026"}
risks:
  - {sev: Critical, title: "Crew landing systems are not yet certified; first crewed landing is planned for 2028", fix: "Fly sorties only after the lander has a demonstrated crewed landing; partner with NASA Moon Base schedule"}
  - {sev: High, title: "Dust in the cabin (on Apollo, dust degraded suit seals and every sample-container seal failed)", fix: "Dust lock or suitports; strict cleaning; sintered surfaces at the hatch"}
  - {sev: High, title: "Spacesuit schedule risk (OIG warned demonstrations could slip to 2031)", fix: "Keep sortie dates flexible; early sorties with minimal EVA"}
  - {sev: High, title: "Medical emergency far from a hospital, with 5–12 s operational delays", fix: "Trained crew medic, telemedicine, and an evacuation plan with a lander on standby"}
  - {sev: High, title: "The MPH is reported as sized for 2 crew on one 7–30-day mission a year, while crewed landers carry 4", fix: "Fly 2-crew surface teams first; add fold-down sleep stations; reach 4 crew by docking the pressurised rover or a second module (M09)"}
  - {sev: Medium, title: "Habitat sits on the surface unshielded during sorties", fix: "Short stays; storm shelter area with water walls; burial in M09"}
---

## The habitat

- **Thales Alenia Space MPH.** Thales is designing it for the Italian Space Agency: about 3 m × 6 m, about 15 t, on wheels, with a minimum 10-year life. Launch is planned for 2033<sup class="r">[1](#s1)</sup><sup class="r">[11](#s11)</sup>.
- **Inflatable alternative.** Sierra Space's LIFE module held 77 psi before bursting in a full-scale test, 27% above NASA's recommended level<sup class="r">[2](#s2)</sup>.

Open Moon designs its habitat zone for a **rigid ~15 t module first**, with room for inflatable modules later. Press reports describe the MPH as sized for **two** astronauts on one 7–30-day mission a year<sup class="r">[11](#s11)</sup>, so early sorties put two people on the surface. Four-person stays wait for a second module or the docked pressurised rover (M07). NASA expects habitats to arrive on cargo landers no earlier than FY2033<sup class="r">[5](#s5)</sup>.

## Life support

- **Base system.** The habitat uses ISS-derived life support. The ISS demonstrated **98% water recovery** in 2023<sup class="r">[3](#s3)</sup>, although NASA's reference page still describes routine recovery as about 90%<sup class="r">[9](#s9)</sup>.
- **Local top-up.** During sorties the system is topped up with water and oxygen from the M06 pilot plants. This is the first time the crew depends on lunar resources.

## Why crew transport dominates the cost

- **Upper bound.** NASA's Inspector General put each SLS/Orion launch at about **$4.1B**<sup class="r">[6](#s6)</sup>. That figure doesn't include the lander.
- **Lower bound.** This plan assumes commercial crew transport eventually costs about $1.5B per mission, but that is an **estimate, not a published price**.
- **Why it matters.** The uncertainty in crew transport is the biggest single uncertainty in the whole budget.

## Step-by-step

1. **Land the habitat** on a heavy lander at pad 2 (M05).
2. **Move it into place.** LTVs tow it to the habitat zone, where it's connected to the habitat microgrid (M04).
3. **Run uncrewed for 3 months.** Life support, leak checks and dust lock tests run from Earth.
4. **Sortie 1 (14 days).** Commission the habitat; inspect power and ISRU; first moonwalks.
5. **Sorties 2–4 (up to 30 days).** Maintenance, installation of M09 equipment, and medical research on partial gravity.
6. **Leave equipment behind.** Each crew leaves the habitat ready for the next one.
