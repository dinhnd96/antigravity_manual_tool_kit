import pandas as pd
import os

# Data for Coverage
coverage_data = [
    ["Business Rule (BR)", "BR_01", "Covered", "2 TC Negative: Bỏ trống trường bắt buộc & Nhập dữ liệu sai định dạng"],
    ["Security & Auth", "Phân quyền", "Covered", "1 TC Negative kiểm tra thao tác Sửa bằng tài khoản Không có quyền"],
    ["Business Rule (BR)", "BR_02", "Covered", "1 TC Happy thao tác Đóng form hủy đổi dữ liệu"],
    ["Business Rule (BR)", "BR_03", "Covered", "2 TC (Integration/Calculation) kiểm tra luồng Time-out và Max failed logins"],
    ["UI Function", "UI-FUNC.01 (Xem)", "Covered", "1 TC UI Happy kiểm tra giao diện View readonly form"],
    ["UI Function", "UI-FUNC.02 (Sửa)", "Covered", "1 TC UI Happy kiểm tra giao diện Edit load data"],
    ["End-to-End", "E2E", "Covered", "1 TC Flow cho luồng Cập nhật và tự động phản ánh ngay lên View/Grid"]
]
df_coverage = pd.DataFrame(coverage_data, columns=["Nhóm Kiểm Thử", "URD/BR_Ref", "Kết Quả Rà Soát", "Ghi Chú"])

# Data for Dedup Log
dedup_data = [
    ["MERGE_BR01", "SA08-BR01-NEG-001", "Bỏ trống \"Thời gian time-out\", bỏ trống \"Số lần tối đa đăng nhập sai\"", "Gộp chung thành 1 Test Case Negative test logic validation form bắt buộc (*). (Ghi chú gộp tại cột Note)."],
    ["DEDUP_UI_EDIT", "SA08-UI-02-EDIT-001", "Luồng Validate nhập thiếu tại UI Sửa và luồng submit", "Đã gỡ Validation ra khỏi TC UI và Note only do tính năng chặn lưu đã được test kỹ ở cụm TC-BR01 và luồng E2E-FLOW."]
]
df_dedup = pd.DataFrame(dedup_data, columns=["Mã Quyết Định", "TC_ID Chính (Giữ Lại)", "Các trường hợp đã Gộp/Loại bỏ", "Lý Do & Hành Động (Ghi Chú Hành Động)"])

