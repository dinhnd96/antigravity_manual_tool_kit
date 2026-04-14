---
name: ProfiX Domain Expert
description: Kỹ năng chuyên gia đọc hiểu nghiệp vụ (Domain Expert) cho dự án ProfiX Phase 1 - Hệ thống quản lý phí tập trung. Dùng kỹ năng này để trả lời các câu hỏi về Business Rule, Entity Relationship, và Workflow trong tài liệu URD/FSD.
sources:
  - "TỔNG QUAN - P1.docx (US01, US02, US06)"
  - "US15 - P2.docx (US15, US16, US17, US18, US19, US20, US21)"
  - "US23 - P3.docx (US23, US27, Quy tắc chung)"
  - "Cập nhật lần cuối: 2026-04-09"
---

# PROFIX DOMAIN EXPERT - BỘ KIẾN THỨC NGHIỆP VỤ

> **Nguồn dữ liệu:** P1 (US01, US02, US05, US15 tree) | P2 (US15-21) | P3 (US23, 27, Quy tắc chung)
> **Trạng thái:** ✅ P1, P2, P3 đã tích hợp đầy đủ | ⏳ P4 chưa tích hợp

---

# I. DANH SÁCH USER STORY (US) - TỔNG QUAN

| ID | Mô tả |
|----|-------|
| US01 | Khai báo SPDV theo mô hình cây phân cấp |
| US02 | Khai báo 1 code phí với thông tin chi tiết về mức phí và điều kiện áp dụng |
| US03 | Khai báo code phí bằng nhân bản |
| US04 | Tự động sinh mã code phí theo nguyên tắc |
| US05 | Định nghĩa công thức tính phí cho code phí |
| US06 | Khai báo 1 biểu phí (bao gồm thiết lập công thức tính phí) |
| US07 | Khai báo biểu phí bằng upload file Excel/CSV |
| US08 | Sao chép 1 biểu phí |
| US09 | Chuyển đổi code phí giữa các biểu phí |
| US10 | Khai báo chương trình ưu đãi theo nhiều tiêu chí |
| US11 | Khai báo CTƯĐ cho danh sách khách hàng xác định |
| US12 | Khai báo CTƯĐ theo từng code phí/biểu phí |
| US13 | Tự động sinh mã CTƯĐ theo nguyên tắc |
| US14 | Xem toàn bộ danh mục SPDV & lịch sử khai báo |
| US15 | Xem danh sách và lịch sử thay đổi Biểu phí |
| US16 | Xem danh sách Chương trình ưu đãi & lịch sử khai báo |
| US17 | Xem danh sách code phí áp dụng cho một khách hàng |
| US18 | Xem lịch sử thu phí theo khách hàng |
| US19 | Tra cứu lịch thu phí dự kiến theo khách hàng |
| US20 | Xem danh sách CTƯĐ theo khách hàng |
| US21 | Đăng nhập vào hệ thống |
| US22 | Đăng xuất khỏi hệ thống |
| US23 | Thay đổi nhóm quyền của một user (Admin) |
| US24 | Khai báo nhóm quyền trên hệ thống (Admin) |
| US25 | Cấu hình ma trận phê duyệt cho tác vụ khai báo tham số phí |
| US26 | Thiết lập quy tắc của 1 điều kiện tính phí |
| US27 | Thiết lập quy tắc xác định nhóm khách hàng theo từng thời kỳ |
| US28 | Xuất sao kê chi tiết giao dịch thu phí |
| US29 | Xuất báo cáo danh sách KH còn nợ phí |
| US30 | Xuất báo cáo dự thu phí dịch vụ kỳ tiếp theo |
| US31 | Xuất báo cáo tổng doanh thu phí |
| US32 | Xem trang báo cáo tổng quan hoạt động thu phí |
| US33 | Tính phí kênh online (hệ thống tự động) |
| US34 | Tính phí kênh quầy/nội bộ |
| US35 | Tự động thu phí định kỳ theo lịch |
| US36 | Tự động truy thu và tận thu phí định kỳ còn nợ |
| US37 | Khởi tạo CTƯĐ từ kết quả phê duyệt ngoại lệ trên hệ thống phê duyệt miễn/giảm phí |

---

# II. CÁC THỰC THỂ CỐT LÕI VÀ MỐI QUAN HỆ

## 1. Sản Phẩm Dịch Vụ (SPDV) - Chi tiết US01
*(Navigation: Tham số >> Danh mục sản phẩm dịch vụ)*

### 1.1 Khai báo Nghiệp vụ (SPDV Cấp 1)
* **Cấu trúc:** Phân cấp dạng cây. SPDV cấp 1 (lớn nhất) gọi là **Nghiệp vụ**. Cấp cuối cùng (cấp n) là nơi được gắn các **Code phí**.
* **Tham số:** Số cấp tối đa `n` được thiết lập tại tham số `PRODUCT_LEVEL`.
* **Mã Nghiệp vụ:** Tự động sinh, số tự tăng 2 chữ số từ 01-99. Trường hợp > 99 → Hệ thống báo lỗi, không cho lưu.
* **Các trường thông tin:** Mã nghiệp vụ (auto), Tên Nghiệp vụ (★), Mô tả (★), Ngày hiệu lực (★), Ngày hết hiệu lực (★).
* **Quy tắc ngày:** Ngày hiệu lực, Ngày hết hiệu lực đều phải >= Ngày hệ thống. Ngày hết hiệu lực >= Ngày hiệu lực.
* **Khi sửa:** Chỉ được sửa Ngày hiệu lực và Ngày hết hiệu lực. Ngày hiệu lực phải <= Ngày hiệu lực các SPDV chi tiết con. Ngày hết hiệu lực phải >= Ngày hết hiệu lực của các SPDV chi tiết con.
* **Trạng thái:** Hoạt động | Không hoạt động.
* **Tự động cập nhật trạng thái (đầu ngày):**
  * T = Ngày hiệu lực + trạng thái = Không hoạt động → Cập nhật thành Hoạt động.
  * T > Ngày hết hiệu lực + trạng thái = Hoạt động → Cập nhật thành Không hoạt động.

