import pandas as pd

data = [
    {
        'TC_ID': 'SA15-BR-HAP-001', 'BR_Ref': 'BR_01', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Tìm kiếm nâng cao',
        'Title': 'Kiểm tra logic AND khi lọc bằng nhiều điều kiện đồng thời',
        'Type': 'Happy', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Truy cập chức năng [Xem danh sách sản phẩm dịch vụ và code phí].\n2. Đảm bảo hệ thống có dữ liệu khớp với bộ lọc.',
        'Steps': '1. Nhấn nút [Lọc nâng cao].\n2. Chọn [Trạng thái] = "Hoạt động".\n3. Chọn [Loại khách hàng] = "KHCN".\n4. Nhấn nút [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống thực hiện lọc và trả về danh sách thỏa mãn đồng thời cả 2 điều kiện.\n(ii) UI: Lưới dữ liệu cập nhật kết quả mới.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Hiển thị đúng số lượng bản ghi thỏa mãn.',
        'Trace_ID': 'BR01-FILTER-AND', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-002', 'BR_Ref': 'BR_02', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Tìm kiếm gần đúng',
        'Title': 'Kiểm tra tìm kiếm gần đúng, không phân biệt hoa thường và không dấu',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình [Xem danh sách sản phẩm dịch vụ].\n2. Có bản ghi tên "Tài khoản thanh toán".',
        'Steps': '1. Nhập từ khóa "tai khoan" (không dấu, chữ thường) vào ô [Tên SPDV].\n2. Nhấn [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống tìm kiếm gần đúng (LIKE %keyword%) và bỏ qua dấu/hoa thường.\n(ii) UI: Hiển thị bản ghi "Tài khoản thanh toán".\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Kết quả hiển thị trên lưới.',
        'Trace_ID': 'BR02-FUZZY-SEARCH', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-003', 'BR_Ref': 'BR_03', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Xử lý dữ liệu đầu vào',
        'Title': 'Kiểm tra tự động Trim khoảng trắng đầu cuối cho từ khóa tìm kiếm',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình [Xem danh sách code phí chưa sử dụng].',
        'Steps': '1. Nhập mã code phí có khoảng trắng: "  CP001  ".\n2. Nhấn [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống tự động cắt bỏ khoảng trắng thừa trước khi gửi request.\n(ii) UI: Trả về kết quả khớp với mã "CP001".\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR03-TRIM-TEXT', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-004', 'BR_Ref': 'BR_05', 'URD_Ref': 'X.4', 'Module': 'SA15', 'Feature': 'Phân trang',
        'Title': 'Kiểm tra quy tắc phân trang mặc định 50 bản ghi/trang',
        'Type': 'Happy', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Đứng tại màn hình [Xem danh sách Biểu phí].\n2. Tổng số bản ghi trên hệ thống > 50.',
        'Steps': '1. Quan sát số lượng bản ghi hiển thị trên trang 1.',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống phân bổ đúng 50 bản ghi mỗi trang.\n(ii) UI: Lưới hiển thị 50 dòng; Footer hiển thị "1-50 của [Tổng số]".\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR05-PAGESIZE-50', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-005', 'BR_Ref': 'BR_06', 'URD_Ref': 'X.4', 'Module': 'SA15', 'Feature': 'Phân trang',
        'Title': 'Kiểm tra Reset số trang về trang 1 sau khi thực hiện Tìm kiếm',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P1',
        'Precondition': '1. Đang đứng tại [Trang 3] của danh sách Biểu phí.',
        'Steps': '1. Nhập một điều kiện lọc bất kỳ.\n2. Nhấn nút [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống thực hiện tìm kiếm và Reset trang hiện tại về 1.\n(ii) UI: Hiển thị những kết quả đầu tiên của bộ lọc; Thanh phân trang highlight số 1.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR06-RESET-PAGE', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-006', 'BR_Ref': 'BR_07', 'URD_Ref': 'VIII.9', 'Module': 'SA15', 'Feature': 'Tra cứu CIF',
        'Title': 'Kiểm tra ràng buộc chọn Tỉnh trước rồi mới chọn Phường/Xã trong Popup CIF',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Mở popup [Tra cứu CIF] từ màn hình [Xem code phí theo khách hàng].',
        'Steps': '1. Quan sát trạng thái Dropdown [Phường/Xã] khi chưa chọn Tỉnh.\n2. Chọn một [Tỉnh] cụ thể.\n3. Kiểm tra lại Dropdown [Phường/Xã].',
        'Expected': '(i) Nghiệp vụ/Logic: Ràng buộc phụ thuộc dữ liệu (Dependency dropdown) hoạt động đúng.\n(ii) UI: Bước 1: [Phường/Xã] bị disable. Bước 3: [Phường/Xã] được enable và chứa dữ liệu thuộc Tỉnh đã chọn.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR07-CIF-DEP-DROP', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-HAP-007', 'BR_Ref': 'BR_09', 'URD_Ref': 'X.3', 'Module': 'SA15', 'Feature': 'Tải xuống',
        'Title': 'Kiểm tra xuất file Excel đúng bộ lọc và đúng định dạng yêu cầu',
        'Type': 'Happy', 'Category': 'Smoke', 'Priority': 'P1',
        'Precondition': '1. Thực hiện lọc [Trạng thái] = "Chưa hiệu lực".\n2. Lưới dữ liệu đang hiển thị 10 bản ghi.',
        'Steps': '1. Nhấn nút [Tải xuống].\n2. Mở file Excel vừa tải.',
        'Expected': '(i) Nghiệp vụ/Logic: Dữ liệu xuất ra khớp 100% với bộ lọc đang chọn.\n(ii) UI: Hiện thông báo bắt đầu tải xuống.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: File Excel có tên theo quy tắc [Tên chức năng] - yyyymmddhhmmss.',
        'Trace_ID': 'BR09-EXPORT-FILTER', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-NEG-001', 'BR_Ref': 'BR_01', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Tìm kiếm nâng cao',
        'Title': 'Kiểm tra tìm kiếm khi không có dữ liệu thỏa mãn',
        'Type': 'Negative', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình danh sách.',
        'Steps': '1. Nhập từ khóa không tồn tại vào các ô lọc.\n2. Nhấn [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống trả về danh sách rỗng.\n(ii) UI: Lưới hiển thị trống; Hiển thị dấu "-" hoặc text "Không tìm thấy kết quả phù hợp".\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'BR01-SEARCH-NONE', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-NEG-002', 'BR_Ref': 'BR_08', 'URD_Ref': 'X.1', 'Module': 'SA15', 'Feature': 'Lọc theo ngày',
        'Title': 'Kiểm tra báo lỗi khi Từ ngày lớn hơn Đến ngày',
        'Type': 'Negative', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình danh sách có lọc [Từ ngày - Đến ngày].',
        'Steps': '1. Nhập [Từ ngày] = 10/04/2026.\n2. Nhập [Đến ngày] = 01/04/2026.\n3. Nhấn [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Chặn hành động tìm kiếm bới bộ lọc không logic.\n(ii) UI: Highlight đỏ trường ngày hoặc hiển thị Toast message cảnh báo.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Hiển thị message: "Từ ngày không được lớn hơn Đến ngày".',
        'Trace_ID': 'BR08-DATE-ORDER', 'Note': ''
    },
    {
        'TC_ID': 'SA15-BR-NEG-003', 'BR_Ref': 'BR_01', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Bảo mật tìm kiếm',
        'Title': 'Kiểm tra xử lý ký tự đặc biệt trong ô tìm kiếm (SQL Injection)',
        'Type': 'Security', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình bất kỳ có ô nhập text tìm kiếm.',
        'Steps': '1. Nhập chuỗi: "\' OR 1=1 --" vào ô [Tên].\n2. Nhấn [Tìm kiếm].',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống xử lý chuỗi dưới dạng text thuần, không thực thi script.\n(ii) UI: Trả về kết quả rỗng (do không có tên nào như vậy).\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không bị crash hệ thống hoặc lộ dữ liệu DB.',
        'Trace_ID': 'BR01-SQL-INJECTION', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-001', 'BR_Ref': 'UI-FUNC.01', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Tìm kiếm nhanh vs Lọc nâng cao',
        'Title': 'Kiểm tra quy tắc độc quyền giữa thanh Tìm kiếm nhanh và Lọc nâng cao',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Truy cập chức năng [Xem danh sách Biểu phí].',
        'Steps': '1. Nhập text vào thanh [Tìm kiếm nhanh].\n2. Quan sát nút [Lọc nâng cao].\n3. Xóa text và nhấn vào [Lọc nâng cao].',
        'Expected': '(i) Nghiệp vụ/Logic: Không cho phép sử dụng 2 chế độ lọc cùng lúc.\n(ii) UI: Khi có text ở Tìm nhanh → Disable nút Lọc nâng cao. Khi mở Lọc nâng cao → Thanh Tìm nhanh bị đóng/disable.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-EXCLUSIVE-SEARCH', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-002', 'BR_Ref': 'UI-FUNC.02', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Xóa lọc',
        'Title': 'Kiểm tra chức năng nút Xóa lọc',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đã chọn nhiều điều kiện lọc và thực hiện tìm kiếm thành công.',
        'Steps': '1. Nhấn nút [Xóa lọc].',
        'Expected': '(i) Nghiệp vụ/Logic: Reset toàn bộ tham số lọc về giá trị mặc định.\n(ii) UI: Các ô nhập xóa trắng, các dropdown về "Tất cả". Lưới load lại toàn bộ danh sách trùng khớp.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-CLEAR-FILTER', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-003', 'BR_Ref': 'UI-FUNC.04', 'URD_Ref': 'X.4', 'Module': 'SA15', 'Feature': 'Điều hướng trang',
        'Title': 'Kiểm tra các nút điều hướng phân trang (Next, Previous, First, Last)',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Hệ thống có 3 trang dữ liệu (>101 bản ghi).',
        'Steps': '1. Nhấn nút [>] (Trang kế tiếp).\n2. Nhấn nút [>>] (Trang cuối).\n3. Nhấn nút [<] (Trang trước).\n4. Nhấn nút [<<] (Trang đầu).',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống chuyển trang tương ứng thành công.\n(ii) UI: Cập nhật dữ liệu mới trên lưới mượt mà; Highlight đúng số trang đang đứng.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-PAGINATION-NAV', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-004', 'BR_Ref': 'UI-FUNC.03', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Trình trạng tải',
        'Title': 'Kiểm tra hiển thị Loading Spinner khi hệ thống đang xử lý dữ liệu tìm kiếm',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Đứng tại màn hình danh sách.',
        'Steps': '1. Thực hiện một lệnh tìm kiếm diện rộng.\n2. Quan sát UI trong lúc chờ phản hồi.',
        'Expected': '(i) Nghiệp vụ/Logic: Đảm bảo trải nghiệm người dùng không bị treo.\n(ii) UI: Hiển thị Spinner/Loading icon cho đến khi data hiển thị trên lưới.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-LOADING-STATE', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-005', 'BR_Ref': 'UI-FUNC.01', 'URD_Ref': 'X.2', 'Module': 'SA15', 'Feature': 'Duy trì trạng thái',
        'Title': 'Kiểm tra giữ trạng thái bộ lọc sau khi xem chi tiết và quay lại',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Thực hiện lọc và tìm kiếm trả về danh sách.\n2. Click vào mã của một bản ghi để xem chi tiết.',
        'Steps': '1. Tại màn hình chi tiết, nhấn nút [Quay lại] (hoặc nút Back trên trình duyệt).',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống duy trì được State của bộ lọc (Persistence state).\n(ii) UI: Màn hình danh sách hiển thị lại đúng bộ lọc và kết quả trước đó, không bị reset.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-FILTER-PERSISTENCE', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-006', 'BR_Ref': 'UI-FUNC.01', 'URD_Ref': 'X.5', 'Module': 'SA15', 'Feature': 'Lịch sử tác động',
        'Title': 'Kiểm tra hiển thị Popup Lịch sử tác động cho bản ghi từ kết quả tìm kiếm',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Hiển thị ít nhất một bản ghi trên lưới kết quả.',
        'Steps': '1. Nhấn vào hyperlink [Ngày cập nhật] (hoặc nút xem lịch sử nếu có).\n2. Quan sát popup.',
        'Expected': '(i) Nghiệp vụ/Logic: Hiển thị đúng lịch sử của bản ghi đang chọn.\n(ii) UI: Popup hiển thị danh sách các lần thay đổi theo thứ tự thời gian duyệt mới nhất trước.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-ACTION-HISTORY', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-007', 'BR_Ref': 'UI-FUNC.06', 'URD_Ref': 'VIII.1', 'Module': 'SA15', 'Feature': 'Cách ly Tab',
        'Title': 'Kiểm tra bộ lọc được cách ly độc lập giữa các Tab trong cùng màn hình',
        'Type': 'Happy', 'Category': 'Regression', 'Priority': 'P2',
        'Precondition': '1. Đứng tại màn hình có 2 tab (VD: Danh mục SPDV vs Code phí chưa dùng).',
        'Steps': '1. Lọc dữ liệu tại Tab 1.\n2. Chuyển sang Tab 2 và thực hiện một lọc khác.\n3. Quay lại Tab 1.',
        'Expected': '(i) Nghiệp vụ/Logic: Search query của các Tab không bị lẫn lộn vào nhau.\n(ii) UI: Tab 1 vẫn giữ nguyên kết quả đã lọc trước đó.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-TAB-ISOLATION', 'Note': ''
    },
    {
        'TC_ID': 'SA15-UI-008', 'BR_Ref': 'UI-FUNC.04', 'URD_Ref': 'X.4', 'Module': 'SA15', 'Feature': 'Hiệu năng phân trang',
        'Title': 'Kiểm tra hệ thống khi nhấn liên tiếp (Rapid Click) các nút phân trang',
        'Type': 'Performance', 'Category': 'Regression', 'Priority': 'P3',
        'Precondition': '1. Danh sách có dữ liệu phân trang.',
        'Steps': '1. Nhấn nút [>] liên tục 5-10 lần với tốc độ nhanh.',
        'Expected': '(i) Nghiệp vụ/Logic: Hệ thống xử lý request an toàn (thường là xử lý request cuối cùng).\n(ii) UI: Giao diện không bị treo hoặc hiển thị lỗi "Dữ liệu không đồng bộ"; Kết quả hiển thị đúng trang cuối cùng được click.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có.',
        'Trace_ID': 'UI-PERF-RAPID-CLICK', 'Note': ''
    }
]

cols = ['TC_ID', 'BR_Ref', 'URD_Ref', 'Module', 'Feature', 'Title', 'Type', 'Category', 'Priority', 'Precondition',
        'Steps', 'Expected', 'Trace_ID', 'Note', 'Status R1', 'Tester R1', 'Date R1', 'Status R2', 'Tester R2', 'Date R2', 'Final Status']

df = pd.DataFrame(data)
for col in cols:
    if col not in df.columns:
        df[col] = ''

df = df[cols]
output_file = 'Profix_Search_Pagination_TestCases.xlsx'
df.to_excel(output_file, index=False, sheet_name='Test Cases')

print(f'File created: {output_file}')
