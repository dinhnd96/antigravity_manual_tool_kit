# 📋 BÁO CÁO REVIEW TEST CASE — SA.07 Quản lý nhóm khách hàng

> **Reviewer:** Senior QA Lead (AI — Antigravity)
> **Ngày review:** 2026-04-02
> **File Test Case:** `Test case/C Thanh - SA07.xlsx`
> **Tài liệu URD:** `Feature_02_SA_Tham_So_He_Thong/tài liệu/SA.07- Quản lý nhóm khách hàng.docx`
> **Tổng số TC đã review:** 17 TC (TC_001 → TC_018, bỏ qua TC_006 — không tồn tại trong file)

---

## I. TỔNG QUAN

| Hạng mục | Số lượng |
|---|---|
| Tổng TC trong file | 17 TC |
| BR trong URD | 3 BR (BR_01, BR_02, BR_03) |
| TC có lỗi phát hiện | 17 (toàn bộ) |
| Lỗi Format Expected Result (thiếu 4 lớp) | 17 (100%) |
| Lỗi GAP (thiếu kịch bản) | 6 điểm |
| Lỗi Logic / Mismatch | 4 TC |
| Lỗi Title chung chung / nghèo thông tin | 8 TC |
| Lỗi Phân loại Feature sai | 6 TC |
| Lỗi TC_ID bị nhảy số | 1 điểm |
| Lỗi Ambiguity (dữ liệu bỏ trống/dấu …) | 2 TC |

---

## II. TRACEABILITY MATRIX — ĐỐI SOÁT BR vs TC

| BR trong URD | Mô tả BR | TC cover | Trạng thái |
|---|---|---|---|
| BR_01 | Operator chỉ có "=" và "IN"; Trạng thái chỉ có "Hoạt động, Không hoạt động"; Operator=IN cho phép nhiều giá trị ngăn cách dấu phẩy | TC_010, TC_011, TC_012, TC_013, TC_014 | ⚠️ Cover một phần — thiếu case Operator="=" nhận 1 giá trị; thiếu happy case validate giá trị trống |
| BR_02 | Nhấn "Đóng" → không lưu; Nhấn "Xác nhận" → kiểm tra bắt buộc, thông báo "Trường này bắt buộc" ngay dưới trường | TC_008, TC_009 | ⚠️ Cover một phần — thiếu xác minh text lỗi cụ thể "Trường này bắt buộc" và vị trí hiển thị |
| BR_03 | Không được sửa trạng thái nếu gắn code phí (HĐ/NHĐ/Chờ gắn); Được sửa nếu chưa gắn code phí hoặc toàn bộ code phí = Huỷ | TC_017, TC_018 | ⚠️ Cover một phần — thiếu case Sửa thành công khi nhóm KH chưa gắn BẤT KỲ code phí nào |
| Chức năng Xem (View) | Xem bản ghi, phân trang, chi tiết | TC_001, TC_002, TC_003, TC_004 | ⚠️ Đã cover cơ bản — thiếu case tìm kiếm/lọc nếu có |
| Chức năng Thêm mới | Thêm mới nhóm KH | TC_005, TC_007 đến TC_014 | ⚠️ Cover một phần |
| Chức năng Sửa | Sửa nhóm KH | TC_015 đến TC_018 | ⚠️ Cover một phần |
| Chức năng Xoá | Xoá bản ghi (nếu có) | Không có TC nào | ❌ GAP — Cần làm rõ với BA |
| Chức năng Tìm kiếm | Search/Filter danh sách | Không có TC nào | ❌ GAP — bổ sung nếu màn hình có tính năng này |

---

## III. BẢNG PHÁT HIỆN LỖI CHI TIẾT