### 1.2 Khai báo SPDV Chi tiết (Cấp 2 trở xuống)
*(Navigation: Tham số >> Danh mục sản phẩm dịch vụ và Code phí >> Thêm mới SPDV)*
* **Mã SPDV chi tiết:** = Mã SPDV cấp cha liền trước + 02 ký tự số tự tăng từ 01-99.
  * Ví dụ: Nghiệp vụ "Tài khoản" mã 06 → SPDV "Tài khoản thanh toán" = 0601.
* **Quy tắc ngày hiệu lực (ràng buộc với cha):**
  * Ngày hiệu lực cha <= Ngày hiệu lực SPDV con <= Ngày hiệu lực các SPDV cấp con bên dưới.
  * Ngày hết hiệu lực cha >= Ngày hết hiệu lực SPDV con >= Ngày hết hiệu lực các SPDV cấp con bên dưới.
* **SPDV cấp cuối:** Hiển thị label "Đây là cấp cuối cùng trong cây sơ đồ sản phẩm dịch vụ".
* **Luồng Maker-Checker:** Tương tự như Nghiệp vụ.

---

## 2. Code Phí - Chi tiết US02 & US05
*(Navigation: Tham số >> Danh mục SPDV >> SPDV cấp cuối >> Thêm mới Code phí >> Thiết lập Quy tắc tính phí)*

### 2.1 Thông tin chung Code phí
| Trường | Bắt buộc | Ghi chú |
|--------|----------|---------|
| Mã phí | ◎ (auto) | Hệ thống tự sinh, không được thay đổi. Xem US04. |
| Tên phí | ★ | Nhập text |
| Loại tiền tệ | ★ | Dropdown - Loại tiền tệ chính của Code phí |
| VAT | — | Số nguyên dương > 0 và < 100. Bỏ trống nếu không chịu VAT. |
| Phí đã bao gồm VAT | — | Checkbox. Nếu tick → VAT bắt buộc nhập. |
| Đối tượng thu phí | ★ | RadioButton: **Khách hàng** hoặc **Merchant** |
| Loại Khách hàng | ★ | Dropdown: KHCN / KHTC / DNSN / CBNV (CBNV ẩn khi Merchant) |
| Khai báo theo phân khúc | — | Checkbox - Quy tắc tính phí áp dụng chung hay riêng theo nhóm KH |
| Loại tính phí | ★ | Dropdown: **Theo giao dịch** / **Định kỳ** |
| Loại tiền tối thiểu/tối đa | — | Có thể khác loại tiền của Code phí |
| Tần suất | — | Chỉ hiện khi Loại tính phí = Định kỳ: Hàng năm / Hàng tháng |
| Ngày thu | — | Chỉ hiện khi Định kỳ. Nếu Hàng tháng: 1-31 (mặc định cuối tháng nếu tháng không đủ ngày). Nếu Hàng năm: DD/MM (tháng 2 tối đa 28). |
| Ngày thu theo dữ liệu | — | RadioButton, chọn thay cho Ngày thu cố định |
| Bảng dữ liệu | — | Chỉ hiện khi Định kỳ + Ngày thu theo dữ liệu. Chọn: ETL KH / ETL Tài khoản / ETL Thẻ |
| Trường dữ liệu | — | Combobox mapping trường lấy ngày thu |
| Mã hạch toán Category | — | Nhập text |
| Ghi chú | — | Nhập text |

### 2.2 Trạng thái Code phí
| Trạng thái | Mô tả |
|-----------|-------|
| Chờ gán (mặc định khi Thêm mới) | Code phí chưa được gán với Biểu phí nào |
| Hoạt động | Code phí đang gán với Biểu phí Đang hiệu lực/Chưa hiệu lực |
| Ngừng hoạt động | Tất cả Biểu phí mà Code trực thuộc đều Hết hiệu lực |
| Hủy | Code phí khai báo sai, không thể tái sử dụng (chỉ Maker sửa thành Hủy) |

### 2.3 Điều kiện tính phí (gắn vào Code phí)
| Loại | Nguồn dữ liệu | Hiển thị khi |
|------|--------------|-------------|
| Điều kiện theo Giao dịch | API | Loại tính phí = Theo giao dịch |
| Điều kiện theo Khách hàng | ETL - Bảng KH | Luôn hiển thị |
| Điều kiện theo Tài khoản | ETL - Bảng TK | Cả Theo giao dịch + Định kỳ |
| Điều kiện theo Thẻ | ETL - Bảng Thẻ | Loại tính phí = Định kỳ |

**Operator theo kiểu dữ liệu:**
| Kiểu | Operator được phép |
|------|--------------------|
| String | =, <>, IN, NOT IN |
| Number | =, <>, IN, NOT IN, >, >=, <, <= |
| Boolean | YES, NO |
| Date | =, >, >=, <, <= |
| DateTime | =, >, >=, <, <= |

**Lưu ý:** Tại mỗi phân vùng điều kiện tính phí, người dùng có thể thêm nhiều điều kiện. Các điều kiện không được trùng lặp.

### 2.4 Quy tắc tính phí (Công thức tính phí) - US05
* Mỗi Code phí có thể có 1 hoặc nhiều công thức khác nhau.
* **Không khai báo theo nhóm KH:** Chỉ 1 công thức, áp dụng chung.
* **Khai báo theo nhóm KH:** Nhiều công thức, mỗi công thức áp dụng riêng cho 1 nhóm KH. Việc khai báo Nhóm khách hàng thực hiện bằng cách thêm mới các mã CIF.
* Số tiền phí tính theo công thức có Loại tiền tệ = Loại tiền tệ của Code phí.
* Có thể khai báo Số tiền phí tối thiểu & tối đa với Loại tiền tệ riêng (khác Code phí).

**Ràng buộc Loại tiền tối thiểu/tối đa:**
* VND/JPY → chỉ nhập số nguyên dương.
* Loại tiền khác → được nhập số thập phân, tối đa 2 chữ số sau dấu thập phân.
* Nếu công thức là 1 giá trị số học cụ thể mà Loại tiền tệ Code phí khác Loại tiền tối thiểu/tối đa → Lỗi, không lưu.

**Nguyên tắc nhập Công thức:**
* **Hàm được phép:** 
  * `MONTHS_BETWEEN`: Tính số tháng giữa 2 ngày (có thể trả về số thập phân).
  * `DATE_DIFF`: Tính số ngày giữa 2 ngày (trả về số nguyên).
  * `ROUND`: Làm tròn toán học (>= 0.5 lên, < 0.5 xuống).
  * `ROUNDUP`, `ROUNDDOWN`: Luôn làm tròn lên / luôn làm tròn xuống.
  * `MIN`, `MAX`: Giá trị nhỏ nhất / lớn nhất.
