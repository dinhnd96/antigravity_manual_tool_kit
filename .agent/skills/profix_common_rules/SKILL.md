---
name: profix_common_rules
description: >
  Kho Quy Tắc Chung (Common Rules) của dự án ProfiX Phase 1 – tổng hợp từ tài liệu "Quy tắc chung.docx".
  Skill này được nhúng tự động vào `manual_requirement_analyzer` và `qa_test_case_generator`
  để AI không hỏi BA lại các câu hỏi đã được định nghĩa ở cấp hệ thống.
---

# Quy Tắc Chung – ProfiX Phase 1

> **Nguồn gốc:** Tài liệu `Quy tắc chung.docx` – dự án ProfiX Phase 1 (PVCB).
> **Phạm vi áp dụng:** Toàn bộ chức năng trong hệ thống ProfiX trừ khi tài liệu US cụ thể ghi đè (override) quy tắc.
> **Cách dùng:** Khi phân tích bất kỳ US nào, AI BẮT BUỘC tra cứu mục này trước khi đặt câu hỏi cho BA về các hành vi chung.

---

## QTC-01 · Định Dạng Trường (Field Formats)

### QTC-01.1 · Combobox
- Người dùng chọn giá trị từ danh sách **hoặc** gõ text để tìm kiếm (search-as-you-type).
- Khi gõ text: hệ thống tìm kiếm dữ liệu theo giá trị người nhập.

### QTC-01.2 · Dropdown List
- Người dùng nhấn vào thanh bar → hệ thống hiển thị danh sách lựa chọn.
- Chỉ được chọn **duy nhất 1 giá trị**.

### QTC-01.3 · Multiple Select Dropdown
- Người dùng có thể chọn **1 hoặc nhiều** giá trị.
- Hỗ trợ gõ text để tìm kiếm trong danh sách.

### QTC-01.4 · Number
- Chỉ được nhập số.
- Hiển thị: phân cách hàng nghìn bằng dấu phẩy (`,`), hàng thập phân bằng dấu chấm (`.`), lấy **2 chữ số** sau dấu chấm.
- Ngoại lệ: VND và JPY **không có** hàng thập phân.

### QTC-01.5 · Date
- Định dạng hiển thị mặc định: `dd/mm/yyyy`.
- Người dùng có thể nhập trực tiếp **hoặc** chọn từ Calendar Picker.
- Tìm kiếm theo khoảng thời gian (Từ ngày – Đến ngày):
  - `Từ ngày` = `dd/mm/yyyy 00:00:00.000`
  - `Đến ngày` = `dd/mm/yyyy 23:59:59.999`

### QTC-01.6 · Text – Giới Hạn Ký Tự Mặc Định
Áp dụng khi cột "Ràng buộc" trong bảng field-description **không ghi rõ** độ dài:

| Loại trường | Độ dài tối đa |
|---|---|
| Mã | 50 ký tự |
| Tên | 50 ký tự |
| Diễn giải / Ghi chú / Nội dung | 300 ký tự |

---

## QTC-02 · Tìm Kiếm Nhanh (Quick Search Bar)

- Tìm kiếm theo **Mã hoặc Tên** (gần đúng / Like search).
- Hành vi:
  - Người dùng nhập text → hệ thống ghi nhận và tìm kiếm.
  - Khi **đang dùng Quick Search**, nút "Lọc nâng cao" bị **disabled** và ngược lại.
- **Quy tắc tìm kiếm chung (Quick Search & Lọc nâng cao):**

| Nội dung | Quy tắc |
|---|---|
| Kết hợp điều kiện | AND giữa các điều kiện |
| Hoa/thường | **Không phân biệt** (case-insensitive) |
| Dấu tiếng Việt | Bỏ dấu khi tìm gần đúng tại các ô nhập text |
| Trim khoảng trắng | **Tự động trim** trước khi gửi backend |
| Điều kiện rỗng | **Không đưa vào query** (bỏ qua trường để trống) |

---

## QTC-03 · Lọc Nâng Cao (Advanced Filter)

