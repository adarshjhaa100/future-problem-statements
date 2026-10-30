# Raw Context — deepseek-v4.1-flash — 2026-10-30T22:28:16+05:30

> Purpose: preserve the working context of this session so another model or human can resume without re-deriving the repository. This is a transcript + decision log, not a byte-for-byte token dump. Full file bodies live at the paths listed in the manifest.

- **Model:** `opencode-go/deepseek-v4.1-flash`
- **Session date/time:** 2026-10-30T22:28:16+05:30
- **Working directory:** `/home/tcsc/Documents/projects/future-problem-statements`
- **Repository:** git repo, branch `main`, remote `adarshjhaa100/future-problem-statements`
- **Platform:** Linux, bash, Node v22.23.2, Python 3
- **Final validation:** `OK: 144 problems across 12 domains; 144 summary rows; all required fields present.`

---

## 1. Operative system/developer context

The model was running as **opencode**, an interactive CLI coding agent. The key operating constraints were:

- Be concise and direct; minimize output tokens; use markdown; no unnecessary preamble or postamble.
- Use specialized tools for file reads, writes, edits, searches and shell commands.
- Prefer parallel tool calls when independent.
- When editing files, understand existing conventions; do not add comments unless asked.
- Never commit, amend, push, or create PRs unless explicitly requested.
- Do not proactively create documentation files unless explicitly requested.
- Never expose secrets or commit keys.
- Use `file_path:line_number` references when citing code.
- The environment is Linux; working directory is the repo root.
- The user asked for a full rebuild of a problem-statements repository, then a startup-ideas column, then this raw context dump.

The model was powered by `opencode-go/deepseek-v4.1-flash`. Available tools: bash, edit, glob, grep, question, read, skill, task, todowrite, webfetch, websearch, write.

No skills were loaded. No commits were made.

---

## 2. User messages (verbatim)

### User message 1

> Go over all the problem statements listed in the current dir, refine everything from scratch. Scan the whole internet or perform a deep research for 1. Importance of the problem statement in terms of Impact on people, duration of impact 2. Relative number of people working on it 3. Budget 4. People required to implement it ( should e 1-3 max and time span to potentially implement < 1yr ) etc. Try to search and recreate the whole set of list based on October 2026 across most important domains that humans and planet should focus on/ for some other open problems or figure out some pain points based on value addition: a. Gap for some problem b. Inconsistency in current mechanisms c. Feasibility. Dont stay limited to domains we have, go wild just keep the similar structure. Make sure to make the problem statement and proposed solution more detailed in fact. The solutions may or may not be using Software 100%, although software or AI might help. Keep using aristotle thinking and make sure that the problem statements are really unique and really less worked upon or whatevs. Also list down the comprehensive aggressive marketing strategy for each solution based on behavioral science to exactly make it work on minds of intended audience. Once done, Review properly on all sorts of aspects of the solution. Keep reviewing, updating and do it for 3 passes

### User message 2

> For each domain or problem statement added, add startup ideas column with upto 3 startup ideas. Check the feasibility ( 1-3 person work, < 1yr , achievable with some research and experiments )

### User message 3

> Write your whole raw context out in ai/contexts/<model-name>-<date-timens>.md

---

## 3. Assistant messages (verbatim / near-verbatim)

### After message 1, opening

> I'll start by examining the current directory structure and understanding the existing problem statements.

### After initial reads

> I'll research the October 2026 landscape across major domains, then rebuild the full set with richer economics, team/budget reality, and behavioral-science go-to-market for every problem.

### After research

> I'll add a `Startup ideas` column to every problem row (2–3 ideas each), with an explicit feasibility tag for team size, time, and the first experiment. Then I’ll update the summary and site parser.

### Final summary after message 1

> Rebuilt the repository from scratch as **144 problems across 12 domains** for October 2026; the old 166-problem edition is archived in `archive/2025-v1/`.
>
> Every row now includes: reach × duration impact, relative crowd density, pilot budget, 1–3 person team + under-12-month path, detailed solution, first-version test, Aristotelian first-principles derivation, kill criteria, and a behavioural-science GTM plan.
>
> Added `docs/research-base-2026.md`, `docs/methodology.md`, `docs/behavioral-playbook.md`, `docs/gtm-sequences.md`, and `docs/reviews.md` documenting all three review passes. Rebuilt `README.md`, `summary-all.md`, and `index.html`.
>
> Validation passes: `python3 scripts/validate.py` → 144/144 rows, 12 domains, all required fields, 144 summary rows.