* **Toán tử:** `+` (cộng), `-` (trừ), `x` (nhân), `:` (chia)
* **Ký tự:** `( ) . , # 0-9`
* **Biến:** Dùng định dạng `#TenBien#`, hệ thống gợi ý khi nhập sau dấu `#`. Trích xuất từ các trường do Core/API gửi về.
* **Giới hạn:** Tối đa 300 ký tự. Hệ thống tự chuyển sang CHỮ HOA.

**Validation Công thức (khi ấn "Xác nhận"):**
1. Nếu công thức có 2+ cấu phần mà có 2 cấu phần đều là giá trị số học cụ thể → Lỗi, không lưu.
2. Các hàm bắt buộc phải có `(` và `)`.
3. `MONTHS_BETWEEN`, `DATE_DIFF` phải có 2 tham số dạng ngày, phân cách bằng `,`, đặt trong `()`. Không được kết hợp 2 hàm này trong cùng 1 cấu phần.
4. `MIN/MAX` không được kết hợp với `MONTHS_BETWEEN/DATE_DIFF` trong cùng 1 cấu phần.

**Phê duyệt Công thức:** Thực hiện đồng thời với phê duyệt Code phí (Maker-Checker).
**Sửa sau phê duyệt:** Chỉ sửa được các giá trị số học. Không sửa hàm hoặc giá trị tính phí trực tiếp → Phải upload lại danh sách code phí tại biểu phí (US07).

---

# III. QUY TRÌNH THU PHÍ (WORKFLOWS - Tổng quan)

## 1. Thu phí theo giao dịch (Kênh Online & Quầy)
* Hệ thống nguồn (PVConnect, Teller...) gọi API `FeeCalculate` → ProfiX chạy rule tính toán → Trả ra số tiền thực thu (sau ưu đãi).
* Có hỗ trợ thu phí Adhoc: Maker chọn Code phí → ProfiX trả kết quả → Nhập input thủ công (nếu công thức cần Số lượng/Giá trị) → Tính phí → Hạch toán.

## 2. Thu phí định kỳ (Recurring)
Quét và thực hiện qua các nhóm Job cấu hình sẵn. Các luồng gồm:
* **Thu đúng hạn đầu ngày:** Quét kỳ thu phí đến hạn sinh số tiền thu → Gửi message qua Topic → Core T24 trừ tiền.
* **Truy thu/tận thu đầu ngày:** Quét CIF nợ phí mà TK T-1 có số dư > 0 → Sinh giao dịch tận thu.
* **Truy thu/tận thu khi phát sinh ghi có:** T24 báo có số dư mới → ProfiX check nợ phí và tiến hành trừ nợ ngay.
* *Ưu tiên thu nợ:* Sắp xếp theo nhóm Level Nghiệp vụ (độ khẩn) → Ngày đến hạn (từ xa đến gần).

---

# IV. VÒNG ĐỜI VÀ TRẠNG THÁI (STATE MACHINE)

## 1. Vòng đời dữ liệu (Hệ thống tự động quét mỗi đầu ngày)
* `Chưa có hiệu lực` → Đến ngày áp dụng → `Đang hiệu lực (Hoạt động)`.
* `Đang hiệu lực` → Quá ngày hết hiệu lực → `Hết hiệu lực (Ngừng hoạt động)`.

## 2. Vòng đời phê duyệt (Maker - Checker)
* Tác vụ sinh ra nằm tại Queue **"Tác vụ chờ duyệt"**.
* **Quy tắc độc quyền:** Tại 1 thời điểm, một bản ghi (ID) chỉ có **DUY NHẤT 1** yêu cầu nằm ở trạng thái Chờ duyệt (bất kể hành động Thêm/Sửa/Xóa).
* **Luồng trạng thái:** `Chờ duyệt` → (Checker) → `Đã duyệt` (Apply bản ghi thật) HOẶC `Từ chối duyệt`.
* Tác vụ bị `Từ chối duyệt`: Maker có thể Sửa/Xóa nó trong màn hình **"Tác vụ pending của tôi"**.
* **Chức năng Admin** (Quản lý User, Phân quyền): Không cần Maker-Checker.
* Phê duyệt theo nguyên tắc Ma trận phê duyệt mô tả tại US25.

---

# V. CÁC THỰC THỂ KHÁC (Tổng quan từ P1)

## 1. Biểu Phí (US06-US09)
* Lắp ghép một hoặc nhiều Code phí vào chung một Biểu phí (Thông qua Upload File DS Code phí).
* Code phí phải có trạng thái **Chờ gán** thì mới được đưa vào Biểu phí.
* Khi Biểu phí hiệu lực, các Code phí thuộc về nó → trạng thái **Hoạt động**.
* Cho phép sao chép/chuyển đổi Code phí giữa các Biểu phí.

## 2. Chương Trình Ưu Đãi - CTƯĐ (US10-US13)
* **Phân loại:** Ưu đãi cho **Toàn bộ Biểu phí** (tỷ lệ % cố định) hoặc **Từng Code phí riêng lẻ** (Miễn giảm định mức tiền / % cố định).
* **Chọn CTƯĐ tối ưu:** Nếu 1 KH thỏa mãn nhiều CTƯĐ → Hệ thống tự chọn CTƯĐ mang lại **phí thấp nhất (ưu đãi nhất)**.

## 3. Điều Kiện Tính Phí (US26)
* Tạo từ Data nguồn (API / Bảng dữ liệu KH/Tài khoản/Thẻ qua ETL).
* Mapping với kiểu dữ liệu: Number, String, Date, Time.
* Chỉ điều kiện trạng thái **"Hoạt động"** mới được hiển thị ở màn Code phí.

## 4. Nhóm Khách Hàng (US27)
* Quản lý tập hợp KH theo từng phân khúc.
* Dùng Operator `=` hoặc `IN` để gom nhóm.

---

# VI. CÁC ĐIỂM QUAN TRỌNG KHÁC (EDGE CASES & EXCEPTIONS)

