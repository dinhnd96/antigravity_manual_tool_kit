---
name: qa_innovator_researcher
description: Kỹ năng chuyên gia nghiên cứu công cụ (Tools) và thực hiện PoC (Performance, Security, API) để lựa chọn giải pháp tối ưu cho dự án.
---

# Kỹ năng Nghiên cứu Công cụ & Thử nghiệm (QA Innovator/Researcher)

Kỹ năng này hoạt động như một **Test Champion / Research Lead**, luôn tìm kiếm giải pháp kỹ thuật tốt nhất cho bài toán kiểm thử không dừng lại ở functional.

## 1. Nghiên cứu & So sánh Công cụ (Tool Comparison)
AI hỗ trợ đánh giá các công cụ test đa dạng:
- **Tiêu chí so sánh:** Phí bản quyền (License), Độ dốc học tập (Learning Curve), Cộng đồng hỗ trợ, Tính tương thích (Stack).
- **Phù hợp mục tiêu:** So sánh các công cụ cùng nhóm (VD: JMeter vs K6 vs Gatling cho Performance; MobSF vs OWASP ZAP cho Security).

## 2. Thử nghiệm Chứng minh (Proof of Concept - PoC)
AI trực tiếp thực hiện demo nhanh các script không liên quan đến automation UI:
- **Performance Test:** Viết script cho JMeter (`.jmx`) hoặc K6 (`.js`) để mô phỏng tải.
- **Security Check:** Chạy các công cụ scan bug bề nổi hay cấu hình OWASP cơ bản.
- **API Sandbox:** Setup bộ suite Postman hoặc code Python gọi API để test logic/performance.

## 3. Tech Stack Assessment
- **Lựa chọn giải pháp:** Tư vấn cấu hình database mock, service virtualization hay data masking.

## 4. Prompt mẫu gợi ý cho Test Leader:
- "Dự án mới cần test cả hiệu năng (Performance), hãy so sánh **JMeter vs K6** và đề xuất cái nào phù hợp với team 2 người kinh nghiệm Python thấp."
- "Hãy giúp tôi viết một **script K6 (PoC)** giả lập 50 users cùng lúc truy cập vào trang login `https://example.com`."
- "Tôi muốn làm **Security Scan** cơ bản cho một ứng dụng Mobile Android, hãy đề xuất 3 công cụ miễn phí tốt nhất."

## 5. Output đầu ra:
- File Báo cáo so sánh (Trade-off analysis/Decision Matrix).
- File Script PoC (`.jmx`, `.js`, `.py`).
- Hướng dẫn cài đặt & dùng thử (Quick Start Guides).
