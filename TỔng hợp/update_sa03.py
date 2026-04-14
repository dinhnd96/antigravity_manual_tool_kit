import pandas as pd
import openpyxl

file_path = 'Feature_02_SA_Tham_So_He_Thong/SA03_Test_Cases.xlsx'
wb = openpyxl.load_workbook(file_path)

# 1. Quick Fixes on Test Cases
ws_tc = wb['Test Cases']
updates = {
    'SA03-BR-NEG-001': {
        'Steps': '1. Nhập thông tin bắt buộc, trong đó trường "User" nhập "quan.nguyen".\n2. Nhấn "Xác nhận".'
    },
    'SA03-BR-HAP-002': {
        'Expected': '(i) Nghiệp vụ/Logic: Lưu người dùng thành công, bản ghi có hiệu lực ngay theo quy trình quản trị.\n(ii) UI: Form thêm mới đóng, quay về màn hình danh sách và hiện thông báo "thêm mới người dùng thành công".\n(iii) Trạng thái/Audit: Sinh bản ghi với Trạng thái = Hoạt động (không đi qua trạng thái Chờ duyệt theo BR_03). Có log Audit.\n(iv) Output: Không.'
    },
    'SA03-BR-HAP-003': {
        'Type': 'Boundary'
    },
    'SA03-BR-HAP-004': {
        'Steps': '1. Đổi trạng thái "tuan.le" sang Inactive -> Lưu lại.\n2. Verify "tuan.le" ko đăng nhập được.\n3. Đổi lại về Active -> Lưu lại.\n4. Đăng nhập "tuan.le" với pass "Password@1".',
        'Expected': '(i) Nghiệp vụ/Logic: Toggle trạng thái ko đổi mật khẩu.\n(ii) UI: Redirect vào trang chủ khi Active.\n(iii) Trạng thái/Audit: Update trạng thái ko sinh trạng thái chờ duyệt (BR_05 Sửa).\n(iv) Output: Không.'
    },
    'SA03-BR-NEG-005': {
        'Feature': 'System Auto-State'
    },
    'SA03-UI-001': {
        'Title': 'Kiểm tra hệ thống chặn lưu khi bỏ trống các trường bắt buộc User (*) và Nhóm quyền trên form Thêm mới / Sửa'
    },
    'SA03-UI-IMP-001': {
        'Title': 'Kiểm tra Import danh sách người dùng từ file Excel thành công, hệ thống thêm mới theo danh sách'
    },
    'SA03-UI-LIST-001': {
        'Expected': '(i) Nghiệp vụ/Logic: Render API data thành công.\n(ii) UI: Grid bao gồm cấc cột: User, Tên hiển thị, Khối, Phòng ban, Nhóm quyền, Trạng thái, Số điện thoại, Email, Ngày tạo, Ngày sửa, Người sửa, Hành động (Nút răng cưa). Có phân trang và filter hiển thị N bản ghi.\n(iii) Trạng thái/Audit: -\n(iv) Output: -'
    }
}

for i, row in enumerate(ws_tc.iter_rows(values_only=False)):
    if i == 0:
        continue
    tc_id = row[0].value
    if tc_id in updates:
        if 'Steps' in updates[tc_id]:
            row[8].value = updates[tc_id]['Steps']
        if 'Expected' in updates[tc_id]:
            row[9].value = updates[tc_id]['Expected']
        if 'Type' in updates[tc_id]:
            row[4].value = updates[tc_id]['Type']
        if 'Title' in updates[tc_id]:
            row[3].value = updates[tc_id]['Title']
        if 'Feature' in updates[tc_id]:
            row[2].value = updates[tc_id]['Feature']

