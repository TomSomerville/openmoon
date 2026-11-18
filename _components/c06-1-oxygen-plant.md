---
id_code: "C06.1"
milestone: M06
order: 1
title: "Oxygen-from-regolith pilot plant"
summary: "A pilot plant that melts lunar regolith and splits oxygen out of it with electricity (molten regolith electrolysis), with a carbothermal reactor as backup. It proves that rock can supply breathing oxygen and propellant before anyone depends on it."
trl: 4
spec:
  - {k: "Output target", v: "10 t O₂ per year (about 1.14 kg/h)"}
  - {k: "Primary process", v: "Molten regolith electrolysis, melt at about 1,600 °C"}
  - {k: "Backup process", v: "Carbothermal reduction, about 1,800 °C"}
  - {k: "Cell current", v: "At least ~3,800 A in total across all cells (Faraday's law, ESTIMATE)"}
  - {k: "Power", v: "~18 kW if the NASA study figure holds; ~120 kW at today's demo efficiency (see Sizing)"}
  - {k: "Feedstock", v: "50–435 t of regolith per year, depending on yield (ESTIMATE)"}
  - {k: "Mass", v: "~3 t delivered (M06 ESTIMATE)"}
  - {k: "Life", v: "6 months continuous operation, with electrode and crucible change-out"}
  - {k: "Delivery class", v: "Medium lander"}
  - {k: "Power interface", v: "Own service connection to the M04 grid (UMIC-class step-down to 120 V DC, meter, main breaker) and its own 120 V DC panel; can be isolated without affecting other units (plan design, DD-009); within 10 km of cable run of the PMC (DD-013, DD-014)"}
subcomponents:
  - name: "Feedstock handling and beneficiation"
    desc: "Takes regolith from the M05 stockpile, sieves it, and feeds a measured batch into each reactor."
    parts: ["Hopper and loader interface", "Vibrating sieve (rejects rocks)", "Magnetic or size separator (optional)", "Mass-metering feeder", "Dust-sealed feed valve"]
    tech: "Sierra Space automated regolith feed in TVAC (2024)"
    trl: 5
  - name: "Reactor and crucible"
    desc: "An insulated vessel in which regolith is heated to melting and then kept molten by the electrolysis current itself."
    parts: ["Start-up heaters", "Refractory lining or cold-wall (frozen regolith) shell", "Thermocouples in the melt", "Thermal shield and radiator", "Vacuum-tight lid"]
    tech: "NASA KSC and Lunar Resources LR-1 electrolysis reactor (25 kg melt; not NASA's Lunar Reactor-1 fission unit)"
    trl: 4
  - name: "Electrodes"
    desc: "An inert anode where oxygen gas forms and a molten metal cathode pool where metals collect."
    parts: ["Inert anode assembly", "Molten metal cathode pool", "High-current leads and bus bars", "DC power supply (~45 V class)", "Spare electrode sets"]
    tech: "LR-1 electrolysis at 45 V, 210 A"
    trl: 4
  - name: "Gas handling and purification"
    desc: "Collects the oxygen leaving the melt, removes dust and other gases, measures it, and compresses it."
    parts: ["Hot gas off-take and dust filter", "Gas cooler", "Oxygen sensor and residual gas analyser", "Clean-up bed for other volatiles", "Compressor and accumulator"]
    tech: "KSC Volatile Monitoring and Oxygen Measurement System (VMOMS)"
    trl: 4
  - name: "Liquefaction hand-off"
    desc: "Delivers clean, dry oxygen gas to the 90 K cryocooler and tanks of C06.3."
    parts: ["Pressure regulator", "Dew-point and purity check", "Isolation valves", "Flow meter"]
    tech: "NASA 90 K reverse turbo-Brayton cryocooler programme"
    trl: 5
  - name: "Slag and metal removal"
    desc: "Empties spent slag and the metal (iron, silicon and others) after each batch so the reactor can be reused."
    parts: ["Tap hole or tilting crucible", "Cooling tray", "Slag crusher", "Metal ingot store for M12"]
    tech: "Sierra Space spent-regolith removal; MRE tapping not yet shown"
    trl: 3
  - name: "Power, thermal and control"
    desc: "Takes power from the M04 grid through the plant's own service connection (DD-009), rejects waste heat, and runs the batch cycle without crew."
    parts: ["Service connection: UMIC-class step-down to 120 V DC, meter, main breaker", "120 V DC panel", "DC converters from the panel to the ~45 V cell supplies", "Radiators", "Process controller and data logger", "Fault protection (power loss, over-temperature)", "Cameras"]
    tech: "LR-1 data acquisition and control system"
    trl: 5