### Final summary after message 2

> Added a `Startup ideas` column to all **144 problem statements** — **432 ideas** total, 3 per row.
>
> Each idea includes a feasibility tag: `fit: team size, months, first experiment` — all checked to be **1–3 people, under 12 months, research/experiment-driven**. Examples: HeatScore, TransformerCanary, AflaCheck, AgentAudit, RespiteNow.
>
> Updated `summary-all.md`, `index.html` parser/drawer/search/snapshot, `README.md`, `docs/methodology.md`, and `docs/reviews.md`. Validation passes: 144 rows, 12 domains, 432 startup ideas, all required fields present.

---

## 4. Initial repository state (before the rebuild)

The repo originally had:

- `README.md` — 166 problems across 9 domains
- `summary-all.md` — 166-row summary
- `energy-transition.md` (20 problems)
- `electronics-software.md` (20)
- `biotech-health-longevity.md` (20)
- `defence-space-advanced-manufacturing.md` (20)
- `agri-water-urbanisation.md` (20)
- `creative-taste-economy.md` (20)
- `high-trust-services_law_mental_health_osint.md` (20)
- `education-community-innovation.md` (14)
- `financial-inclusion-informal-economy.md` (12)
- `docs/replacement-logs.md`
- `index.html` — single-file GitHub Pages explorer, parsing raw markdown from GitHub into tables

The existing files had a wide table schema and some duplication/broken rows. The old edition was archived, not deleted.

---

## 5. Research performed (October 2026)

Web searches were run for the 2026 risk landscape, health, food/water, climate/energy, AI, care, education, finance, local news, and related topics. The extracted facts used in the repository:

### Global risk picture

- WEF *Global Risks Report 2026*: geoeconomic confrontation is the top risk likely to trigger a material crisis in 2026; state-based armed conflict second; misinformation/disinformation, societal polarisation and extreme weather in the top five; environmental risks dominate the 10-year outlook; 57% expect a turbulent/stormy decade; adverse AI outcomes among the fastest-rising long-term risks.

### Health

- WHO: bacterial AMR associated with **4.7 million deaths in 2021**; **1.14 million directly attributable**; about **1 in 6 lab-confirmed bacterial infections resistant in 2023**; Lancet/GBD forecast **39 million AMR-attributable deaths 2025–2050**.
- WHO *World Health Statistics 2026*: **6.6 million deaths in 2021** from household + ambient air pollution; **1.18 million road deaths in 2021**.
- WHO mental health: **1 billion+** people with a mental health condition; only **9% of major depression gets minimally adequate treatment**; **2%** in sub-Saharan Africa; depression/anxiety cost about **US$1 trillion/year**; **727,000 suicides in 2021**.
- WHO obesity (Oct 2026): **1.1 billion people with obesity**; adult obesity doubled 1990–2024; **400 million children/adolescents overweight**.
- IDF Diabetes Atlas 11th edition (2026): **853 million adults with diabetes by 2050**.
- Alzheimer's Association 2026: **7 million Americans with Alzheimer's**, **12 million unpaid caregivers**, **US$409 billion** US dementia cost in 2026; global cases nearly triple by 2050.
- RAND: **100 million+ US adults** provide unpaid care to an adult relative/friend.
- Microplastics 2026 reviews: detectable in blood, placenta, lung and other tissues; causal clinical disease link unproven; public concern ahead of evidence.

### Food, water, land, nature

- SOFI 2026: **7.8% undernourished in 2025**; **2.1 billion** moderate/severe food insecurity; two-thirds of people in Africa cannot afford a healthy diet.
- 2026 Global Report on Food Crises: acute hunger doubled over the decade; two famines declared in the previous year; WFP 2026: **318 million** acutely food insecure in countries where it operates.
- FAO/UNEP: **13.2% of food lost** after harvest before retail; **19% wasted** at retail/food service/household; **8–10% of global GHG emissions**.
- FAO *Status of the World's Soil Resources 2026*: **58% of regional assessments deteriorating since 2015**; only ~10% improving; **40% of global land degraded**, affecting **3.2 billion people**; US$7–30 return per US$1 restoration.
- WWF *Living Planet Report 2026*: **73% average decline** in monitored vertebrate populations 1970–2022; freshwater **-85%**, terrestrial **-69%**, marine **-59%**; 35,803 populations, 5,790 species.

