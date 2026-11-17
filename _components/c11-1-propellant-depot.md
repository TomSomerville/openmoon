---
id_code: "C11.1"
milestone: M11
order: 1
title: "Surface propellant depot and lander refuelling"
summary: "A farm of insulated, cooled tanks near the landing pads that liquefies and stores lunar oxygen at industrial scale, and an automated arm that connects to landers and fills them. It turns lunar oxygen into a product landers can buy."
trl: 4
spec:
  - {k: "Throughput", v: "300 t of LOX per year (about 34 kg/h), from M11"}
  - {k: "Storage", v: "100 t of LOX in four 25 t tanks (design choice)"}
  - {k: "Tank size", v: "Spheres ~3.6 m diameter, 24 m³ each with ullage (ESTIMATE)"}
  - {k: "Liquefaction", v: "~3.9 kW of cooling at 90 K (ESTIMATE)"}
  - {k: "Storage cooling", v: "~250 W at 90 K for the farm (ESTIMATE)"}
  - {k: "Transfer", v: "Up to 50 t per lander visit at ~200 L/min, ~4 h (design case)"}
  - {k: "Hydrogen", v: "Optional later phase; 20 K cooling needed"}
  - {k: "Delivery", v: "Part of ~10 t depot and transfer equipment (M11 ESTIMATE)"}
subcomponents:
  - name: "Storage farm"
    desc: "Four shaded, insulated, actively cooled LOX tanks, set back from the pads behind a regolith berm."
    parts: ["Aluminium spheres, 25 t each", "Multi-layer insulation", "Sun shades and berms", "Tank-mounted 90 K coolers", "Isolation valves between tanks"]
    tech: "C06.3 pilot storage; NASA GRC zero boil-off test"
    trl: 5
  - name: "Liquefaction scale-up"
    desc: "Turns oxygen gas from the M11 plants into liquid, in many small units rather than one large one."
    parts: ["90 K reverse turbo-Brayton coolers (~30 units of 150 W class)", "Gas dryer and purity check", "Pre-cooler heat exchangers", "Radiators", "Spare units"]
    tech: "NASA 90 K cryocooler development"
    trl: 4
  - name: "Transfer arm and couplings at the pad"
    desc: "An automated arm that brings a dust-tolerant cryogenic coupling to the lander, connects, fills and disconnects without crew."
    parts: ["Robotic arm or ground umbilical tower", "Dust-tolerant cryogenic coupling", "Electrical and data connector", "Purge and dust cover", "Breakaway safety release"]
    tech: "NASA KSC automated commodity transfer interface; NASA Armstrong magnetically latching coupler"
    trl: 4
  - name: "Transfer lines and pumps"
    desc: "Vacuum-jacketed pipes and pumps that move LOX from the farm to the pad."
    parts: ["Vacuum-jacketed lines (buried)", "Cryogenic pump", "Chill-down recirculation loop", "Flow meter", "Relief valves"]
    tech: "Terrestrial launch pad LOX systems"
    trl: 5
  - name: "Quantity gauging"
    desc: "Measures mass delivered and mass in each tank, for billing and lander safety."
    parts: ["Radio-frequency mass gauges", "Coriolis or turbine flow meters", "Load cells under tanks", "Temperature and pressure sensors"]
    tech: "NASA Radio Frequency Mass Gauge (IM-1 tanks)"
    trl: 6
  - name: "Safety systems"
    desc: "Protects the depot, landers and crew from oxygen fires, plume debris and over-pressure."
    parts: ["Keep-out zones and berms", "Oxygen-clean components", "Emergency shut-off valves", "Leak and fire detection", "Remote operation from the habitat"]
    tech: "Launch pad oxygen safety practice"
    trl: 5
