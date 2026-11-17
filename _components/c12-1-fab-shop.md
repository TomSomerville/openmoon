---
id_code: "C12.1"
milestone: M12
order: 1
title: Fabrication shop
summary: "A pressurised workshop with a metal 3D printer, polymer printers and a plastic recycler, a small regolith printer, machine tools and a test lab. It makes spare parts and tools on site and checks that they are strong enough to use."
trl: 5
spec:
  - {k: "Location", v: "One pressurised module bay, ~30 m² floor (ESTIMATE)"}
  - {k: "Metal process", v: "Wire-fed laser printing in a sealed inert-gas box (ESA ISS printer heritage)"}
  - {k: "Polymer materials", v: "ABS, ULTEM 9085, HDPE (ISS AMF materials)"}
  - {k: "Recycling", v: "Used parts and packaging back to filament (Refabricator heritage)"}
  - {k: "Output target", v: "~1 t of parts per year (plan design target, ESTIMATE)"}
  - {k: "Power", v: "~10 kW peak, ~3 kW average (ESTIMATE)"}
  - {k: "Delivered mass", v: "~5 t with 1 t of starter feedstock (ESTIMATE)"}
  - {k: "Quality control", v: "Witness coupons with every build; on-site tensile testing"}
  - {k: "Feedstock", v: "Earth wire and filament first; lunar metals and recycled plastics later"}
subcomponents:
  - name: Metal printer
    desc: "A laser melts metal wire onto a build plate inside a sealed box filled with inert gas."
    parts: ["Laser source and optics", "Wire feeder and spool store", "Sealed build chamber with nitrogen or argon purge", "Replaceable build plates", "Fume and particle filter"]
    tech: "ESA Metal 3D Printer on ISS (Airbus-led)"
    trl: 6
  - name: Polymer printers and recycler
    desc: "Filament printers make plastic parts. A recycler turns failed prints, old parts and packaging back into feedstock."
    parts: ["Two FFF printers (ABS, ULTEM 9085, HDPE)", "Shredder", "Filament extruder (positrusion type)", "Dry-heat and UV steriliser", "Filament dryer and store"]
    tech: "Redwire AMF; Tethers Unlimited Refabricator and ERASMUS"
    trl: 7
  - name: Regolith printer
    desc: "A small printer mixes regolith with a binder to make tiles, blocks and fixtures; a furnace can sinter them."
    parts: ["Regolith-binder print head", "Sieved regolith hopper", "Small sintering furnace", "Print bed and enclosure"]
    tech: "Redwire Regolith Print on ISS (2021)"
    trl: 5
  - name: Machining and finishing
    desc: "Machine tools bring printed parts to final size and surface finish, and make simple parts from bar stock."
    parts: ["Compact 5-axis CNC mill", "Lathe", "Band saw and grinder", "Heat-treat oven", "Chip and dust extraction"]
    tech: "NASA ISM Vulcan (print + 5-axis CNC) and MAMBA (press + CNC mill)"
    trl: 5
  - name: Inspection and testing
    desc: "Measures every part and breaks test coupons from every build, so crew know a part is fit to use."
    parts: ["Coordinate measuring arm and calipers", "Optical microscope", "Tensile and compression test frame", "Hardness tester", "Digital records for each build"]
    tech: "NASA-STD-6030 witness-specimen practice; ISS printed-specimen testing"
    trl: 6
  - name: Feedstock preparation
    desc: "Turns lunar metal by-products, regolith and waste plastic into feedstock the printers can use."
    parts: ["Metal powder sieving and drying", "Metal refining and wire-making (research)", "Regolith sieving and drying", "Packaging collection and sorting"]
    tech: "FFC (ESA) and MRE (Blue Alchemist) by-products; NASA common-use materials"
    trl: 3
