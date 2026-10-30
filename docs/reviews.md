# Three Review Passes

The repository was rebuilt from scratch for October 2026. This file records what the reviews actually changed, including the rows that were rejected or rewritten. The goal is not to claim perfection; it is to make the reasoning auditable.

## Pass 1 — Importance, Evidence and Neglectedness

**Question:** Is this problem big enough, long enough and neglected enough to deserve a place?

### What changed

| Issue found | Action | Example |
|---|---|---|
| The old edition had rows that were already well served by commercial or open-source products. | Removed them from the new set and archived the old files. | Pick-and-place machines, mesh radios, generic dubbing engines, crop-disease classifiers, battery-management boards, generic solar marketplaces, generic LMS platforms. |
| Several "problems" were really features of an existing platform. | Rewrote around the missing institution or measurement. | "AI tutor" → teacher retention early warning, apprenticeship matching, proof-of-human-skill portfolio. |
| Impact was often a headline number without duration. | Every impact cell now states reach and how long the harm lasts or compounds. | Heat-safe rentals: 100M+ renters, 3–6 dangerous months a year, developmental effects over decades. |
| Some domains were technology-heavy and missed the human actualising conditions. | Added Care Economy, Governance/Justice and Planetary Health as first-class domains. | Dementia caregiver micro-respite, prison family connection, flood mould prevention. |
| Duplicate mechanisms appeared under different nouns. | Kept only where the efficient cause differed. | Heat appears in planetary (rental score), cities (bus-stop shade), and health (heat illness); each has a different actor and budget line. |
| "Who pays" was vague. | Added a named payer or budget line to every row. | Insurer, utility, municipal ward, hospital, buyer, cooperative, court, employer. |
| Evidence was stale or unsourced. | Added the shared 2026 research base and domain summaries with sources. | WEF 2026, WHO 2026, FAO 2026, WWF 2026, IEA 2026, IRENA 2026, UNESCO 2026, RBI 2026. |
| Some claims were overconfident. | Labelled projections and contested evidence; removed causal claims where evidence is preliminary. | Microplastics: exposure is documented, causal disease link is not; the problem is exposure reduction and measurement, not alarmism. |

### Rows rejected or reframed in Pass 1

- **Generic crop-disease AI app** → replaced with aflatoxin testing at the collection centre. The plant-disease app market is crowded; the loss point is the buyer's batch.
- **Generic mental-health chatbot** → replaced with school self-harm escalation, men's peer support, grief postvention and task-shifting supervision. Chatbots are crowded; the gap is the pathway and the trusted human.
- **Another solar marketplace / battery BMS** → replaced with distribution transformer monitoring, rooftop grid-support retrofit and magnet recycling. The former are saturated; the latter are infrastructure seams.
- **Another legal chatbot** → replaced with legal aid matching, court interpreter scheduling and evidence organisation for self-represented litigants. The bottleneck is access and procedure, not text generation.
- **Another "smart city" dashboard** → replaced with street-vending allocation, bus-stop audits, black-spot retrofit and loading-bay booking. The gap is allocation and maintenance, not visualisation.

### Pass 1 outcome

- 144 problems across 12 domains.
- Every domain has a research summary and an axiom list.
- Every row has a reach × duration impact statement and a relative crowd assessment.

---

## Pass 2 — Feasibility, Adoption and Behavioural GTM

**Question:** Can 1–3 people actually ship a first version under 12 months, and will the intended person adopt it?

### What changed

