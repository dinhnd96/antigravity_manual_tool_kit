"""US32 Part B Merged - Data only"""

# (ID, Reference, Question, Category, Proposal, BA_Answer)
# Categories: Nghiệp vụ, Giới hạn, Toàn vẹn dữ liệu, UI-UX

HM1_DATA = [
    (
        'US32-QA-01.1',
        'Mục "Yêu cầu nghiệp vụ", đoạn "Khi vào các màn hình báo cáo tổng quan, hệ thống dựa trên thông tin khối của người dùng..."',
        'Phân quyền dữ liệu QTC-10 áp dụng cho Dashboard: User thuộc Khối KHCN → Dashboard chỉ hiển thị dữ liệu KHCN hay hiển thị tất cả nhưng filter mặc định theo Khối? Tài liệu không nói rõ Dashboard lọc ở tầng nào (lọc toàn bộ biểu đồ hay chỉ lọc bảng danh sách).',
        'Nghiệp vụ',
        'Đề xuất: QTC-10 áp dụng cho TOÀN BỘ dữ liệu trên Dashboard (cả biểu đồ lẫn bảng). User Khối KHCN chỉ thấy dữ liệu giao dịch thu phí của KH thuộc Khối KHCN trên mọi biểu đồ.',
    ),
    (
        'US32-QA-01.2',
        'Mục "Yêu cầu nghiệp vụ", Phân vùng chỉ số tổng quan, đoạn "Phần trăm thay đổi..."',
        'Công thức % thay đổi: (Tháng này − Tháng trước) / Tháng trước × 100%. Nếu Tháng trước = 0 (không có giao dịch nào), phép chia cho 0 xảy ra. Hệ thống xử lý như thế nào?',
        'Nghiệp vụ',
        'Đề xuất: Nếu mẫu số = 0, hiển thị "N/A" hoặc "—" thay vì % và không áp dụng logic màu xanh/đỏ.',
    ),
    (
        'US32-QA-01.3',
        'Mục "Yêu cầu nghiệp vụ", Phân vùng chỉ số tổng quan, đoạn "Nếu kết quả >=100% thì hiển thị màu xanh; <100% đỏ"',
        'Logic màu: >=100% = xanh, <100% = đỏ. Tuy nhiên công thức % thay đổi có thể cho ra giá trị ÂM (VD: tháng này=100, tháng trước=200 → %=-50%). Giá trị 0% hoặc âm thuộc nhóm nào? Cần xác nhận: ngưỡng so sánh 100% hay 0% để phân biệt tăng/giảm?',
        'Nghiệp vụ',
        'Đề xuất: Nếu % ≥ 0 → xanh (tăng/giữ nguyên); Nếu % < 0 → đỏ (giảm). Tham khảo Mockup: badge hiển thị mũi tên lên/xuống.',
    ),
    (
        'US32-QA-01.4',
        'Mục "Dashboard theo Chi nhánh", biểu đồ "Nợ phí và truy thu theo chi nhánh", đoạn "mặc định hiển thị 7 chi nhánh (theo thứ tự alphabet)"',
        'Biểu đồ Nợ phí mặc định 7 chi nhánh theo alphabet, trong khi các biểu đồ khác (cùng Module 1) mặc định top 5. Tại sao con số 7 và tiêu chí alphabet thay vì top theo giá trị? Đây là thiết kế có chủ đích hay lỗi copy?',
        'Nghiệp vụ',
        'Đề xuất: Xác nhận 7 là con số thiết kế. Nếu user muốn thấy chi nhánh có nợ phí cao nhất thì cần tự chọn lại qua combobox.',
    ),
    (
        'US32-QA-01.5',
        'Mục "Dashboard theo Sản phẩm", biểu đồ "Số giao dịch thu phí theo sản phẩm", đoạn "Sắp xếp chi nhánh có số giao dịch thu phí cao nhất lên top"',
        'Tài liệu viết "Sắp xếp CHI NHÁNH có số giao dịch cao nhất" nhưng biểu đồ này là về SẢN PHẨM (SPDV cấp 1). Đây là lỗi copy-paste từ Module 1. Logic đúng phải là sắp xếp SẢN PHẨM.',
        'Nghiệp vụ',
        'Đề xuất: Sửa thành "Sắp xếp SPDV cấp 1 có số giao dịch thu phí cao nhất lên top". Nhờ BA update tài liệu.',
    ),
    (
        'US32-QA-01.6',
        'Mục "Dashboard theo Khối", biểu đồ "Nợ phí và truy thu", trục X: "Khối KHCN, Khối KHDNL, Khối KHDN"',
        'Trục X cố định 3 khối. Nếu user thuộc Khối KHCN (theo QTC-10 chỉ thấy dữ liệu KHCN), biểu đồ có hiển thị đủ 3 khối nhưng 2 khối kia = 0? Hay chỉ hiển thị khối mà user có quyền?',
        'Nghiệp vụ',
        'Đề xuất: Chỉ hiển thị các Khối mà user có quyền xem. User KHCN → biểu đồ chỉ có 1 điểm Khối KHCN.',
    ),
    (
        'US32-QA-01.7',
        '[VA] Mục "Danh sách KH giao dịch nhiều nhất" — thời điểm chốt dữ liệu',
        'Bảng KH top giao dịch "trong ngày hệ thống". Nếu ngày hệ thống là hôm nay, dữ liệu có cập nhật realtime trong ngày không? Hay là dữ liệu batch cuối ngày hôm trước?',
        'Nghiệp vụ',
        'Đề xuất: Xác nhận rõ dữ liệu bảng KH là realtime trong ngày hay batch cuối ngày hôm trước. Điều này ảnh hưởng kịch bản test.',
    ),
    (
        'US32-QA-01.8',
        '[VA] Mục "Nợ phí và truy thu theo chi nhánh" — định nghĩa nợ phí',
        'Tài liệu không định nghĩa rõ "nợ phí" là gì: (A) Phí đến hạn chưa thu được trong tháng hiện tại (MTD); hay (B) Tổng nợ lũy kế từ các tháng trước đến nay? Phạm vi tính nợ phí ảnh hưởng trực tiếp đến logic tính toán biểu đồ.',
        'Nghiệp vụ',
        'Đề xuất: BA cần định nghĩa rõ phạm vi tính nợ phí: chỉ tháng hiện tại (MTD) hay lũy kế từ các tháng trước.',
    ),
]

