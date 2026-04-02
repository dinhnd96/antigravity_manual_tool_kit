import pandas as pd

# 1. Coverage Data
coverage_data = [
    ["TC theo BR", "BR_01", "COVERED", "2 TC (Happy/Negative)"],
    ["TC theo BR", "BR_02", "COVERED", "1 TC (Luồng Đóng không lưu)"],
    ["TC theo BR", "BR_03", "COVERED", "1 TC (Unique mã nhóm)"],
    ["TC theo BR", "BR_04", "COVERED", "1 TC (Logic filter cây SPDV theo tần suất/ngày thu)"],
    ["TC theo BR", "BR_05", "COVERED", "1 TC (Code phí duy nhất trong 1 nhóm)"],
    ["TC theo BR", "BR_06", "COVERED", "1 TC (Cấu hình Priority ghi Topic)"],
    ["TC chức năng UI", "UI-FUNC.01", "COVERED", "Thêm mới (UI flow)"],
    ["TC chức năng UI", "UI-FUNC.02", "COVERED", "Chọn mã phí từ cây SPDV"],
    ["TC chức năng UI", "UI-FUNC.03", "COVERED", "Sửa bản ghi"],
    ["TC chức năng UI", "UI-FUNC.04", "COVERED", "Xem bản ghi (Read-only)"],
    ["TC chức năng UI", "UI-FUNC.05", "COVERED", "Xóa bản ghi (Confirm)"],
    ["TC chức năng UI", "UI-FUNC.06", "COVERED", "Tìm kiếm/Lọc trên lưới"],
    ["TC chức năng UI", "UI-FUNC.07", "COVERED", "Tải xuống Excel"],
]
df_coverage = pd.DataFrame(coverage_data, columns=["Phân loại", "Mã Ref", "Trạng thái", "Ghi chú"])

# 2. Dedup Log Data
dedup_log_data = [
    ["Kiểm tra báo lỗi thiếu trường A, B, C...", "GỘP vào SA09-BR01-NEG-001", "Sử dụng biến thể Step 3a/3b/3c để tránh tạo 10 TC lặp lại cho từng trường."],
    ["Kiểm tra button Thêm mới/Mở form", "GỘP vào SA09-UI-01-EXPAND-001", "Tận dụng luồng UI bề mặt để kiểm tra trạng thái form."],
]
df_dedup = pd.DataFrame(dedup_log_data, columns=["Cặp Test Case có khả năng trùng", "Quyết định", "Lý do & Vị trí Note"])

