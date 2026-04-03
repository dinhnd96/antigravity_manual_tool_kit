# 📋 BÁO CÁO REVIEW TEST CASE — SA.06 Danh mục điều kiện tính phí

> **Reviewer:** Senior QA Lead (AI — Antigravity)  
> **Ngày review:** 2026-04-02  
> **File Test Case:** `Test case/C - Thanh SA06.xlsx`  
> **Tài liệu URD:** `I.1.1.1. SA.06- Danh mục điều kiện tính phí.docx`  
> **Tổng số TC đã review:** 28 TC (TC_001 → TC_028)

---

## I. TỔNG QUAN

| Hạng mục | Số lượng |
|---|---|
| Tổng TC trong file | 28 |
| TC bao phủ BR từ URD | 6 / 6 BR (bao phủ một phần) |
| TC có lỗi phát hiện | 14 |
| Lỗi GAP (thiếu kịch bản) | 5 |
| Lỗi Format Expected Result | 28 (toàn bộ) |
| Lỗi Logic / Mismatch | 4 |
| Lỗi Title chung chung | 7 |
| Lỗi nhẹ / gợi ý cải tiến | 4 |

---

## II. TRACEABILITY MATRIX — ĐỐI SOÁT BR vs TC

| BR trong URD | Mô tả BR | TC cover | Trạng thái |
|---|---|---|---|
| BR_01 | Nhập đủ trường bắt buộc (*) trước khi Xác nhận | TC_006, TC_016 | Đã cover |
| BR_02 | Nhấn "Đóng" không lưu dữ liệu | TC_009, TC_017 | Đã cover |
| BR_03 | Mã điều kiện và Tên điều kiện phải là duy nhất | TC_010, TC_011, TC_018, TC_019 | Đã cover |
| BR_04 | Kiểu dữ liệu gồm: Number/String/Date/Time | TC_012 | Đã cover (thiếu case Edit) |
| BR_05 | Ràng buộc chỉnh sửa trạng thái theo gắn kết CTƯĐ/Code phí | TC_020, TC_021 | Đã cover một phần - thiếu case verify dropdown chỉ hiển thị điều kiện Hoạt động |
| BR_06 | Nguồn dữ liệu API -> Mapping note Msg; ETL -> Bảng dữ liệu | TC_013, TC_014 | Đã cover một phần - thiếu case không chọn nguồn; thiếu case Edit nguồn dữ liệu |
| Luồng nghiệp vụ | Thêm mới -> Xác nhận -> Hiển thị danh sách | TC_005, TC_007, TC_008 | Đã cover |
| Chức năng View | Xem/View chi tiết | TC_001 đến TC_004 | Đã cover |
| Chức năng Tìm kiếm | Search full/partial/no result/clear | TC_022 đến TC_025 | Đã cover |
| Chức năng Export | Export full/filter/empty | TC_026 đến TC_028 | Cover một phần |

---

## III. BẢNG PHÁT HIỆN LỖI CHI TIẾT

