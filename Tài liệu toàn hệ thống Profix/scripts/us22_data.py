# US22 Data for Part A and Part B generation
FEATURE = "US22 – Đăng xuất hệ thống"
PART_A_FILE = "US22_PartA_Summary.docx"
PART_B_FILE = "US22_PartB_QA.docx"
OUTPUT_DIR = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong"

# Part A content
CORE_VALUE = (
    "Tính năng US22 cho phép người dùng kết thúc phiên làm việc trên hệ thống ProfiX "
    "một cách an toàn. Hệ thống hỗ trợ 2 cơ chế đăng xuất: (1) Đăng xuất thủ công do "
    "người dùng chủ động thực hiện, và (2) Tự động đăng xuất khi phiên hết hạn hoặc khi "
    "đăng nhập phiên mới trên thiết bị khác. Người dùng cuối: Tất cả người dùng hệ thống ProfiX."
)

MODULES = [
    {
        "name": "Module 1: Đăng xuất thủ công",
        "happy": [
            "Người dùng nhấn nút \"Đăng xuất\" tại khu vực thông tin user (góc trái màn hình, sidebar dưới cùng).",
            "Hệ thống (FE) hiển thị Popup xác nhận: \"Bạn có chắc chắn muốn đăng xuất không?\".",
            "Người dùng nhấn \"Đồng ý\" → FE gửi yêu cầu đăng xuất → BE nhận và xử lý đăng xuất.",
            "FE kết thúc phiên làm việc và hiển thị màn hình Đăng nhập.",
        ],
        "alt": [
            "Người dùng nhấn \"Hủy bỏ\" → FE đóng popup xác nhận, người dùng quay lại màn hình hiện tại.",
            "Lưu ý: Các tác vụ đang thực hiện (chưa hoàn tất) sẽ KHÔNG được lưu khi đăng xuất.",
        ],
    },
    {
        "name": "Module 2: Tự động đăng xuất",
        "happy": [
            "Timeout: Hệ thống tự động đăng xuất phiên nếu người dùng không có thao tác sau khoảng thời gian quy định tại tham số SESSION_TIMEOUT.",
            "Multi-session: Khi người dùng đăng nhập phiên mới (trên cùng hoặc khác thiết bị), phiên hiện tại sẽ bị kết thúc tự động.",
            "Sau khi tự động đăng xuất, hệ thống hiển thị popup: \"Phiên đăng nhập của bạn hết hạn. Vui lòng đăng nhập lại\" với nút \"Đăng nhập\".",
            "Người dùng nhấn \"Đăng nhập\" → hệ thống hiển thị màn hình Đăng nhập (xem US21).",
        ],
        "alt": [
            "Các tác vụ đang thực hiện (chưa hoàn tất) sẽ KHÔNG được lưu khi bị tự động đăng xuất.",
        ],
    },
]

PRECONDITIONS = [
    ("Tham số hệ thống", "SESSION_TIMEOUT phải được cấu hình (giá trị thời gian idle tối đa trước khi auto-logout)."),
    ("Phiên đăng nhập", "Người dùng phải đang có phiên đăng nhập hợp lệ (đã xác thực qua US21)."),
    ("Quyền truy cập", "Tất cả người dùng đều có quyền đăng xuất (không phân quyền riêng)."),
]

QTC_APPLIED = [
    ("QTC-15", "Hành vi nút Đóng/Hủy: Khi nhấn \"Hủy bỏ\" trên popup xác nhận → đóng popup, không lưu, quay về màn hình trước."),
]