| Issue found | Action | Example |
|---|---|---|
| Some rows implicitly needed a large team or a lab. | Reduced to 1–3 named roles; split hardware/space pilots into narrow slices. | Rad-hard RISC-V is an FPGA prototype with a radiation test plan, not a fab. |
| "3-month" was used as a slogan. | Clarified 3-month first version vs 6–11-month implementation; every row now has a time horizon under one year. | 100 rentals over one summer; 10 clinics over 9 months; one feeder over 8 months. |
| Budgets were missing or unrealistic. | Added a pilot budget in ₹ and US$; most are ₹8–40 lakh, with hardware/space up to ₹80 lakh. | Transformer canary: ₹20–35L for 50 transformers. |
| Adoption plans were generic "awareness" campaigns. | Replaced with a diagnosis of the binding behavioural gap and at most three levers. | Landlords: loss aversion + social proof + insurance rebate; clinicians: peer comparison + default + liability. |
| Low-trust users were assumed to download apps. | Added WhatsApp/IVR, local messengers, paper backups and human intermediaries. | Flood kits distributed with relief; fisher cold chain via cooperatives; police complaints via legal aid. |
| Fear marketing was overused. | Added ethical guardrails and gain framing where fear would backfire. | Heat insurance uses fast-payout trust, not doom; teen safety audit avoids sensationalism. |
| No kill criteria. | Added a measurable stop rule to every row. | Kill if indoor temperature drop <2°C; if antibiotic prescribing falls <15%; if claim payout >7 days. |
| Some horizons were exactly 12 months, which violates the <1-year constraint. | Reduced implementation horizons to 11 months where needed; moved long-term outcome measurement into a separate tracking note. | Tree survival is deployed in 9 months with a 9-month survival proxy; the 24-month warranty is tracked separately. |
| Some product terms (e.g. follow-up) exceeded the build horizon. | Separated the build/pilot horizon from the service term. | Foster-care navigation is built in 8 months; the follow-up protocol can run 24 months. |
| Regulatory dependencies were hidden. | Named the regulator or certification path. | PESO for LPG, export control for defence, clinical governance for wound/mental health, court acceptance for evidence tools. |
| "Who pays" was still weak in some rows. | Added the payer's existing loss line. | Insurer readmission penalty, utility demand-response budget, municipal avoided liability, buyer rejection cost. |

### Rows rewritten in Pass 2

- **Heat-safe rental housing** — originally a generic "cool roof" idea. Rewritten as a tenancy-time heat score plus a tenancy-safe kit, because the split incentive is the actual blocker.
- **Dementia caregiver support** — originally a generic caregiver app. Rewritten as micro-respite with safeguarding and an employer benefit, because the binding constraint is a break, not information.
- **AI voice-scam protection** — originally another deepfake detector. Rewritten as a family verification protocol plus bank confirmation, because detection is crowded and voice is not identity.
- **Local news** — originally a generic membership tool. Rewritten as micro-donation at the point of reading plus funded-story targets, because the unit of value is a story, not a subscription.
- **Defence procurement** — originally a broad "govtech" idea. Rewritten as clause tagging and audit for DP&P/export control, with a compliance partner and human sign-off.
- **Craft e-commerce** — originally another artisan marketplace. Rewritten as cluster provenance plus cooperative verification, because the gap is trust and middleman capture, not another storefront.

### Pass 2 outcome

- Every row has a team of 1–3, a budget, a time horizon, a first-version test and a kill criterion.
- Every row has a behavioural GTM plan with first 100 users, a loop and an ethical guardrail.
- Hard dependencies are named; no row pretends it can start without the partner.

---

## Pass 3 — Uniqueness, Coherence and Aristotle

**Question:** Is this row genuinely different, internally coherent, and does it change the efficient cause?

### What changed

| Issue found | Action | Example |
|---|---|---|
| Some solutions were "AI on data" without a mechanism. | Rewrote to name the physical, contractual or behavioural mechanism. | Not "AI for credit" but "GST-verified invoice + lien + auction"; not "AI for health" but "photo triage + nurse escalation". |
| Aristotle's four causes were sometimes decorative. | Made the first-principles cell answer material, formal, efficient and telos, plus feasibility. | Heat: material (roof/windows), formal (split incentive), efficient (lease disclosure + kit), telos (safe shelter). |
| Some rows had a weak telos or an ethical risk. | Added the ethical guardrail and, where needed, changed the design. | No tenant surveillance; no teen surveillance; no public shaming of clinicians; no cultural extraction. |
| Cross-domain duplication remained possible. | Ran a mechanism audit. Kept only rows with a different efficient cause. | Insurance appears as heat (planetary), funeral/livestock (finance), trade credit (finance), but each has a different peril and payer. |
| The set was unbalanced toward software. | Ensured each domain has hardware, process, community or finance rows. | Planetary has kits and protocols; care has services; governance has court and prison operations. |
| Some "thin" crowds were actually "impossible". | Rechecked feasibility; removed or narrowed rows requiring new molecules, new laws or new standards. | Rad-hard RISC-V is a prototype with a test plan; no row requires a new drug or a new statute before the first version. |
| The summary and index could drift from the domain files. | Added a validator and rebuilt the summary from the domain tables. | `scripts/validate.py` checks 12 rows per domain, required columns, and duplicate titles. |
| One civic-tech row was too close to existing participation platforms. | Replaced it with a municipal contract change-order leak detector, which has a different mechanism and payer. | Polis/Consider.it crowd public-comment analysis; change-order anomaly detection is thin. |
| Marketing could become manipulation. | Added a seven-question GTM template and an ethical floor. | No fabricated statistics, fake scarcity, shaming or dark patterns. |

