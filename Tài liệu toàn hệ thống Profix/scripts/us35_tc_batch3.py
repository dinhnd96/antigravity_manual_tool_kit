# -*- coding: utf-8 -*-
"""US35 TC Batch 3 (SC-38 → SC-54): Business Logic chính"""
TC_BATCH3 = [
    ("US35-TC-038","SC-38","YCNV – \"nếu có nhiều TK thỏa mãn và có cùng số dư thì lấy ngẫu nhiên\"","Thu phí định kỳ","Kiểm tra TK thu phí","Nhiều TK thay thế cùng số dư lớn nhất → lấy ngẫu nhiên","Business Logic","Medium",
     "1. ĐT = Customer, TK mặc định fail ĐK\n2. TK_A: đủ ĐK, số dư = 50,000,000\n3. TK_B: đủ ĐK, số dư = 50,000,000",
     "1. Tìm TK thay thế → TK_A, TK_B cùng số dư lớn nhất\n2. Hệ thống chọn ngẫu nhiên 1 trong 2",
     "(i) Nghiệp vụ/Logic: Hệ thống chọn 1 TK ngẫu nhiên trong các TK cùng số dư lớn nhất.\n(ii) UI: N/A.",""),

    ("US35-TC-039","SC-39","Bảng XLTP, Bước 2 – \"TK phải cùng loại tiền với loại tiền của Code phí\"","Thu phí định kỳ","Kiểm tra TK thu phí","TK mặc định khác loại tiền Code phí → fallback","Negative Path","High",
     "1. Code phí: Loại tiền = USD\n2. TK mặc định: Loại tiền = VND\n3. KH có TK_B (USD, đủ ĐK khác)",
     "1. Kiểm tra TK mặc định → loại tiền VND ≠ USD → fail ĐK 1\n2. Tìm TK thay thế → TK_B (USD) đủ ĐK\n3. Dùng TK_B",
     "(i) Nghiệp vụ/Logic: TK mặc định bị loại do khác loại tiền. Hệ thống chọn TK_B thay thế.\n(ii) UI: N/A.",""),

    ("US35-TC-040","SC-40","Bảng XLTP, Bước 2 – \"SP TK phải thuộc DS các SP được phép trích thu phí...CA_PRODUCT\"","Thu phí định kỳ","Kiểm tra TK thu phí","SP TK không thuộc CA_PRODUCT → fallback","Negative Path","High",
     "1. TK mặc định: SP = 'Tiết kiệm' (không nằm trong CA_PRODUCT)\n2. CA_PRODUCT = ['Thanh toán', 'Vãng lai']",
     "1. Kiểm tra SP → 'Tiết kiệm' ∉ CA_PRODUCT → fail ĐK 2\n2. Tìm TK thay thế có SP thuộc CA_PRODUCT",
     "(i) Nghiệp vụ/Logic: TK mặc định bị loại do SP không thuộc CA_PRODUCT.\n(ii) UI: N/A.",""),

    ("US35-TC-041","SC-41","Bảng XLTP, Bước 2 – \"Trạng thái TK được phép: HĐ, Tạm ngừng HĐ, Tạm khóa ghi có\"","Thu phí định kỳ","Kiểm tra TK thu phí","TK trạng thái không hợp lệ (VD: Đã đóng) → fallback","Negative Path","High",
     "1. TK mặc định: TT = 'Đã đóng'\n2. DS trạng thái hợp lệ: HĐ, Tạm ngừng HĐ, Tạm khóa ghi có",
     "1. Kiểm tra TT → 'Đã đóng' ∉ DS hợp lệ → fail ĐK 3\n2. Tìm TK thay thế có TT hợp lệ",
     "(i) Nghiệp vụ/Logic: TK mặc định bị loại do trạng thái 'Đã đóng' không hợp lệ.\n(ii) UI: N/A.",""),

    ("US35-TC-042","SC-42","Bảng XLTP, Bước 3.1 – \"dựa trên Nhóm KH của CIF để xác định bản ghi QTTP\"","Thu phí định kỳ","Tính phí","Code phí khai báo theo Nhóm KH → xác định QTTP theo Nhóm","Business Logic","High",
     "1. Code phí CP01: Khai báo theo Nhóm KH = 'Có'\n2. KH: CIF = 'C001', Nhóm KH = 'VIP'\n3. QTTP cho Nhóm VIP: Số cố định = 50,000 VND",
     "1. Xác định Nhóm KH của CIF C001 = 'VIP'\n2. Tìm bản ghi QTTP tương ứng → Số cố định = 50,000\n3. Tính phí = 50,000 VND",
     "(i) Nghiệp vụ/Logic: Hệ thống chọn đúng QTTP của Nhóm KH 'VIP'. Phí = 50,000 VND.\n(ii) UI: N/A.",""),

    ("US35-TC-043","SC-43","Bảng XLTP, Bước 3.3 – \"Loại tiền Code phí = VND → Tỷ giá bán giao ngay\"","Thu phí định kỳ","Tính phí","Quy đổi Min/Max: Code phí = VND, Min/Max = USD → dùng tỷ giá bán","Business Logic","High",
     "1. Code phí: Loại tiền = VND\n2. Min/Max: Loại tiền = USD, Min = 5 USD, Max = 50 USD\n3. Tỷ giá bán giao ngay USD/VND = 25,000",
     "1. Loại tiền Code phí = VND → dùng Tỷ giá bán giao ngay\n2. Min quy đổi = 5 × 25,000 = 125,000 VND\n3. Max quy đổi = 50 × 25,000 = 1,250,000 VND",
     "(i) Nghiệp vụ/Logic: Min = 125,000 VND, Max = 1,250,000 VND. Dùng tỷ giá bán giao ngay.\n(ii) UI: N/A.",""),

    ("US35-TC-044","SC-44","Bảng XLTP, Bước 3.3 – \"Loại tiền Code phí <> VND → Tỷ giá chéo T3 = T1/T2\"","Thu phí định kỳ","Tính phí","Quy đổi khi cả 2 loại tiền ≠ VND → tỷ giá chéo","Business Logic","High",
     "1. Code phí: Loại tiền = USD\n2. Min/Max: Loại tiền = EUR\n3. T1 (EUR/VND bán) = 27,500, T2 (USD/VND mua) = 24,500",
     "1. Cả 2 loại tiền ≠ VND → dùng Tỷ giá chéo\n2. T3 = T1/T2 = 27,500/24,500 = 1.1224...\n3. Min(EUR) × T3 = Min quy đổi (USD)",
     "(i) Nghiệp vụ/Logic: Tỷ giá chéo T3 = T1/T2. Min/Max quy đổi sang USD đúng tỷ giá.\n(ii) UI: N/A.",""),

    ("US35-TC-045","SC-45","Bảng XLTP, Bước 4 – \"Trường hợp 1: CTƯĐ không đánh giá định kỳ\"","Thu phí định kỳ","Ưu đãi CTƯĐ","CTƯĐ TH1: không đánh giá định kỳ → kiểm tra 5 ĐK","Business Logic","High",
     "1. CTƯĐ P1: Loại = Không đánh giá định kỳ\n2. SPDV cấp cuối Code phí nằm trong DS SPDV của CTƯĐ\n3. KH thỏa ĐK KH, TK thỏa ĐK TK\n4. KH nằm trong DS KH\n5. KH chưa chạm ngưỡng ƯĐ",
     "1. Kiểm tra SPDV cấp cuối → ✓\n2. Kiểm tra ĐK KH → ✓\n3. Kiểm tra ĐK TK/Thẻ → ✓\n4. Kiểm tra DS KH → ✓\n5. Kiểm tra ngưỡng ƯĐ → chưa chạm → ✓\n6. CTƯĐ P1 vào Danh sách D",
     "(i) Nghiệp vụ/Logic: CTƯĐ P1 đủ 5 ĐK → được đưa vào Danh sách D để xét ƯĐ.\n(ii) UI: N/A.","Tham chiếu US12"),

    ("US35-TC-046","SC-46","Bảng XLTP, Bước 4 – \"Trường hợp 2: CTƯĐ có đánh giá định kỳ\"","Thu phí định kỳ","Ưu đãi CTƯĐ","CTƯĐ TH2: có đánh giá định kỳ → kiểm tra SPDV + DS KH chu kỳ","Business Logic","High",
     "1. CTƯĐ P2: Loại = Có đánh giá định kỳ\n2. SPDV cấp cuối nằm trong DS SPDV của CTƯĐ\n3. KH đã nằm trong DS KH xác định theo chu kỳ đánh giá",
     "1. Kiểm tra SPDV cấp cuối → ✓\n2. Kiểm tra DS KH theo chu kỳ đánh giá → KH nằm trong DS → ✓\n3. CTƯĐ P2 vào Danh sách D",
     "(i) Nghiệp vụ/Logic: CTƯĐ P2 thỏa 2 ĐK → vào Danh sách D.\n(ii) UI: N/A.","Tham chiếu US12"),

    ("US35-TC-047","SC-47","Bảng XLTP, Bước 5.2 – \"Lấy CTƯĐ có Số tiền ƯĐ lớn nhất...thời gian khởi tạo xa nhất\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Nhiều CTƯĐ → chọn ƯĐ lớn nhất. Bằng nhau → khởi tạo xa nhất","Business Logic","High",
     "1. CTƯĐ P1: ƯĐ = 20,000, khởi tạo 01/01/2025\n2. CTƯĐ P2: ƯĐ = 30,000, khởi tạo 15/06/2025\n3. CTƯĐ P3: ƯĐ = 30,000, khởi tạo 01/03/2025",
     "1. So sánh ƯĐ: P2 (30K) = P3 (30K) > P1 (20K)\n2. P1 bị loại\n3. Tiebreak P2 vs P3: khởi tạo xa nhất → P3 (01/03/2025 < 15/06/2025)\n4. Chọn CTƯĐ P3",
     "(i) Nghiệp vụ/Logic: Hệ thống chọn CTƯĐ P3 (ƯĐ lớn nhất + khởi tạo xa nhất). Số tiền ƯĐ = 30,000.\n(ii) UI: N/A.","BA QA-01.7 đã sửa 'hiệu lực xa nhất' → 'khởi tạo xa nhất'"),

    ("US35-TC-048","SC-48","BA QA-01.5: \"Không có CTƯĐ → Phí cần thu đi thẳng, không qua bước 5\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Không có CTƯĐ áp dụng → bỏ qua bước 5","Business Logic","Medium",
     "1. Code phí CP01 không có CTƯĐ nào áp dụng\n2. Phí cần thu = 100,000 VND",
     "1. Bước 4: Kiểm tra CTƯĐ → không tìm thấy CTƯĐ nào\n2. Bỏ qua bước 5 (không tính ƯĐ)\n3. Phí thực thu = 100,000 VND → chuyển thẳng bước 6",
     "(i) Nghiệp vụ/Logic: Không áp dụng ƯĐ. Phí thực thu = Phí cần thu = 100,000 VND.\n(ii) UI: N/A.","BA QA-01.5 xác nhận"),

    ("US35-TC-049","SC-49","Bảng XLTP, Bước 5.3 – \"Quy đổi Số tiền tối thiểu, Số tiền tối đa\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Quy đổi Min/Max CTƯĐ khi khác loại tiền (tương tự bước 3.3)","Business Logic","Medium",
     "1. CTƯĐ: Min = 10 USD, Max = 100 USD\n2. Code phí: Loại tiền = VND\n3. Tỷ giá bán giao ngay USD/VND = 25,000",
     "1. Loại tiền Code phí = VND → dùng tỷ giá bán\n2. Min quy đổi = 10 × 25,000 = 250,000 VND\n3. Max quy đổi = 100 × 25,000 = 2,500,000 VND",
     "(i) Nghiệp vụ/Logic: Min CTƯĐ = 250,000, Max CTƯĐ = 2,500,000 VND. Quy đổi tương tự bước 3.3.\n(ii) UI: N/A.",""),

    ("US35-TC-050","SC-50","BA QA-01.11: \"Bước 3.4 áp trước, kết quả đó vào bước 5\"","Thu phí định kỳ","Tính phí","Thứ tự: Min/Max Code phí (3.4) trước → Min/Max CTƯĐ (5.4) sau","Business Logic","High",
     "1. Code phí: Min = 50,000, Max = 500,000\n2. CTƯĐ: ƯĐ = 20%, Min CTƯĐ = 30,000, Max CTƯĐ = 400,000\n3. Phí gốc = 40,000 VND (< Min Code phí)",
     "1. Bước 3.4: 40,000 < 50,000 → clamp = 50,000 (áp Min Code phí)\n2. Bước 5.1: ƯĐ = 20% × 50,000 = 10,000 → Phí sau ƯĐ = 40,000\n3. Bước 5.4: 40,000 ≥ 30,000 (Min CTƯĐ) → giữ nguyên\n4. Phí thực thu = 40,000 VND",
     "(i) Nghiệp vụ/Logic: Min/Max Code phí áp TRƯỚC (bước 3.4) → kết quả đó mới vào bước 5 (Min/Max CTƯĐ). Tuần tự, không xung đột.\n(ii) UI: N/A.","BA QA-01.11 xác nhận"),

    ("US35-TC-051","SC-51","YCNV – \"cho phép cài đặt thứ tự ưu tiên...theo nhóm code phí\"","Thu phí định kỳ","Sinh dữ liệu phí","Thứ tự ưu tiên ghi Kafka theo nhóm code phí","Business Logic","Medium",
     "1. Job A: Nhóm 'SMS' ưu tiên = 1, Nhóm 'Quản lý TK' ưu tiên = 2\n2. Có khoản phí thuộc cả 2 nhóm",
     "1. Hệ thống sắp xếp khoản phí theo ưu tiên nhóm\n2. Ghi nhóm SMS (ưu tiên 1) trước\n3. Ghi nhóm Quản lý TK (ưu tiên 2) sau",
     "(i) Nghiệp vụ/Logic: Khoản phí được ghi vào Kafka theo thứ tự ưu tiên nhóm code phí đã cài đặt.\n(ii) UI: N/A.",""),

    ("US35-TC-052","SC-52","YCNV – \"Thêm mới: chưa gửi yêu cầu\" → \"Đang xử lý: đã ghi vào Topic\"","Thu phí định kỳ","Update kết quả","Trạng thái: Thêm mới → Đang xử lý (sau ghi Kafka)","Business Logic","High",
     "1. Khoản phí vừa được sinh, trạng thái = 'Thêm mới'",
     "1. Hệ thống ghi khoản phí vào Topic Kafka\n2. Sau khi ghi thành công → cập nhật trạng thái = 'Đang xử lý'",
     "(i) Nghiệp vụ/Logic: Trạng thái chuyển từ 'Thêm mới' → 'Đang xử lý' sau khi ghi Kafka thành công.\n(ii) UI: N/A.",""),

    ("US35-TC-053","SC-53","YCNV – \"cho phép cài đặt có truy thu/tận thu theo nhóm code phí...US36\"","Thu phí định kỳ","Update kết quả","Nợ phí + cài đặt truy thu/tận thu → tham chiếu US36","Business Logic","Medium",
     "1. Khoản phí: TT = 'Thanh toán một phần' → Nợ phí\n2. Nhóm code phí: cài đặt Truy thu = Có",
     "1. Xác định khoản phí là Nợ phí\n2. Kiểm tra cài đặt nhóm: Truy thu = Có\n3. Khoản phí chuyển sang luồng US36 (truy thu/tận thu)",
     "(i) Nghiệp vụ/Logic: Nợ phí + cài đặt Truy thu = Có → khoản phí vào luồng US36.\n(ii) UI: N/A.","Tham chiếu US36"),

    ("US35-TC-054","SC-54","Bảng XLTP, Bước 2 – \"TK thay thế chỉ...phí đúng hạn, không áp dụng cho truy thu/tận thu\"","Thu phí định kỳ","Kiểm tra TK thu phí","TK thay thế chỉ dùng cho phí đúng hạn","Business Logic","High",
     "1. Khoản phí = phí truy thu (không phải đúng hạn)\n2. TK mặc định fail ĐK",
     "1. Hệ thống kiểm tra: phí = truy thu → không tìm TK thay thế\n2. Ghi TK mặc định (dù fail ĐK)\n3. Gửi T24 → T24 xử lý",
     "(i) Nghiệp vụ/Logic: TK thay thế KHÔNG áp dụng cho truy thu/tận thu. Chỉ dùng TK mặc định.\n(ii) UI: N/A.",""),
]