risks:
  - {sev: Critical, title: "No lander operator has committed to buy lunar oxygen", fix: "Sign agreements and an open coupling standard with lander operators before building the depot"}
  - {sev: High, title: "Cryogenic transfer between separate vehicles is not yet flight-proven; large-scale tests are scheduled from 2027", fix: "Use results from Starship and LOXSAT tests; ground-test the full arm and coupling with LOX in a dusty vacuum chamber"}
  - {sev: High, title: "Lander plumes blast regolith onto the farm and arm", fix: "Place the farm behind berms at a distance set by M05 pad plume data; stow the arm under a cover during landings"}
  - {sev: High, title: "Dust in couplings causes leaks or stuck connectors", fix: "Dust-tolerant couplings with purge and covers; spare seals; inspect after each use"}
  - {sev: High, title: "LOX leak near organic materials or hot surfaces can start a fire", fix: "Oxygen-clean design; automatic shut-off; no crew at the pad during transfer"}
  - {sev: Medium, title: "Each lander may need a different coupling and flow rate", fix: "Publish one interface standard; adapters for early landers"}
  - {sev: Medium, title: "Liquefaction capacity lags plant output and gas has to be held or vented", fix: "Modular coolers added with each plant batch; gas accumulators as buffer"}
  - {sev: Medium, title: "Gauge errors cause billing disputes or underfilled landers", fix: "Two independent methods (RF gauge plus flow meter); calibrate on the Moon"}