risks:
  - {sev: High, title: "Metal printing in space is barely demonstrated: ISS prints are under 250 g and take weeks", fix: "Use Earth-qualified printers built for higher rates; keep CNC machining as a backup; scale up only after test data."}
  - {sev: High, title: "Lunar process metal is a mixed alloy whose usefulness is unknown", fix: "Start with Earth wire; test and refine local metal batch by batch; use it first for non-critical parts."}
  - {sev: High, title: "A weak printed part could fail in a life-critical system", fix: "Witness coupons and tensile tests for every build; use printed parts only in non-critical roles until a database of properties exists."}
  - {sev: Medium, title: "Electronics and precision parts cannot be made locally", fix: "Ship electronics; make structures, brackets, enclosures and tools locally."}
  - {sev: Medium, title: "Fumes, fine powder, lasers and noise in a closed habitat", fix: "Sealed printer box with inert gas; filtered extraction; separate shop module with sound insulation."}
  - {sev: Medium, title: "No published results yet on how recycled ISS plastic held up", fix: "Run recycle-and-test cycles on the ground and in the shop; track strength over each cycle."}
  - {sev: Medium, title: "Metal chips and dust float longer and spread further in 1/6 g", fix: "Fully enclosed machines; dry machining with vacuum extraction; clean-room-style housekeeping."}
