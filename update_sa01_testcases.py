import openpyxl
from openpyxl.styles import Alignment

file_path = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/SA01_Đăng nhập.xlsx"
wb = openpyxl.load_workbook(file_path)
ws = wb["TestCases"]

row_to_delete = None

# Update existing rows
for idx, row in enumerate(ws.iter_rows(min_row=2), start=2):
    if not row[0].value: 
        continue
    
    tc_id = str(row[0].value)
    
    # 1. Update Title and Expected of SA01-HAPPY-001
    if tc_id == "SA01-HAPPY-001":
        ws.cell(row=idx, column=6).value = "Đăng nhập thành công → Hệ thống điều hướng về Dashboard hoặc màn hình phiên trước"
        ws.cell(row=idx, column=12).value = "(i) Nghiệp vụ: Hệ thống xác thực thành công.\n(ii) UI: Chuyển hướng đến màn hình Trang chủ (Dashboard) hoặc màn hình ở phiên đăng nhập trước.\n(iii) Trạng thái/Log: Trạng thái tài khoản bình thường, ghi log Security Audit đăng nhập thành công."
    
    # 2. Tách Expected 4 lớp cho SA01-HAPPY-007
    if tc_id == "SA01-HAPPY-007":
        ws.cell(row=idx, column=12).value = "(i) Nghiệp vụ: Cookie/Session được lưu phía client.\n(ii) UI: Tên đăng nhập được tự động điền khi mở lại trang login.\n(iii) Trạng thái/Log: Phụ thuộc config Cookie."
        
    # 3. Thêm lớp (i) Nghiệp vụ cho SA01-UI-008
    if tc_id == "SA01-UI-008":
        ws.cell(row=idx, column=12).value = "(i) Nghiệp vụ: Giá trị mật khẩu thực tế không bị thay đổi khi bật/tắt hiển thị.\n(ii) UI: Mật khẩu hiển thị ở dạng text khi bật và dạng dấu chấm/sao khi ẩn; Icon thay đổi trạng thái."

    # Highlight FLOW-011 cho deletion
    if tc_id == "SA01-FLOW-011":
        row_to_delete = idx
        
    # Thêm Backlog prefix cho SA01-SECURITY-012
    if tc_id == "SA01-SECURITY-012":
        ws.cell(row=idx, column=6).value = "[BACKLOG] " + str(ws.cell(row=idx, column=6).value)
        ws.cell(row=idx, column=9).value = "Pending"

# Xóa TC trùng lặp SA01-FLOW-011
if row_to_delete:
    ws.delete_rows(row_to_delete)

# Thêm TC mới cho gap BR_03
ws.append([
    "SA01-NEG-016", # TC_ID
    "BR_03",        # BR_Ref
    "II.5.4.1",     # URD_Ref
    "SA.01",        # Module
    "Đăng nhập",    # Feature
    "Kiểm tra khi không tích chọn Ghi nhớ mật khẩu", # Title
    "Negative",     # Type
    "Regression",   # Category
    "P2",           # Priority
    "-",            # Precondition
    "1. Nhập Username/Password hợp lệ.\n2. Không tích chọn 'Ghi nhớ'.\n3. Đăng nhập thành công.\n4. Đăng xuất, tắt Browser, mở lại trang đăng nhập.", # Steps
    "(i) Nghiệp vụ: Hệ thống không lưu cookie ghi nhớ đăng nhập.\n(ii) UI: Màn hình đăng nhập hiển thị với các trường thông tin trống.", # Expected
    "SA01-NEG-016", # Trace_ID
    "Bổ sung từ kết quả review QA" # Note
])

# Re-align items
for row in ws.iter_rows(min_row=2):
    for cell in row:
        if cell.value:
            cell.alignment = Alignment(wrap_text=True, vertical='top')

wb.save(file_path)
print("SA01 Test cases updated successfully.")