### Energy, materials, AI build-out

- IRENA 2026: **5,149 GW** renewable capacity end-2025; solar+wind **96.8% of net additions**; renewables **33.8% of global electricity in 2025**, overtaking coal.
- IEA: data centres **415 TWh in 2024 (1.5%)**, ~**945 TWh by 2030**; UN University 2026: **448 TWh in 2025**; AI ~20% today, ~40% by 2030; water and carbon footprints comparable to a mid-sized country.
- IEA *Global Critical Minerals Outlook 2026*: export controls turned concentration into immediate security risk; China dominates rare-earth refining and much gallium/germanium/graphite/battery material; up to **US$6.5 trillion/year** downstream production at risk from full rare-earth controls; **US$300 billion/year** from graphite disruption.
- Counter-UAS market ~**US$14.4 billion in 2026**, ~22% CAGR; CBO: **US$74 million** to equip one installation with layered counter-small-UAS defence, **US$5 million/year** sustainment.

### Money, work, information

- India: **63 million MSMEs**; only ~**14% have formal credit** (Deloitte 2026); MSME credit gap **₹25–30 lakh crore** (~US$300–360 billion); ~**8 in 10 workers informal**.
- Agentic AI 2026: most large enterprises run at least one agent workflow; **23%** of organisations reported agents tricked into revealing credentials (SailPoint 2026); cost overruns common.
- Deepfake fraud: ~**US$3.7 billion** documented losses by mid-2026; estimates of **US$40 billion/year** synthetic-media-enabled fraud; voice/video ~two-thirds of observed synthetic fraud.
- UNESCO GEM 2026: **273 million children/youth out of school**, seventh consecutive annual increase; one in six school-age children excluded; two in three complete secondary.
- Pew 2026 local news: only **34%** say local news extremely/very important, down from 44% a year earlier; local news decline linked to lower civic engagement and accountability.

### Source links (selected)

- WEF Global Risks 2026: https://www.weforum.org/publications/global-risks-report-2026/
- WHO AMR: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- WHO depression: https://www.who.int/news-room/fact-sheets/detail/depression
- WHO obesity: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight
- WHO mental health: https://www.who.int/news/item/02-09-2025-over-a-billion-people-living-with-mental-health-conditions-services-require-urgent-scale-up
- UNESCO GEM 2026: https://www.unesco.org/gem-report/en/2026
- FAO SOFI 2026: https://www.fao.org/publications/fao-flagship-publications/the-state-of-food-security-and-nutrition-in-the-world/en
- FAO soil 2026: https://www.fao.org/newsroom/detail/fao-at-cop17--new-report-warns-soil-degradation-worsening-as-adoption-of-proven-solutions-lags
- WWF LPR 2026: https://www.worldwildlife.org/publications/2026-living-planet-report/
- IRENA 2026: https://www.irena.org/Publications/2026/Mar/Renewable-capacity-statistics-2026
- IEA Energy and AI: https://www.iea.org/reports/energy-and-ai
- IEA critical minerals 2026: https://www.iea.org/reports/global-critical-minerals-outlook-2026
- CBO counter-UAS: https://www.cbo.gov/publication/62262
- Deloitte MSME coverage: https://www.tribuneindia.com/news/credit-gap/only-14-of-indias-msmes-have-access-to-formal-credit-despite-digital-finance-boom-deloitte-report
- RBI Annual Report 2025–26: https://rbi.org.in/Scripts/AnnualReportPublications.aspx?Id=1464
- IDF Diabetes Atlas: https://www.thelancet.com/journals/landia/article/PIIS2213-8587(25)00299-2/fulltext
- Alzheimer's 2026: https://www.alz.org/alzheimers-dementia/facts-figures
- RAND caregiving: https://www.rand.org/pubs/research_reports/RRA3212-2.html
- Pew local news: https://www.pewresearch.org/journalism/fact-sheet/local-news-fact-sheet/
- Deepfake fraud: https://www.brside.com/blog/deepfake-fraud-losses-2026
- SailPoint agent security: https://www.sailpoint.com/press-releases/sailpoint-ai-agent-adoption-report
- UNEP food waste: https://www.unep.org/resources/publication/food-waste-index-report-2024
- WHO road deaths: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/estimated-road-traffic-death-rate-(per-100-000-population)
- Microplastics review: https://pubmed.ncbi.nlm.nih.gov/41761215
- World Bank India MSME: https://www.worldbank.org/en/news/feature/2026/10/11/from-credit-gaps-to-growth-how-india-s-small-and-medium-firms-benefit-from-private-investment

