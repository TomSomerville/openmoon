---
id_code: "C06.2"
milestone: M06
order: 2
title: "Ice mining and water extraction plant"
summary: "Cold-rated excavators dig icy regolith inside a permanently shadowed crater, heat it in a sealed oven, and catch the water vapour on a cold trap. The water is cleaned and stored for drinking, fuel cells and propellant."
trl: 4
spec:
  - {k: "Output target", v: "10 t of purified water per year"}
  - {k: "Assumed ice content", v: "5% by mass, 75% extracted (NASA study assumptions)"}
  - {k: "Regolith to process", v: "~267 t per year (ESTIMATE)"}
  - {k: "Mine area", v: "~26 m × 26 m per year at 30 cm depth (ESTIMATE)"}
  - {k: "Working temperature", v: "PSR surfaces 50–120 K (NASA study assumption)"}
  - {k: "Power at mine", v: "~15 kW (ESTIMATE, scaled from NASA study)"}
  - {k: "Mass", v: "~3 t including excavator (M06 ESTIMATE)"}
  - {k: "Haul distance", v: "~5 km each way, slopes ~16° (NASA study site)"}
  - {k: "Delivery class", v: "Medium lander"}
subcomponents:
  - name: "Cold-rated excavator"
    desc: "Removes the dry top layer and digs icy regolith in the dark at 50–120 K."
    parts: ["Counter-rotating bucket drums", "Heated electronics box", "Wheels and drive motors rated for cryogenic temperature", "Lights, lidar and cameras", "Battery and tether option"]
    tech: "NASA RASSOR; Break the Ice Lunar Challenge rovers (2024)"
    trl: 4
  - name: "Haul and transfer"
    desc: "Moves icy regolith to the oven and spent regolith back to the pit; carries water out of the crater."
    parts: ["Regolith hopper", "Water tanker vehicle", "Insulated water tank", "Dust-tolerant fluid coupling"]
    tech: "NASA polar water case study (2 tankers); KSC dust-tolerant umbilical"
    trl: 4
  - name: "Sealed heating chamber (oven)"
    desc: "Heats icy regolith in a closed volume so the ice turns to vapour and does not escape to vacuum."
    parts: ["Auger dryer with heated casing", "Inlet and outlet seals or lock", "Heaters (electric or waste heat)", "Temperature and pressure sensors", "Spent regolith chute"]
    tech: "Auger dryer modelled in NASA case study; lab breadboards"
    trl: 3
  - name: "Cold trap"
    desc: "Freezes the water vapour onto cold plates as ice, then warms to release it as liquid or move it as ice."
    parts: ["Cold plates or finned condenser", "Radiator to the PSR sky", "Defrost heaters", "Non-condensable gas vent"]
    tech: "NASA thermal mining and frost-deposition tests"
    trl: 4
  - name: "Purification"
    desc: "Removes dissolved gases, dust and trace metals so the water is safe to drink and to electrolyse."
    parts: ["Degassing step (CO, CO₂, NH₃, H₂S, CH₄)", "Particle filters", "Ion-exchange or sorbent beds for metals including mercury", "Distillation stage", "Conductivity and pH sensors"]
    tech: "Terrestrial water treatment; ISS water processing heritage"
    trl: 4
  - name: "Water storage"
    desc: "Holds clean water above freezing near the base and hands it to C06.3 and the M04 fuel cells."
    parts: ["Aluminium tanks", "Heaters and insulation", "Level and quality sensors", "Transfer pump"]
    tech: "Standard spacecraft water tanks"
    trl: 6
risks:
  - {sev: Critical, title: "No ice deposit suitable for mining has been located yet; the real ice content may be far below 5%", fix: "Site the plant only from M01 drilling data; oxygen-from-rock (C06.1) covers breathing oxygen if ice fails"}
  - {sev: High, title: "Electronics, lubricants and seals must work at 50–120 K", fix: "Keep electronics in heated boxes; use dry lubricants; test at temperature in a thermal-vacuum chamber"}
  - {sev: High, title: "LCROSS saw CO, NH₃, CH₄, H₂S and mercury with the water; some are toxic", fix: "Multi-stage purification and testing of every batch; vent or capture gases as by-products"}
  - {sev: High, title: "Abrasive dust wears oven seals and lets vapour leak", fix: "Replaceable seals; measure leak rate; design the oven so a leak lowers yield instead of stopping it"}
  - {sev: Medium, title: "A dry top layer of unknown depth must be removed first", fix: "Measure overburden with M01 drilling; size excavator time with margin"}
  - {sev: Medium, title: "Many round trips into and out of the crater wear vehicles", fix: "Larger water tanks to cut trips; plan maintenance at the sunlit base"}
  - {sev: Medium, title: "Cold trap fills unevenly and loses capture efficiency", fix: "Several smaller traps cycled in turn; measure deposit rate in ground tests"}
  - {sev: Medium, title: "Navigation and communication in permanent darkness", fix: "Lidar and lights on vehicles; M03 relay at the crater rim"}
