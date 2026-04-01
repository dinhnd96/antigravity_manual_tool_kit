---
description: Generate manual test cases from requirements.
skills:
  - qa-automation-engineer
---

> **BẮT BUỘC (MANDATORY SKILL):** Bạn PHẢI nạp và đọc kỹ nội dung của skill **`qa-automation-engineer`** (tại `.agent/skills/qa-automation-engineer/SKILL.md`) trước khi bắt đầu thực hiện tác vụ này.

Generate manual test cases based on the provided requirement.

Steps:

1. Analyze the requirement carefully.
2. Identify the main user scenarios.
3. Generate detailed manual test cases.

Include:

- positive test cases
- negative test cases
- boundary cases
- validation cases

> [!IMPORTANT]
> **Quy tắc Tránh Redundancy và Lỗi Logic Test Steps (Đặc biệt cho UI):**
> Khi sinh Test Case, TUYỆT ĐỐI không dùng chung 1 template Expected Result cho tất cả các hành động UI. Phải tách bạch theo ngữ cảnh:
> 1. **Đối với Luồng XEM (View-only) / ĐÓNG FORM (Close/Cancel):**
>    - *Steps:* Chỉ mở form Xem hoặc nhập text rồi bấm Đóng/Hủy. (KHÔNG chèn các step như "Nhấn xác nhận", "Kiểm tra trạng thái").
>    - *Expected Result:* UI hiển thị lại màn hình cũ, Hủy bỏ dữ liệu nháp (nếu có). KHÔNG gọi API Save, KHÔNG sinh bản ghi "Chờ duyệt", KHÔNG thay đổi Data State.
> 2. **Đối với Luồng THÊM MỚI / LƯU (Create/Submit):**
>    - *Steps:* Nhập liệu hợp lệ/không hợp lệ -> Nhấn Lưu.
>    - *Expected Result:* Validate thông tin, thông báo "Thành công" hoặc "Lỗi đỏ", sau đó mới sinh bản ghi.
> 3. **Tránh Mâu thuẫn Nghiệp Vụ Sinh Lỗi:** Không đưa kết quả "Hiển thị đúng thông báo lỗi trên UI" cho các Business rule sinh tự động (Auto-generated fields) vì user không thể tương tác trực tiếp. Chỉ test logic Positive.

Output format:

Test Case ID  
Title  
Preconditions  
Steps  
Expected Result  
Priority