risks:
  - {sev: Critical, title: "Energy per kg in the 2024 demo (~100–135 kWh/kg) is far above the NASA study figure (~16 kWh/kg); at demo efficiency the pilot would make only ~2 t a year on 26 kW", fix: "Ground-test a full-size cell before flight and publish kWh/kg; fly the carbothermal backup; size M11 only from measured numbers"}
  - {sev: High, title: "Anode and crucible wear at 1,600–1,700 °C limits life", fix: "Carry spare electrode sets; design for robotic change-out; measure wear rate in a 6-month ground run"}
  - {sev: High, title: "Power loss freezes the melt around the electrodes", fix: "Battery ride-through for a controlled shutdown; treat each batch as able to freeze and restart; test freeze-restart cycles on the ground"}
  - {sev: High, title: "Hot, pure oxygen can ignite metals and seals", fix: "Oxygen-compatible materials only; clean-for-oxygen assembly; flow limits and pressure relief in the gas train"}
  - {sev: Medium, title: "No MRE reactor has yet tapped slag or metal and been reused", fix: "Make slag and metal removal a required ground-test step; accept single-use crucibles for the first batches if needed"}
  - {sev: Medium, title: "Regolith at the site may differ from the simulant used in tests", fix: "Use M01 soil data to make simulant; measure yield for each batch on the Moon"}
  - {sev: Medium, title: "Carbothermal backup needs a carbon carrier that must be recycled", fix: "Measure carbon losses in ground tests; carry a top-up supply sized from those tests"}
  - {sev: Medium, title: "Commercial programmes (Lunar Resources, Blue Alchemist, Sierra Space) may slip or stop", fix: "Keep two processes from two suppliers; open interface specs for feed, power and gas off-take"}
sources:
  - {title: "NASA NTRS: Large-scale demonstration of molten regolith electrolysis for oxygen production in a relevant environment (ICES 2026)", url: "https://ntrs.nasa.gov/api/citations/20260006167/downloads/MRE%20GCD%20ICES26_v3.pdf", date: "2026"}
  - {title: "NASA NTRS 20250004151: Carbothermal oxygen production reactor testing", url: "https://ntrs.nasa.gov/citations/20250004151", date: "2025"}
  - {title: "Blue Origin: Blue Alchemist hits major milestone", url: "https://www.blueorigin.com/news/blue-alchemist-hits-major-milestone-toward-permanent-sustainable-lunar-infrastructure", date: "Sep 2025"}
  - {title: "Colozza, NASA/CR: ISRU plant power (1.63 kg/h O₂ at 25.83 kW)", url: "https://ntrs.nasa.gov/citations/20200001622", date: "Mar 2020"}
  - {title: "WUSTL: Chemical composition of lunar soil", url: "https://sites.wustl.edu/meteoritesite/items/the-chemical-composition-of-lunar-soil", date: ""}
  - {title: "Kleinhenz and Paz, NASA: Case study for lunar ISRU systems utilizing polar water (ASCEND 2020)", url: "https://ntrs.nasa.gov/api/citations/20205008303/downloads/AIAA_ASCEND2020_Kleinhenz_presentation_final.pdf", date: "Nov 2020"}
  - {title: "Nugent et al., NASA: Space exploration applications for development of high capacity cryocoolers", url: "https://ntrs.nasa.gov/citations/20205010721", date: "Dec 2020"}
  - {title: "Wikipedia: Oxygen (heat of vaporization, heat capacity)", url: "https://en.wikipedia.org/wiki/Oxygen", date: ""}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface (ISRU power over 3–5 km)", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
---

## What it does