# 2. Append new test cases
new_tcs = [
    ('SA03-BR-NEG-006', 'SA03', 'Thêm mới', 'Kiểm tra tạo người dùng với trạng thái Inactive không thể đăng nhập', 'Negative', 'Regression', 'P1', 
        '1. Đang ở form Thêm mới.',
        '1. Nhập các trường thông tin hợp lệ.\n2. Chọn Trạng thái: "Không hoạt động" (Inactive).\n3. Lưu lại.\n4. Mở tab ẩn danh, đăng nhập bằng User vừa tạo.', 
        '(i) Nghiệp vụ/Logic: Lưu thành công nhưng hệ thống từ chối đăng nhập.\n(ii) UI: Báo lỗi tài khoản không hoạt động khi cố login.\n(iii) Trạng thái/Audit: Lưu trạng thái = Inactive. Sinh log tạo mới.\n(iv) Output: Không.',
        'SA.03', 'BR_01 (Thêm)', 'BR-INACT-NEW', 'Bổ sung Gap #1'),
    ('SA03-BR-HAP-007', 'SA03', 'Sửa', 'Kiểm tra đổi Nhóm quyền thì Grid phân quyền reload và Read-only', 'Happy', 'Regression', 'P2', 
        '1. Đang ở màn hình Sửa thông tin tài khoản "tuan.le".',
        '1. Đổi dropdown Nhóm quyền từ "Checker" sang "Maker".\n2. Cố gắng tương tác với các ô checkbox trên lưới quyền.', 
        '(i) Nghiệp vụ/Logic: Nhóm quyền được cập nhật preview chính xác cho Nhóm mới.\n(ii) UI: Bảng Grid phía dưới tự reload lại data ứng với Maker. Tất cả control trên grid vẫn Disabled, ko tương tác được.\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'SA.03', 'BR_06 (Sửa)', 'BR-06-RO', 'Bổ sung Gap #3'),
    ('SA03-UI-SEARCH-001', 'SA03', 'Tìm kiếm', 'Tìm kiếm với User/Tên hiển thị tồn tại trong hệ thống trả kết quả khớp', 'Happy', 'Regression', 'P2', 
        '1. Ở màn hình Quản lý người dùng, có data sẵn.',
        '1. Nhập text search khớp một phần hoặc khớp hoàn toàn User.\n2. Nhấn Tìm kiếm (Icon loop/Button).', 
        '(i) Nghiệp vụ/Logic: DB Filter đúng theo tiêu chí.\n(ii) UI: Grid hiển thị các record thỏa mãn điệu kiện search.\n(iii) Trạng thái/Audit: -\n(iv) Output: -',
        'SA.03', 'UI-FUNC.05', 'UI-SRCH-HAP', 'Bổ sung Gap #4'),
    ('SA03-UI-SEARCH-002', 'SA03', 'Tìm kiếm', 'Tìm kiếm với keyword không tồn tại trả về grid rỗng', 'Negative', 'Regression', 'P2', 
        '1. Ở màn hình Quản lý người dùng.',
        '1. Nhập string linh tinh (VD: "xyz123999").\n2. Nhấn Tìm kiếm.', 
        '(i) Nghiệp vụ/Logic: DB Filter không ra bản ghi nào.\n(ii) UI: Grid rỗng, hiển thị text "Không tìm thấy dữ liệu".\n(iii) Trạng thái/Audit: -\n(iv) Output: -',
        'SA.03', 'UI-FUNC.05', 'UI-SRCH-NEG', 'Bổ sung Gap #4'),
    ('SA03-UI-EXPORT-001', 'SA03', 'Tải xuống', 'Kiểm tra Tải xuống (Export) danh sách thành công', 'Happy', 'Regression', 'P2', 
        '1. Ở màn hình Quản lý người dùng, có dữ liệu.',
        '1. Nhấn nút "Tải xuống" (Màu vàng).', 
        '(i) Nghiệp vụ/Logic: Tác vụ kết xuất dữ liệu thực thi.\n(ii) UI: Hiển thị toast báo tải về. Trình duyệt tải tệp tin.\n(iii) Trạng thái/Audit: Sinh log export.\n(iv) Output: File excel có các cột khớp với hiển thị trên lưới Grid web.',
        'SA.03', 'UI-FUNC.06', 'UI-EXP', 'Bổ sung Gap #5'),
    ('SA03-UI-VIEW-001', 'SA03', 'Xem', 'Kiểm tra xem chi tiết người dùng dưới dạng Form Read-Only', 'Happy', 'Regression', 'P2', 
        '1. Ở màn hình danh sách người dùng.',
        '1. Chọn hành động Xem chi tiết (Nếu UI hỗ trợ thông qua click row hoặc icon).', 
        '(i) Nghiệp vụ/Logic: Lấy đúng data từ DB đổ lên Form.\n(ii) UI: Form xem hiển thị đầy đủ thông tin (User, Tên hiển thị...). Tất cả đều Disabled (kể cả dropdown, button lưu).\n(iii) Trạng thái/Audit: -\n(iv) Output: -',
        'SA.03', 'UI-FUNC.04', 'UI-VIEW', 'Bổ sung Gap #7'),
    ('SA03-UI-IMP-NEG-001', 'SA03', 'Khác/Import', 'Kiểm tra Import chặn thêm các bản ghi bị trùng lặp User', 'Negative', 'Regression', 'P1', 
        '1. Chuẩn bị file Excel có cấu trúc đúng, dòng 1 hợp lệ, dòng 2 chứa "User" quen thuộc đã có trong DB.',
        '1. Chọn "Tải lên".\n2. Upload file.\n3. Xác nhận Import.', 
        '(i) Nghiệp vụ/Logic: DB chỉ lưu dòng 1, reject dòng 2 do vi phạm khóa duy nhất.\n(ii) UI: Báo lỗi "Dòng 2: User đã tồn tại".\n(iii) Trạng thái/Audit: Chỉ sinh data cho dòng 1.\n(iv) Output: -',
        'SA.03 Import', 'UI-FUNC.02', 'UI-IMP-DUP', 'Bổ sung Gap #6')
]

for new_tc in new_tcs:
    ws_tc.append(new_tc)

# 3. Update Coverage Sheet
ws_cov = wb['Coverage']
new_cov_rows = [
    ('Business Rule', 'BR_05 (Sửa)', 'Covered', 'Tham chiếu: SA03-BR-HAP-004'),
    ('UI Function', 'UI-FUNC.04 (Xem Form)', 'Covered', 'Tham chiếu: SA03-UI-VIEW-001'),
    ('UI Function', 'UI-FUNC.05 (Search)', 'Covered', 'Tham chiếu: SA03-UI-SEARCH-001, 002'),
    ('UI Function', 'UI-FUNC.06 (Export)', 'Covered', 'Tham chiếu: SA03-UI-EXPORT-001')
]
for cov in new_cov_rows:
    ws_cov.append(cov)

wb.save('Feature_02_SA_Tham_So_He_Thong/SA03_Test_Cases_Updated.xlsx')
print('DONE!')
