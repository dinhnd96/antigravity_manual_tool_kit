# -*- coding: utf-8 -*-
import docx
import os
import sys

# Ensure scripts folder is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from us06_reference_data import US06_REFERENCE_MAP

def update_references():
    source_file = "/Users/mac/antigravity-testing-kit/Tài liệu toàn hệ thống Profix/US1-10/US06_Part_C_TestCase_Coverage.docx"
    temp_output_file = "/Users/mac/antigravity-testing-kit/Tài liệu toàn hệ thống Profix/US1-10/US06_Part_C_TestCase_Coverage_Updated.docx"
    
    if not os.path.exists(source_file):
        print(f"Error: Source file not found at {source_file}")
        return False
        
    doc = docx.Document(source_file)
    updated_count = 0
    not_found_sc = []
    
    print("Starting update of references...")
    
    for t_idx, table in enumerate(doc.tables):
        # We need headers to find "Mã SC" and "Trích dẫn tài liệu"
        if len(table.rows) == 0:
            continue
            
        headers = [cell.text.strip() for cell in table.rows[0].cells]
        
        sc_col_idx = -1
        ref_col_idx = -1
        
        for idx, h in enumerate(headers):
            if "Mã SC" in h or h == "Mã":
                sc_col_idx = idx
            elif "Trích dẫn tài liệu" in h or "Reference" in h:
                ref_col_idx = idx
                
        if sc_col_idx != -1 and ref_col_idx != -1:
            print(f"Table {t_idx}: Found columns - Mã SC index {sc_col_idx}, Trích dẫn index {ref_col_idx}")
            for r_idx in range(1, len(table.rows)):
                row = table.rows[r_idx]
                sc_id = row.cells[sc_col_idx].text.strip()
                
                if not sc_id:
                    continue
                    
                if sc_id in US06_REFERENCE_MAP:
                    new_ref = US06_REFERENCE_MAP[sc_id]
                    # Check length rule
                    if len(new_ref) > 200:
                        print(f"Warning: Reference for {sc_id} exceeds 200 characters ({len(new_ref)} chars)")
                    
                    old_ref = row.cells[ref_col_idx].text.strip()
                    row.cells[ref_col_idx].text = new_ref
                    updated_count += 1
                else:
                    not_found_sc.append((sc_id, t_idx, r_idx))
                    
    doc.save(temp_output_file)
    print(f"\nUpdate completed! Saved to: {temp_output_file}")
    print(f"Total test case references updated: {updated_count}")
    
    if not_found_sc:
        print(f"\nWarning: The following SC IDs were found in document but have NO mapping in python data:")
        for sc_id, t, r in not_found_sc:
            print(f"  - {sc_id} (Table {t}, Row {r})")
            
    return True

if __name__ == "__main__":
    update_references()