sources:
  - {title: "Kleinhenz and Paz, NASA: Case study for lunar ISRU systems utilizing polar water (ASCEND 2020)", url: "https://ntrs.nasa.gov/api/citations/20205008303/downloads/AIAA_ASCEND2020_Kleinhenz_presentation_final.pdf", date: "Nov 2020"}
  - {title: "NASA: California teams win $1.5 million in NASA's Break the Ice Lunar Challenge", url: "https://www.nasa.gov/centers-and-facilities/marshall/california-teams-win-1-5-million-in-nasas-break-the-ice-lunar-challenge", date: "Jun 2024"}
  - {title: "NASA: NASA missions uncover the Moon's buried treasures (LCROSS and LRO results)", url: "https://www.nasa.gov/news-release/nasa-missions-uncover-the-moons-buried-treasures", date: "Oct 2010"}
  - {title: "Colaprete et al., Science: Detection of water in the LCROSS ejecta plume", url: "https://experts.arizona.edu/en/publications/detection-of-water-in-the-lcross-ejecta-plume/", date: "Oct 2010"}
  - {title: "Townsend, Mueller and Tamasy, NASA KSC: Dust tolerant commodity transfer interface mechanisms for planetary surfaces", url: "https://ntrs.nasa.gov/citations/20150000177", date: "Oct 2014"}
---

## What it does

Ice is trapped in the cold, permanently shadowed regions (PSRs) near the poles. The LCROSS impact into Cabeus crater found water ice at about 5.6 ± 2.9% by mass in the regolith<sup class="r">[4](#s4)</sup>. This plant digs that icy soil, heats it, captures the water and cleans it. Water gives drinking supply, fuel-cell storage for M04 and, once split, hydrogen and oxygen.

## How it works

This plan follows the architecture of a NASA case study. Excavators work in the PSR. Water is extracted at the mine and carried out of the crater by tankers to a sunlit ridge<sup class="r">[1](#s1)</sup>.

**Excavator.** The NASA study used RASSOR, a dual bucket-drum excavator<sup class="r">[1](#s1)</sup>. In NASA's Break the Ice Lunar Challenge (June 2024), the second-place rover used a drum scraping tool to mine, collect and haul material<sup class="r">[2](#s2)</sup>. The study assumed PSR surface temperatures between 50 K and 120 K<sup class="r">[1](#s1)</sup>.

**Oven.** Icy regolith is heated so the water leaves as vapour. The NASA study modelled an auger that moves regolith through a heated casing, with 75% extraction efficiency<sup class="r">[1](#s1)</sup>. The chamber is sealed so vapour goes to the cold trap, not to vacuum.

**Cold trap.** Vapour freezes onto cold plates. In the NASA study, extracted water is frozen into a tank on a mobile tanker<sup class="r">[1](#s1)</sup>.

**Purification.** LCROSS and LRO found that up to 20% of the material thrown up by the impact was volatiles. These included methane, ammonia, hydrogen, carbon dioxide and carbon monoxide, plus light metals such as sodium and mercury<sup class="r">[3](#s3)</sup>. Sulfur-bearing species and light hydrocarbons were also seen<sup class="r">[4](#s4)</sup>. The NASA study did not yet include water clean-up<sup class="r">[1](#s1)</sup>. This plan adds degassing, filtration, sorbent beds and distillation.

**Transfer and storage.** The NASA study used a dust-tolerant automated umbilical for fluid transfer<sup class="r">[1](#s1)</sup>. NASA KSC has built and demonstrated an automated interface for fluids, power and data, designed against regolith dust<sup class="r">[5](#s5)</sup>.

## Sizing

The NASA baseline: 15 t of water from regolith with 5% water and 75% extraction needed 398 t of regolith, a 32 m × 32 m mine 30 cm deep, and 22 kW at the mine, over 225 days of production<sup class="r">[1](#s1)</sup>.

This pilot (ESTIMATE, same assumptions):

| Item | Working | Result |
|---|---|---|
| Regolith | 10 t ÷ (0.05 × 0.75) | 267 t/yr |
| Volume | 267 t ÷ 1.3 t/m³<sup class="r">[1](#s1)</sup> | 205 m³ |
| Mine area at 30 cm | 205 ÷ 0.3 | 684 m² (~26 m × 26 m) |
| Mine power | 22 kW × (10 ÷ 15), same 225 operating days | ~15 kW |

The NASA study found that at 1% water the extraction system no longer scales well<sup class="r">[1](#s1)</sup>. If M01 measures less than about 3%, this plant should be resized before flight.

## Testing and qualification

1. Test each part at 50–120 K in a thermal-vacuum chamber with icy simulant.
2. Run the oven and cold trap together in vacuum. Measure recovery, energy per kg and seal leakage.
3. Add known amounts of CO, NH₃, H₂S and mercury to the simulant and prove the purification removes them.
4. Drive the excavator and tanker over a 5 km course with 16° slopes, as in the NASA study site<sup class="r">[1](#s1)</sup>.
5. On the Moon, start with short excursions from the crater edge, then extend run time. Publish yield and contaminant data.

## Open questions

- What is the real ice content and depth at the chosen PSR? (M01)
- Should water be carried out as ice or as liquid?
- Can waste heat from the power system heat the oven, to save electricity?
- How much mercury and sulphur is in the water, and which purification stage removes it best?
- How fast does dust wear the oven seals?