## 1. VAT
* Không chịu VAT → Bỏ trống trường VAT.
* Chịu VAT + **KHÔNG tick** "Phí đã bao gồm VAT": Phí thực thu = Phí tính ra + (VAT% × Phí tính ra).
* Chịu VAT + **CÓ tick** "Phí đã bao gồm VAT": Phí thực thu = Phí tính ra (VAT đã gộp trong đó).

## 2. Ngoại tệ (Cross-currency)
* Tỷ giá chéo tính theo quy tắc USD làm đồng định giá cơ sở giữa 2 ngoại tệ mua/bán.
* Lấy tỷ giá tại thời điểm thực hiện giao dịch.

## 3. Bảo mật & Đăng nhập
* Sai mật khẩu 5 lần liên tiếp → Tài khoản bị Inactive.
* Inactive → Bắt buộc Admin vào Active lại (chức năng Admin không cần Maker-Checker).

## 4. Xóa nợ phí
* Không xóa trực tiếp ở ProfiX.
* Thực hiện trên hệ thống Pricing → Trình phê duyệt → Gọi API xuống ProfiX để xóa.

## 5. Luồng Khai báo Code phí (thứ tự bắt buộc)
Khi khai báo Code phí, người dùng **phải khai báo trước** các thông tin sau làm căn cứ xác định Điều kiện & Quy tắc tính phí:
1. Loại tiền tệ
2. Loại khách hàng
3. Loại tính phí
4. Loại tiền tối thiểu/tối đa

**Lưu ý thứ tự nhập tiền tệ:**
* Chọn Loại tiền tệ Code phí TRƯỚC → Loại tiền tối thiểu/tối đa **TỰ CẬP NHẬT** theo.
* Chọn Loại tiền tối thiểu/tối đa TRƯỚC → Chọn Loại tiền tệ Code phí SAU → Hệ thống **KHÔNG cập nhật** loại tiền tối thiểu/tối đa theo.

---

# VII. NAVIGATION MAP (Đường dẫn menu chính)

| Chức năng | Đường dẫn |
|-----------|----------|
| Khai báo Nghiệp vụ | Tham số >> Danh mục sản phẩm dịch vụ >> Thêm mới Nghiệp vụ |
| Khai báo SPDV chi tiết | Tham số >> Danh mục sản phẩm dịch vụ và Code phí >> Thêm mới SPDV |
| Khai báo Code phí | Tham số >> Danh mục SPDV >> SPDV cấp cuối >> Thêm mới Code phí |
| Thiết lập Quy tắc tính phí | Tham số >> Danh mục SPDV >> SPDV cấp cuối >> Thêm mới Code phí >> Quy tắc tính phí |
| Tác vụ pending của Maker | Màn hình "Tác vụ Pending của tôi" |
| Tác vụ chờ duyệt của Checker | Màn hình "Tác vụ chờ duyệt" |

---

*📝 Ghi chú: File này sẽ được cập nhật tiếp khi tích hợp P3, P4.*

---

# VIII. CÁC CHỨC NĂNG TRA CỨU - XEM DANH MỤC (US15-US21 từ P2)

## 1. US15 - Xem Danh Mục SPDV & Code Phí

### 1.1 Chức năng Quản lý Danh mục SPDV và Code phí (Tham số)
*(Navigation: Tham số >> Danh mục SPDV và code phí)*

**Tab 1: Danh mục sản phẩm dịch vụ** (Mặc định)
* **Tìm kiếm nhanh:** Nhập mã/tên → tìm kiếm gần đúng.
* **Lọc nâng cao:** Cấp khai báo | Tên | Từ ngày - Đến ngày (theo ngày hiệu lực).
* **Lưới kết quả:** Mã code phí, Loại, Mã SPDV, Tên SPDV, Trạng thái, Ngày tạo, Ngày hiệu lực, Ngày hết hiệu lực, Người tạo, Ngày duyệt, Người duyệt, Ngày sửa, Người sửa.
* **Xem chi tiết SPDV:** Click vào mã SPDV → Hiển thị: Tên, Mã SPDV, Mô tả, Cấp SPDV, Ngày tạo, Người tạo, Ngày duyệt, Người duyệt, Ngày sửa, Người sửa, Ngày hiệu lực, Ngày hết hiệu lực, Trạng thái, Code phí.
* **SPDV cấp cuối:** Hiển thị các code phí đang hiệu lực gắn với SPDV đó + nút Thêm code phí mới. Nút **Chuyển đổi code phí** hiển thị khi có ít nhất 1 code phí.
* **Trạng thái SPDV:**
  * `Hoạt động` — SPDV đang có hiệu lực.
  * `Không hoạt động` — SPDV chưa đến ngày hiệu lực hoặc đã hết hiệu lực.
* **Tải xuống:** Xuất file Excel danh sách SPDV theo kết quả tìm kiếm.

**Tab 2: Danh sách code phí chưa sử dụng**
* **Mục đích:** Hiển thị code phí chưa được gán vào Biểu phí.
* **Trạng thái code phí hiển thị:** Hủy | Ngừng hoạt động | Chờ gán.
* **Lọc nâng cao:** Tên | Từ ngày - Đến ngày (theo ngày **tạo**).
* **Lưới kết quả:** Code phí, Tên phí, Mã SPDV, Tên SPDV, Trạng thái, Ngày tạo, Người tạo, Ngày sửa, Người sửa.
* **Xem chi tiết code phí:** Hiển thị các trường như màn thêm mới/chỉnh sửa + popup **Lịch sử tác động**.

### 1.2 Chức năng Xem nghiệp vụ theo cây thư mục (Tra cứu)
*(Navigation: Tra cứu >> Xem nghiệp vụ theo cây thư mục)*

Màn hình gồm **2 cấu phần độc lập:**

**A. Danh mục toàn hàng (Cây thư mục SPDV):**
* Mặc định hiển thị toàn bộ SPDV cấp 1.
* Người dùng có thể Expand/Collapse đến cấp cuối.
* Phân trang: 20 SPDV cấp 1 / trang.
* Nhấn vào 1 SPDV:
  * Nếu **SPDV cấp cuối** → Hiển thị chi tiết + hyperlink **"Xem code phí đi kèm"**.
  * Nếu **không phải cấp cuối** → Hiển thị chi tiết + hyperlink **"Xem biểu phí đi kèm"**.