HM2_DATA = [
    (
        'US32-QA-02.1',
        'Mục "Yêu cầu nghiệp vụ", đoạn "Các số tiền trên dashboard đều có đơn vị Triệu VND"',
        'Đơn vị "Triệu VND" nhưng không nêu rõ quy tắc làm tròn. Ví dụ: 12,231,456 VND → hiển thị 12.23 hay 12.2 hay 12 Triệu VND? Số thập phân sau dấu chấm là bao nhiêu?',
        'Giới hạn',
        'Đề xuất: Hiển thị số nguyên (12,231 = 12 tỷ 231 triệu) hoặc 2 chữ số thập phân (12.23 triệu). BA cần xác nhận.',
    ),
    (
        'US32-QA-02.2',
        '[VA] Mục "Top [n] chi nhánh" — khi n > tổng số chi nhánh thực tế',
        'Nếu ngân hàng chỉ có 8 chi nhánh, user chọn top 15: hệ thống hiển thị 8 chi nhánh thực tế hay báo lỗi? Phần "Còn lại" trong Donut chart = 0 thì ẩn hay vẫn hiển thị?',
        'Giới hạn',
        'Đề xuất: Hiển thị tất cả chi nhánh hiện có (không đủ n thì lấy hết), phần "Còn lại" = 0 thì ẩn.',
    ),
    (
        'US32-QA-02.3',
        'Mục "Nợ phí và truy thu theo chi nhánh", đoạn "được chọn tối đa 10 chi nhánh"',
        'Khi user đã chọn đủ 10 chi nhánh và thử chọn thêm chi nhánh thứ 11, FE xử lý thế nào? Disable checkbox hay hiển thị cảnh báo?',
        'Giới hạn',
        'Đề xuất: FE disable các chi nhánh chưa chọn khi đã đủ 10. Hiển thị gợi ý "Đã chọn tối đa 10 chi nhánh".',
    ),
    (
        'US32-QA-02.4',
        '[VA] Mục "Chọn sản phẩm dịch vụ" — tham số product_level',
        'Nếu tham số product_level = 1 (chỉ có SPDV cấp 1), dropdown cấp SPDV hiển thị thế nào? Có còn dropdown chọn cấp không? Giới hạn tối đa 10 SPDV có thay đổi không?',
        'Giới hạn',
        'Đề xuất: Nếu product_level = 1, ẩn dropdown chọn cấp, mặc định lấy cấp 1. Giới hạn 10 SPDV giữ nguyên.',
    ),
    (
        'US32-QA-02.5',
        'Mục "Dashboard theo Sản phẩm", đoạn "Cho phép chọn tối đa 10 SPDV cùng cấp"',
        'Khi user đã chọn 10 SPDV và thử chọn SPDV thứ 11, FE xử lý thế nào?',
        'Giới hạn',
        'Đề xuất: FE disable checkbox SPDV chưa chọn khi đã đủ 10, kèm gợi ý "Đã chọn tối đa 10 SPDV".',
    ),
    (
        'US32-QA-02.6',
        'Toàn bộ Dashboard — không có dữ liệu (empty state)',
        'Tài liệu không đề cập hành vi khi không có DỮ LIỆU (tháng mới, chưa có giao dịch). Tất cả biểu đồ + KPI card hiển thị gì? Biểu đồ có empty state hay trống hoàn toàn?',
        'Giới hạn',
        'Đề xuất: KPI card hiển thị giá trị 0, % thay đổi = "N/A". Biểu đồ hiển thị trạng thái empty state ("Chưa có dữ liệu").',
    ),
    (
        'US32-QA-02.7',
        '[VA] Toàn bộ Dashboard — tần suất refresh dữ liệu',
        'Dashboard có tự động refresh dữ liệu không? Nếu có, tần suất bao lâu/lần? Hay user phải F5 thủ công? Ảnh hưởng đến kịch bản test khi dữ liệu thay đổi trong lúc user đang xem.',
        'Giới hạn',
        'Đề xuất: Làm rõ refresh policy. Nếu auto-refresh, cần document interval và hành vi khi đang tương tác (VD: giữ nguyên filter đang chọn).',
    ),
]

