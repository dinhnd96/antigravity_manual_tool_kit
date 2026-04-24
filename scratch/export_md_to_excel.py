import pandas as pd
import os

md_path = "/Users/mac/.gemini/antigravity/brain/8c7d2c67-5d54-4f86-921e-2832ca47a5b7/artifacts/US01_Analysis_Report_Final_V4.md"
out_path = "/Users/mac/antigravity-testing-kit/artifacts/US01_Analysis_Report_Final_V4.xlsx"

with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

tables = []
current_table = []
in_table = False

for line in lines:
    stripped = line.strip()
    if stripped.startswith('|') and stripped.endswith('|'):
        in_table = True
        current_table.append(stripped)
    else:
        if in_table:
            tables.append(current_table)
            current_table = []
            in_table = False

if in_table:
    tables.append(current_table)

def parse_table(table_lines):
    if not table_lines or len(table_lines) < 3:
        return None
    headers = [col.strip() for col in table_lines[0].strip('|').split('|')]
    data = []
    for row in table_lines[2:]:
        data.append([col.strip() for col in row.strip('|').split('|')])
    return pd.DataFrame(data, columns=headers)

if tables:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
        if len(tables) > 0:
            df1 = parse_table(tables[0])
            if df1 is not None:
                df1.to_excel(writer, sheet_name='Test Case Matrix', index=False)
        if len(tables) > 1:
            df2 = parse_table(tables[1])
            if df2 is not None:
                df2.to_excel(writer, sheet_name='Q&A for BA', index=False)
    print(f"Exported successfully to {out_path}")
else:
    print("No tables found.")
