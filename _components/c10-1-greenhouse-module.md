---
id_code: "C10.1"
milestone: M10
order: 1
title: Buried greenhouse module
summary: "Pressurised modules under regolith, filled with stacked hydroponic racks under LED lights. Together they grow about half the crew's calories, take up CO₂ and give back oxygen and clean water. Lighting power is the main cost."
trl: 5
spec:
  - {k: "Target", v: "≥50% of calories for the 6-person design crew (M10, DD-006); handover peaks of 9 eat stored food"}
  - {k: "Growing area", v: "~196 m² canopy (ESTIMATE, half of BVAD's 65.3 m² per person × 6)"}
  - {k: "Modules", v: "3 modules × ~66 m² canopy, 3 rack tiers each (plan design choice; was 4 for 8 crew)"}
  - {k: "Lighting", v: "LEDs, ~2.5 µmol/J fixture efficacy (ESTIMATE from best tested fixtures)"}
  - {k: "Light per day", v: "17 (lettuce) to 115 (wheat) mol/m²/day; ~33 averaged over the crop mix"}
  - {k: "Average power", v: "~38 kW lighting, ~46 kW total (ESTIMATE)"}
  - {k: "Gas exchange", v: "~5.6 kg CO₂ taken up and ~4.1 kg O₂ released per day (ESTIMATE, scaled 6/8 from the 8-crew BVAD working)"}
  - {k: "Water transpired", v: "~0.9 t per day, condensed and reused (ESTIMATE)"}
  - {k: "Delivered mass", v: "~13–16 t for 3 modules (ESTIMATE)"}
  - {k: "Shielding", v: "≥2 m regolith cover, as C09.1"}
  - {k: "Power interface", v: "Each greenhouse module has its own service connection to the M04 grid (UMIC-class step-down to 120 V DC, meter, main breaker) and its own 120 V DC panel for lighting, pumps and fans (plan design, DD-009)"}
subcomponents:
  - name: Growth racks
    desc: "Stacked hydroponic trays, with aeroponic root chambers for potatoes, holding the crops at the right spacing."
    parts: ["Nutrient film trays for greens and wheat", "Aeroponic chambers for potatoes and sweet potatoes", "Three-tier rack frames", "Seed cassettes and transplant trays", "Removable root-zone covers"]
    tech: "NASA Biomass Production Chamber; Veggie; Advanced Plant Habitat"
    trl: 6
  - name: LED lighting
    desc: "Red, blue and white LED panels, water-cooled, switched on staggered schedules to smooth the power demand."
    parts: ["White + red LED panels", "Dimmable drivers", "Cold plates on the habitat water loop", "Photoperiod and dimming controller", "Spare panels"]
    tech: "Commercial horticultural LEDs; Veggie LED heritage"
    trl: 6
  - name: Atmosphere and climate
    desc: "A separate air loop keeps CO₂, humidity and temperature at plant settings, not crew settings."
    parts: ["CO₂ feed from the crew cabin air", "Condensing heat exchanger", "Circulation fans", "Ethylene and trace gas scrubber", "Gas isolation valves to the habitat"]
    tech: "BPC closed chamber; ISS condensing heat exchangers"
    trl: 5
  - name: Water and nutrient delivery
    desc: "Pumps circulate nutrient solution and add acid and stock solution as the plants use them up. Condensate from the air goes back to the water loop."
    parts: ["Nutrient reservoirs (one per module)", "Circulation pumps", "pH and conductivity dosing", "UV disinfection", "Condensate return to life support"]
    tech: "BPC nutrient delivery (BVAD data)"
    trl: 6
  - name: Waste processing
    desc: "Inedible plant mass is broken down so that its nutrients go back into the solution."
    parts: ["Shredder", "Stirred-tank bioreactor or composter", "Solids separator", "Nutrient recovery filter"]
    tech: "NASA KSC biomass bioreactor research; Lunar Palace 1"
    trl: 4
  - name: Shell and access
    desc: "A pressurised module with a central aisle, buried under regolith like the habitats."
    parts: ["Pressure shell (~4.5 m × 10 m)", "Central crew aisle", "Hatch to the habitat", "Regolith cover (C09.1)"]
    tech: "Habitat module heritage (M08)"
    trl: 5
