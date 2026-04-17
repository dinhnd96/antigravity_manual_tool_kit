import xml.etree.ElementTree as ET
import os

def extract_text_from_xml(xml_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    output = []
    
    # Iterate through all elements to preserve order
    for elem in root.iter():
        if elem.tag.endswith('p'): # Paragraph
            text = "".join([t.text for t in elem.findall('.//w:t', ns) if t.text])
            if text:
                output.append(text)
        elif elem.tag.endswith('tbl'): # Table
            output.append("\n[TABLE START]")
            for row in elem.findall('.//w:tr', ns):
                cells = []
                for cell in row.findall('.//w:tc', ns):
                    cell_text = "".join([t.text for t in cell.findall('.//w:t', ns) if t.text])
                    cells.append(cell_text.strip())
                output.append(" | ".join(cells))
            output.append("[TABLE END]\n")
            
    return "\n".join(output)

if __name__ == "__main__":
    xml_file = "US14_temp/word/document.xml"
    if os.path.exists(xml_file):
        text = extract_text_from_xml(xml_file)
        with open("US14_content.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Success: Content extracted to US14_content.txt")
    else:
        print("Error: document.xml not found")