- Người dùng nhấn "Lọc nâng cao" → hệ thống hiển thị màn hình Lọc nâng cao (thường là Drawer).
- Nếu chưa nhập trường bắt buộc → thông báo `"Trường này bắt buộc"` hiển thị ngay dưới trường thiếu.
- Nếu dữ liệu hợp lệ → nhấn "Áp dụng" → hệ thống trả kết quả thoả mãn **đồng thời** các điều kiện (AND).
- Nếu để trống tất cả điều kiện → nhấn "Áp dụng" → hệ thống hiển thị **toàn bộ dữ liệu**.
- Nhấn "Xóa lọc" → reset tất cả trường về trống → **đóng Drawer** → lưới trở về trạng thái mặc định.
- Quy tắc tìm kiếm: **giống QTC-02** (AND, case-insensitive, bỏ dấu, auto-trim, rỗng bỏ qua).

---

## QTC-04 · Tra Cứu (Search with Explicit Button)
- Khi truy cập chức năng  → hệ thống **mặc định không hiển thị danh sách** (kết quả rỗng, chờ user nhập điều kiện).
- Nếu người dùng không nhập điều kiện và tất cả các điều kiện tìm kiếm là không bắt buộc mà bấm tra cứu thì hệ thống hiển thị tất cả dữ liệu thuộc chức năng
- Người dùng nhập điều kiện → nhấn nút "Tra cứu" → hệ thống tìm kiếm.
- Nhấn "Xóa tra cứu" → hệ thống clear điều kiện → **danh sách trở về mặc định** (không hiển thị kết quả nếu không nhập điều kiện theo từng chức năng cụ thể).

---

## QTC-05 · Tải Xuống (Export / Download)

- Nút "Tải xuống" hiển thị khi màn hình **có lưới dữ liệu**.
- Tải xuống dữ liệu **theo điều kiện tìm kiếm đang áp dụng** (không phải toàn bộ DB).
- **Định dạng mặc định:** Excel (`.xlsx`). Nếu US cụ thể dùng định dạng khác → sẽ ghi rõ trong tài liệu US đó.
- **Tên file:** `{Tên chức năng} - {yyyymmddhhmmss}`
  - Ví dụ: `Quản lý Chương trình ưu đãi - 20260421101500.xlsx`
- **Template:** Theo các trường dữ liệu được mô tả trên lưới danh sách của từng chức năng cụ thể.
- Không có giới hạn số dòng

---

## QTC-06 · Phân Trang (Pagination)

- Mặc định hiển thị **50 bản ghi / trang**.
- Nếu chức năng cụ thể dùng số bản ghi khác → sẽ ghi rõ trong tài liệu US đó.
- Các nút điều hướng:
  - **Số trang:** nhấn để nhảy đến trang đó.
  - **Trang tiếp theo:** disabled nếu đang ở trang cuối.
  - **Trang trước đó:** disabled nếu đang ở trang đầu.
- ⚠️ Thứ tự sắp xếp mặc định (sort mặc định của lưới)theo ngày update, ngày tạo giảm dần
---

## QTC-07 · Upload File

- Định dạng được phép upload: **Excel** (`.xlsx`).
- Dung lượng tối đa: **theo tham số hệ thống** (không có con số cứng trong Quy tắc chung).
- Validate sau khi upload:
  - Định dạng/dung lượng không hợp lệ → toast `"Định dạng hoặc dung lượng không hợp lệ"` → user chọn lại.
  - Dữ liệu hợp lệ → hiển thị danh sách bản ghi thành công.
  - Dữ liệu không hợp lệ → **highlight** dòng lỗi.
- Chi tiết rule validate từng trường → xem tại mục Upload của US tương ứng.

---

## QTC-08 · Lịch Sử Tác Động (Audit Trail / History)

- Áp dụng cho: **Code phí, Biểu phí, Chương trình ưu đãi**.
- Vị trí: Màn hình Xem chi tiết của từng chức năng quản lý.
- Cách truy cập: Nhấn vào link/button **"Lịch sử tác động"** → hệ thống hiển thị **popup**.
- Nội dung popup – sắp xếp từ **gần nhất đến xa nhất** (theo thời gian duyệt):