HM3_DATA = [
    (
        'US32-QA-03.1',
        'Mục "Yêu cầu nghiệp vụ", đoạn "không tính các giao dịch đã bị reverse"',
        'Nếu 1 giao dịch được reverse SAU khi Dashboard đã load, Dashboard có tự động cập nhật hay phải reload trang?',
        'Toàn vẹn dữ liệu',
        'Đề xuất: Dashboard hiển thị dữ liệu tại thời điểm load. Muốn thấy dữ liệu mới nhất → user refresh trang.',
    ),
    (
        'US32-QA-03.2',
        'Mục "Dashboard theo Chi nhánh", đoạn "số tiền phí thực thu VND > 0"',
        'Nếu giao dịch có phí thực thu bằng ngoại tệ (USD, EUR) nhưng quy đổi VND > 0, có được tính không? Hay chỉ tính giao dịch phí gốc = VND?',
        'Toàn vẹn dữ liệu',
        'Đề xuất: "Phí thực thu VND" = số tiền phí đã quy đổi sang VND. Mọi giao dịch (bất kể ngoại tệ gốc) nếu có quy đổi VND > 0 đều được tính.',
    ),
    (
        'US32-QA-03.3',
        'Mục "Dashboard theo Khối", trục X "Khối KHCN, Khối KHDNL, Khối KHDN"',
        'Tên Khối "KHDNL" trong tài liệu không khớp với QTC-10 (chỉ có KHCN, KHDN). "KHDNL" là viết tắt của gì? Có phải = Khối KHDN Lớn (tương đương KHTC)?',
        'Toàn vẹn dữ liệu',
        'Đề xuất: BA xác nhận mapping: KHDNL = ? và quan hệ với ma trận dữ liệu QTC-10.',
    ),
    (
        'US32-QA-03.4',
        '[VA] Biểu đồ Chi nhánh/Sản phẩm — CN hoặc SPDV bị deactivate giữa tháng',
        'Nếu chi nhánh hoặc SPDV bị đóng/hủy hiệu lực giữa tháng, các giao dịch phát sinh trước khi deactivate có còn được tính vào biểu đồ tháng đó không? CN/SPDV đã deactivate có hiển thị trên biểu đồ?',
        'Toàn vẹn dữ liệu',
        'Đề xuất: Dữ liệu lịch sử giao dịch vẫn giữ nguyên; CN/SPDV deactivate vẫn hiển thị trên dashboard tháng đó kèm dữ liệu đã phát sinh.',
    ),
    (
        'US32-QA-03.5',
        '[VA] Mục "Nợ phí và truy thu" — định nghĩa "truy thu thành công"',
        'Tài liệu không định nghĩa rõ "truy thu thành công" là gì. Đây là khi giao dịch nợ phí được thu lại thành công qua hệ thống? Hay bao gồm cả thu offline? Sự kiện nào trigger "truy thu thành công" để BE query chính xác?',
        'Toàn vẹn dữ liệu',
        'Đề xuất: BA cần định nghĩa rõ sự kiện trigger "truy thu thành công" và phạm vi tính (chỉ qua hệ thống hay gồm offline).',
    ),
]

