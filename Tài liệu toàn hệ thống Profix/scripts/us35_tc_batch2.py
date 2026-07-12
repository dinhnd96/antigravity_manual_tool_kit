# -*- coding: utf-8 -*-
"""US35 TC Batch 2 (SC-18 → SC-37): Negative + BVA + Field Validation"""
TC_BATCH2 = [
    ("US35-TC-018","SC-18","Bảng XLTP, Bước 3.2 – \"Nếu Số tiền phí tính ra ≤ 0 thì ghi nhận Phí = 0, VAT = 0\"","Thu phí định kỳ","Tính phí","Công thức tính ra Phí ≤ 0 → Phí = 0, VAT = 0, không gửi T24","Negative Path","High",
     "1. Code phí có QTTP = Công thức\n2. Kết quả tính theo cấu phần = -5,000 VND (< 0)",
     "1. Tính phí theo Công thức → kết quả = -5,000 VND\n2. Phí ≤ 0 → ghi nhận Phí thu được = 0, VAT = 0\n3. Không gửi khoản phí này sang T24",
     "(i) Nghiệp vụ/Logic: Phí thu được = 0, VAT = 0. Khoản phí KHÔNG được gửi sang T24.\n(ii) UI: N/A.","BA đã cập nhật US"),

    ("US35-TC-019","SC-19","Bảng XLTP, Bước 3.3 – \"Nếu không tồn tại Tỷ giá phù hợp...thì báo lỗi\"","Thu phí định kỳ","Tính phí","Không tồn tại Tỷ giá khi quy đổi Min/Max Code phí → báo lỗi","Negative Path","High",
     "1. Code phí: Loại tiền = USD, Min/Max loại tiền = EUR\n2. Không có bản ghi tỷ giá EUR/VND trong dữ liệu tỷ giá",
     "1. Cần quy đổi Min/Max → lấy tỷ giá EUR/VND\n2. Không tìm được tỷ giá phù hợp\n3. Hệ thống báo lỗi không tìm thấy tỷ giá",
     "(i) Nghiệp vụ/Logic: Hệ thống báo lỗi \"không tìm thấy tỷ giá tương ứng\". Khoản phí không được tính.\n(ii) UI: N/A.",""),

    ("US35-TC-020","SC-20","Bảng XLTP, Bước 5.3 – \"Nếu không tồn tại Tỷ giá phù hợp...thì báo lỗi\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Không tồn tại Tỷ giá khi quy đổi Min/Max CTƯĐ → báo lỗi","Negative Path","High",
     "1. CTƯĐ có Min/Max với loại tiền = GBP\n2. Code phí loại tiền = VND\n3. Tỷ giá GBP/VND = 0 (giá trị không hợp lệ)",
     "1. Cần quy đổi Min/Max CTƯĐ → lấy tỷ giá GBP/VND\n2. Tìm được tỷ giá nhưng giá trị = 0\n3. Hệ thống báo lỗi không tìm thấy tỷ giá",
     "(i) Nghiệp vụ/Logic: Tỷ giá = 0 → coi như không hợp lệ → báo lỗi. Khoản phí không tính ƯĐ.\n(ii) UI: N/A.",""),

    ("US35-TC-021","SC-21","BA QA-01.9: \"Chưa thanh toán thì ko ghi nhận vào lịch sử\"","Thu phí định kỳ","Update kết quả","T24 trả Chưa thanh toán → KHÔNG ghi lịch sử","Negative Path","High",
     "1. Khoản phí đã gửi T24\n2. Số dư TK = 0",
     "1. T24 trả kết quả = 'Chưa thanh toán'\n2. ProfiX đọc message kết quả\n3. Kiểm tra: KHÔNG ghi vào lịch sử thu phí\n4. Cập nhật trạng thái kỳ nợ = 'Chưa thanh toán'",
     "(i) Nghiệp vụ/Logic: Lịch sử thu phí KHÔNG được ghi nhận. Trạng thái = 'Chưa thanh toán'. Khoản phí = Nợ phí.\n(ii) UI: N/A.","BA QA-01.9 xác nhận"),

    ("US35-TC-022","SC-22","BA QA-03.2: \"ProfiX vẫn sinh dữ liệu...kết quả chắc chắn = Không thành công\"","Thu phí định kỳ","Update kết quả","TK đóng trên Core (chênh T-1) → T24 trả Không thành công","Negative Path","High",
     "1. TK mặc định KH trạng thái 'Hoạt động' trên ProfiX (dữ liệu T-1)\n2. Trên Core T24, TK đã bị đóng trong khoảng T-1→T",
     "1. ProfiX dùng dữ liệu T-1 → TK vẫn hợp lệ → sinh khoản phí\n2. Ghi vào Kafka → T24 nhận\n3. T24 kiểm tra TK đã đóng → trả 'Chưa thanh toán'\n4. ProfiX cập nhật trạng thái = 'Chưa thanh toán'",
     "(i) Nghiệp vụ/Logic: ProfiX vẫn sinh dữ liệu phí (dùng T-1). T24 trả kết quả = 'Chưa thanh toán' do TK không hợp lệ.\n(ii) UI: N/A.",""),

    ("US35-TC-023","SC-23","Bảng XLTP, Bước 3.4 – \"Nếu Số tiền tối thiểu <= Phí <= Số tiền tối đa\"","Thu phí định kỳ","Tính phí","BVA: Phí = Min (biên dưới) → giữ nguyên","Boundary Value","Medium",
     "1. Code phí: Min = 50,000, Max = 500,000 VND\n2. Phí đã tính = 50,000 VND (= Min)",
     "1. So sánh: Phí (50,000) = Min (50,000) → nằm trong khoảng\n2. Phí cần thu = 50,000 VND (giữ nguyên)",
     "(i) Nghiệp vụ/Logic: Phí cần thu = 50,000 = Phí đã tính = Min. Không clamping.\n(ii) UI: N/A.","BVA biên dưới"),

    ("US35-TC-024","SC-24","Bảng XLTP, Bước 3.4 – \"Nếu Phí < Số tiền tối thiểu thì Phí = Số tiền tối thiểu\"","Thu phí định kỳ","Tính phí","Phí < Min → Phí cần thu = Min (clamping dưới)","Business Logic","High",
     "1. Code phí: Min = 50,000, Max = 500,000 VND\n2. Phí đã tính = 30,000 VND (< Min)",
     "1. So sánh: 30,000 < 50,000 (Min)\n2. Áp dụng clamping: Phí cần thu = 50,000 VND (Min)",
     "(i) Nghiệp vụ/Logic: Phí cần thu = 50,000 VND = Min. Clamping dưới áp dụng.\n(ii) UI: N/A.",""),

    ("US35-TC-025","SC-25","Bảng XLTP, Bước 3.4 – \"Nếu Phí > Số tiền tối đa thì Phí = Số tiền tối đa\"","Thu phí định kỳ","Tính phí","Phí > Max → Phí cần thu = Max (clamping trên)","Business Logic","High",
     "1. Code phí: Min = 50,000, Max = 500,000 VND\n2. Phí đã tính = 600,000 VND (> Max)",
     "1. So sánh: 600,000 > 500,000 (Max)\n2. Áp dụng clamping: Phí cần thu = 500,000 VND (Max)",
     "(i) Nghiệp vụ/Logic: Phí cần thu = 500,000 VND = Max. Clamping trên áp dụng.\n(ii) UI: N/A.",""),

    ("US35-TC-026","SC-26","Bảng XLTP, Bước 3.4 – \"Nếu Số tiền tối thiểu <= Phí <= Số tiền tối đa\"","Thu phí định kỳ","Tính phí","BVA: Phí = Max (biên trên) → giữ nguyên","Boundary Value","Medium",
     "1. Code phí: Min = 50,000, Max = 500,000 VND\n2. Phí đã tính = 500,000 VND (= Max)",
     "1. So sánh: Phí (500,000) = Max (500,000) → trong khoảng\n2. Phí cần thu = 500,000 VND",
     "(i) Nghiệp vụ/Logic: Phí cần thu = 500,000 = Max = Phí đã tính. Không clamping.\n(ii) UI: N/A.","BVA biên trên"),

    ("US35-TC-027","SC-27","BA QA-02.5: \"Chỉ có Min → chỉ so Min\"","Thu phí định kỳ","Tính phí","Code phí chỉ có Min (Max = null) → chỉ so Min","Boundary Value","Medium",
     "1. Code phí: Min = 50,000, Max = null\n2. Phí đã tính = 30,000 VND (< Min)",
     "1. Kiểm tra: Max = null → bỏ qua so sánh Max\n2. So sánh Min: 30,000 < 50,000 → Phí = 50,000 (Min)",
     "(i) Nghiệp vụ/Logic: Chỉ áp dụng Min. Phí cần thu = 50,000. Max không kiểm tra.\n(ii) UI: N/A.","BA xác nhận theo đề xuất QC"),

    ("US35-TC-028","SC-28","BA QA-02.5: \"Chỉ có Max → chỉ so Max\"","Thu phí định kỳ","Tính phí","Code phí chỉ có Max (Min = null) → chỉ so Max","Boundary Value","Medium",
     "1. Code phí: Min = null, Max = 500,000\n2. Phí đã tính = 600,000 VND (> Max)",
     "1. Kiểm tra: Min = null → bỏ qua so sánh Min\n2. So sánh Max: 600,000 > 500,000 → Phí = 500,000 (Max)",
     "(i) Nghiệp vụ/Logic: Chỉ áp dụng Max. Phí cần thu = 500,000. Min không kiểm tra.\n(ii) UI: N/A.","BA xác nhận theo đề xuất QC"),

    ("US35-TC-029","SC-29","Bảng XLTP, Bước 5.4 – \"Nếu Phí sau ƯĐ < Số tiền tối thiểu\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Phí sau ƯĐ < Min CTƯĐ → Phí thực thu = Min","Business Logic","High",
     "1. CTƯĐ có Min = 20,000, Max = 200,000\n2. Phí sau ƯĐ = 10,000 VND (< Min CTƯĐ)",
     "1. So sánh: 10,000 < 20,000 (Min CTƯĐ)\n2. Phí thực thu = 20,000 VND (Min CTƯĐ)",
     "(i) Nghiệp vụ/Logic: Phí thực thu = 20,000 = Min CTƯĐ. Clamping CTƯĐ dưới áp dụng.\n(ii) UI: N/A.",""),

    ("US35-TC-030","SC-30","Bảng XLTP, Bước 5.4 – \"Nếu Phí sau ƯĐ > Số tiền tối đa\"","Thu phí định kỳ","Ưu đãi CTƯĐ","Phí sau ƯĐ > Max CTƯĐ → Phí thực thu = Max","Business Logic","High",
     "1. CTƯĐ có Min = 20,000, Max = 200,000\n2. Phí sau ƯĐ = 250,000 VND (> Max CTƯĐ)",
     "1. So sánh: 250,000 > 200,000 (Max CTƯĐ)\n2. Phí thực thu = 200,000 VND (Max CTƯĐ)",
     "(i) Nghiệp vụ/Logic: Phí thực thu = 200,000 = Max CTƯĐ. Clamping CTƯĐ trên áp dụng.\n(ii) UI: N/A.",""),

    ("US35-TC-031","SC-31","Bảng XLTP, Bước 3.2 – \"Phí ≤ 0 → Phí = 0, VAT = 0\" (BA QA-01.10)","Thu phí định kỳ","Ưu đãi CTƯĐ","ƯĐ 100% → Phí sau ƯĐ = 0 → Phí = 0, VAT = 0","Boundary Value","High",
     "1. Phí cần thu = 100,000 VND\n2. CTƯĐ: Ưu đãi theo tỷ lệ = Yes, Tỷ lệ = 100%",
     "1. Số tiền ƯĐ = 100% × 100,000 = 100,000\n2. Phí sau ƯĐ = 100,000 - 100,000 = 0\n3. Phí ≤ 0 → Phí thu được = 0, VAT = 0\n4. Không gửi T24",
     "(i) Nghiệp vụ/Logic: Phí thu được = 0, VAT = 0. Khoản phí KHÔNG gửi sang T24.\n(ii) UI: N/A.","BA QA-01.10"),

    ("US35-TC-032","SC-32","BA QA-01.15: \"Số dư = 0 → Chưa thanh toán\"","Thu phí định kỳ","Update kết quả","BVA: Số dư TK = 0 → Chưa thanh toán (không phải TT một phần)","Boundary Value","High",
     "1. Phí cần thu = 100,000 VND\n2. Số dư TK = 0 VND",
     "1. T24 nhận khoản phí → kiểm tra số dư = 0\n2. Không thể thu bất kỳ đồng nào\n3. Trả kết quả = 'Chưa thanh toán' (KHÔNG phải 'TT một phần')",
     "(i) Nghiệp vụ/Logic: Kết quả = 'Chưa thanh toán'. Số dư = 0 → KHÔNG được phân loại thành 'Thanh toán một phần'.\n(ii) UI: N/A.","BA QA-01.15 xác nhận"),

    ("US35-TC-033","SC-33","BA QA-01.15: \"0 < số dư < phí → Thanh toán một phần\"","Thu phí định kỳ","Update kết quả","BVA: 0 < Số dư < Phí → Thanh toán một phần","Boundary Value","High",
     "1. Phí cần thu = 100,000 VND\n2. Số dư TK = 1 VND (> 0 nhưng < phí)",
     "1. T24 nhận → số dư = 1 VND > 0\n2. Tận thu 1 VND\n3. Trả kết quả = 'Thanh toán một phần'",
     "(i) Nghiệp vụ/Logic: Kết quả = 'Thanh toán một phần'. Số tiền thu được = 1 VND. Nợ phí = 99,999.\n(ii) UI: N/A.","BVA biên dưới TT một phần"),

    ("US35-TC-034","SC-34","BA QA-01.6 + US02: \"ngày 31 → thu vào ngày cuối cùng của các tháng\"","Thu phí định kỳ","Sinh dữ liệu phí","Ngày cố định = 31, tháng 2 → chạy ngày 28/29","Boundary Value","Medium",
     "1. Code phí: ngày thu định kỳ = 31\n2. Tháng 2/2026 (28 ngày, không nhuận)",
     "1. Đầu tháng 2, Job xác định lịch chạy ngày 31\n2. Tháng 2 chỉ có 28 ngày → chạy ngày 28/02/2026\n3. Sinh khoản phí đúng hạn",
     "(i) Nghiệp vụ/Logic: Job chạy vào ngày 28/02/2026 (ngày cuối tháng 2). Khoản phí sinh đúng hạn.\n(ii) UI: N/A.","Tham chiếu US02"),

    ("US35-TC-035","SC-35","Bảng XLTP, Bước 6 – \"VND/JPY thì làm tròn đến số nguyên\"","Thu phí định kỳ","Tính VAT","Loại tiền VND → làm tròn VAT + Phí đến số nguyên","Field Validation","Medium",
     "1. Code phí loại tiền = VND, VAT ≠ ''\n2. Phí thực thu = 99,999 VND, VAT = Có",
     "1. VAT = 99,999/110×10 = 9,090.818...\n2. Làm tròn VAT = 9,091 VND (số nguyên)\n3. Phí thu được = 99,999 - 9,091 = 90,908 VND",
     "(i) Nghiệp vụ/Logic: VAT và Phí thu được đều là số nguyên (không có thập phân). Làm tròn chỉ áp dụng ở kết quả cuối.\n(ii) UI: N/A.","[QTC-01.4]"),

    ("US35-TC-036","SC-36","Bảng XLTP, Bước 6 – \"Loại tiền # VND,JPY → 02 chữ số thập phân\"","Thu phí định kỳ","Tính VAT","Loại tiền USD → làm tròn đến 2 chữ số thập phân","Field Validation","Medium",
     "1. Code phí loại tiền = USD, VAT ≠ ''\n2. Phí thực thu = 99.99 USD, VAT = Có",
     "1. VAT = 99.99/110×10 = 9.09\n2. Làm tròn → 9.09 USD (2 chữ số thập phân)\n3. Phí thu được = 99.99 - 9.09 = 90.90 USD",
     "(i) Nghiệp vụ/Logic: VAT = 9.09 USD, Phí thu được = 90.90 USD. Đều có 2 chữ số thập phân.\n(ii) UI: N/A.",""),

    ("US35-TC-037","SC-37","Bảng XLTP, Bước 6 – \"Lưu ý không làm tròn ở các phép tính trung gian\"","Thu phí định kỳ","Tính VAT","Không làm tròn phép tính trung gian","Field Validation","Medium",
     "1. Phí gốc qua nhiều bước tính: QTTP → Min/Max → ƯĐ → Min/Max CTƯĐ → VAT\n2. Mỗi bước có kết quả lẻ thập phân",
     "1. Bước 3.2: Phí = 123,456.789 (không làm tròn)\n2. Bước 3.4: Clamping → 123,456.789 (không làm tròn)\n3. Bước 5: ƯĐ → 98,765.4312 (không làm tròn)\n4. Bước 6: Tính VAT → làm tròn KẾT QUẢ CUỐI CÙNG",
     "(i) Nghiệp vụ/Logic: Tất cả phép tính trung gian giữ nguyên giá trị lẻ. Chỉ làm tròn ở kết quả cuối (VAT, Phí thu được).\n(ii) UI: N/A.",""),
]
