import pandas as pd
import xlsxwriter
import re
import os

# 1. Define Test Cases Data
tc_data = [
    # ==========================================
    # Lớp 1: E2E Integration Luồng nghiệp vụ
    # ==========================================
    {
        'TC_ID': 'SA03-E2E-HAP-001',
        'Module': 'SA03',
        'Feature': 'Tổng hợp',
        'Title': 'Kiểm tra luồng Thêm mới, Tìm kiếm, Sửa và Export người dùng thành công',
        'Type': 'Integration',
        'Category': 'Smoke',
        'Priority': 'P1',
        'Precondition': '1. Người quản trị đã đăng nhập và được phần quyền quản lý người dùng.',
        'Steps': '1. Nhập thông tin hợp lệ tại form Thêm mới và Xác nhận.\n2. Thực hiện Tìm kiếm với User vừa tạo.\n3. Xem thông tin trên lưới và nhấn icon Sửa (bánh răng) tại dòng dữ liệu.\n4. Sửa Trạng thái/Nhóm quyền rồi lưu lại.\n5. Tải xuống danh sách hiện tại.',
        'Expected': '(i) Nghiệp vụ/Logic: Luồng dữ liệu xuyên suốt được xử lý thành công, thông tin lưu toàn vẹn.\n(ii) UI: Chuyển đổi màn hình trơn tru, hiển thị các popup báo thành công.\n(iii) Trạng thái/Audit: Ghi nhận log khởi tạo và chỉnh sửa đầy đủ.\n(iv) Output: Xuất file Excel chứa user vừa thao tác.',
        'URD_Ref': 'SA.03',
        'BR_Ref': 'UI-FUNC.01, UI-FUNC.04, UI-FUNC.06',
        'Trace_ID': 'E2E-001',
        'Note': ''
    },
    
    # ==========================================
    # Lớp 2: Business Rules (Thêm Mới & Sửa)
    # ==========================================
    {
        'TC_ID': 'SA03-BR-NEG-001',
        'Module': 'SA03',
        'Feature': 'Thêm mới',
        'Title': 'Kiểm tra chặn lưu người dùng khi username đã tồn tại (Duy nhất)',
        'Type': 'Negative',
        'Category': 'Regression',
        'Priority': 'P1',
        'Precondition': '1. Tồn tại sẵn 1 người dùng với User: "quan.nguyen" trong hệ thống.\n2. Ở màn hình Thêm thông tin người dùng.',
        'Steps': '1. Nhập thông tin bắt buộc, trong đố trường "User" nhập "quan.nguyen".\n2. Nhấn "Xác nhận".',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống chặn thêm mới do trùng khóa duy nhất User (BR_02).\n(ii) UI: Cảnh báo "User đã tồn tại" hiển thị dưới trường nhập liệu hoặc popup.\n(iii) Trạng thái/Audit: Không sinh thông tin lưu DB.\n(iv) Output: Không.',
        'URD_Ref': 'SA.03',
        'BR_Ref': 'BR_02',
        'Trace_ID': 'BR-02-DUP',
        'Note': ''
    },
    {
        'TC_ID': 'SA03-BR-HAP-002',
        'Module': 'SA03',
        'Feature': 'Thêm mới',
        'Title': 'Kiểm tra lưu người dùng thành công và không qua duyệt (Trạng thái Active)',
        'Type': 'Happy',
        'Category': 'Smoke',
        'Priority': 'P1',
        'Precondition': '1. User Quản trị viên đang ở màn hình Thêm mới.',
        'Steps': '1. Nhập User (VD: "tu.nguyen"), tên hiển thị, khối, phòng ban, email, số điện thoại hợp lệ.\n2. Chọn Nhóm quyền và Trạng thái "Hoạt động".\n3. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: Lưu người dùng thành công, bản ghi có hiệu lực ngay theo quy trình quản trị (BR_03).\n(ii) UI: Form thêm mới đóng, quay về màn hình danh sách và hiện thông báo "thêm mới người dùng thành công".\n(iii) Trạng thái/Audit: Sinh 1 bản ghi với Trạng thái = Active / Hoạt động (BR_01). Có log Audit tạo mới.\n(iv) Output: Không.',
        'URD_Ref': 'SA.03',
        'BR_Ref': 'BR_01, BR_03',
        'Trace_ID': 'BR-03-HAP',
        'Note': ''
    },
    {
        'TC_ID': 'SA03-BR-HAP-003',
        'Module': 'SA03',
        'Feature': 'Thêm mới/Sửa',
        'Title': 'Kiểm tra bảng phân quyền hiển thị theo nhóm ở chế độ Read-Only',
        'Type': 'Happy',
        'Category': 'Regression',
        'Priority': 'P2',
        'Precondition': '1. Đang ở màn hình Thêm Mới hoặc Sửa thông tin người dùng.',
        'Steps': '1. Click combo box "Nhóm quyền" và trỏ tới nhóm "Checker".\n2. Nỗ lực click chọn/bỏ chọn checkbox trong bảng phân quyền chi tiết (Tham số, SPDV...).',
        'Expected': '(i) Nghiệp vụ/Logic: Không cho phép sửa đổi quyền con lẻ tẻ trong nhóm (BR_04 & Sửa BR_06).\n(ii) UI: Bảng grid phân quyền hiển thị tự động. Các checkbox/switch đều ở trạng thái disabled, không phản hồi click chuột.\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'URD_Ref': 'SA.03',
        'BR_Ref': 'BR_04, BR_06',
        'Trace_ID': 'BR-04-READONLY',
        'Note': 'Gộp cho 2 form Thêm và Sửa do chung một behavior theo URD.'
    },
    {
        'TC_ID': 'SA03-BR-HAP-004',
        'Module': 'SA03',
        'Feature': 'Sửa',
        'Title': 'Kiểm tra chuyển trạng thái tài khoản không ảnh hưởng mật khẩu',
        'Type': 'Happy',
        'Category': 'Regression',
        'Priority': 'P2',
        'Precondition': '1. Tài khoản "tuan.le" đang ở trạng thái Active, password="Password@1".',
        'Steps': '1. Quản trị viên sửa: Đổi trạng thái "tuan.le" sang Inactive -> Lưu lại.\n2. Quản trị viên đổi lại trạng thái "tuan.le" về Active -> Lưu lại.\n3. Đăng nhập hệ thống dưới role "tuan.le" với pass "Password@1".',
        'Expected': '(i) Nghiệp vụ/Logic: Tài khoản đăng nhập thành công với mật khẩu sinh hiệu lực, ko bị reset do việc toggle Trạng thái tài khoản (BR_04 update).\n(ii) UI: Redirect vào trang chủ hệ thống.\n(iii) Trạng thái/Audit: -.\n(iv) Output: -',
        'URD_Ref': 'SA.03 Update',
        'BR_Ref': 'BR_04 (Sửa)',
        'Trace_ID': 'BR-04-UP-PASS',
        'Note': ''
    },
    {
        'TC_ID': 'SA03-BR-NEG-005',
        'Module': 'SA03',
        'Feature': 'Login',
        'Title': 'Kiểm tra chuyển sang trạng thái Inactive khi đăng nhập sai 5 lần',
        'Type': 'Negative',
        'Category': 'Smoke',
        'Priority': 'P1',
        'Precondition': '1. Tài khoản "minh.tran" đang ở trạng thái Active.',
        'Steps': '1. Đăng nhập bằng tên "minh.tran" và mật khẩu không đúng 5 lần liên tiếp.\n2. Đăng nhập lần 6 bằng tên "minh.tran" và mật khẩu chuẩn.',
        'Expected': '(i) Nghiệp vụ/Logic: Lần thứ 5 sai -> DB update status tài khoản chuyển sang Inactive (BR_03 phần Sửa).\n(ii) UI: Lần thứ 6 sẽ báo lỗi "Tài khoản đang bị khóa" dù nhập đúng MK.\n(iii) Trạng thái/Audit: Status đổi "Inactive".\n(iv) Output: Không.',
        'URD_Ref': 'SA.03 Update',
        'BR_Ref': 'BR_03 (Sửa)',
        'Trace_ID': 'BR-03-LOCK',
        'Note': 'BR_03 (phần Update Sửa tài khoản).'
    },
    
    # ==========================================
    # Lớp 3: UI Function (Layout, View, Bắt đầu bằng UI-FUNC)
    # ==========================================
    {
        'TC_ID': 'SA03-UI-001',
        'Module': 'SA03',
        'Feature': 'Thêm mới/Sửa',
        'Title': 'Kiểm tra validate bỏ trống các trường thông tin không cho lưu',
        'Type': 'Negative',
        'Category': 'Regression',
        'Priority': 'P2',
        'Precondition': '1. Ở màn hình form Quản lý (Thêm mới/Sửa).',
        'Steps': '1. Nhập form nhưng bỏ trống một số trường (3a: User, 3b: Phân nhóm quyền, 3c: Tên hiển thị).\n2. Nhấn nút Xác nhận',
        'Expected': '(i) Nghiệp vụ/Logic: Báo lỗi Validation chặn.\n(ii) UI: Bôi viền đỏ các control chưa nhập, Form không được đóng lại.\n(iii) Trạng thái/Audit: Không can thiệp DB.\n(iv) Output: Không.',
        'URD_Ref': 'SA.03 Form Input',
        'BR_Ref': 'UI Valid',
        'Trace_ID': 'UI-EMPTY',
        'Note': 'Dedup check chung Validation'
    },
    {
        'TC_ID': 'SA03-UI-002',
        'Module': 'SA03',
        'Feature': 'Thêm mới/Sửa',
        'Title': 'Kiểm tra hủy thao tác khi nhấn nút Đóng trên form',
        'Type': 'Exception',
        'Category': 'Regression',
        'Priority': 'P2',
        'Precondition': '1. Ở màn hình form Quản lý (Thêm mới/Sửa).',
        'Steps': '1. Thay đổi hoặc nhập mới 1 số ký tự vào trường User.\n2. Nhấn nút "Đóng".',
        'Expected': '(i) Nghiệp vụ/Logic: Không lưu.\n(ii) UI: Form Tắt, grid list bên dưới không phản chiếu bất kỳ bản ghi nào mới (hoặc update).\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'URD_Ref': 'SA.03 Form Action',
        'BR_Ref': 'UI Valid',
        'Trace_ID': 'UI-CLOSE',
        'Note': ''
    },
    {
        'TC_ID': 'SA03-UI-LIST-001',
        'Module': 'SA03',
        'Feature': 'Xem danh sách',
        'Title': 'Verify hiển thị giao diện lưới Danh sách người dùng theo Mockup',
        'Type': 'Happy',
        'Category': 'Regression',
        'Priority': 'P3',
        'Precondition': '1. Có ít nhất 5 records người dùng trong hệ thống.',
        'Steps': '1. Truy cập tính năng Quản lý người dùng.',
        'Expected': '(i) Nghiệp vụ/Logic: Render API data thành công.\n(ii) UI: Grid bao gồm cấc cột: User, Tên hiển thị, Khối, Phòng ban, Nhóm quyền, Trạng thái, Số điện thoại, Email, Ngày tạo, Ngày sửa, Người sửa, Hành động (Nút răng cưa). Có phân trang và filter hiển thị N bản ghi.\n(iii) Trạng thái/Audit: -\n(iv) Output: -',
        'URD_Ref': 'SA.03 Screen 1',
        'BR_Ref': 'UI-FUNC.04 (Xem)',
        'Trace_ID': 'UI-LST',
        'Note': ''
    },
    {
        'TC_ID': 'SA03-UI-IMP-001',
        'Module': 'SA03',
        'Feature': 'Khác',
        'Title': 'Kiểm tra hiển thị luồng Import danh sách / Tải lên',
        'Type': 'Happy',
        'Category': 'Regression',
        'Priority': 'P2',
        'Precondition': '1. Có file Excel mẫu hợp lệ.',
        'Steps': '1. Chọn Tải lên (Import).\n2. Gửi file lên hệ thống.',
        'Expected': '(i) Nghiệp vụ/Logic: Xử lý theo quy định, các bản ghi import phải validate như nhập form tay (UI-FUNC.02).\n(ii) UI: Lưới được tải lại phản ánh các rows trong Excel.\n(iii) Trạng thái/Audit: Ghi Log Audit.\n(iv) Output: -',
        'URD_Ref': 'SA.03 Import',
        'BR_Ref': 'UI-FUNC.02',
        'Trace_ID': 'UI-IMPORT',
        'Note': ''
    }
]