sources:
  - {title: "NASA HLS IAC 2026 presentation (propellant transfer test schedule)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "Hines et al., NASA MSFC: Tank pressure control using zero boil-off active thermal control for LOXSAT", url: "https://ntrs.nasa.gov/citations/20220008696", date: "Jan 2023"}
  - {title: "Nugent et al., NASA: Space exploration applications for development of high capacity cryocoolers", url: "https://ntrs.nasa.gov/citations/20205010721", date: "Dec 2020"}
  - {title: "Plachta et al., NASA GRC: Cryogenic boil-off reduction system testing", url: "https://ntrs.nasa.gov/citations/20150000134", date: "Jul 2014"}
  - {title: "Townsend, Mueller and Tamasy, NASA KSC: Dust tolerant commodity transfer interface mechanisms for planetary surfaces", url: "https://ntrs.nasa.gov/citations/20150000177", date: "Oct 2014"}
  - {title: "Heersema et al., NASA Armstrong: Magnetically latching cryogenic fluid coupler for lunar surface operations", url: "https://ntrs.nasa.gov/citations/20230017745", date: "Jan 2024"}
  - {title: "NASA Glenn: NASA propellant tech could fuel long-duration missions (Radio Frequency Mass Gauge)", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-propellant-tech-could-fuel-long-duration-missions", date: "Mar 2025"}
  - {title: "Wikipedia: Liquid oxygen", url: "https://en.wikipedia.org/wiki/Liquid_oxygen", date: ""}
  - {title: "Wikipedia: Oxygen (heat of vaporization, heat capacity)", url: "https://en.wikipedia.org/wiki/Oxygen", date: ""}
  - {title: "Kleinhenz and Paz, NASA: Case study for lunar ISRU systems utilizing polar water (ASCEND 2020)", url: "https://ntrs.nasa.gov/api/citations/20205008303/downloads/AIAA_ASCEND2020_Kleinhenz_presentation_final.pdf", date: "Nov 2020"}
---

## What it does

M11 targets at least 300 t of oxygen a year and requires at least one lander to be refuelled on the surface. The depot sits between the plants and the pads. It liquefies oxygen, stores it with no boil-off, and pumps it into landers through an automated arm.

## How it works

**Storage farm.** Each tank is a scaled-up version of the C06.3 pilot tank. A cryocooler holds it at about 90 K. NASA Glenn has shown zero boil-off LOX storage with a 90 K cooler and full pressure control in a vacuum chamber<sup class="r">[4](#s4)</sup>. The LOXSAT flight demonstration targets zero boil-off LOX storage in orbit<sup class="r">[2](#s2)</sup>.

**Liquefaction scale-up.** NASA puts the need for in-situ oxygen liquefaction at about 150 W of 90 K cooling, and is developing scalable, high-capacity reverse turbo-Brayton coolers<sup class="r">[3](#s3)</sup>. The depot needs roughly 26 times that (see Sizing). This plan uses many identical units so one failure only cuts capacity a little.

**Transfer arm and couplings.** Regolith dust finer than 100 microns can jam mechanisms and damage seals and connectors. NASA KSC built and demonstrated an automated interface that joins cryogenic fluid, power and data connectors<sup class="r">[5](#s5)</sup>. NASA Armstrong has developed a magnetically latching cryogenic coupler for lunar surface use<sup class="r">[6](#s6)</sup>. The arm reaches the lander after it lands and is safed, connects, chills the line, fills, and withdraws.

**Quantity gauging.** NASA's Radio Frequency Mass Gauge was tested with liquid oxygen and methane in Intuitive Machines' IM-1 lander tanks<sup class="r">[7](#s7)</sup>. The depot pairs it with flow meters and load cells.

**Safety.** Organic materials burn rapidly in liquid oxygen, and some materials soaked in it can detonate from a spark or impact<sup class="r">[8](#s8)</sup>. The depot uses oxygen-clean parts, automatic shut-off, and runs transfers with no crew at the pad.

**Hydrogen (later).** If water is split for hydrogen, the NASA polar water study assumed an oxygen-to-hydrogen mixture ratio of 6<sup class="r">[10](#s10)</sup>. NASA estimates lunar hydrogen liquefaction needs about 300 W of cooling at 20 K<sup class="r">[3](#s3)</sup>. That is a later phase of this depot.

**Readiness of transfer.** NASA's 2026 schedule lists a Starship large-scale cryogenic propellant transfer test in the 2027 period<sup class="r">[1](#s1)</sup>. Lessons from it feed the coupling design.

## Sizing

This plan's arithmetic (ESTIMATE):

| Item | Working | Result |
|---|---|---|
| Output rate | 300,000 kg ÷ 8,766 h | 34.2 kg/h |
| Liquefaction heat per kg | 0.918 kJ/kg·K × 210 K + 213 kJ/kg<sup class="r">[9](#s9)</sup> | ~406 kJ/kg |
| Liquefaction load | 34.2 kg/h ÷ 3,600 × 406 kJ/kg | ~3.9 kW at 90 K (~26 × 150 W) |
| Tank volume | 25,000 kg ÷ 1.141 kg/L<sup class="r">[8](#s8)</sup> × 1.1 ullage | ~24 m³; sphere ~3.6 m, ~40 m² |
| Farm heat leak | 4 × 40 m² × 1 W/m² (assumed) + ~90 W pipes and struts | ~250 W at 90 K |
| Stored supply | 100 t ÷ 0.82 t/day | ~4 months of output |
| Transfer time | 50 t ÷ 1.141 kg/L = 43,800 L ÷ 200 L/min | ~3.7 h |

Design choices: 100 t of storage, a 50 t lander fill, and 200 L/min are this plan's assumptions. They should be reset when lander operators state their needs.

## Testing and qualification

1. Qualify one 25 t tank with cooler on the ground: 90 days of zero boil-off with a heated floor and sun lamp.
2. Test the arm and coupling with liquid nitrogen, then LOX, in a dusty vacuum chamber. Do at least 100 connect-disconnect cycles.
3. Calibrate the RF gauge and flow meter against weighed transfers.
4. On the Moon, install one tank and the arm first. Transfer LOX into a test tank on a dummy lander stand.
5. Refuel a real lander, at first with a small top-up, then a full fill.

## Open questions

- What propellant loads, flow rates and coupling locations will lander operators need?
- How far from the pads must the farm sit to be safe from plume debris?
- Is it better to store hydrogen, or store water and split it just before a fill?
- Can one industry-wide coupling standard be agreed?
- How should lunar oxygen be priced against oxygen shipped from Earth?
