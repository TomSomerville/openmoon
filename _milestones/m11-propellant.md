---
id_code: M11
order: 11
title: Propellant and industrial-scale ISRU
phase: 4
window: "2036–2042"
summary: Scale the pilot plants up to hundreds of tonnes of oxygen and water a year, so landers can refuel on the Moon and the base pays its way.
objective: "Produce at least 300 t of oxygen and 100 t of water per year, store them, and refuel landers on the surface. Power the plants with a grid of at least 500 kW."
trl_min: 5
depends_on: [M04, M05, M06]
spec:
  - {k: Oxygen, v: "≥300 t/yr from regolith and ice"}
  - {k: Water, v: "≥100 t/yr from PSR ice"}
  - {k: Power, v: "≥500 kW total (more reactors + solar)"}
  - {k: Depot, v: "Cryogenic storage and transfer at the pads"}
cost: {low: 14.0, high: 42.0, note: "plant modules, power expansion and depot"}
cost_items:
  - {item: "Plant modules ×10 (build)", low: 1.0, high: 3.0, basis: "ESTIMATE; repeat builds of M06 modules"}
  - {item: "Delivery of plant modules (~30 t)", low: 6.0, high: 18.0, basis: "30 t × $0.2–0.6M/kg (ESTIMATE)"}
  - {item: "Two more fission units (build)", low: 0.5, high: 1.5, basis: "ESTIMATE; repeat builds"}
  - {item: "Delivery of fission units (~20 t)", low: 4.0, high: 12.0, basis: "2 × ~10 t × $0.2–0.6M/kg"}
  - {item: "Cryogenic depot and transfer equipment (build + ~10 t delivery)", low: 2.5, high: 7.5, basis: "ESTIMATE"}
exit_criteria:
  - "Sustained production of ≥300 t O₂ and ≥100 t water per year."
  - "At least one lander refuelled with lunar oxygen on the surface."
  - "Plant availability above 80% over a year."
  - "Cost per kg of lunar oxygen below the cost of shipping it from Earth."
workstreams:
  - name: Scale oxygen
    desc: Many modules, not one giant plant.
    items: ["~10 oxygen modules", "Automated feedstock supply", "Electrode and crucible replacement"]
  - name: Scale water
    desc: Mining in PSRs.
    items: ["Multiple cold-rated excavators", "Heated haul containers", "Purification"]
  - name: Power expansion
    desc: Grow the grid to ≥500 kW.
    items: ["Two more fission units", "More solar towers", "Grid reinforcement"]
  - name: Propellant depot
    desc: Store and transfer cryogenics.
    items: ["Liquefaction and storage tanks", "Transfer lines at the pads", "Boil-off control"]
technologies:
  - {name: "Pilot plant results (M06)", use: "Basis for scale-up", status: "To be demonstrated", trl: 5, src: 1}
  - {name: "Cryogenic propellant transfer", use: "Refuelling landers", status: "Ship-to-ship transfer demo (Starship) planned ~Q1 2027", trl: 5, new: true, src: 2}
  - {name: "In-orbit LOX storage demo (LOXSAT)", use: "Cryogenic storage heritage", status: "Eta Space / Rocket Lab demo targeted 2026", trl: 6, src: 3}
sources:
  - {title: "NASA NTRS: Molten regolith electrolysis ground demonstration (ICES 2026)", url: "https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf", date: "2026"}
  - {title: "NASA HLS IAC 2026 presentation (propellant transfer demo schedule)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "Rocket Lab: LOXSAT", url: "https://rocketlabcorp.com/missions/missions-launched/loxsat/", date: ""}
  - {title: "Astrobotic Payload User's Guide ($1.2M/kg to surface)", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "Colozza, NASA/CR: ISRU plant power", url: "https://ntrs.nasa.gov/citations/20200001622", date: "Mar 2020"}
risks:
  - {sev: Critical, title: "Pilot results may show higher energy or wear than expected", fix: "Size M11 only from measured M06 data; keep two processes in parallel"}
  - {sev: High, title: "No customer for propellant yet", fix: "Agreements with lander operators before building the depot"}
  - {sev: High, title: "Cryogenic boil-off on the surface", fix: "Shaded, buried tanks; cryocoolers powered by the grid"}
---

## Why scale up

- **Pilot plants (M06)** prove the processes work.
- **Industrial plants** make the Moon cheaper to operate than Earth supply.
- **The arithmetic.** At today's published price of $1.2M per kg landed<sup class="r">[4](#s4)</sup>, 300 t of oxygen shipped from Earth would cost about $360B a year. Even at this plan's heavy-lander assumption of $0.2M per kg, it's $60B a year. If there are buyers for that much oxygen (see the risks), making it locally pays back the whole milestone cost within about a year of full operation.

## Step-by-step

1. **Freeze the plant design** from M06 measured data.
2. **Deliver oxygen and water modules** in batches. Each batch increases output.
3. **Expand power** with two more fission units and more solar towers (≥500 kW in total).
4. **Build the depot** at the pads.
5. **First surface refuelling** of a lander.
