# Problem Statements Repository — 166 Buildable Problems Across 9 Domains

A hand-built collection of problem statements that an engineer — or in a couple of domains, a community — can take from zero to a working first version in about three months. Each problem carries its competitive-landscape check, an economic or human "why", and honest caveats about what could kill it.

This is a living document. Problems that turned out to be already well-solved were replaced, and new domains were added as the gaps became obvious. The latest additions are in **Domain 8 (Education)** and **Domain 9 (Financial Inclusion)** — see the notes at the bottom.

---

## Repository Structure

| File | Description |
|------|-------------|
| [`summary-all.md`](./summary-all.md) | Consolidated tabular view of every problem with cross-domain validation |
| [`energy-transition.md`](./energy-transition.md) | Problems 1–20: LPG safety, solar, grid, EV, demand response, carbon markets |
| [`electronics-software.md`](./electronics-software.md) | Problems 1–20: RISC-V, embedded systems, TinyML, FOTA, test & measurement |
| [`biotech-health-longevity.md`](./biotech-health-longevity.md) | Problems 1–20: Diagnostics, genomics, women's & child health, mental health, preventive care |
| [`defence-space-advanced-manufacturing.md`](./defence-space-advanced-manufacturing.md) | Problems 1–20: Drones, GNSS resilience, SDR, CNC, wargaming, space |
| [`agri-water-urbanisation.md`](./agri-water-urbanisation.md) | Problems 1–20: Soil health, onion storage, water, counterfeit inputs, waste mgmt |
| [`creative-taste-economy.md`](./creative-taste-economy.md) | Problems 1–20: Dubbing & dubbing QA, Indic scripts, film, gaming, sound |
| [`high-trust-services_law_mental_health_osint.md`](./high-trust-services_law_mental_health_osint.md) | Problems 1–20: Legal AI, ODR, dementia care, rental agreements, OSINT |
| [`education-community-innovation.md`](./education-community-innovation.md) | **New — Problems 1–14:** the community innovation school (60/40 skills), Indian science + Adhyatmic scaffolding, F1-style competitions, freedom-fighter management & way-of-life course |
| [`financial-inclusion-informal-economy.md`](./financial-inclusion-informal-economy.md) | **New — Problems 1–12:** credit for the thin-file borrower, micro-pension, micro-insurance, gold-loan transparency, SHG credit, money desk |

---

## Domain Overview

### 1. Energy Transition & Climate Resilience
**File:** [`energy-transition.md`](./energy-transition.md)  
**Focus:** LPG clean-cooking safety, solar soiling prediction, P2P trading, EV charging, second-life batteries, micro-hydro, carbon MRV, classroom IAQ, green hydrogen, biomass logistics, agri-pump demand response  
**Axiom base:** Thermodynamics, real-time grid balance, cost minimization, land constraint, incentive design  
**Key stat:** India targets 500 GW non-fossil capacity by 2030

### 2. Electronics & Software
**File:** [`electronics-software.md`](./electronics-software.md)  
**Focus:** RISC-V cores, micro-RTOS, EMI pre-compliance, KiCad procurement/DFM, MCU FOTA, board bring-up copilots, test fixtures, PMIC design  
**Axiom base:** Moore's Law deceleration, physical computation limits, signal integrity, abstraction overhead, mask cost  
**Key stat:** India imports ~$35B of semiconductors annually

### 3. Biotech, Health & Longevity
**File:** [`biotech-health-longevity.md`](./biotech-health-longevity.md)  
**Focus:** Paper-strip diagnostics, genomic privacy, mental-health screening, respiratory devices, newborn care (phototherapy, hypothermia), anemia, diabetes self-management  
**Axiom base:** Physical/chemical laws of biology, individual variation, Eroom's Law, early-detection value, information asymmetry  
**Key stat:** 100M diabetics, 0.75 psychiatrists per 100K population

