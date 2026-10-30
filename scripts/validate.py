#!/usr/bin/env python3
"""Validate the problem-statement tables and the repo's cross-file counts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = [
    "planetary-health-climate.md",
    "energy-grid-materials.md",
    "food-water-land.md",
    "health-biosecurity-longevity.md",
    "ai-trust-information.md",
    "care-mental-health-development.md",
    "education-skills-work.md",
    "financial-inclusion-real-economy.md",
    "cities-mobility-housing.md",
    "industry-space-defence.md",
    "governance-justice-civic.md",
    "creative-attention-economy.md",
]
REQUIRED = [
    "problem", "type", "why unsolved", "crowd", "impact", "budget",
    "team & time", "proposed solution", "first version", "first principles",
    "validation", "marketing", "startup ideas",
]
EXPECTED_PER_DOMAIN = 12


def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def main() -> int:
    errors: list[str] = []
    titles: dict[str, str] = {}
    total = 0

    for filename in DOMAINS:
        path = ROOT / filename
        if not path.exists():
            errors.append(f"missing domain file: {filename}")
            continue
        lines = path.read_text().splitlines()
        header = None
        rows = 0
        for line in lines:
            if not line.strip().startswith("|"):
                continue
            cs = cells(line)
            if header is None and any("problem" in c.lower() for c in cs):
                header = [c.lower() for c in cs]
                missing = [c for c in REQUIRED if c not in header]
                if missing:
                    errors.append(f"{filename}: missing columns: {', '.join(missing)}")
                continue
            if header is None or re.fullmatch(r":?-{2,}:?", cs[0]):
                continue
            if not re.match(r"^\d+$", cs[0]):
                continue
            rows += 1
            total += 1
            if len(cs) != len(header):
                errors.append(f"{filename}: row {cs[0]} has {len(cs)} cells, expected {len(header)}")
                continue
            record = dict(zip(header, cs))
            title = re.sub(r"\*\*", "", record.get("problem", "")).strip()
            if title in titles:
                errors.append(f"duplicate title: {title!r} in {titles[title]} and {filename}")
            titles[title] = filename
            for field in ("impact", "crowd", "budget", "team & time", "proposed solution", "first version", "validation", "marketing", "startup ideas"):
                if not record.get(field, "").strip():
                    errors.append(f"{filename}: row {cs[0]} has empty {field!r}")
        if rows != EXPECTED_PER_DOMAIN:
            errors.append(f"{filename}: {rows} rows, expected {EXPECTED_PER_DOMAIN}")

    if total != len(DOMAINS) * EXPECTED_PER_DOMAIN:
        errors.append(f"total rows {total}, expected {len(DOMAINS) * EXPECTED_PER_DOMAIN}")

    summary = (ROOT / "summary-all.md").read_text()
    summary_rows = len(re.findall(r"^\| (?:Planetary|Energy|Food|Health|AI|Care|Education|Financial|Cities|Industry|Governance|Creative)[^|]* \| \d+ \|", summary, re.M))
    if summary_rows != total:
        errors.append(f"summary-all.md has {summary_rows} parsed rows, expected {total}")

    readme = (ROOT / "README.md").read_text()
    if f"{total} Problems" not in readme and f"{total} problems" not in readme:
        errors.append(f"README.md does not mention {total} problems")

    index = (ROOT / "index.html").read_text()
    for filename in DOMAINS:
        if f'file:"{filename}"' not in index:
            errors.append(f"index.html DOMAINS missing {filename}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {total} problems across {len(DOMAINS)} domains; {summary_rows} summary rows; all required fields present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