# Part B - Q&A data: (id, ref, question, category, suggestion)
QA_DATA = [
    ("US22-QA-01.1",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn Tự động đăng xuất – \"Chi tiết về luồng Đăng nhập, xem tại US22 – Là người dùng, tôi muốn đăng nhập vào hệ thống\"",
     "Tham chiếu sai US: Đoạn text dẫn \"xem tại US22\" nhưng US22 chính là tính năng Đăng xuất này. Đúng ra phải tham chiếu đến US21 (Đăng nhập).",
     "Nghiệp vụ",
     "Đề xuất: Sửa tham chiếu thành \"xem tại US21 – Là người dùng, tôi muốn đăng nhập vào hệ thống\"."),
    ("US22-QA-01.2",
     "Mục \"Lưu đồ\" – Flowchart chỉ vẽ luồng Đăng xuất thủ công (Start → Chọn Đăng xuất → Popup → Đồng ý/Hủy → End)",
     "Flowchart thiếu hoàn toàn luồng Tự động đăng xuất (session timeout và đăng nhập phiên mới) trong khi text mô tả rõ 2 cơ chế.",
     "Nghiệp vụ",
     "Đề xuất: Bổ sung Flowchart riêng cho luồng Tự động đăng xuất, hoặc xác nhận chỉ cần Flowchart cho luồng thủ công."),
    ("US22-QA-01.3",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn Tự động đăng xuất – \"hiển thị popup thông báo [...] Người dùng chọn button Đăng nhập\"",
     "Popup tự động đăng xuất chỉ mô tả nút \"Đăng nhập\". Nếu user nhấn nút X (đóng popup) thay vì nhấn \"Đăng nhập\" thì hành vi hệ thống là gì? Phiên đã hết hạn nên không thể quay lại.",
     "Nghiệp vụ",
     "Đề xuất: Popup không có nút X (force user chọn \"Đăng nhập\"), hoặc nhấn X cũng redirect về màn hình Đăng nhập."),
    ("US22-QA-01.4",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn Tự động đăng xuất – \"tự động đăng xuất phiên làm việc nếu người dùng không có thao tác sau một khoảng thời gian\"",
     "Tài liệu không đề cập cơ chế cảnh báo trước khi hết phiên (countdown warning). User đang nhập liệu phức tạp có thể mất toàn bộ dữ liệu mà không được cảnh báo trước.",
     "Nghiệp vụ",
     "Đề xuất: Hiển thị popup countdown cảnh báo (VD: 2 phút trước khi hết phiên) để user có thể gia hạn phiên."),
    ("US22-QA-02.1",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn Tự động đăng xuất – \"tham số cấp hệ thống SESSION_TIMEOUT\"",
     "Tham số SESSION_TIMEOUT: Giá trị mặc định là bao nhiêu? Đơn vị tính (phút/giây)? Phạm vi giá trị hợp lệ? Tham số này được cấu hình ở US nào?",
     "Giới hạn",
     "Đề xuất: Cần xác nhận giá trị mặc định (VD: 30 phút), đơn vị, và US quản lý tham số này."),
    ("US22-QA-02.2",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn Tự động đăng xuất – \"người dùng không có thao tác sau một khoảng thời gian\"",
     "Định nghĩa \"không có thao tác\" (idle) chưa rõ: Chỉ tính click/keystroke, hay bao gồm mouse move, scroll? API call tự động (auto-refresh) có reset timer không?",
     "Giới hạn",
     "Đề xuất: Cần BA định nghĩa cụ thể các hành động được tính là \"thao tác\" để reset session timer."),
    ("US22-QA-02.3",
     "Mục \"Yêu cầu nghiệp vụ\" – \"đăng nhập một phiên làm việc mới [...] phiên làm việc hiện tại sẽ kết thúc\"",
     "Multi-session: Nếu user có N phiên đang mở (trên nhiều thiết bị) → đăng nhập phiên mới → tất cả N phiên cũ đều bị đăng xuất hay chỉ phiên cũ nhất?",
     "Giới hạn",
     "Đề xuất: Xác nhận chính sách single-session (chỉ 1 phiên duy nhất tại mọi thời điểm) hay cho phép N phiên đồng thời."),
    ("US22-QA-03.1",
     "Mục \"Yêu cầu nghiệp vụ\" – \"Các tác vụ đang thực hiện (chưa hoàn tất) sẽ không được lưu khi người dùng Đăng xuất\"",
     "Nếu user đã nhấn \"Xác nhận\" (submit request) nhưng BE chưa xử lý xong → tại thời điểm đó bị auto-logout → request đang pending có bị hủy hay vẫn được xử lý hoàn tất?",
     "Toàn vẹn dữ liệu",
     "Đề xuất: Request đã submit thành công (BE đã nhận) phải được xử lý hoàn tất bất kể trạng thái session."),
    ("US22-QA-03.2",
     "Mục \"Yêu cầu nghiệp vụ\" – \"hệ thống đăng xuất người dùng đó khỏi phiên làm việc\"",
     "Token/session sau khi đăng xuất: Access token cũ có bị invalidate ngay lập tức không? Nếu gọi API bằng token cũ sau đăng xuất → BE reject hay vẫn xử lý?",
     "Toàn vẹn dữ liệu",
     "Đề xuất: Token phải bị invalidate ngay sau đăng xuất. Mọi API call bằng token cũ phải bị reject (401 Unauthorized)."),
    ("US22-QA-04.1",
     "Bảng \"Mô tả chi tiết các trường\", STT 2 \"Đồng ý\" – Mô tả ghi \"Đồn ý\" thay vì \"Đồng ý\"",
     "Lỗi typo trong bảng mô tả trường: STT 2 ghi \"Đồn ý\" thiếu chữ \"g\", cần sửa thành \"Đồng ý\".",
     "UI-UX",
     "Đề xuất: Sửa lỗi typo \"Đồn ý\" → \"Đồng ý\" trong bảng mô tả trường."),
    ("US22-QA-04.2",
     "Mục \"Giao diện\" – Chỉ có mockup Popup xác nhận đăng xuất thủ công, không có mockup popup tự động đăng xuất",
     "Thiếu mockup cho popup tự động đăng xuất (\"Phiên đăng nhập của bạn hết hạn. Vui lòng đăng nhập lại\" với nút \"Đăng nhập\"). Mockup này khác popup thủ công.",
     "UI-UX",
     "Đề xuất: Bổ sung mockup cho popup tự động đăng xuất để QC có cơ sở thiết kế test case UI."),
]