| # | BR_ID / TC_ID | Loại phát hiện | Mô tả sự cố / Mâu thuẫn | Mức độ | Đề xuất sửa đổi |
|---|---|---|---|---|---|
| 1 | **Toàn bộ 17 TC** | **Format — Critical** | THIẾU CẤU TRÚC 4 LỚP EXPECTED RESULT. 100% TC đang viết Expected dưới dạng 1 câu chung chung, không đánh số (i)(ii)(iii)(iv). Thiếu hoàn toàn lớp (ii) UI feedback, lớp (iii) Trạng thái & Audit, lớp (iv) Output. | **Critical** | Bắt buộc rewrite toàn bộ Expected Result theo chuẩn 4 lớp. Xem mẫu tại Mục IV. |
| 2 | **TC_001** | Title chung chung | Title: "Kiểm tra hiển thị màn hình view" — Không thể hiện mục tiêu cụ thể. | Medium | Đổi: "Kiểm tra màn hình Danh sách nhóm khách hàng hiển thị đúng các cột và nút thao tác theo thiết kế" |
| 3 | **TC_002** | Title chung chung + **Ambiguity** | Expected để dấu "…" không điền ngưỡng số lượng bản ghi cụ thể. TC không thể thực thi vì tester không biết ngưỡng phân trang. | **High** | Làm rõ ngưỡng phân trang với BA (VD: 10/20/50 bản ghi). Điền số cụ thể vào Expected. |
| 4 | **TC_004** | Logic Mismatch | Expected gộp 2 ý vào 1 câu, thiếu xác nhận UI rõ ràng: field ở chế độ read-only, không có nút Lưu/Xác nhận. | Medium | Tách thành (i) Hiển thị đúng thông tin chi tiết; (ii) Toàn bộ field read-only, nút Edit/Lưu bị ẩn/disable. |
| 5 | **TC_005** | Title chung chung + Format | Title: "Hiển thị màn hình thêm mới" — Cực kỳ chung. Expected: "Hiển thị màn hình thêm mới nhóm KH" — Thiếu xác nhận nội dung màn hình, field cần có, trạng thái mặc định. | Medium | Title: "Kiểm tra nhấn nút Thêm mới mở form Thêm mới nhóm KH với đầy đủ các trường theo thiết kế". |
| 6 | **TC_006 (MISSING)** | **TC_ID bị nhảy số** | File có TC_005 nhảy thẳng sang TC_007, không tồn tại TC_006. | Medium | Kiểm tra lại file. Nếu bỏ qua có chủ đích thì chèn ghi chú "TC_006: Đã xóa / Dự phòng". |
| 7 | **TC_007** | Title + Format + Logic | Expected: "Hiển thị message thành công, lưu thông tin vào DB" — Thiếu: nội dung message cụ thể, trạng thái bản ghi sau lưu, Audit log. | **High** | Bổ sung 4 lớp: (i) Lưu DB thành công; (ii) Toast "Thêm mới thành công một nhóm khách hàng" (theo URD Table 3); (iii) Bản ghi mới xuất hiện danh sách; (iv) N/A. |
| 8 | **TC_008** | Logic Mismatch — BR_02 | Expected: "Hiển thị thông báo bắt buộc nhập và không cho lưu" — Thiếu: text lỗi cụ thể, vị trí hiển thị. URD BR_02 quy định rõ text = **"Trường này bắt buộc"** và ngay dưới field. | **High** | Expected (ii): "Hiển thị text lỗi màu đỏ 'Trường này bắt buộc' ngay bên dưới từng field bắt buộc bị bỏ trống". Dẫn chứng: URD BR_02. |
| 9 | **TC_009** | Title sai ngữ nghĩa + Format | Title dùng từ "không lưu" mang hàm ý thất bại, nhưng đây là Cancel flow chủ đích. Expected thiếu xác nhận: user quay về màn hình nào sau khi đóng. | Medium | Title: "Kiểm tra nhấn Đóng trên form Thêm mới hủy bỏ nhập liệu và trở về màn hình danh sách". |
| 10 | **TC_010** | Title + Format | Title mô tả dạng yêu cầu hơn là test scenario. Expected thiếu xác nhận KHÔNG có giá trị nào khác. | Medium | Title: "Kiểm tra dropdown Operator chỉ hiển thị đúng 2 lựa chọn '=' và 'IN', không có lựa chọn khác". |
| 11 | **TC_011** | **Logic Mismatch Critical — BR_01** | Expected: "Hiển thị các giá trị 'Hoạt động', **'Ngưng hoạt động'**" — **SAI SO VỚI URD**. BR_01 quy định text = **"Không hoạt động"**. Dẫn chứng: URD Table 4 - BR_01. | **Critical** | Sửa Expected thành **"Hoạt động, Không hoạt động"** đúng URD BR_01. Kiểm tra lại hệ thống thực tế. |
| 12 | **TC_012** | Format + Logic GAP | Expected: "Cho phép nhập nhiều giá trị, lưu thành công" — Thiếu xác nhận cách hiển thị dấu phẩy ngăn cách, format lưu trong DB. | Medium | Expected bổ sung: (i) Nhập A,B,C thành công; (ii) Field hiển thị "A,B,C"; (iii) DB lưu đúng chuỗi với dấu phẩy. |
| 13 | **TC_013** | Format + Ambiguity | Expected: "Hiển thị lỗi validate" — Quá chung. Steps: "Nhập value không có dấu phẩy đúng format" — mơ hồ, không biết nhập cụ thể gì. | Medium | Steps: "Nhập chuỗi thiếu dấu phẩy, VD: 'ABC DEF'". Expected (ii): Text lỗi cụ thể theo hệ thống. |
| 14 | **TC_014** | Format + Logic GAP | Expected: "Hiển thị lỗi **hoặc** không cho nhập" — Chữ "hoặc" thể hiện tester chưa rõ hành vi. Cần quyết định: chặn nhập hay báo lỗi khi submit. | **High** | Làm rõ với BA hành vi field khi Operator="=". Xóa chữ "hoặc". Expected chỉ định rõ 1 hành vi. |
| 15 | **TC_015, TC_016, TC_017, TC_018** | **Phân loại Feature sai** | 4 TC thuộc chức năng Sửa (Edit) đang bị phân loại Feature = **"Add"** — sai hoàn toàn. | Medium | Chuyển Feature = **"Edit"** cho TC_015, TC_016, TC_017, TC_018. |
| 16 | **TC_015** | Title chung chung + Format | Title: "Sửa thông tin nhóm KH thành công" — Không nêu điều kiện dữ liệu đầu vào. Expected: "Lưu thành công" — cực kỳ nghèo thông tin. | Medium | Title: "Kiểm tra sửa thông tin nhóm KH với dữ liệu hợp lệ lưu thành công vào hệ thống". Expected bổ sung 4 lớp. |
| 17 | **TC_017** | Logic Mismatch — BR_03 | Precondition viết tối nghĩa. Expected: "hệ thống không cho sửa và hiển thị thông báo" — thiếu content message cụ thể. | **High** | Làm rõ nội dung message lỗi với BA. Viết lại Precondition rõ ràng. Bổ sung 4 lớp Expected. |
| 18 | **TC_018** | Logic GAP — BR_03 | Precondition chỉ cover "toàn bộ Code phí = Huỷ". URD BR_03 còn quy định: **"Nhóm KH chưa được gắn vào code phí nào"** — là trường hợp RIÊNG BIỆT cũng được phép sửa trạng thái. | **High** | Tách thành 2 TC: TC_018a (chưa gắn code phí nào) và TC_018b (toàn bộ code phí đang gắn = Huỷ). |
| 19 | **GAP — Chức năng Xoá** | GAP | URD Table 1 liệt kê 3 chức năng: Thêm mới, Sửa, Xem — không đề cập Xoá. Cần xác nhận với BA nút Xoá có trên UI thực tế không. | Medium | Làm rõ với BA. Nếu có: bổ sung TC Xoá thành công và Xoá thất bại khi có ràng buộc. |
| 20 | **GAP — Tìm kiếm/Lọc** | GAP | Không có TC nào kiểm tra Search/Filter trên danh sách. | Medium | Confirm UI với BA. Nếu có search: bổ sung TC Search (chính xác/không kết quả/partial match). |
| 21 | **GAP — Thêm mới trùng tên** | GAP | Không có TC kiểm tra thêm mới với tên nhóm KH đã tồn tại — negative case quan trọng. | **High** | Làm rõ với BA: Tên nhóm KH có phải duy nhất không? Nếu có → thêm TC_NEW_01. |
| 22 | **GAP — Validate Operator="=" nhận 1 giá trị** | GAP — BR_01 | TC_014 chỉ có negative case. Thiếu happy case: Operator="=" + nhập đúng 1 giá trị → lưu thành công. | Medium | Bổ sung TC_NEW_02: Kiểm tra Operator="=" nhập đúng 1 giá trị hợp lệ → lưu thành công. |

