---
name: test_case_management_sync
description: Kỹ năng đồng bộ hóa, quản trị tập trung và dọn dẹp (Clean-up) bộ Test Case chuyên nghiệp cho dự án ProfiX.
---

# Test Case Management Sync Skill

## Giới thiệu
Kỹ năng này hoạt động như một **Test Data / Process Engineer**, chuyên xử lý, chuẩn hóa và quản trị bộ Test Case từ nhiều nguồn độc lập vào một Master File (`Test case_Management_ProfiX.xlsx`) và ngược lại. Khả năng lõi bao gồm:
- **Đồng bộ hai chiều (Two-way Sync):** Gộp các file nhỏ thành Master hoặc bơm ngược (Backpropagate) dữ liệu đã chỉnh sửa từ Master về lại các file module độc lập.
- **Dọn rác & Sửa lỗi Logic (Anti-pattern Clean-up):** Tự động phát hiện và cắt bỏ các cụm Steps/Expected Results bị copy-paste sai ngữ cảnh (Ví dụ: Chức năng Xem/Đóng nhưng lại có bước 'Nhấn xác nhận' và kết quả 'Sinh trạng thái Chờ duyệt').
- **Định dạng & Bảo toàn Công thức (Formatting & Formula Preservation):** Thay vì dùng các thư viện làm mất định dạng, skill này dùng `openpyxl` để bảo toàn nguyên vẹn cấu trúc file, Dashboard công thức (`COUNTIF`, `COUNTA`), thêm viền (Borders), căn dòng (Wrap Text) cho các ô chữ dài.

## Cách sử dụng
Gọi skill khi bạn cần:
1. Gộp file hoặc phân tách file Test Case (Sync In/Out).
2. Dọn rác hàng loạt các Test case UI sinh bởi AI bị dính lỗi Copy-Paste dập khuôn.
3. Refresh lại giao diện Master File (chuẩn các hàng dễ đọc, auto-width, vertical top).
4. Khôi phục lại Dashboard đếm số lượng Test Case từ file `.bak` dự phòng.

## Quy trình hành động (Workflow)
1. **Quét (Scan):** Đọc danh sách file Test Case rời hoặc file Master `.bak`.
2. **Làm sạch (Cleanse):** Quét cột Thao tác (Steps) và Kết quả mong đợi (Expected). Appy bộ lọc Anti-pattern cấm 'Lưu thành công' hay 'Nhấn xác nhận' đối với giao diện View-Only/Close.
3. **Đồng bộ (Sync):** Map dữ liệu theo `TC_ID` và ghi đè nội dung sạch.
4. **Trang điểm (Format):** Chỉnh lại độ rộng cột `Steps (45)`, `Expected (45)`, bật cờ `Wrap Text=True`.
5. **Báo cáo (Report):** Đảm bảo Sheet `📊 Dashboard` đã kết nối lại công thức thống kê chuẩn xác.

## Yêu cầu môi trường
- **Ngôn ngữ:** Python 3.8+
- **Thư viện Engine bắt buộc:** Bắt buộc dùng `openpyxl` để tránh mất Format (Không bao giờ dùng thư viện chỉ đọc Data như `pandas` thuần khi thao tác lưu đè).

## Gợi ý Prompts lệnh gọi cho User
- *"Hãy dùng skill test_case_management_sync để format lại file Master, kẻ bảng cho dễ nhìn và update công thức đếm TC ở Dashboard."*
- *"Chạy lệnh đồng bộ ngược dữ liệu từ file Master Excel về lại 14 file Test Case trong thư mục nhánh."*
- *"Dọn dẹp các Test Case chức năng Đóng/Hủy bị dính chữ 'Nhấn Xác nhận' rồi format lại file giúp tôi."*
