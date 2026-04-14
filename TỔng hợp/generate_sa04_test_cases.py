import pandas as pd
import os

# Data for Test Cases (21 columns)
columns = [
    "TC_ID", "BR_Ref", "URD_Ref", "Module", "Feature", "Title",
    "Type", "Category", "Priority", "Precondition",
    "Steps", "Expected", "Trace_ID", "Note",
    "Status R1", "Tester R1", "Date R1", "Status R2", "Tester R2", "Date R2", "Final Status"
]

tc_data = [
    [
        "SA04-BR-HAP-001", "BR_01, BR_04, BR_05", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra Thêm mới Nhóm quyền thành công khi nhập đủ các trường bắt buộc và chọn 1 vài quyền trong nhóm",
        "Happy", "Smoke", "P1", 
        "1. Người quản trị đăng nhập và có quyền.\n2. Ở màn hình Thêm mới Nhóm quyền.", 
        "1. Nhập trường ID nhóm quyền, Tên nhóm quyền hợp lệ chưa tồn tại.\n2. Tích chọn một vài phân quyền cụ thể trong 1 nhóm.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Lưu bản ghi nhóm quyền thành công, không qua duyệt bảo trì.\n(ii) UI: Form đóng thông báo 'Thêm mới Nhóm quyền thành công'.\n(iii) Trạng thái/Audit: Bản ghi lưu đổi trạng thái hiển thị trên lưới (Hoạt động/Saved). Sinh log Audit.\n(iv) Output: Không sinh message/file.",
        "BR01-BR04", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-BR-HAP-002", "BR_01, BR_04, BR_05", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra Thêm mới Nhóm quyền thành công khi tích chọn Toàn quyền",
        "Happy", "Smoke", "P1", 
        "1. Người quản trị đăng nhập và có quyền.\n2. Ở màn hình Thêm mới Nhóm quyền.", 
        "1. Nhập ID và Tên nhóm quyền hợp lệ chưa tồn tại.\n2. Tích chọn checkbox Toàn quyền cho phân nhóm.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Lưu bản ghi nhóm quyền thành công và ghi nhận toàn bộ các quyền đã chọn.\n(ii) UI: Form đóng thông báo 'Thêm mới Nhóm quyền thành công' màu xanh.\n(iii) Trạng thái/Audit: Bản ghi lưu thành công. Sinh log Audit.\n(iv) Output: Không.",
        "BR04-ALL", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-BR-NEG-001", "BR_01", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra hệ thống báo lỗi không cho lưu khi bỏ trống các trường bắt buộc",
        "Negative", "Regression", "P2", 
        "1. Người quản trị đăng nhập và có quyền.\n2. Ở màn hình Thêm mới Nhóm quyền.", 
        "1. Để trống một trong các trường bắt buộc (3a: ID nhóm quyền, 3b: Tên nhóm quyền, 3c: Quyền).\n2. Nhập các thông tin còn lại hợp lệ.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Hệ thống chặn không cho phép lưu bản ghi do vi phạm ràng buộc trống.\n(ii) UI: Form không tắt, focus và bôi đỏ viền ô lỗi (cảnh báo bắt buộc nhập).\n(iii) Trạng thái/Audit: Không tạo thay đổi, không sinh log.\n(iv) Output: Không sinh message/file.",
        "BR01-EMPTY", "Gộp các trường hợp: [3a: Bỏ trống ID nhóm quyền, 3b: Bỏ trống Tên nhóm quyền, 3c: Không chọn Quyền nào]", "", "", "", "", "", "", ""
    ],
    [
        "SA04-BR-NEG-002", "BR_03", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra hệ thống báo lỗi khi nhập trùng ID nhóm quyền đã tồn tại",
        "Negative", "Smoke", "P1", 
        "1. Tồn tại nhóm quyền có ID \"NQC01\".\n2. Người quản trị ở màn hình Thêm mới Nhóm quyền.", 
        "1. Nhập ID nhóm quyền là \"NQC01\".\n2. Nhập các trường khác hợp lệ chưa tồn tại.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Hệ thống chặn lưu vì ID nhóm quyền bị trùng.\n(ii) UI: Màn hình giữ nguyên, hiển thị popup/text báo lỗi 'ID nhóm quyền đã tồn tại'.\n(iii) Trạng thái/Audit: Không tạo thay đổi, không sinh log.\n(iv) Output: Không.",
        "BR03-DUP-ID", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-BR-NEG-003", "BR_03", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra hệ thống báo lỗi khi nhập trùng Tên nhóm quyền đã tồn tại",
        "Negative", "Regression", "P2", 
        "1. Tồn tại nhóm quyền có Tên \"Nhóm báo cáo\".\n2. Người quản trị ở màn hình Thêm mới Nhóm quyền.", 
        "1. Nhập Tên nhóm quyền là \"Nhóm báo cáo\".\n2. Nhập các trường khác hợp lệ chưa tồn tại.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Hệ thống chặn lưu vì Tên nhóm quyền bị trùng.\n(ii) UI: Màn hình giữ nguyên, hiển thị text báo lỗi 'Tên nhóm quyền đã tồn tại'.\n(iii) Trạng thái/Audit: Không tạo thay đổi, không sinh log.\n(iv) Output: Không.",
        "BR03-DUP-NAME", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-BR-HAP-003", "BR_02", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra hành vi hệ thống hủy lưu dữ liệu khi chọn nút Đóng",
        "Happy", "Regression", "P2", 
        "1. Người quản trị đăng nhập và có quyền.\n2. Mở màn hình Thêm mới Nhóm quyền.", 
        "1. Nhập bất kỳ thông tin nào vào form Thêm mới.\n2. Chọn nút Đóng.",
        "(i) Nghiệp vụ/Logic: Hủy thao tác nhập liệu, hệ thống không lưu thông tin vừa nhập.\n(ii) UI: Đóng form Thêm mới, trở về màn hình danh sách Nhóm quyền.\n(iii) Trạng thái/Audit: Không sinh bản ghi, không sinh log.\n(iv) Output: Không.",
        "BR02-CLOSE", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-001", "UI-FUNC.01", "SA.04", "SA04", "Thêm mới", 
        "Kiểm tra hiển thị màn hình Thêm mới Nhóm quyền từ danh sách",
        "Happy", "Regression", "P2", 
        "1. Đang ở màn hình danh sách Quản lý phân quyền.", 
        "1. Click vào nút 'Thêm mới'.",
        "(i) Nghiệp vụ/Logic: Gọi API lấy dữ liệu form thành công.\n(ii) UI: Hiển thị màn hình Thêm mới Nhóm quyền có đầy đủ các field: ID, Tên, danh sách Quyền, nút Xác nhận, Đóng.\n(iii) Trạng thái/Audit: Không thay đổi.\n(iv) Output: Không.",
        "UI-ADD-DISPLAY", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-002", "UI-FUNC.02", "SA.04", "SA04", "Sửa", 
        "Kiểm tra hiển thị thông tin và chỉnh sửa bản ghi Nhóm quyền",
        "Happy", "Smoke", "P1", 
        "1. Tồn tại 1 bản ghi Nhóm quyền.\n2. Đang ở màn hình Quản lý phân quyền.", 
        "1. Nhấn nút Sửa tại dòng bản ghi.\n2. Thay đổi giá trị Tên nhóm quyền và quyền hệ thống.\n3. Nhấn Xác nhận.",
        "(i) Nghiệp vụ/Logic: Cập nhật thông tin bản ghi thành công trong CSDL.\n(ii) UI: Bảng grid tải lại dòng tương ứng, hiển thị thông báo lưu thành công màu xanh.\n(iii) Trạng thái/Audit: Cập nhật bản ghi thành công. Sinh log Audit chỉnh sửa.\n(iv) Output: Không.",
        "UI-EDIT-SAVE", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-003", "UI-FUNC.03", "SA.04", "SA04", "Xem", 
        "Kiểm tra thông tin hiển thị chính xác ở màn hình Xem",
        "Happy", "Regression", "P2", 
        "1. Tồn tại 1 bản ghi Nhóm quyền.\n2. Đang ở màn hình Quản lý phân quyền.", 
        "1. Nhấn nút/icon Xem tại dòng bản ghi.\n2. Kiểm tra thông tin hiển thị.\n3. Nhấn Đóng.",
        "(i) Nghiệp vụ/Logic: Đọc đúng thông tin từ CSDL theo bản ghi đã chọn.\n(ii) UI: Hiển thị form Xem với các trường bị vô hiệu hóa (disabled). Nhấn Đóng tắt form.\n(iii) Trạng thái/Audit: Không sinh log hay đổi dữ liệu CSDL.\n(iv) Output: Không.",
        "UI-VIEW-DISPLAY", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-004", "UI-FUNC.04", "SA.04", "SA04", "Xóa", 
        "Kiểm tra loại bỏ (Xóa) bản ghi Nhóm quyền thành công",
        "Happy", "Smoke", "P1", 
        "1. Tồn tại 1 nhóm quyền không bị ràng buộc (không có user gán).\n2. Ở màn hình danh sách.", 
        "1. Nhấn Xóa tại dòng bản ghi.\n2. Xác nhận xóa trên popup hệ thống.",
        "(i) Nghiệp vụ/Logic: Xóa hoặc đánh dấu xóa bản ghi trong CSDL thành công.\n(ii) UI: Tải lại lưới dữ liệu, dòng tương ứng biến mất, thông báo xóa thành công bật lên.\n(iii) Trạng thái/Audit: Xóa thành công. Sinh log Audit xóa.\n(iv) Output: Không.",
        "UI-DEL-HAP", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-005", "UI-FUNC.05", "SA.04", "SA04", "Tìm kiếm", 
        "Kiểm tra kết quả hiển thị trên lưới khi Tìm kiếm theo tiêu chí có giá trị",
        "Happy", "Smoke", "P1", 
        "1. Tồn tại ít nhất 2 bản ghi nhóm quyền.\n2. Ở màn hình danh sách Quản lý phân quyền.", 
        "1. Nhập tiêu chí tìm kiếm hợp lệ (3a: Theo ID nhóm quyền, 3b: Theo Tên nhóm quyền).\n2. Nhấn nút Tìm kiếm.",
        "(i) Nghiệp vụ/Logic: Lấy đúng bộ dữ liệu khớp với tiêu chí tìm kiếm.\n(ii) UI: Bảng grid hiển thị các hàng kết quả khớp, bộ đếm trang cập nhật đúng.\n(iii) Trạng thái/Audit: Không đổi.\n(iv) Output: Không.",
        "UI-SEARCH", "Gộp các trường hợp: [3a: Tìm kiếm theo ID nhóm quyền, 3b: Tìm kiếm theo Tên nhóm quyền]", "", "", "", "", "", "", ""
    ],
    [
        "SA04-UI-006", "UI-FUNC.06", "SA.04", "SA04", "Tải xuống", 
        "Kiểm tra xuất file (Tải xuống) danh sách Nhóm quyền ra Excel",
        "Happy", "Regression", "P2", 
        "1. Đang ở màn hình danh sách có sẵn các bản ghi Nhóm quyền.", 
        "1. Nhấn nút Tải xuống.",
        "(i) Nghiệp vụ/Logic: Kết xuất dữ liệu hệ thống đang hiển thị tại màn hình ra file.\n(ii) UI: Hiển thị toast báo tải thành công, trình duyệt mở popup tải file.\n(iii) Trạng thái/Audit: Có thể sinh log Tải xuống.\n(iv) Output: File (.xlsx) chứa dữ liệu trùng khớp với các cột dữ liệu hiển thị hiện hành.",
        "UI-EXPORT", "", "", "", "", "", "", "", ""
    ],
    [
        "SA04-E2E-HAP-001", "UI-FUNC.01, UI-FUNC.05, UI-FUNC.03, UI-FUNC.02, UI-FUNC.06", "SA.04", "SA04", "E2E", 
        "Kiểm tra luồng E2E thêm mới, tìm kiếm, xem, sửa và xuất file tải xuống Nhóm quyền",
        "Integration", "Smoke", "P1", 
        "1. Người quản trị có đủ quyền thực hiện các thao tác quản lý phân quyền.", 
        "1. Ở tính năng quản lý phân quyền, click Thêm mới Nhóm quyền.\n2. Nhập thông tin bắt buộc, chọn quyền và Xác nhận.\n3. Nhập ID vừa tạo để Tìm kiếm trên danh sách.\n4. Click nút Xem để đối chiếu, sau đó Đóng.\n5. Click nút Sửa, cấp quyền mới, Xác nhận.\n6. Click Tải xuống.",
        "(i) Nghiệp vụ/Logic: Xử lý thành công toàn bộ chuỗi nghiệp vụ không lỗi, luồng dữ liệu thông suốt.\n(ii) UI: Chuyển hướng đúng, các form pop-up hiện đủ, báo xanh.\n(iii) Trạng thái/Audit: Sinh log audit tuần tự theo thao tác.\n(iv) Output: File excel có thể mở xem bình thường, nội dung khớp hiển thị thực tế.",
        "E2E-FULL-FLOW", "", "", "", "", "", "", "", ""
    ]
]

