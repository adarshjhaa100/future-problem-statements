# Methodology — Aristotle, First Principles, and the 12-Month Test

## 1. Why Aristotle in 2026

Most "problem lists" fail because they are lists of symptoms. Aristotle gives a compact discipline for going from symptom to cause:

- **Material cause** — what the situation is made of: atoms, water, data, trust, time, attention, cash flow.
- **Formal cause** — the structure that reproduces the situation: incentives, contracts, property rights, workflows, norms, interfaces.
- **Efficient cause** — the agent or mechanism that can actually change it: a landlord, a nurse, a municipal engineer, a procurement officer, a battery, a subsidy, a nudge.
- **Final cause (telos)** — the human good the work serves: safety, dignity, health, autonomy, justice, flourishing.

A problem statement is mature when it names all four. A solution is serious when it changes the **efficient cause** in a way that is compatible with the **material cause**, repairs the **formal cause**, and serves a defensible **telos**. Technologies that only describe the material cause ("we will use AI on the data") are not solutions.

We also use Aristotle's distinction between **potentiality and actuality**. A community may have the potential for clean water, safe housing, or fair credit, but the actualising conditions — maintenance, verification, trust, cash flow — are missing. Most of the 144 problems are actualisation problems, not invention problems. That is why many are non-software or only partly software.

## 2. The axiom stack

Each domain file carries its own axioms, but the repository uses five recurring classes:

1. **Physical axioms** — thermodynamics, conservation, latency, material limits, biology. You cannot negotiate with them.
2. **Information axioms** — measurement changes behaviour; information asymmetry creates rents; verification is expensive; provenance is not free.
3. **Economic axioms** — agents respond to incentives; someone must pay; split incentives block otherwise rational upgrades; small tickets have high fixed costs.
4. **Behavioural axioms** — attention is scarce; losses loom larger than gains; defaults and friction dominate; people copy trusted peers; identity and dignity shape adoption more than information.
5. **Institutional axioms** — rules need enforcement; liability follows responsibility; procurement is a product; trust is local and slow to build, fast to lose.

The derivation chain in each row is deliberately short: *axiom → mechanism → gap → intervention → falsifiable test*. If the chain needs ten steps, the problem is probably too abstract for a 1–3 person team.

## 3. The six filters

Every problem must pass:

### Filter 1 — Importance
Reach (how many people), severity (death, disability, loss of livelihood, loss of dignity), and duration (how long the harm lasts or compounds). A problem that kills 100 people a year for 30 years can outrank a problem that annoys 10 million people for a week. We record impact as **who × how long**.

### Filter 2 — Neglectedness
Relative number of credible people or teams working on it. We use four labels:

- **SATURATED** — well-funded incumbents, many startups, strong open-source; roughly 100+ credible teams.
- **CROWDED** — real competition, but a defensible niche exists; roughly 20–100 credible teams.
- **THIN** — a handful of teams, often not productised, often not localised; roughly 3–20 credible teams.
- **NEAR-ZERO** — no credible product or field team; mostly papers, pilots, or NGOs; roughly 0–3 credible teams.

These are relative density estimates, not a census. A "THIN" label can hide a stealth startup, a government pilot or a research group. The named examples in the rows are the evidence for the label.

"Thin" is not automatically good; a thin field can be thin because it is impossible. That is why Filter 3 exists.

### Filter 3 — Feasibility
Can 1–3 people produce a legible first version in under 12 months? We define "legible" as something a buyer, regulator, clinician, or community can test and either adopt or reject. Feasibility includes regulatory path, data access, hardware supply, and whether the team needs a lab or a licence.

### Filter 4 — Budget
Pilot budgets are stated in both ₹ and US$ (roughly ₹85/US$1). The ceiling is usually **US$150K** for the first version. Hardware and field pilots can exceed it, but then the first version must be a deliberately narrow slice (one ward, one clinic, one factory, one feeder).

