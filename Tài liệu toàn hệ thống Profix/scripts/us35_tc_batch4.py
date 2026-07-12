# -*- coding: utf-8 -*-
"""US35 TC Batch 4 (SC-55 → SC-67): Data Integrity + NFR + Bổ sung Review"""
TC_BATCH4 = [
    ("US35-TC-055","SC-55","BA QA-03.3: \"fee_due_list lưu cả TK mặc định và TK thay thế\"","Thu phí định kỳ","Update kết quả","fee_due_list lưu cả TK mặc định + thay thế; history lưu TK ghi nợ","Data Integrity","Medium",
     "1. KH có TK mặc định (VND, fail ĐK) + TK thay thế (VND, đủ ĐK)\n2. Khoản phí thu thành công bằng TK thay thế",
     "1. Kiểm tra bảng fee_due_list → có cả 2 TK (mặc định + thay thế)\n2. Kiểm tra bảng fee_collection_history → chỉ có TK thay thế (TK ghi nợ thành công)",
     "(i) Nghiệp vụ/Logic: fee_due_list lưu đầy đủ TK mặc định và TK thay thế. fee_collection_history chỉ lưu TK thực tế ghi nợ.\n(ii) UI: N/A.","BA QA-03.3 xác nhận"),

    ("US35-TC-056","SC-56","BA QA-02.4: \"trạng thái = Đang xử lý nên sẽ không bị ghi lại lần 2\"","Thu phí định kỳ","Sinh dữ liệu phí","Job retry → khoản Đang xử lý KHÔNG sinh trùng","Data Integrity","High",
     "1. Khoản phí K1: trạng thái = 'Đang xử lý' (đã ghi Kafka)\n2. Job chạy lại (retry) do lỗi mạng tạm thời",
     "1. Job trigger lại → quét danh sách khoản phí\n2. Kiểm tra K1 → TT = 'Đang xử lý' → bỏ qua\n3. Chỉ xử lý khoản phí có TT = 'Thêm mới'",
     "(i) Nghiệp vụ/Logic: Khoản phí K1 KHÔNG bị ghi lại lần 2 vào Kafka. Đảm bảo idempotency.\n(ii) UI: N/A.","BA QA-02.4 xác nhận"),

    ("US35-TC-057","SC-57","BA QA-03.5: \"Ngưỡng ƯĐ: theo số lần/số tiền GD → tham chiếu US12\"","Thu phí định kỳ","Ưu đãi CTƯĐ","KH đã chạm ngưỡng ƯĐ → CTƯĐ không áp dụng","Data Integrity","High",
     "1. CTƯĐ P1: ngưỡng ƯĐ = tối đa 5 lần GD\n2. KH đã sử dụng ƯĐ 5 lần (đã chạm ngưỡng)",
     "1. Bước 4: Kiểm tra CTƯĐ P1\n2. KH đã chạm ngưỡng 5 lần → P1 không đưa vào Danh sách D\n3. Phí thu = phí gốc (không giảm)",
     "(i) Nghiệp vụ/Logic: CTƯĐ P1 KHÔNG áp dụng do KH chạm ngưỡng. Phí thực thu = Phí cần thu.\n(ii) UI: N/A.","Tham chiếu US12"),

    ("US35-TC-058","SC-58","BA QA-01.8: \"Trạng thái Xóa nợ được tạo trong luồng US36\"","Thu phí định kỳ","Update kết quả","Trạng thái Xóa nợ KHÔNG xuất hiện trong US35","Data Integrity","Medium",
     "1. Khoản phí K1: TT = 'Chưa thanh toán' (Nợ phí)",
     "1. Trong luồng US35: K1 chỉ có thể chuyển sang TT một phần hoặc TT toàn bộ\n2. Trạng thái 'Xóa nợ' KHÔNG được tạo trong US35\n3. 'Xóa nợ' chỉ xuất hiện ở luồng US36",
     "(i) Nghiệp vụ/Logic: US35 không tạo trạng thái 'Xóa nợ'. Trạng thái này chỉ được tạo trong US36.\n(ii) UI: N/A.","BA QA-01.8"),

    ("US35-TC-059","SC-59","YCNV – \"dữ liệu lưu trữ...được đồng bộ T-1 về ProfiX theo mô tả US33\"","Thu phí định kỳ","Sinh dữ liệu phí","Dữ liệu đồng bộ T-1 từ Core → ProfiX dùng snapshot T-1","NFR","Medium",
     "1. Ngày T = 19/05/2026\n2. Dữ liệu Core đã đồng bộ T-1 (18/05/2026)",
     "1. Job chạy ngày T\n2. Hệ thống lấy dữ liệu KH/TK/Thẻ từ snapshot đồng bộ T-1\n3. Sinh khoản phí dựa trên dữ liệu T-1",
     "(i) Nghiệp vụ/Logic: ProfiX sử dụng snapshot T-1 (18/05) để sinh phí. Thay đổi trên Core ngày T chưa được phản ánh.\n(ii) UI: N/A.","Tham chiếu US33"),

    ("US35-TC-060","SC-60","BA QA-02.2: \"lấy theo tỷ giá nhận được gần nhất\"","Thu phí định kỳ","Tính phí","Tỷ giá lấy bản ghi gần nhất từ Core (không nhất thiết ngày T)","NFR","Medium",
     "1. Ngày T = 19/05/2026\n2. Bản ghi tỷ giá USD/VND gần nhất: ngày 17/05/2026 = 25,100\n3. Không có bản ghi ngày 18-19/05",
     "1. Cần quy đổi tỷ giá USD/VND\n2. Tìm bản ghi gần nhất → 17/05/2026 (25,100)\n3. Sử dụng tỷ giá 25,100 để quy đổi",
     "(i) Nghiệp vụ/Logic: Tỷ giá = 25,100 (bản ghi gần nhất 17/05). Không yêu cầu tỷ giá phải đúng ngày T.\n(ii) UI: N/A.","BA QA-02.2 đã cập nhật US"),

    ("US35-TC-061","SC-61","Bảng XLTP, Bước 3.3 – \"Nếu Loại tiền phí tối thiểu/tối đa = Loại tiền Code phí\"","Thu phí định kỳ","Tính phí","Cùng loại tiền Min/Max vs Code phí → không quy đổi","Business Logic","Medium",
     "1. Code phí: Loại tiền = VND\n2. Min/Max: Loại tiền = VND, Min = 50,000, Max = 500,000",
     "1. Loại tiền Min/Max = Loại tiền Code phí = VND → không cần quy đổi\n2. Dùng trực tiếp Min = 50,000, Max = 500,000 VND",
     "(i) Nghiệp vụ/Logic: Không quy đổi tỷ giá. Min/Max dùng trực tiếp.\n(ii) UI: N/A.",""),

    ("US35-TC-062","SC-62","Bảng XLTP, Bước 5.4 – \"Nếu Số tiền tối thiểu <= Phí sau ƯĐ <= Số tiền tối đa\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Clamping CTƯĐ: Min ≤ Phí sau ƯĐ ≤ Max → giữ nguyên","Business Logic","Medium",
     "1. CTƯĐ: Min = 20,000, Max = 200,000\n2. Phí sau ƯĐ = 80,000 VND (trong khoảng)",
     "1. So sánh: 20,000 ≤ 80,000 ≤ 200,000 → trong khoảng\n2. Phí thực thu = 80,000 VND (giữ nguyên)",
     "(i) Nghiệp vụ/Logic: Phí thực thu = 80,000 = Phí sau ƯĐ. Không clamping.\n(ii) UI: N/A.",""),

    ("US35-TC-063","SC-63","YCNV – \"chưa nhận được kết quả thu phí thì trạng thái duy trì là Đang xử lý\"","Thu phí định kỳ","Update kết quả","Chưa nhận kết quả → trạng thái duy trì 'Đang xử lý'","Business Logic","High",
     "1. Khoản phí K1 đã ghi Kafka, TT = 'Đang xử lý'\n2. T24 chưa trả kết quả (message chưa về Topic kết quả)",
     "1. ProfiX đọc Topic kết quả → không có message cho K1\n2. Trạng thái K1 duy trì = 'Đang xử lý'\n3. Không thay đổi bất kỳ dữ liệu nào",
     "(i) Nghiệp vụ/Logic: Trạng thái duy trì 'Đang xử lý' khi chưa nhận kết quả. Không tự chuyển sang trạng thái khác.\n(ii) UI: N/A.",""),

    ("US35-TC-064","SC-64","Bảng XLTP, Bước 1 – \"TK thỏa mãn ĐK theo TK và CIF thỏa mãn ĐK theo KH\"","Thu phí định kỳ","Sinh dữ liệu phí","ĐT = Account/Card: logic AND (ĐK TK AND ĐK KH)","Data Integrity","High",
     "1. ĐT = Account\n2. TK_A: thỏa ĐK theo TK (SP, loại tiền OK) nhưng CIF KHÔNG thỏa ĐK theo KH",
     "1. Kiểm tra TK_A: ĐK TK → ✓\n2. Kiểm tra CIF: ĐK KH → ✗\n3. Logic AND: TK_A ∧ CIF = FALSE → TK_A không vào danh sách C",
     "(i) Nghiệp vụ/Logic: TK_A bị loại do CIF không thỏa ĐK KH. Logic kết hợp là AND (cả 2 phải thỏa).\n(ii) UI: N/A.",""),

    ("US35-TC-065","SC-65","YCNV – \"Yêu cầu về truy thu/tận thu nợ phí sẽ được mô tả cụ thể tại US36\"","Thu phí định kỳ","Update kết quả","Kỳ nợ tiếp theo sinh phí = toàn bộ phí gốc","Data Integrity","Medium",
     "1. KH đã nợ phí kỳ trước: phí gốc = 100,000, đã thu 60,000, còn nợ 40,000\n2. Kỳ thu phí tiếp theo đến hạn",
     "1. Job chạy kỳ mới → sinh phí cho KH\n2. Phí kỳ mới = 100,000 (toàn bộ phí gốc, KHÔNG phải 40,000)\n3. Nợ cũ xử lý qua US36 (truy thu/tận thu)",
     "(i) Nghiệp vụ/Logic: Phí kỳ mới = phí gốc 100,000 (không chỉ phần thiếu). Nợ cũ xử lý riêng ở US36.\n(ii) UI: N/A.","Tham chiếu US36"),

    ("US35-TC-066","SC-66","Bảng XLTP, Bước 3.2 – \"Nếu Số tiền phí tính ra ≤ 0 thì ghi nhận Phí = 0, VAT = 0\"","Thu phí định kỳ","Tính phí","BVA: Phí tính ra = 0 (đúng bằng 0) → Phí = 0, VAT = 0","Boundary Value","High",
     "1. Code phí: QTTP = Công thức\n2. Kết quả tính = 0 VND (đúng bằng 0)",
     "1. Tính phí theo Công thức → kết quả = 0 VND\n2. Phí = 0 (≤ 0) → ghi nhận Phí thu được = 0, VAT = 0\n3. Không gửi T24",
     "(i) Nghiệp vụ/Logic: Phí = 0 (biên = 0). Phí thu được = 0, VAT = 0. KHÔNG gửi T24.\n(ii) UI: N/A.","BVA biên = 0"),

    ("US35-TC-067","SC-67","Bảng XLTP, Bước 3.2 – \"Nếu Số tiền phí tính ra ≤ 0 thì ghi nhận Phí = 0, VAT = 0\" + BA QA-01.10","Thu phí định kỳ","Ưu đãi CTƯĐ","Phí sau ƯĐ < 0 (ƯĐ số tiền giảm > phí) → Phí = 0, VAT = 0","Boundary Value","High",
     "1. Phí cần thu = 50,000 VND\n2. CTƯĐ: ƯĐ theo số tiền giảm = 80,000 VND (> phí)",
     "1. Số tiền ƯĐ = 80,000 > 50,000\n2. Phí sau ƯĐ = 50,000 - 80,000 = -30,000\n3. Phí ≤ 0 → Phí thu được = 0, VAT = 0\n4. Không gửi T24",
     "(i) Nghiệp vụ/Logic: Phí sau ƯĐ = -30,000 (< 0) → Phí thu được = 0, VAT = 0. KHÔNG gửi T24.\n(ii) UI: N/A.","BA QA-01.10"),
]
