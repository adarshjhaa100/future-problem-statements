#!/usr/bin/env python3
"""Add 'Problem Statement (Details)' and 'Proposed Solution (Details)' columns to all tables."""

import re
import os

DOMAINS = [
    "energy-transition.md",
    "electronics-software.md",
    "biotech-health-longevity.md",
    "defence-space-advanced-manufacturing.md",
    "agri-water-urbanisation.md",
    "creative-taste-economy.md",
    "high-trust-services.md",
]
ROOT = "/Users/adarsh/Documents/research/futures-202606/problem-statements"


def generate_details(why_unsolved, impact, prototype, derivation):
    """Generate detailed Problem Statement and Proposed Solution from existing columns."""
    # Problem Statement Details: combine Why Unsolved + Impact
    problem_detail = why_unsolved.strip()
    if not problem_detail.endswith("."):
        problem_detail += "."
    impact_clean = impact.strip()
    if impact_clean:
        if not impact_clean.startswith("Human") and not impact_clean.startswith("Planet") and not impact_clean.startswith("Human/Planet"):
            problem_detail += f" {impact_clean}"
        else:
            problem_detail += f" Impact: {impact_clean}"
    if not problem_detail.endswith("."):
        problem_detail += "."

    # Proposed Solution Details: combine Prototype + Derivation
    proto_clean = prototype.strip()
    deriv_clean = derivation.strip()
    if proto_clean and deriv_clean:
        solution_detail = f"{proto_clean}. {deriv_clean}"
    elif proto_clean:
        solution_detail = proto_clean
    else:
        solution_detail = deriv_clean
    if not solution_detail.endswith("."):
        solution_detail += "."

    return problem_detail, solution_detail


def process_table_lines(lines, start_idx, end_idx):
    """Process a markdown table from start_idx to end_idx, adding 2 new columns."""
    new_lines = list(lines)
    
    # The header row
    header = new_lines[start_idx]
    # Remove leading/trailing |
    header_content = header.strip().strip("|")
    cols = [c.strip() for c in header_content.split("|")]
    
    # Column indices: # (0), Problem Statement (1), Domain Type (2), Why Unsolved (3), Impact (4), 3-Month Prototype (5), First-Principles (6), Validation (7)
    # Insert new columns after Impact (index 4) and after 3-Month Prototype (index 5)
    # New order: #, Problem Statement, Domain Type, Why Unsolved, Impact, Problem Statement (Details), Proposed Solution (Details), 3-Month Prototype, First-Principles, Validation
    # Actually let me re-read the user's request: "add 2 columns which explain the Problem Statement and Proposed solution in Details"
    # So insert "Problem Statement (Details)" after the existing short "Problem Statement" column, 
    # and "Proposed Solution (Details)" after "3-Month Prototype"
    
    new_col_names = []
    for i, c in enumerate(cols):
        new_col_names.append(c)
        if i == 1:  # After Problem Statement
            new_col_names.append("Problem Statement (Details)")
        if i == 5:  # After 3-Month Prototype
            new_col_names.append("Proposed Solution (Details)")
    
    new_header = "| " + " | ".join(new_col_names) + " |"
    new_lines[start_idx] = new_header
    
    # Separator line
    sep_line = new_lines[start_idx + 1]
    sep_cols = sep_line.strip().split("|")
    # Calculate how many separator columns we need
    new_sep_cols = []
    col_idx = 0
    for i, s in enumerate(sep_cols):
        if i == 0:
            new_sep_cols.append(s)
            continue
        new_sep_cols.append(s)
        # After Problem Statement column (index 1 in sep terms = after first |)
        if col_idx == 1:
            new_sep_cols.append("---")
        # After 3-Month Prototype column (index 5 in sep terms)
        if col_idx == 5:
            new_sep_cols.append("---")
        col_idx += 1
    new_sep = "|".join(new_sep_cols)
    new_lines[start_idx + 1] = new_sep
    
    # Data rows
    for row_idx in range(start_idx + 2, end_idx):
        row = new_lines[row_idx]
        if not row.strip().startswith("|"):
            continue
        row_content = row.strip().strip("|")
        cells = [c.strip() for c in row_content.split("|")]
        
        # Expected: 8 cells (#, Problem, Type, Why, Impact, Prototype, Derivation, Validation)
        if len(cells) < 8:
            continue
        
        num = cells[0]
        problem = cells[1]
        dtype = cells[2]
        why = cells[3]
        impact = cells[4]
        prototype = cells[5]
        derivation = cells[6]
        validation = cells[7]
        
        prob_detail, sol_detail = generate_details(why, impact, prototype, derivation)
        
        # Rebuild with new columns: #, Problem, ProbDetail, Type, Why, Impact, Prototype, SolDetail, Derivation, Validation
        new_cells = [num, problem, prob_detail, dtype, why, impact, prototype, sol_detail, derivation, validation]
        new_row = "| " + " | ".join(new_cells) + " |"
        new_lines[row_idx] = new_row
    
    return new_lines


def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    lines = content.split("\n")
    
    # Find table boundaries: lines starting with "| # |"
    i = 0
    result = list(lines)
    while i < len(result):
        line = result[i]
        # Detect table start: a line that starts with "| # |" or matches the header pattern
        if line.strip().startswith("| # ") and "|" in line:
            # Find the separator line
            if i + 1 < len(result) and "---" in result[i + 1]:
                # Find end of table (next blank line or end of section)
                end = i + 2
                while end < len(result) and result[end].strip().startswith("|"):
                    end += 1
                # Process this table
                result = process_table_lines(result, i, end)
                i = end
                continue
        i += 1
    
    with open(filepath, "w") as f:
        f.write("\n".join(result))
    print(f"Updated: {os.path.basename(filepath)}")


for domain in DOMAINS:
    filepath = os.path.join(ROOT, domain)
    process_file(filepath)

# Process summary separately (different format - abbreviated table)
print("Done processing domain files.")