| # | BR_ID / TC_ID | Loại phát hiện | Mô tả sự cố / Mâu thuẫn | Mức độ | Đề xuất sửa đổi |
|---|---|---|---|---|---|
| 1 | Toàn bộ 28 TC | Format — Critical | THIẾU CẤU TRÚC 4 LỚP EXPECTED RESULT. 100% TC đang viết Expected Result dưới dạng 1-3 câu chung chung, không có đánh số (i)(ii)(iii)(iv). Thiếu hoàn toàn lớp (ii) UI feedback, lớp (iii) Trạng thái & Audit log, lớp (iv) Output. | Critical | Bắt buộc rewrite toàn bộ Expected Result theo chuẩn 4 lớp. Xem mẫu tại Mục IV. |
| 2 | TC_001 | Title chung chung | Title: "Kiểm tra hiển thị màn hình view" — Không thể hiện mục tiêu test cụ thể. Đọc vào không biết màn hình nào, hiển thị gì. | Medium | Đổi thành: "Kiểm tra màn hình Danh sách điều kiện tính phí hiển thị đúng cột dữ liệu và trạng thái theo thiết kế" |
| 3 | TC_002 | Title chung chung + Ambiguity | Title: "Kiểm tra hiển thị phân trang" — Chung chung. Expected bị bỏ ngỏ dấu "…" (không điền ngưỡng số lượng bản ghi cụ thể). | Medium | Làm rõ với BA ngưỡng phân trang. Điền số cụ thể vào Expected. |
| 4 | TC_004 | Logic Mismatch | Expected gộp "Hiển thị detail" và "Không cho phép edit" vào 1 câu mà thiếu xác nhận UI rõ ràng: field read-only, disable, không có nút Lưu. | Medium | Tách 2 expected: (i) Hiển thị đúng thông tin chi tiết; (ii) Tất cả field ở chế độ read-only, nút Lưu bị ẩn/disable. |
| 5 | TC_005 | Format + Logic GAP | Expected có 3 bullet nhưng thiếu lớp (ii) mô tả toast message (màu/vị trí), (iii) trạng thái bản ghi = "Hoạt động" và Audit log. | High | Bổ sung đủ 4 lớp: (i) Lưu thành công; (ii) Toast xanh "Thêm mới điều kiện thành công"; (iii) Status = Hoạt động, Audit log; (iv) Hiện trong dropdown Code phí/CTƯĐ. |
| 6 | TC_006 | Title chung chung + Format | Title: "Kiểm tra hiển thị validate khi bỏ trống trường bắt buộc" — Không nêu rõ trường nào. Expected: "Hệ thống hiển thị lỗi validate" — Hoàn toàn chung chung. | High | Đổi title nêu rõ tên field. Expected (ii): viền đỏ + text lỗi xuất hiện dưới từng field bị bỏ trống. |
| 7 | TC_007 | Logic GAP — BR_05 | Expected thiếu verify: điều kiện tạo với trạng thái "Không hoạt động" phải KHÔNG hiện trong dropdown tại màn hình tạo Code phí/CTƯĐ (quy định BR_05). | High | Bổ sung Expected (iv): "Điều kiện vừa tạo (trạng thái Không hoạt động) KHÔNG xuất hiện trong dropdown tạo/sửa Code phí và CTƯĐ" |
| 8 | TC_009 | Title sai ngữ nghĩa | Title: "Thêm mới không thành công khi user chọn button Đóng" — Bấm "Đóng" là hành động hủy bỏ có chủ đích, không phải "không thành công". | Medium | Đổi title: "Kiểm tra nhấn nút Đóng trên form Thêm mới hủy bỏ nhập liệu và không lưu dữ liệu". Phân loại lại nhóm "Cancel/Close". |
| 9 | TC_017 | Title sai ngữ nghĩa | Tương tự TC_009 nhưng ở chức năng Edit: "Edit không thành công khi user chọn button Đóng". | Medium | Đổi title: "Kiểm tra nhấn nút Đóng trên form Edit hủy bỏ chỉnh sửa và không lưu data". |
| 10 | TC_021 | Priority bị bỏ trống | Cột Priority của TC_021 = Null — thiếu giá trị độ ưu tiên. | Low | Điền Priority = High (case kiểm tra phép sửa trạng thái — quan trọng về nghiệp vụ). |
| 11 | BR_05 / GAP | GAP — Thiếu kịch bản | URD BR_05: "List điều kiện tại màn tạo/sửa Code phí, CTƯĐ chỉ hiển thị điều kiện Status = Hoạt động" — Không có TC nào verify từ góc nhìn màn hình Code phí/CTƯĐ. | High | Thêm TC_NEW_01: "Kiểm tra dropdown điều kiện tính phí tại màn hình tạo Code phí chỉ hiển thị điều kiện Status = Hoạt động". |
| 12 | BR_06 / GAP | GAP — Thiếu kịch bản | Không có TC nào kiểm tra bỏ trống cả API lẫn ETL khi thêm mới. Nếu Nguồn dữ liệu là bắt buộc thì đây là Negative case quan trọng. | Medium | Làm rõ với BA: Nguồn dữ liệu có bắt buộc nhập không? Nếu có thì thêm TC validate bắt buộc. |
| 13 | BR_06 / Edit GAP | GAP — Thiếu kịch bản | Không có TC nào kiểm tra chỉnh sửa Nguồn dữ liệu (API sang ETL hoặc ngược lại) trong Edit — trong khi đây là trường có logic hiển thị điều kiện quan trọng. | Medium | Thêm TC_NEW_03 và TC_NEW_04 (xem Mục V). |
| 14 | TC_028 / Export | Ambiguity + Incomplete | Expected: "File rỗng / cảnh báo (kiểm tra lại xem tải xuống file rỗng hay cảnh báo)" — Expected đang là câu hỏi chưa giải đáp. TC này chưa hoàn thiện, không thể dùng để test thực tế. | High | Làm rõ với BA expected khi không có data. Cập nhật cụ thể: "Tải file Excel chỉ có header" hoặc "Hiển thị popup: Không có dữ liệu để xuất". |

---

## IV. MẪU REWRITE EXPECTED RESULT CHUẨN 4 LỚP

### TC_005 — Thêm mới thành công, trạng thái Hoạt động

