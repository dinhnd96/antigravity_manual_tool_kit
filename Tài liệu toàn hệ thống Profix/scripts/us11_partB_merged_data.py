"""Data for merged US11 Part B Q&A — AI + VA consolidated."""

# Format: (ID, Reference, Question, Category, Suggestion, Source)
# Source: "AI" | "VA" | "BOTH" (overlapping)

QA_DATA = [
    # ═══ HM1: Nghiệp vụ / Luồng xử lý ═══
    ("US11-QA-01.1",
     "Flowchart Thêm mới CTƯĐ, Bước 10 - User chọn 'Xác nhận'",
     "Flowchart không thể hiện nhánh validate khi Bộ tham số trống (user nhấn Xác nhận mà chưa nhấn 'Thêm bộ tham số'). Hệ thống có bắt buộc phải có ít nhất 1 Bộ tham số không?",
     "Nghiệp vụ",
     "Đề xuất: FE chặn, hiển thị lỗi 'Cần thêm ít nhất 1 Bộ tham số' và không cho phép Xác nhận.",
     "VA"),

    ("US11-QA-01.2",
     "Flowchart Thêm mới CTƯĐ, Bước 9 - Khai báo Lịch đánh giá",
     "Flowchart không vẽ nhánh validate số lịch đánh giá tối thiểu. Mỗi Bộ tham số có bắt buộc ít nhất bao nhiêu lịch đánh giá (ngoài Lần 1 mặc định)?",
     "Nghiệp vụ",
     "Đề xuất: Xác nhận số lịch tối thiểu (ví dụ >= 1) để thiết kế validate FE.",
     "VA"),

    ("US11-QA-01.3",
     "Mục 'Chỉnh sửa CTƯĐ', đoạn trạng thái Đang hiệu lực + Flowchart Bước 3.b",
     "Khi CTƯĐ Đang hiệu lực, tài liệu cho phép sửa Lịch đánh giá nhưng không nói rõ về Điều kiện đánh giá. Xác nhận: (a) Điều kiện đánh giá bị khóa hoàn toàn (readonly)? (b) Lịch đánh giá đã được hệ thống thực thi (đã qua ngày) có cho sửa/xóa không?",
     "Nghiệp vụ",
     "Đề xuất: (a) Điều kiện đánh giá readonly khi Đang hiệu lực. (b) Chỉ cho sửa/xóa lịch có Ngày đánh giá > Ngày hiện tại. Lịch đã qua → readonly.",
     "BOTH"),

    ("US11-QA-01.4",
     "Mục 'Chỉnh sửa CTƯĐ', đoạn trạng thái Đang hiệu lực, phần 'Chi tiết ưu đãi'",
     "Khi Đang hiệu lực, tài liệu ghi 'cho phép thêm mới chi tiết ưu đãi'. Vậy có cho phép SỬA hoặc XÓA các chi tiết ưu đãi đã tồn tại không?",
     "Nghiệp vụ",
     "Đề xuất: Khi Đang hiệu lực, các chi tiết ưu đãi đã tồn tại ở trạng thái readonly. Chỉ cho phép THÊM MỚI dòng ưu đãi mới.",
     "AI"),

    ("US11-QA-01.5",
     "Mục 'Thêm mới CTƯĐ', đoạn Bộ tham số",
     "Tài liệu cho phép nhiều bộ tham số. Khi 2 bộ tham số có điều kiện đánh giá overlap (cùng 1 KH thỏa cả 2 bộ), KH đó được áp dụng ưu đãi của bộ nào? Có cho phép cộng dồn ưu đãi hay chỉ áp dụng bộ có giá trị cao nhất?",
     "Nghiệp vụ",
     "Đề xuất: Hệ thống áp dụng ưu đãi của bộ tham số có mức ưu đãi cao nhất (most favorable), không cộng dồn. Cần BA xác nhận logic xử lý chồng lấn.",
     "AI"),

    ("US11-QA-01.6",
     "Mục 'Xử lý tự động', phần 'Đầu ngày tái đánh giá', Bước 1",
     "Khi tái đánh giá phát hiện KH không còn thỏa → hủy ưu đãi các kỳ còn hiệu lực. Vậy kỳ ưu đãi đang được áp dụng tại thời điểm tái đánh giá có bị hủy ngay không, hay chỉ hủy các kỳ TƯƠNG LAI?",
     "Nghiệp vụ",
     "Đề xuất: Cần BA xác nhận: hủy ngay kỳ đang áp dụng hay chỉ hủy kỳ tương lai.",
     "AI"),

    ("US11-QA-01.7",
     "Mục 'Xử lý tự động', phần 'Trong ngày khi phát sinh KH mới'",
     "Cơ chế KH mở mới chỉ áp dụng với Loại ưu đãi = Theo KH. Vậy khi Loại ưu đãi = Theo TK hoặc Theo Thẻ, KH mở mới TK/Thẻ trong ngày có được tự động đánh giá không? Hay phải chờ đến lần tái đánh giá tiếp theo?",
     "Nghiệp vụ",
     "Đề xuất: Theo tài liệu, cơ chế real-time chỉ áp dụng cho Loại ưu đãi = Theo KH. Loại TK/Thẻ chờ đến lần tái đánh giá kế tiếp. Cần BA xác nhận.",
     "AI"),

    ("US11-QA-01.8",
     "Mục 'Chỉnh sửa CTƯĐ', đoạn kiểm tra tác vụ Chờ duyệt",
     "Tài liệu chỉ kiểm tra tác vụ 'Chỉnh sửa' Chờ duyệt. Nếu tồn tại tác vụ 'Thêm mới' Chờ duyệt (CTƯĐ vừa tạo chưa duyệt), có cho phép Chỉnh sửa không? CTƯĐ đang trong luồng duyệt nhiều cấp (chưa đến cấp cuối) có được phép chỉnh sửa không?",
     "Nghiệp vụ",
     "Đề xuất: (a) CTƯĐ chưa duyệt (Thêm mới Chờ duyệt) không hiển thị trên lưới chính thức → không có nút Chỉnh sửa. (b) CTƯĐ đang duyệt đa cấp → không cho chỉnh sửa. Cần BA xác nhận.",
     "BOTH"),

    ("US11-QA-01.9",
     "Flowchart Thêm mới CTƯĐ, Bước 8 - Khai báo Điều kiện đánh giá",
     "Flowchart không mô tả rõ: Nếu người dùng nhấn 'Hủy' tại bước khai báo Bộ tham số thì CTƯĐ có bị hủy luôn không? Hay chỉ thoát khỏi form Bộ tham số?",
     "Nghiệp vụ",
     "Đề xuất: BA làm rõ hành vi nút Hủy tại bước khai báo Bộ tham số.",
     "VA"),

    ("US11-QA-01.10",
     "Mục 'Thêm mới CTƯĐ', Lưu đồ Thêm mới, Bước 11 (Diễn giải)",
     "Diễn giải lưu đồ tại Bước 11 ghi: 'Thông tin hợp lệ → Bước 11.a' VÀ 'Thông tin không hợp lệ → Bước 11.a'. Cả 2 nhánh đều trỏ về 11.a — lỗi copy-paste. Nhánh không hợp lệ phải trỏ về bước nào? Đồng thời, Bước '10.1' và '10.a' phía sau bị đánh số trùng với Bước 10 — cần chỉnh thành '11.1' và '11.a'.",
     "Nghiệp vụ",
     "Đề xuất: Nhánh không hợp lệ trỏ về '11.1' (Hiển thị thông báo lỗi). Cần sửa đánh số trong tài liệu.",
     "AI"),

]
