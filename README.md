# Problem Statements Repository — 140 Buildable Problems Across 7 Domains

A first-principles-derived collection of 140 validated problem statements (20 per domain) that an engineer can build a working prototype for in ~3 months. Each problem includes competitive landscape validation, economic quantification, and critical-thinking caveats.

---

## Repository Structure

| File | Description |
|------|-------------|
| [`instructions.md`](./instructions.md) | Original research brief with methodology (first-principles derivation, axiomatic reduction) |
| [`summary-all.md`](./summary-all.md) | Consolidated tabular view of all 140 problems with cross-domain validation |
| [`energy-transition.md`](./energy-transition.md) | Problems 1–20: Solar, grid, EV, carbon markets, energy efficiency |
| [`electronics-software.md`](./electronics-software.md) | Problems 1–20: RISC-V, embedded systems, TinyML, FOTA, PCB tools |
| [`biotech-health-longevity.md`](./biotech-health-longevity.md) | Problems 1–20: Diagnostics, genomics, mental health, preventive care |
| [`defence-space-advanced-manufacturing.md`](./defence-space-advanced-manufacturing.md) | Problems 1–20: Drones, SDR, C4ISR, CNC, space, wargaming |
| [`agri-water-urbanisation.md`](./agri-water-urbanisation.md) | Problems 1–20: Soil health, cold chain, wastewater, irrigation, waste mgmt |
| [`creative-taste-economy.md`](./creative-taste-economy.md) | Problems 1–20: Dubbing, gaming, textile AI, OTT, animation, fashion |
| [`high-trust-services.md`](./high-trust-services_law_mental_health_osint.md) | Problems 1–20: Legal AI, ODR, mental health, OSINT, compliance |

---

## Domain Overview

### 1. Energy Transition & Climate Resilience
**File:** [`energy-transition.md`](./energy-transition.md)  
**Focus:** Solar inverters, grid balancing, EV charging, battery 2nd-life, carbon credits, micro-hydro, green hydrogen, biomass logistics  
**Axiom base:** Thermodynamics (energy cannot be created/destroyed), real-time grid balance, cost minimization, land constraint  
**Key stat:** India targets 500 GW non-fossil capacity by 2030

### 2. Electronics & Software
**File:** [`electronics-software.md`](./electronics-software.md)  
**Focus:** RISC-V cores, micro-RTOS, pick-and-place machines, TinyML compilers, PMIC design, USB analyzers, FOTA, FPGA motor controllers  
**Axiom base:** Moore's Law deceleration, physical computation limits, signal integrity, abstraction overhead, mask cost  
**Key stat:** India imports ~$35B of semiconductors annually

### 3. Biotech, Health & Longevity
**File:** [`biotech-health-longevity.md`](./biotech-health-longevity.md)  
**Focus:** Paper-strip diagnostics, genomic privacy, AI triage, CGM wearables, ADR prediction, infant warmers, lab automation, voice biomarkers  
**Axiom base:** Biological physical/chemical laws, individual variation, Eroom's Law, early detection value, information asymmetry  
**Key stat:** 100M diabetics, 0.75 psychiatrists per 100K population

### 4. Defence, Space & Advanced Manufacturing
**File:** [`defence-space-advanced-manufacturing.md`](./defence-space-advanced-manufacturing.md)  
**Focus:** Drone mission computers, SDR, swarm protocols, satellite ground stations, predictive maintenance, CBRN sensors, CNC controllers, anti-drone systems  
**Axiom base:** Information dominance, supply chain security, physics constraints, deterrence economics, dual-use technology  
**Key stat:** Defence budget FY27: ₹7.84L Cr

### 5. Agri-Food, Water & Urbanisation
**File:** [`agri-water-urbanisation.md`](./agri-water-urbanisation.md)  
**Focus:** Wastewater treatment, stubble burning detection, soil health sensors, solar cold storage, waste segregation, water leak detection, crop disease AI, desalination, smart irrigation, digital twins  
**Axiom base:** Closed-loop cycles, photosynthesis efficiency, circular economy, scale economics, local trust  
**Key stat:** 72% of urban sewage untreated, 40% food lost post-harvest

### 6. Creative & Strategic Taste Economy
**File:** [`creative-taste-economy.md`](./creative-taste-economy.md)  
**Focus:** AI dubbing (22 languages), IP valuation, indie game publishing, textile pattern AI, OTT recommendation, esports controllers, virtual production, sound design, film pre-production, script analysis  
**Axiom base:** Attention scarcity, cultural moat, network effects, non-fungible taste, IP as real asset, local language advantage  
**Key stat:** India's media & entertainment sector ~$30B, 500M gamers

### 7. High-Trust Services
**File:** [`high-trust-services.md`](./high-trust-services.md)  
**Focus:** Legal document simplification, ODR for small claims, mental health triage, OSINT for disinformation, regulatory compliance, tele-psychiatry, contract review, case timeline prediction, legal awareness, blockchain evidence  
**Axiom base:** Trust as risk-reduction, time value of justice, bounded rationality, information asymmetry, formal rule semantics  
**Key stat:** 5 Cr+ pending court cases, 150M+ need mental health support

---

## Methodology

Each problem was derived using a **first-principles framework**:

1. **Research Summary** — key facts, statistics, and constraints per domain
2. **Axiom List** — fundamental truths that cannot be reduced further (e.g., thermodynamics, physics bounds, economic principles)
3. **Derivation** — logic chain connecting axioms to problem identification
4. **Problem Statements** — tabular format with:
   - Problem name & type (SW+IOT / HW / SW)
   - Why it remains unsolved/inefficient
   - Human/Planet impact
   - 3-month prototype description
   - First-principles derivation
   - Validation (stats, economics, Bhagwad Gita principle, critical caveats)
   - **Competitive landscape** against existing solutions

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Total Problem Statements | 140 (20 per domain) |
| SW+IOT Problems | ~80 |
| Hardware (HW) Problems | ~35 |
| SW-only Problems | ~25 |
| Estimated buildable in 3 months | 140 |
| Domains covered | 7 |

---

## How to Use This Repository

1. **Browse domains** via the table above or `summary-all.md` for a quick overview
2. **Deep dive** into any domain file for full problem details, competitive validation, and first-principles derivation
3. **Pick a problem** and build the 3-month prototype described
4. **Contribute back** — add your build notes, expand the competitive landscape, or propose new problems

---

## Cross-Cutting Concerns

1. Regulatory approval timelines (health, defence) often exceed 3-month build cycle
2. Adoption in rural/trust-based markets requires community engagement beyond prototype
3. Interoperability standards must be solved for systemic (not point) solutions
4. Privacy/security must be built in, not bolted on
5. Talent pipeline for hardware+AI is the binding constraint in India
6. First-principles solutions must still pass the "who pays" test