### 4. Defence, Space & Advanced Manufacturing
**File:** [`defence-space-advanced-manufacturing.md`](./defence-space-advanced-manufacturing.md)  
**Focus:** GPS-denied visual-inertial odometry, GNSS jamming/spoofing detection, swarm protocols, cubesat ADCS simulation, machine-tool condition monitoring, CBRN sensors, SDR HF/VHF tactical waveform, anti-drone acoustic detection, wargaming, NavIC stack  
**Axiom base:** Information dominance, supply-chain security, physics constraints, deterrence economics, dual-use technology  
**Key stat:** Defence budget FY27: ₹7.84L Cr

### 5. Agri-Food, Water & Urbanisation
**File:** [`agri-water-urbanisation.md`](./agri-water-urbanisation.md)  
**Focus:** Onion curing & storage, decentralized wastewater, stubble burning, soil health sensors, water leak detection, counterfeit-input verification, desalination, smart irrigation, digital twins  
**Axiom base:** Closed-loop cycles, photosynthesis efficiency, circular economy, scale economics, local trust  
**Key stat:** 72% of urban sewage untreated, 40% food lost post-harvest

### 6. Creative & Strategic Taste Economy
**File:** [`creative-taste-economy.md`](./creative-taste-economy.md)  
**Focus:** Consent-based Indian voice corpus, IP valuation, indie game publishing, textile patterns, OTT recommendation, mobile-esports tournament integrity, film pre-production, sound libraries  
**Axiom base:** Attention scarcity, cultural moat, network effects, non-fungible taste, IP as a real asset, local-language advantage  
**Key stat:** India's media & entertainment sector ~$30B, 500M gamers

### 7. High-Trust Services
**File:** [`high-trust-services_law_mental_health_osint.md`](./high-trust-services_law_mental_health_osint.md)  
**Focus:** Legal document simplification, ODR, dementia caregiver support, rental-agreement escrow, OSINT, tele-psychiatry, contract review, prison reform  
**Axiom base:** Trust as risk-reduction, time value of justice, bounded rationality, information asymmetry, formal rule semantics  
**Key stat:** 5 Cr+ pending court cases, 150M+ need mental health support

### 8. Education — Community Innovation & the Indian Way of Learning *(New)*
**File:** [`education-community-innovation.md`](./education-community-innovation.md)  
**Focus:** The community innovation school (one craft, deep mastery, 60% core + 40% business/research/soft skills), science + Adhyatmic grounding, rapid mentorship, real-world problem statements, F1-style monthly competitions, open-source output, a freedom-fighter way-of-life & management course, and the wider "how India learns" problems  
**Axiom base:** Learn by doing and teaching, motivation as the binding constraint, mentor time as the scarce resource, skill + character, inherited ways of life, openness compounding, rightly staged competition, trust by small consistent acts  
**Key insight:** Technology is optional. Many of these problems are runbooks, curricula, and community systems — not devices.

### 9. Financial Inclusion & the Informal Economy *(New)*
**File:** [`financial-inclusion-informal-economy.md`](./financial-inclusion-informal-economy.md)  
**Focus:** UPI/GST-based credit scoring for the thin-file borrower, nano-loans with community guarantee, gold-loan transparency, portable micro-pension, benefit navigators, MSPME invoice discounting, micro-insurance, migrant remittance + savings, SHG credit, money clinics, "trace your money"  
**Axiom base:** Money as medium of trust, data-exhaust as credit signal, small/frequent shapes, honest and fast claims, transparent pricing, frictionless small savings, one-time digitalisation of seams, portable identity  
**Key stat:** ~8 in 10 workers are informal; informal credit can cost 24–60%+ APR

---

## Methodology

Each problem was derived with the same discipline:

1. **Research Summary** — key facts, statistics, and constraints per domain
2. **Axiom List** — fundamental truths that cannot be reduced further
3. **Derivation** — the logic chain from axiom to problem
4. **Problem Statements** — tabular, one line per problem, covering:
   - Problem + why it is still unsolved
   - Human or planet impact
   - The proposed approach
   - A 3-month first version (pilot, prototype, or runbook)
   - The first-principles derivation
   - Validation (including the competitive landscape and honest caveats)

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Total Problem Statements | 166 |
| Domains covered | 9 |
| Estimated buildable in ~3 months | 166 (100%) |
| Mostly tech-heavy (SW / HW / IoT) | 140 across the original 7 domains |
| Education & financial (mixed; many non-tech/community) | 26 |
| Replaced because a solution already existed | 17 (across two passes; see notes) |