| Trường | Định dạng | Mô tả |
|---|---|---|
| Ngày cập nhật | `dd/mm/yyyy` (hyperlink) | Thời điểm hành động được phê duyệt. Nhấn hyperlink → xem bản lịch sử trước khi sửa. |
| Tác động | Text | Hành động: `Thêm mới`, `Chỉnh sửa` |
| Người cập nhật | Text | Username của người thực hiện hành động |
| Người phê duyệt | Text | Hiển thị người phê duyệt cuối của chức năng |

---

## QTC-09 · Tra Cứu CIF

Mục đích: Cung cấp màn hình Popup tra cứu nhanh CIF theo các thông tin thể nhân của Khách hàng tại module Tra cứu, Báo cáo.
- **Nút Tra cứu CIF:** Mở popup tìm kiếm.
- **Nút Tra cứu / Xóa tra cứu:** 
  - Tra cứu: Hệ thống ghi nhận và tìm kiếm.
  - Xóa tra cứu: Reset/Xóa các điều kiện lọc.

**Các trường điều kiện tìm kiếm:**
1. **Số điện thoại** (Text): Bắt buộc bắt đầu bằng số `0`. Nếu sai format báo lỗi *"Định dạng chưa đúng"*.
2. **Loại khách hàng** (Dropdown): Chọn 1 trong danh sách: `KHCN`, `KHTC`, `DNSN`, `CBNV`.
3. **Chi nhánh quản lý** (Combobox).
4. **Tỉnh** (Combobox): Phải chọn Tỉnh rồi mới chọn được Phường/xã.
5. **Phường/Xã** (Combobox): Lọc theo Tỉnh. Disable nếu chưa chọn Tỉnh. Nếu đổi Tỉnh → Reset Phường/xã về rỗng.
6. **Trạng thái** (Dropdown): `Hoạt động`, `Tạm dừng`.

**Lưới kết quả:**
- STT, Mã CIF, Số điện thoại, Tên, Chi nhánh quản lý, Tỉnh, Trạng thái.
- **Hành vi click "Mã CIF":** Màn hình tra cứu đóng lại → Hệ thống tự động back và fill Mã CIF được chọn vào trường "Mã CIF" ở màn hình gọi nó ra (Tra cứu/Báo cáo tương ứng).

---

## QTC-10 · Nguyên Tắc Phân Quyền Dữ Liệu (Data Authorization by Block)

Áp dụng cho các chức năng: Danh mục SPDV & Code phí, Biểu phí, Chương trình ưu đãi, Xem nghiệp vụ theo cây thư mục, Xem code phí theo KH, Lịch sử thu phí, Lịch thu phí dự kiến, Xem CTƯĐ theo KH, Tác vụ chờ duyệt, Báo cáo.

### Logic phân quyền theo Khối (Block):

**Màn hình không có trường lọc "Khối":**
- Hệ thống tự động xác định Khối từ thông tin người dùng.

**Màn hình có trường lọc "Khối":**
- User thuộc **Khối KHCN hoặc KHDN** → mặc định hiển thị Khối của user, **không cho sửa**.
- User **không thuộc** KHCN/KHDN → hiển thị dropdown chọn Khối tự do.

### Ma trận dữ liệu theo Khối:

| Loại dữ liệu | Khối KHCN | Khối KHDN | Khối khác |
|---|---|---|---|
| SPDV & Code phí | SPDV: Tất cả. Code phí: Loại KH = KHCN/DNSN/CBNV | SPDV: Tất cả. Code phí: Loại KH = KHTC | Tất cả |
| Biểu phí | Biểu phí có Code phí Loại KH = KHCN/DNSN/CBNV | Biểu phí có Code phí Loại KH = KHTC | Tất cả |
| Chương trình ưu đãi | CTƯĐ có Loại KH = KHCN/DNSN/CBNV | CTƯĐ có Loại KH = KHTC | Tất cả |
| Lịch sử/Lịch thu phí dự kiến | Khách hàng là KHCN/DNSN | Khách hàng là KHTC | Tất cả |

---

## QTC-11 · Nguyên Tắc Xử Lý Lỗi (FE-First Error Handling)

