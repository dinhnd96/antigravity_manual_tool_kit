# 📋 SKILL: Quản Lý Đội Ngũ Kiểm Thử (Test Lead Management)

## Mô tả
Lộ trình 4 tuần chuyên sâu dành cho Test Leader để nâng tầm từ quản lý tác vụ sang quản lý chiến lược, con người và công nghệ.

---

## 🗓️ LỘ TRÌNH HỌC TẬP 4 TUẦN

### 🟦 TUẦN 1: Chiến Lược & Quản Lý Rủi Ro (Strategy & Risk)
*Mục tiêu: Xây dựng nền móng vững chắc cho dự án.*
- **Ngày 1-2:** Phân biệt Test Policy, Test Strategy và Test Plan. Cách viết Chiến lược kiểm thử cho dự án Agile/DevOps.
- **Ngày 3:** Risk-Based Testing (RBT): Nhận diện, phân tích và ưu tiên kiểm thử dựa trên rủi ro.
- **Ngày 4:** Ước lượng (Estimation): Kỹ thuật 3 điểm, T-shirt sizing và lập kế hoạch nguồn lực (Resource Planning).
- **Ngày 5:** Chiến lược "Shift-Left": Cách đẩy hoạt động kiểm thử lên sớm nhất trong chu kỳ phát triển.

### 🟨 TUẦN 2: Quy Trình & Chỉ Số Chất Lượng (Process & Metrics)
*Mục tiêu: Tối ưu hóa vận hành và đo lường hiệu quả.*
- **Ngày 1-2:** STLC trong Agile: Cách phối hợp nhịp nhàng với Sprint, Scrum.
- **Ngày 3:** Defect Management & Triage: Quy trình xử lý lỗi và cách điều phối các buổi họp Triage hiệu quả.
- **Ngày 4:** Metrics that Matter: Defect Density, Test Coverage, Leakage Rate, và ROI của Automation.
- **Ngày 5:** Testing in CI/CD: Hiểu về luồng pipeline và vai trò của QA trong quy trình tự động hóa.

### 🟩 TUẦN 3: Quản Lý Con Người & Lãnh Đạo (People & Leadership)
*Mục tiêu: Xây dựng đội ngũ mạnh và gắn kết.*
- **Ngày 1:** Phân tích kỹ năng (Gaps analysis) và lập kế hoạch đào tạo cho từng thành viên.
- **Ngày 2:** Kỹ năng giao tiếp và quản lý kỳ vọng của Stakeholders (Dev, PO, Khách hàng).
- **Ngày 3:** Quản lý hiệu suất: Thiết lập KPI theo chuẩn SMART và cách phản hồi (Feedback) hiệu quả.
- **Ngày 4:** Giải quyết xung đột trong team và giữa QA - Dev.
- **Ngày 5:** Coaching & Mentoring: Cách giúp Junior vươn lên Senior.

### 🟥 TUẦN 4: Công Nghệ Nâng Cao & Tương Lai (Advanced Tech & Future)
*Mục tiêu: Đón đầu xu hướng và tối ưu hóa bằng công cụ.*
- **Ngày 1-2:** Automation Strategy: Lập lộ trình tự động hóa, chọn công cụ (Playwright, Selenium, Appium) và tính toán điểm hòa vốn.
- **Ngày 3:** AI in Testing: Sử dụng LLMs (như Antigravity) để sinh dữ liệu test, viết test case và phân tích log lỗi.
- **Ngày 4:** Quality Engineering (QE): Chuyển đổi tư duy từ "kiểm tra lỗi" sang "đảm bảo chất lượng hệ thống".
- **Ngày 5:** Tổng kết, thực hành lập Kế hoạch Chiến lược cho năm tới.

---

## 🏢 PHÂN BIỆT TEST POLICY - STRATEGY - PLAN

Đây là 3 tầng tài liệu quan trọng để quản lý chất lượng ở quy mô lớn:

| Loại tài liệu | Mục tiêu | Nội dung chính | Tần suất thay đổi |
|---|---|---|---|
| **Test Policy** (Chính sách) | Tầm nhìn dài hạn | Sứ mệnh chất lượng của công ty ("Automation là trọng tâm", "Zero tolerance for security bugs"). | Rất ít (nhiều năm) |
| **Test Strategy** (Chiến lược) | Phương pháp luận | Cách tiếp cận cho dự án cụ thể (Công cụ như Katalon, Môi trường, Tỷ lệ Automation). | Theo dự án (6-12 tháng) |
| **Test Plan** (Kế hoạch) | Phân bổ thực thi | Lịch trình chi tiết theo Sprint, ai làm tính năng gì, thời hạn bàn giao. | Thường xuyên (mỗI Sprint) |

---

## 🏃 CHIẾN LƯỢC KIỂM THỬ CHO AGILE / DEVOPS (BANK FEE)

Trong dự án nhạy cảm như **Quản lý phí Ngân hàng**, chiến lược phải tập trung vào tốc độ và độ chính xác:

### 🎯 Các điểm mấu chốt:
1.  **Shift-Left:** QA tham gia ngay từ lúc PO viết User Stories để bắt lỗi logic sớm.
2.  **Katalon Automation Strategy (Bậc thang):**
    - P0 (Smoke): Luôn chạy tự động mỗi khi có code mới.
    - P1 (Regression): Chạy tự động hàng đêm để bảo vệ các logic tính phí cũ.
    - Manual: Dành cho UI mới hoặc các Edge cases cực khó.
3.  **Definition of Done (DoD) chuẩn Ngân hàng:**
    - 0 lỗi P0/P1.
    - 100% P0 kịch bản Katalon phải pass.
    - Release Notes có chữ ký xác nhận của Product Owner.

### 🤖 Testing trong kỷ nguyên Cách mạng AI
- **Sử dụng AI để bứt phá:** Dùng AI (như Antigravity) để sinh test data khổng lồ và audit chất lượng kịch bản test.
- **Tập trung vào Business Logic:** AI có thể test nhanh, nhưng bạn là người hiểu vì sao biểu phí đó lại quan trọng.
- **Dẫn dắt 20 tester:** Chuyển đổi team dần sang hướng **Quality Engineering (QE)** thay vì chỉ manual đơn thuần.

---

## 💡 Tư Duy Cốt Lõi Của Một Test Leader
1. **Chất lượng là trách nhiệm tập thể**, không phải của riêng QA.
2. **Ưu tiên giá trị kinh doanh:** Tập trung vào những gì quan trọng nhất với người dùng.
3. **Luôn học hỏi:** Công nghệ QA (AI, Automation) thay đổi hàng ngày, hãy luôn tò mò.
