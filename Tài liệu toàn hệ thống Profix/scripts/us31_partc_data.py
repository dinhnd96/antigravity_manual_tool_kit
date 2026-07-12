"""US31 - Part C: Test Case Coverage Data
BA feedback đã chốt:
- Nút Tra cứu CIF: ĐÃ XÓA khỏi US (v2 không còn nút này)
- Lỗi copy-paste "dự thu phí": BA đã sửa → "Lưới danh sách tổng doanh thu phí"
- Lỗi đánh số 3.1/3.2: BA đã sửa flowchart v2 (không còn nhánh 3.3 CIF)
- Nguyên tệ vs VND khi VND: Cả 2 cột cùng giá trị (BA xác nhận)
- Tổng cộng: Footer cố định (sticky), tính toàn bộ DL, hiển thị 0 khi rỗng. Tách riêng "Thông tin khác"
- "Ngày giao dịch": BA đã thống nhất tên = "Ngày giao dịch"
- Không giới hạn khoảng thời gian tra cứu
- Không giới hạn Number tối đa
- Tỷ giá: Đã lưu từ thời điểm phát sinh GD, không tính lại khi xuất BC
- Aggregation: Group by (Chi nhánh+Loại tiền+Loại tính phí+Biểu phí+Code phí) → BA đã update US
- Khối disabled: Combobox vẫn hiển thị nhưng disabled
- Cột # = STT: Ưu tiên mô tả chi tiết
- Từ ngày/Đến ngày lưới: hiển thị dd/mm/yyyy theo mô tả chi tiết
- KHDNL: Khối riêng (Khách hàng doanh nghiệp lớn), khác KHDN (vừa và nhỏ) → cần update QTC-10
"""

FEATURE = "US31 - Báo cáo tổng doanh thu phí"