> **Chiến lược xử lý lỗi hiện tại của dự án ProfiX:**
> FE là tầng **chặn lỗi đầu tiên** để hạn chế tối đa việc hiển thị mã lỗi kỹ thuật từ BE lên màn hình người dùng. Tuy nhiên, nếu FE **chưa chặn được** một trường hợp nào đó, mã lỗi từ BE vẫn có thể xuất hiện trên UI.

### Nguyên tắc thiết kế Test Case theo QTC-11:

**Luồng Happy Path / Validation thông thường:**
- **Expected Result ưu tiên mô tả hành vi FE:** FE không cho phép thực hiện hoặc hiển thị thông báo lỗi thân thiện (toast, inline message, highlight field…).
- Không còn tham chiếu bảng mã lỗi PR.XX cứng trong Expected Result.

**Luồng Negative / Edge Case FE chưa chặn:**
- Vẫn thiết kế Test Case bao phủ các trường hợp FE **có thể bỏ sót** (bypass validation, gọi API trực tiếp, edge case dữ liệu hiếm gặp…).
- **Expected Result cho trường hợp này:** Hệ thống vẫn xử lý an toàn — hoặc hiển thị thông báo lỗi BE (dạng mã lỗi kỹ thuật) — **không crash, không mất dữ liệu**.

### Hướng dẫn viết Expected Result:

| Tình huống | Expected Result mẫu |
|---|---|
| FE chặn được hoặc validate thành công (chặn được) | `FE không cho phép thực hiện hoặc hiển thị thông báo "[Nội dung lỗi thân thiện]" tại [vị trí field/toast]` |
| FE chưa chặn → BE trả lỗi | `Hệ thống hiển thị thông báo lỗi từ BE (có thể dạng mã lỗi kỹ thuật). Dữ liệu không bị thay đổi.` |
| Cả FE & BE đều xử lý đúng | `Hệ thống ngăn lưu thành công. Không có side-effect.` |

---

## QTC-12 · Luồng Maker-Checker (Quản lý Phê duyệt - US25)

> **Dựa trên US25 (Quản lý Phê duyệt), áp dụng cho toàn bộ các chức năng có luồng phê duyệt (Maker-Checker):**

### 1. Tác vụ chờ duyệt (Dành cho Checker)
- **Hành động hiển thị phụ thuộc phân quyền:**
  - Nếu Checker **được phân quyền** tại cấp duyệt hiện tại và trạng thái tác vụ = **Chờ duyệt** → Hiển thị 3 nút: **Xem, Phê duyệt, Từ chối**.
  - Nếu Checker **không được phân quyền** tại cấp duyệt hiện tại, hoặc bản ghi ở trạng thái **Đã duyệt / Từ chối duyệt** → Chỉ hiển thị nút **Xem** (Không có Phê duyệt/Từ chối).
- **Lịch sử phê duyệt:** Khi nhấn "Xem lịch sử phê duyệt", hệ thống hiển thị Popup gồm: Cấp duyệt, Người thực hiện (phê duyệt/từ chối), Khối, Phòng ban, Trạng thái duyệt, Lý do, Ngày thực hiện.

### 2. Tác vụ pending của tôi (Dành cho Maker)
- **Quy tắc hiển thị hành động theo trạng thái:**
  - **Xem:** Hiển thị ở **tất cả** các trạng thái của bản ghi.
  - **Chỉnh sửa:** Chỉ hiển thị khi Trạng thái = **Từ chối duyệt** VÀ Tác vụ là (Thêm mới / Chỉnh sửa / Chuyển đổi code phí).
  - **Xóa:** Hiển thị khi Trạng thái = **Chờ duyệt** hoặc **Từ chối duyệt**.
- **Ghi chú (Lý do từ chối):** Lưới sẽ hiển thị lý do từ chối gần nhất của bản ghi khi trạng thái = Từ chối duyệt.
- Lịch sử phê duyệt hiển thị tương tự như màn hình của Checker.

### 3. Nguyên tắc sinh Mã (Nếu có)
- Mã **chỉ được sinh chính thức** sau khi cấp duyệt cuối cùng (Checker) phê duyệt thành công.
- Ở bước Maker (trạng thái Chờ duyệt), Mã = trống/N/A.