risks:
  - {sev: High, title: "Lighting and plant systems need ~46 kW on average, more than two 20 kWe LR-1-class reactors give, so M10 keeps three (DD-002)", fix: "Phase crops by calories per kWh; greens first; grow power in step (M11); stagger photoperiods so peak power stays close to the average."}
  - {sev: High, title: "Disease or a system failure wipes out a module", fix: "Three isolated modules with separate air and water loops; seed bank; 12-month stored food reserve (M10)."}
  - {sev: High, title: "~46 kW of heat and ~0.9 t a day of transpired water must be removed", fix: "Size condensing heat exchangers and surface radiators for full load, because the regolith cover is a near-perfect insulator and passes well under 1% of it (C09.1); test in a ground chamber at full scale."}
  - {sev: Medium, title: "Delivered mass (~13–16 t) is an estimate with no hardware behind it", fix: "Consider inflatable shells; deliver in two phases; make racks locally once the fab shop works (C12.1)."}
  - {sev: Medium, title: "Raw lunar soil stunts plants", fix: "Use hydroponics; research treated regolith separately."}
  - {sev: Medium, title: "Effects of 1/6 g on crops over many generations are unknown", fix: "Start with ISS-proven crops; track yields per crop; keep shipped food until yields are proven."}
  - {sev: Medium, title: "Microbes on fresh produce make crew ill", fix: "Microbial testing before eating; sanitising wash; clean-handling rules."}
sources:
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): crop growth, lighting and growth chamber data", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "Kusuma, Pattison and Bugbee, Horticulture Research: From physics to fixtures to food, current and potential LED efficacy", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC7105460/", date: "Mar 2020"}
  - {title: "NASA: Science in space, plant science (Veggie)", url: "https://www.nasa.gov/missions/station/iss-research/science-in-space-week-of-july-10-2023-plant-science/", date: "Jul 2023"}
  - {title: "NASA: Houston, we have a pepper", url: "https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/", date: "2021"}
  - {title: "Lunar Palace 1 (Lunar Palace 365 mission), Wikipedia", url: "https://en.wikipedia.org/wiki/Lunar_Palace_1", date: "accessed Nov 2026"}
  - {title: "NASA: Scientists grow plants in lunar soil (Univ. of Florida, 2022)", url: "https://www.nasa.gov/?p=96327", date: "May 2022"}
---

## What it does

The greenhouse grows fresh food and staple crops for the crew. Plants also take up the crew's CO₂, release oxygen, and turn nutrient water into clean condensate. It is buried for the same radiation reasons as the habitat (C09.1). So all light has to come from electricity.

## How it works

