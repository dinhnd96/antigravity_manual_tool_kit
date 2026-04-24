# Báo Cáo Review Test Case - US02: Khai báo Code Phí

**Người thực hiện:** QA Test Case Reviewer (AI)
**Tài liệu tham chiếu:** `US02.docx`
**Test Case File:** `Test_Cases_US02.xlsx`

## 1. Bảng 1: Lỗi Nghiệp Vụ & Gap Analysis

| LOG_ID / URD_Ref | Loại phát hiện | Mô tả Sự cố / Mâu thuẫn | Mức độ Nghiêm trọng | Đề xuất sửa chữa |
| :--- | :--- | :--- | :--- | :--- |
| **Bảng 1 - R2 (Trường Tên phí)** | **GAP (BVA)** | Chưa có Test Case kiểm tra giá trị biên (Boundary) đối với trường Tên phí. Tài liệu quy định "Nhập tối đa 100 ký tự", nhưng không có TC nào test việc nhập 100 ký tự (Hợp lệ) và 101 ký tự (Báo lỗi). | **Medium** | Bổ sung 2 TC biên: 1 TC Happy (Tên phí dài đúng 100 ký tự) và 1 TC Negative (Tên phí = 101 ký tự, bị chặn). |
| **Bảng 1 - R21 (Validation chéo Nguồn dữ liệu)** | **GAP (Nghiệp vụ Mức cao)** | Bỏ sót hoàn toàn một quy tắc ràng buộc logic rất quan trọng: *"Khi Loại tính phí = Định kỳ... hệ thống sẽ kiểm tra các trường giá trị tại Công thức tính phí phải tồn tại tối thiểu 01 trường điều kiện tính phí được lấy tại CÙNG NGUỒN DỮ LIỆU đó"*. | **High** | Bổ sung ít nhất 2 TC. 1 TC Negative: Chọn biến công thức từ nguồn ETL_A nhưng không tạo điều kiện nào thuộc ETL_A ➔ Báo lỗi. 1 TC Happy: Khai báo đầy đủ. |
| **Bảng 1 - R18 (Mã hạch toán Category)** | **GAP (Data Type/Mâu thuẫn)** | Chưa có TC test trường "Mã hạch toán Category". Ngoài ra có mâu thuẫn trong spec: Cột Định dạng ghi `Number`, nhưng cột Mô tả lại ghi `Nhập text`. Cần làm rõ đây là số hay chữ để test Validation. | **Medium** | Đặt câu hỏi Q&A cho BA để chốt Data type. Sau đó bổ sung 1 TC kiểm tra Validation bắt lỗi Data type của trường này. |
| **Bảng 1 - R15 (Tần suất thu phí)** | **GAP (Nghiệp vụ)** | Chưa có TC kiểm tra bắt lỗi ràng buộc *"Chỉ hiển thị nếu Loại tính phí = Định kỳ"*. Hiện tại bộ TC chỉ test Happy path hiển thị điều kiện, chưa test việc ẩn/disable trường này khi Loại tính phí = "Theo giao dịch". | **Low** | Bổ sung 1 TC UI check sự biến mất của trường Tần suất thu phí và Ngày thu khi chọn Loại tính phí là Theo giao dịch. |

## 2. Bảng 2: Lỗi Tiêu Chuẩn Enterprise Format

Nhìn chung, bộ Test Case đã tuân thủ **cực kỳ xuất sắc** các chuẩn khắt khe: 
- **Test Data** được dùng số liệu thực/cứng (như 101, 10.55, 29/02, ABC@123$). Zero placeholder.
- **URD_Ref** tuân thủ tuyệt đối format `[Vị trí] - [Trích dẫn ngắn gọn]`.
- **Expected Result** chia đúng 4 Layer rất dễ đọc.

Tuy nhiên, có một điểm nhỏ về Format cần khắc phục để đạt chuẩn Enterprise B2:

| TC_ID | Hạng mục Vi Phạm | Mô tả Vi Phạm | Hướng khắc phục |
| :--- | :--- | :--- | :--- |
| **US02-UI-002, US02-UI-003, US02-BR-NEG-008, US02-BR-HAP-004** | **Expected Result Layer** | Ở lớp `(iii) Trạng thái/DB` và `(iv) Output`, người viết đang dùng từ viết tắt `N/A` hoặc `Không ghi nhận` vì đây là các case check UI. Mặc dù đúng ý, nhưng văn phong Enterprise yêu cầu viết thành câu hoàn chỉnh để tránh bắt bẻ từ đối tác. | Sửa chữ `N/A` thành câu hoàn chỉnh: <br>`(iii) Trạng thái: Không thay đổi dữ liệu bản ghi.` <br>`(iv) Output: Không có file/báo cáo xuất ra.` |

## 3. Tổng kết
- **Mức độ tuân thủ format Enterprise:** **90%**. Việc thiết kế data và cấu trúc luồng của bộ này rất chất lượng, người viết am hiểu hệ thống.
- **Coverage & Logic:** Đã cover được hầu hết các rule khó (như đồng bộ tiền tệ, điều kiện Thẻ + TK, năm nhuận). Tuy nhiên, bộ TC đang bị thủng một Rule validation chéo quan trọng giữa Công thức và Điều kiện (R21) và thiếu các case Boundary Value cơ bản của trường Text. Cần update thêm khoảng 4 TC để đóng băng scope rủi ro.
