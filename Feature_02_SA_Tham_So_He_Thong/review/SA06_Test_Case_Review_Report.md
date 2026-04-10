# 📋 BÁO CÁO REVIEW TEST CASE — SA.06 Danh mục điều kiện tính phí

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** I.1.1.1. SA.06- Danh mục điều kiện tính phí.docx
> **Bộ Test Case:** SA06_Danh_Muc_Dieu_Kien_Tinh_Phi_TestCases.xlsx (15 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng | Đánh giá |
|:---|:---|:---|
| Tổng TC đã có | **15** | Đủ bao phủ toàn bộ BR từ URD. |
| Lỗi Role/Luồng duyệt | **0** | ✅ XUẤT SẮC! Hoàn toàn không dính từ khóa "Maker/Checker" hay "Chờ duyệt". |
| Lỗi Tên trường/Mockup | **1** | Mâu thuẫn thuật ngữ giữa Lưới (Grid) và Form tạo mới. |
| Gap nghiệp vụ | **0** | Đã cover quá tốt các rule phức tạp (Condition Binding). |
| Điểm sáng QA | Rất nhiều | Phân tích sâu logic ràng buộc với Code phí & CTƯĐ. |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Bộ TC SA.06 là một bộ xuất sắc tuyệt đối về mặt tư duy luồng nghiệp vụ. Tác giả có cái nhìn phân tích Data & Integration rất vững. Thể hiện qua các TC mã số `SA06-BR-HAP-005` (Test Intergration trạng thái Dropdown) và `SA06-BR-NEG-003` (Chặn cập nhật trạng thái nếu đã bị reference). Lỗi di truyền "Maker" bị diệt sạch tận gốc. File chỉ còn tì vết nhỏ liên quan đến lỗi thiết kế thuật ngữ của Designer.

---

## 2. PHÂN TÍCH MOCKUP UI & SỰ MÂU THUẪN

Tài liệu cung cấp 2 Mockup:
- **image1.png** (Màn List Danh sách): Các trường trên form bộ lọc và lưới gồm: `Mã điều kiện`, `Mô tả`, `Nguồn dữ liệu`...
- **image2.png** (Màn Create Thêm mới): Các trường nhập liệu gồm: `Mã điều kiện`, **`Tên điều kiện`**.

👉 **Lỗi Inconsistency Design:** Ở màn hình thêm mới, Designer gọi nó là `"Tên điều kiện"`. Nhưng lưu ra ngoài Grid danh sách và ô Tìm kiếm thì lại gọi nó là `"Mô tả"`. Sự mâu thuẫn này dễ gây phân mảnh Validation. Bộ Test Case (cụ thể TC `SA06-UI-004`) đang bị vướng một chút do gọi tên theo URD ("Tìm kiếm tên điều kiện") nhưng UI thực tế không có trường Filter nào tên như vậy.

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | Validate các trường bắt buộc | SA06-BR-HAP-001, SA06-BR-NEG-001 | ✅ Đủ các tổ hợp thiếu trường. |
| BR_02 | Cancel thao tác (Đóng form) | SA06-BR-HAP-002 | ✅ Đủ |
| BR_03 | Unique Tên và Mã điều kiện | SA06-BR-NEG-002 | ✅ Đủ |
| BR_04 | Kiểu dữ liệu (DataType formats) | SA06-BR-HAP-003 | ✅ Đủ |
| BR_05 | Logic khóa Status nếu đang bị trói buộc | SA06-BR-HAP-004, SA06-BR-NEG-003, SA06-BR-HAP-005 | ✅ **Cực kỳ Xuất sắc** |
| BR_06 | Logic Mapping tùy biến ETL/API | SA06-BR-HAP-006 | ✅ Rất tinh tế khi Test đổi Dropdown |

---

## 4. CHI TIẾT PHÁT HIỆN TÌ VẾT (MINORS BUGS)

| # | TC_ID | Loại phát hiện | Mô tả sự cố | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | SA06-UI-004 | **Data Name Mismatch** | Tại Step lọc đang ghi *"Nhập text một phần Tên điều kiện"*. Tuy nhiên Field tìm kiếm thực tế trên Mockup có nhãn là **"Mô tả"**. | 🟠 Medium | Nêu Comment cờ đỏ báo cho BA để thống nhất lại thuất ngữ là `Tên điều kiện` hay `Mô tả`. Giữ nguyên TC. |
| 2 | N/A | **Tối ưu hóa UI Test** | Có các TC thuần giao diện như SA06-UI-001. Luồng chạy tay tốn thời gian mà giá trị bắt bug ít. | 🔵 Low | (Tùy chọn) Gộp check UI vào chung TC Happy Path để giảm số lượng Test case ảo. |

---

## 5. KẾT LUẬN

Bộ **SA.06** hoàn toàn Đạt chuẩn nghiệm thu xuất sắc (Ready for Execution). Lỗi mâu thuẫn Label là do khuyết điểm của bản vẽ Mockup (Designer), không phải do người duyệt TC. Không cần chạy Script sửa logic Test Case, chỉ cần forward Report này cho BA để đính chính thuật ngữ Mockup là hoàn mỹ!
