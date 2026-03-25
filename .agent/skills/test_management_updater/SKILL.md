---
name: test_case_management_sync
description: Kỹ năng đồng bộ hóa và quản trị tập trung bộ Test Case chuyên nghiệp cho dự án ProfiX.
---

# Test Case Management Sync Skill

## Giới thiệu
Kỹ năng này được thiết kế để tự động hóa việc quản trị bộ Test Case (TC) từ các file đơn lẻ vào một file quản lý tổng thể (`TC_Management_ProfiX.xlsx`). Nó giải quyết các bài toán về:
-   **Đồng bộ hóa:** Gộp nhiều file Excel riêng lẻ vào các Sheet tương ứng.
-   **Tiêu chuẩn hóa:** Tự động thêm các cột phục vụ Execution (Status R1/R2, Tester, Final Status).
-   **Báo cáo:** Tự động cập nhật Dashboard và Daily Tracking theo thời gian thực.
-   **Định dạng:** Áp dụng Wrap Text, Căn lề, và Conditional Formatting (Xanh/Đỏ).

## Cách sử dụng
Sử dụng kỹ năng này khi:
1.  Người dùng có các file Test Case mới trong thư mục `Test case/`.
2.  Cần khởi tạo hoặc cập nhật file Dashboard tổng thể.
3.  Muốn chuẩn hóa định dạng (xuống dòng, đánh số thứ tự) cho toàn bộ tài liệu.

### Quy trình hành động (Workflow)
1.  **Quét (Scan):** Tìm tất cả các file `.xlsx` trong thư mục `Test case/`.
2.  **Đồng bộ (Sync):** Tạo (hoặc cập nhật) Master File `TC_Management_ProfiX.xlsx`.
3.  **Mở rộng (Extend):** Thêm các cột phục vụ chạy test (Status/Tester/Cycle) cho mỗi sheet.
4.  **Báo cáo (Report):** Cập nhật Dashboard thống kê tổng và Sheet theo dõi hằng ngày.

## Yêu cầu môi trường
-   **Python:** 3.8+
-   **Thư viện:** `pandas`, `openpyxl`

## Kịch bản (Prompts) gợi ý cho User
-   *"Hãy dùng skill test_case_management_sync để gộp tất cả test case vào file quản lý tổng giúp tôi."*
-   *"Cập nhật Dashboard tiến độ trong file TC_Management từ các file test case mới."*
-   *"Chuẩn hóa cột Precondition và thêm cột Status Pass/Fail cho toàn bộ bộ test case."*

## Cấu trúc Master File hỗ trợ
-   **📊 Dashboard:** Thống kê tổng số lượng TC, % Pass/Fail theo từng module.
-   **📅 Daily Tracking:** Ghi nhận khối lượng thực hiện theo ngày/tester.
-   **🧪 Sheets chi tiết:** Chứa dữ liệu kịch bản kèm cột R1/R2 để theo dõi lỗi.