### The Aristotle audit

Every row was checked against seven questions:

1. **Material:** Is the bill of materials or the human labour real?
2. **Formal:** What rule, contract or workflow changes? Who signs?
3. **Efficient:** Who wakes up on Monday and does the work? Is that person reachable?
4. **Final:** Whose flourishing is served? Is anyone made worse off?
5. **Potential → actual:** What maintenance, trust or verification condition is missing?
6. **Virtue:** Does the solution require deception, surveillance or dependency?
7. **Falsification:** What result would prove the team wrong, and when?

### Rows that survived but were narrowed

- **Critical-mineral recovery from smelter dust** — narrowed to a 100-kg pilot with a smelter partner; not a refinery.
- **Radiation-hardened RISC-V** — narrowed to an FPGA prototype and a radiation test plan; not a fab.
- **Data-centre waste heat to cold storage** — narrowed to one 200-kW data centre and a 10-tonne cold room; not a district heating network.
- **Disaster debris reuse** — narrowed to one disaster-affected district with structural testing; not a national marketplace.
- **Local film archive restoration** — narrowed to 100 reels with an archive partner; not a studio.

### Pass 3 outcome

- 144 unique rows, 12 per domain, with no duplicate titles.
- Every row has a mechanism, a payer, a first-version test, a kill criterion and a GTM plan.
- The set is balanced across survival, systems and trust layers.
- The summary, README and index are generated or checked against the same domain files.

---

## What is still uncertain

This is a living document, not a peer-reviewed portfolio. The main uncertainties are:

- **Crowd estimates** are relative and based on public products, research and visible teams, not a census. A "THIN" label can hide a stealth startup or a government pilot.
- **Budgets** are planning ranges, not quotes. Hardware certification, field logistics and legal review can double them.
- **Impact estimates** are order-of-magnitude and often global; local pilots need local baselines.
- **Behavioural GTM** is a hypothesis. The first 100 users are the test, not the proof.
- **Regulatory paths** can change. Every health, defence, finance and court row needs a local legal review before launch.

The correct use of this repository is to pick a row, test the assumption that matters most, and report back — including the failures.

---

## Post-review addition — Startup-idea feasibility

After the three passes, a startup-idea layer was added to every problem row: **432 concepts** (3 per row), each with a `fit:` tag for team size, months, and the first experiment. This was a separate audit, not a cosmetic column.

### What was checked

- **Team:** every idea is scoped to 1–3 people. Concepts that implicitly needed a sales team, a fab, a hospital network or a national regulator were rejected or narrowed.
- **Time:** every idea is scoped to under 12 months for the first legible pilot or partner decision. Long certification paths are named as risks, not hidden.
- **Experiment:** every idea names a first experiment (site, sample, partner, dataset). "Build the platform" is not an experiment.
- **Payer:** every idea names a buyer or budget line to test. "Consumers" or "the market" is not a payer.
- **Mechanism:** every idea uses the same causal mechanism as the problem row. Generic "AI platform" and "marketplace" ideas were rewritten.

### Examples of narrowing

| Problem | Rejected startup shape | Narrowed idea |
|---|---|---|
| Rad-hard RISC-V | Fab a rad-hard chip | FPGA prototype plus TMR library and radiation test plan |
| Critical minerals from smelter dust | Build a refinery | 100-kg modular recovery pilot with one smelter |
| Data-centre waste heat | District heating network | One 200-kW data centre plus a 10-tonne cold room |
| Court evidence authenticity | National forensic platform | 10-case litigation kit with one law firm |
| Voice licensing | Global voice marketplace | 100-voice consent corpus with scoped licences |
| Dementia care | Full home-care agency | 2–4 hour micro-respite blocks with safeguarding |

### What is still uncertain

- A `fit:` tag is a planning estimate, not a validated schedule.
- Some ideas depend on a partner who may say no: a utility, insurer, defence programme, court or hospital.
- The startup column is not a recommendation to incorporate. Some ideas are better run as a cooperative, a service line inside an existing institution, or an open-source project.
- The first experiment is the real test. If the named experiment cannot be run, the idea should be rewritten before any build.