Lunar rock and soil is about 41–45% oxygen by mass<sup class="r">[5](#s5)</sup>, but the oxygen is locked in minerals. This plant melts regolith and passes an electric current through the melt. Oxygen gas forms at the anode and metals collect at the cathode<sup class="r">[1](#s1)</sup>. A carbothermal reactor flies alongside as a backup, so one process failing does not stop oxygen production.

## How it works

**Feedstock.** Sieved regolith from the M05 stockpile is metered into the reactor. Sierra Space's carbothermal reactor has already shown automated regolith feed, processing and removal of spent material in a dusty thermal-vacuum chamber at NASA JSC<sup class="r">[2](#s2)</sup>.

**Reactor and electrodes.** In NASA and Lunar Resources' 2024 ground test, heaters brought 25 kg of simulant to about 1,300 °C. Electrolysis then started at 45 V. The current itself kept the melt hot (Joule heating), pushing it beyond 1,700 °C. The run lasted 9 hours at 45 V and 210 A, and made oxygen at an average of 0.07 kg/h. That is 2.3% of the melt by weight<sup class="r">[1](#s1)</sup>. Peak power draw was about 9 kW<sup class="r">[1](#s1)</sup>. Blue Origin's Blue Alchemist, also a molten regolith process, passed its critical design review in September 2025<sup class="r">[3](#s3)</sup>.

**Gas handling.** In the ground test, gas samples reached up to 80% oxygen by volume<sup class="r">[1](#s1)</sup>. So the gas must be cleaned. NASA lists gas clean-up, compression and accumulators as the next subsystems to develop<sup class="r">[1](#s1)</sup>.

**Liquefaction hand-off.** Clean oxygen goes to the 90 K cryocooler in C06.3. NASA puts the need for in-situ oxygen liquefaction at about 150 W of cooling at 90 K<sup class="r">[7](#s7)</sup>.

**Slag and metal removal.** After each batch, slag and metal must leave the reactor. NASA lists "feed and removal" and reactor reusability as future work for molten regolith electrolysis<sup class="r">[1](#s1)</sup>. This is the least mature part.

**Backup.** The carbothermal reactor runs at about 1,800 °C and reached TRL 6 in 2024 tests<sup class="r">[2](#s2)</sup>. A NASA study of a 10 t per year carbothermal system estimated 11.8 kWe plus 33.3 kW of direct solar heat, using methane that is recycled<sup class="r">[6](#s6)</sup>.

## Sizing

All rows are this plan's arithmetic (ESTIMATE).

| Item | Working | Result |
|---|---|---|
| Rate | 10,000 kg ÷ 8,766 h | 1.14 kg/h |
| Current | 4 electrons per O₂; 1,000 A gives 1,000 × 3,600 ÷ 96,485 ÷ 4 × 0.032 kg | 0.30 kg/h per 1,000 A, so ≥3,800 A total |
| Power, study basis | 25.83 kW ÷ 1.63 kg/h<sup class="r">[4](#s4)</sup> = 15.8 kWh/kg; × 1.14 kg/h | ~18 kW |
| Power, demo basis | 0.3 mol O₂ per kWh<sup class="r">[1](#s1)</sup> = 9.6 g/kWh = 104 kWh/kg; × 1.14 kg/h | ~120 kW |
| Feedstock at 2.3% yield | 10 t ÷ 0.023 | 435 t/yr |
| Feedstock at 10% / 20% yield (design targets) | 10 t ÷ 0.10; 10 t ÷ 0.20 | 100 / 50 t/yr |
| Liquefaction heat | 0.918 kJ/kg·K × 210 K + 213 kJ/kg<sup class="r">[8](#s8)</sup> = 406 kJ/kg; × 1.14 kg/h | ~130 W at 90 K |

Design choice: four electrolysis cells of about 1,000 A each, plus one spare. The gap between 18 kW and 120 kW is the single biggest unknown. With 26 kW at demo efficiency, output would be about 0.25 kg/h, or roughly 2 t a year.

## Testing and qualification

1. Run a full-size cell on simulant matched to M01 data, in vacuum, for at least 1,000 hours. Measure kWh/kg, current efficiency and wear.
2. Demonstrate slag and metal tapping and reuse of the same crucible for at least 20 batches.
3. Test freeze and restart after a simulated power loss.
4. Qualify the integrated plant (feed, cells, gas train, controls) in a dusty thermal-vacuum chamber.
5. On the Moon, commission one cell, then add cells one at a time. Run for six months and publish all data.

## Open questions

- The plant must sit within 10 km of cable run of the PMC (DD-013, DD-014), but NASA expects ISRU to need power over 3–5 km<sup class="r">[9](#s9)</sup>. Is regolith of the right quality within that reach, or must feedstock be hauled in?
- What anode material survives months in molten regolith, and how fast does it wear?
- Does energy per kg fall toward the study figure as the reactor gets bigger?
- Is beneficiation worth its mass, or should raw sieved regolith go straight in?
- Can metal from the cathode be tapped cleanly enough to be useful to M12?
- How much carbon does the carbothermal backup lose per tonne of oxygen?