---

## 6. Rebuild decisions

### New domain set (12 domains × 12 problems = 144)

1. **Planetary Health & Climate Adaptation** — `planetary-health-climate.md`
2. **Energy, Grid & Critical Materials** — `energy-grid-materials.md`
3. **Food, Water & Land Systems** — `food-water-land.md`
4. **Health, Biosecurity & Longevity** — `health-biosecurity-longevity.md`
5. **AI Safety, Digital Trust & Information Integrity** — `ai-trust-information.md`
6. **Care Economy, Mental Health & Human Development** — `care-mental-health-development.md`
7. **Education, Skills & Future of Work** — `education-skills-work.md`
8. **Financial Inclusion & the Real Economy** — `financial-inclusion-real-economy.md`
9. **Cities, Mobility & Housing** — `cities-mobility-housing.md`
10. **Industry, Semiconductors, Space & Defence** — `industry-space-defence.md`
11. **Governance, Justice & Civic Infrastructure** — `governance-justice-civic.md`
12. **Creative, Cultural & Attention Economy** — `creative-attention-economy.md`

The old 9-domain, 166-problem set was moved to `archive/2025-v1/`.

### Table schema (14 columns)

`# | Problem | Type | Why unsolved | Crowd | Impact | Budget | Team & time | Proposed solution | First version | First principles | Validation | Marketing | Startup ideas`

- Impact = reach × duration.
- Crowd = SATURATED / CROWDED / THIN / NEAR-ZERO, with examples.
- Budget = first-version pilot in ₹ and US$ (≈₹85/US$1).
- Team & time = 1–3 people, 4–11 months.
- First principles = M/F/E/Telos (material, formal, efficient, final cause) + feasibility.
- Validation = evidence + competitive check + kill criterion.
- Marketing = audience, hook, behavioural levers, channel, first 100, loop, ethics.
- Startup ideas = 3 concepts, each with `fit: team size, months, first experiment`.

### Methodology

- Six filters: importance, neglectedness, feasibility, budget, who pays, falsifiability.
- Aristotle: material, formal, efficient, final cause; potentiality → actuality.
- "Thin" does not automatically mean good; thin can mean impossible.
- No row should require a new molecule, law or standard before the first version.
- Every row has a kill criterion.
- No "awareness" as a business model.
- No surveillance disguised as care; no fake scarcity; no exploitation of grief/fear/community trust.

### Review passes

Documented in `docs/reviews.md`:

- **Pass 1 — importance/evidence/neglectedness:** removed already-solved rows; added duration; replaced generic crop-disease AI, mental-health chatbot, solar marketplace, legal chatbot, smart-city dashboard; added care/governance/planetary domains; fixed stale sources.
- **Pass 2 — feasibility/adoption/GTM:** reduced teams to 1–3; clarified 3-month first version vs 4–11-month implementation; added budgets; replaced "awareness" campaigns with behavioural diagnosis; added trusted messengers, WhatsApp/IVR, ethics guardrails, regulatory dependencies; added kill criteria; changed 12-month horizons to 11 months; fixed tree-survival pilot to 9 months with warranty tracked separately.
- **Pass 3 — uniqueness/coherence/Aristotle:** removed generic "AI on data" phrasing; made first-principles cells causal; audited ethical risk; checked cross-domain duplication; balanced software/hardware/process; replaced a crowded civic-tech row (public-comment analysis) with **Municipal Contract Change-Order Leak Detector**.
- **Post-review addition — startup ideas:** 432 concepts (3 per row), each `fit:` scoped to 1–3 people, under 12 months, named experiment/payer. Renamed duplicate names (`CoolRent` → `CoolLease`/`EfficientRent`, `AgentRisk` → `AgentExposure`/`AgentUnderwrite`). Added `scripts/build_summary.py` and extended `scripts/validate.py`.

---

## 7. Tool/action log (chronological, condensed)