sources:
  - {title: "ESA: ESA launches first metal 3D printer to ISS", url: "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/ESA_launches_first_metal_3D_printer_to_ISS", date: "Jan 2024"}
  - {title: "ESA: ESA 3D prints first metal part on the ISS", url: "https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station", date: "Sep 2024"}
  - {title: "ESA: 3D-printed metal, unlocking crew autonomy", url: "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/epsilon/3D-printed_metal_unlocking_crew_autonomy", date: "Jul 2026"}
  - {title: "NASA NTRS 20190030402: Overview of the In-Space Manufacturing technology portfolio", url: "https://ntrs.nasa.gov/api/citations/20190030402/downloads/20190030402.pdf", date: "Jul 2019"}
  - {title: "NASA NTRS 20180006405: In-Space Manufacturing at NASA Marshall (AIAA SPACE 2018)", url: "https://ntrs.nasa.gov/api/citations/20180006405/downloads/20180006405.pdf", date: "2018"}
  - {title: "Redwire: Redwire to demonstrate in-space additive manufacturing for lunar surface on the ISS", url: "https://rdw.com/newsroom/redwire-to-demonstrate-in-space-additive-manufacturing-for-lunar-surface-on-the-international-space-station", date: "Jul 2021"}
  - {title: "NASA-STD-6030: Additive manufacturing requirements for spaceflight systems", url: "https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/2021-04-21_nasa-std-6030-approveddocx.pdf", date: "Apr 2021"}
  - {title: "ESA: ESA opens oxygen plant making air out of moondust", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust", date: "Jan 2020"}
  - {title: "Blue Origin: Blue Alchemist powers our lunar future", url: "https://www.blueorigin.com/news/blue-alchemist-powers-our-lunar-future/", date: "Feb 2023"}
  - {title: "Geology of the Moon (regolith composition), Wikipedia", url: "https://en.wikipedia.org/wiki/Geology_of_the_Moon", date: "accessed Nov 2026"}
---

## What it does

The fab shop makes spare parts, tools, brackets and fittings on site. That way a broken part does not have to wait for the next cargo landing. NASA notes that, historically, **95% of spares are never used**, yet it is impossible to know in advance which ones will be needed<sup class="r">[4](#s4)</sup>. Making parts on demand cuts the spares that must be shipped. It is also how M12 reaches **≥50% of spare-part mass made on site**.

## How it works

**Metal printer.** ESA's Metal 3D Printer on the ISS was built by an Airbus-led team. A high-power laser melts stainless-steel wire inside a fully sealed box. The box's oxygen is replaced with nitrogen so the hot metal does not oxidise. The unit is about **180 kg**. Its test prints are each **under 250 g** and take **two to four weeks**. Noise rules limit printing to **four hours a day**<sup class="r">[1](#s1)</sup>. It printed the first metal part in space in 2024<sup class="r">[2](#s2)</sup>. By July 2026 it had made a fifth sample. Three samples were being compared with ground prints at ESTEC and DTU, and one print had been halted after an anomaly<sup class="r">[3](#s3)</sup>.

**Polymers and recycling.** NASA's first ISS printer made **55** ABS specimens. NASA saw no engineering-significant effect of microgravity on the results<sup class="r">[5](#s5)</sup>. The Additive Manufacturing Facility (AMF) prints ABS, ULTEM 9085 and HDPE<sup class="r">[4](#s4)</sup>. The Refabricator, built by Tethers Unlimited, is a printer and recycler that turns ULTEM parts back into filament. Its test plan was seven print-and-recycle cycles, with five tensile specimens per cycle returned to Earth for testing<sup class="r">[5](#s5)</sup>. ERASMUS adds dry-heat and UV sterilisation, so recycled plastic can be used for medical and food items<sup class="r">[4](#s4)</sup>.

**Regolith printer.** Redwire's Regolith Print used the AMF on the ISS to test printing with a regolith simulant in microgravity<sup class="r">[6](#s6)</sup>.

**Machining.** Printed metal parts need finishing. NASA has funded Vulcan, which combines wire-and-arc printing with a 5-axis CNC mill. It has printed titanium and aluminium. NASA has also funded MAMBA, which presses scrap into ingots and then mills them<sup class="r">[4](#s4)</sup>. NASA's FabLab target for one ISS rack was **2,000 W**, **576 lb** and **16 ft³**, with built-in inspection<sup class="r">[4](#s4)</sup>.

**Inspection and testing.** NASA-STD-6030 sets the rules for additively manufactured flight parts, including witness specimens built alongside the parts<sup class="r">[7](#s7)</sup>. The shop prints coupons with every build and pulls them on its own tensile frame.

**Lunar feedstock.** ESA's molten-salt process works at **950 °C**. It leaves behind a mix of metals, and whether that mix can be printed directly or must be refined first is still open<sup class="r">[8](#s8)</sup>. Blue Origin reports making wire from simulant with molten regolith electrolysis<sup class="r">[9](#s9)</sup>. Highland regolith is ~24% Al₂O₃ and ~5.9% FeO<sup class="r">[10](#s10)</sup>, so aluminium is the likelier local metal at the pole.

## Sizing (ESTIMATE)

| Item | Working |
|---|---|
| Output target | 1 t/yr ÷ 365 ≈ **2.7 kg/day** of parts |
| ESA ISS printer rate | <250 g per 2–4 weeks<sup class="r">[1](#s1)</sup> ≈ **~10 g/day** |
| Gap | 2.7 kg ÷ 10 g ≈ **270×**. The lunar shop needs faster, larger printers plus machining from bar stock. |
| Peak power | metal printer 2 kW (FabLab class<sup class="r">[4](#s4)</sup>) + CNC 3 kW + furnace 3 kW + the rest 2 kW ≈ **10 kW** |
| Mass | printer ~1 t + machine tools ~1 t + polymer and recycler ~0.3 t + test lab ~0.6 t + feedstock prep ~1 t + starter feedstock ~1 t ≈ **5 t** |

## Testing and qualification

1. Qualify each machine on Earth with the same feedstock and procedures. Build a database of material properties (NASA-STD-6030 approach<sup class="r">[7](#s7)</sup>).
2. Fly a copy of each process on the ISS or an early lander, where possible, and compare the results with ground prints, as ESA is doing<sup class="r">[3](#s3)</sup>.
3. On the Moon, print and test reference coupons before making any real part.
4. Make non-critical parts first, then move to load-bearing ones as the data grows.
5. Bring in lunar feedstock one material at a time, with tensile tests on every batch.

## Open questions

- Which lunar alloy from FFC or MRE by-products is good enough to print, and how much refining does it need?
- How fast can a crew-safe, sealed metal printer run on the Moon?
- How much strength does recycled ULTEM lose per cycle? Are results from the ISS Refabricator available?
- Which spare parts make up most of the mass, and can they be printed?
