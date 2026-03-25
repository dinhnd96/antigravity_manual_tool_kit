# API Automation Workflow (Swagger -> HTML Report)

Workflow này hướng dẫn các bước thực hiện tự động hóa API Test cho dự án ProfiX.

## 1. Phân tích & Chuẩn bị
1.  **Swagger Analysis:** Đọc tài liệu Swagger (JSON/YAML) để trích xuất Endpoint.
2.  **Collection Setup:** Import Swagger vào Postman Collection hoặc tạo mới.
3.  **Environment Variables:** Khởi tạo `baseUrl` và `bearerToken`.

## 2. Thiết lập Automation (Automation Scripting)
// turbo
1.  Chèn Script tự động lấy Token tại API Login.
2.  Chèn Script kiểm tra Status Code 200/201 tại tất cả APIs.
3.  Chèn Script kiểm tra Schema & Performance (Response Time < 1s).

## 3. Thực thi Test hàng loạt (Cực nhanh)
// turbo
1.  Sử dụng **Newman** để chạy Collection đã chèn test.
2.  Kết hợp biến môi trường `.postman_environment.json`.
3.  Cấu hình xuất báo cáo qua thư viện **htmlextra**.

## 4. Phân tích lỗi (Root Cause Analysis - RCA)
// turbo
1.  Sử dụng script `parse_newman_errors.py` để trích xuất các lỗi từ file `summary.json`.
2.  Tạo bảng đánh giá lỗi (Assessment) dựa trên mã lỗi 4xx (Client), 5xx (Server).

---
## Lệnh thực thi nhanh (Quick Run)
Mở terminal và chạy lệnh:
```bash
./node_modules/.bin/newman run collection.json -e env.json -r htmlextra --reporter-htmlextra-export ./Reports/Report.html
```
