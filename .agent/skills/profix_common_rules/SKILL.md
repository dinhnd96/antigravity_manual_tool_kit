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

## Giải Thích Thuật Ngữ

| STT | Ký hiệu / Từ viết tắt | Giải thích |
|-----|------------------------|------------|
| 1 | ◎ | Trường ở dạng disable, không cho phép nhập/sửa |
| 2 | ★ | Trường bắt buộc phải nhập |
| 3 | – | Trường không bắt buộc nhập |
| 4 | KH | Khách hàng |
| 5 | KHCN | Khách hàng cá nhân |
| 6 | KHTC | Khách hàng doanh nghiệp lớn và Khách hàng doanh nghiệp vừa và nhỏ (= KHDNL + KHDN) |
| 7 | KHDNL | Khách hàng doanh nghiệp lớn |
| 8 | KHDN | Khách hàng doanh nghiệp vừa và nhỏ |
| 9 | DNSN | Khách hàng doanh nghiệp siêu nhỏ |
| 10 | CBNV | Cán bộ nhân viên |
| 11 | SPDV | Sản phẩm dịch vụ |
| 12 | CTƯĐ | Chương trình ưu đãi |
| 13 | MTD | Month to date |

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

### QTC-01.7 · Hiển Thị Dữ Liệu Rỗng (Empty Data) Trên Lưới
- Mặc định trên tất cả các lưới danh sách/báo cáo, nếu một trường dữ liệu (ví dụ: Mã CTƯĐ, Tên CTƯĐ...) không có giá trị, hệ thống sẽ hiển thị **trống (blank)**.
- **Không** hiển thị các ký tự thay thế như dấu gạch ngang (`-`), `N/A`, `Null`... trừ khi có quy định khác trong tài liệu yêu cầu.

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

- Luôn cho phép tải xuống dù có dữ liệu hay không có dữ liệu
- Tải xuống dữ liệu **theo điều kiện tìm kiếm đang áp dụng** (không phải toàn bộ DB).
- **Định dạng mặc định:** Excel (`.xlsx`) hoặc PDF (nếu US có yêu cầu xuất PDF).
- **Tên file:** `{Tên chức năng} - {yyyymmddhhmmss}`
  - Ví dụ: `Quản lý Chương trình ưu đãi - 20260421101500.xlsx` hoặc `.pdf`
- **Template (áp dụng chung cho cả Excel và PDF):** Trên màn hình (lưới danh sách) có các field nào thì file xuất ra sẽ hiển thị các field đó kèm dữ liệu tương ứng. Không cần yêu cầu BA đính kèm file template mẫu nếu chỉ là xuất danh sách cơ bản.
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

## QTC-10 · Nguyên Tắc Phân Quyền Dữ Liệu Tra Cứu/Tìm Kiếm (Data Authorization by Block)

> **Nguồn:** Tài liệu "Nguyên tắc phân quyền dữ liệu tra cứu.docx" — áp dụng cho toàn bộ chức năng tra cứu/tìm kiếm/xem.

Áp dụng cho các chức năng (Tìm kiếm nhanh, Lọc nâng cao, Tra cứu, Xem): Danh mục SPDV & Code phí, Danh mục Biểu phí, Chương trình ưu đãi, Xem nghiệp vụ theo cây thư mục, Xem code phí theo KH, Xem lịch sử thu phí theo KH, Xem lịch thu phí dự kiến theo KH, Xem CTƯĐ theo KH, Tác vụ chờ duyệt, Các chức năng truy xuất báo cáo.

### Logic phân quyền theo Khối (Block):

**Màn hình không có trường lọc "Khối":**
- Hệ thống tự động xác định Khối từ thông tin người dùng.

**Màn hình có trường lọc "Khối":**
- User thuộc **Khối KHCN, KHDN hoặc KHDNL** → mặc định hiển thị Khối của user, **không cho sửa**.
- User **không thuộc** KHCN/KHDN/KHDNL → hiển thị dropdown chọn Khối tự do.

### Ma trận dữ liệu theo Khối:

