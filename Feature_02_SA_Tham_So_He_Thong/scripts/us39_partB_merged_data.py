# US39 Part B Merged - Data file
# Format: (ID, Reference, Issue, Category, Proposal, BA_Answer, Source)

QA_DATA = [
    # ===== HM1: Nghiệp vụ / Luồng xử lý =====
    ("US39-QA-01.1",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn \"T24 sẽ gọi API để yêu cầu ProfiX tính phí tự động cho giao dịch\"",
     "Tài liệu tham chiếu US33 cho logic tính phí, nhưng US33 mô tả kênh online. Với kênh offline (T24), request/response API tính phí có khác gì so với kênh online không? Cụ thể: (1) Các tham số đầu vào API có giống nhau? (2) Kênh offline có cần truyền thêm tham số nào đặc thù (VD: mã chi nhánh, mã user T24)?",
     "Nghiệp vụ",
     "Đề xuất: BA làm rõ API spec cho kênh offline T24. Nếu hoàn toàn giống US33, cần ghi rõ \"API input/output tương tự US33, không có tham số đặc thù kênh offline\".",
     "", "AI"),

    ("US39-QA-01.2",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn văn P10: \"Với các khách hàng không tham gia Chương trình ưu đãi, phí trả nợ trước hạn sẽ áp dụng theo mức phí chung quy định tại Biểu phí dịch vụ trong từng thời kỳ\"",
     "Tài liệu ghi KH không tham gia CTƯĐ → áp dụng Biểu phí dịch vụ chung. Nhưng không mô tả luồng mapping cụ thể: (1) ProfiX dựa vào tiêu chí nào để xác định LD \"không tham gia CTƯĐ\" (thiếu Mã hạch toán? Mã hạch toán = null? Mã hạch toán không match với Code phí nào trong Biểu phí CTƯĐ)? (2) Khi xác định là KH không tham gia CTƯĐ, ProfiX tự động chuyển sang tìm Biểu phí chung hay cần cấu hình mapping riêng?",
     "Nghiệp vụ",
     "Đề xuất: Mô tả rõ logic phân nhánh: (a) Nếu LD có Mã hạch toán match → áp dụng Biểu phí CTƯĐ, (b) Nếu không match hoặc không có Mã hạch toán → fallback sang Biểu phí chung. Cần chỉ rõ điều kiện fallback.",
     "", "VA"),

    ("US39-QA-01.3",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn \"Code phí gom nhóm các bậc thang... với điều kiện Mã hạch toán tương ứng\"",
     "Tài liệu mô tả Code phí gom nhóm các bậc thang THKV của tất cả CTƯĐ cho vay có cùng điều kiện. Nếu 1 khoản vay (LD) có Mã hạch toán match với NHIỀU Code phí trong cùng Biểu phí CTƯĐ (do khai báo chồng chéo điều kiện THKV), ProfiX xử lý thế nào? Lấy Code phí nào? Có validate chống chồng chéo khi khai báo Code phí không?",
     "Nghiệp vụ",
     "Đề xuất: BA làm rõ quy tắc ưu tiên khi match nhiều Code phí. Nếu không cho phép chồng chéo, cần có validate khi khai báo Code phí.",
     "", "AI+VA"),

    ("US39-QA-01.4",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn văn P9: \"Nếu THKV>36M hoặc THKV > 70% thời hạn hợp đồng: Miễn phí\"",
     "Tài liệu mô tả điều kiện miễn phí: \"THKV > 36M HOẶC THKV > 70% thời hạn hợp đồng\". Đây là điều kiện OR (thỏa 1 trong 2 là miễn phí) hay AND (phải thỏa cả 2)? Ví dụ: Khoản vay 60 tháng, THKV = 38M → 38 > 36M (thỏa điều 1), 38/60 = 63% < 70% (không thỏa điều 2). Nếu OR → miễn phí, nếu AND → vẫn thu phí.",
     "Nghiệp vụ",
     "Đề xuất: Làm rõ toán tử logic giữa 2 điều kiện miễn phí (OR hay AND) và cung cấp ví dụ minh họa để test case boundary chính xác.",
     "", "VA"),

    ("US39-QA-01.5",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn văn P29: \"T24 hiển thị thông tin phí và cho phép người dùng sửa số tiền phí cần thu\"",
     "Người dùng nào được phép sửa số tiền phí (chỉ Maker hay cả Checker)? Việc Maker tự ý sửa số tiền phí xuống thấp hơn mức ProfiX tính có cần một cấp phê duyệt đặc biệt không? Hay T24 chỉ validate trong khoảng Min/Max rồi cho phép submit bình thường?",
     "Nghiệp vụ",
     "Đề xuất: Làm rõ quy trình phê duyệt khi số tiền phí bị sửa: chỉ Maker-Checker thông thường, hay cần cấp phê duyệt cao hơn nếu giảm phí đáng kể.",
     "", "VA"),

    ("US39-QA-01.6",
     "Lưu đồ, Bước 7→8→9 (Phê duyệt giao dịch)",
     "Flowchart chỉ vẽ luồng Checker phê duyệt thành công (happy path). Thiếu hoàn toàn nhánh Checker TỪ CHỐI giao dịch. Khi Checker từ chối: (1) Giao dịch quay về Maker để sửa lại? (2) Giao dịch bị hủy hoàn toàn? (3) ProfiX có cần nhận thông báo từ chối không?",
     "Nghiệp vụ",
     "Đề xuất: Bổ sung nhánh từ chối tại bước 7 trên Flowchart. Giao dịch bị từ chối → Maker có thể sửa và commit lại → ProfiX không nhận thông báo cho đến khi giao dịch được duyệt thành công.",
     "", "AI+VA"),

    ("US39-QA-01.7",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn văn P23: \"Phần trăm thời hạn hợp đồng (dùng để khai báo vào điều kiện 'Thời gian vay thực tế' của Code phí)\"",
     "Trường ETL \"Phần trăm thời hạn hợp đồng\" được tính như thế nào? = (Số tháng đã vay / Tổng thời hạn hợp đồng) × 100%? Giá trị này được tính tại ngày ETL (T-1) hay ngày giao dịch (T)? Tương tự vấn đề THKV, dùng T-1 có thể gây sai lệch tại ngày boundary gần mốc 70%.",
     "Nghiệp vụ",
     "Đề xuất: Làm rõ công thức tính % thời hạn hợp đồng và thời điểm tính (T-1 hay T) để đảm bảo tính chính xác khi giao dịch xảy ra gần mốc 70%.",
     "", "VA"),

    ("US39-QA-01.8",
     "Lưu đồ, Bước 6 (Decision): \"User thực hiện?\"",
     "Flowchart chỉ vẽ 2 nhánh: (1) Sửa số tiền phí → commit, (2) Nhấn commit trực tiếp. Thiếu nhánh: User KHÔNG muốn tiếp tục → Hủy giao dịch (thoát ra, bỏ giao dịch sau khi ProfiX đã tính phí nhưng chưa commit). ProfiX có cần nhận thông báo hủy không? Hay ProfiX không lưu gì nếu giao dịch không được commit?",
     "Nghiệp vụ",
     "Đề xuất: Bổ sung nhánh \"Hủy giao dịch\" tại bước 6 trên Flowchart. Nếu hủy chỉ ở phía T24 (không call API ProfiX), cần ghi rõ. ProfiX không lưu bất kỳ thông tin nào nếu giao dịch không được commit.",
     "", "AI+VA"),

    ("US39-QA-01.9",
     "Mục \"Yêu cầu nghiệp vụ\", đoạn \"Sau khi người dùng nhấn commit giao dịch, T24 sẽ chuyển giao dịch sang bước phê duyệt\"",
     "Khoảng thời gian giữa Maker commit (bước 6) và Checker duyệt (bước 7) có thể kéo dài. Trong khoảng thời gian này, nếu dữ liệu ETL được cập nhật (T-1 mới) dẫn đến THKV thay đổi → phí tính lại có thể khác. ProfiX có tính lại phí tại thời điểm Checker duyệt không? Hay dùng phí đã tính ban đầu?",
     "Nghiệp vụ",
     "Đề xuất: ProfiX KHÔNG tính lại phí khi Checker duyệt. Phí đã chốt tại thời điểm Maker commit. Tuy nhiên cần BA xác nhận.",
     "", "AI"),
]