* Danh sách biểu phí: Mã biểu phí, Tên biểu phí, Tên văn bản, Ngày ban hành, Ngày hiệu lực, Ngày hết hiệu lực, Trạng thái, Người tạo, Ngày tạo, Người sửa, Ngày sửa, Người duyệt, Ngày duyệt.
* Danh sách code phí: Tải xuống, Mã code phí, Tên code phí, Công thức tính phí, Người tạo, Ngày tạo, Người sửa, Ngày sửa, Người duyệt, Ngày duyệt.

**B. Danh mục sản phẩm dịch vụ (Tab Tra cứu):**
* Mặc định **không hiển thị** danh sách khi vào tab (phải nhấn "Tra cứu" mới có kết quả).
* Điều kiện tra cứu: Cấp khai báo | Tên | Từ ngày – Đến ngày (theo ngày hiệu lực).
* Lưới: Mã SPDV, Tên SPDV, Loại (cấp SPDV), Mã Code phí, Trạng thái, Ngày tạo, Ngày hiệu lực, Ngày hết hiệu lực, Người tạo, Ngày duyệt, Người duyệt, Ngày sửa, Người sửa.

**C. Danh mục biểu phí (Tab Tra cứu):**
* Mặc định **không hiển thị** danh sách khi vào tab.
* Điều kiện tra cứu: Tên biểu phí | Số văn bản | Tên văn bản | Loại khách hàng (KHCN/KHTC/KHDNSN/CBNV) | Từ ngày – Đến ngày (theo ngày hiệu lực) | Trạng thái (Đang hiệu lực / Chưa hiệu lực / Hết hiệu lực).
* Lưới: Mã biểu phí, Tên biểu phí, Số văn bản, Tên văn bản, Trạng thái, Ngày hiệu lực, Ngày hết hiệu lực, Ngày tạo, Người tạo, Ngày duyệt, Người duyệt, Ngày sửa, Người sửa.

---

## 2. US16 - Xem Danh Mục Biểu Phí
*(Navigation: Tham số >> Quản lý Danh mục biểu phí)*

* **Trạng thái Biểu phí:**
  * `Đang hiệu lực` — Ngày hiệu lực đã bắt đầu, còn trong khoảng ngày hiệu lực → ngày hết hiệu lực.
  * `Chưa hiệu lực` — Ngày hiệu lực chưa bắt đầu.
  * `Hết hiệu lực` — Đã qua ngày hết hiệu lực.
* **Lọc nâng cao:** Tên biểu phí | Trạng thái | Từ ngày – Đến ngày (theo ngày hiệu lực).
* **Lưới danh sách:** Mã biểu phí, Tên biểu phí, Trạng thái, Ngày hiệu lực (dd/mm/yyyy), Ngày hết hiệu lực (dd/mm/yyyy hoặc "-"), Ngày tạo (hh:mm:ss – dd/mm/yyyy), Người tạo, Ngày sửa (hoặc "-"), Người sửa (hoặc "-"), Ngày duyệt (hoặc "-"), Người duyệt (hoặc "-").
* **Xem chi tiết biểu phí:** Hiển thị các trường như màn tạo/chỉnh sửa + popup **Lịch sử tác động**.
* Có nút **Thêm mới**, **Sao chép** và **Tải xuống** tại màn danh sách.

---

## 3. US17 - Xem Danh Sách Chương Trình Ưu Đãi (CTƯĐ)
*(Navigation: Tham số >> Chương trình ưu đãi >> Quản lý Chương trình ưu đãi)*

* **Mặc định:** Hiển thị **Ưu đãi có đánh giá định kỳ** khi vào màn hình.
* **Loại ưu đãi:** Ưu đãi có đánh giá định kỳ / Ưu đãi không đánh giá định kỳ (dropdown chọn).
* **Trạng thái CTƯĐ:** `Hoạt động` | `Tạm dừng`.
* **Lọc nâng cao:** Mã CTƯĐ | Tên CTƯĐ | Trạng thái | Ngày hiệu lực | Ngày hết hiệu lực | Loại ưu đãi (Ưu đãi theo biểu phí / Ưu đãi theo code phí).
* **Lưới danh sách:** Mã CTƯĐ, Tên CTƯĐ, Trạng thái, Ngày hiệu lực (dd/mm/yyyy), Ngày hết hiệu lực (dd/mm/yyyy hoặc "-"), Ngày tạo (hh:mm:ss – dd/mm/yyyy), Người tạo, Ngày sửa (hoặc "-"), Người sửa (hoặc "-"), Ngày duyệt (hoặc "-"), Người duyệt (hoặc "-").
* **Xem chi tiết CTƯĐ:** Hiển thị các trường như màn tạo/chỉnh sửa + popup **Lịch sử tác động**.

---

## 4. US18 - Xem Code Phí Áp Dụng Cho Một Khách Hàng
*(Navigation: Tra cứu >> Xem code phí theo khách hàng)*

* **Điều kiện tra cứu bắt buộc:** Mã CIF (chỉ nhập 1 mã).
* **Điều kiện tùy chọn:** Sản phẩm dịch vụ (Multiple select, tìm kiếm theo tên SPDV/Code phí).
* **Lưới kết quả:** STT, CIF áp dụng, Code phí, Tên, Biểu phí, Sản phẩm dịch vụ, Công thức tính phí, Người tạo, Ngày tạo, Người sửa, Ngày sửa, Người duyệt, Ngày duyệt.
* Nhấn vào **Mã code phí** → Xem chi tiết code phí.
* **Button Tra cứu CIF:** Mở popup tìm kiếm KH theo thể nhân, điền CIF tự động vào ô tìm kiếm.
  * Điều kiện tra cứu CIF: Số điện thoại (★ bắt buộc) | Loại khách hàng | Chi nhánh quản lý | Tỉnh (phải chọn trước Phường/xã) | Phường/Xã | Trạng thái.
  * Lưới CIF: STT, CIF, Số điện thoại, Tên, Chi nhánh quản lý, Tỉnh, Trạng thái.
  * Click vào CIF → Auto fill vào ô Mã CIF ở màn tra cứu.

---

## 5. US19 - Xem Lịch Sử Thu Phí Theo Khách Hàng
*(Navigation: Tra cứu >> Xem lịch sử thu phí theo khách hàng)*

