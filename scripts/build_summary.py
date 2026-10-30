#!/usr/bin/env python3
"""Rebuild summary-all.md from the domain tables."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ("planetary-health-climate.md", "Planetary Health & Climate"),
    ("energy-grid-materials.md", "Energy, Grid & Materials"),
    ("food-water-land.md", "Food, Water & Land"),
    ("health-biosecurity-longevity.md", "Health & Biosecurity"),
    ("ai-trust-information.md", "AI & Digital Trust"),
    ("care-mental-health-development.md", "Care & Human Development"),
    ("education-skills-work.md", "Education & Work"),
    ("financial-inclusion-real-economy.md", "Financial Inclusion"),
    ("cities-mobility-housing.md", "Cities & Housing"),
    ("industry-space-defence.md", "Industry, Space & Defence"),
    ("governance-justice-civic.md", "Governance & Justice"),
    ("creative-attention-economy.md", "Creative & Culture"),
]


def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def clean(s: str) -> str:
    return re.sub(r"\*\*", "", s).replace("|", "/").strip()


def short(s: str, n: int) -> str:
    s = clean(s)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


def main() -> None:
    out = [
        "# Summary — 144 Problems Across 12 Domains (October 2026)\n",
        "A compact scan of every problem. Full rows live in the domain files. Impact is stated as reach × duration; crowd is relative team density; budgets are first-version pilots, not scale. Startup ideas include a fit tag: team size, months, and the first experiment.\n",
        "| Domain | # | Problem | Type | Impact | Crowd | Budget | Team & time | Startup ideas |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for filename, label in FILES:
        for line in (ROOT / filename).read_text().splitlines():
            if re.match(r"^\| \d+ \|", line):
                c = cells(line)
                if len(c) < 14:
                    continue
                out.append(
                    f"| {label} | {clean(c[0])} | {clean(c[1])} | {clean(c[2])} | "
                    f"{short(c[5], 120)} | {short(c[4], 85)} | {clean(c[6])} | {clean(c[7])} | "
                    f"{clean(c[13])} |"
                )
    out += [
        "\n## How to read the columns\n",
        "- **Impact** — who is affected and for how long. A row with “decades” compounds; a row with “weeks” is acute.\n"
        "- **Crowd** — SATURATED, CROWDED, THIN or NEAR-ZERO, with named players or the specific gap.\n"
        "- **Budget** — the cost of the first version, in ₹ and US$ at roughly ₹85/US$1.\n"
        "- **Team & time** — the minimum viable team and the path to a repeatable deployment, not a demo.\n"
        "- **Startup ideas** — 3 concepts with a fit tag: team size, months, and the first experiment. All are scoped to 1–3 people and under one year.\n",
        "\n## Portfolio shape\n",
        "| Layer | Domains | What they change |",
        "|---|---|---|",
        "| Survival & health | Planetary, Food/Water, Health, Care | The physical and human preconditions for everything else |",
        "| Systems & infrastructure | Energy/Materials, Cities, Industry/Defence | The grids, materials, streets and supply chains that carry daily life |",
        "| Trust & capability | AI Trust, Education/Work, Finance, Governance, Creative | The rules, credentials, contracts and information that let people act |",
        "\nThe tiers are implicit: rows with large reach, long duration, thin crowds and a clear payer are the first picks. Rows with a hard regulatory or partner dependency are later bets, not weaker ones.\n",
    ]
    (ROOT / "summary-all.md").write_text("\n".join(out))
    print("wrote summary-all.md")


if __name__ == "__main__":
    main()
