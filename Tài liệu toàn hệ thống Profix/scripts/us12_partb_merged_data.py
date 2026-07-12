"""US12 Part B Merged - DATA ONLY"""
# Format: (ID, Phan_loai, Trich_xuat, Cau_hoi, De_xuat, Nguon)
# Nguon: AI = AI sinh, VA = VA review, BOTH = cả 2 phát hiện

QA_DATA = [
    # === HẠNG MỤC 1: NGHIỆP VỤ ===
    ("US12-QA-01.1", "Nghiệp vụ",
     'Mục "Yêu cầu nghiệp vụ", đoạn "Điều kiện áp dụng"',
     'Tài liệu text đề cập 4 nguồn dữ liệu (ETL KH/TK/Thẻ/API giao dịch). Bảng mô tả chi tiết trường "Nguồn dữ liệu" chỉ liệt kê 3 giá trị: ETL KH, ETL TK, ETL Thẻ — thiếu "API giao dịch".',
     'Đề xuất: Bổ sung "API giao dịch" vào Bảng mô tả chi tiết trường "Nguồn dữ liệu".',
     'BOTH'),

    ("US12-QA-01.2", "Nghiệp vụ",
     'Flowchart Thêm mới, Bước 13.a → 13.b → 13.c → 13.d → 13.e',
     'Flowchart bước 13.b ghi "Gửi yêu cầu truy vấn CIF" nhưng không có nhánh xử lý khi CIF không tồn tại trong hệ thống hoặc CIF+SPDV đã tồn tại trong danh sách Chi tiết ưu đãi hiện tại.',
     'Đề xuất: Bổ sung nhánh lỗi khi CIF không tồn tại (FE hiển thị cảnh báo) và nhánh lỗi khi CIF+SPDV trùng lặp.',
     'VA'),

    ("US12-QA-01.3", "Nghiệp vụ",
     'Mục "Chỉnh sửa CTƯĐ", đoạn trạng thái "Đang hiệu lực"; Flowchart Bước 3.a',
     'Flowchart bước 3.a ghi "chỉ cho phép chỉnh Ngày hết hiệu lực", nhưng tài liệu text mô tả thêm 3 hành động Chi tiết ưu đãi (Upload thay thế / Thêm mới / Xóa). Flowchart thiếu phần này. Ngoài ra, khi chỉnh sửa Chi tiết ưu đãi ở trạng thái "Đang hiệu lực", người dùng có được thay đổi Toggle "Ưu đãi theo tỷ lệ" (On/Off) không?',
     'Đề xuất: Cập nhật Flowchart bước 3.a phản ánh đầy đủ. Disable toggle Ưu đãi theo tỷ lệ khi Đang hiệu lực.',
     'BOTH'),

    ("US12-QA-01.4", "Nghiệp vụ",
     'Flowchart Chỉnh sửa, Bước 3.1',
     'Bước 3.1 ghi "sửa toàn bộ trừ mã CTƯĐ". Nhưng text ghi "trừ mã CTƯĐ VÀ Số văn bản_Tên viết tắt CTƯĐ". Flowchart thiếu ràng buộc readonly cho trường "Số VB_Tên viết tắt CTƯĐ".',
     'Đề xuất: Cập nhật Flowchart Bước 3.1 ghi rõ "trừ Mã CTƯĐ và Số VB_Tên viết tắt CTƯĐ".',
     'BOTH'),

    ("US12-QA-01.5", "Nghiệp vụ",
     'Mục "Chỉnh sửa CTƯĐ", đoạn sau khi Maker chỉnh sửa thành công',
     'Khi CTƯĐ đang hiệu lực bị Maker chỉnh sửa → trạng thái Chờ duyệt. CTƯĐ bản gốc có tiếp tục được áp dụng cho các giao dịch trong thời gian chờ duyệt không? Hay tạm dừng?',
     'Đề xuất: Xác nhận CTƯĐ bản gốc vẫn hoạt động bình thường cho đến khi Checker phê duyệt bản sửa đổi.',
     'VA'),

    ("US12-QA-01.6", "Nghiệp vụ",
     'Flowchart Chỉnh sửa, Bước 2 "Có Tác vụ Chờ duyệt không?"',
     'Phạm vi kiểm tra: Tác vụ Chờ duyệt của chính CTƯĐ đang chọn, hay toàn bộ Tác vụ Chờ duyệt của user trong hệ thống?',
     'Đề xuất: Xác nhận kiểm tra Tác vụ Chờ duyệt gắn với chính CTƯĐ đó. Bổ sung vào tài liệu.',
     'VA'),

    ("US12-QA-01.7", "Nghiệp vụ",
     'Mục "Chi tiết ưu đãi", đoạn "Upload file để thay thế toàn bộ"',
     '"Thay thế toàn bộ" có nghĩa xóa sạch danh sách KH cũ thay bằng danh sách mới khi Checker duyệt, hay merge (giữ lại KH cũ + bổ sung mới)? Nếu xóa sạch, KH cũ đã có giao dịch tích lũy Ngưỡng dừng — dữ liệu lũy kế có bị reset không?',
     'Đề xuất: Xác nhận hành vi "thay thế toàn bộ" = xóa sạch + thay mới. Làm rõ xử lý dữ liệu lũy kế KH bị loại.',
     'BOTH'),

    ("US12-QA-01.8", "Nghiệp vụ",
     'Mục "Yêu cầu nghiệp vụ", đoạn "Chu kỳ áp dụng"',
     'Khi người dùng chuyển đổi giữa "Theo chu kỳ" và "Liên tục", hệ thống có tự động clear các giá trị đã chọn trong phân vùng Chu kỳ (Thứ, Ngày cụ thể, Ngày trong tháng, Tuần) hay không? Tài liệu chỉ đề cập clear cho toggle Ưu đãi.',
     'Đề xuất: Hệ thống nên clear giá trị Chu kỳ cũ khi chuyển đổi để tránh lưu dữ liệu rác.',
     'AI'),

    ("US12-QA-01.9", "Nghiệp vụ",
     'Mục "Yêu cầu nghiệp vụ", đoạn "Khi khai báo CTƯĐ..."',
     'Tài liệu yêu cầu khai báo trước Đối tượng thu phí, Khối, Loại ưu đãi... trước khi khai báo Chi tiết ưu đãi. FE enforce thứ tự bằng cách nào? Disable section hay chỉ validate khi Xác nhận?',
     'Đề xuất: FE disable section "Chi tiết ưu đãi" cho đến khi các trường bắt buộc trên đã điền đủ.',
     'BOTH'),

    ("US12-QA-01.10", "Nghiệp vụ",
     'Tài liệu US12 — Toàn bộ',
     'Tài liệu KHÔNG cung cấp mockup màn hình chỉnh sửa CTƯĐ. Cần mockup để xác nhận trường nào readonly/disabled khi Đang hiệu lực.',
     'Đề xuất: BA cung cấp mockup màn hình chỉnh sửa khi CTƯĐ ở trạng thái "Đang hiệu lực".',
     'AI'),

    ("US12-QA-01.11", "Nghiệp vụ",
     'Mục "Chi tiết ưu đãi", đoạn Ngày hiệu lực/Ngày hết hiệu lực KH',
     'Tài liệu ghi Ngày HL/HHL KH "ưu tiên áp dụng hơn Ngày HL/HHL CTƯĐ (Override)". Ngày HL KH có được phép NHỎ HƠN Ngày HL CTƯĐ hay phải nằm trong khoảng [Ngày HL CTƯĐ, Ngày HHL CTƯĐ]?',
     'Đề xuất: Ràng buộc Ngày HL KH ≥ Ngày HL CTƯĐ và Ngày HHL KH ≤ Ngày HHL CTƯĐ.',
     'AI'),

    # === HẠNG MỤC 2: GIỚI HẠN ===
    ("US12-QA-02.1", "Giới hạn",
     'Mục "Chi tiết ưu đãi", toàn bộ phần mô tả',
     'Không quy định giới hạn số KH tối đa trong 1 CTƯĐ / file upload. Hệ thống có hard limit không?',
     'Đề xuất: Xác nhận giới hạn tối đa số KH (VD: 500/1000/5000).',
     'BOTH'),

    ("US12-QA-02.2", "Giới hạn",
     'Bảng mô tả trường "Ngưỡng dừng ưu đãi" — mô tả bị cắt câu',
     'Mô tả trường bị cắt giữa chừng ("...Khi đạt đến"). Khi KH đạt ngưỡng dừng, CTƯĐ ngừng áp dụng ngay tại giao dịch vượt ngưỡng hay từ giao dịch tiếp theo?',
     'Đề xuất: Bổ sung đầy đủ mô tả hành vi khi đạt ngưỡng dừng ưu đãi.',
     'VA'),

    ("US12-QA-02.3", "Giới hạn",
     'Mục "Điều kiện áp dụng"',
     'Không giới hạn số lượng Nhóm điều kiện và số dòng điều kiện chi tiết trong mỗi nhóm. Có giới hạn tối đa không?',
     'Đề xuất: Xác nhận giới hạn tối đa số Nhóm điều kiện và số dòng trong mỗi nhóm.',
     'AI'),

    ("US12-QA-02.4", "Giới hạn",
     'Bảng mô tả trường "Ngưỡng dừng ưu đãi"',
     'Trường chỉ yêu cầu "số dương > 0" nhưng không quy định giá trị tối đa. Hệ thống xử lý ra sao khi nhập giá trị cực lớn?',
     'Đề xuất: Xác nhận giá trị tối đa cho phép.',
     'AI'),

    # === HẠNG MỤC 3: TOÀN VẸN DỮ LIỆU ===
    ("US12-QA-03.1", "Toàn vẹn dữ liệu",
     'Mục "Chi tiết ưu đãi", đoạn SPDV',
     'Nếu SPDV trong CTƯĐ đã duyệt bị chuyển "Không hoạt động" — CTƯĐ có bị ảnh hưởng? Dòng Chi tiết ưu đãi liên quan tự vô hiệu hay tiếp tục áp dụng?',
     'Đề xuất: BA làm rõ cascade behavior khi SPDV ngừng hoạt động.',
     'AI'),

    ("US12-QA-03.2", "Toàn vẹn dữ liệu",
     'Bảng "Kiểm tra Danh sách khách hàng upload", Ràng buộc CIF',
     'Chỉ kiểm tra CIF "tồn tại trong ETL". Không kiểm tra trạng thái CIF (Hoạt động/Tạm dừng). CIF đã đóng vẫn cho phép thêm vào CTƯĐ?',
     'Đề xuất: Bổ sung kiểm tra trạng thái CIF = "Hoạt động".',
     'AI'),

    ("US12-QA-03.3", "Toàn vẹn dữ liệu",
     'Bảng "Kiểm tra Danh sách khách hàng upload", Ràng buộc SPDV cha-con',
     'Phạm vi kiểm tra cha-con SPDV: chỉ trong file upload hiện tại (intra-file) hay bao gồm bản ghi đã tồn tại trong CTƯĐ (cross-check DB)?',
     'Đề xuất: Kiểm tra trên toàn bộ danh sách (cũ + mới).',
     'BOTH'),

    ("US12-QA-03.4", "Toàn vẹn dữ liệu",
     'Bảng "Kiểm tra Danh sách khách hàng upload", Ràng buộc CIF+SPDV',
     'Scope unique CIF+SPDV: chỉ trong 1 CTƯĐ hay unique trên toàn bộ CTƯĐ đang hiệu lực? Một KH có thể tham gia nhiều CTƯĐ với cùng SPDV?',
     'Đề xuất: BA xác nhận scope unique.',
     'AI'),

    ("US12-QA-03.5", "Toàn vẹn dữ liệu",
     'Mục "Chi tiết ưu đãi", Ngày HL/HHL khi Chu kỳ',
     'Khi CTƯĐ áp dụng "Theo chu kỳ", cột Ngày HL/HHL của KH ẩn trên UI. Nếu file upload chứa dữ liệu Ngày HL/HHL, hệ thống validate lỗi hay bỏ qua?',
     'Đề xuất: Bỏ qua giá trị Ngày HL/HHL trong file upload khi CTƯĐ áp dụng Theo chu kỳ, không báo lỗi.',
     'VA'),

    ("US12-QA-03.6", "Toàn vẹn dữ liệu",
     'Bảng mô tả trường, Mã CTƯĐ: "tham chiếu tới US04"',
     'Mã CTƯĐ tham chiếu US04 (Mã phí). Quy tắc sinh Mã CTƯĐ có khác Mã phí không? Cần xác nhận cấu trúc (prefix, số tự tăng, độ dài).',
     'Đề xuất: Ghi rõ cấu trúc Mã CTƯĐ vào tài liệu US12 thay vì chỉ tham chiếu.',
     'VA'),

    # === HẠNG MỤC 4: UI-UX ===
    ("US12-QA-04.1", "UI-UX",
     'Mockup — Phân vùng Đối tượng thu phí',
     'Mockup hiển thị "Đối tượng thu phí" dạng Checkbox (☐ KH ☑ Merchant) — cho phép multi-select. Bảng mô tả ghi "Dropdown list, chọn 1 trong 2". Mâu thuẫn component.',
     'Đề xuất: BA xác nhận component là Dropdown (single-select) hay Checkbox (multi-select).',
     'AI'),

    ("US12-QA-04.2", "UI-UX",
     'Bảng mô tả trường "Chu kỳ áp dụng"; Mockup Thêm mới',
     'Bảng mô tả: "Chu kỳ áp dụng" = Radio Button (Hàng tuần / Hàng tháng). Mockup: hiển thị 2 Checkbox "Theo chu kỳ" / "Liên tục" — không phải Radio Button và giá trị khác. Mâu thuẫn component + giá trị.',
     'Đề xuất: Đồng nhất Mockup với bảng mô tả. Xác nhận component + giá trị thực tế.',
     'VA'),

    ("US12-QA-04.3", "UI-UX",
     'Mockup Theo chu kỳ vs Mockup Liên tục — Section Chi tiết ưu đãi',
     'Mockup Theo chu kỳ chỉ có "Tải xuống", KHÔNG có "Tải lên". Mockup Liên tục có cả 2. Bảng mô tả ghi cả 2 nút đều bắt buộc (★). Lỗi mockup?',
     'Đề xuất: Xác nhận cả 2 chế độ đều có "Tải lên". Cập nhật Mockup Theo chu kỳ.',
     'BOTH'),

    ("US12-QA-04.4", "UI-UX",
     'Bảng mô tả trường "Số văn bản_Tên viết tắt CTƯĐ"; Mockup Thêm mới',
     'Bảng mô tả liệt kê trường "Số VB_Tên viết tắt CTƯĐ" (★, 20 ký tự, bắt buộc dấu gạch dưới). Mockup chỉ hiển thị "Số văn bản" và "Tên văn bản" — không có trường này.',
     'Đề xuất: Bổ sung trường "Số VB_Tên viết tắt CTƯĐ" vào Mockup.',
     'VA'),

    ("US12-QA-04.5", "UI-UX",
     'Mockup Theo chu kỳ vs Mockup Liên tục — Toggle "Ưu đãi theo tỷ lệ"',
     'Mockup Liên tục: toggle "Ưu đãi theo tỷ lệ" hiển thị = ON. Mockup Theo chu kỳ: toggle này KHÔNG xuất hiện. Tài liệu mô tả toggle áp dụng chung cả 2 chế độ. Lỗi Mockup?',
     'Đề xuất: Xác nhận toggle hiển thị ở cả 2 chế độ. Cập nhật Mockup Theo chu kỳ.',
     'VA'),

    ("US12-QA-04.6", "UI-UX",
     'Bảng mô tả trường "Loại tiền tối thiểu/tối đa"; Mockup lưới Chi tiết ưu đãi',
     '"Loại tiền tối thiểu/tối đa" — Mockup chỉ hiển thị 1 cột. Thực tế là 1 dropdown dùng chung cho cả Min và Max, hay 2 dropdown riêng?',
     'Đề xuất: Xác nhận 1 hay 2 dropdown. Cập nhật tên trường và Mockup.',
     'VA'),

    ("US12-QA-04.7", "UI-UX",
     'Bảng mô tả trường "Số VB_Tên viết tắt CTƯĐ"',
     'Ràng buộc "Phía trước dấu gạch dưới chỉ nhận ký tự là số". Phía SAU dấu gạch dưới cho phép gì? Chỉ chữ hay cả số+chữ? VD: "123_A1B" hợp lệ?',
     'Đề xuất: BA xác nhận quy tắc ký tự cho phần sau dấu gạch dưới.',
     'AI'),

    ("US12-QA-04.8", "UI-UX",
     'Bảng "Kiểm tra Danh sách KH upload" — Ngày HL/HHL',
     'Bảng upload ghi format Date = "dd-mm-yyyy" (gạch ngang). QTC-01.5 quy định "dd/mm/yyyy" (gạch chéo). Mâu thuẫn format.',
     'Đề xuất: Thống nhất format Date upload = dd/mm/yyyy theo QTC-01.5.',
     'AI'),

    ("US12-QA-04.9", "UI-UX",
     'Mockup — Phân vùng Điều kiện áp dụng',
     'Mockup hiển thị Dropdown "And/Or" giữa các Nhóm điều kiện và giữa các dòng trong cùng nhóm. Bảng mô tả KHÔNG đề cập logic "And/Or".',
     'Đề xuất: BA bổ sung mô tả logic kết hợp giữa các nhóm điều kiện (AND/OR).',
     'AI'),
]