| Loại dữ liệu | Khối KHCN | Khối KHDN (DN vừa & nhỏ) | Khối KHDNL (DN lớn) | Các khối khác |
|---|---|---|---|---|
| SPDV & Code phí | SPDV: Tất cả. Code phí: Loại KH = KHCN/DNSN/CBNV **hoặc** Đối tượng tính phí = Merchant | SPDV: Tất cả. Code phí: Loại KH = KHTC **và** Đối tượng tính phí = Khách hàng | SPDV: Tất cả. Code phí: Loại KH = KHTC **và** Đối tượng tính phí = Khách hàng | Tất cả |
| Biểu phí | Biểu phí có Code phí Loại KH = KHCN/DNSN/CBNV **hoặc** Đối tượng tính phí = Merchant | Biểu phí có Code phí Loại KH = KHTC **và** Đối tượng tính phí = Khách hàng | Biểu phí có Code phí Loại KH = KHTC **và** Đối tượng tính phí = Khách hàng | Tất cả |
| Chương trình ưu đãi | CTƯĐ có Loại KH = KHCN/DNSN/CBNV | CTƯĐ có **Khối = KHDN** | CTƯĐ có **Khối = KHDNL** | Tất cả |
| Lịch sử/Lịch thu phí dự kiến | Khách hàng là KHCN/DNSN | Khách hàng là KHTC | Khách hàng là KHTC | Tất cả |

> **Lưu ý thay đổi quan trọng so với phiên bản cũ:**
> 1. **Tách Khối KHDN thành 2**: Khối KHDN (doanh nghiệp vừa & nhỏ) và Khối KHDNL (doanh nghiệp lớn).
> 2. **Bổ sung điều kiện "Đối tượng tính phí"**: Khối KHCN thấy Code phí có Đối tượng tính phí = Merchant; Khối KHDN/KHDNL chỉ thấy Code phí có Đối tượng tính phí = Khách hàng.
> 3. **CTƯĐ**: Khối KHDN/KHDNL lọc theo **Khối** (không phải Loại KH), Khối KHCN vẫn lọc theo Loại KH.

### Lưu ý quan trọng — Dropdown "Loại khách hàng" KHÔNG lọc theo Khối:

> **BA xác nhận:** Trường dropdown "Loại khách hàng" (KHCN / KHTC / DNSN / CBNV) trên các màn hình tra cứu, khai báo **KHÔNG bị lọc/ẩn** dựa theo Khối của user đăng nhập.
>
> **Lý do:** 1 merchant thuộc Loại KH = KHTC vẫn có thể được Khối KHCN nhìn thấy và xử lý. Phân quyền Khối chỉ áp dụng ở tầng **dữ liệu hiển thị trên lưới kết quả** (theo Ma trận dữ liệu ở trên), **không áp dụng lên dropdown filter**.

**Quy tắc cho AI khi sinh Test Case:**
- ❌ KHÔNG sinh TC kiểm tra "User Khối KHCN → dropdown Loại KH chỉ hiển thị KHCN/DNSN/CBNV" — đây là case SAI.
- ✅ Dropdown "Loại khách hàng" luôn hiển thị ĐẦY ĐỦ tất cả giá trị (KHCN, KHTC, DNSN, CBNV) bất kể Khối của user.
- ✅ Phân quyền Khối chỉ lọc **dữ liệu trả về trên lưới**, không lọc giá trị dropdown.
- ✅ Khi test SPDV & Code phí hoặc Biểu phí, phải kiểm tra thêm điều kiện **Đối tượng tính phí** (Merchant vs Khách hàng) ngoài Loại KH.

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

## QTC-14 · Quy Tắc Nghiệp Vụ Bổ Sung (BA Đã Xác Nhận)

> **Các quy tắc dưới đây đã được BA xác nhận chính thức. AI KHÔNG được hỏi lại các vấn đề này.**

### QTC-14.1 · Xử Lý Khi Không Có Thay Đổi (No-Change Guard)
- **FE:** Nếu người dùng nhấn "Xác nhận" / "Lưu" mà **không có bất kỳ thay đổi nào** so với dữ liệu hiện tại → FE **disable nút Xác nhận** hoặc hiển thị cảnh báo `"Không có thay đổi để lưu"`. Không gửi request lên BE.
- **BE:** Không tạo bản ghi **Chờ duyệt** nếu không có thay đổi thực tế (dirty check).
- **Áp dụng:** Toàn bộ chức năng có luồng Chỉnh sửa → Chờ duyệt.