# Data for Test Cases
tc_columns = ["TC_ID", "BR_Ref", "URD_Ref", "Module", "Feature", "Title", "Type", "Category", "Priority", "Precondition", "Steps", "Expected", "Trace_ID", "Note"]
tc_data = [
    [
        "SA08-BR01-NEG-001", "BR_01", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra hệ thống báo lỗi khi người dùng bỏ trống các trường dữ liệu bắt buộc trên màn hình Sửa tham số", 
        "Negative", "Regression", "P1", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền Quản lý tham số. Đang ở màn hình Sửa tham số mặc định.", 
        "1. Xóa toàn bộ dữ liệu tại trường bắt buộc muốn kiểm tra. \n2. Nhấn nút Xác nhận.", 
        "(i) Nghiệp vụ/Logic: Hệ thống chặn không cho phép lưu thay đổi do vi phạm ràng buộc dữ liệu đầu vào. \n(ii) UI: Form quản lý không đóng lại, hệ thống focus và bôi đỏ viền ô lỗi, hiển thị cảnh báo 'Trường bắt buộc nhập' ngay dưới ô bị thiếu. \n(iii) Trạng thái/Audit: Bản ghi tham số không bị lưu đè cập nhật, không sinh log audit. \n(iv) Output: Không sinh message/file.", 
        "SA08-BR01-REQ", "Gộp các trường hợp: Bỏ trống trường Thời gian time-out, bỏ trống trường Số lần tối đa đăng nhập sai"
    ],
    [
        "SA08-BR01-NEG-002", "BR_01", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra hệ thống báo lỗi khi nhập dữ liệu không hợp lệ (số âm, chữ cái, thập phân) vào các trường tham số", 
        "Negative", "Regression", "P1", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền. Đang ở màn hình Sửa tham số mặc định.", 
        "1. Nhập một giá trị không hợp lệ (như số âm -5, số thập phân 1.5, hoặc ký tự đặc biệt @abc) vào trường [Thời gian time-out] hoặc [Số lần tối đa đăng nhập sai]. \n2. Nhấn nút Xác nhận.", 
        "(i) Nghiệp vụ/Logic: Hệ thống chặn không cho phép lưu thay đổi do dữ liệu đầu vào sai định dạng. \n(ii) UI: Form quản lý không đóng lại, hệ thống focus và bôi đỏ viền ô lỗi, hiển thị cảnh báo 'Dữ liệu không hợp lệ' ngay dưới ô nhập. \n(iii) Trạng thái/Audit: Bản ghi tham số không bị lưu đè cập nhật, không sinh log audit. \n(iv) Output: Không sinh message/file.", 
        "SA08-BR01-FMT", ""
    ],
    [
        "SA08-BR02-HPY-001", "BR_02", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra hệ thống hủy bỏ thao tác cập nhật và không lưu dữ liệu khi chọn nút Đóng trên màn hình Sửa", 
        "Happy", "Regression", "P2", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền quản lý tham số. Đang mở màn hình Sửa tham số mặc định cho một bản ghi bất kỳ.", 
        "1. Nhập thay đổi thông tin (VD: đổi thời gian time-out thành một giá trị khác). \n2. Nhấn nút Đóng trên form. \n3. Mở xem lại bản ghi tham số vừa thao tác.", 
        "(i) Nghiệp vụ/Logic: Hệ thống hủy bỏ thao tác thay đổi, không lưu dữ liệu cập nhật mới vào Database. \n(ii) UI: Form Sửa đóng lại ngay lập tức và trang trả về màn hình Danh sách tham số mặc định. \n(iii) Trạng thái/Audit: Bản ghi không thay đổi, giữ nguyên giá trị cũ, không có hệ thống log cập nhật. \n(iv) Output: Không sinh message/file.", 
        "SA08-BR02-CLS", ""
    ],
    [
        "SA08-BR03-HPY-001", "BR_03", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra chức năng cập nhật Thời gian time-out và tự động đăng xuất người dùng khi hết phiên", 
        "Calculation", "Smoke", "P1", 
        "Có tài khoản test. Người dùng được phân quyền. Đang ở màn hình Quản lý tham số.", 
        "1. Mở màn hình Sửa tham số. \n2. Cập nhật trường [Thời gian time-out] thành giá trị N (phút). \n3. Nhấn Xác nhận. \n4. Đăng nhập 1 acc test trên một trình duyệt khác, giữ nguyên trạng thái không thao tác (không tải lại trang, không tương tác gọi API) trong đúng N phút. \n5. Thực hiện click 1 chức năng hoặc liên kết bất kỳ trên trang.", 
        "(i) Nghiệp vụ/Logic: Lưu thành công tham số cấu hình. Quá thời gian N phút, phiên tài khoản kết thúc, chặn toàn bộ truy cập tiếp theo. \n(ii) UI: Tại Step 3 thao tác thành công. Tại Step 5, hệ thống đẩy khỏi trang lỗi về Màn hình Đăng nhập và báo lỗi Phiên đã hết hạn. \n(iii) Trạng thái/Audit: Tham số Time-out = N, hệ thống ghi log Audit thành công cho user Maker. \n(iv) Output: Không sinh message/file.", 
        "SA08-BR03-TOUT", ""
    ],
    [
        "SA08-BR03-HPY-002", "BR_03", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra chức năng cập nhật Số lần tối đa đăng nhập sai và hệ thống tự động khóa tài khoản khi nhập lỗi vượt định mức", 
        "Calculation", "Smoke", "P1", 
        "Có tài khoản test. Người dùng được phân quyền. Đang ở màn hình Quản lý tham số.", 
        "1. Mở màn hình Sửa tham số. \n2. Cập nhật trường [Số lần tối đa đăng nhập sai] thành giá trị M (lần). \n3. Nhấn Xác nhận. \n4. Dùng tài khoản test chưa đăng nhập, nhập sai mật khẩu liên tiếp đúng M lần. \n5. Thực hiện đăng nhập lần thứ M+1 với thông tin bất kỳ.", 
        "(i) Nghiệp vụ/Logic: Lưu cấu hình thành công. Khi tài khoản login sai chạm ngưỡng định mức M, tiến hành khóa tài khoản ngay lập tức. \n(ii) UI: Tại lần đăng nhập lỗi thứ M (hoặc vượt ngưỡng), hiển thị thông báo 'Tài khoản của bạn đã bị khóa do đăng nhập sai quá M lần'. \n(iii) Trạng thái/Audit: Status account bị đổi từ Active thành Khóa (Blocked). \n(iv) Output: Không sinh message/file.", 
        "SA08-BR03-FAIL", ""
    ],
    [
        "SA08-UI-01-VIEW-001", "UI-FUNC.01", "SA.08", "SA08", "Xem Tham số mặc định", 
        "Kiểm tra giao diện và luồng hiển thị readonly dữ liệu của bản ghi chi tiết trên màn hình Xem tham số", 
        "Happy", "Regression", "P2", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền. Đang ở màn hình Danh sách tham số mặc định.", 
        "1. Tại lưới danh sách, nhấn icon / nút Xem tại bản ghi tham số cần kiểm tra. \n2. Kiểm tra giao diện popup Xem chi tiết. \n3. Nhấn nút Đóng.", 
        "(i) Nghiệp vụ/Logic: Đọc đúng dữ liệu của bản ghi từ Database lên UI hiển thị thành công. \n(ii) UI: Hiển thị form Xem với trạng thái readonly (tất cả trường nhập bị disable viền xám, không trỏ con chuột vào được), load đúng thông tin. Khi click Đóng, form tắt ngay lập tức. \n(iii) Trạng thái/Audit: Không tạo thay đổi, không sinh log. \n(iv) Output: Không sinh message/file.", 
        "SA08-UI-VW01", ""
    ],
    [
        "SA08-UI-02-EDIT-001", "UI-FUNC.02", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra giao diện và load hiển thị thông tin khởi tạo trên form Sửa tham số", 
        "Happy", "Regression", "P2", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền. Đang ở màn hình Danh sách tham số mặc định.", 
        "1. Tại lưới danh sách, nhấn icon / nút Sửa tại bản ghi tham số. \n2. Kiểm tra giao diện popup form Sửa và dữ liệu đang được load tại các trường form.", 
        "(i) Nghiệp vụ/Logic: Lấy đúng dữ liệu mới nhất từ DB load liền lên form. \n(ii) UI: Hiển thị form Sửa (các ô cho phép edit, viền trắng, focus được), đổ đúng giá trị hiện tại vào ô. Nút Xác nhận và Đóng khả dụng. \n(iii) Trạng thái/Audit: Không sinh log. \n(iv) Output: Không sinh message/file.", 
        "SA08-UI-ED01", "ĐÃ COVER thao tác Lưu/Validate tại TC_ID=SA08-BR03-HPY-001 và TC_ID=SA08-BR01-NEG-001"
    ],
    [
        "SA08-ETE-FLOW-001", "E2E", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra luồng luân chuyển End-to-End đầy đủ cho nghiệp vụ cập nhật và hiển thị lại đối với cấu hình tham số mặc định", 
        "Happy", "Smoke", "P1", 
        "Người dùng đã đăng nhập hệ thống và được phân quyền. Đang ở màn hình Danh sách tham số mặc định.", 
        "1. Tại lưới Tham số mặc định, nhấn Sửa bản ghi cấu hình [Số lần tối đa đăng nhập sai]. \n2. Thay đổi giá trị tham số sang một giá trị mới hợp lệ khác biệt. \n3. Nhấn nút Xác nhận. \n4. Nhấn nút Xem tại bản ghi vừa được thay đổi trên Grid để tra cứu thử nội dung.", 
        "(i) Nghiệp vụ/Logic: Lưu liền mạch dữ liệu qua tầng Logic và hiển thị ngay bản ghi mới khi Query. \n(ii) UI: Hệ thống đóng form Sửa khi lưu thành công, bật Toast thông báo 'Sửa tham số mặc định thành công', lưới danh sách reload lại ngay lập tức hiển thị giá trị mới ở cột cấu hình. Khi mở Xem, thì data cũng khớp với thông tin sửa đổi. \n(iii) Trạng thái/Audit: Bản ghi cập nhật mới hoàn tất xuống CSDL. Sinh Audit log Maker. \n(iv) Output: Không sinh message/file.", 
        "SA08-E2E-FL01", ""
    ],
    [
        "SA08-AUTH-NEG-001", "N/A", "SA.08", "SA08", "Sửa Tham số mặc định", 
        "Kiểm tra hệ thống từ chối truy cập và thực thi cập nhật khi sử dụng tài khoản không được phân quyền", 
        "Negative", "Regression", "P1", 
        "Có 1 tài khoản test hoàn toàn KHÔNG CÓ Quyền Quản lý tham số.", 
        "1. Đăng nhập bằng tài khoản không có quyền. \n2. Cố tình truy cập trực tiếp bằng URL của màn hình Sửa tham số (nếu có) hoặc gọi thẳng API cập nhật.", 
        "(i) Nghiệp vụ/Logic: Dịch vụ/Server chặn hoàn toàn request cập nhật. \n(ii) UI: Trả về trang 403 Access Denied / Không có quyền truy cập, hiển thị thông báo lỗi 'Bạn không có quyền thực hiện chức năng này'. \n(iii) Trạng thái/Audit: Không lưu dữ liệu, có thể ghi log chặn truy cập trái phép. \n(iv) Output: Không sinh message/file.", 
        "SA08-AUTH-N01", ""
    ]
]
df_tc = pd.DataFrame(tc_data, columns=tc_columns)

output_file = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/SA08_Test_Cases.xlsx"

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_coverage.to_excel(writer, sheet_name='Coverage', index=False)
    df_dedup.to_excel(writer, sheet_name='Dedup Log', index=False)
    df_tc.to_excel(writer, sheet_name='Test Cases', index=False)

print(f"File created successfully at {output_file}")
