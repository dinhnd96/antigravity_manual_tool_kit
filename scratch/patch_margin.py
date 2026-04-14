import re

file = 'scratch/generate_us02_qa_report_master.py'
with open(file, 'r') as f:
    content = f.read()

margin_patch = """
    # Set narrow margins & Landscape
    sections = doc.sections
    for section in sections:
        section.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
        # Swap width and height for landscape
        new_width, new_height = section.page_height, section.page_width
        section.page_width = new_width
        section.page_height = new_height
        
        # Set narrow margins (0.5 inches)
        section.top_margin = docx.shared.Inches(0.5)
        section.bottom_margin = docx.shared.Inches(0.5)
        section.left_margin = docx.shared.Inches(0.5)
        section.right_margin = docx.shared.Inches(0.5)
"""

if "section.orientation" not in content:
    # insert right after doc = docx.Document()
    content = re.sub(r'doc = docx.Document\(\)', r'doc = docx.Document()' + '\n' + margin_patch, content)
    
with open(file, 'w') as f:
    f.write(content)
print("✅ Python script patched for margins.")
