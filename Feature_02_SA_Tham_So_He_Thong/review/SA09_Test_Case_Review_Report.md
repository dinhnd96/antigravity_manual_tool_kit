# 📋 BÁO CÁO REVIEW TEST CASE — SA.09 Quản lý Nhóm Code Phí Định Kỳ

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** I.1.1.1. SA.09 – Quản lý nhóm code phí định kỳ (.docx)
> **Bộ Test Case:** SA09.xlsx (Sheet: TestCases — 15 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng |
|:---|:---|
| Tổng TC đã có | **15** |
| TC phát hiện lỗi / cần sửa | **11** |
| Gap nghiệp vụ (thiếu kịch bản) | **7** |
| Lỗi Logic / Expected sai nội dung | **4** |
| Lỗi Tên trường không khớp mockup | **3 TC bị ảnh hưởng** |
| Lỗi Format (Precondition, Expected) | **5** |
| TC đề xuất bổ sung mới | **7** |

> [!IMPORTANT]
> Bộ TC SA09 có cấu trúc khá tốt (4 lớp Expected, Coverage sheet, Dedup_Log). Tuy nhiên so khớp với Mockup UI thực tế phát hiện nhiều tên trường sai và thiếu nghiêm trọng các kịch bản Checker và State Transition.

---

## 2. PHÂN TÍCH MOCKUP UI

**Form Thêm mới — Field thực tế (image2):**
- Cột trái: `Mã` (*), `Tên nhóm code phí` (*), `Thứ tự ưu tiên` (*)
- Cột phải: `Tần suất` (radio: **Hàng tháng** / **Hàng năm**), `Ngày thu` (radio + input), `Ngày thu theo dữ liệu` (radio), `Bảng dữ liệu` (dropdown), `Trường dữ liệu` (dropdown), `Code phí` (dropdown + nút **Kiểm tra**)
- Grid "Danh sách code phí": `Mã phí` | `Tên phí` | `Loại tiền tệ` | `Mã hạch toán` | `VAT` | `Công thức tính phí`
- Nút: `Xác nhận` | `Đóng`

**Màn hình Danh sách — Cột grid (image1):**
`Mã nhóm` | `Tên nhóm code phí` | `Tần suất` | `Thứ tự ưu tiên` | `Ngày thu` | `Số lượng code phí` | `Hành động (Sửa/Xem/Xóa)`

> [!WARNING]
> **Tần suất chỉ có "Hàng tháng" và "Hàng năm"** — KHÔNG có "Quý". TC SA09-BR-HAP-002 dùng `Tần suất = "Quý"` là SAI hoàn toàn.

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | Nhập đủ trường (*) trước khi "Xác nhận" | SA09-BR-HAP-001, SA09-BR-NEG-001 | ⚠️ Tên field sai |
| BR_02 | Chọn "Đóng" → không lưu | SA09-BR-HAP-004 | ✅ Đủ |
| BR_03 | Mã nhóm Code phí phải duy nhất | SA09-BR-NEG-002 | ✅ Đủ |
| BR_04 | Lọc Code phí theo Loại=Định kỳ + Tần suất | SA09-BR-HAP-002 | ❌ Tần suất "Quý" không tồn tại |
| BR_05 | 1 Code phí chỉ trong 1 nhóm | SA09-BR-NEG-003 | ✅ Đủ |
| BR_06 | Priority ghi Topic theo thứ tự thấp→cao | SA09-BR-HAP-003 | ⚠️ Thiếu Precondition + Output |
| — | Chờ duyệt → Đã duyệt (Checker Approve) | **KHÔNG CÓ** | 🔴 GAP NGHIÊM TRỌNG |
| — | Checker Reject | **KHÔNG CÓ** | 🔴 GAP NGHIÊM TRỌNG |
| — | Tần suất = Hàng tháng (BR_04 variant) | **KHÔNG CÓ** | ⚠️ GAP |
| — | Tần suất = Hàng năm (BR_04 variant) | **KHÔNG CÓ** | ⚠️ GAP |
| — | Ngày thu theo dữ liệu | Ghi Note nhưng chưa tạo TC | ⚠️ GAP |
| — | Nút "Kiểm tra" trên form | **KHÔNG CÓ** | ⚠️ GAP |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI

| # | TC_ID / BR_ID | Loại | Mô tả sự cố | Mức độ | Đề xuất |
|:---|:---|:---|:---|:---|:---|
| 1 | BR_04 / SA09-BR-HAP-002 | **Logic Mismatch** | Step 1: `Tần suất = "Quý"` nhưng Mockup chỉ có radio **"Hàng tháng"** / **"Hàng năm"**. TC sẽ FAIL ngay bước đầu vì giá trị không tồn tại. | 🔴 High | Sửa Step 1: Chọn `"Hàng tháng"`. Tạo 2 variants: SA09-BR-HAP-002A (Hàng tháng) và SA09-BR-HAP-002B (Hàng năm). |
| 2 | BR_06 / SA09-BR-HAP-003 | **Logic Incomplete** | (a) Precondition thiếu điều kiện cả 2 nhóm phải ở trạng thái **Đã duyệt** trước khi Job chạy. (b) `(iv) Output` quá chung: không nêu thứ tự offset message hoặc nội dung trường Priority trong JSON. | 🔴 High | Thêm Precondition 4: *"Cả 2 Nhóm phí đã ở trạng thái Đã duyệt."* Sửa Output: *"Message trên Topic Kafka: Nhóm A (priority=1) có offset thấp hơn Nhóm B (priority=2). JSON có trường priority đúng giá trị."* |
| 3 | BR_01 / SA09-BR-HAP-001 | **Tên Field Sai** | Step 2 dùng: `"Mã nhóm, Tên nhóm, Mức độ ưu tiên"`. Label thực tế trên mockup là: **"Mã"**, **"Tên nhóm code phí"**, **"Thứ tự ưu tiên"**. | 🔴 High | Sửa Step 2: `"Nhập: Mã (*), Tên nhóm code phí (*), Thứ tự ưu tiên (*), Tần suất, Ngày thu."` |
| 4 | UI-FUNC.01 / SA09-UI-01-ADD-001 | **Tên Field Sai + Expected Thiếu** | `(ii) UI` ghi field: `"Mã nhóm, Tên nhóm, Loại tính phí, Mức độ ưu tiên"`. Sai: (a) Tên field sai; (b) Không có field **"Loại tính phí"** trên form này; (c) Thiếu hoàn toàn: Bảng dữ liệu, Trường dữ liệu, Code phí (+ nút Kiểm tra), grid Danh sách code phí 6 cột. | 🔴 High | Sửa lại `(ii) UI` liệt kê đầy đủ tất cả field đúng tên theo mockup: *Mã (*), Tên nhóm code phí (*), Thứ tự ưu tiên (*), Tần suất (Hàng tháng/Hàng năm), Ngày thu, Ngày thu theo dữ liệu, Bảng dữ liệu, Trường dữ liệu, Code phí + nút Kiểm tra. Grid: Mã phí, Tên phí, Loại tiền tệ, Mã hạch toán, VAT, Công thức tính phí.* |
| 5 | GAP | **Gap — Thiếu Checker** | Luồng nghiệp vụ: Maker → Chờ duyệt → Checker Approve/Reject → Đã duyệt. Toàn bộ bộ TC **không có TC Checker nào**. | 🔴 High | Thêm: `SA09-FLOW-CHECKER-001` (Checker Duyệt → Đã duyệt) và `SA09-FLOW-CHECKER-002` (Checker Từ chối → Maker nhận thông báo). |
| 6 | GAP | **Gap — Variant Tần suất** | Không có TC filter theo **"Hàng tháng"** và **"Hàng năm"** (2 giá trị thực tế). | 🟠 Medium | Tạo SA09-BR-HAP-002A (Hàng tháng) và SA09-BR-HAP-002B (Hàng năm). |
| 7 | GAP | **Gap — Ngày thu theo dữ liệu** | Note ghi cần bổ sung nhưng không tạo TC. Note còn bị viết trùng lặp 2 lần cùng nội dung. | 🟠 Medium | Tạo `SA09-BR-HAP-002C`: Chọn "Ngày thu theo dữ liệu", chọn Bảng dữ liệu + Trường dữ liệu, mở cây SPDV, verify filter. |
| 8 | GAP | **Gap — Nút "Kiểm tra"** | Form có nút **"Kiểm tra"** cạnh Code phí — không có TC nào test. | 🟠 Medium | `SA09-UI-KIEMTRA-001` (Happy) và `SA09-UI-KIEMTRA-002` (Negative: code phí đã gán nhóm khác). |
| 9 | UI-FUNC.05 / SA09-UI-05-DELETE-001 | **Gộp Trạng Thái** | Precondition gộp: *"trạng thái **Nháp/Chờ duyệt**"* vào 1 TC. | 🟠 Medium | Bóc tách: SA09-UI-05-DELETE-001 (Nháp) và SA09-UI-05-DELETE-003 (Chờ duyệt). |
| 10 | BR_01 / SA09-BR-NEG-001 | **Precondition Thiếu** | Precondition chỉ ghi *"Tại màn hình Thêm mới"* — thiếu điều kiện đăng nhập/phân quyền. Tên field trong Steps cũng sai tương tự #3. | 🟠 Medium | Sửa Precondition và tên field theo mockup. |
| 11 | FLOW / SA09-FLOW-001 | **Flow Thiếu Checker** | TC E2E Lifecycle chỉ đi Maker CRUD, không có bước Checker Approve giữa. | 🟠 Medium | Thêm Step 2.5: *"[Checker] Đăng nhập Checker, duyệt bản ghi → trạng thái 'Đã duyệt'."* |
| 12 | SA09-BR-HAP-003 | **Format Precondition** | Điểm 2 bị bỏ qua, có 2 điểm mang số 3 (1, 3, 3). | 🟡 Low | Sửa: đánh số thứ tự 1, 2, 3 đúng thứ tự. |
| 13 | SA09-BR-HAP-002 | **Format Note Trùng** | Cột Note ghi 2 lần cùng nội dung. | 🟡 Low | Xóa dòng trùng. |
| 14 | SA09-UI-07-EXCEL-001 | **Format Audit** | `(iii)` ghi *"User A"* thay vì vai trò cụ thể. | 🟡 Low | Sửa: *"Maker"*. |
| 15 | GAP | **Gap — Phân trang** | Mockup có phân trang, không có TC kiểm tra. | 🟡 Low | TC smoke phân trang cơ bản. |

---

## 5. CHECKLIST FORMAT

| TC_ID | 4 lớp Expected | Precondition đánh số | Note gộp variant |
|:---|:---:|:---:|:---:|
| SA09-BR-HAP-001 | ✅ | ✅ | N/A |
| SA09-BR-NEG-001 | ✅ | ❌ Thiếu đk đăng nhập | ✅ Có Note |
| SA09-BR-HAP-004 | ✅ | ✅ | N/A |
| SA09-BR-NEG-002 | ✅ | ✅ | N/A |
| SA09-BR-HAP-002 | ✅ | ✅ | ❌ Note lặp 2 lần |
| SA09-BR-NEG-003 | ✅ | ✅ | N/A |
| SA09-BR-HAP-003 | ✅ | ❌ Đánh số trùng (1,3,3) | N/A |
| SA09-UI-06-SEARCH-001 | ✅ | ✅ | N/A |
| SA09-UI-04-VIEW-001 | ✅ | ✅ | N/A |
| SA09-UI-07-EXCEL-001 | ✅ | ✅ | N/A |
| SA09-UI-03-EDIT-001 | ✅ | ✅ | N/A |
| SA09-UI-05-DELETE-001 | ✅ | ❌ Gộp "Nháp/Chờ duyệt" | N/A |
| SA09-FLOW-001 | ✅ | ✅ | ✅ Có Note |
| SA09-UI-01-ADD-001 | ✅ | ✅ | N/A |
| SA09-UI-05-DELETE-002 | ✅ | ✅ | N/A |

---

## 6. TC CẦN BỔ SUNG MỚI

| TC_ID đề xuất | BR Ref | Mục đích |
|:---|:---|:---|
| SA09-BR-HAP-002A | BR_04 | Filter code phí, Tần suất = **Hàng tháng** |
| SA09-BR-HAP-002B | BR_04 | Filter code phí, Tần suất = **Hàng năm** |
| SA09-BR-HAP-002C | BR_04 | Filter theo **Ngày thu theo dữ liệu** |
| SA09-UI-KIEMTRA-001 | UI-FUNC.01 | Nút **"Kiểm tra"** Happy — code phí hợp lệ |
| SA09-UI-KIEMTRA-002 | UI-FUNC.01 | Nút **"Kiểm tra"** Negative — code phí đã gán |
| SA09-FLOW-CHECKER-001 | FLOW | Checker **Duyệt** → trạng thái: Đã duyệt |
| SA09-FLOW-CHECKER-002 | FLOW | Checker **Từ chối** → Maker nhận thông báo |

---

## 7. ƯU TIÊN XỬ LÝ

```
🔴 CRITICAL — Xử lý ngay trước Regression:
  1. Sửa tên Field theo mockup (SA09-BR-HAP-001, SA09-BR-NEG-001, SA09-UI-01-ADD-001):
     "Mã nhóm" → "Mã" | "Tên nhóm" → "Tên nhóm code phí" | "Mức độ ưu tiên" → "Thứ tự ưu tiên"
  2. Sửa SA09-BR-HAP-002: Tần suất "Quý" → tách 2 TC (Hàng tháng / Hàng năm)
  3. Tạo SA09-FLOW-CHECKER-001 và SA09-FLOW-CHECKER-002 (Checker Approve/Reject)
  4. Bổ sung Precondition cho SA09-BR-HAP-003: cả 2 nhóm phải ở trạng thái Đã duyệt

🟠 MEDIUM — Xử lý Sprint hiện tại:
  5. Bóc tách SA09-UI-05-DELETE-001 thành 2 TC (Nháp / Chờ duyệt)
  6. Tạo SA09-BR-HAP-002C (Ngày thu theo dữ liệu)
  7. Tạo SA09-UI-KIEMTRA-001/002 (nút "Kiểm tra")
  8. Bổ sung bước Checker vào SA09-FLOW-001
  9. Sửa Precondition SA09-BR-NEG-001

🟡 LOW — Sprint tiếp theo:
  10. Sửa đánh số Precondition SA09-BR-HAP-003
  11. Xóa Note trùng SA09-BR-HAP-002
  12. TC Phân trang
  13. Sửa "User A" → "Maker" trong SA09-UI-07-EXCEL-001
```

---

> **Đánh giá tổng thể:** Bộ TC SA09 đạt ~**65% hoàn thiện**. Điểm mạnh: cấu trúc 4 lớp Expected, Coverage sheet, Dedup_Log. Điểm yếu nghiêm trọng: **thiếu hoàn toàn luồng Checker** và **tên field không khớp Mockup**.
