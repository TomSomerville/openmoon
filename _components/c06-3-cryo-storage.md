---
id_code: "C06.3"
milestone: M06
order: 3
title: "Liquid oxygen and water storage"
summary: "Insulated, shaded tanks with grid-powered cryocoolers that liquefy the pilot plants' oxygen and keep it with no boil-off, plus heated tanks that keep water liquid. Storage lets the base bank its products for crew and landers."
trl: 5
spec:
  - {k: "LOX capacity", v: "5 t (design choice, about half a year of pilot output)"}
  - {k: "LOX tank", v: "One sphere, ~2.1 m diameter with 10% ullage (ESTIMATE)"}
  - {k: "Water capacity", v: "10 t in two 5 m³ tanks (design choice)"}
  - {k: "Storage temperature", v: "LOX at about 90 K; water kept above 273 K"}
  - {k: "Cooling", v: "~150 W at 90 K (liquefaction plus tank heat leak, ESTIMATE)"}
  - {k: "Cryocooler input power", v: "~2–4 kW (ESTIMATE)"}
  - {k: "Boil-off target", v: "Zero with cooler on; ~8 kg per day if cooler off (ESTIMATE)"}
  - {k: "Mass", v: "Part of the ~2 t tanks, liquefier and electrolyser delivery (M06 ESTIMATE)"}
subcomponents:
  - name: "Cryocoolers"
    desc: "Remove heat at 90 K to turn oxygen gas into liquid and to cancel heat leaking into the tank."
    parts: ["Reverse turbo-Brayton cooler units (2, one spare)", "Cold heat exchanger on tank wall", "Broad-area cooled shield", "Radiator for waste heat", "Drive electronics"]
    tech: "NASA GRC zero boil-off LOX test (2014); 90 K cryocooler development"
    trl: 5
  - name: "Tanks and insulation"
    desc: "Thin-wall aluminium tanks wrapped in multi-layer insulation, which works well only in vacuum, as on the Moon."
    parts: ["Aluminium LOX sphere", "Multi-layer insulation blanket (40+ layers)", "Low-conduction support struts", "Water tanks with heaters", "Pressure relief valves"]
    tech: "Spacecraft propellant tanks; MLI"
    trl: 6
  - name: "Shading and burial"
    desc: "Keeps sunlight and warm ground away from the cold tank."
    parts: ["Sun shade", "Regolith berm or burial", "Thermal standoffs from ground", "Shade deployment mechanism"]
    tech: "Design for the lunar polar thermal environment"
    trl: 4
  - name: "Boil-off management"
    desc: "Controls tank pressure and recovers any vapour so no oxygen is lost."
    parts: ["Pressure controller", "Vent-to-recovery line back to the liquefier", "Mixer or spray bar", "Emergency vent"]
    tech: "LOXSAT zero boil-off demonstration (planned)"
    trl: 5
  - name: "Transfer lines"
    desc: "Moves product from the plants to the tanks and from the tanks to users."
    parts: ["Vacuum-jacketed lines", "Cryogenic valves", "Dust-tolerant quick disconnects", "Chill-down bypass"]
    tech: "NASA KSC dust-tolerant cryogenic connectors"
    trl: 4
  - name: "Instrumentation"
    desc: "Measures how much product is stored and how fast any of it is lost."
    parts: ["Temperature sensors (silicon diodes)", "Pressure transducers", "Radio-frequency mass gauge", "Flow meters", "Heat-leak calorimetry by boil-off"]
    tech: "NASA Radio Frequency Mass Gauge (IM-1 tanks)"
    trl: 6
risks:
  - {sev: Critical, title: "Cryocooler failure lets LOX warm and vent", fix: "Two coolers with one spare; tank sized to ride through repair; vent recovery to the liquefier"}
  - {sev: High, title: "Zero boil-off of LOX has only been shown in a simulated-orbit vacuum chamber, not on a planetary surface", fix: "Ground test with a heated floor and sun simulator; measure heat leak on the Moon in the first month"}
  - {sev: High, title: "Heat leak from warm ground and sunlit surfaces (up to ~300 K on ridges) is higher than in orbit", fix: "Shade, standoffs and regolith berm; size coolers with 2× margin"}
  - {sev: High, title: "Power outages during lunar night stop cooling", fix: "Coolers on the priority M04 bus; the tank's thermal mass gives hours to days of ride-through"}
  - {sev: Medium, title: "Dust degrades insulation and radiators", fix: "Covered MLI outer layer; place radiators upwind of traffic; periodic inspection"}
  - {sev: Medium, title: "Water freezes and splits a tank after a heater fault", fix: "Redundant heaters; partially fill tanks; burial for thermal mass"}
  - {sev: Medium, title: "Liquid oxygen makes organic materials burn violently", fix: "Oxygen-clean parts only; no organics near tanks; keep-out zone"}