# Sheet 2: Dedup Log
dedup_cols = ["Mã TC gốc (Merged/Gộp)", "Nội dung gộp/Giảm tải", "Ghi chú"]
dedup_data = [
    ["SA04-BR-NEG-001", "Gộp 3 cases: Bỏ trống ID, Bỏ trống Tên, và Không chọn quyền nào, do kết quả Expectation (focus ô lỗi, báo đỏ) hoàn toàn giống nhau.", "Sử dụng 3a, 3b, 3c ở phần Step."],
    ["SA04-UI-005", "Gộp 2 cases: Tìm kiếm theo ID nhóm quyền và Tìm kiếm theo Tên nhóm quyền.", "Rút gọn để giảm số test case bị trùng lường."]
]

# Sheet 1: Coverage
cov_cols = ["Loại Rules/Chức năng", "Mã tham chiếu (Ref)", "Trạng thái Coverage", "Ghi chú"]
cov_data = [
    ["Business Rule", "BR_01", "Covered", "Tham chiếu bởi SA04-BR-HAP-001, SA04-BR-NEG-001, SA04-BR-HAP-002"],
    ["Business Rule", "BR_02", "Covered", "Tham chiếu bởi SA04-BR-HAP-003"],
    ["Business Rule", "BR_03", "Covered", "Tham chiếu bởi SA04-BR-NEG-002, SA04-BR-NEG-003"],
    ["Business Rule", "BR_04", "Covered", "Tham chiếu bởi SA04-BR-HAP-001, SA04-BR-HAP-002"],
    ["Business Rule", "BR_05", "Covered", "Tham chiếu bởi SA04-BR-HAP-001"],
    ["UI Function", "UI-FUNC.01", "Covered", "Chức năng Thêm mới: Tham chiếu bởi SA04-UI-001 và SA04-E2E-HAP-001"],
    ["UI Function", "UI-FUNC.02", "Covered", "Chức năng Sửa: Tham chiếu bởi SA04-UI-002 và SA04-E2E-HAP-001"],
    ["UI Function", "UI-FUNC.03", "Covered", "Chức năng Xem: Tham chiếu bởi SA04-UI-003 và SA04-E2E-HAP-001"],
    ["UI Function", "UI-FUNC.04", "Covered", "Chức năng Xóa: Tham chiếu bởi SA04-UI-004"],
    ["UI Function", "UI-FUNC.05", "Covered", "Chức năng Tìm kiếm: Tham chiếu bởi SA04-UI-005 và SA04-E2E-HAP-001"],
    ["UI Function", "UI-FUNC.06", "Covered", "Chức năng Tải xuống: Tham chiếu bởi SA04-UI-006 và SA04-E2E-HAP-001"]
]

df_tc = pd.DataFrame(tc_data, columns=columns)
df_dedup = pd.DataFrame(dedup_data, columns=dedup_cols)
df_cov = pd.DataFrame(cov_data, columns=cov_cols)

output_file = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/SA04_Test_Cases.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_cov.to_excel(writer, sheet_name="Coverage", index=False)
    df_dedup.to_excel(writer, sheet_name="Dedup_Log", index=False)
    df_tc.to_excel(writer, sheet_name="Test Cases", index=False)

print(f"File created successfully at {output_file}")