# (SC_ID, Feature, Module, Category, Title, Traceability)
TC_DATA = [
    # ===== 🟢 Happy Path =====
    ("SC-01", FEATURE, "Tra cứu", "Happy Path",
     "Tra cứu với đầy đủ điều kiện hợp lệ (Khối + Chi nhánh + Biểu phí + Code phí + Loại tính phí + Từ ngày + Đến ngày) → Lưới hiển thị kết quả đúng, group by theo tổ hợp Chi nhánh + Loại tiền + Loại tính phí + Biểu phí + Code phí",
     "Mục \"Yêu cầu nghiệp vụ\" – *\"Hiển thị tổng doanh thu phí nguyên tệ đã thu được của mỗi nhóm Chi nhánh + Loại tiền + Loại tính phí + Biểu phí + Code phí\"* + BA xác nhận QA-03.2"),
    ("SC-02", FEATURE, "Tra cứu", "Happy Path",
     "Tra cứu chỉ với Từ ngày + Đến ngày (bỏ trống tất cả điều kiện không bắt buộc) → Hệ thống hiển thị toàn bộ dữ liệu trong khoảng thời gian [Theo QTC-04]",
     "QTC-04 – *\"Nếu không nhập điều kiện tìm kiếm không bắt buộc, hệ thống tìm kiếm tất cả\"*"),
    ("SC-03", FEATURE, "Tra cứu", "Happy Path",
     "Tra cứu với Khối = KHCN (user thuộc Khối KHCN) → Combobox Khối hiển thị KHCN và disabled, lưới chỉ hiển thị dữ liệu thuộc Khối KHCN [Theo QTC-10]",
     "Bảng mô tả trường STT 1 (Khối) + BA xác nhận Combobox disabled"),
    ("SC-04", FEATURE, "Tra cứu", "Happy Path",
     "Tra cứu với user không thuộc KHCN/KHDN/KHDNL → Combobox Khối cho phép chọn tự do, để trống → tìm tất cả các Khối",
     "Bảng mô tả trường STT 1 (Khối), mô tả nhánh \"không thuộc Khối\""),
    ("SC-05", FEATURE, "Tra cứu", "Happy Path",
     "Xóa tra cứu → Hệ thống xóa tất cả điều kiện, lưới trở về trạng thái mặc định (không hiển thị kết quả) [Theo QTC-04]",
     "Bảng mô tả nút STT 2 (Xoá tra cứu) + QTC-04"),
    ("SC-06", FEATURE, "Tra cứu", "Happy Path",
     "Tra cứu không tìm thấy kết quả → Lưới hiển thị rỗng, dòng Tổng cộng hiển thị = 0",
     "Bảng mô tả trường STT 20 – *\"trường hợp lưới danh sách tổng doanh thu phí không có dữ liệu thì Tổng cộng hiển thị = 0\"*"),
    ("SC-07", FEATURE, "Tải xuống", "Happy Path",
     "Nhấn nút Tải xuống → Hiển thị dropdown Excel/PDF → Chọn Excel → Hệ thống tải file .xlsx, tên file = 'Báo cáo tổng doanh thu phí - yyyymmddhhmmss.xlsx' [Theo QTC-05]",
     "Bảng mô tả nút STT 3 (Tải xuống) + QTC-05"),
    ("SC-08", FEATURE, "Tải xuống", "Happy Path",
     "Nhấn nút Tải xuống → Chọn PDF → Hệ thống tải file .pdf, tên file = 'Báo cáo tổng doanh thu phí - yyyymmddhhmmss.pdf' [Theo QTC-05]",
     "Bảng mô tả nút STT 3 (Tải xuống) + QTC-05"),
    ("SC-09", FEATURE, "Tải xuống", "Happy Path",
     "Tải xuống khi lưới không có dữ liệu → Hệ thống vẫn cho phép tải file (file rỗng hoặc chỉ có header) [Theo QTC-05]",
     "QTC-05: Luôn cho phép tải xuống dù có dữ liệu hay không"),

    # ===== 🔴 Negative Path =====
    ("SC-10", FEATURE, "Tra cứu", "Negative Path",
     "Bỏ trống trường bắt buộc Từ ngày → FE chặn, hiển thị 'Trường này bắt buộc' dưới field Từ ngày [Theo QTC-14.5]",
     "Bảng mô tả trường STT 6 (Từ ngày ★) + QTC-14.5"),
    ("SC-11", FEATURE, "Tra cứu", "Negative Path",
     "Bỏ trống trường bắt buộc Đến ngày → FE chặn, hiển thị 'Trường này bắt buộc' dưới field Đến ngày [Theo QTC-14.5]",
     "Bảng mô tả trường STT 7 (Đến ngày ★) + QTC-14.5"),
    ("SC-12", FEATURE, "Tra cứu", "Negative Path",
     "Nhập Từ ngày > Đến ngày → FE không cho phép chọn/hiển thị lỗi validation",
     "Bảng mô tả trường STT 6: 'Không chọn ngày lớn hơn field Đến ngày'"),
    ("SC-13", FEATURE, "Tra cứu", "Negative Path",
     "Nhập ngày không hợp lệ (dd/mm/yyyy sai format, ví dụ: 32/13/2025) vào Từ ngày hoặc Đến ngày → FE chặn, không cho nhập hoặc hiển thị lỗi format",
     "Bảng mô tả trường STT 6-7 (Date, dd/mm/yyyy) + QTC-01.5"),

    # ===== 📐 Boundary Value =====
    ("SC-14", FEATURE, "Tra cứu", "Boundary Value",
     "Tra cứu với Từ ngày = Đến ngày (cùng 1 ngày) → Hệ thống trả kết quả giao dịch trong đúng 1 ngày đó (00:00:00.000 – 23:59:59.999) [Theo QTC-01.5]",
     "Bảng mô tả trường STT 6-7 + QTC-01.5"),
    ("SC-15", FEATURE, "Tra cứu", "Boundary Value",
     "Tra cứu với khoảng thời gian rất lớn (ví dụ: 5 năm) → Hệ thống vẫn xử lý và trả kết quả (BA xác nhận không giới hạn thời gian)",
     "BA trả lời QA-02.1 – *\"Đã có quy tắc chung về việc không giới hạn dữ liệu\"*"),
    ("SC-16", FEATURE, "Lưới kết quả", "Boundary Value",
     "Doanh thu phí (VND) và Tổng cộng đạt giá trị rất lớn (hàng nghìn tỷ) → Hệ thống hiển thị đúng format Number (phân cách hàng nghìn) không bị overflow [Theo QTC-01.4]",
     "BA feedback QA-02.2 + QTC-01.4"),
    ("SC-17", FEATURE, "Lưới kết quả", "Boundary Value",
     "Kết quả có đúng 50 bản ghi → Hiển thị 1 trang, phân trang disabled [Theo QTC-06]",
     "QTC-06: 50 bản ghi/trang mặc định"),
    ("SC-18", FEATURE, "Lưới kết quả", "Boundary Value",
     "Kết quả có 51 bản ghi → Hiển thị 2 trang, trang 1 = 50 bản ghi, trang 2 = 1 bản ghi [Theo QTC-06]",
     "QTC-06: phân trang mặc định"),

    # ===== 🎨 UI/UX & Field Validation =====
    ("SC-19", FEATURE, "Điều kiện tìm kiếm", "UI/UX & Field Validation",
     "Combobox Biểu phí hiển thị đúng format 'Mã biểu phí - Tên biểu phí', cho phép gõ text tìm kiếm theo mã hoặc tên [Theo QTC-01.1]",
     "Bảng mô tả trường STT 3 (Biểu phí) + QTC-01.1"),
    ("SC-20", FEATURE, "Điều kiện tìm kiếm", "UI/UX & Field Validation",
     "Combobox Code phí hiển thị đúng format 'Mã code phí - Tên code phí', cho phép gõ text tìm kiếm theo mã hoặc tên [Theo QTC-01.1]",
     "Bảng mô tả trường STT 4 (Code phí) + QTC-01.1"),
    ("SC-21", FEATURE, "Điều kiện tìm kiếm", "UI/UX & Field Validation",
     "Dropdown Loại tính phí hiển thị đúng 2 giá trị: 'Theo giao dịch' / 'Theo định kỳ', chỉ chọn 1 [Theo QTC-01.2]",
     "Bảng mô tả trường STT 5 (Loại tính phí, Dropdownlist) + QTC-01.2"),
    ("SC-22", FEATURE, "Lưới kết quả", "UI/UX & Field Validation",
     "Lưới hiển thị đúng 12 cột theo mô tả: STT, Mã Chi nhánh, Tên chi nhánh, Loại tiền, Loại tính phí, Biểu phí, Code phí, Tên phí, Doanh thu phí (Nguyên tệ), Doanh thu phí (VND), Từ ngày, Đến ngày",
     "Bảng mô tả trường STT 8-19 + BA feedback QA-04.2: Ưu tiên mô tả chi tiết"),
    ("SC-23", FEATURE, "Lưới kết quả", "UI/UX & Field Validation",
     "Cột Doanh thu phí (Nguyên tệ) và Doanh thu phí (VND) hiển thị đúng format Number: phân cách hàng nghìn bằng dấu phẩy, 2 số thập phân. Ngoại lệ: VND và JPY không có thập phân [Theo QTC-01.4]",
     "Bảng mô tả trường STT 16-17 (Number) + QTC-01.4"),
    ("SC-24", FEATURE, "Lưới kết quả", "UI/UX & Field Validation",
     "Cột Từ ngày và Đến ngày trên lưới hiển thị đúng format dd/mm/yyyy (không bao gồm giờ phút giây) [Theo QTC-01.5]",
     "Bảng mô tả trường STT 18-19 (Date) + BA feedback QA-04.4: Ưu tiên mô tả chi tiết + QTC-01.5"),
    ("SC-25", FEATURE, "Lưới kết quả", "UI/UX & Field Validation",
     "Trường dữ liệu rỗng trên lưới hiển thị blank (không hiển thị '-', 'N/A', 'Null') [Theo QTC-01.7]",
     "QTC-01.7 – *\"Trường hợp các trường dữ liệu không có giá trị, hệ thống hiển thị blank (rỗng)\"*"),
    ("SC-26", FEATURE, "Tổng cộng", "UI/UX & Field Validation",
     "Dòng Tổng cộng hiển thị ở vùng riêng (Thông tin khác) ngoài lưới danh sách, tính trên toàn bộ dữ liệu (không chỉ trang hiện tại), format Number [Theo QTC-01.4]",
     "Bảng mô tả trường STT 20 (Tổng cộng, mục 'Thông tin khác') + BA feedback QA-01.5 + QA-04.3"),
    ("SC-27", FEATURE, "Màn hình", "UI/UX & Field Validation",
     "Truy cập màn hình lần đầu → Lưới mặc định không hiển thị kết quả (rỗng), chờ user nhập điều kiện và nhấn Tra cứu [Theo QTC-04]",
     "QTC-04: Mặc định không hiển thị danh sách"),

    # ===== 🧠 Business Logic =====
    ("SC-28", FEATURE, "Tra cứu", "Business Logic",
     "User thuộc Khối KHDNL → Combobox Khối hiển thị 'KHDNL' và disabled, lưới chỉ trả dữ liệu thuộc Khối KHDNL (BA xác nhận KHDNL là Khối riêng biệt)",
     "Bảng mô tả trường STT 1 (Khối) + BA feedback QA-04.5: KHDNL là Khối riêng"),
    ("SC-29", FEATURE, "Tra cứu", "Business Logic",
     "User thuộc Khối KHDN → Combobox Khối hiển thị 'KHDN' và disabled, lưới chỉ trả dữ liệu thuộc Khối KHDN",
     "Bảng mô tả trường STT 1 (Khối) + QTC-10"),
    ("SC-30", FEATURE, "Lưới kết quả", "Business Logic",
     "Kết quả lưới hiển thị dữ liệu doanh thu phí nguyên tệ VND → Cả 2 cột Doanh thu phí (Nguyên tệ) và Doanh thu phí (VND) hiển thị cùng giá trị (BA xác nhận)",
     "BA feedback QA-01.4: Khi Loại tiền = VND, 2 cột cùng giá trị"),
    ("SC-31", FEATURE, "Lưới kết quả", "Business Logic",
     "Doanh thu phí (VND) = giá trị đã lưu từ thời điểm phát sinh giao dịch (không tính lại tỷ giá khi tra cứu)",
     "BA feedback QA-03.1: 'Dữ liệu đã được quy đổi và lưu từ thời điểm phát sinh giao dịch'"),
    ("SC-32", FEATURE, "Lưới kết quả", "Business Logic",
     "Lưới sắp xếp mặc định theo ngày update/tạo giảm dần [Theo QTC-06]",
     "QTC-06 – *\"Sắp xếp mặc định theo ngày update, ngày tạo giảm dần\"*"),

    # ===== 🔗 Data Integrity =====
    ("SC-33", FEATURE, "Lưới kết quả", "Data Integrity",
     "Dữ liệu group by đúng theo tổ hợp (Chi nhánh + Loại tiền + Loại tính phí + Biểu phí + Code phí) — mỗi dòng là 1 tổ hợp duy nhất, Doanh thu = tổng các giao dịch thuộc tổ hợp đó (BA đã update US)",
     "Mục \"Yêu cầu nghiệp vụ\" v2 đoạn P22-P23 + BA feedback QA-03.2"),
    ("SC-34", FEATURE, "Tải xuống", "Data Integrity",
     "File Excel/PDF tải xuống chứa đúng dữ liệu đang hiển thị trên lưới (theo điều kiện tra cứu đang áp dụng), bao gồm tất cả các cột trên lưới [Theo QTC-05]",
     "QTC-05: Tải xuống theo điều kiện tìm kiếm + template = field trên lưới"),
    ("SC-35", FEATURE, "Tổng cộng", "Data Integrity",
     "Tổng cộng = Tổng tất cả Doanh thu phí (VND) của toàn bộ bản ghi trong khoảng Từ ngày – Đến ngày (xuyên suốt tất cả các trang)",
     "Bảng mô tả trường STT 20 (Tổng cộng) + BA feedback QA-01.5"),

    # ===== ⚡ NFR =====
    ("SC-36", FEATURE, "Phân quyền", "NFR",
     "User không có quyền truy cập menu Báo cáo >> Báo cáo tổng doanh thu phí → Menu bị ẩn hoặc hiển thị thông báo không có quyền",
     "Mục \"Yêu cầu nghiệp vụ\", Navigation + QTC-10"),
    ("SC-37", FEATURE, "Tra cứu", "NFR",
     "Spam click nút Tra cứu liên tiếp (double-click) → Hệ thống chỉ xử lý 1 request, không gửi trùng lặp",
     "Bảng mô tả nút STT 1 (Tra cứu) – Best practice NFR: Chống spam click, chỉ xử lý 1 request/click"),
    ("SC-38", FEATURE, "Tải xuống", "NFR",
     "Spam click nút Tải xuống liên tiếp (double-click) → Hệ thống chỉ tải 1 file, không tải trùng lặp",
     "Bảng mô tả nút STT 3 (Tải xuống) – Best practice NFR: Chống spam click, chỉ xử lý 1 request/click"),

    # ===== Bổ sung từ VA Review =====
    ("SC-39", FEATURE, "Màn hình", "UI/UX & Field Validation",
     "Xác nhận nút \"Tra cứu CIF\" đã bị xóa khỏi màn hình v2 — không còn hiển thị trên vùng Điều kiện tìm kiếm hoặc bất kỳ vị trí nào trên màn hình (regression test sau khi BA loại bỏ tính năng)",
     "BA xác nhận QA-01.1: Trường dư, BA đã cập nhật US v2 — xóa nút Tra cứu CIF"),
    ("SC-40", FEATURE, "Tra cứu", "Data Integrity",
     "Hệ thống lọc dữ liệu chính xác dựa theo trường \"Ngày giao dịch\" được ghi nhận trong lịch sử thu phí thực tế (không lọc theo ngày tạo bản ghi hay ngày khác)",
     "BA trả lời QA-01.6 – *\"BA đã cập nhật US dùng thống nhất trường Ngày giao dịch\"* + Bảng mô tả trường STT 6-7"),

    # ===== Bổ sung từ Review Round 2 =====
    ("SC-41", FEATURE, "Điều kiện tìm kiếm", "UI/UX & Field Validation",
     "Combobox Mã Chi nhánh hỗ trợ tìm kiếm theo mã hoặc tên chi nhánh (search-as-you-type), chỉ chọn 1 chi nhánh [Theo QTC-01.1]",
     "Bảng mô tả trường STT 2 – *\"Cho phép người dùng tìm kiếm và chọn chi nhánh\"* + QTC-01.1"),
    ("SC-42", FEATURE, "Tra cứu", "Business Logic",
     "Tra cứu với Loại tính phí = 'Theo giao dịch' → Lưới chỉ hiển thị dữ liệu có Loại tính phí = Theo giao dịch. Tương tự cho 'Theo định kỳ' → chỉ hiển thị Theo định kỳ",
     "Bảng mô tả trường STT 5 – *\"Cho phép người dùng chọn loại tính phí: Theo giao dịch/Theo định kỳ\"*"),
    ("SC-43", FEATURE, "Tải xuống", "Data Integrity",
     "File Excel/PDF tải xuống bao gồm cả dòng Tổng cộng doanh thu phí VND (Tổng cộng nằm ở mục 'Thông tin khác', ngoài lưới danh sách)",
     "Bảng mô tả trường STT 20 – *\"Hiển thị tổng doanh thu phí VND\"* + QTC-05: template = fields trên lưới"),
]