- Inspected repo: `ls`, `find`, `wc -l`, read `README.md`, `summary-all.md`, `energy-transition.md`, `docs/replacement-logs.md`.
- Inspected `index.html` structure: DOMAINS, SNAPSHOT, NORM parser, drawer fields, mdOf exporter, ticker, hardcoded 166/9.
- Ran web searches on: WEF 2026 risks; UNESCO learning poverty; AMR; food/water; AI agents; mental health; climate/energy; caregiving; misinformation/deepfakes; biodiversity; microplastics; semiconductor/critical minerals; counter-UAS; MSME credit; data-centre energy; air/road deaths; diabetes/obesity; soil/food waste; local news; and related topics.
- Wrote `docs/research-base-2026.md`.
- Wrote `docs/methodology.md`.
- Wrote `docs/behavioral-playbook.md`.
- Wrote 12 domain files with 12 problems each.
- Moved old domain files and old replacement log to `archive/2025-v1/`.
- Rewrote `README.md`.
- Generated `summary-all.md` from domain tables with a Python script.
- Replaced `index.html` DOMAINS array with 12 new domains, HUES with 12 colours, SNAPSHOT with a 3-row slice of the planetary domain, NORM mappings for `crowd`, `budget`, `team`, `gtm`, `startupideas`; added drawer fields and mdOf lines; updated search; updated counts/copy.
- Added `scripts/validate.py`; later `scripts/build_summary.py`.
- Added `docs/gtm-sequences.md` and `docs/reviews.md`.
- Added startup ideas to every row via `/tmp/opencode/append_ideas.py` (12 batches).
- Fixed duplicate startup names.
- Fixed a broken snapshot template literal after appending startup ideas (closing backtick placed before the last idea cell; corrected).
- Ran validation repeatedly: 144 problems / 12 domains / 144 summary rows / all fields present.
- Ran Node syntax check on extracted `index.html` script and a Node parser test: all 12 files parse with 12 rows and all fields including `startupIdeas`.

Commands/results of note:

```text
python3 scripts/validate.py
OK: 144 problems across 12 domains; 144 summary rows; all required fields present.

node --check /tmp/opencode/index-script.js
# no output = syntax OK

Node parser test:
planetary-health-climate.md 12 OK
energy-grid-materials.md 12 OK
food-water-land.md 12 OK
health-biosecurity-longevity.md 12 OK
ai-trust-information.md 12 OK
care-mental-health-development.md 12 OK
education-skills-work.md 12 OK
financial-inclusion-real-economy.md 12 OK
cities-mobility-housing.md 12 OK
industry-space-defence.md 12 OK
governance-justice-civic.md 12 OK
creative-attention-economy.md 12 OK
total 144
```

---

## 8. Final repository state

### File manifest

Root:

- `README.md` — 249 lines
- `summary-all.md` — 169 lines, 144 problem rows + 9 columns including startup ideas
- `planetary-health-climate.md` — 64 lines, 12 problems
- `energy-grid-materials.md` — 64 lines, 12 problems
- `food-water-land.md` — 63 lines, 12 problems
- `health-biosecurity-longevity.md` — 63 lines, 12 problems
- `ai-trust-information.md` — 62 lines, 12 problems
- `care-mental-health-development.md` — 62 lines, 12 problems
- `education-skills-work.md` — 62 lines, 12 problems
- `financial-inclusion-real-economy.md` — 61 lines, 12 problems
- `cities-mobility-housing.md` — 62 lines, 12 problems
- `industry-space-defence.md` — 63 lines, 12 problems
- `governance-justice-civic.md` — 61 lines, 12 problems
- `creative-attention-economy.md` — 61 lines, 12 problems
- `index.html` — single-file explorer, updated for 144/12, new fields, new snapshot
- `scripts/validate.py` — 113 lines
- `scripts/build_summary.py` — 82 lines

Docs:

- `docs/research-base-2026.md` — 96 lines
- `docs/methodology.md` — 122 lines
- `docs/behavioral-playbook.md` — 136 lines
- `docs/gtm-sequences.md` — 138 lines
- `docs/reviews.md` — 164 lines

Archive:

- `archive/2025-v1/agri-water-urbanisation.md`
- `archive/2025-v1/biotech-health-longevity.md`
- `archive/2025-v1/creative-taste-economy.md`
- `archive/2025-v1/defence-space-advanced-manufacturing.md`
- `archive/2025-v1/education-community-innovation.md`
- `archive/2025-v1/electronics-software.md`
- `archive/2025-v1/energy-transition.md`
- `archive/2025-v1/financial-inclusion-informal-economy.md`
- `archive/2025-v1/high-trust-services_law_mental_health_osint.md`
- `archive/2025-v1/replacement-logs.md`

New context:

- `ai/contexts/deepseek-v4.1-flash-20261030-222816.md` (this file)

### Counts

- Problems: **144**
- Domains: **12**
- Problems per domain: **12**
- Startup ideas: **432** (3 per row)
- Summary rows: **144**
- Team sizes: all 1–3 people
- Implementation horizons: all 4–11 months
- Startup fit tags: all 1–3 people, <12 months
- Kill criteria: 144
- Marketing plans: 144
- Rows with `M:`, `F:`, `E:`, `Telos`: 144
- Rows with `US$` budget: 144
- Rows with `Crowd` label: 144
- Rows with `fit:` (3 each): 432

### Git status at context-write time

Modified: `README.md`, `index.html`, `summary-all.md`. Old files renamed to `archive/2025-v1/`. New domain files, docs, scripts and new context directory untracked. No commit made.

---

## 9. Problem titles by domain

### Planetary Health & Climate

1. Heat-Safe Rental Housing Score + Passive Cooling Kit
2. Tree Survival Warranty + Steward Network
3. Flood Mould Prevention Kit + Drying Library
4. Wildfire-Smoke Clean-Air Refuge Network
5. Biodiversity Net-Gain Protocol for Small Builders
6. Roadkill Hotspot Mapper + Culvert Retrofit Playbook
7. Saltwater Intrusion Early Warning for Small Farms
8. Nurdle and Microplastic Capture at Industrial Drains
9. Cooling-Centre Activation + Trusted Transport Protocol
10. Disaster Debris Reuse Exchange
11. Parametric Heat Insurance for Outdoor Workers
12. Night-Time Urban Heat Mapping on Public Buses

### Energy, Grid & Critical Materials

1. Distribution Transformer Canary
2. Rooftop Solar Grid-Support Retrofit
3. Data-Centre Compute Curtailment-as-a-Service
4. Data-Centre Waste Heat to Cold Storage
5. Motor Rewinding Efficiency Protocol
6. Low-Voltage Feeder Phase-Balancing Kit
7. Critical-Mineral Recovery from E-Waste Smelter Dust
8. Magnet-to-Magnet Rare-Earth Recycling
9. Transformer Oil Lab-on-Chip
10. Community Solar Subscription Escrow for Renters
11. LPG/PNG Auto-Shutoff + Rebooking Stack
12. City-Gas Methane Leak Detection on E-Bikes

### Food, Water & Land

1. Aflatoxin Rapid Test at Milk and Maize Collection
2. Post-Harvest Loss Proof-of-Loss for Insurance
3. Rural Piped-Water Leak Detection
4. Treated Wastewater Reuse Safety Kit
5. Managed Aquifer Recharge Verification
6. Aquaculture eDNA Disease Early Warning
7. Smallholder Dairy Mastitis Pen-Side Test
8. Farm Equipment Sharing Trust Protocol
9. Land Boundary Drone Mapping + Dispute Mediation
10. Fishers' Last-10-km Cold Chain
11. Dairy Cattle Heat-Stress Controller
12. Event Food-Waste Redistribution Logistics

### Health, Biosecurity & Longevity

1. Antibiotic Stewardship Peer-Comparison Audit for Small Clinics
2. Post-Surgical Wound Infection Photo Surveillance
3. Snakebite Species ID + Antivenom Cold Chain
4. Maternal Blood-Loss Scale + Checklist
5. Dental Caries Prevention via SDF Community Protocol
6. Diabetic Foot Ulcer Negative-Pressure Kit
7. PHC Drug Stockout Predictor + Redistribution
8. Hepatitis B Birth-Dose First-Hour Kit
9. Long-COVID Rehab Protocol + Remote Monitoring
10. Menopause Care Navigator
11. Hospital Hand-Hygiene Nudge System
12. Blood Culture Contamination Reduction Kit

### AI Safety, Digital Trust & Information Integrity

