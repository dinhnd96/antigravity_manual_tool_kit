---
description: Chiến lược khám phá toàn bộ ứng dụng và sinh Automation bằng AI Agent (Agentic Full Discovery)
---

# WORKFLOW: AGENTIC FULL DISCOVERY (AI KHÁM PHÁ TOÀN DIỆN)

## 🏗️ QUY TRÌNH "HÀNH ĐỘNG" CHI TIẾT

### 1. Phân phối Tài khoản & Login (Phát pháo đầu tiên)
- AI sẽ khởi động trình duyệt nội tại (Browser Subagent).
- Đi đến trang Login của Profix và thực hiện đăng nhập.
- **Xác nhận:** Đảm bảo trang chính của Dashboard đã hiện ra.

### 2. Quét Side-Menu & Lấy danh sách Module (Kiểm kê Folder)
- AI lướt qua toàn bộ Side-menu (Thanh điều hướng bên trái/trên).
- Chụp ảnh màn hình và lấy danh sách các đường link (URL) của từng module (Sản phẩm, Người dùng, Biểu phí...).
- **Xếp hạng:** Ưu tiên các Folder có nghiệp vụ quan trọng trước.

### 3. Lặp (Loop) Khám phá cho từng Module (Theo chiều sâu)
Với mỗi Folder Module đã tìm thấy:
- **Khám phá Bảng:** Chạy Filter, Search, Pagination để xem cách API lấy danh sách dữ liệu.
- **Tạo mới:** Tự tìm nút "Thêm", tự điền Form (Sử dụng dữ liệu thông minh "Faker").
- **Duyệt chi tiết:** Click vào một bản ghi bất kỳ để xem API lấy dữ liệu Item.
- **Hành động đặc biệt:** Tìm các nút như "In", "Tải Excel", "Gửi phê duyệt".
- **Dọn dẹp:** Nếu có nút Xóa, AI sẽ xóa dữ liệu demo vừa tạo.

### 4. Thu thập & Ghép nối dữ liệu (Smart Chaining)
- Trong lúc AI thao tác, toàn bộ gói tin Network (POST, GET, PUT...) sẽ được lưu lại ngầm.
- **Phân tích Chaining:** AI tự phân tích: "Dữ liệu ở API Tạo mới có `ID = 123` ➔ API Sửa cũng dùng `ID = 123`" ➔ Tự thiết lập biến trong Postman.

### 5. Xuất bản Bộ kịch bản (Automation Output)
- Tổng hợp toàn bộ dữ liệu khám phá được thành một tập tin Postman Collection (.json) hoàn chỉnh.
- Đặt tên folder theo nghiệp vụ thực tế (Ví dụ: `Module_Sản_Phẩm`, `Module_Phê_Duyệt`).
- Nhúng đầy đủ các Assertions (Kiểm tra 200, Performance, JSON Body).

## 📊 BÁO CÁO KẾT QUẢ (FINAL REPORT)
- Danh sách các Folder đã khám phá thành công.
- Tổng số API đã tìm thấy và đưa vào Automation.
- Các lỗi 500 hoặc rủi ro UI/API đã phát hiện được trong lúc "cày quét".

---
// turbo-all
// Workflow này được thiết kế để AI tự hành động (Self-Operating) 100% khi được kích hoạt.
