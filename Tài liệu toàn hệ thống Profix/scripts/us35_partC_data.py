# -*- coding: utf-8 -*-
"""
US35 Part C - Test Case Coverage Data
Phân loại câu trả lời BA → Logic chốt → Sinh SC
"""

FEATURE = "US35 – Thu phí định kỳ tự động"

# ============================================================
# PHÂN TÍCH CÂU TRẢ LỜI BA (BA Response Interpretation)
# ============================================================
BA_ANALYSIS = [
    # (ID, Dạng, Logic chốt)
    ("US35-QA-01.1", "Dạng 5", "BA xác nhận: Nếu ĐT tính phí = Customer, bước 2 kiểm tra TK mặc định → nếu không đủ ĐK → tìm TK thay thế theo quy tắc. Nếu ĐT = Account/Card → bỏ qua bước 2, sang bước 3 (đã mô tả trong bảng)."),
    ("US35-QA-01.2", "Dạng 5", "BA xác nhận: Nếu không tìm được TK thay thế nào, ProfiX vẫn ghi TK mặc định vào Topic → T24 xử lý → kết quả = Chưa thanh toán."),
    ("US35-QA-01.3", "Dạng 5", "BA xác nhận: Thứ tự ưu tiên cài đặt theo nhóm code phí ở cấp Job. Trong cùng 1 nhóm code phí, tất cả khoản phí ngang hàng."),
    ("US35-QA-01.4", "Dạng 3", "BA đã cập nhật US: Bổ sung nhánh phí ≤ 0 tại bước 3.2 → Phí thu được = 0, VAT = 0, không gửi T24."),
    ("US35-QA-01.5", "Dạng 5", "BA xác nhận: Nếu Code phí không có CTƯĐ áp dụng → Phí cần thu đi thẳng, không qua bước 5."),
    ("US35-QA-01.6", "Dạng 5", "BA xác nhận tham chiếu US02: Ngày thu = 31 → thu vào ngày cuối cùng của tháng (28/29/30)."),
    ("US35-QA-01.7", "Dạng 3", "BA đã cập nhật US: Sửa 'hiệu lực xa nhất' thành 'thời gian khởi tạo xa nhất' (tiebreak)."),
    ("US35-QA-01.8", "Dạng 5", "BA xác nhận: Trạng thái Xóa nợ được tạo trong luồng US36."),
    ("US35-QA-01.9", "Dạng 5", "BA xác nhận: Kết quả = Chưa thanh toán → KHÔNG ghi lịch sử thu phí."),
    ("US35-QA-01.10", "Dạng 3", "BA đã cập nhật US: Bổ sung Phí ≤ 0 → ghi nhận Phí thu được = 0, VAT = 0."),
    ("US35-QA-01.11", "Dạng 5", "BA xác nhận: Bước 3.4 áp Min/Max Code phí trước → kết quả đó mới vào bước 5 áp Min/Max CTƯĐ. Tuần tự, không xung đột."),
    ("US35-QA-01.12", "Dạng 3", "BA đã cập nhật tài liệu: Bổ sung tham chiếu US36 cho truy thu/tận thu."),
    ("US35-QA-01.13", "Dạng 3", "BA đã cập nhật US: Thống nhất 'Số tiền phí thực thu' = 'Số tiền phí sau ưu đãi' tại thời điểm tính phí là cùng 1 giá trị."),
    ("US35-QA-01.14", "Dạng 4", "BA từ chối: Thời điểm Job chạy do ngân hàng quyết định, phụ thuộc mốc kết thúc ngày trên Core → Drop. KHÔNG sinh SC."),
    ("US35-QA-01.15", "Dạng 1", "BA xác nhận theo đề xuất QC: Số dư = 0 → Chưa thanh toán. 0 < số dư < phí → Thanh toán một phần."),
    ("US35-QA-02.1", "Dạng 4", "BA: Pending - giải pháp BE. KHÔNG sinh SC cho QA này."),
    ("US35-QA-02.2", "Dạng 3", "BA đã cập nhật US: Lấy theo tỷ giá nhận được gần nhất từ Core."),
    ("US35-QA-02.3", "Dạng 5", "BA xác nhận: VAT = '' (chuỗi rỗng) → không có VAT → để trống VAT trong response."),
    ("US35-QA-02.4", "Dạng 5", "BA xác nhận: Khoản đã ghi Kafka → trạng thái = Đang xử lý → không bị ghi lại lần 2."),
    ("US35-QA-02.5", "Dạng 1", "BA xác nhận theo đề xuất QC: Chỉ có Min → chỉ so Min. Chỉ có Max → chỉ so Max."),
    ("US35-QA-02.6", "Dạng 5", "BA xác nhận tham chiếu US05: Nếu Min và Max đều có dữ liệu thì Min phải < Max (validate tại cài đặt Code phí)."),
    ("US35-QA-03.1", "Dạng 5", "BA: Sẽ bổ sung sau khi thống nhất NH → Chỉ viết TC theo mô tả hiện tại (3 trạng thái: HĐ, Tạm ngừng HĐ, Tạm khóa ghi có)."),
    ("US35-QA-03.2", "Dạng 5", "BA xác nhận: ProfiX vẫn sinh dữ liệu → gửi T24 → kết quả = Không thành công (Chưa thanh toán)."),
    ("US35-QA-03.3", "Dạng 5", "BA xác nhận: fee_due_list lưu cả TK mặc định + TK thay thế. fee_collection_history lưu TK ghi nợ thành công."),
    ("US35-QA-03.4", "Dạng 4", "BA: Pending - giải pháp BE. KHÔNG sinh SC cho QA này."),
    ("US35-QA-03.5", "Dạng 5", "BA xác nhận: Ngưỡng ƯĐ = 2 loại: theo số lần/số tiền GD → tham chiếu US12 về CTƯĐ không đánh giá định kỳ."),
    ("US35-QA-04.1", "Dạng 5", "BA xác nhận: Có nhiều US tra cứu/báo cáo → QC chủ động xác định phạm vi E2E."),
    ("US35-QA-04.2", "Dạng 1", "BA xác nhận theo hướng QC: Flowchart chỉ high-level, Tester đọc bảng mô tả chi tiết, không cập nhật tài liệu."),
]
