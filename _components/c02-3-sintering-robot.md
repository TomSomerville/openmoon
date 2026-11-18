---
id_code: "C02.3"
milestone: M02
order: 3
title: Regolith sintering and construction robot
summary: "A mobile robot that spreads thin layers of regolith and fuses them with a laser or microwave beam, building pad surfaces, road sections and berm crests from local material."
trl: 4
spec:
  - {k: "Heritage", v: "ICON Project Olympus (laser VMX); NASA MMPACT microwave sintering"}
  - {k: "Quantity", v: "2 units (M02 plan)"}
  - {k: "Mass per unit", v: "~1.5 t (ESTIMATE; M02 budgets ~3 t for two; NASA studied a 2 t microwave paver vehicle)"}
  - {k: "Beam power", v: "30 kW per unit (design choice, ESTIMATE)"}
  - {k: "Fusing rate", v: "~72 kg/h per unit (ESTIMATE, see Sizing)"}
  - {k: "Layer", v: "Thin layers built up to 50 mm surfaces (design choice)"}
  - {k: "Product", v: "Fused regolith, ~2.7 g/cm³, ~50,000 psi compressive (ICON lab data)"}
  - {k: "Power", v: "Cable from the M04 grid, with a small battery for moves"}
  - {k: "Control", v: "Autonomous build paths, supervised from Earth"}
subcomponents:
  - name: Energy source
    desc: "A high-power laser (baseline) or microwave applicator heats each layer to sinter and melt it onto the layer below."
    parts: ["Fibre laser modules (or magnetron and horn)", "Beam delivery optics", "Cooling loop and radiator", "Dust-protected output window"]
    tech: "ICON laser VMX toolhead; NASA MSFC microwave tests"
    trl: 4
  - name: Gantry or arm
    desc: "A robotic arm on a mobile base moves the toolhead across the work area in set paths."
    parts: ["6-DOF thermal-vacuum rated arm", "Mobile base with wheels", "Stabiliser feet", "Multi-tool end effector"]
    tech: "ICON TVAC robot arm"
    trl: 4
  - name: Feed system
    desc: "Scoops, filters and tamps regolith into a flat, even layer before fusing."
    parts: ["Scoop and hopper", "Sieve to remove large grains and rocks", "Spreader blade", "Tamp or roller", "Interface to excavator dumps (C02.1)"]
    tech: "ICON scoop/tamp/filter system, designed with NASA KSC"
    trl: 4
  - name: Sensors
    desc: "Sensors map the layer before fusing, watch temperature during fusing and check the result after."
    parts: ["Lidar or structured light for layer height", "Thermal camera or microwave radiometer", "Off-gas mass spectrometer", "Visual cameras with dust covers"]
    tech: "MMPACT forward work list"
    trl: 3
  - name: Power and thermal
    desc: "A tethered cable brings grid power; waste heat goes to a radiator."
    parts: ["Tether reel and connector", "Power conversion for laser drivers", "Battery for moves and safe shutdown", "Radiator and heaters"]
    tech: "Plan design choice; M04 grid"
    trl: 4
risks:
  - {sev: Critical, title: "Laser or microwave fusing at pad scale has not been shown in vacuum; ICON's arm was only scheduled for full-scale TVAC testing in 2024", fix: "Build a full-size pad section in a large vacuum chamber before flight; keep paver and polymer fallbacks."}
  - {sev: High, title: "Fusing rate and energy per kilogram are not published, so build times are uncertain", fix: "Measure rate and energy in chamber tests; size the fleet and grid power from measured data."}
  - {sev: High, title: "Regolith is a strong insulator and its microwave absorption varies with mineralogy", fix: "Tune settings to M01 site samples; carry both laser and microwave options until tests pick one."}
  - {sev: High, title: "Optics and applicators face an 1100 °C surface and released volatiles", fix: "Purge or shutter the output window; plan window and applicator replacement as spares."}
  - {sev: Medium, title: "Dust during site prep can cause navigation and positioning errors", fix: "Use fixed survey markers; fuse areas soon after they are prepared."}
  - {sev: Medium, title: "Uneven layers give weak spots and varying density", fix: "Scan each layer before fusing; re-tamp or skip areas out of tolerance; inspect finished areas."}
  - {sev: Medium, title: "High-power laser is an eye and equipment hazard near crew", fix: "Robot works only when no crew are in line of sight; interlocks and keep-out zones."}
