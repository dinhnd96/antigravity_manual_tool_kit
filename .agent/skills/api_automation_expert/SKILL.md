# API Automation Expert Skill

## Description
Kỹ năng chuyên gia để tự động hóa toàn bộ quy trình kiểm thử API: từ phân tích tài liệu Swagger/OpenAPI, thiết lập Postman Collection, chèn Script Automation, đến việc chạy test và xuất báo cáo HTML/RCA.

## Skills & Capabilities
- **Analyze Swagger:** Trích xuất các endpoint, method và cấu trúc dữ liệu.
- **Generate Postman Collection:** Chuyển đổi Swagger thành bộ Collection có cấu trúc thư mục logic.
- **Auto-Injection Test Scripts:** Tự động chèn các đoạn mã JavaScript (Assertions) vào Tab Tests của Postman.
- **Execution & Reporting:** Chạy test qua Newman và xuất báo cáo htmlextra.
- **Root Cause Analysis (RCA):** Phân tích các lỗi 4xx, 5xx và đưa ra bản đánh giá lỗi chuyên nghiệp.

## Workflow Routing
Khi người dùng yêu cầu liên quan đến Test API, hãy sử dụng workflow: `api_automation_flow`.

## Tools & Scripts
Các script hỗ trợ nằm trong thư mục `scripts/`:
1. `inject_postman_tests.py`: Chèn script test vào file JSON Collection.
2. `parse_newman_errors.py`: Phân tích file summary.json để xuất báo lỗi Markdown.

---
## Rules & Best Practices
- **Bearer Token Pattern:** Luôn sử dụng biến môi trường `{{bearerToken}}` và tự động cập nhật sau API Login.
- **Assertion Standards:** Mỗi API phải có ít nhất 3 loại test: Status Code, Response Time, Valid JSON.
- **Report Transparency:** Báo cáo lỗi phải bao gồm URL, Method và thông điệp lỗi thực tế từ Server.