* **Điều kiện tra cứu bắt buộc:** Mã CIF.
* **Điều kiện tùy chọn:** Sản phẩm dịch vụ | Biểu phí | Code phí | Từ ngày – Đến ngày (theo **ngày thu**).
* **Lưới kết quả:** STT, CIF áp dụng, Tài khoản thu phí, Code phí (Mã - Tên), Loại tiền code phí, Biểu phí, Sản phẩm dịch vụ, VAT, Số tiền phí nguyên tệ, Số tiền phí quy đổi VNĐ, Ngày thu (hh:mm:ss – dd/mm/yyyy).
* Reuse màn hình **Tra cứu CIF** từ US18.
* **Lưu ý:** Dropdown Biểu phí hiển thị dạng "Mã biểu phí - Tên biểu phí". Dropdown Code phí hiển thị dạng "Mã code phí - Tên code phí".

---

## 6. US20 - Tra Cứu Lịch Thu Phí Dự Kiến Theo Khách Hàng
*(Navigation: Tra cứu >> Xem lịch thu phí dự kiến theo khách hàng)*

* **Điều kiện tra cứu bắt buộc:** Mã CIF.
* **Điều kiện tùy chọn:** Sản phẩm dịch vụ | Biểu phí | Code phí | Từ ngày – Đến ngày. 
  * ⚠️ **Lưu ý (Ràng buộc phạm vi thời gian):** Tìm kiếm theo **ngày thu dự kiến** và bị giới hạn tối đa trong khoảng thời gian **1 năm** (bao gồm ngày hôm nay).
* **Lưới kết quả:** STT, CIF áp dụng, Tài khoản thu phí, **Số thẻ** (khác US19), Code phí (Mã - Tên), Loại tiền Code phí, Biểu phí, Sản phẩm dịch vụ, VAT, Số tiền phí nguyên tệ, Số tiền phí quy đổi VNĐ, **Ngày thu dự kiến** (dd/mm/yyyy — khác US19).
* ⚠️ **Điểm khác biệt với US19:** Có thêm cột **Số thẻ** và cột ngày là **Ngày thu dự kiến** (format dd/mm/yyyy) thay vì Ngày thu (hh:mm:ss – dd/mm/yyyy). Mặc định các số tiền hiển thị là khoản tiền "dự kiến sẽ thu".

---

## 7. US21 - Xem CTƯĐ Áp Dụng Theo Khách Hàng
*(Navigation: Tra cứu >> Xem CTƯĐ theo khách hàng)*

* **Điều kiện tra cứu bắt buộc:** Mã CIF.
* **Điều kiện tùy chọn:** Sản phẩm dịch vụ | Từ ngày – Đến ngày (theo ngày hiệu lực) | Loại khách hàng (KHCN/KHTC/KHDNSN/CBNV).
* **Lưới kết quả:** STT, CIF áp dụng, Code phí, Tên code phí, Biểu phí, Sản phẩm dịch vụ, Công thức tính phí, **Mã CTƯĐ**, **Tên CTƯĐ**, Ngày hiệu lực CTƯĐ, Ngày hết hiệu lực CTƯĐ, Người tạo, Ngày tạo, Người sửa, Ngày sửa, Người duyệt, Ngày duyệt.
* Nhấn vào **Mã CTƯĐ** → Xem chi tiết CTƯĐ.
* Reuse màn hình **Tra cứu CIF** từ US18.

---

## IX. QUẢN TRỊ HỆ THỐNG - ĐĂNG NHẬP, NGƯỜI DÙNG & ĐIỀU KIỆN TÍNH PHÍ (US22 - US26)

### 1. US22 - Đăng nhập (Login)
* **Quy tắc tính hợp lệ:** Username phải tồn tại + Trạng thái `Hoạt động` + Đúng Mật khẩu.
* **Thông báo lỗi (Validation messages):**
  * Tên ĐN không tồn tại → `"Tên đăng nhập không tồn tại trên hệ thống"`
  * Trạng thái khác Hoạt động → `"Tài khoản hiện đang không hoạt động. Vui lòng liên hệ quản trị viên"`
  * Sai Pass/User → `"Tên đăng nhập hoặc Mật khẩu không hợp lệ"`
  * Bỏ trống → `"Tên đăng nhập/Mật khẩu không được để trống"`
* **Phiên làm việc (Session Rules):**
  * Tự động đăng xuất sau `n` phút không thao tác (Theo cấu hình tham số `SESSION_TIMEOUT`).
  * **1 Session per User:** Mỗi tài khoản chỉ được phép có **1 phiên thiết bị đăng nhập đồng thời**. Đăng nhập mới sẽ tự động **kick** (đăng xuất) session cũ ra khỏi trình duyệt.

### 2. US23 - Đăng xuất (Logout)
* **Logout chủ động:** Nhấn "Đăng xuất" ở góc trái màn hình → Hiển thị Popup Xác nhận → Đồng ý → Quay về màn hình Đăng nhập.
* **Logout thụ động (Session timeout):** Hết giờ → Tự đăng xuất → Hiện popup *"Phiên đăng nhập của bạn hết hạn. Vui lòng đăng nhập lại"* → Nhấn Đăng nhập để về màn login.
* **Lưu ý:** Chữ ký số / các tác vụ đang thực hiện dở dang sẽ KHÔNG ĐƯỢC LƯU khi bị đăng xuất.

### 3. US24 - Quản lý người dùng
*(Navigation: Quản trị hệ thống >> Quản lý người dùng)*

* **Lưới danh sách mặc định:** Sort theo "Ngày sửa" hoặc "Ngày tạo" gần nhất ở trên cùng (DESC).
* **Thêm mới lẻ (Thêm từng User):**
  * Tên đăng nhập (Username): Chữ viết liền, không dấu, không có khoảng trắng. (Duplicate → "Tên đăng nhập đã tồn tại"; Sai định dạng → "Tên đăng nhập không hợp lệ").
  * Trường bắt buộc (★): Tên đăng nhập, Tên hiển thị, Khối, Phòng ban, Nhóm quyền, Trạng thái (Hoạt động/Không HĐ), Số điện thoại, Email.
* **Tải lên danh sách (Import Excel đa lượng):**
  * Logic Validate tương tự như khi thêm mới từng user.
  * **Ràng buộc UI:** Nếu có **ít nhất 1 dòng (user) bị lỗi** → Hệ thống bôi đỏ text những điểm lỗi → **Disable button Xác nhận** (không cho phép import bán phần).
  * Chỉ khi 100% data đẩy file lên là hợp lệ → Mới cho phép ấn **Xác nhận** đẩy toàn bộ vào lưới.