### QTC-14.2 · Tên Nghiệp Vụ Không Yêu Cầu Unique
- Tên Nghiệp vụ **không cần unique** trên toàn hệ thống.
- Hệ thống phân biệt bản ghi bằng **Mã (Code)** tự động sinh, không bằng Tên.

### QTC-14.3 · Tên SPDV Không Yêu Cầu Unique Trong Cùng Cấp Cha
- Tên SPDV **không cần unique** trong cùng cấp cha (siblings).
- Hệ thống phân biệt các SPDV bằng **Mã SPDV** tự động sinh, không bằng Tên.

### QTC-14.4 · Không Hỗ Trợ Chỉnh Sửa Tên Và Mô Tả Sau Khi Duyệt
- Hệ thống **không cần bổ sung** cho phép chỉnh sửa Tên và Mô tả sau khi đã duyệt.
- **Không cung cấp** cơ chế đặc biệt (superadmin) để sửa lỗi chính tả đối với Tên/Mô tả đã duyệt.
- Nếu cần sửa → phải thực hiện qua luồng **Chỉnh sửa → Chờ duyệt** tiêu chuẩn.

### QTC-14.5 · Thiếu Nhánh Validate FE Khi Tra Cứu Trong Flowchart
- Trong các luồng Tra cứu, nếu Flowchart đi thẳng từ bước người dùng nhấn "Tra cứu" sang bước FE gửi yêu cầu cho BE mà **KHÔNG vẽ nhánh/bước validate FE** cho các lỗi cơ bản như:
  - Thiếu trường bắt buộc (VD: Từ ngày, Đến ngày).
  - Logic thời gian sai (VD: Từ ngày > Đến ngày).
  - Dữ liệu nhập không hợp lệ (VD: CIF không hợp lệ).
- **Quy định:** Mặc định FE sẽ tự validate các điều kiện này và hiển thị lỗi tương ứng trước khi gọi BE. Việc thiếu nhánh trên Flowchart chỉ là do giản lược biểu đồ.
- **AI KHÔNG ĐƯỢC HỎI LẠI** về trường hợp thiếu nhánh validate FE trong Flowchart cho các trường hợp này.

### QTC-14.6 · Thiếu Nhánh Lặp (Loop) Tra Cứu Trong Flowchart
- Trong các luồng Tra cứu, nếu Flowchart kết thúc (End) ngay sau khi hiển thị danh sách kết quả mà **KHÔNG vẽ nhánh quay lại (loop)** cho phép người dùng thay đổi điều kiện và tra cứu tiếp.
- **Quy định:** Mặc định người dùng luôn có thể nhấn "Tra cứu" hoặc "Xóa tra cứu" nhiều lần liên tiếp ngay trên màn hình. Chi tiết này đã được quy định ở QTC-04 và trong mô tả chi tiết các trường. Flowchart kết thúc ở End chỉ là để thể hiện xong một chu trình (1 request).
- **AI KHÔNG ĐƯỢC HỎI LẠI** BA/QA về việc bổ sung nhánh lặp (loop) từ cuối Flowchart quay lại bước nhập điều kiện/lựa chọn.

   - ❌ "Trường hợp không có dữ liệu, hệ thống hiển thị rỗng (blank) hay dấu '-' trên lưới?" → ✅ Đã có: QTC-01.7, Hiển thị rỗng (blank).
   - ❌ "Nếu Kafka down/unavailable, retry bao nhiêu lần? Rollback trạng thái không?" → ✅ Đã có: QTC-16, Giải pháp BE, không hỏi BA.
   - ❌ "ProfiX không nhận được kết quả từ Topic sau timeout, có cơ chế monitoring không?" → ✅ Đã có: QTC-16, Giải pháp BE, không hỏi BA.
   - ❌ "API xác thực bằng cơ chế gì? Rate limit bao nhiêu?" → ✅ Đã có: QTC-16, Giải pháp BE, không hỏi BA.
3. **Chỉ hỏi BA các điểm thực sự thiếu** hoặc US hiện tại có quy tắc riêng mâu thuẫn/ghi đè Quy tắc chung.
4. **Trong báo cáo phân tích**, khi nhắc đến Quy tắc chung, ghi rõ tham chiếu **[QTC-XX]** để tăng traceability.
   - ❌ "Nhấn 'Đóng' có hiện popup xác nhận không?" → ✅ Đã có: QTC-15, Không hiện popup, không lưu, quay về màn hình trước.


---

