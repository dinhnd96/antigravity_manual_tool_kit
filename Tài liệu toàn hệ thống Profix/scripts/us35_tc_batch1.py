# -*- coding: utf-8 -*-
"""US35 Test Case Data - Batch 1 (SC-01 → SC-17): Happy Path + Negative Path đầu"""
TC_BATCH1 = [
    # TC_ID, SC_Ref, Reference, Feature, Module, Title, Type, Priority, Precondition, Steps, Expected, Note
    ("US35-TC-001","SC-01","Bảng XLTP, Bước 1 – \"hệ thống đối chiếu danh sách KH trong bảng Customer với DS code phí B\"","Thu phí định kỳ","Sinh dữ liệu phí","Job chạy đầu ngày T → sinh danh sách khoản phí thành công cho ĐT = Customer","Happy Path","High",
     "1. Job A đã được cài đặt với đối tượng tính phí = Customer, lịch chạy = ngày T\n2. Danh sách code phí B gồm ≥ 1 code phí đang hoạt động\n3. Có ≥ 1 KH thỏa điều kiện của code phí trong DS",
     "1. Đầu ngày T, hệ thống tự động trigger Job A\n2. Job xác định danh sách code phí B gắn với Job A\n3. Hệ thống đối chiếu danh sách KH trong bảng Customer với DS code phí B\n4. Sinh danh sách khoản phí C cho các KH thỏa điều kiện",
     "(i) Nghiệp vụ/Logic: Hệ thống sinh thành công danh sách khoản phí C chứa tất cả KH thỏa điều kiện code phí. Mỗi khoản phí có trạng thái = 'Thêm mới'.\n(ii) UI: N/A (backend process). Dữ liệu có thể tra cứu tại các US tra cứu/báo cáo.",""),

    ("US35-TC-002","SC-02","Bảng XLTP, Bước 1 – \"đối chiếu danh sách TK trong bảng Account với DS code phí B\"","Thu phí định kỳ","Sinh dữ liệu phí","Job chạy → sinh danh sách khoản phí thành công cho ĐT = Account","Happy Path","High",
     "1. Job A có đối tượng tính phí = Account\n2. Có ≥ 1 TK thỏa ĐK theo TK AND CIF thỏa ĐK theo KH",
     "1. Đầu ngày T, Job A trigger\n2. Hệ thống đối chiếu bảng Account với DS code phí B\n3. Kiểm tra (1) TK thỏa ĐK theo TK và (2) CIF của TK thỏa ĐK theo KH\n4. Sinh danh sách khoản phí C (bỏ qua bước 2 kiểm tra TK thay thế)",
     "(i) Nghiệp vụ/Logic: Sinh danh sách C thành công. Không qua bước 2 (kiểm tra TK thay thế). Trạng thái = 'Thêm mới'.\n(ii) UI: N/A (backend).",""),

    ("US35-TC-003","SC-03","Bảng XLTP, Bước 1 – \"đối chiếu danh sách thẻ trong bảng Card với DS code phí B\"","Thu phí định kỳ","Sinh dữ liệu phí","Job chạy → sinh danh sách khoản phí thành công cho ĐT = Card","Happy Path","High",
     "1. Job A có đối tượng tính phí = Card\n2. Có ≥ 1 Thẻ thỏa ĐK theo Thẻ AND CIF thỏa ĐK theo KH\n3. Chu kỳ thu = hàng năm, tròn năm từ ngày kích hoạt thẻ",
     "1. Đầu ngày T (tròn năm từ ngày kích hoạt), Job A trigger\n2. Hệ thống đối chiếu bảng Card với DS code phí B\n3. Sinh danh sách khoản phí C (bỏ qua bước 2)",
     "(i) Nghiệp vụ/Logic: Sinh danh sách C thành công cho Thẻ thỏa ĐK. Trạng thái = 'Thêm mới'.\n(ii) UI: N/A (backend).",""),

    ("US35-TC-004","SC-04","Bảng XLTP, Bước 2 – \"TK phải cùng loại tiền...SP thuộc CA_PRODUCT...Trạng thái: HĐ, Tạm ngừng HĐ [...]\"","Thu phí định kỳ","Kiểm tra TK thu phí","ĐT = Customer, TK mặc định đủ 3 ĐK → dùng TK mặc định","Happy Path","High",
     "1. ĐT tính phí = Customer\n2. TK mặc định: cùng loại tiền VND với Code phí, SP thuộc CA_PRODUCT, trạng thái = 'Hoạt động'",
     "1. Job sinh khoản phí cho KH\n2. Hệ thống kiểm tra TK mặc định\n3. TK đủ 3 ĐK: (1) cùng loại tiền, (2) SP thuộc CA_PRODUCT, (3) TT hợp lệ\n4. Ghi TK mặc định vào khoản phí",
     "(i) Nghiệp vụ/Logic: Hệ thống sử dụng TK mặc định để thu phí. Không tìm TK thay thế.\n(ii) UI: N/A (backend).",""),

    ("US35-TC-005","SC-05","Bảng XLTP, Bước 2 – \"tìm TK thay thế...ưu tiên lấy TK có số dư lớn nhất\"","Thu phí định kỳ","Kiểm tra TK thu phí","TK mặc định không đủ ĐK → tìm TK thay thế có số dư lớn nhất","Happy Path","High",
     "1. ĐT = Customer\n2. TK mặc định không cùng loại tiền Code phí (ĐK 1 fail)\n3. KH có ≥ 2 TK khác đủ 3 ĐK, TK_A số dư = 50,000,000, TK_B số dư = 30,000,000",
     "1. Job sinh khoản phí → kiểm tra TK mặc định → fail ĐK 1\n2. Hệ thống tìm TK thay thế trong DS TK của KH\n3. Lọc TK đủ 3 ĐK → TK_A (50M), TK_B (30M)\n4. Chọn TK_A (số dư lớn nhất)",
     "(i) Nghiệp vụ/Logic: Hệ thống chọn TK_A (số dư = 50,000,000) làm TK thu phí thay thế.\n(ii) UI: N/A (backend).",""),

    ("US35-TC-006","SC-06","Bảng XLTP, Bước 3.2 – \"Nếu Quy tắc tính phí = Số cố định\"","Thu phí định kỳ","Tính phí","Quy tắc tính phí = Số cố định → Phí cần thu = giá trị cố định","Happy Path","High",
     "1. Code phí CP01 có Quy tắc tính phí = 'Số cố định', giá trị = 100,000 VND\n2. KH đã nằm trong danh sách C",
     "1. Hệ thống xác định QTTP cho KH → Số cố định\n2. Tính Số tiền phí = 100,000 VND\n3. Chuyển sang bước 4 (xác định CTƯĐ)",
     "(i) Nghiệp vụ/Logic: Số tiền phí cần thu = 100,000 VND (đúng bằng giá trị Số cố định đã cài đặt).\n(ii) UI: N/A.",""),

    ("US35-TC-007","SC-07","Bảng XLTP, Bước 3.2 – \"Nếu Quy tắc tính phí = Công thức\"","Thu phí định kỳ","Tính phí","Quy tắc tính phí = Công thức → tính theo cấu phần","Happy Path","High",
     "1. Code phí CP02 có Quy tắc tính phí = 'Công thức', tham chiếu US05\n2. Số tiền phí tính ra = 250,000 VND (> 0)",
     "1. Hệ thống xác định QTTP = Công thức\n2. Tính phí theo cấu phần US05 → kết quả = 250,000 VND\n3. Phí > 0 → chuyển bước 3.3/3.4 (nếu có Min/Max) hoặc bước 4",
     "(i) Nghiệp vụ/Logic: Số tiền phí cần thu = 250,000 VND. Tính đúng theo công thức cấu phần.\n(ii) UI: N/A.","Tham chiếu US05 về Quy tắc tính phí"),

    ("US35-TC-008","SC-08","Bảng XLTP, Bước 3.3-3.4 – \"Nếu Số tiền tối thiểu <= Phí <= Số tiền tối đa\"","Thu phí định kỳ","Tính phí","Code phí có Min/Max cùng loại tiền, phí trong khoảng → giữ nguyên","Happy Path","Medium",
     "1. Code phí: Min = 50,000 VND, Max = 500,000 VND, Loại tiền = VND\n2. Phí đã tính = 200,000 VND (nằm trong khoảng)",
     "1. Kiểm tra Loại tiền Min/Max = Loại tiền Code phí → không quy đổi\n2. So sánh: 50,000 <= 200,000 <= 500,000 → trong khoảng\n3. Phí cần thu = 200,000 VND (giữ nguyên)",
     "(i) Nghiệp vụ/Logic: Phí cần thu = 200,000 VND = Phí đã tính. Không clamping.\n(ii) UI: N/A.",""),

    ("US35-TC-009","SC-09","Bảng XLTP, Bước 5.1 – \"Nếu Ưu đãi theo tỷ lệ = Yes\"","Thu phí định kỳ","Ưu đãi CTƯĐ","CTƯĐ có ƯĐ theo tỷ lệ = Yes → tính ƯĐ = Tỷ lệ × Phí","Happy Path","High",
     "1. Code phí có 1 CTƯĐ áp dụng, Ưu đãi theo tỷ lệ = Yes, Tỷ lệ = 20%\n2. Phí cần thu = 100,000 VND",
     "1. Hệ thống xác định CTƯĐ áp dụng\n2. Tính Số tiền ƯĐ = 20% × 100,000 = 20,000 VND\n3. Phí sau ƯĐ = 100,000 - 20,000 = 80,000 VND",
     "(i) Nghiệp vụ/Logic: Số tiền ƯĐ = 20,000. Phí sau ƯĐ = 80,000 VND.\n(ii) UI: N/A.",""),

    ("US35-TC-010","SC-10","Bảng XLTP, Bước 5.1 – \"Nếu Ưu đãi theo tỷ lệ = No, Số tiền ƯĐ = Số tiền giảm\"","Thu phí định kỳ","Ưu đãi CTƯĐ","CTƯĐ có ƯĐ theo số tiền giảm cố định","Happy Path","High",
     "1. Code phí có 1 CTƯĐ áp dụng, Ưu đãi theo tỷ lệ = No, Số tiền giảm = 30,000 VND\n2. Phí cần thu = 100,000 VND",
     "1. Xác định CTƯĐ áp dụng\n2. Số tiền ƯĐ = 30,000 VND (cố định)\n3. Phí sau ƯĐ = 100,000 - 30,000 = 70,000 VND",
     "(i) Nghiệp vụ/Logic: Số tiền ƯĐ = 30,000 (cố định). Phí sau ƯĐ = 70,000 VND.\n(ii) UI: N/A.",""),

    ("US35-TC-011","SC-11","Bảng XLTP, Bước 6 – \"Phí đã bao gồm VAT? = Có: VAT = Số tiền phí thực thu/110*10\"","Thu phí định kỳ","Tính VAT","Code phí có VAT, Phí đã bao gồm VAT = Có","Happy Path","High",
     "1. Code phí có VAT ≠ '', Phí đã bao gồm VAT = 'Có'\n2. Phí thực thu = 110,000 VND",
     "1. Kiểm tra VAT ≠ '' → có VAT\n2. Phí đã bao gồm VAT = 'Có' → VAT = 110,000/110×10 = 10,000 VND\n3. Phí thu được = 110,000 - 10,000 = 100,000 VND\n4. Làm tròn: VND → số nguyên (đã là số nguyên)",
     "(i) Nghiệp vụ/Logic: VAT = 10,000 VND. Phí thu được = 100,000 VND.\n(ii) UI: N/A.",""),

    ("US35-TC-012","SC-12","Bảng XLTP, Bước 6 – \"Phí đã bao gồm VAT? = Không: VAT = Số tiền phí thực thu/100*10\"","Thu phí định kỳ","Tính VAT","Code phí có VAT, Phí đã bao gồm VAT = Không","Happy Path","High",
     "1. Code phí có VAT ≠ '', Phí đã bao gồm VAT = 'Không'\n2. Phí thực thu = 100,000 VND",
     "1. VAT ≠ '' → có VAT\n2. Phí chưa bao gồm VAT → VAT = 100,000/100×10 = 10,000 VND\n3. Phí thu được = 100,000 VND (giữ nguyên)\n4. Làm tròn: VND → số nguyên",
     "(i) Nghiệp vụ/Logic: VAT = 10,000 VND. Phí thu được = 100,000 VND (chưa bao gồm VAT).\n(ii) UI: N/A.",""),

    ("US35-TC-013","SC-13","Bảng XLTP, Bước 6 – \"Code phí có VAT = '' (phí không có VAT): để trống VAT\"","Thu phí định kỳ","Tính VAT","Code phí không có VAT → để trống VAT trong response","Happy Path","Medium",
     "1. Code phí có VAT = '' (chuỗi rỗng)\n2. Phí thực thu = 100,000 VND",
     "1. Kiểm tra VAT = '' → không có VAT\n2. Để trống VAT trong dữ liệu gửi đi\n3. Phí thu được = 100,000 VND",
     "(i) Nghiệp vụ/Logic: VAT = trống (không tính). Phí thu được = 100,000 VND.\n(ii) UI: N/A.","BA QA-02.3 xác nhận"),

    ("US35-TC-014","SC-14","YCNV – \"ghi danh sách vào Topic Kafka theo thứ tự ưu tiên\"","Thu phí định kỳ","Ghi Kafka","Ghi danh sách khoản phí vào Topic Kafka theo thứ tự ưu tiên","Happy Path","High",
     "1. Danh sách khoản phí C đã sinh thành công\n2. Thứ tự ưu tiên: Nhóm SMS (ưu tiên 1) > Nhóm Quản lý TK (ưu tiên 2)",
     "1. ProfiX ghi khoản phí nhóm SMS vào Topic Kafka trước\n2. Tiếp theo ghi khoản phí nhóm Quản lý TK\n3. T24 đọc và hạch toán theo thứ tự nhận được",
     "(i) Nghiệp vụ/Logic: Khoản phí được ghi vào Kafka đúng thứ tự ưu tiên đã cài đặt theo nhóm code phí.\n(ii) UI: N/A.",""),

    ("US35-TC-015","SC-15","Bảng Diễn giải, Bước 4 – \"Ghi nhận lịch sử thu phí, Update trạng thái\"","Thu phí định kỳ","Update kết quả","T24 trả Thanh toán toàn bộ → ghi lịch sử + cập nhật trạng thái","Happy Path","High",
     "1. Khoản phí đã gửi T24, phí cần thu = 100,000 VND\n2. Số dư TK đủ: ≥ 100,000 VND",
     "1. T24 hạch toán thu 100,000 VND thành công\n2. T24 ghi kết quả 'Thanh toán toàn bộ' vào Topic kết quả\n3. ProfiX đọc message → ghi lịch sử thu phí\n4. Cập nhật trạng thái kỳ nợ = 'Thanh toán toàn bộ'",
     "(i) Nghiệp vụ/Logic: Lịch sử thu phí được ghi nhận. Trạng thái kỳ nợ = 'Thanh toán toàn bộ'. Số tiền = 100,000 VND.\n(ii) UI: N/A (kết quả tra cứu tại US tra cứu lịch sử thu phí).",""),

    ("US35-TC-016","SC-16","YCNV – \"Thanh toán một phần: Đã thu được một phần số tiền phí cần thu\"","Thu phí định kỳ","Update kết quả","T24 trả Thanh toán một phần → ghi lịch sử + xác định Nợ phí","Happy Path","High",
     "1. Phí cần thu = 100,000 VND\n2. Số dư TK = 60,000 VND (< phí cần thu nhưng > 0)",
     "1. T24 tận thu 60,000 VND (một phần)\n2. Ghi kết quả 'Thanh toán một phần' vào Topic\n3. ProfiX đọc → ghi lịch sử thu phí (60,000)\n4. Cập nhật trạng thái = 'Thanh toán một phần' → Nợ phí = 40,000",
     "(i) Nghiệp vụ/Logic: Lịch sử thu phí ghi nhận 60,000 VND. Trạng thái = 'Thanh toán một phần'. Khoản phí được xác định là Nợ phí (còn nợ 40,000).\n(ii) UI: N/A.",""),

    ("US35-TC-017","SC-17","YCNV – \"Nếu không có TK nào thỏa mãn thì...ghi nhận số TK mặc định\" + BA: kết quả = Không thành công","Thu phí định kỳ","Kiểm tra TK thu phí","Không có TK thay thế → vẫn gửi TK mặc định → T24 trả Chưa thanh toán","Negative Path","High",
     "1. ĐT = Customer\n2. TK mặc định: TT = 'Đã đóng' (không hợp lệ)\n3. KH không có TK nào khác đủ 3 ĐK",
     "1. Job sinh khoản phí → kiểm tra TK mặc định → fail\n2. Tìm TK thay thế → không có TK nào đủ ĐK\n3. Vẫn ghi TK mặc định vào Topic Kafka\n4. T24 hạch toán → trả kết quả 'Chưa thanh toán'",
     "(i) Nghiệp vụ/Logic: ProfiX vẫn gửi TK mặc định cho T24. Kết quả thu phí = 'Chưa thanh toán'. Khoản phí trở thành Nợ phí.\n(ii) UI: N/A.","BA QA-01.2 xác nhận"),
]
