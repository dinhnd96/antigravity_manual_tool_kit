
import pandas as pd
import re
import os
import traceback
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# Configuration
TEST_CASE_DIR = "Test case"
TARGET_FILE   = "TC_Management_ProfiX.xlsx"

# Colors
DARK_BLUE   = "1F3864"
MID_BLUE    = "2E75B6"
LIGHT_BLUE  = "D6E4F7"
WHITE       = "FFFFFF"
PASS_GREEN  = "70AD47"
FAIL_RED    = "FF0000"

TC_HEADERS = [
    "TC_ID", "Module", "Feature", "Title", "Type", "Category", "Priority", 
    "Precondition", "Steps", "Expected", "URD_Ref", "BR_Ref", "Trace_ID", "Note",
    "Status R1", "Tester R1", "Date R1", 
    "Status R2", "Tester R2", "Date R2", 
    "Final Status"
]

STATUS_OPTIONS = '"Pass,Fail,Doing,Blocked,N/A"'
TESTER_OPTIONS = '"Định,Thanh,Vân Anh,Hiệp"'

def thin_border():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

def style_header_row(ws, row_num, col_count, bg_color=MID_BLUE, font_color=WHITE):
    fill = PatternFill("solid", fgColor=bg_color)
    for col in range(1, col_count + 1):
        cell = ws.cell(row=row_num, column=col)
        cell.fill = fill
        cell.font = Font(bold=True, color=font_color, size=11)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border()

def clean_sheet_name(filename):
    match = re.search(r'(II\.\d+\.\d+\.\d+\.\d+|II\.\d+\.\d+\.\d+|II\.\d+\.\d+|PR\.\d+|OT\.\d+)', filename)
    name = match.group(1) if match else filename.replace(".xlsx", "")[:31]
    return name[:31]

def robust_format_content(text):
    if not isinstance(text, str): return text
    # Clean redundant numbering
    lines = text.split('\n')
    cleaned = []
    for l in lines:
        p = re.sub(r'^\d+[\.\)]\s*', '', l).strip()
        if re.match(r'^\d+$', p) or not p: continue
        cleaned.append(p)
    
    full = ' '.join(cleaned)
    # Split by dot+space or semicolon
    parts = re.split(r'[;]|\.\s+', full)
    final = []
    for pt in parts:
        pt = pt.strip()
        if pt:
            if not pt.endswith('.'): pt += '.'
            final.append(pt)
    return '\n'.join([f"{i}. {p}" for i, p in enumerate(final, 1)])

def build_management_workbook():
    if not os.path.exists(TEST_CASE_DIR):
        print(f"Lỗi: Không tìm thấy thư mục '{TEST_CASE_DIR}'")
        return

    print("--- Đang bắt đầu đồng bộ dữ liệu ---")
    wb = Workbook()
    ws_dash = wb.active
    ws_dash.title = "📊 Dashboard"
    ws_daily = wb.create_sheet("📅 Daily Tracking")

    files = sorted([f for f in os.listdir(TEST_CASE_DIR) if f.endswith(".xlsx") and not f.startswith("~$")])
    tc_sheets = []
    used_names = set()

    for f in files:
        full_path = os.path.join(TEST_CASE_DIR, f)
        base_name = clean_sheet_name(f)
        
        # Ensure unique names
        sheet_name = base_name
        counter = 1
        while sheet_name in used_names:
            sheet_name = f"{base_name[:28]}_{counter}"
            counter += 1
        used_names.add(sheet_name)
        tc_sheets.append(sheet_name)

        print(f"Đang xử lý: {f} -> Sheet: {sheet_name}")
        try:
            ws = wb.create_sheet(sheet_name)
            ws.merge_cells(f"A1:{get_column_letter(len(TC_HEADERS))}1")
            ws["A1"].value = f"TEST CASES — {f.replace('.xlsx', '')}"
            ws["A1"].font = Font(bold=True, size=13, color=WHITE)
            ws["A1"].fill = PatternFill("solid", fgColor=DARK_BLUE)
            ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
            
            for j, h in enumerate(TC_HEADERS, 1): ws.cell(row=2, column=j, value=h)
            style_header_row(ws, 2, len(TC_HEADERS))
            
            df = pd.read_excel(full_path)
            for i, row in df.iterrows():
                row_num = i + 3
                for j, header in enumerate(TC_HEADERS, 1):
                    val = row.get(header, "")
                    if header in ['Precondition', 'Steps', 'Expected']:
                        val = robust_format_content(val)
                    if header == "Final Status":
                        val = f'=IF(R{row_num}<>"", R{row_num}, O{row_num})'
                    
                    c = ws.cell(row=row_num, column=j, value=val)
                    c.border = thin_border()
                    c.alignment = Alignment(vertical="top", wrap_text=True)
                    if i % 2 == 1: c.fill = PatternFill("solid", fgColor=LIGHT_BLUE)

            for j, h in enumerate(TC_HEADERS, 1):
                ws.column_dimensions[get_column_letter(j)].width = 50 if h in ['Precondition', 'Steps', 'Expected', 'Title'] else 18

            dv_status = DataValidation(type="list", formula1=STATUS_OPTIONS, allow_blank=True)
            dv_tester = DataValidation(type="list", formula1=TESTER_OPTIONS, allow_blank=True)
            max_r = ws.max_row + 10
            dv_status.sqref = f"O3:O{max_r} R3:R{max_r}"
            dv_tester.sqref = f"P3:P{max_r} S3:S{max_r}"
            ws.add_data_validation(dv_status)
            ws.add_data_validation(dv_tester)
        except Exception:
            print(f"Lỗi khi xử lý file {f}:")
            traceback.print_exc()

    # Dashboard Logic
    ws_dash.merge_cells("A1:G1")
    ws_dash["A1"].value = "📊 QA DASHBOARD — PROFIX"
    ws_dash["A1"].font = Font(bold=True, size=14, color=WHITE)
    ws_dash["A1"].fill = PatternFill("solid", fgColor=DARK_BLUE)
    ws_dash["A1"].alignment = Alignment(horizontal="center")
    
    headers = ["Sheet Name", "Total TCs", "✅ Pass", "❌ Fail", "🟠 Blocked", "Doing", "Pass Rate (%)"]
    for j, h in enumerate(headers, 1): ws_dash.cell(row=3, column=j, value=h)
    style_header_row(ws_dash, 3, len(headers))
    
    for i, sname in enumerate(tc_sheets, 4):
        ws_dash.cell(row=i, column=1, value=sname).border = thin_border()
        ws_dash.cell(row=i, column=2, value=f'=COUNTA(\'{sname}\'!A:A)-2').border = thin_border()
        ws_dash.cell(row=i, column=3, value=f'=COUNTIF(\'{sname}\'!U:U,"Pass")').border = thin_border()
        ws_dash.cell(row=i, column=4, value=f'=COUNTIF(\'{sname}\'!U:U,"Fail")').border = thin_border()
        ws_dash.cell(row=i, column=7, value=f'=IFERROR(ROUND(C{i}/B{i}*100,1),0)').border = thin_border()

    wb.save(TARGET_FILE)
    print(f"--- HOÀN THÀNH: Đã cập nhật {TARGET_FILE} ---")

if __name__ == "__main__":
    build_management_workbook()