---

## How to Use This Repository

1. **Browse domains** via the table above or `summary-all.md`
2. **Deep dive** into any domain file for the full problem, its competitive check, and its derivation
3. **Pick a problem** and build the 3-month first version described
4. **Contribute back** — add build notes, extend the competitive landscape, or propose new problems

---

## Cross-Cutting Concerns (and the "who pays" test)

1. Regulatory approval timelines (health, defence, banking) often exceed the 3-month build cycle
2. Adoption in rural/trust-based markets requires community engagement beyond the prototype
3. Interoperability standards must be solved for systemic — not point — solutions
4. Privacy/security must be built in, not bolted on (DPDP Act 2023 is now a fact of life)
5. Talent pipeline for hardware+AI remains the binding constraint in India
6. Every problem, no matter how noble, still has to pass the "who pays" test — the answer is written into each validation line

---

## What Changed Recently (and why)

- **Domain 8 (Education)** and **Domain 9 (Financial Inclusion)** were added because the original seven domains covered *what India makes* but not *how India thinks and earns*. The education domain deliberately needs almost no technology: most of it is model design, curriculum, and community ritual.
- **Replacement pass 1:** a few problem statements described things the market has already got. Those were swapped for sharper gaps:
  - *Grid-tie inverter* → **LPG clean-cooking safety** (inverters are now commodity; LPG accidents kill)
  - *Rooftop solar estimation tool* → **Classroom IAQ ventilation** (Project Sunroof-type tools exist)
  - *P2P carbon marketplace* → **PM-KUSUM agri-pump demand response** (carbon aggregation duplicates #9)
  - *Solar cold storage* → **Onion curing & storage controller** (Ecozen/Inficold already ship at scale)
  - *Crop-disease AI app* → **Counterfeit pesticide verification** (Plantix already has 100M+ answers)
  - *TB adherence tracker* → **Adolescent mental-health screening** (99DOTS/Nikshay already runs nationwide)
  - *The biotech file was also completed from 10 → 20 problems* so every domain has a full set.
- **Replacement pass 2:** the electronics, defence, and creative files carried entries that overlapped existing open-source or commercial solutions. 11 problems were swapped:
  - *Pick-and-place machine* → **EMI/EMC pre-compliance kit** (LumenPnP/OpenPnP already ship sub-$1K machines)
  - *RISC-V IDE + debugger toolchain* → **KiCad procurement & DFM plugin** (PlatformIO + OpenOCD + VS Code already support RISC-V)
  - *Open-hardware RISC-V debug probe* → **Board bring-up copilot** (CMSIS-DAP, WCH-Link, esp-prog exist)
  - *WebUSB firmware flasher* → **Flying-probe in-circuit tester** (esptool.js / ESP Web Serial tool exist)
  - *Drone mission computer* → **GPS-denied visual-inertial odometry** (Pixhawk/CubePilot dominate the hardware)
  - *SDR spectrum monitoring* → **GNSS jamming & spoofing detection** (RTL-SDR + GNU Radio is the commodity baseline)
  - *Satellite ground station tracker* → **Cubesat ADCS simulator + HIL testbed** (SatNOGS solves the tracker)
  - *Open-source CNC controller* → **Machine-tool condition monitoring** (GRBL/LinuxCNC exist)
  - *Encrypted mesh comms device* → **SDR HF/VHF tactical waveform** (Meshtastic already does the LoRa mesh)
  - *AI dubbing engine* → **Consent-based Indian voice corpus + licensing layer** (Dubverse already ships 60+ language lip-synced dubbing)
  - *Open-hardware esports controller* → **Mobile-esports tournament integrity analytics** (sub-₹1,500 gamepads exist)
- The **Replacement Log** tables (what was swapped and the existing solution found) live in [`docs/replacement-logs.md`](docs/replacement-logs.md).
- Note: `instructions.md` is referenced in an old README but was never committed; the reference has been dropped.