## QTC-15 · Hành Vi Nút "Đóng" (Close Button Behavior)

> **Áp dụng cho toàn bộ các màn hình có nút "Đóng" (Close / X) trong hệ thống ProfiX.**

- Khi người dùng nhấn nút **"Đóng"**:
  1. Hệ thống **KHÔNG hiển thị popup xác nhận** (không hỏi "Bạn có chắc muốn đóng?").
  2. Dữ liệu đang nhập/chỉnh sửa trên form **KHÔNG được lưu** (discard changes).
  3. Hệ thống **điều hướng người dùng về màn hình trước đó** (previous screen / parent screen).

- **Lưu ý:** Quy tắc này áp dụng mặc định. Nếu US cụ thể yêu cầu hành vi khác (ví dụ: hiện popup cảnh báo mất dữ liệu), tài liệu US đó phải ghi rõ override.

---

## QTC-16 · Giải Pháp Kỹ Thuật BE/Infra (Không Thuộc Phạm Vi URD/FSD)

> **Các câu hỏi về giải pháp kỹ thuật của Backend/Infrastructure KHÔNG thuộc phạm vi tài liệu nghiệp vụ. AI KHÔNG ĐƯỢC hỏi BA các câu dạng này.**

### Nguyên tắc

- **Tài liệu URD/FSD** chỉ mô tả **nghiệp vụ** (business logic, luồng xử lý, trạng thái, quy tắc).
- **Giải pháp kỹ thuật** (retry, timeout, rate limit, authentication, circuit breaker, message queue config...) là trách nhiệm của **team BE/DevOps** và được mô tả trong tài liệu kỹ thuật riêng (ISD, Technical Spec).
- BA sẽ **luôn bác bỏ** các câu hỏi dạng này với phản hồi: *"Đây là giải pháp của BE, sẽ trao đổi với BE và cập nhật lại sau"* hoặc *"Không mô tả trong tài liệu này"*.

### Danh sách câu hỏi CẤM hỏi BA (ví dụ thực tế)

| ❌ CẤM hỏi BA | Lý do | Hành động đúng |
|---|---|---|
| "Nếu Kafka down, retry bao nhiêu lần?" | Giải pháp BE | Ghi note: *[QTC-16] Giải pháp BE, QC tham chiếu ISD* |
| "Timeout chờ kết quả từ Topic là bao lâu?" | Giải pháp BE | Ghi note: *[QTC-16]* |
| "API xác thực bằng OAuth hay JWT?" | Giải pháp BE | Ghi note: *[QTC-16] QC tham chiếu ISD* |
| "API có rate limit không? Bao nhiêu request/s?" | Giải pháp BE | Ghi note: *[QTC-16]* |
| "Message queue dùng at-least-once hay exactly-once?" | Giải pháp Infra | Ghi note: *[QTC-16]* |
| "Circuit breaker khi service downstream unavailable?" | Giải pháp BE | Ghi note: *[QTC-16]* |
| "Database transaction isolation level?" | Giải pháp BE | Ghi note: *[QTC-16]* |
| "Cơ chế idempotent chống duplicate request?" | Giải pháp BE | Ghi note nếu BA đã trả lời nghiệp vụ (VD: "báo lỗi trạng thái không hợp lệ") → sinh TC từ câu trả lời nghiệp vụ, KHÔNG hỏi thêm kỹ thuật |

### Quy tắc xử lý

1. **Khi phân tích (Part B):** Nếu phát hiện gap liên quan kỹ thuật → **KHÔNG đưa vào danh sách Q&A cho BA**. Thay vào đó ghi nhận nội bộ: *"[QTC-16] Giải pháp BE — QC chủ động tham chiếu ISD khi có"*.
2. **Khi sinh TC (Part C/TC):** Nếu SC liên quan kỹ thuật thuần túy → **KHÔNG sinh TC**. Nếu BA đã phản hồi phần nghiệp vụ (VD: "request duplicate → báo lỗi trạng thái") → sinh TC từ phần nghiệp vụ đó.
3. **Phân biệt ranh giới:**
   - ✅ **Hỏi BA:** "Khi request xóa nợ trùng, hệ thống phản hồi gì?" → Đây là hành vi nghiệp vụ.
   - ❌ **KHÔNG hỏi BA:** "API xóa nợ có idempotent key không?" → Đây là giải pháp kỹ thuật.

