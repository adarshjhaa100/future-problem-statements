#!/usr/bin/env python3
"""Clean up duplicate columns and add detail columns properly in one pass."""

import re

ROOT = "/Users/adarsh/Documents/research/futures-202606/problem-statements"
DOMAINS = [
    "energy-transition.md",
    "electronics-software.md",
    "biotech-health-longevity.md",
    "defence-space-advanced-manufacturing.md",
    "agri-water-urbanisation.md",
    "creative-taste-economy.md",
    "high-trust-services.md",
]

def unwrap_bold(name):
    return name.replace("**", "").strip()

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    lines = content.split("\n")
    result = []

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect table start
        if line.strip().startswith("| #") and "|" in line:
            # Parse original columns from first header row
            header = line.strip().strip("|")
            raw_cols = [c.strip() for c in header.split("|")]
            
            # Strip to unique column names, removing duplicates
            seen = set()
            unique_cols = []
            for c in raw_cols:
                key = unwrap_bold(c).lower()
                if key not in seen:
                    seen.add(key)
                    unique_cols.append(c)
            
            # Determine original column indices (before any detail columns were added)
            # Original: #, Problem Statement, Domain Type, Why Unsolved/Inefficient, Impact, 3-Month Prototype, First-Principles Derivation, Validation
            # After adding 2: #, Problem Statement, ProbStmt(Detail), Domain Type, Why Unsolved, Impact, 3-Month Prototype, ProposedSol(Detail), First-Principles Derivation, Validation
            
            # Build new header
            new_uniq = []
            inserted_first = False
            inserted_second = False
            for idx, c in enumerate(unique_cols):
                new_uniq.append(c)
                c_key = unwrap_bold(c).lower()
                # After Problem Statement (column index 1 in original 8-col table)
                if not inserted_first and c_key == "problem statement":
                    new_uniq.append("Problem Statement (Details)")
                    inserted_first = True
                # After 3-Month Prototype (column index 5 in original 8-col table)
                if not inserted_second and c_key == "3-month prototype":
                    new_uniq.append("Proposed Solution (Details)")
                    inserted_second = True
            
            new_header = "| " + " | ".join(new_uniq) + " |"
            result.append(new_header)
            i += 1
            
            # Separator line
            sep = lines[i]
            # Count how many dashes we need
            n_cols = len(new_uniq)
            sep_parts = ["---"] * n_cols
            new_sep = "| " + " | ".join(sep_parts) + " |"
            result.append(new_sep)
            i += 1
            
            # Data rows
            while i < len(lines) and lines[i].strip().startswith("|") and not lines[i].strip().startswith("|---"):
                row = lines[i]
                # Parse cells - handle complex content with pipes inside
                row_content = row.strip()
                if row_content.startswith("|"):
                    row_content = row_content[1:]
                if row_content.endswith("|"):
                    row_content = row_content[:-1]
                
                cells = [c.strip() for c in row_content.split("|")]
                
                # If we have more cells than expected (due to duplicates), deduplicate
                # Strip to unique content cells
                unique_cells = []
                seen_content = set()
                for c in cells:
                    key = c.strip().lower()
                    if key not in seen_content:
                        seen_content.add(key)
                        unique_cells.append(c)
                
                # Determine which cells correspond to which columns
                # Original: #(0), Problem Statement(1), Domain Type(2), Why Unsolved(3), Impact(4), 3-Month Prototype(5), First-Principles(6), Validation(7)
                # We want: #(0), Problem Statement(1), ProbDetail(new), Domain Type(2), Why(3), Impact(4), Prototype(5), SolDetail(new), Derivation(6), Validation(7)
                
                if len(unique_cells) >= 8:
                    num = unique_cells[0]
                    problem = unique_cells[1]
                    dtype_orig = unique_cells[2]
                    why = unique_cells[3]
                    impact = unique_cells[4]
                    proto = unique_cells[5]
                    deriv = unique_cells[6]
                    val = unique_cells[7]
                    
                    # Generate details
                    prob_detail = why
                    if not prob_detail.endswith("."):
                        prob_detail += "."
                    impact_clean = impact.replace("Human: ", "").replace("Planet: ", "").replace("Human/Planet: ", "")
                    prob_detail += f" This affects {impact_clean}."
                    
                    sol_detail = proto
                    if not sol_detail.endswith("."):
                        sol_detail += "."
                    sol_detail += f" Based on first-principles: {deriv.split('→')[0].strip() if '→' in deriv else deriv[:100]}."
                    
                    new_cells = [num, problem, prob_detail, dtype_orig, why, impact, proto, sol_detail, deriv, val]
                    new_row = "| " + " | ".join(new_cells) + " |"
                    result.append(new_row)
                else:
                    # Fallback: keep original
                    result.append(row)
                
                i += 1
            continue
        else:
            result.append(line)
            i += 1
    
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    print(f"Fixed: {filepath}")


for domain in DOMAINS:
    process_file(f"{ROOT}/{domain}")

print("Done")