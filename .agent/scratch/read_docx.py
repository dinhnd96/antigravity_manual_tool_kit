import zipfile
import xml.etree.ElementTree as ET
import sys

def docx_to_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespace for docx
            namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_parts = []
            for paragraph in tree.findall('.//w:p', namespace):
                paragraph_text = []
                for run in paragraph.findall('.//w:r', namespace):
                    for text in run.findall('.//w:t', namespace):
                        if text.text:
                            paragraph_text.append(text.text)
                text_parts.append("".join(paragraph_text))
            
            return "\n".join(text_parts)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(docx_to_text(sys.argv[1]))
