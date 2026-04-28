import pandas as pd
import json

# 1. Logic for preference-based allocation
def get_alloc_value(row, tag_keys, flat_col):
    # Try to get from parsed JSON first
    tags = row['Parsed_Tags']
    for key in tag_keys:
        if key in tags and str(tags[key]).strip() not in ['', 'nan', '#VALUE!']:
            return tags[key]
    # Fallback to flat column
    fallback = str(row[flat_col]).strip()
    return fallback if fallback not in ['', 'nan', '#VALUE!'] else "Unallocated"

# 2. Status Determination
def get_tag_status(tags):
    found = 0
    if any(k in tags for k in ['application', 'Project']): found += 1
    if any(k in tags for k in ['environment', 'env']): found += 1
    if any(k in tags for k in ['business_unit', 'org']): found += 1
    
    if found == 3: return "Tagged"
    if found > 0: return "Partially Tagged"
    return "Untagged"