# 2. Coverage Rules
coverage_data = [
    ('Business Rule', 'BR_01', 'Covered', 'Tham chiếu: SA03-BR-HAP-002'),
    ('Business Rule', 'BR_02', 'Covered', 'Tham chiếu: SA03-BR-NEG-001 (User duy nhất)'),
    ('Business Rule', 'BR_03 (Add)', 'Covered', 'Tham chiếu: SA03-BR-HAP-002 (Không yêu cầu duyệt)'),
    ('Business Rule', 'BR_04 (Add)', 'Covered', 'Tham chiếu: SA03-BR-HAP-003 (Read-only Grid Permission)'),
    ('Business Rule', 'BR_03 (Edit)', 'Covered', 'Tham chiếu: SA03-BR-NEG-005 (Sai MK 5 lần switch status)'),
    ('Business Rule', 'BR_04 (Edit)', 'Covered', 'Tham chiếu: SA03-BR-HAP-004 (Active toggle vs Mật khẩu)'),
    ('Business Rule', 'BR_06 (Edit)', 'Covered', 'Tham chiếu: SA03-BR-HAP-003 (Read-only Grid)'),
    ('UI Function', 'UI-FUNC.01, 04, 06', 'Covered', 'Tham chiếu: E2E-001, SA03-UI-LIST-001'),
    ('UI Function', 'UI-FUNC.02 (Import)', 'Covered', 'Tham chiếu: SA03-UI-IMP-001')
]