### Filter 5 — Who pays
There must be an adopter whose own interest aligns: insurer, utility, hospital, municipality, platform, employer, cooperative, exporter, landlord, or household. "Government should" is not a business model. "Government already pays for the failure" is.

### Filter 6 — Falsifiability
Every row has a kill criterion. Examples: "kill if indoor peak temperature falls by less than 2°C", "kill if antibiotic prescribing does not fall by 15%", "kill if claim settlement takes more than 7 days". The first version is an experiment, not a demonstration.

## 4. What counts as a 3-month-first-version vs a 6–11-month implementation

The repository uses two horizons:

- **3-month first version:** a prototype, runbook, curriculum, or single-site pilot that can be shown to a sceptical outsider. It is not a company.
- **6–12-month implementation:** the path from first version to a repeatable deployment with one paying or adopting partner. This is the "time to potential implementation" we report.

A 1–3 person team can do one, sometimes two, of these at a time. The team field names the minimum roles, not the ideal team.

## 5. Uniqueness test

A problem is rejected or rewritten if:

- A well-funded company already ships the exact product at the target price point.
- The "problem" is a feature of an existing platform, not a standalone pain.
- The solution requires a new law, a new molecule, or a new standard before the first version.
- The problem is only interesting to a conference audience.
- The solution's main value is "raising awareness".
- The same mechanism appears in another domain with only the noun changed.

We allow related problems across domains only when the **efficient cause** is different (e.g., a heat-safe rental score vs a cooling-centre activation protocol). The cross-domain map in the README shows these adjacencies.

## 6. The Aristotle review questions

Every row is reviewed against these questions:

1. **Material:** what is the intervention physically made of? Is the bill of materials real?
2. **Formal:** what rule, contract, or workflow changes? Who signs?
3. **Efficient:** who wakes up on Monday and does the work? Is that person in the team's reach?
4. **Final:** whose flourishing is served? Is anyone made worse off?
5. **Potential → actual:** what is the actualising condition (maintenance, trust, verification, payment) that everyone forgets?
6. **Virtue:** does the solution require deception, surveillance, or dependency to work? If yes, redesign.
7. **Falsification:** what result would prove the team wrong, and when will they know?

## 7. Startup idea layer

Each problem row now carries 2–3 startup concepts. The test is deliberately stricter than "could this be a company":

1. **1–3 people:** the first version must be buildable by the named minimum team, not a hypothetical 20-person startup.
2. **Under 12 months:** the path to a legible pilot, demo, runbook or partner decision must be under a year.
3. **Research/experiment:** there must be a specific test, site, dataset or partner that can falsify the idea quickly.
4. **Payer:** the idea must name the buyer or budget line it will test.
5. **Mechanism:** the idea must use the same causal mechanism as the problem row, not a generic "AI for X" wrapper.

The `fit:` tag in each cell is shorthand for **team size / months / first experiment**. It is a planning claim, not a guarantee. Hardware certification, clinical governance, defence procurement and court acceptance can extend the path; those risks are named in the row's validation cell.

## 8. Scoring and tiers

The summary uses three tiers:

- **Tier A — compounding:** high reach and long duration, strong neglectedness, clear payer. These are the first picks.
- **Tier B — strong niche:** smaller reach or harder adoption, but high severity per person and a credible path.
- **Tier C — speculative or infrastructure:** important, but dependent on a partner, standard, or policy window. Build only with a specific partner.

Tiers are not moral rankings. A Tier C problem can change a system; it is simply less likely to succeed as a 1–3 person, 12-month project.

## 9. What the repository deliberately is not

- It is not a startup idea list. Some problems are best run by a cooperative, municipality, hospital, or standards body.
- It is not a claim that technology is the answer. Many rows are runbooks, contracts, curricula, inspection protocols, and financing structures.
- It is not a forecast. It is a portfolio of bets with stated kill criteria.
- It is not a substitute for local knowledge. Every pilot needs a local partner who can say "that is not how it works here".

The standard is simple: **a sceptical, capable person should be able to read a row and know whether to spend the next six months on it.**