HM4_DATA = [
    (
        'US32-QA-04.1',
        '[VA] Mockup image1 — Donut chart "Doanh thu phí dịch vụ theo chi nhánh"',
        'Số liệu mockup mâu thuẫn: Phần trung tâm donut = "Tổng: 2,000" nhưng legend mỗi chi nhánh hiển thị 34,200 (lớn hơn tổng). Format hiển thị legend gồm: Tên chi nhánh + Giá trị doanh thu. Xác nhận label "Tổng:" ở trung tâm là tổng tất cả chi nhánh hay chỉ top n?',
        'UI-UX',
        'Đề xuất: BA xác nhận label "Tổng:" ở trung tâm = tổng toàn bộ chi nhánh. Update mockup số liệu nhất quán.',
    ),
    (
        'US32-QA-04.2',
        'Mockup image2 và image3 — Vùng "Tính năng đang phát triển"',
        'Cả 2 màn hình Dashboard theo Sản phẩm và Dashboard theo Khối đều có 1 vùng lớn hiển thị "Tính năng đang phát triển". Tài liệu text không đề cập. Đây là placeholder cho biểu đồ sẽ bổ sung sau? Timeline dự kiến?',
        'UI-UX',
        'Đề xuất: BA xác nhận tên tính năng đang phát triển, timeline dự kiến, và có cần tạo placeholder UI theo spec không.',
    ),
    (
        'US32-QA-04.3',
        '[VA] Mục "Số giao dịch thu phí theo sản phẩm" — trục X/Y của line chart',
        'Tài liệu không mô tả trục X và trục Y của biểu đồ line chart theo sản phẩm. Mockup cho thấy trục X là danh sách SPDV (SP1, SP2...). Cần bổ sung mô tả trục X/Y như đã làm với biểu đồ stacked bar chart.',
        'UI-UX',
        'Đề xuất: Bổ sung mô tả: Trục X = Danh sách SPDV cấp 1, Trục Y = Số giao dịch thu phí.',
    ),
    (
        'US32-QA-04.4',
        '[VA] Mục "Chọn Khối" – Dashboard theo Khối, component UI mâu thuẫn',
        'Mockup image3 hiển thị 2 UI component khác nhau cho cùng chức năng "Chọn Khối": (1) Dropdown đơn "Chọn Khối" trong header bảng danh sách KH; (2) Checkbox multi-select (KHCN, KHDNL, KHDN) ở bên phải. Dùng component nào? Hay cả 2 tồn tại song song?',
        'UI-UX',
        'Đề xuất: Thống nhất 1 component. Nếu cho chọn nhiều Khối → dùng checkbox/multi-select. Cập nhật mockup nhất quán.',
    ),
    (
        'US32-QA-04.5',
        'Mục "Dashboard theo Sản phẩm", biểu đồ "Doanh thu phí theo SPDV", đoạn "Sau khi thoát khỏi dropdown list..."',
        'Tài liệu nói "Sau khi thoát khỏi dropdown list Chọn SPDV" nhưng không nói cách thoát. Click ngoài vùng dropdown? Hay có nút "Áp dụng"/"Đóng"? Mockup không thấy nút "Áp dụng".',
        'UI-UX',
        'Đề xuất: Thoát dropdown bằng cách click ra ngoài (auto-apply sau khi đóng). Không cần nút "Áp dụng" riêng.',
    ),
    (
        'US32-QA-04.6',
        'Cột "Doanh thu" — Bảng danh sách KH, Dashboard theo Khối',
        'Cột Doanh thu trong bảng KH top giao dịch: hiển thị đơn vị Triệu VND (thống nhất header) hay VND nguyên? Mockup hiển thị giá trị nhỏ (274, 185...) không rõ đơn vị.',
        'UI-UX',
        'Đề xuất: Xác nhận đơn vị cột Doanh thu. Nếu Triệu VND, cần ghi chú đơn vị trong header cột hoặc title bảng.',
    ),
    (
        'US32-QA-04.7',
        '[VA] Badge % thay đổi KPI header — format hiển thị dấu +/- và icon mũi tên',
        'Mockup hiển thị "-3.7%" (có dấu trừ) và "4.7%" (không có dấu cộng). Tài liệu không mô tả: (1) Có hiển thị dấu "+" khi tăng không? (2) Icon mũi tên lên/xuống kèm theo? (3) Màu badge khác màu text %?',
        'UI-UX',
        'Đề xuất: Bổ sung format badge: [icon mũi tên ↑/↓] [±giá trị]%. Xác nhận dấu "+" cho tăng và icon mũi tên theo chiều thay đổi.',
    ),
    (
        'US32-QA-04.8',
        '[VA] Biểu đồ "Nợ phí và truy thu theo Khối" — thứ tự Khối trên trục X',
        'Tài liệu liệt kê thứ tự: KHCN, KHDNL, KHDN. Mockup image3 trục X hiển thị: KHCN, KHDN, KHDNL (khác tài liệu). Cần thống nhất thứ tự.',
        'UI-UX',
        'Đề xuất: Thống nhất thứ tự các Khối trên trục X. Cập nhật tài liệu hoặc mockup cho nhất quán.',
    ),
]
