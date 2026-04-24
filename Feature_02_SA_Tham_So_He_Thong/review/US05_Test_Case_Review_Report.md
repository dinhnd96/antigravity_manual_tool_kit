# Báo Cáo Review Test Case - US05: Định nghĩa công thức tính phí

**Người thực hiện:** QA Test Case Reviewer (AI)
**Tài liệu tham chiếu:** `US05.docx`
**Test Case File:** `Test_Cases_US05.xlsx`

## 1. Bảng 1: Lỗi Nghiệp Vụ & Gap Analysis

| LOG_ID / URD_Ref | Loại phát hiện | Mô tả Sự cố / Mâu thuẫn | Mức độ Nghiêm trọng | Đề xuất sửa chữa |
| :--- | :--- | :--- | :--- | :--- |
| **Bảng 1 - R19 (Trường Công thức)** | **GAP (BVA)** | Chưa có Test Case kiểm tra giá trị biên đối với độ dài của Công thức. Tài liệu quy định "Nhập tối đa 300 ký tự", nhưng không có case nào test độ dài = 300 (HAP) và độ dài > 300 (NEG). | **High** | Bổ sung 2 TC biên: 1 TC Happy (công thức dài đúng 300 ký tự) và 1 TC Negative (công thức > 300 ký tự bị chặn không cho nhập/lưu). |
| **Bảng 1 - R9, R10 (Trường Tối thiểu, Tối đa)** | **GAP (BVA)** | Chưa có TC kiểm tra các giá trị biên của trường "Tối thiểu" và "Tối đa" (ví dụ: Tối thiểu = 0, Tối thiểu số âm, Tối đa vượt quá giới hạn Number của hệ thống, hoặc nhập ký tự Text vào Number). | **Medium** | Bổ sung các TC Negative validation cho data type và limit của trường Tối thiểu/Tối đa. |
| **LOG-FORMULA-VALIDATE-CCY-MISMATCH** | **Logic Mismatch** | TC#9 (`PR02-BR-NEG-005`) mong đợi báo lỗi chặn lưu khi Loại tiền Tối thiểu/Tối đa khác Loại tiền Code phí (đối với công thức số cố định). Tuy nhiên, **tại Q&A Q1**, BA đã phản hồi "Drop" rule bắt lỗi này vì việc quy đổi chéo được thực hiện ở US33. | **High** | Xóa bỏ `PR02-BR-NEG-005` hoặc sửa lại thành Happy Path (Hệ thống cho phép lưu thành công mà không báo lỗi loại tiền). |
| **LOG-FORMULA-FUNC-OP-SEQ** | **Logic Mismatch** | TC#5 (`PR02-BR-HAP-002`) mong đợi việc nhập "Các toán tử liên tiếp" như `#LC_AMOUNT# * / 0.01` là **hợp lệ**. Theo chuẩn toán học và logic parse công thức, 2 toán tử `*` và `/` không thể đứng liền nhau, hệ thống sẽ văng lỗi cú pháp. | **High** | Chuyển `PR02-BR-HAP-002` thành TC Negative (Báo lỗi Syntax do sai cú pháp toán học). |

## 2. Bảng 2: Lỗi Tiêu Chuẩn Enterprise Format

Nhìn chung, bộ Test Case đạt chất lượng xuất sắc về format: Data được hardcode chính xác, URD_Ref rõ ràng và đủ 4 Layer cho phần lớn TC. Tuy nhiên, vẫn còn một số điểm cần chuẩn hóa:

| TC_ID | Hạng mục Vi Phạm | Mô tả Vi Phạm | Hướng khắc phục |
| :--- | :--- | :--- | :--- |
| **PR02-UI-001** | **Expected Result Layer** | Vi phạm cấu trúc 4 lớp: Lớp `(iv)` được quy định là Output/Download nhưng lại mô tả "Danh sách Trường giá trị tính phí hiển thị...". Đồng thời thiếu hẳn lớp `(iii)` Database State. | Đưa mô tả hiển thị danh sách lên lớp `(i)` hoặc `(ii)`. Bổ sung lớp `(iii) Không có thay đổi dữ liệu` và lớp `(iv) Không có file output`. |
| **PR02-UI-005** | **Expected Result Layer** | Ở lớp (iv) bị cắt cụt do typo (giới hạn ký tự): `"Không có output fil"`. Các TC UI thường gộp chung check state nhưng cũng cần đảm bảo tính nguyên vẹn text. | Chỉnh sửa lại typo: `"Không có output file"`. |

## 3. Tổng kết
- **Mức độ tuân thủ format Enterprise:** **95%** (Rất xuất sắc). Việc áp dụng URD_Ref và đánh số các Step/Layer được thực hiện cực kỳ triệt để. Test Data luôn dùng hardcode rõ ràng (như 50000, 10000).
- **Coverage & Logic:** Cần fix lại lỗi mâu thuẫn theo Q&A (TC#9) và bổ sung 2 nhóm Test Case Boundary (Độ dài công thức 300 ký tự, và Biên Tối thiểu/Tối đa) để bộ TC đạt mức bao phủ 100%.