### 4. US26 - Danh mục Điều kiện tính phí
*(Navigation: Quản trị hệ thống >> Danh mục điều kiện tính phí)*
* **Thêm mới Điều kiện tính phí:**
  * **Nguồn dữ liệu = API**: Bắt buộc nhập `Mapping note msg` (Tên field trong API).
  * **Nguồn dữ liệu = ETL**: Bắt buộc chọn `Bảng dữ liệu` (Khách hàng/Tài khoản/Thẻ) và `Trường dữ liệu`.
  * **Kiểu dữ liệu**: Phải chọn từ danh sách Number / String / Date / Time.
* **Validation sửa/đổi Trạng thái:**
  * **Chặn sửa:** Nếu Điều kiện đang gắn với CTƯĐ (Chưa HL/Đang HL) hoặc Code phí (Hoạt động/Ngưng hoạt động/Chờ gán) → Báo lỗi: *"Không thể sửa trạng thái. Điều kiện tính phí đang sử dụng trong hệ thống"*.
  * **Cho phép sửa:** Chưa gắn CTƯĐ/Code phí, hoặc CTƯĐ = Hết HL, Code phí = Hủy.
* **Quy tắc mapping màn hình khác:** Chỉ các Điều kiện tính phí có **Trạng thái = Hoạt động** mới được hiển thị trong dropdown list khi người dùng Thêm/Sửa Code phí và CTƯĐ.

---

## X. TỰ ĐỘNG TÍNH PHÍ, THU PHÍ & TRUY THU NỢ PHÍ (US33 - US36)

### 1. US33 & US34 - Tính phí tự động Online & Kênh Quầy (Adhoc)
* **Xác định CTƯĐ áp dụng (nếu có nhiều CTƯĐ hợp lệ):**
  1. Chọn CTƯĐ có số tiền ưu đãi **LỚN NHẤT**.
  2. Nếu bằng nhau → Chọn CTƯĐ có **Ngày hết hiệu lực XA NHẤT**.
* **Quy đổi Tỷ giá tiền tệ đối với Số tiền Min/Max:** 
  * Nếu Loại tiền khác nhau, hệ thống luôn lấy **Tỷ giá bán giao ngay**. Nếu cả 2 đều khác VND (ví dụ EUR -> USD), dùng Tỷ giá chéo `T1/T2`.
* **Tính thuế VAT:**
  * `Phí ĐÃ BAO GỒM VAT? = CÓ` → VAT = Số tiền sau ưu đãi / 110 * 10 
  * `Phí ĐÃ BAO GỒM VAT? = KHÔNG` → VAT = Số tiền sau ưu đãi / 100 * 10
  * **Làm tròn:** VND, JPY → Làm tròn số nguyên. Loại tiền tệ khác → Làm tròn 2 số thập phân.
* **Luồng Adhoc (Kênh quầy):** User chọn SPDV → Hệ thống tải công thức. Nếu là Số cố định → Hiện luôn tiền. Nếu công thức → Cho User chọn dạng nhập liệu "Thủ công" (tự nhập số tiền cuối) hoặc "Tự động" (nhập biến số lượng/đơn giá để hệ thống tự tính). Bất kỳ sửa đổi Manual nào đều bị check qua Ràng buộc Min/Max của code phí.

### 2. US35 - Tự động thu phí định kỳ (Cronjob)
* **Verify Điều kiện Tài khoản thu phí mặc định:**
  1. Cùng loại tiền mã phí.
  2. Sản phẩm tài khoản thuộc biến cấu hình `CA_PRODUCT`.
  3. Trạng thái tài khoản = `Hoạt động, Tạm ngừng hoạt động, Tạm khóa ghi có`.
* **Luồng backup (Fallback):** Nếu TK mặc định lỗi/hết tiền, hệ thống tự động quét các TK khác của khách hàng thỏa 3 điều kiện trên. Lúc này ưu tiên TK nào có **Số dư lớn nhất** (Bằng nhau thì lấy Random).

### 3. US36 - Tự động truy thu, tận thu Khách hàng Ghi nợ 
* **Quét đầu ngày:** Quét tài khoản khách hàng T-1 có số dư > 0.
* **Tận thu Realtime:** Đọc biến động từ Topic T24 (Tk phát sinh ghi có) → Kích hoạt thu nợ. (Nguyên tắc: Tận thu = thu được bao nhiêu hay bấy nhiêu kể cả không đủ số tiền hóa đơn nợ phí).
* **Quy tắc ưu tiên trừ nợ (nếu 1 KH thiếu nhiều kỳ nợ):**
  1. Đóng tiền theo **Độ ưu tiên Nghiệp vụ** (từ thấp -> cao cấu hình trên nhóm Code phí).
  2. Bằng nhau → Đóng tiền theo **Ngày đến hạn** (từ xa nhất đến gần nhất).
  3. Bằng nhau tiếp → Random nợ phí.
* **Xóa Nợ Phí:** Thực hiện ở công cụ (Pricing). Pricing gọi API sang ProfiX cập nhật trạng thái Không truy thu nữa.

---

## 8. Quy tắc chung về Tra cứu (Common Rules)

| Quy tắc | Mô tả |
|---------|-------|
| Tìm kiếm gần đúng | Mã/tên điều kiện đều hỗ trợ tìm kiếm gần đúng (like/contains) |
| Tải xuống | Xuất file Excel theo dữ liệu đang hiển thị trên lưới. Tham chiếu "Quy tắc tải xuống tại mục Quy tắc chung". |
| Lịch sử tác động | Popup hiển thị khi xem chi tiết bất kỳ bản ghi nào. Tham chiếu "mục Lịch sử tác động tại Quy tắc chung". |
| Giá trị không có dữ liệu | Hiển thị dấu "-" trên lưới thay vì để trống. |
| Format ngày tạo/sửa/duyệt | `hh:mm:ss – dd/mm/yyyy` |
| Format ngày hiệu lực | `dd/mm/yyyy` |
| Tra cứu CIF (Popup dùng chung) | Được dùng tại US18, US19, US20, US21. Bắt buộc nhập **Số điện thoại**. Chọn Tỉnh trước rồi mới chọn Phường/Xã. Click CIF → auto fill mã CIF vào form chính. |

