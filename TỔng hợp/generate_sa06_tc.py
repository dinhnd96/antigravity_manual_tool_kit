import pandas as pd
import os

# Define file path
output_file = 'Feature_02_SA_Tham_So_He_Thong/test case/SA06_Danh_Muc_Dieu_Kien_Tinh_Phi_TestCases.xlsx'

# Ensure directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Define column structure
columns = [
    'TC_ID', 'BR_Ref', 'URD_Ref', 'Module', 'Feature', 'Title', 
    'Type', 'Category', 'Priority', 'Precondition', 'Steps', 
    'Expected', 'Trace_ID', 'Note', 
    'Status R1', 'Tester R1', 'Date R1', 
    'Status R2', 'Tester R2', 'Date R2', 'Final Status'
]

# Generate data
data = [
    # FLOW
    {
        'TC_ID': 'SA06-FLOW-HAP-001', 'BR_Ref': '', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Danh mục điều kiện tính phí',
        'Title': 'Kiểm tra luồng nghiệp vụ E2E: Thêm mới -> Tìm kiếm -> Xem -> Sửa -> Tải xuống',
        'Type': 'Integration', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Tải khoản có quyền thao tác tính năng "Danh mục điều kiện tính phí".',
        'Steps': '1. Truy cập chức năng Thêm mới, nhập thông tin hợp lệ -> Lưu.\n2. Truy cập chức năng Tìm kiếm với bản ghi vừa tạo.\n3. Nhấn Xem bản ghi.\n4. Nhấn Sửa bản ghi, thay đổi thông tin -> Lưu.\n5. Đánh dấu bản ghi và nhấn Tải xuống.',
        'Expected': '(i) Nghiệp vụ/Logic: Luồng nghiệp vụ liền mạch, hệ thống xử lý đúng tại từng bước (Lưu tạo mới, Tìm thấy bản ghi, Xem chặn sửa, Cập nhật thành công, Xuất file dúng dữ liệu).\n(ii) UI: Chuyển hướng màn hình và hiển thị grid đúng.\n(iii) Trạng thái/Audit: Bản ghi lưu trữ trạng thái cuối cùng, sinh đủ log audit.\n(iv) Output: File excel tải xuống chứa dữ liệu cập nhật cuối cùng.',
        'Trace_ID': 'SA06-FLOW-E2E', 'Note': ''
    },
    
    # BR_01
    {
        'TC_ID': 'SA06-BR-HAP-001', 'BR_Ref': 'BR_01', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới Trường điều kiện',
        'Title': 'Kiểm tra chức năng Thêm mới thành công khi nhập đầy đủ các trường bắt buộc',
        'Type': 'Happy', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Đăng nhập với quyền truy cập chức năng Thêm mới điều kiện tính phí.\n2. Chuẩn bị thông tin điều kiện mới.',
        'Steps': '1. Tại màn "Danh mục điều kiện tính phí", chọn "Thêm mới".\n2. Nhập đầy đủ và hợp lệ các trường bắt buộc (Mã, Tên, Kiểu dữ liệu, Trạng thái, Nguồn dữ liệu).\n3. Nhấn "Xác nhận".',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống lưu thành công thông tin điều kiện tính phí vào Database.\n(ii) UI: Đóng form thêm mới, trở về grid, hiển thị thông báo "Thêm mới điều kiện thành công".\n(iii) Trạng thái/Audit: Bản ghi có trạng thái mặc định (theo quy trình), ghi log tạo mới.\n(iv) Output: Không có.',
        'Trace_ID': 'BR01-ADD-OK', 'Note': ''
    },
    {
        'TC_ID': 'SA06-BR-NEG-001', 'BR_Ref': 'BR_01', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới/Sửa Trường điều kiện',
        'Title': 'Kiểm tra hệ thống chặn lưu khi không nhập các trường bắt buộc',
        'Type': 'Negative', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Tài khoản có quyền thao tác Thêm mới/Sửa điều kiện tính phí.',
        'Steps': '1. Mở màn hình Thêm/Sửa.\n2. Thực hiện: \n  2a. Bỏ trống Mã điều kiện\n  2b. Bỏ trống Tên điều kiện\n  2c. Bỏ trống cả Mã và Tên.\n3. Nhấn "Xác nhận".',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống chặn lưu bản ghi do thiếu trường bắt buộc.\n(ii) UI: Form vẫn giữ nguyên, focus bôi đỏ ô chưa nhập kèm cảnh báo "Trường bắt buộc nhập".\n(iii) Trạng thái/Audit: Không tạo hoặc đổi trạng thái bản ghi, không sinh log audit.\n(iv) Output: Không có.',
        'Trace_ID': 'BR01-ADD-MISSING', 'Note': 'Gộp các trường hợp: [Bỏ trống Mã, Bỏ trống Tên, Bỏ trống cả 2]'
    },
    
    # BR_02
    {
        'TC_ID': 'SA06-BR-HAP-002', 'BR_Ref': 'BR_02', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới/Sửa Trường điều kiện',
        'Title': 'Kiểm tra thao tác Đóng form không lưu lại thông tin sửa đổi',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đang ở form Thêm mới hoặc Sửa điều kiện tính phí.',
        'Steps': '1. Nhập một số thông tin (Mã, Tên...).\n2. Nhấn nút "Đóng" hoặc nút (X).',
        'Expected': '(i) Nghiệp vụ/Logic: Không thực hiện lưu dữ liệu vào hệ thống (hủy thao tác).\n(ii) UI: Form đóng lại, trở về màn hình danh sách trước đó, dữ liệu trên grid không thay đổi.\n(iii) Trạng thái/Audit: Không sinh log audit.\n(iv) Output: Không có.',
        'Trace_ID': 'BR02-CLOSE-BTN', 'Note': 'Cover luôn cho TC-UI đóng form'
    },
    
    # BR_03
    {
        'TC_ID': 'SA06-BR-NEG-002', 'BR_Ref': 'BR_03', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới Trường điều kiện',
        'Title': 'Kiểm tra hệ thống báo lỗi khi nhập trùng Mã điều kiện hoặc Tên điều kiện đã tồn tại',
        'Type': 'Negative', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Hệ thống đã tồn tại bản ghi có Mã "COND01" và Tên "Fee01".\n2. Đang ở màn Thêm mới.',
        'Steps': '1. Thực hiện lần lượt:\n  1a. Nhập Mã "COND01", Tên "Fee99"\n  1b. Nhập Mã "COND99", Tên "Fee01"\n  1c. Nhập trùng cả Mã "COND01" và Tên "Fee01"\n2. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: DB kiểm tra kiểm tra constraint (Unique) và chặn tạo mới bản ghi.\n(ii) UI: Hiển thị lỗi tương ứng cho Mã điều kiện / Tên điều kiện đã tồn tại. Form không tắt.\n(iii) Trạng thái/Audit: Không tạo thay đổi, không sinh log.\n(iv) Output: Không có.',
        'Trace_ID': 'BR03-UNIQUE', 'Note': 'Gộp các trường hợp: [Trùng Mã, Trùng Tên, Trùng Cả 2]'
    },
    
    # BR_04
    {
        'TC_ID': 'SA06-BR-HAP-003', 'BR_Ref': 'BR_04', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới Trường điều kiện',
        'Title': 'Kiểm tra ghi nhận đúng [Kiểu dữ liệu] vào hệ thống theo 4 định dạng',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đang ở màn hình Thêm mới/Sửa.',
        'Steps': '1. Nhập Mã và Tên.\n2. Tại field "Kiểu dữ liệu", lần lượt chọn:\n  2a. Number\n  2b. String\n  2c. Date (YYYY-MM-DD)\n  2d. Time (HH:MM:SS)\n3. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: Bản ghi được lưu với đúng schema DataType tương ứng.\n(ii) UI: Lưu thành công, grid hiển thị đúng định dạng đã chọn.\n(iii) Trạng thái/Audit: Bản ghi lưu vết Audit.\n(iv) Output: Không có.',
        'Trace_ID': 'BR04-DATATYPE', 'Note': 'Gộp 4 biến thể DataType'
    },
    
    # BR_05
    {
        'TC_ID': 'SA06-BR-HAP-004', 'BR_Ref': 'BR_05', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Sửa Trường điều kiện',
        'Title': 'Kiểm tra cho phép sửa trạng thái khi Điều kiện tính phí không vi phạm điều kiện gán',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Tồn tại bản ghi Điều kiện tính phí chưa gán CTƯĐ/Code phí HOẶC gán CTƯĐ (Hết hiệu lực) / Code phí (Hủy).\n2. Trạng thái hiện tại: Không hoạt động.',
        'Steps': '1. Mở màn hình Sửa thông tin bản ghi đạt điều kiện.\n2. Thay đổi trạng thái thành "Hoạt động".\n3. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: Cho phép cập nhật chuyển trạng thái.\n(ii) UI: Đóng form, thông báo Sửa thành công, màn hình danh sách cập nhật trạng thái "Hoạt động".\n(iii) Trạng thái/Audit: Ghi log sửa trạng thái.\n(iv) Output: Không.',
        'Trace_ID': 'BR05-STATUS-OK', 'Note': ''
    },
    {
        'TC_ID': 'SA06-BR-NEG-003', 'BR_Ref': 'BR_05', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Sửa Trường điều kiện',
        'Title': 'Kiểm tra chặn sửa trạng thái khi Điều kiện tính phí đang gán với CTƯĐ/Code phí đang dùng',
        'Type': 'Negative', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Tồn tại bản ghi đang gán CTƯĐ (Chưa hiệu lực/Đang hiệu lực) HOẶC gán Code phí (Hoạt động/Ngưng HĐ/Chờ gán).',
        'Steps': '1. Mở màn hình Sửa thông tin bản ghi nói trên.\n2. Sửa thông tin trạng thái khác trạng thái ban đầu.\n3. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: Phát hiện ràng buộc tham chiếu, chặn update.\n(ii) UI: Hệ thống bật popup/toast cảnh báo "Không cho phép sửa trạng thái do đang gán với [Tên/Mã CTƯĐ/Code phí]".\n(iii) Trạng thái/Audit: Không tạo thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR05-STATUS-BLOCK', 'Note': ''
    },
    {
        'TC_ID': 'SA06-BR-HAP-005', 'BR_Ref': 'BR_05', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Tích hợp Code phí',
        'Title': 'Kiểm tra chỉ hiển thị danh sách điều kiện tính phí có trạng thái = "Hoạt động" tại màn tạo Code phí',
        'Type': 'Integration', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. "COND-ACT" trạng thái Hoạt động, "COND-INACT" trạng thái Không hoạt động.\n2. Mở màn hình tạo/sửa Code phí.',
        'Steps': '1. Xem danh sách dropdown "Điều kiện tính phí".',
        'Expected': '(i) Nghiệp vụ/Logic: Filter query API trả về chỉ list các Item Active.\n(ii) UI: Dropdown có "COND-ACT", không có "COND-INACT".\n(iii) Trạng thái/Audit: Không thay đổi.\n(iv) Output: Không.',
        'Trace_ID': 'BR05-INTEGRATION', 'Note': ''
    },
    
    # BR_06
    {
        'TC_ID': 'SA06-BR-HAP-006', 'BR_Ref': 'BR_06', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới/Sửa Trường điều kiện',
        'Title': 'Kiểm tra hiển thị động trường nhập liệu theo giá trị của [Nguồn dữ liệu]',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Mở màn hình Thêm mới/Sửa.',
        'Steps': '1. Tại dropdown "Nguồn dữ liệu", lần lượt chọn:\n  1a. Chọn "API". \n  1b. Chọn "ETL". \n2. Nhập thông tin lần lượt cho ô "Mapping note Msg" hoặc chọn list của "Bảng dữ liệu" (VD: ETL Khách hàng).\n3. Nhấn Xác nhận.',
        'Expected': '(i) Nghiệp vụ/Logic: Lưu chuẩn cấu hình ánh xạ theo Nguồn (API ghi nhận Map Note Msg, ETL ghi nhận Tên bảng).\n(ii) UI: (1a) Hiển thị input "Mapping note Msg" – (1b) Ẩn input "Mapping", hiển thị Dropdown "Bảng dữ liệu". Lưu thành công toast xanh.\n(iii) Trạng thái/Audit: Sinh log audit config source tương ứng.\n(iv) Output: Không có.',
        'Trace_ID': 'BR06-DATASOURCE', 'Note': 'Gộp 2 biến thể mapping API và ETL'
    },
    
    # UI TESTS
    {
        'TC_ID': 'SA06-UI-001', 'BR_Ref': 'UI-FUNC.01', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Thêm mới Trường điều kiện',
        'Title': 'Kiểm tra giao diện màn hình Thêm mới Trường điều kiện',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Đăng nhập thành công, vào menu Tính phí -> Danh mục.',
        'Steps': '1. Click nút "Thêm mới".\n2. Quan sát mở màn hình popup / tab Thêm mới.',
        'Expected': '(i) Nghiệp vụ/Logic: Gọi thành công dữ liệu MasterData (nếu có drop down).\n(ii) UI: Popup bật lên mượt mà, bao gồm đủ các trường (Mã, Tên, Kiểu DL, Cờ Trạng thái mặc định Hoạt động). \n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'Trace_ID': 'UI-ADD-FORM', 'Note': 'Chỉ check UI'
    },
    {
        'TC_ID': 'SA06-UI-002', 'BR_Ref': 'UI-FUNC.02', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Sửa Trường điều kiện',
        'Title': 'Kiểm tra màn hình hiển thị đẩy đủ thông tin khi mở form Thiết lập (Sửa)',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Có sẵn 1 bản ghi trên lưới (COND_X).',
        'Steps': '1. Click icon "Sửa" dòng COND_X.',
        'Expected': '(i) Nghiệp vụ/Logic: Fetch API detail chính xác cấu hình cũ theo ID.\n(ii) UI: Form load xong, điền đẩy đủ các thông số của COND_X vào các input tương ứng (kể cả phần mapping API/ETL ẩn hiện đúng quy tắc).\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'Trace_ID': 'UI-EDIT-LOAD', 'Note': ''
    },
    {
        'TC_ID': 'SA06-UI-003', 'BR_Ref': 'UI-FUNC.03', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Xem',
        'Title': 'Kiểm tra màn hình Xem chi tiết bản ghi (chỉ đọc, không cho sửa)',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Có sẵn 1 bản ghi.',
        'Steps': '1. Click icon "Xem chi tiết" tại lưới.',
        'Expected': '(i) Nghiệp vụ/Logic: Fetch API chi tiết và không khóa chặn thao tác ghi DB.\n(ii) UI: Tất cả các field đều bị disabled/ẩn tính năng sửa. Nút "Lưu" biến mất hoặc mờ đi. Có nút quay lại/đóng.\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'Trace_ID': 'UI-VIEW-ONLY', 'Note': 'Khẳng định quy tắc không chèn lệnh nhấn Xác Nhận ở Luồng View'
    },
    {
        'TC_ID': 'SA06-UI-004', 'BR_Ref': 'UI-FUNC.04', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Tìm kiếm',
        'Title': 'Kiểm tra chức năng Tìm kiếm (Filter) với các trường thông tin trên lưới',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Có sẵn nhiều bản ghi với trạng thái/tên khác nhau.',
        'Steps': '1. Thực hiện tìm kiếm:\n  1a. Nhập text một phần Tên điều kiện\n  1b. Chọn trạng thái = "Không hoạt động"\n2. Nhấn tùy chọn Tìm kiếm (hoặc tự động tải).\n3. Click "Xóa bộ lọc / Clear".',
        'Expected': '(i) Nghiệp vụ/Logic: Gọi Search API kèm query params thiết lập chuẩn.\n(ii) UI: Lưới reload (có loading indicator) hiển thị kết quả đúng với filter. Khi Clear filter thì trả về trạng thái mặc định như bước load màn. Lưới phân trang đúng quy chiếu.\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Không.',
        'Trace_ID': 'UI-SEARCH-BASIC', 'Note': 'Gộp tìm Tên, Trạng thái, Clear'
    },
    {
        'TC_ID': 'SA06-UI-005', 'BR_Ref': 'UI-FUNC.05', 'URD_Ref': 'I.1.1.1', 'Module': 'SA.06', 'Feature': 'Tải xuống',
        'Title': 'Kiểm tra tải xuống dữ liệu (Export Danh sách)',
        'Type': 'Integration', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Có dữ liệu trên lưới. Máy có kết nối mạng ổn định.',
        'Steps': '1. Click icon / Nút "Tải xuống" trên thanh thao tác.',
        'Expected': '(i) Nghiệp vụ/Logic: Trigger Export API, gom dữ liệu (có / không filter) tuỳ context lưới.\n(ii) UI: Không chuyển trang, có thể hiện spinner chờ export.\n(iii) Trạng thái/Audit: Ghi nhận log Audit Export (nếu dự án yêu cầu).\n(iv) Output: File excel dạng .xlsx tải xuống local, đủ header, không vỡ font tiếng Việt.',
        'Trace_ID': 'UI-EXPORT', 'Note': ''
    }
]