---

## IV. MẪU REWRITE EXPECTED RESULT CHUẨN 4 LỚP

### TC_007 — Thêm mới thành công nhóm KH với dữ liệu hợp lệ

**HIỆN TẠI (sai format):**
> "Hiển thị message thành công, lưu thông tin vào DB"

**CHUẨN 4 LỚP (đề xuất):**
```
(i)  Nghiệp vụ: Hệ thống lưu thành công bản ghi Nhóm khách hàng mới
     với toàn bộ thông tin hợp lệ đã nhập.
(ii) UI: Form đóng lại. Toast notification hiển thị:
     "Thêm mới thành công một nhóm khách hàng"
     (dẫn chứng: URD Luồng nghiệp vụ - Table 3, Step cuối).
     Grid danh sách reload, bản ghi mới xuất hiện với đầy đủ thông tin chính xác.
(iii) Trạng thái & Audit: Bản ghi có Trạng thái = "Hoạt động" (hoặc theo thiết kế).
      Ghi Audit log: Người tạo + Thời điểm tạo.
(iv) Output: N/A.
```

---

### TC_008 — Validate BR_02: Bắt buộc nhập trường bắt buộc

**HIỆN TẠI (sai format):**
> "Hiển thị thông báo bắt buộc nhập và không cho lưu"

