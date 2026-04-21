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

- Người dùng nhấn "Lọc nâng cao" → hệ thống hiển thị màn hình Lọc nâng cao (thường là Popup/Drawer).
- Nếu chưa nhập trường bắt buộc → thông báo `"Trường này bắt buộc"` hiển thị ngay dưới trường thiếu.
- Nếu dữ liệu hợp lệ → nhấn "Áp dụng" → hệ thống trả kết quả thoả mãn **đồng thời** các điều kiện (AND).
- Nếu để trống tất cả điều kiện → nhấn "Áp dụng" → hệ thống hiển thị **toàn bộ dữ liệu**.
- Nhấn "Xóa lọc" → reset tất cả trường về trống → **đóng popup** → lưới trở về trạng thái mặc định.
- Quy tắc tìm kiếm: **giống QTC-02** (AND, case-insensitive, bỏ dấu, auto-trim, rỗng bỏ qua).

---

## QTC-04 · Tra Cứu (Search with Explicit Button)

- Người dùng nhập điều kiện → nhấn nút "Tra cứu" → hệ thống tìm kiếm.
- Nhấn "Xóa tra cứu" → hệ thống clear điều kiện → **danh sách trở về mặc định** (không hiển thị kết quả nếu không nhập điều kiện theo từng chức năng cụ thể).
- Nếu không nhập điều kiện → hệ thống **mặc định không hiển thị danh sách** (kết quả rỗng, chờ user nhập điều kiện).

---

## QTC-05 · Tải Xuống (Export / Download)

- Nút "Tải xuống" hiển thị khi màn hình **có lưới dữ liệu**.
- Tải xuống dữ liệu **theo điều kiện tìm kiếm đang áp dụng** (không phải toàn bộ DB).
- **Định dạng mặc định:** Excel (`.xlsx`). Nếu US cụ thể dùng định dạng khác → sẽ ghi rõ trong tài liệu US đó.
- **Tên file:** `{Tên chức năng} - {yyyymmddhhmmss}`
  - Ví dụ: `Quản lý Chương trình ưu đãi - 20260421101500.xlsx`
- **Template:** được đính kèm tại mục Tải xuống của từng chức năng cụ thể.
- ⚠️ Không có giới hạn số dòng được ghi rõ trong Quy tắc chung → **cần hỏi BA** nếu chức năng có dữ liệu lớn.

---

## QTC-06 · Phân Trang (Pagination)

- Mặc định hiển thị **50 bản ghi / trang**.
- Nếu chức năng cụ thể dùng số bản ghi khác → sẽ ghi rõ trong tài liệu US đó.
- Các nút điều hướng:
  - **Số trang:** nhấn để nhảy đến trang đó.
  - **Trang tiếp theo:** disabled nếu đang ở trang cuối.
  - **Trang trước đó:** disabled nếu đang ở trang đầu.
- ⚠️ Thứ tự sắp xếp mặc định (sort mặc định của lưới) **không được định nghĩa** trong Quy tắc chung → **cần hỏi BA** hoặc tham chiếu mục Lưới của US cụ thể.

---

## QTC-07 · Upload File

- Định dạng được phép upload: **Excel** (`.xlsx`).
- Dung lượng tối đa: **theo tham số hệ thống** (không có con số cứng trong Quy tắc chung).
- Validate sau khi upload:
  - Định dạng/dung lượng không hợp lệ → toast `"Định dạng hoặc dung lượng không hợp lệ"` → user chọn lại.
  - Dữ liệu hợp lệ → hiển thị danh sách bản ghi thành công.
  - Dữ liệu không hợp lệ → toast `"Dữ liệu của bạn không hợp lệ"` → **highlight** dòng lỗi.
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

---

## QTC-09 · Nguyên Tắc Phân Quyền Dữ Liệu (Data Authorization by Block)

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

---

## QTC-10 · Bảng Mã Lỗi Hệ Thống (System Error Codes)

| Mã chức năng | Mã lỗi | Nội dung |
|---|---|---|
| PR.01 | PR.01.01 | Chưa nhập đủ các trường bắt buộc |
| PR.01 | PR.01.02 | Khai báo cấp Nghiệp vụ thành công |
| PR.01 | PR.01.03 | Chưa thay đổi Ngày hiệu lực/Ngày hết hiệu lực |
| PR.01 | PR.01.04 | Sửa cấp Nghiệp vụ thành công |
| PR.01 | PR.01.05 | Khai báo SPDV chi tiết thành công |
| PR.01 | PR.01.06 | Sửa cấp SPDV chi tiết thành công |
| PR.02 | PR.02.01 | Dữ liệu Code phí chưa hợp lệ |
| PR.02 | PR.02.02 | Khai báo Code phí thành công |
| PR.11 | PR.11.01 | Dữ liệu Khai báo Chương trình ưu đãi chưa hợp lệ |
| PR.11 | PR.11.02 | Khai báo Chương trình ưu đãi thành công |

---

## QTC-11 · Nguyên Tắc Sử Dụng Skill Này

> **AI BẮT BUỘC áp dụng khi phân tích bất kỳ US nào trong ProfiX:**

1. **Tra cứu trước khi hỏi:** Trước khi đặt câu hỏi Q&A cho BA về bất kỳ hành vi nào, kiểm tra xem QTC-01 đến QTC-10 đã trả lời chưa.
2. **Không hỏi lại câu hỏi đã có đáp án trong Quy tắc chung**, ví dụ:
   - ❌ "Tìm kiếm có phân biệt hoa thường không?" → ✅ Đã có: QTC-02, Không phân biệt.
   - ❌ "Tải xuống ra định dạng gì?" → ✅ Đã có: QTC-05, Excel `.xlsx`.
   - ❌ "Phân trang mặc định bao nhiêu dòng?" → ✅ Đã có: QTC-06, 50 bản ghi/trang.
   - ❌ "Upload file định dạng gì?" → ✅ Đã có: QTC-07, Excel.
   - ❌ "Lịch sử tác động gồm những cột nào?" → ✅ Đã có: QTC-08.
3. **Chỉ hỏi BA các điểm thực sự thiếu** hoặc US hiện tại có quy tắc riêng mâu thuẫn/ghi đè Quy tắc chung.
4. **Trong báo cáo phân tích**, khi nhắc đến Quy tắc chung, ghi rõ tham chiếu **[QTC-XX]** để tăng traceability.