df_tc = pd.DataFrame(data, columns=columns)
df_tc = df_tc.astype(object).fillna('')

# Coverage Data
coverage_data = [
    {'Rule/UI': 'BR_01', 'Status': 'Covered', 'Note': 'SA06-BR-HAP-001, SA06-BR-NEG-001'},
    {'Rule/UI': 'BR_02', 'Status': 'Covered', 'Note': 'SA06-BR-HAP-002'},
    {'Rule/UI': 'BR_03', 'Status': 'Covered', 'Note': 'SA06-BR-NEG-002'},
    {'Rule/UI': 'BR_04', 'Status': 'Covered', 'Note': 'SA06-BR-HAP-003'},
    {'Rule/UI': 'BR_05', 'Status': 'Covered', 'Note': 'SA06-BR-HAP-004, -005, SA06-BR-NEG-003'},
    {'Rule/UI': 'BR_06', 'Status': 'Covered', 'Note': 'SA06-BR-HAP-006'},
    {'Rule/UI': 'UI-FUNC.01 (Thêm mới)', 'Status': 'Covered', 'Note': 'SA06-UI-001'},
    {'Rule/UI': 'UI-FUNC.02 (Sửa)', 'Status': 'Covered', 'Note': 'SA06-UI-002'},
    {'Rule/UI': 'UI-FUNC.03 (Xem)', 'Status': 'Covered', 'Note': 'SA06-UI-003'},
    {'Rule/UI': 'UI-FUNC.04 (Tìm kiếm)', 'Status': 'Covered', 'Note': 'SA06-UI-004'},
    {'Rule/UI': 'UI-FUNC.05 (Tải xuống)', 'Status': 'Covered', 'Note': 'SA06-UI-005'},
]

