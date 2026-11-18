---
id_code: M12
order: 12
title: Manufacturing and construction from regolith
phase: 3
window: "2037–2044"
summary: Make metals, glass, solar cells, building blocks and spare parts on the Moon, so new structures and repairs need little from Earth.
objective: "Produce at least 80% of new construction mass and at least 50% of spare-part mass (by mass, not by value) from lunar materials."
trl_min: 4
depends_on: [M05, M06, M11]
spec:
  - {k: Metals, v: "Iron, aluminium, silicon from regolith processing by-products"}
  - {k: Construction, v: "Sintered and printed regolith structures"}
  - {k: Parts, v: "Metal and polymer 3D printing; recycling"}
  - {k: Power, v: "Solar cells from regolith"}
cost: {low: 5.5, high: 16.0, note: "factory equipment and delivery"}
cost_items:
  - {item: "Factory equipment development", low: 1.0, high: 3.0, basis: "ESTIMATE"}
  - {item: "Delivery of factory equipment (~20 t)", low: 4.0, high: 12.0, basis: "20 t × $0.2–0.6M/kg (ESTIMATE)"}
  - {item: "Operations", low: 0.5, high: 1.0, basis: "ESTIMATE"}
exit_criteria:
  - "≥80% of new construction mass from lunar materials over a year."
  - "≥50% of spare-part mass printed or made on site over a year."
  - "First lunar-made solar array producing power on the grid."
workstreams:
  - name: Metals
    desc: Recover metals from oxygen-plant by-products.
    items: ["Iron and silicon from MRE", "Mixed metals from molten salt electrolysis", "Aluminium extraction research"]
  - name: Construction
    desc: Build with regolith.
    items: ["Regolith construction systems (ICON Olympus)", "Printed regolith dome (ESA / Foster+Partners concept)", "Sintered bricks"]
  - name: Parts manufacturing
    desc: Print what breaks.
    items: ["Metal 3D printing (ESA ISS printer heritage)", "Polymer printing and recycling (ISS AMF, Refabricator)", "Machining for finishing"]
  - name: Solar cells
    desc: Make power hardware locally.
    items: ["Silicon from regolith", "Cover glass from by-products", "Array assembly"]
technologies:
  - {name: "Blue Origin Blue Alchemist", use: "Silicon, solar cells, wire from regolith", status: "Company reports solar cells and wire from simulant; passed CDR 2025; autonomous ground demo planned 2026", trl: 5, new: true, src: 9}
  - {name: "ESA metal 3D printer on ISS", use: "Printing metal parts", status: "First metal part printed in space, Aug 2024", trl: 7, src: 2}
  - {name: "Redwire / Made In Space AMF on ISS", use: "Polymer parts", status: "Commercial polymer printer on ISS (ABS, ULTEM, HDPE); parts printed since at least Feb 2017", trl: 9, src: 3}
  - {name: "Redwire Regolith Print", use: "Printing with regolith simulant", status: "Printed with regolith simulant on ISS (launched Aug 2021)", trl: 5, src: 4}
  - {name: "ICON Project Olympus", use: "Regolith construction", status: "$57.2M NASA SBIR Phase III contract", trl: 4, new: true, src: 5}
  - {name: "Molten salt electrolysis (Metalysis/ESA)", use: "Metals + oxygen", status: "ESA prototype plant (2020); leaves a tangle of mixed metals", trl: 4, new: true, src: 6}
sources:
  - {title: "Blue Origin: Blue Alchemist powers our lunar future", url: "https://www.blueorigin.com/news/blue-alchemist-powers-our-lunar-future/", date: "Feb 2023"}
  - {title: "ESA: ESA 3D prints first metal part on the ISS", url: "https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station", date: "Sep 2024"}
  - {title: "NASA NTRS 20190030402: In-space manufacturing on ISS", url: "https://ntrs.nasa.gov/api/citations/20190030402/downloads/20190030402.pdf", date: "2019"}
  - {title: "Redwire: Regolith manufacturing technology", url: "https://rdw.com/newsroom/redwire-regolith-manufacturing-technology-wins-popular-science-2021-best-of-whats-new-award/", date: "Dec 2021"}
  - {title: "ICON: $57.2M NASA award", url: "https://www.iconbuild.com/newsroom/icon-to-develop-lunar-surface-construction-system-with-57-2-million-nasa-award", date: "Nov 2022"}
  - {title: "ESA: ESA opens oxygen plant making air out of moondust", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust", date: "Jan 2020"}
  - {title: "ESA: Building a lunar base with 3D printing", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Building_a_lunar_base_with_3D_printing", date: "Jan 2013"}
  - {title: "Geology of the Moon (regolith composition), Wikipedia", url: "https://en.wikipedia.org/wiki/Geology_of_the_Moon", date: "accessed Nov 2026"}
  - {title: "Blue Origin: Blue Alchemist hits major milestone toward permanent, sustainable lunar infrastructure", url: "https://www.blueorigin.com/news/blue-alchemist-hits-major-milestone-toward-permanent-sustainable-lunar-infrastructure", date: "Sep 2025"}
  - {title: "NASA M2M-30044 Lunar Surface Data Book (south pole is highlands terrain)", url: "https://ntrs.nasa.gov/citations/20250002845", date: "Mar 2025"}
risks:
  - {sev: High, title: "Many processes are only proven in labs (TRL 4)", fix: "Start with the most mature (printing, sintering); add metals as they mature"}
  - {sev: High, title: "Electronics and precision parts can't be made locally", fix: "Ship electronics; make structures, enclosures and bulk parts locally"}
  - {sev: Medium, title: "Quality control of lunar-made parts", fix: "Test coupons from every batch; tensile testing on site"}
---

## What regolith contains

Average lunar surface composition<sup class="r">[8](#s8)</sup>:

| Oxide | Maria | Highlands |
|---|---|---|
| FeO | ~14.1% | ~5.9% |
| Al₂O₃ | ~14.9% | ~24.0% |
| TiO₂ | ~3.9% | ~0.6% |
| SiO₂ | ~45% | ~45% |

**What this means at the base:** the south pole is highlands terrain<sup class="r">[10](#s10)</sup>, so the regolith is richer in aluminium and poorer in iron.

## Step-by-step

1. **Polymer and metal printers** inside the habitat, building on ISS heritage<sup class="r">[2](#s2)</sup><sup class="r">[3](#s3)</sup>.
2. **Regolith construction** for berms, pads and shells, building on ICON's NASA-funded work<sup class="r">[5](#s5)</sup> and ESA's regolith 3D printing tests<sup class="r">[7](#s7)</sup>.
3. **Metal recovery** from oxygen-plant by-products<sup class="r">[1](#s1)</sup><sup class="r">[6](#s6)</sup>.
4. **Solar cells from regolith.** Blue Origin reports making solar cells from simulant<sup class="r">[1](#s1)</sup><sup class="r">[9](#s9)</sup>. Install the first lunar-made array.