sources:
  - {title: "Plachta et al., NASA GRC: Cryogenic boil-off reduction system testing", url: "https://ntrs.nasa.gov/citations/20150000134", date: "Jul 2014"}
  - {title: "Nugent et al., NASA: Space exploration applications for development of high capacity cryocoolers", url: "https://ntrs.nasa.gov/citations/20205010721", date: "Dec 2020"}
  - {title: "Plachta et al., NASA: NASA cryocooler technology developments and goals to achieve zero boil-off and to liquefy cryogenic propellants", url: "https://ntrs.nasa.gov/citations/20180004710", date: "Jul 2017"}
  - {title: "Wikipedia: Liquid oxygen", url: "https://en.wikipedia.org/wiki/Liquid_oxygen", date: ""}
  - {title: "Wikipedia: Multi-layer insulation", url: "https://en.wikipedia.org/wiki/Multi-layer_insulation", date: ""}
  - {title: "Hines et al., NASA MSFC: Tank pressure control using zero boil-off active thermal control for LOXSAT", url: "https://ntrs.nasa.gov/citations/20220008696", date: "Jan 2023"}
  - {title: "Kleinhenz and Paz, NASA: Case study for lunar ISRU systems utilizing polar water (ASCEND 2020)", url: "https://ntrs.nasa.gov/api/citations/20205008303/downloads/AIAA_ASCEND2020_Kleinhenz_presentation_final.pdf", date: "Nov 2020"}
  - {title: "NASA Glenn: NASA propellant tech could fuel long-duration missions (Radio Frequency Mass Gauge)", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-propellant-tech-could-fuel-long-duration-missions", date: "Mar 2025"}
  - {title: "Townsend, Mueller and Tamasy, NASA KSC: Dust tolerant commodity transfer interface mechanisms for planetary surfaces", url: "https://ntrs.nasa.gov/citations/20150000177", date: "Oct 2014"}
  - {title: "Wikipedia: Oxygen (heat of vaporization)", url: "https://en.wikipedia.org/wiki/Oxygen", date: ""}
---

## What it does

The pilot plants make oxygen gas (C06.1) and water (C06.2). This component liquefies the oxygen and stores it, and keeps water liquid. M06 requires that products are stored for at least a month without loss, with boil-off measured.

Liquid oxygen boils at 90.19 K and has a density of 1.141 kg/L<sup class="r">[4](#s4)</sup>. Any heat that reaches it turns some to gas. The aim is zero boil-off: a cryocooler removes heat as fast as it leaks in.

## How it works

**Cryocoolers.** NASA Glenn tested a reverse turbo-Brayton cryocooler at 90 K, linked to a tank shield and tank wall under multi-layer insulation, in a vacuum chamber. It achieved zero boil-off of liquid oxygen with full tank pressure control<sup class="r">[1](#s1)</sup>. NASA is developing 90 K cryocoolers both to prevent boil-off and to liquefy oxygen made in place<sup class="r">[3](#s3)</sup>. It puts the need for in-situ oxygen liquefaction at about 150 W of cooling at 90 K<sup class="r">[2](#s2)</sup>.

**Tanks and insulation.** The NASA polar water study used thin-wall (3 mm) aluminium tanks<sup class="r">[7](#s7)</sup>. A typical MLI blanket has 40 or more layers and is about 20 mm thick. MLI needs vacuum to work well<sup class="r">[5](#s5)</sup>, which the Moon provides.

**Shading and burial.** Sunlit ridges near the pole range from about 100 K to 300 K in the NASA study's assumptions<sup class="r">[7](#s7)</sup>. A sun shade and a regolith berm keep the tank out of direct sun and away from warm ground.

**Boil-off management.** Pressure is held by the cooler. Any vented gas goes back to the liquefier, not to space. The LOXSAT flight demonstration has the same main goal: zero boil-off storage of liquid oxygen<sup class="r">[6](#s6)</sup>.

**Transfer lines.** Lines are vacuum-jacketed. Connectors must keep out dust finer than 100 microns, which can jam mechanisms and damage seals. NASA KSC has built dust-tolerant cryogenic connectors<sup class="r">[9](#s9)</sup>.

**Instrumentation.** NASA's Radio Frequency Mass Gauge estimates propellant quantity by matching a measured radio spectrum inside the tank against simulations. It was tested with liquid oxygen and methane in Intuitive Machines' IM-1 lander tanks<sup class="r">[8](#s8)</sup>.

## Sizing

This plan's arithmetic (ESTIMATE):

| Item | Working | Result |
|---|---|---|
| LOX volume | 5,000 kg ÷ 1.141 kg/L<sup class="r">[4](#s4)</sup> | 4.38 m³ (4.8 m³ with 10% ullage) |
| Sphere | diameter for 4.8 m³ | ~2.1 m; area ~13.8 m² |
| Tank heat leak | assume 1 W/m² through MLI plus ~6 W through struts and pipes | ~20 W |
| Boil-off if cooler off | 20 W ÷ 213 kJ/kg (6.82 kJ/mol ÷ 0.032 kg/mol)<sup class="r">[10](#s10)</sup> | ~8 kg/day (0.16% per day) |
| Liquefaction load | from C06.1 sizing | ~130 W |
| Total cooling | 20 W + 130 W | ~150 W at 90 K |
| Input power | assume 15–25 W input per W of cooling | ~2–4 kW |

The 1 W/m² heat leak and the cooler efficiency are assumptions. Measuring them is a goal of the pilot.

## Testing and qualification

1. Fill a full-size tank with liquid nitrogen, then liquid oxygen, in a vacuum chamber with a heated floor and sun lamp. Measure boil-off with the cooler off.
2. Switch the cooler on and hold zero boil-off for 30 days.
3. Run liquefaction and storage together with a gas supply matching C06.1 output.
4. Test cooler failure and recovery, and a simulated lunar night with reduced power.
5. On the Moon, measure heat leak in the first week, then hold LOX for at least a month with no loss.

## Open questions

- What is the real heat leak of MLI on a tank sitting on lunar regolith?
- Is burial better than a shaded, raised tank?
- Should water be stored as ice in a cold place instead of heated liquid?
- How should the cooler be sized when liquefaction and storage share one unit?
- How well does the radio-frequency gauge work in lunar gravity with a settled liquid?
