---
id_code: M08
order: 8
title: Base habitats, shielding and life support
phase: 1
window: "Years 4–8"
summary: Before anyone lands, robots install three standard 3-person habitat modules side by side, connect them, bury them under regolith, and run life support, the storm shelter and the medical bay uncrewed until the base is ready for its first crew.
objective: "Land three standard 3-person habitat modules (detailed design to be defined later), connect them, cover them with at least 2 m of regolith (3 m over the sleeping quarters), and run life support sized for 6 people continuously and 9 at handover peaks, uncrewed, for at least 3 months, so the base is complete when the first crew lands (Phase 2, M09)."
trl_min: 4
depends_on: [M02, M03, M04, M05, M06, M07]
spec:
  - {k: Habitat, v: "3 × standard 3-person module, landed side by side and connected (DD-007); design to be defined later (open)"}
  - {k: "Beds", v: "9: 6 resident + 3 flexible for handovers (3 × 3, DD-006, DD-007)"}
  - {k: "Module mass", v: "~15 t each, PROVISIONAL placeholder from the Thales Alenia MPH class"}
  - {k: "Connections", v: "Hatches or tunnels between modules: needed, not yet designed"}
  - {k: "Life support", v: "Sized for 6 continuous, 9 peak (C08.2)"}
  - {k: "Shielding", v: "≥2 m regolith everywhere, 3 m over sleeping quarters, finished before first crew (C09.1)"}
  - {k: "Storm shelter", v: "Holds 9 for 3 days (C09.2)"}
  - {k: Crew, v: "None. This milestone is uncrewed (DD-005)"}
cost: {low: 13.2, high: 39.6, note: "habitat module delivery dominates"}
cost_items:
  - {item: "3 standard habitat modules (build)", low: 3.0, high: 9.0, basis: "PROVISIONAL placeholder: 3 × $1.0–3.0B per module (ESTIMATE, unchanged per-module figure; was 1 module in M08 + 2 in M09)"}
  - {item: "Delivery of 3 modules (~45 t, heavy cargo)", low: 9.0, high: 27.0, basis: "3 × ~15 t PROVISIONAL placeholder [src 11] × $0.2–0.6M/kg (ESTIMATE; was 15 t in M08 + 30 t in M09)"}
  - {item: "Extra excavators for burial", low: 0.2, high: 0.5, basis: "ESTIMATE; reuses M05 fleet (moved from M09, DD-005)"}
  - {item: "Life support closure upgrades", low: 0.3, high: 1.0, basis: "ESTIMATE (moved from M09, DD-005)"}
  - {item: "Extra life support capacity for 6 continuous / 9 peak (third CO₂ scrubber, second oxygen generator, spares)", low: 0.1, high: 0.3, basis: "ESTIMATE; driven by DD-006 crew size (C08.2 sizing)"}
  - {item: "Spacesuits, EVA tools, airlock/dust lock", low: 0.3, high: 0.8, basis: "ESTIMATE"}
  - {item: "Mission operations for the uncrewed build and checkout", low: 0.3, high: 1.0, basis: "ESTIMATE"}
exit_criteria:
  - "Three habitat modules landed, connected to each other with sealed hatches or tunnels, and each powered from the M04 grid through its own service connection and 120 V DC panel; switching any one off leaves the other two powered (DD-009)."
  - "Regolith cover of at least 2 m everywhere and 3 m over the sleeping quarters complete, and its dose checked with area monitors, before the first crew lands."
  - "Life support running uncrewed for at least 3 months with simulated loads for 6 people, and for 9 people for at least 2 weeks of that."
  - "Storm shelter filled and checked for 9 people; medical bay and exercise equipment installed and tested remotely."
  - "Dust lock, suits and EVA tools checked out remotely and ready for the first crew."
workstreams:
  - name: Habitat modules
    desc: One standard module design, built three times (DD-007).
    items: ["Standard 3-person module, design to be defined later", "Delivered on heavy cargo landers (~15 t each, provisional)", "Landed and placed side by side in the habitat zone", "Connecting hatches or tunnels between modules (needed, not yet designed)", "One service connection and 120 V DC panel per module (DD-009)"]
  - name: Shielding
    desc: Bury the modules before people arrive (C09.1).
    items: ["Support arch over the three modules", "≥2 m regolith, 3 m over sleeping quarters", "Radiators and pumped loops installed before burial", "Dose checks with area monitors"]
  - name: Life support
    desc: ISS-derived systems sized for 6 continuous and 9 peak (C08.2).
    items: ["Water recovery with brine processing", "Oxygen generation", "CO₂ removal (three 4BCO2-class units)", "Top-up from M06 water and oxygen"]
  - name: Crew safety systems
    desc: Ready before the first landing.
    items: ["Storm shelter for 9 (C09.2)", "Medical bay and exercise area (C09.3)", "Dust lock / suitports (C08.3)", "Suits and EVA tools (C08.4)"]
  - name: Remote commissioning
    desc: Everything a crew would have checked by hand is checked from Earth.
    items: ["Simulated crew loads (CO₂, humidity, water)", "Leak checks on every module and connection", "Utility robots inspect and fix", "Earth-based operations team"]
