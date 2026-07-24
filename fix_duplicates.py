#!/usr/bin/env python3
"""Remove duplicated columns from markdown tables."""

import re

ROOT = "/Users/adarsh/Documents/research/futures-202606/problem-statements"
DOMAINS = [
    "energy-transition.md", "electronics-software.md", "biotech-health-longevity.md",
    "defence-space-advanced-manufacturing.md", "agri-water-urbanisation.md",
    "creative-taste-economy.md", "high-trust-services.md",
]

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    lines = content.split("\n")
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line has the duplicate pattern
        if "Problem Statement (Details) | Problem Statement (Details)" in line:
            # Fix header
            line = line.replace("Problem Statement (Details) | Problem Statement (Details)", "Problem Statement (Details)")
            i += 1
            # Fix separator if next line
            if i < len(lines) and "---" in lines[i]:
                sep = lines[i]
                parts = sep.split("|")
                if len(parts) >= 12:
                    # Remove one extra --- at positions corresponding to duplicate
                    # Just recount
                    sep = "|" + "---|" * 10
                lines[i] = sep
            # Fix data rows until end of table
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i]
                # Remove the extra cell - the duplicated part
                # Pattern: there's a duplicated cell after "Problem Statement (Details)"
                # Find the position of the second "Problem Statement (Details)" equivalent
                parts = row.split("|")
                if len(parts) >= 12:
                    # Remove the extra cell (position 3 in 0-indexed after splitting on |)
                    # After split, parts[0] is empty (before first |) or contains start
                    new_parts = parts[:3] + parts[4:]
                    row = "|".join(new_parts)
                # Now fix "Proposed Solution (Details)" duplicate
                # Count occurrences
                row = row.replace(" | **Low-cost", "| **Low-cost")  # temp fix, just rebuild
                lines[i] = row
                i += 1
            continue
        
        result.append(line)
        i += 1
    
    # Actually this approach is too fragile. Let me just do it right.
    # Re-read and do proper table parsing
    return result  # placeholder


# Simpler approach: just rebuild the files using a proper regex-based table parser
import csv
import io

def fix_tables_in_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Find all table blocks (lines starting with | that form contiguous blocks)
    lines = content.split("\n")
    new_lines = []
    
    in_table = False
    table_start = 0
    table_lines = []
    
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and "|" in stripped:
            if not in_table:
                in_table = True
                table_start = idx
                table_lines = [line]
            else:
                table_lines.append(line)
        else:
            if in_table:
                # Process the table block
                processed = process_table_block(table_lines)
                new_lines.extend(processed)
                in_table = False
                table_lines = []
            new_lines.append(line)
    
    if in_table:
        processed = process_table_block(table_lines)
        new_lines.extend(processed)
    
    with open(filepath, "w") as f:
        f.write("\n".join(new_lines))
    print(f"Fixed: {filepath}")


def process_table_block(table_lines):
    """Remove duplicate columns from a markdown table block."""
    if not table_lines:
        return table_lines
    
    # Parse
    header = table_lines[0]
    sep = table_lines[1] if len(table_lines) > 1 else ""
    data_rows = table_lines[2:] if len(table_lines) > 2 else []
    
    # Get header columns
    h = header.strip().strip("|")
    cols = [c.strip() for c in h.split("|")]
    
    # Detect and remove duplicates
    seen = []
    dupe_indices = []
    for i, c in enumerate(cols):
        key = c.replace("**", "").strip().lower()
        if key in seen:
            dupe_indices.append(i)
        else:
            seen.append(key)
    
    if not dupe_indices:
        return table_lines  # No duplicates
    
    # Fix header
    new_cols = [c for i, c in enumerate(cols) if i not in dupe_indices]
    new_header = "| " + " | ".join(new_cols) + " |"
    
    # Fix separator
    sep_cols = [s for i, s in enumerate(sep.strip().split("|")) if i not in dupe_indices]
    new_sep = "|".join(sep_cols)
    
    result = [new_header, new_sep]
    
    # Fix data rows
    for row in data_rows:
        r = row.strip()
        if not r.startswith("|"):
            result.append(row)
            continue
        cells = []
        # Parse cells properly
        r_content = r[1:] if r.startswith("|") else r
        r_content = r_content[:-1] if r_content.endswith("|") else r_content
        
        # Smart split: handle bold markers
        # Split by | but be careful
        cell_list = [c.strip() for c in r_content.split("|")]
        
        new_cell_list = [c for i, c in enumerate(cell_list) if i not in dupe_indices]
        # Pad if needed to match column count
        while len(new_cell_list) < len(new_cols):
            new_cell_list.append("")
        new_row = "| " + " | ".join(new_cell_list[:len(new_cols)]) + " |"
        result.append(new_row)
    
    return result


for domain in DOMAINS:
    fix_tables_in_file(f"{ROOT}/{domain}")

print("Done")