**CHUẨN 4 LỚP (đề xuất):**
```
(i)  Nghiệp vụ: Hệ thống không lưu bản ghi. Dữ liệu không được insert vào DB.
(ii) UI: Hiển thị text lỗi màu đỏ "Trường này bắt buộc" ngay bên dưới
     từng trường bắt buộc bị bỏ trống (dẫn chứng: URD BR_02).
     Form vẫn mở, không đóng lại.
(iii) Trạng thái & Audit: Không thay đổi dữ liệu. Không ghi Audit log.
(iv) Output: N/A.
```

---

### TC_017 — Không cho phép sửa trạng thái khi nhóm KH đang gắn code phí hiệu lực

**HIỆN TẠI (sai format):**
> "hệ thống không cho sửa và hiển thị thông báo"

**CHUẨN 4 LỚP (đề xuất):**
```
(i)  Nghiệp vụ: Hệ thống từ chối lưu thay đổi trạng thái.
     Giá trị trạng thái trong DB không bị thay đổi.
(ii) UI: Hiển thị popup/toast cảnh báo màu đỏ/cam với nội dung message
     ràng buộc (cần xác nhận text message cụ thể với BA).
(iii) Trạng thái & Audit: Trạng thái nhóm KH giữ nguyên giá trị ban đầu.
      Không ghi Audit log thay đổi.
(iv) Output: N/A.
```

---

## V. DANH SÁCH TC CẦN BỔ SUNG MỚI (GAP)

| TC_ID mới | Nhóm | Mô tả | BR / Điểm tham chiếu |
|---|---|---|---|
| TC_NEW_01 | Add | Kiểm tra thêm mới nhóm KH có tên đã tồn tại → hệ thống báo lỗi (nếu constraint unique) | Cần xác nhận BA |
| TC_NEW_02 | Add | Kiểm tra Operator="=" nhập đúng 1 giá trị hợp lệ → lưu thành công | BR_01 |
| TC_NEW_03 | Add | Kiểm tra validate text lỗi cụ thể "Trường này bắt buộc" hiển thị ngay dưới từng field bị bỏ trống | BR_02 |
| TC_NEW_04 | Edit | Kiểm tra sửa trạng thái thành công khi nhóm KH **chưa được gắn vào bất kỳ code phí nào** | BR_03 |
| TC_NEW_05 | Edit | Kiểm tra nhấn Đóng trên form Sửa hủy bỏ chỉnh sửa và không lưu dữ liệu | BR_02 |
| TC_NEW_06 | Search | Kiểm tra tìm kiếm nhóm KH theo tên (nếu màn hình có search bar) | Confirm UI với BA |
| TC_NEW_07 | Add | Kiểm tra validate format sai khi Operator=IN, VD: nhập "ABC DEF" không có dấu phẩy → hiển thị lỗi cụ thể | BR_01 |

---

## VI. KẾT LUẬN & KHUYẾN NGHỊ

### �� P1 — Sửa ngay (Blockers):
1. **Rewrite toàn bộ Expected Result** theo chuẩn 4 lớp (i, ii, iii, iv) — lỗi format ảnh hưởng 100% TC (17/17).
2. **Sửa TC_011 Logic Critical**: Expected "Ngưng hoạt động" **sai với URD** — phải là **"Không hoạt động"** (URD BR_01). Logic Mismatch mức Critical, ảnh hưởng trực tiếp kết quả test.
3. **Làm rõ Ambiguity TC_002**: Điền ngưỡng phân trang cụ thể thay cho dấu "…".
4. **Tách TC_018** thành 2 TC riêng biệt để cover đủ 2 nhánh của BR_03.

### 🟡 P2 — Sửa tiếp (Improvements):
5. Chuyển Feature = **"Edit"** cho TC_015, TC_016, TC_017, TC_018 (đang bị gắn nhầm vào "Add").
6. Điền lại TC_006 hoặc ghi chú giải thích lý do nhảy số.
7. Sửa Expected TC_008 theo text message chính xác **"Trường này bắt buộc"** (URD BR_02).
8. Bổ sung TC_NEW_01, TC_NEW_02, TC_NEW_03, TC_NEW_04, TC_NEW_05 để cover đầy đủ validate và BR_03.

### 🟢 P3 — Cải tiến / Làm rõ (Nice-to-have):
9. Xác nhận với BA: Có chức năng Xoá không? Nếu có → bổ sung TC tương ứng.
10. Xác nhận với BA: Màn hình có Search/Filter không? Nếu có → bổ sung TC_NEW_06.
11. Xác nhận nội dung toast message chính xác sau Thêm mới / Sửa thành công.
12. Sửa Title các TC chung chung: TC_001, TC_002, TC_005, TC_009, TC_010, TC_015.

---

> **Ghi chú:** Báo cáo thực hiện dựa trên tài liệu `SA.07- Quản lý nhóm khách hàng.docx` phiên bản hiện hành.
> Các điểm GAP và Ambiguity cần xác nhận lại với BA trước khi bổ sung TC chính thức vào bộ test.
