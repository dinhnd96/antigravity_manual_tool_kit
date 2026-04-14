import re

file = 'scratch/generate_us02_qa_report_master.py'
with open(file, 'r') as f:
    content = f.read()

# Biến đổi đoạn gán header:
patch = """
    from docx.shared import Inches, Cm
    # Set table width
    table.autofit = False
    table.allow_autofit = False

    # Define widths
    widths = [Cm(1.5), Cm(2.0), Cm(9.0), Cm(3.0), Cm(5.0), Cm(4.0)]
    
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].width = widths[i]
"""

if "widths =" not in content:
    content = re.sub(r'    for i, h in enumerate\(headers\):\n        hdr_cells\[i\].text = h\n        hdr_cells\[i\].paragraphs\[0\].runs\[0\].font.bold = True', patch.strip("\n"), content)
    
    # Also need to set width for all rows
    row_patch = """
        row_cells = table.add_row().cells
        for i, text in enumerate(row_data):
            row_cells[i].text = text
            row_cells[i].width = widths[i]
"""
    content = content.replace("        row_cells = table.add_row().cells\n        for i, text in enumerate(row_data):\n            row_cells[i].text = text", row_patch.strip('\n'))

with open(file, 'w') as f:
    f.write(content)
print("✅ Python script patched for table widths.")
