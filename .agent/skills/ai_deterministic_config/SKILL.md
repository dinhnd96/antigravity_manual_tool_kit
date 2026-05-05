---
name: ai_deterministic_config
description: Quy tắc bắt buộc thiết lập Temperature = 0 để loại bỏ tính ngẫu nhiên của AI, đảm bảo kết quả phân tích và sinh Test Case nhất quán, không bị sót kịch bản.
---

### CẤU HÌNH HỆ THỐNG: LOẠI BỎ TÍNH NGẪU NHIÊN CỦA AI (BẮT BUỘC)
Để đảm bảo kết quả phân tích luôn nhất quán, logic và không bị sót case giữa các lần chạy khác nhau, User/Tester **BẮT BUỘC** phải thiết lập thông số của AI ở mức **Temperature = 0** (hoặc mức thấp nhất có thể tùy nền tảng) trước khi bắt đầu phiên làm việc. Điều này loại bỏ hoàn toàn sự "sáng tạo ngẫu nhiên" không cần thiết và ép AI hoạt động theo hướng Deterministic (Tất định).