### Mẫu Expected Result cho luồng Phê duyệt:

 - **Dành cho luồng Thêm mới :**
    ```
    --- TRƯỚC KHI DUYỆT (MAKER) ---
    (i) Nghiệp vụ/Logic: [Hệ thống ghi nhận lưu thành công. Bản ghi ở trạng thái 'Chờ duyệt', Mã chưa được sinh (đối với yêu cầu có sinh mã tự động).]
    (ii) UI: Toast 'Thêm mới thành công'. Bản ghi hiển thị tại màn hình Tác vụ Pending của tôi.

    --- SAU KHI LAST CHECKER DUYỆT ---
    (i) Nghiệp vụ/Logic: [Hệ thống lưu dữ liệu chính thức. Mã được sinh tự động theo quy tắc (đối với yêu cầu có sinh mã tự động). Bản ghi được cập nhật trạng thái là Đã duyệt.]
    (ii) UI: Toast 'Phê duyệt thành công'. Bản ghi hiển thị trên lưới chính thức với Mã đã sinh (đối với yêu cầu có sinh mã tự động).
    ```
  - **Dành cho luồng Chỉnh sửa (Mã không đổi):**
    ```
    --- TRƯỚC KHI DUYỆT (MAKER) ---
    (i) Nghiệp vụ/Logic: [Hệ thống ghi nhận lưu thành công. Bản ghi nháp ở trạng thái 'Chờ duyệt', Mã giữ nguyên không đổi.]
    (ii) UI: Toast 'Chỉnh sửa thành công'. Bản ghi hiển thị tại màn hình Tác vụ Pending của tôi.

    --- SAU KHI LAST CHECKER DUYỆT ---
    (i) Nghiệp vụ/Logic: [Hệ thống cập nhật dữ liệu chính thức. Mã giữ nguyên không đổi. Bản ghi đổi trạng thái thành Đã duyệt.]
    (ii) UI: Toast 'Phê duyệt thành công'. Bản ghi hiển thị thông tin mới cập nhật trên lưới chính thức.
    ```

---

## QTC-13 · Nguyên Tắc Sử Dụng Skill Này

> **AI BẮT BUỘC áp dụng khi phân tích bất kỳ US nào trong ProfiX:**

1. **Tra cứu trước khi hỏi:** Trước khi đặt câu hỏi Q&A cho BA về bất kỳ hành vi nào, kiểm tra xem QTC-01 đến QTC-12 đã trả lời chưa.
2. **Không hỏi lại câu hỏi đã có đáp án trong Quy tắc chung**, ví dụ:
   - ❌ "Tìm kiếm có phân biệt hoa thường không?" → ✅ Đã có: QTC-02, Không phân biệt.
   - ❌ "Tải xuống ra định dạng gì?" → ✅ Đã có: QTC-05, Excel `.xlsx`.
   - ❌ "Phân trang mặc định bao nhiêu dòng?" → ✅ Đã có: QTC-06, 50 bản ghi/trang.
   - ❌ "Upload file định dạng gì?" → ✅ Đã có: QTC-07, Excel.
   - ❌ "Lịch sử tác động gồm những cột nào?" → ✅ Đã có: QTC-08 (Thêm cả Người phê duyệt).
   - ❌ "Tra cứu CIF hoạt động thế nào?" → ✅ Đã có: QTC-09.
   - ❌ "Expected Result lỗi validation viết như thế nào?" → ✅ Đã có: QTC-11, ưu tiên mô tả hành vi FE.
   - ❌ "Checker thấy những hành động gì khi chưa được phân quyền?" → ✅ Đã có: QTC-12, Chỉ thấy nút Xem.
3. **Chỉ hỏi BA các điểm thực sự thiếu** hoặc US hiện tại có quy tắc riêng mâu thuẫn/ghi đè Quy tắc chung.
4. **Trong báo cáo phân tích**, khi nhắc đến Quy tắc chung, ghi rõ tham chiếu **[QTC-XX]** để tăng traceability.