---

## 9. So Sánh các màn Tra Cứu Lịch Sử/Dự Kiến

| Tiêu chí | US19 - Lịch sử thu phí | US20 - Lịch thu dự kiến |
|----------|----------------------|------------------------|
| Navigation | Tra cứu >> Xem lịch sử thu phí theo KH | Tra cứu >> Xem lịch thu phí dự kiến theo KH |
| Điều kiện thêm | Không có Số thẻ | Không có |
| Cột Số thẻ | ❌ Không có | ✅ Có |
| Cột ngày | Ngày thu (`hh:mm:ss – dd/mm/yyyy`) | Ngày thu dự kiến (`dd/mm/yyyy`) |
| VAT | Số tiền VAT đã thu | Số tiền VAT dự kiến thu |
| Số tiền phí | Đã thu (nguyên tệ + quy đổi VNĐ) | Dự kiến thu (nguyên tệ + quy đổi VNĐ) |

---

---

# X. QUY TẮC CHUNG TOÀN HỆ THỐNG (Appendix từ P3)

## 1. Định dạng trường dữ liệu (Field Formats)
* **Combobox:** Cho phép chọn từ danh sách hoặc gõ text để tìm kiếm gợi ý.
* **Dropdown List:** Chỉ được chọn 1 giá trị từ danh sách có sẵn.
* **Multiple Select Dropdown:** Chọn 1 hoặc nhiều giá trị. Hỗ trợ gõ text để search.
* **Number:** 
  * Phân cách hàng nghìn bằng dấu phẩy (`,`), hàng thập phân bằng dấu chấm (`.`).
  * Mặc định lấy **2 chữ số thập phân**.
  * **Ngoại lệ:** Đồng tiền **VND** và **JPY** không có hàng thập phân (luôn là số nguyên).
* **Date:** 
  * Định dạng `dd/mm/yyyy`. 
  * Khi lọc theo khoảng `Từ ngày - Đến ngày`: 
    * Từ ngày = `00:00:00.000`
    * Đến ngày = `23:59:59.999`
* **Text:** 
  * Mặc định tối đa: Mã (50 ký tự), Tên (50 ký tự), Ghi chú/Diễn giải (300 ký tự).

## 2. Quy tắc Tìm kiếm & Lọc (Search & Filter)
* **Logic:** AND giữa các điều kiện lọc.
* **Xử lý Text:** Không phân biệt HOA/thường; Bỏ dấu tiếng Việt khi tìm gần đúng; Tự động **Trim khoảng trắng** trước khi gửi đi.
* **Lọc nâng cao vs Tìm nhanh:** Chỉ được chọn 1 trong 2. Khi nhập search bar tìm nhanh → Disable nút Lọc nâng cao và ngược lại.
* **Advanced Filter (Xoá lọc):** Có nút xóa từng điều kiện (x) hoặc xóa toàn bộ (Xoá lọc).

## 3. Tải xuống (Download)
* Button hiển thị khi lưới có dữ liệu.
* Định dạng mặc định: **Excel**.
* Tên file: `[Tên chức năng] - yyyymmddhhmmss`.

## 4. Phân trang (Pagination)
* Mặc định hiển thị **50 bản ghi/trang** (trừ trường hợp cụ thể có mô tả khác).

## 5. Lịch sử tác động (Action History)
* Hiển thị danh sách thay đổi theo thứ tự thời gian **duyệt** từ gần nhất đến xa nhất.
* Các trường: Ngày cập nhật (hyperlink để xem bản record cũ), Tác động (Thêm/Sửa), Người cập nhật.

---

# XI. CHỨC NĂNG HỆ THỐNG & QUẢN TRỊ (US23, US27 từ P3)

## 1. US23 - Đăng xuất hệ thống
*(Navigation: Menu User >> Đăng xuất)*
* **Xác nhận:** Hiển thị Popup Xác nhận trước khi thoát.
* **Tự động đăng xuất:** Dựa trên tham số `SESSION_TIMEOUT` (phút) cấu hình tại Quản trị hệ thống. 
* **Thông báo hết hạn:** "Phiên đăng nhập của bạn hết hạn. Vui lòng đăng nhập lại".
* **Đăng xuất cưỡng bức:** Khi đăng nhập trên thiết bị/phiên làm việc mới, phiên cũ sẽ bị logout tự động.
* **Dữ liệu:** Các tác vụ chưa lưu sẽ bị mất khi logout.

## 2. US27 - Danh mục điều kiện tính phí
*(Navigation: Quản trị hệ thống >> Danh mục điều kiện tính phí)*

### 2.1 Cấu trúc thực thể Điều kiện
* **Mã điều kiện:** (★) Chữ VIẾT HOA, duy nhất.
* **Tên điều kiện:** (★) Nhập text.
* **Nguồn dữ liệu:** (★) API hoặc ETL.
  * **API:** Bắt buộc nhập `Mapping note msg` (Tên field trong API response).
  * **ETL:** Bắt buộc chọn `Bảng dữ liệu` (KH/Tài khoản/Thẻ) và `Trường dữ liệu` tương ứng.
* **Kiểu dữ liệu:** (★) Number / String / Date / Time.
* **Trạng thái:** Hoạt động / Không hoạt động.

### 2.2 Quy tắc nghiệp vụ (Business Rules)
* **Danh sách sử dụng:** Chỉ các điều kiện ở trạng thái "Hoạt động" mới xuất hiện trong màn hình khai báo Code phí/CTƯĐ.
* **Quy tắc chặn sửa trạng thái:**
  * **KHÔNG cho phép** chuyển sang "Không hoạt động" nếu điều kiện đang được gắn với:
    * CTƯĐ (trạng thái Chưa hiệu lực / Đang hiệu lực).
    * Code phí (trạng thái Hoạt động / Ngừng hoạt động / Chờ gán).
  * **CHO PHÉP sửa** nếu chưa gán hoặc chỉ gán với CTƯĐ Hết hiệu lực / Code phí Huỷ.
* **Màn hình Danh mục:**
  * Hỗ trợ Lọc nâng cao (Mã, Nguồn, Trạng thái, Mapping msg).
  * Hỗ trợ Tải xuống danh sách Excel.

---

*📝 Ghi chú: File này sẽ được cập nhật tiếp khi tích hợp P4.*