df_cov = pd.DataFrame(coverage_data)

# Dedup Logic
dedup_data = [
    {
        'Issue identified': 'Bỏ trống trường bắt buộc có nhiều trường (Mã, Tên, 1 trong 2)',
        'Decision': 'Gộp các trường hợp lỗi bắt buộc nhập vào 1 TC: SA06-BR-NEG-001',
        'Note': 'Dùng step 2a, 2b, 2c để tối ưu'
    },
    {
        'Issue identified': 'Trùng khóa chính nhiều tổ hợp (Mã, Tên, Cả 2)',
        'Decision': 'Gộp trùng uniqueness vào 1 TC: SA06-BR-NEG-002',
        'Note': 'Dùng step 1a, 1b, 1c'
    },
    {
        'Issue identified': 'Nhiều định dạng Kiểu dữ liệu (4 formats)',
        'Decision': 'Gộp luồng happy path kiểm tra Data Type vào: SA06-BR-HAP-003',
        'Note': ''
    },
    {
        'Issue identified': 'Nhiều tuỳ chọn Filter, Clear Filter',
        'Decision': 'Gộp thao tác Search Basic & Clear vào: SA06-UI-004',
        'Note': ''
    }
]

df_dedup = pd.DataFrame(dedup_data)

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_tc.to_excel(writer, sheet_name='Test Cases', index=False)
    df_cov.to_excel(writer, sheet_name='Coverage', index=False)
    df_dedup.to_excel(writer, sheet_name='Dedup_Log', index=False)

print(f'Successfully created {output_file}')