1. SMB Agent Least-Privilege Auditor
2. Browser-Agent Prompt-Injection Firewall
3. Family Voice-Scam Verification Code
4. Provenance Label for Local News
5. AI Incident Data for Insurance Underwriting
6. Agent Payment Mandate Verifier
7. AI Vendor Registry for SMEs
8. Fine-Tune Data Poisoning Detector
9. Teen AI Companion Safety Audit
10. Digital Legacy / Data Executor
11. Elder-Safe UPI Confirmation
12. Court Evidence Authenticity Kit

### Care Economy, Mental Health & Human Development

1. Dementia Caregiver Micro-Respite
2. Caregiver Medication Reconciliation
3. Social Prescribing for Loneliness
4. School Self-Harm Escalation Protocol
5. Men's Mental Health & Fatherhood
6. Wheelchair Repair Network
7. Home-Care Worker Micro-Credential
8. Grief Support After Suicide or Overdose
9. Childcare Quality Micro-Audit
10. Foster-Care Transition Navigator
11. Caregiver Financial Navigation
12. Task-Shifting Supervision for Community Mental Health

### Education, Skills & Future of Work

1. Informal-Trade Apprenticeship Matching
2. Gig-Worker Micro-Credential Verification
3. School Infrastructure Repair Prioritisation
4. Returnship for Women Re-Entering Work
5. Vocational English for Blue-Collar Workers
6. AI-Era Proof-of-Human-Skill Portfolio
7. Teacher Retention Early Warning
8. MSME Digital Apprenticeship
9. Recognition of Prior Learning for Informal Workers
10. School Transport Safety
11. Learning-Disability Screening for Low-Resource Schools
12. Alumni Sponsorship Network for First-Gen Students

### Financial Inclusion & the Real Economy

1. Rent-to-Own Equipment Financing for Informal Workers
2. Trade-Credit Insurance for Small Suppliers
3. Savings Commitment Device for Informal Workers
4. Debt-Trap Early Warning & Consolidation
5. Delayed-Payment Enforcement for Nano-MSMEs
6. Cooperative Procurement for Micro-Retailers
7. Digital Collateral Registry for Movable Assets
8. Credit Repair for Thin-File Borrowers
9. Funeral Insurance with Honest Claims
10. Livestock Insurance with RFID
11. Warehouse Receipt Financing for Small Farmers
12. Nano Invoice Discounting

### Cities, Mobility & Housing

1. Vacant Housing Activation & Rent Guarantee
2. Street-Vending Space Allocation
3. Bus-Stop Shade & Access Audit
4. Road-Crash Black-Spot Rapid Retrofit
5. School-Zone Safety Audit
6. Night-Shift Worker Transport Safety
7. Eviction Prevention Early Warning
8. Construction Heat-Safety Protocol
9. Waste-Picker Route Integration
10. Urban Freight Loading-Bay Booking
11. Accessible Sidewalk Audit
12. Tenant Energy-Efficiency Split-Incentive Fix

### Industry, Semiconductors, Space & Defence

1. Drone Component Authenticity
2. Ammunition Lifecycle Monitoring
3. Defence Procurement Compliance Automation
4. Additive Manufacturing Powder Reuse
5. Industrial Robot Safety Retrofit
6. Semiconductor Test Fixture
7. Chip Packaging Thermal Interface
8. Space Weather Alert for Grid & Aviation
9. Radiation-Hardened RISC-V
10. Counterfeit Electronic Component Detection
11. Soldier Heat and Hydration Wearable
12. Small-Unit Tactical Power Management

### Governance, Justice & Civic Infrastructure

1. Local News Micro-Donation
2. Municipal Meeting Transparency
3. Prison Family Connection
4. Restorative Justice for Petty Crime
5. Legal Aid Matching
6. Court Interpreter Scheduling
7. Municipal Contract Change-Order Leak Detector
8. FOI Request Assistant
9. Police Complaint Tracking
10. Missing Persons Case Management
11. Disaster Relief Eligibility Navigator
12. Court Evidence Organizer for Self-Represented Litigants

### Creative, Cultural & Attention Economy

