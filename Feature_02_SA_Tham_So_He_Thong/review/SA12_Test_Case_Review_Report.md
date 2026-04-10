# 📋 BÁO CÁO REVIEW TEST CASE — SA.12 Quản lý biểu mẫu

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** I.1.1.1. SA.12- Quản lý biểu mẫu.docx
> **Bộ Test Case:** SA12_Quan_Ly_Bieu_Mau_Final.xlsx (Sheet: TestCases — 10 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng |
|:---|:---|
| Tổng TC đã có | **10** |
| Số lượng TC bị lỗi Role/Luồng duyệt | **10/10** (Sai mindset Maker/Checker, lỗi gán status Chờ duyệt) |
| Lỗi thiếu sót Field | **1** (Tại case bắt lỗi rỗng thiếu trường Nội dung Email) |
| Gap nghiệp vụ | **0** (Cover rất tốt các rules đặc thù như Placeholder, Rich Text) |
| Điểm sáng QA (Assumptions) | Có tư duy xác nhận (Verify) tài liệu chưa thiết kế với BA |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Bộ TC SA.12 là bộ có nội dung cốt lõi **tốt nhất** trong dàn tham số! Tư duy viết TC kiểm thử được cả các góc độ phức tạp như: tool soạn thảo (BR04) và binding biến Placeholder (BR05), thậm chí đưa ra assumption bắt bẻ tài liệu URD. Điểm trừ duy nhất là dính lỗi di truyền từ template: Sử dụng keyword "Maker" và status "Chờ duyệt" cho chức năng KHÔNG DUYỆT.

---

## 2. PHÂN TÍCH MOCKUP UI

*Ghi chú: Tài liệu docx của SA.12 hoàn toàn bị thiếu folder Media (Không có hình ảnh Mockup nào được cung cấp). Do vậy review Test Case phải bám sát %100 vào các Field liệt kê ở BR table là chính:*
- `Mã Biểu mẫu`
- `Tên Biểu mẫu`
- `Tiêu đề`
- `Bảng nguồn dữ liệu`
- `Nội dung` (với thanh công cụ Rich Text Editor)

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | Validate các trường bắt buộc (*) | SA12-BR01-HAP-001, SA12-BR01-NEG-001 | ⚠️ Thiếu field Nội dung trong dàn variant bỏ trống |
| BR_02 | Cancel thao tác (Nút Đóng) | SA12-BR02-UI-001 | ✅ Đủ |
| BR_03 | Unique Tên và Mã biểu mẫu | SA12-BR03-NEG-001 | ✅ Đủ |
| BR_04 | Công cụ Editor format | SA12-BR04-HAP-001 | ✅ Đủ |
| BR_05 | Auto binding Placeholder #fieldname# | SA12-BR05-HAP-001, SA12-LOG-01-INTEGRATION | ✅ **Excellent** (Nghĩ ra case validation tag rác) |
| General | Các chức năng View, Sửa, Tìm kiếm | SA12-UI-01, SA12-UI-04, SA12-UI-02 | ✅ Đủ |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI (FINDINGS & RECOMMENDATIONS)

| # | TC_ID / BR_ID | Loại phát hiện | Mô tả sự cố (Bug Insight) | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | Toàn bộ 10 TCs | **Logic Mismatch (Role/Mindset)** | Tất cả Precondition của 10 dòng đều ghi là *"Đăng nhập Maker"*. Giống các module trước, đây là tính năng **Tạo xong dùng ngay, KHÔNG DUYỆT**, việc dùng Role Maker là sai ý đồ phân quyền của chủ quy trình. Ở case `SA12-BR01-HAP-001` có expected: *"Trạng thái/Audit: Bản ghi ở trạng thái [Hoạt động] hoặc [Chờ duyệt]"* -> Chắc chắn không có "Chờ duyệt", viết kiểu 50/50 thế này dev sẽ hỏi vặn lại ngay. | 🔴 High | Sử dụng Find & Replace: Đổi hàng loạt "Maker" thành **"Người dùng"**. Xóa thẳng cụm status "hoặc [Chờ duyệt]" khỏi kết quả của SA12-BR01-HAP. |
| 2 | SA12-BR01-NEG-001 | **Thiếu Validate Field** | TC đang liệt kê các trường cố tình để trống để hệ thống báo lỗi đỏ: *[Mã biểu mẫu], [Tên biểu mẫu], [Bảng nguồn dữ liệu], [Tiêu đề]* nhưng quên mất một trường bự nhất là **[Nội dung]**. Một email mẫu không thể rỗng ruột (Blank content) được. | 🟠 Medium | Thêm field **[Nội dung]** vào danh sách các trường được test "Để trống" tại Step 1. |
| 3 | SA12-LOG-01-INTEGRATION | **Điểm sáng phân tích System (Khen ngợi)** | Tester đã rất nhạy cảm khi nhận ra BR.05 chỉ đề cập tới Placeholder chung chung mà kều thiếu cơ chế Validate: Liệu nhập tag lung tung không thuộc "Bảng nguồn" (ví dụ chọn Bảng User nhưng placeholder lại gọi \#balance) thì hệ thống xử lý gãy đổ hay chặn ngay lúc tạo. Câu Assumption *"Cần BA xác nhận..."* đặt ở Note là đạt mười điểm chất lượng Engineer QA! | 🟢 Highlight | Cứ giữ nguyên, hãy copy note gởi trực tiếp cho BA để bếch rules mới vào tài liệu sớm nhất. |

---

## 5. ƯU TIÊN XỬ LÝ SỬA CHỮA (ACTION PLAN)

```text
🔴 CRITICAL ACTION:
  - Xóa triệt để danh xưng "Maker" và gán lại là "Người dùng" hoặc "User phân quyền".
  - Chốt hạ Trạng thái Post-condition chỉ là "Hoạt động", nghiêm cấm xuất hiện Keyword "Chờ duyệt" trong các tính năng tạo-dùng-ngay.

🟠 MEDIUM/LOW ACTION:
  - Bổ sung validation kiểm tra bỏ trống [Nội dung email] ở case Negative.
  - Review với BA sớm về Assumption của case tích hợp nguồn cấu hình Placeholder để chốt requirement trước đi đưa cho Dev Code.
```

> **Review Complete.**