HIỆN TẠI (sai format):
- Hệ thống lưu thành công Điều kiện tính phí và hiển thị thông báo "Thêm mới điều kiện thành công"
- Điều kiện tính phí vừa được tạo hiển thị trên màn hình list danh sách điều kiện
- Điều kiện tính phí vừa được tạo được hiển thị trên dropdown list khi tạo code phí/CTƯĐ

CHUẨN 4 LỚP (đề xuất):
(i)  Nghiệp vụ: Hệ thống lưu thành công bản ghi Trường điều kiện mới với toàn bộ thông tin đã nhập.
(ii) UI: Toast notification màu xanh lá hiển thị góc trên bên phải: "Thêm mới điều kiện thành công".
     Màn hình reload, bản ghi mới xuất hiện đầu grid Danh sách điều kiện với đầy đủ thông tin chính xác.
(iii) Trạng thái & Audit: Bản ghi có Status = "Hoạt động". Ghi Audit log: Người tạo + Thời điểm tạo.
(iv) Output: Điều kiện vừa tạo (Status = Hoạt động) xuất hiện trong dropdown tại màn hình
     Thêm mới/Sửa Code phí và Chương trình ưu đãi.

---

### TC_020 — Không cho phép sửa trạng thái khi đã gắn CTƯĐ/Code phí đang hiệu lực

HIỆN TẠI:
Hệ thống không cho phép sửa trạng thái, hiển thị cảnh báo ràng buộc.

CHUẨN 4 LỚP (đề xuất):
(i)  Nghiệp vụ: Hệ thống từ chối lưu thay đổi; dữ liệu trạng thái không bị thay đổi trong DB.
(ii) UI: Hiển thị popup/toast cảnh báo màu đỏ/cam:
     "Không thể thay đổi trạng thái vì điều kiện đang được sử dụng bởi CTƯĐ/Code phí đang có hiệu lực."
(iii) Trạng thái & Audit: Trạng thái điều kiện giữ nguyên giá trị ban đầu. Không ghi Audit log thay đổi.
(iv) Output: N/A.

---

## V. DANH SÁCH TC CẦN BỔ SUNG MỚI (GAP)

| TC_ID mới | Nhóm | Mô tả | BR tham chiếu |
|---|---|---|---|
| TC_NEW_01 | Add/Verify | Kiểm tra dropdown điều kiện tại màn tạo Code phí chỉ hiển thị điều kiện Status = Hoạt động | BR_05 |
| TC_NEW_02 | Add | Kiểm tra validate/báo lỗi khi không chọn Nguồn dữ liệu trong form Thêm mới | BR_06 |
| TC_NEW_03 | Edit | Thay đổi Nguồn dữ liệu từ API sang ETL: ẩn "Mapping note Msg", hiện "Bảng dữ liệu" ETL | BR_06 |
| TC_NEW_04 | Edit | Thay đổi Nguồn dữ liệu từ ETL sang API: ẩn "Bảng dữ liệu", hiện "Mapping note Msg" | BR_06 |
| TC_NEW_05 | Export | Làm rõ expected và hoàn thiện TC Export khi không có data (TC_028 chưa hoàn thiện) | URD - Tải xuống |

---

## VI. KẾT LUẬN & KHUYẾN NGHỊ

P1 — Sửa ngay (Blockers):
1. Rewrite toàn bộ Expected Result theo chuẩn 4 lớp (i, ii, iii, iv) — lỗi format ảnh hưởng 100% TC.
2. Hoàn thiện TC_028 (Export khi empty) — TC chưa hoàn chỉnh, không thể dùng để test.
3. Bổ sung TC_NEW_01 (BR_05 gap) — verify dropdown tại màn hình Code phí/CTƯĐ.

P2 — Sửa tiếp (Improvements):
4. Sửa Title các TC: TC_001, TC_002, TC_006, TC_009, TC_017.
5. Bổ sung TC_NEW_02, TC_NEW_03, TC_NEW_04 để cover đầy đủ BR_06.
6. Điền Priority cho TC_021 (đang bị None -> High).

P3 — Cải tiến dài hạn (Nice-to-have):
7. Tách expected TC_004 thành 2 phần riêng biệt (view detail + read-only check).
8. Bổ sung verify TC_007: điều kiện "Không hoạt động" không hiển thị trong dropdown.
9. Làm rõ Ambiguity ngưỡng phân trang với BA để cập nhật TC_002.

---

Ghi chú: Báo cáo thực hiện dựa trên tài liệu URD I.1.1.1. SA.06 phiên bản hiện hành.
Các điểm GAP và Ambiguity cần xác nhận lại với BA trước khi bổ sung TC chính thức.