# 3. Dedup Log
dedup_data = [
    ('SA03-BR-HAP-003', 'Gộp kiểm tra lưới (grid) phân quyền disabled cho cả luồng Thêm mới và Sửa vào chung 1 TC.', 'URD quy định BR_04 (Thêm) và BR_06 (Sửa) hoàn toàn giống nhau chức năng.'),
    ('SA03-UI-001', 'Gộp báo lỗi Validation để trống vào 1 list check.', 'Giảm lượng TC cho các validation đơn lẻ thông thường (3a, 3b, 3c).'),
    ('SA03-BR-HAP-004 / 005', 'Tách Negative Lock pass (005) ra khỏi Validation đổi status thủ công (004).', 'Nguồn gốc kích hoạt State là khác nhau (Login trigger vs Admin UI trigger).')
]

# 4. Generate Excel using XlsxWriter & Pandas
output_file = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/SA03_Test_Cases.xlsx'

df_tc = pd.DataFrame(tc_data)
df_cov = pd.DataFrame(coverage_data, columns=['Loại Rules/Chức năng', 'Mã tham chiếu (Ref)', 'Trạng thái Coverage', 'Ghi chú QA'])
df_dedup = pd.DataFrame(dedup_data, columns=['Mã TC gốc (Merged/Gộp)', 'Nội dung gộp/Giảm tải', 'Lý do QA'])

with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df_cov.to_excel(writer, sheet_name='Coverage', index=False)
    df_dedup.to_excel(writer, sheet_name='Dedup_Log', index=False)
    df_tc.to_excel(writer, sheet_name='Test Cases', index=False)
    
    # Auto-fit columns logic (Basic formatting)
    workbook = writer.book
    
    wrap_format = workbook.add_format({'text_wrap': True, 'valign': 'top'})
    header_format = workbook.add_format({'bold': True, 'bg_color': '#D9D9D9', 'border': 1})
    
    for sheet_name, df in zip(['Coverage', 'Dedup_Log', 'Test Cases'], [df_cov, df_dedup, df_tc]):
        worksheet = writer.sheets[sheet_name]
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            # set width width dynamically
            worksheet.set_column(col_num, col_num, 20, wrap_format)
            
    # Manually tweak specific heavy columns on Test Cases
    ws_tc = writer.sheets['Test Cases']
    ws_tc.set_column('H:H', 35, wrap_format) # Precondition
    ws_tc.set_column('I:I', 45, wrap_format) # Steps
    ws_tc.set_column('J:J', 60, wrap_format) # Expected

print(f"XONG! Generated test case suite at: {output_file}")