sources:
  - {title: "ICON: ICON to develop lunar surface construction system with $57.2M NASA award", url: "https://www.iconbuild.com/newsroom/icon-to-develop-lunar-surface-construction-system-with-57-2-million-nasa-award", date: "Nov 2022"}
  - {title: "ICON: Project Olympus, LSIC slides", url: "https://lsic.jhuapl.edu/uploadedDocs/focus-files/2291-ICON%20Olympus%20LSIC%20Slides%2031JAN2024.pdf", date: "Jan 2024"}
  - {title: "NASA: NASA enables construction technology for Moon and Mars exploration (Olympus, Duneflow)", url: "https://www.nasa.gov/directorates/stmd/nasa-enables-construction-technology-for-moon-and-mars-exploration/", date: "May 2025"}
  - {title: "Effinger, NASA MSFC: Microwave sintering lunar landing pads and horizontal infrastructure (MMPACT)", url: "https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf", date: "Dec 2020"}
  - {title: "Gelino et al., NASA KSC: In-situ lunar launch and landing pad construction with regolith-thermoset polymer composites", url: "https://ntrs.nasa.gov/api/citations/20220000334/downloads/In%20situ%20Lunar%20Launch%20and%20Landing%20Pad%20Construction%20with%20Regolith%20and%20Thermoset%20Polymers%20ASCE%20Earth%20and%20Space%202022%20Paper%20SUBMITTED.pdf", date: "2022"}
---

## What it does

The construction robot turns loose regolith into a hard, ceramic-like surface. It builds the fused cores of the C02.2 landing pads, busy road sections and the crests of berms. It uses only local regolith, so Open Moon does not have to ship binder from Earth.

## How it works

**Energy source.** ICON's Laser Vitreous Multi-material Transformation (VMX) is a powder-bed method. The robot lays thin layers of regolith and fuses them with a laser. Each spot is preheated, sintered, melted onto the layer below and then crystallised<sup class="r">[2](#s2)</sup>. ICON holds a $57.2M NASA SBIR Phase III contract for Project Olympus. Its stated targets are landing pads, blast shields and roads<sup class="r">[1](#s1)</sup>. The other option is microwave sintering. NASA's MMPACT project worked on it for pads and roads, aiming at a 2 t microwave paver vehicle<sup class="r">[4](#s4)</sup>. Open Moon uses laser as the baseline and keeps microwave as an alternative.

**Arm.** ICON's process uses a 6-DOF robot arm with a multi-tool end effector. ICON reported the arm working in thermal vacuum at subsystem scale. A full-scale test at NASA Marshall was planned for early 2024<sup class="r">[2](#s2)</sup>. Open Moon mounts the arm on a wheeled base.

**Feed.** ICON's scoop, tamp and filter system was designed with NASA KSC<sup class="r">[2](#s2)</sup>. C02.1 excavators dump regolith next to the robot. The robot sieves it, spreads it and tamps it flat.

**Sensors.** MMPACT lists the sensors still to be adapted: terrain mapping, applicator positioning, temperature measurement by radiometer or thermography, and off-gas mass spectrometry<sup class="r">[4](#s4)</sup>.

**Product.** ICON's vacuum-made VMX material measured about 50,000 psi compressive strength at 25 °C. After one year of lunar thermal-vacuum cycling it measured about 36,500 psi. Its density is 2.7 g/cm³<sup class="r">[2](#s2)</sup>. ICON's Duneflow experiment flew on a Blue Origin suborbital flight in February 2025. It tested regolith flow in about two minutes of lunar gravity<sup class="r">[3](#s3)</sup>.

## Sizing

The energy needed per kilogram of fused regolith is not published for VMX or MMPACT. The figure below is an assumption that contributors should replace with test data.

| Item | Value | Basis |
|---|---|---|
| Beam power per unit | 30 kW | Design choice (ESTIMATE) |
| Energy to fuse 1 kg | 1.5 MJ | ASSUMPTION, unsourced |
| Rate per unit | 72 kg/h | 30 kW × 3,600 s ÷ 1.5 MJ |
| Rate, 2 units | 144 kg/h | 2 × 72 |
| Pad 1 core (~95 t, C02.2) | ~660 h, ~28 days nonstop | 95,000 ÷ 144 |
| Pad 2 core (~265 t, C02.2) | ~1,840 h, ~77 days nonstop | 265,000 ÷ 144 |
| Grid draw, 2 units | ~70 kW | 60 kW beam + ~10 kW other loads (ESTIMATE) |

At 50% uptime, pad 1 takes about 2 months and pad 2 about 5 months. That is a large share of the early grid. So fusing should be scheduled when the ISRU plant is not running at full power.

## Testing and qualification

1. **Coupons in vacuum** from site-like simulants. Measure strength, density and energy per kilogram.
2. **Hot-fire tests** of fused coupons, as NASA did for pavers and polymer pads<sup class="r">[5](#s5)</sup>.
3. **Full-scale arm and toolhead in a thermal vacuum chamber**, building a multi-square-metre section.
4. **Field test on Earth:** build a 10 m test pad with the excavators, in the open.
5. **On the Moon:** fuse a small test patch, scan it and test it. Then build pad 1.

## Open questions

- What is the real energy per kilogram in vacuum, with site regolith?
- Laser or microwave: which tolerates dust, volatiles and varying minerals better?
- How long do optics or applicators last before replacement?
- Can the same robot build vertical structures for the habitat zone (M08) later?
