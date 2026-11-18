---
id_code: M13
order: 13
title: Self-sustaining colony
phase: 4
window: "2040–2050"
summary: Grow the base into a colony of 50–100 people that makes most of what it uses, with Earth supplying only electronics, medicines, specialist parts and people.
objective: "Reach a population of 50–100 with at least 90% of consumables mass and at least 80% of construction mass produced on the Moon, and a local economy that sells propellant, services and data to cover a meaningful share of operating costs."
trl_min: 4
depends_on: [M09, M10, M11, M12]
spec:
  - {k: Population, v: "50–100"}
  - {k: "Local consumables", v: "≥90% by mass"}
  - {k: "Local construction", v: "≥80% by mass"}
  - {k: "From Earth", v: "Electronics, medicines, specialist parts, people"}
cost: {low: 40.0, high: 120.0, note: "10 years of operations and expansion"}
cost_items:
  - {item: "Operations, 10 years", low: 30.0, high: 80.0, basis: "ESTIMATE; ISS operations cost about $3B per year [benchmark]; range $3–8B/yr"}
  - {item: "Expansion: habitats, power, greenhouses", low: 10.0, high: 40.0, basis: "ESTIMATE; mostly built from local materials by this stage"}
exit_criteria:
  - "Population of at least 50 living continuously on the Moon."
  - "≥90% of consumables mass and ≥80% of construction mass produced locally."
  - "Colony revenue covers a published share of operating costs."
  - "A governance and safety framework agreed with all operators at the site."
workstreams:
  - name: Population growth
    desc: Grow from the 6-person crewed base (M09, DD-006) as housing, food and health data allow.
    items: ["Habitat expansion with local construction", "Longer rotations only when health data supports them", "Medical facility"]
  - name: Local economy
    desc: Earn revenue.
    items: ["Propellant sales to landers", "Hosting payloads and science", "Data, communications and services"]
  - name: Governance
    desc: Operate under international law.
    items: ["Outer Space Treaty (no territorial claims)", "Artemis Accords deconfliction", "Shared rules with other operators"]
  - name: Future growth
    desc: Options beyond 2050.
    items: ["Lava tubes for large shielded volumes", "Larger industrial base"]
technologies:
  - {name: "Everything in M00–M12", use: "Foundation", status: "See earlier milestones", trl: 4}
  - {name: "Lava tubes", use: "Future shielded volume", status: "Radar evidence of a cave under the Mare Tranquillitatis pit (2024); Marius Hills pit ~40 m deep", trl: 2, new: true, src: 2}
sources:
  - {title: "NASA OIG IG-22-005: ISS operations cost (~$3B/yr)", url: "https://oig.nasa.gov/docs/IG-22-005.pdf", date: "Nov 2021"}
  - {title: "phys.org: Lunar lava tube cave (Carrer et al., Nature Astronomy)", url: "https://phys.org/news/2024-07-lunar-lava-tube-cave.html", date: "Jul 2024"}
  - {title: "PwC: Lunar market assessment, 2nd edition (Building the lunar economy)", url: "https://images.content.pwc.com/Web/PwCGlobal/%7Bfe86e29b-7590-4a9e-acf9-d7fdb3c55ba6%7D_FR_FY26_Lunar_Market_Assessment_Edition2_Download.pdf", date: "Jan 2026"}
  - {title: "UNOOSA: Outer Space Treaty", url: "https://www.unoosa.org/pdf/publications/ST_SPACE_51E.pdf", date: ""}
  - {title: "NASA: Artemis Accords", url: "https://www.nasa.gov/artemis-accords/", date: ""}
  - {title: "US Public Law 114-90 (Commercial Space Launch Competitiveness Act)", url: "https://www.govinfo.gov/content/pkg/PLAW-114publ90/html/PLAW-114publ90.htm", date: "Nov 2015"}
  - {title: "LROC: Marius Hills pit – lava tube skylight?", url: "https://lroc.im-ldi.com/images/202", date: ""}
risks:
  - {sev: Critical, title: "Long-term health at 1/6 g is unknown, including pregnancy and child development", fix: "Grow only on data; this plan does not assume families or births on the Moon"}
  - {sev: High, title: "Revenue may not materialise (PwC projects $94–127B in cumulative lunar surface revenue 2026–2050, across five market segments)", fix: "Plan on government funding as the base case; treat revenue as upside"}
  - {sev: High, title: "Total independence from Earth is not achievable with today's technology (chips, medicines)", fix: "Define self-sustaining by mass, not by value; keep a reliable supply chain for high-tech items"}
---

## What "self-sustaining" means here

**Honest definition:** no realistic technology will make a lunar colony fully independent of Earth by 2050. Chips, medicines and precision instruments will still come from Earth. Open Moon defines self-sustaining **by mass**:

- at least 90% of consumables made on the Moon
- at least 80% of construction mass made on the Moon

That's measurable, and it is what drives cost.

## The economy

- **Market forecast.** PwC's 2026 update forecasts **$93.9–127.3B** of cumulative revenue from lunar surface activities for 2026–2050, summed across five market segments<sup class="r">[3](#s3)</sup>.
- **Legal basis.** US law lets citizens keep and sell space resources they recover<sup class="r">[6](#s6)</sup>, within the Outer Space Treaty's ban on territorial claims<sup class="r">[4](#s4)</sup>.

## Beyond 2050

Lava tubes could offer large, naturally shielded spaces:

- radar points to a cave under the Mare Tranquillitatis pit<sup class="r">[2](#s2)</sup>
- the Marius Hills pit is about 40 m deep<sup class="r">[7](#s7)</sup>

Both are far from the south pole, and building in them is beyond this plan's 3–5 year technology rule.