**Crops.** The ISS has grown lettuces, Chinese cabbage, mizuna and kale in Veggie<sup class="r">[3](#s3)</sup>, and chile peppers in the Advanced Plant Habitat<sup class="r">[4](#s4)</sup>. These come first. Potatoes, wheat and soy follow for calories. NASA's BVAD lists the light, photoperiod and growth period for each candidate crop. For example, potatoes need **28 mol/m²/day**, soybeans **28**, lettuce **17** and wheat **115**<sup class="r">[1](#s1)</sup>.

**Growing medium.** Plants germinated in real Apollo soil but grew stunted<sup class="r">[6](#s6)</sup>. So the racks are hydroponic. BVAD's water and nutrient data come from NASA's hydroponic Biomass Production Chamber<sup class="r">[1](#s1)</sup>.

**Lighting.** The best independently tested fixtures reach about **2.78 µmol/J** (white + red) and **3.0 µmol/J** (blue + red). Protecting them from water and high humidity costs about **10%**<sup class="r">[2](#s2)</sup>. BVAD's nominal figure for how much light reaches the canopy is **0.8**<sup class="r">[1](#s1)</sup>.

**Atmosphere.** Plants grow best at **0.10–0.20 kPa** of CO₂ and about **75%** humidity. Wheat and potatoes prefer temperatures below crew comfort<sup class="r">[1](#s1)</sup>. That is why the greenhouse has its own air loop, fed with CO₂-rich cabin air. China's Lunar Palace 1 showed that plants and crew can also share one atmosphere<sup class="r">[1](#s1)</sup><sup class="r">[5](#s5)</sup>.

**Nutrients and waste.** Supplying all of a person's calories with crops needs about **90–100 kg of fertiliser salts per person per year**. More than **50%** of those nutrients could be recycled from inedible plant mass, using stirred-tank reactors or composting<sup class="r">[1](#s1)</sup>.

## Sizing (ESTIMATE)

BVAD gives a growing area of **65.29 m² per crew member** for a diet that uses all of its listed crops. Most of that area is soybean (46.4 m²)<sup class="r">[1](#s1)</sup>. This plan assumes that diet covers a full calorie need. So half of it, for the 6-person design crew (DD-006), is 0.5 × 6 × 65.29 ≈ **196 m²**. The base holds 9 people for about 2 weeks every 3 months, which raises the yearly average headcount to 6.5; those extra meals come from stored food.

| Step | Working |
|---|---|
| Light per day, area-weighted | Σ(area × light) ÷ Σ(area), using BVAD values for each crop<sup class="r">[1](#s1)</sup> = 2,184 ÷ 65.3 ≈ **33.5 mol/m²/day** |
| Light delivered per joule | 2.78 µmol/J × 0.9 (water protection)<sup class="r">[2](#s2)</sup> ≈ 2.5; × 0.8 delivery<sup class="r">[1](#s1)</sup> = **2.0 µmol/J** |
| Energy per m² | 33.5 mol ÷ 2.0 µmol/J = 16.7 MJ ≈ **4.65 kWh/m²/day** |
| Lighting, 196 m² | 196 × 4.65 ≈ 911 kWh/day ≈ **38 kW average** |
| Pumps, fans, dehumidifying | +20% (assumption) ≈ **46 kW average**, nearly all of it rejected as heat |
| Gas exchange | Using BVAD per-crop rates<sup class="r">[1](#s1)</sup>, scaled from the 8-crew working: ~5.6 kg CO₂ taken up and ~4.1 kg O₂ released per day |
| Water transpired | ~0.9 t/day, condensed and returned |
| Inedible biomass | 3 × 6.66 kg per crew-member-day<sup class="r">[1](#s1)</sup> ≈ **20 kg/day** (fresh) |
| Mass | ~33 kg/m² of growing hardware × 198 m² ≈ 6.5 t, plus 3 shells at 2–3 t each ≈ **13–16 t**. The hardware figure starts from BVAD's chamber values (shoot zone, mechanisation, structure)<sup class="r">[1](#s1)</sup>, with LEDs (~15 kg/m²) and trays (~5 kg/m²) assumed. |

For comparison, six people produce about 6 × 1.085 ≈ 6.5 kg of CO₂ a day<sup class="r">[1](#s1)</sup>. So the plants would take up most of it.

**Power is not resized.** ~46 kW is more than two 20 kWe reactors give, so M10 keeps the three LR-1-class units it already costs (DD-002), with ~14 kW of margin (this plan's arithmetic).

## Testing and qualification

1. Build one full-size module on Earth and grow each crop through a full cycle.
2. Measure yield, power, heat and water balance against the table above.
3. Run a 12-month closed test with crew-produced CO₂, as Lunar Palace 1 did<sup class="r">[5](#s5)</sup>.
4. On the Moon, start with a Veggie-class unit in the crewed base (M09). Then commission one module growing greens only, and add staples module by module.

## Open questions

- Does BVAD's all-crop diet area really supply full calories, and how does the crop mix change the power needed?
- Can staggered photoperiods hold peak power near the average?
- How do crops yield at 1/6 g over many generations?
- Is a shared crew–plant atmosphere simpler than a separate loop?