technologies:
  - {name: "Thales Alenia Space Multi-Purpose Habitation (MPH)", use: "Reference hardware for the standard module (heritage only, DD-007)", status: "Preliminary design contract with ASI (Jul 2025); ~15 t, ~3 m × 6 m, 10-yr life; launch planned 2033", trl: 5, src: 11}
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
  - {title: "Zhang et al., Science Advances: radiation dose on the lunar surface (Chang'e-4, 1,369 µSv/day)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "NASA OCHMO-TB-020: Radiation protection technical brief (600 mSv career limit)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf", date: "Dec 2022"}
  - {title: "Savage, IAC-24 abstract: regolith shielding depth (OLTARIS; ~150 mSv per 180 days at 2 m)", url: "https://iafastro.directory/iac/paper/id/82864/abstract-pdf/IAC-24,D3,IP,1,x82864.brief.pdf", date: "2024"}
risks:
  - {sev: Critical, title: "No crew checks the base before people depend on it; the first crew lands on systems never used by people", fix: "Run life support for at least 3 months with simulated loads for 6 and 9 people; inspect with utility robots; keep the crew lander ready to leave"}
  - {sev: Critical, title: "Burial must finish before the first landing, and it is slow: ~225–355 days at 4 × 200 kg/h, ~3–5 years at the IPEx design rate (C09.1)", fix: "Start piling as soon as the arch is up; add excavators; set the first crew date by measured burial progress, not by the calendar"}
  - {sev: High, title: "The standard 3-person module does not exist yet; its design is to be defined later (DD-007)", fix: "Use MPH-class figures (~15 t) only as placeholders; track the MPH and an inflatable as reference designs; freeze the module design before Phase 1 deliveries"}
  - {sev: High, title: "Connections between modules are new leak paths and are not yet designed", fix: "Each module can be sealed off on its own; leak-check every connection during the uncrewed run; carry spare seals"}
  - {sev: High, title: "Dust in the cabin (on Apollo, dust degraded suit seals and every sample-container seal failed)", fix: "Dust lock or suitports; strict cleaning; sintered surfaces at the hatch"}
  - {sev: High, title: "Spacesuit schedule risk (OIG warned demonstrations could slip to 2031)", fix: "Suits are needed only when the first crew lands (M09); check them out remotely in the dust lock first"}
  - {sev: Medium, title: "Buried modules cannot shed heat through regolith (C09.1)", fix: "Install surface radiators and two pumped loops before burial, sized for 9 people"}
---

## The habitat

- **One standard module, three times.** The habitat is one module design that houses **3 people**. Three are landed next to each other and connected, for **9 beds**: 6 for residents and 3 flexible beds for handovers (this plan's arithmetic, DD-006, DD-007). The detailed design is **to be defined later (open)**.
- **Connections.** Hatches or tunnels must join the modules. They are a needed element, not yet designed.
- **Reference hardware.** Thales Alenia Space is designing the MPH for the Italian Space Agency: about 3 m × 6 m, about 15 t, on wheels, with a minimum 10-year life. Launch is planned for 2033<sup class="r">[1](#s1)</sup><sup class="r">[11](#s11)</sup>. Open Moon uses it only as heritage, and uses its ~15 t only as a provisional mass for each module.
- **Inflatable alternative.** Sierra Space's LIFE module held 77 psi before bursting in a full-scale test, 27% above NASA's recommended level<sup class="r">[2](#s2)</sup>.
- **Delivery date.** NASA expects habitats to arrive on cargo landers no earlier than FY2033<sup class="r">[5](#s5)</sup>.

## Why the cover must be finished before the first crew

There are no short visits any more. The first crew lands and stays for a tour of about 6.5 months (DD-006).

- **Unshielded.** Chang'e-4 measured about **1,369 µSv per day** on the surface<sup class="r">[13](#s13)</sup>. Over a 198-day tour that is about **271 mSv** (this plan's arithmetic), 45% of NASA's **600 mSv** career limit<sup class="r">[14](#s14)</sup>.
- **Under 2 m.** One OLTARIS study gives about 150 mSv per 180 days at 2 m<sup class="r">[15](#s15)</sup>, so about **165 mSv** per tour (this plan's arithmetic).
- **Decision (plan design, DD-005).** The ≥2 m cover, and the 3 m cover over the sleeping quarters, must be complete and dose-checked before crew 1 lands. Piling regolith next to a crewed module would also put people and excavators in the same work zone.

## Life support

- **Base system.** The habitat uses ISS-derived life support. The ISS demonstrated **98% water recovery** in 2023<sup class="r">[3](#s3)</sup>, although NASA's reference page still describes routine recovery as about 90%<sup class="r">[9](#s9)</sup>.
- **Sizing.** It is sized for 6 people all the time and 9 for two weeks at each handover (C08.2).
- **Local top-up.** The system is topped up with water and oxygen from the M06 pilot plants from the start.

## What changed in the cost

- **Moved in from M09 (DD-005).** Two more modules and their delivery, burial excavators and life support upgrades now happen before the first crew.
- **Added (DD-006).** About $0.1–0.3B of extra life support capacity for 6 continuous and 9 peak (ESTIMATE).
- **Removed.** The four crewed sorties ($6.0–16.4B) are gone. Crew transport is now costed in M09.
- **Total.** $10.6–30.2B before, **$13.2–39.6B** now.

## Step-by-step

1. **Land three habitat modules** on heavy landers at the pads (M05), one at a time.
2. **Place them side by side.** LTVs and robots move them into the habitat zone, where they are connected to each other. Each module gets its own service connection to the M04 grid: a service drop, a UMIC-class converter to 120 V DC, a meter and a main breaker feeding its DC panel (C08.1, design change DD-009).
3. **Install radiators and pumped loops,** then build the support arch.
4. **Bury the modules** with the M05 excavators: ≥2 m everywhere, 3 m over the sleeping quarters (C09.1).
5. **Fit out the crew systems:** storm shelter for 9 (C09.2), medical bay (C09.3), dust lock and suits (C08.3, C08.4).
6. **Run uncrewed for at least 3 months.** Life support runs with simulated loads for 6 people, and for 9 for at least 2 weeks. Leak checks and dose checks run from Earth.
7. **Declare the base ready.** The first crew landing starts Phase 2 (M09).
