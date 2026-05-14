# US38 Part B Merged Data - AI + VA consolidated
# Format: (ID, Reference, Question, Category, Proposal, BA_Answer, Source)

QA_DATA = [
    # ===== HM1: Nghiệp vụ / Luồng xử lý =====
    ("US38-QA-01.1",
     "Mục Yêu cầu nghiệp vụ, đoạn mô tả kỳ thu phí đầu tiên (tham chiếu US34)",
     "Tài liệu ghi: 'T24 sẽ gọi API để yêu cầu ProfiX tính phí cho kỳ thu phí đầu tiên tương tự như US34'. Câu hỏi: Trong trường hợp T24 gọi API ProfiX lần đầu khi phát hành bảo lãnh, ProfiX cần những thông tin đầu vào gì từ T24? API spec (request/response) cho lần call này có giống hoàn toàn với API tính phí kênh quầy tại US34 không?",
     "Nghiệp vụ",
     "Đề xuất: BA/SA cần xác nhận API spec cho lần call đầu tiên: danh sách tham số đầu vào (CIF, Số MD, Giá trị bảo lãnh, Loại tiền, Sản phẩm BL...) và response (số tiền phí, mã giao dịch...).",
     "", "VA"),

    ("US38-QA-01.2",
     "Mục Yêu cầu nghiệp vụ, đoạn khoảng thời gian tính phí kỳ đầu",
     "Tài liệu ghi 'khoảng thời gian tính phí gửi cho ProfiX là số ngày của tháng hiện tại' (VD: 07/05 → 31 ngày). Điều này có nghĩa phí kỳ đầu luôn tính cho NGUYÊN THÁNG bất kể ngày phát hành nằm giữa tháng? Hay tính theo số ngày thực tế từ ngày phát hành đến cuối tháng (07/05 → 31/05 = 25 ngày)?",
     "Nghiệp vụ",
     "Đề xuất: BA làm rõ 'số ngày của tháng hiện tại' là (a) tổng số ngày lịch của tháng (31) hay (b) số ngày còn lại từ ngày phát hành. Nếu (a), KH bị tính phí nhiều hơn thực tế sử dụng kỳ đầu.",
     "", "AI+VA"),

    ("US38-QA-01.3",
     "Mục Yêu cầu nghiệp vụ, đoạn batch job đầu ngày và thu phí định kỳ tiếp theo",
     "Tài liệu ghi ProfiX tự động kiểm tra khoản bảo lãnh đến hạn thu phí 'trong ngày'. Câu hỏi: Ngày đến hạn kỳ thu phí tiếp theo (sau kỳ đầu) được tính thế nào? VD: Phát hành ngày 07/05 → kỳ 2 là ngày 07/06 (cộng 1 tháng) hay là ngày 01/06 (đầu tháng tiếp theo)? Nếu ngày phát hành = 31/01 thì kỳ tiếp theo tháng 2 (chỉ 28 ngày) xử lý ra sao?",
     "Nghiệp vụ",
     "Đề xuất: BA cần làm rõ quy tắc tính ngày đến hạn kỳ tiếp theo với ví dụ cụ thể, bao gồm edge case tháng có số ngày khác nhau.",
     "", "VA"),

    ("US38-QA-01.4",
     "Mục Yêu cầu nghiệp vụ, đoạn 'Thu phí tự động = Không → hệ thống không xử lý gì tiếp theo'",
     "Khi Thu phí tự động = Không, hệ thống có ghi nhận kỳ phí đến hạn vào danh sách 'Chờ thu thủ công' không? Hay kỳ phí đó bị bỏ qua hoàn toàn và không có cơ chế nhắc nhở người dùng thu thủ công? Nếu bị bỏ qua, làm sao biết kỳ nào đến hạn mà chưa thu?",
     "Nghiệp vụ",
     "Đề xuất: Bổ sung cơ chế ghi nhận kỳ phí đến hạn ở trạng thái 'Chờ thu thủ công' khi Thu phí tự động = Không, để người dùng có danh sách cần xử lý.",
     "", "VA"),

    ("US38-QA-01.5",
     "Bảng TABLE 1 – Bước 5-8, Flowchart 2 bước 6-7",
     "Maker commit giao dịch → T24 gọi API ProfiX lần 2 để kiểm tra trạng thái. Câu hỏi: (a) Tại sao phải gọi API 2 lần (bước 2 và bước 6)? (b) Trạng thái 'không hợp lệ' cụ thể là gì? VD: kỳ thu phí đã được batch job tự động thanh toán giữa lúc Maker chọn (bước 5) và commit (bước 6)?",
     "Nghiệp vụ",
     "Đề xuất: BA liệt kê các trạng thái thanh toán hợp lệ/không hợp lệ và xác nhận mục đích gọi API lần 2 (double-check race condition).",
     "", "AI+VA"),

    ("US38-QA-01.6",
     "Flowchart 2 – Bước 8.1 (Hiển thị thông báo lỗi)",
     "Nhánh 'Trạng thái không hợp lệ' chỉ đến bước 8.1 'Hiển thị thông báo lỗi' và KHÔNG có mũi tên quay lại hay kết thúc. Sau khi báo lỗi, Maker có thể chọn lại kỳ khác không? Hay giao dịch bị hủy hoàn toàn?",
     "Nghiệp vụ",
     "Đề xuất: Bổ sung nhánh sau bước 8.1: (a) Maker quay về bước 5 chọn lại kỳ, HOẶC (b) Giao dịch rollback, Maker tạo lại từ đầu.",
     "", "AI+VA"),

    ("US38-QA-01.7",
     "Mục Yêu cầu nghiệp vụ, trường ETL 'Tần suất thu phí = Tháng/Quý'",
     "Toàn bộ phần yêu cầu chỉ mô tả logic thu 1 tháng/lần. Nếu Tần suất = Quý: (a) Kỳ đầu tính phí bao nhiêu ngày? (b) Kỳ tiếp theo: 07/05 → 07/08 (cộng 3 tháng) hay 01/07 (đầu quý)? (c) Công thức tính số ngày phí kỳ Quý?",
     "Nghiệp vụ",
     "Đề xuất: BA làm rõ logic Tần suất = Quý với ví dụ cụ thể gồm ngày đến hạn và số ngày tính phí.",
     "", "AI+VA"),

    ("US38-QA-01.8",
     "Mục Yêu cầu nghiệp vụ, đoạn đồng bộ vào bảng ETL Tài khoản",
     "Bảo lãnh phát hành lúc 16:00, DWH batch ETL chạy lúc 23:00 cùng ngày, dữ liệu có mặt ProfiX vào T+1. Kỳ phí định kỳ thứ 2 có được tính đúng không nếu dữ liệu nguồn chậm 1 ngày?",
     "Nghiệp vụ",
     "Đề xuất: Xác định SLA của DWH ETL (thời điểm hoàn thành đồng bộ) và ảnh hưởng đến tính phí kỳ tiếp theo.",
     "", "VA"),

    ("US38-QA-01.9",
     "Flowchart 2 – Bước 9 (Checker phê duyệt giao dịch)",
     "Tài liệu không mô tả luồng Checker TỪ CHỐI phê duyệt. Khi từ chối: (a) Giao dịch về trạng thái nào? (b) Maker có thể chỉnh sửa và submit lại? (c) Các kỳ thu phí đã chọn có bị lock trong thời gian chờ duyệt?",
     "Nghiệp vụ",
     "Đề xuất: BA bổ sung luồng Checker từ chối vào Flowchart, xác định trạng thái giao dịch sau từ chối và cơ chế lock/unlock kỳ thu phí.",
     "", "AI"),

    ("US38-QA-01.10",
     "Mục Yêu cầu nghiệp vụ, đoạn thu phí kỳ đầu tham chiếu US34",
     "Khoản bảo lãnh chưa xác định thời hạn có được phép miễn/giảm phí theo CTƯĐ không? Nếu có, CTƯĐ áp dụng kỳ đầu có hiệu lực xuyên suốt các kỳ định kỳ sau không?",
     "Nghiệp vụ",
     "Đề xuất: BA xác nhận bảo lãnh chưa xác định thời hạn có nằm trong scope CTƯĐ hay không, và hiệu lực CTƯĐ xuyên kỳ hay chỉ kỳ đầu.",
     "", "AI"),

    ("US38-QA-01.11",
     "Bảng TABLE 1 – Bước 5 (Maker lựa chọn các kỳ cần thu)",
     "Maker chọn nhiều kỳ cùng lúc. Nếu bước 8 phát hiện 1 kỳ không hợp lệ: (a) Cả batch bị rollback (all-or-nothing) hay chỉ reject kỳ lỗi (partial)? (b) Maker có thấy breakdown phí từng kỳ trước khi commit?",
     "Nghiệp vụ",
     "Đề xuất: BA xác nhận cơ chế all-or-nothing hay partial success khi multi-select, và Maker có thấy chi tiết phí từng kỳ không.",
     "", "AI"),
]
