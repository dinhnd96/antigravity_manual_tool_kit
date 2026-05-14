# ProfiX Phase 1 - Business Matrix & Traceability

> [!NOTE]
> Tài liệu này bóc tách hệ thống thành dạng Ma trận Phân quyền (CRUD Matrix) đối với các thực thể dữ liệu (Data Entities) và tóm tắt các Quy tắc cốt lõi (Common Rules) áp dụng trên toàn bộ hệ thống. 

## 1. Ma trận Nghiệp vụ (CRUD Matrix)

Dựa trên nguyên tắc thiết lập hệ thống Ngân hàng (có Ma trận phê duyệt - US25), dữ liệu sẽ tuân thủ mô hình **Maker - Checker**. 
Chú thích: `C` (Create - Khởi tạo), `R` (Read - Xem/Tra cứu), `U` (Update - Cập nhật), `D` (Delete - Xóa/Hủy), `A` (Approve - Phê duyệt), `X` (Execute - Thực thi tự động).

| Phân hệ / Đối tượng (Entity) | Admin | NV Khai báo (Maker) | NV Phê duyệt (Checker) | Core Engine | User Stories Liên kết |
| --- | :---: | :---: | :---: | :---: | --- |
| **Quản lý danh mục SPDV** | | C, R, U | R, A | | US01, US10, US14 |
| **Code phí & Quy tắc tính phí** | | C, R, U, D* | R, A | R | US02, US03, US04, US05, US09 |
| **Biểu phí định kỳ / Quyết định** | | C, R, U | R, A | R | US06, US07, US08, US15 |
| **Chương trình Ưu đãi (CTƯĐ)** | | C, R, U | R, A | X | US11, US12, US13, US16, US37 |
| **Báo cáo & Dashboard** | | R | R | | US29, US30, US31, US32 |
| **Tra cứu Giao dịch / Khách hàng** | | R | R | | US17, US18, US19, US20, US28 |
| **Người dùng & Phân quyền** | C, R, U, D | | | | US23, US24, US25 |
| **Quy tắc hệ thống (Tập KH, ...)** | C, R, U | | R, A | R | US26, US27 |
| **Transaction / Billing Logs** | | R | R | C, X | US33 -> US40 |

*(D*) Việc "Xóa" trên hệ thống ngân hàng thường là "Hủy hiệu lực" (Deactivate/Inactive) thay vì xóa vật lý khỏi Database, nhằm giữ lại Lịch sử tác động (Audit Log).*

---

## 2. Các Quy tắc Nền tảng (Common Rules)

Phần này tóm tắt Phụ lục FSD, các quy tắc này được áp dụng ngầm định (Implicitly) trên toàn bộ các màn hình của Hệ thống ProfiX. Khi viết Test Case, các quy tắc này phải được tính đến mà không cần BA nhắc lại.

### 2.1. Quy tắc Thao tác UI (User Interface)
- **Tìm kiếm (Search) & Lọc nâng cao (Advanced Filter):** Hỗ trợ tìm kiếm tương đối (like) và tuyệt đối (exact match). Có thể kết hợp nhiều tiêu chí bằng toán tử AND.
- **Phân trang (Pagination):** Mặc định hiển thị danh sách dạng lưới (Grid/Table) có phân trang (ví dụ: 10/20/50 dòng/trang) để tránh quá tải.
- **Tra cứu CIF:** Bất kỳ thao tác nào cần thông tin khách hàng đều phải gọi API lấy dữ liệu chuẩn từ hệ thống Core thông qua mã CIF (Customer Information File).

### 2.2. Quy tắc Nhập/Xuất Dữ liệu
- **Tải xuống (Export):** Cho phép xuất dữ liệu lưới (Grid) ra định dạng Excel/CSV. Thường có giới hạn số lượng dòng export tối đa trong 1 lần.
- **Upload File (Import - US07):** Quá trình import phải có cơ chế validate (kiểm tra định dạng, dung lượng, tính hợp lệ của dữ liệu) trước khi ghi vào Database. Có log lỗi cụ thể nếu import thất bại.
- **Định dạng trường (Field Format):** Ràng buộc chặt chẽ kiểu dữ liệu (Numeric, Text, Date/Time, Currency). Tiền tệ cần định dạng theo chuẩn ngân hàng (ví dụ: `1,000,000 VND`).

### 2.3. Quy tắc Bảo mật & Dữ liệu
- **Nguyên tắc phân quyền dữ liệu:** Dữ liệu tra cứu bị giới hạn bởi Nhóm quyền (Role) và Đơn vị (Branch/Phòng ban) của người đăng nhập.
- **Lịch sử tác động (Audit Trail):** Mọi hành động `C/U/D/A` của User đối với Tham số/Code phí/Biểu phí đều phải lưu lại vết (Ai làm, làm khi nào, giá trị cũ, giá trị mới). 

> [!IMPORTANT]
> **Loopholes / Gap Analysis Note:** Đối với hệ thống có phê duyệt (Ma trận duyệt), cần kiểm tra kỹ rủi ro: Nếu bản ghi đang ở trạng thái `Chờ duyệt`, liệu Maker có thể tiếp tục `Update` bản ghi đó không? Hoặc Engine có được phép gọi bản ghi đang `Chờ duyệt` ra tính phí hay không? (Chỉ bản ghi `Active/Approved` mới được dùng).