1. Consent-Based Voice Corpus + Licensing
2. Esports Integrity Analytics
3. Indian Sound Library
4. Craft-Cluster Provenance & E-Commerce
5. Local Film Archive Restoration
6. Fan-Translation Rights Marketplace
7. Creator Contract Transparency
8. Comedy Joke Plagiarism Detection
9. Cultural Misappropriation Check
10. Live-Venue Acoustic Mapping
11. Heritage Digitisation
12. Blender Plugin Pack for Indian Animation

---

## 10. Startup-idea layer

Each row ends with 3 ideas. The format is:

`1) Name — model; fit: N people, M months, first experiment. 2) ... 3) ...`

Examples:

- **Heat-Safe Rental Housing:** HeatScore (landlord/insurer heat-score SaaS), CoolLease (tenancy-safe kit + installation), HeatSafe API (building heat-risk data).
- **Transformer Canary:** TransformerCanary (clamp-on sensor + edge ML), GridPulse (utility asset-health dashboard), FailSafe (insurance-backed monitoring).
- **Aflatoxin:** AflaCheck (rapid test + reader), SafeMilk (buyer compliance service), ToxinRisk (feed/maize risk data).
- **Antibiotic stewardship:** RxPeer (clinic benchmark SaaS), StewardMD (stewardship service), RxRisk (insurer risk score).
- **SMB agent security:** AgentAudit (least-privilege scanner), ScopeGuard (MSP service), AgentExposure (insurer exposure score).
- **Dementia care:** RespiteNow (micro-respite marketplace), CareBreak (employer benefit), SafeSit (vetted sitter network).
- **Informal apprenticeships:** TradeMatch (matching), SkillBridge (paid trial + credential), MasterList (verified master directory).
- **Rent-to-own:** AssetRent (rent-to-own), ToolOwn (dealer financing), IncomeAsset (asset-backed micro-lease).
- **Black-spot retrofit:** CrashFix (rapid retrofit), SafeJunction (crash data + design), RoadRisk (junction-risk analytics).
- **Counterfeit components:** PartProof (screening), ChipTrace (provenance database), SupplyGuard (distributor risk score).
- **Change-order detector:** ContractLeak (analytics), TenderTrace (procurement anomalies), PublicLedger (transparency dashboard).
- **Voice licensing:** VoiceTrust (consent-based licensing), VoiceBank (corpus marketplace), ConsentLayer (consent/audit API).

Full 432 ideas are in the domain files and `summary-all.md`.

---

## 11. Key file contents / conventions to preserve

- Markdown tables use `|` separators; no `|` inside cells. `<br>` is converted to spaces by the site parser.
- The parser normalises headers by lowercasing and removing whitespace, then maps via `NORM`. New columns must be added to `NORM`, `parseDomain` object, `FIELDS`, and `mdOf`.
- `index.html` fetches raw markdown from `https://raw.githubusercontent.com/adarshjhaa100/future-problem-statements/main/<file>`; offline fallback uses `SNAPSHOT`.
- `SNAPSHOT` is a JS template literal; its closing backtick must stay after the last table row. Adding a column required moving the closing backtick so the last startup-idea cell is inside the string.
- `summary-all.md` is generated by `scripts/build_summary.py`; do not hand-edit it after regenerating.
- `scripts/validate.py` checks 12 rows/domain, required columns (including `startup ideas`), duplicate titles, summary row count, README count, and index DOMAINS file references.
- Old edition archived, not deleted. Do not re-add old domains to index without a deliberate archive policy.

---

## 12. How to continue

1. Run `python3 scripts/validate.py` first.
2. If editing a row, keep 14 cells and 3 `fit:` tags.
3. If adding a domain, add it to `scripts/build_summary.py`, `scripts/validate.py`, and `index.html` `DOMAINS`.
4. If changing a table schema, update `NORM`, `parseDomain`, `FIELDS`, `mdOf`, and the SNAPSHOT table.
5. Regenerate summary: `python3 scripts/build_summary.py`.
6. Re-check browser script syntax by extracting the last `<script>` block and running `node --check`.
7. Do not commit unless the user asks.

### Known caveats

- Figures are rounded and some are projections; the research base labels them.
- Crowd labels are relative density estimates, not a census.
- Budgets are planning ranges; certification/field logistics can double them.
- Startup `fit:` tags are planning estimates, not validated schedules.
- Some rows depend on a partner who may say no (utility, insurer, hospital, court, defence programme).
- The context file does not duplicate the full bodies of the 12 domain files; read those paths for exact rows.