# 3. Test Cases Data
test_cases_data = [
    ["SA09-BR01-HAP-001", "BR_01", "I.1.1.1", "SA.09", "Thêm mới", "Kiểm tra Thêm mới Nhóm code phí thành công với đầy đủ các trường bắt buộc", "Happy", "Smoke", "P1", "User Maker được phân quyền. Có sẵn Code phí định kỳ chưa thuộc nhóm nào.", "1. Chọn Thêm mới.\n2. Nhập: Mã nhóm, Tên nhóm, Tần suất, Ngày thu, Mức độ ưu tiên.\n3. Chọn các Code phí định kỳ từ danh sách.\n4. Nhấn Xác nhận.", "- Sau bước 4: Hệ thống báo 'Thêm mới job thành công'.\n- Bản ghi hiển thị trên lưới ở trạng thái [Chờ duyệt].\n- Audit log ghi nhận đúng Maker/Ngày tạo.", "BR01-CREATE-ALL", ""],
    ["SA09-BR01-NEG-002", "BR_01", "I.1.1.1", "SA.09", "Thêm mới", "Kiểm tra báo lỗi khi bỏ trống một trong các trường bắt buộc (*)", "Negative", "Regression", "P2", "Tại màn hình Thêm mới.", "1. Để trống một trong các trường: [Mã nhóm], [Tên nhóm], [Tần suất], [Ngày thu], [Mức độ ưu tiên].\n2. Nhập các trường còn lại.\n3. Nhấn Xác nhận.", "- Hệ thống không cho phép lưu.\n- Hiển thị cảnh báo lỗi đỏ dưới field tương ứng hoặc thông báo: 'Vui lòng nhập đầy đủ các trường bắt buộc'.", "BR01-MANDATORY-VALID", "Gộp các trường hợp: Bỏ trống từng field (*) theo variants 1a, 1b, 1c..."],
    ["SA09-BR02-UI-001", "BR_02", "I.1.1.1", "SA.09", "Thêm mới", "Kiểm tra hệ thống không lưu dữ liệu khi nhấn nút 'Đóng'", "UI", "Smoke", "P2", "Tại màn hình Thêm mới, đã nhập liệu một phần.", "1. Nhập thông tin Mã nhóm, Tên nhóm.\n2. Nhấn nút 'Đóng' hoặc icon (X) góc form.", "- Form đóng lại và quay về màn hình danh sách chính.\n- Không có bản ghi mới nào được sinh ra trên lưới danh sách.", "BR02-CANCEL-ACTION", ""],
    ["SA09-BR03-NEG-001", "BR_03", "I.1.1.1", "SA.09", "Thêm mới", "Kiểm tra báo lỗi khi nhập Mã nhóm Code phí đã tồn tại", "Negative", "Regression", "P2", "Đã có Mã nhóm 'FIXED_001' tồn tại trong hệ thống.", "1. Tại màn hình thêm mới, nhập Mã nhóm = 'FIXED_001'.\n2. Nhập đầy đủ các thông tin khác hợp lệ.\n3. Nhấn Xác nhận.", "- Hệ thống kiểm tra ID duy nhất.\n- Báo lỗi: 'Mã nhóm Code phí đã tồn tại, vui lòng kiểm tra lại'.", "BR03-UNIQUE-CODE", ""],
    ["SA09-BR04-HAP-001", "BR_04", "I.1.1.1", "SA.09", "Cây SPDV", "Kiểm tra logic lọc Code phí trên cây SPDV theo Tần suất và Ngày thu", "Happy", "Regression", "P2", "Tại màn hình thêm mới/sửa. Có các mã phí khác nhau về Tần suất/Loại tính phí trong hệ thống.", "1. Chọn Tần suất = 'Tháng', Ngày thu = '01'.\n2. Click chọn/mở Cây SPDV để xem danh sách Code phí.", "- Cây SPDV chỉ hiển thị các Code phí thỏa mãn đồng thời:\n+ Loại tính phí = 'Định kỳ'.\n+ Có Tần suất/Ngày thu tương ứng với giá trị đã chọn ở Bước 1.", "BR04-FILTER-LOGIC", ""],
    ["SA09-BR05-NEG-001", "BR_05", "I.1.1.1", "SA.09", "Thêm/Sửa", "Kiểm tra báo lỗi khi cố tình thêm một Code phí đã thuộc nhóm khác", "Negative", "Regression", "P2", "Code phí 'FEE_SA01' đã được gán cho Nhóm A. Đang mở màn hình thêm mới Nhóm B.", "1. Thao tác chọn Code phí 'FEE_SA01' từ cây SPDV hoặc danh sách.\n2. Nhấn Xác nhận.", "- Hệ thống báo lỗi logic: 'Code phí [FEE_SA01] đã thuộc Nhóm phí khác, không thể gán vào nhóm này'.", "BR05-ONE-CODE-ONLY", ""],
    ["SA09-BR06-HAP-001", "BR_06", "I.1.1.1", "SA.09", "Priority", "Kiểm tra cấu hình mức độ ưu tiên (Priority) phục vụ ghi tin Topic", "Happy", "Integration", "P2", "Hệ thống có nhiều nhóm code phí định kỳ đến hạn thu trong cùng 1 ngày.", "1. Cấu hình Nhóm phí A: Priority=1, Nhóm phí B: Priority=2.\n2. Lưu và Duyệt.\n3. Đến ngày thu phí, kiểm tra thứ tự ghi tin vào Topic trả ra.", "- Hệ thống ghi tin theo thứ tự ưu tiên tăng dần (1 rồi đến 2).\n- Trường dữ liệu priority trong message Topic đúng với cấu hình.", "BR06-PRIORITY-QUEUE", ""],
    ["SA09-UI-01-BASIC-001", "UI-FUNC.01", "I.1.1.1", "SA.09", "Tìm kiếm", "Kiểm tra giao diện tìm kiếm và xóa bộ lọc (Clear Filter)", "UI", "Regression", "P3", "Tại màn hình danh sách chính.", "1. Nhập từ khóa vào ô Tìm kiếm theo Tên nhóm.\n2. Nhấn 'Tìm kiếm'.\n3. Nhấn 'Làm mới' (Clear).", "- Bước 2: Lưới chỉ hiển thị các bản ghi có tên chứa từ khóa.\n- Bước 3: Các ô filter về trống, lưới hiển thị lại toàn bộ bản ghi.", "UI-LIST-FILTER", ""],
    ["SA09-UI-04-VIEW-001", "UI-FUNC.04", "I.1.1.1", "SA.09", "Xem", "Kiểm tra màn hình Xem chi tiết bản ghi (Chế độ Read-only)", "UI", "Regression", "P3", "Đã có sẵn bản ghi trên lưới.", "1. Click icon 'Xem' (con mắt) tại 1 bản ghi.\n2. Thao tác nhập liệu vào các field.", "- Form Xem hiển thị đúng thông tin của bản ghi.\n- BẮT BUỘC: Tất cả các field ở trạng thái Disable (mờ), không cho phép sửa đổi dữ liệu.", "UI-VIEW-READONLY", ""],
    ["SA09-UI-07-EXCEL-001", "UI-FUNC.07", "I.1.1.1", "SA.09", "Xuất Excel", "Kiểm tra chức năng Tải xuống danh sách nhóm code phí", "Report", "Regression", "P3", "Lưới đang hiển thị dữ liệu sau khi filter.", "1. Chọn nút 'Tải xuống' / 'Xuất Excel'.\n2. Mở file excel vừa tải.", "- File tải về đúng format (.xlsx).\n- Nội dung file khớp 100% với dữ liệu hiển thị trên lưới tại thời điểm tải (bao gồm cả các bản ghi đã filter).", "UI-EXPORT-EXCEL", ""],
]
columns_tc = ["TC_ID", "BR_Ref", "URD_Ref", "Module", "Feature", "Title", "Type", "Category", "Priority", "Precondition", "Steps", "Expected", "Trace_ID", "Note"]
df_test_cases = pd.DataFrame(test_cases_data, columns=columns_tc)

# Write to Excel
output_file = "/Users/mac/antigravity-testing-kit/Test_Cases_SA09_Quan_Ly_Nhom_Code_Phi.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_coverage.to_excel(writer, sheet_name="Coverage", index=False)
    df_dedup.to_excel(writer, sheet_name="Dedup_Log", index=False)
    df_test_cases.to_excel(writer, sheet_name="TestCases", index=False)

# Optional: Adding column width to TestCases for readability
from openpyxl.utils import get_column_letter
workbook = writer.book
worksheet = workbook["TestCases"]
column_widths = [15, 10, 10, 10, 15, 40, 10, 10, 10, 30, 50, 50, 15, 30]
for i, width in enumerate(column_widths):
    worksheet.column_dimensions[get_column_letter(i+1)].width = width

workbook.save(output_file)
print(f"File saved successfully at {output_file}")
