# 🔄 QUY TRÌNH KỂM THỬ SHIFT-LEFT (THỰC CHIẾN CHO TEST LEAD)

Tài liệu này hướng dẫn chi tiết các bước **thực thi** chiến lược Shift-Left trong một chu kỳ phát triển phần mềm (SDLC/Agile Sprint), giúp Test Lead đưa team QA tham gia vào quá trình đảm bảo chất lượng từ những ngày đầu tiên.

---

## BƯỚC 1: Giai đoạn Khởi tạo & Phân tích Yêu cầu (Requirements & Analysis)
*Mục tiêu: Bắt lỗi logic, mâu thuẫn nghiệp vụ ngay trên giấy.*

1. **Review URD/BRD/User Story sớm:**
   - QA không chờ đến khi có file chốt cuối cùng. Tham gia đọc tài liệu ngay từ bản Draft.
   - Tập trung tìm kiếm rủi ro, các case ngoại lệ (Edge cases, Error paths) chưa được nhắc đến.
2. **Tham gia Grooming/Refinement Sessions:**
   - Đặt câu hỏi "What if" (Điều gì xảy ra nếu...) để thách thức hệ thống.
   - Đảm bảo mỗi User Story đều có Acceptance Criteria (AC) rõ ràng, có thể test được.
3. **Thống nhất Acceptance Criteria (AC):**
   - Cùng PO/BA chốt AC. Có thể áp dụng BDD (Behavior Driven Development) viết dưới dạng `Given - When - Then`.
- **Đầu ra:** Q&A Log (Danh sách câu hỏi làm rõ), Danh sách AC được duyệt, High-level Test Scenarios.

## BƯỚC 2: Giai đoạn Thiết kế (Design & Architecture)
*Mục tiêu: Đảm bảo thiết kế hệ thống đáp ứng tính dễ kiểm thử (Testability).*

1. **Review API Specs / Database Design:**
   - QA Lead/Senior QA cùng Technical Lead xem xét tài liệu thiết kế API.
   - Kiểm tra xem API có trả về đủ field để verify UI không? Có mã lỗi (Error Code) rõ ràng không?
2. **Lập Kế hoạch Kiểm thử (Test Planning):**
   - Lên chiến lược test, phân bổ nguồn lực. Xác định cần tool nào để test (Postman, JMeter, Katalon, v.v.).
3. **Chuẩn bị Test Data & Môi trường Sớm:**
   - Đề xuất tạo Mock API hoặc chuẩn bị data (tài khoản, số dư, thẻ) ngay lúc này.
- **Đầu ra:** Test Plan (bản nháp), API Test Scenarios, Danh sách Test Data cần chuẩn bị.

## BƯỚC 3: Giai đoạn Phát triển (Development & Coding)
*Mục tiêu: Đảm bảo Developer code đúng hướng và QA có sẵn kịch bản khi code xong.*

1. **Kick-off "The Three Amigos":**
   - BA, Dev, QA họp nhanh 10-15 phút trước khi Dev bắt tay vào code ticket đó để chốt lại hiểu biết về AC.
2. **Viết Test Case chi tiết & Automation Script:**
   - QA viết test case chi tiết hoặc script Automation dựa trên AC và Mock API (không cần đợi UI).
3. **Khuyến khích Unit Test & Peer Review:**
   - Đốc thúc Dev viết Unit Test và review code chéo. QA có thể lấy coverage report để tham khảo.
- **Đầu ra:** Test Cases hoàn chỉnh, Automation Scripts (mức API/UI bằng Mock data), Unit Test Coverage.

## BƯỚC 4: Giai đoạn Tích hợp & Kiểm thử Sớm (Continuous Testing)
*Mục tiêu: Tìm và sửa lỗi ngay trên máy Dev hoặc ngay khi vừa tích hợp.*

1. **Pair Testing / Desk Check (CỰC KỲ QUAN TRỌNG):**
   - Ngay khi Dev code xong chức năng (trên máy Dev/Trunk), QA ngồi cùng Dev khoảng 10-15 phút test các luồng chính (Happy Path). 
   - Sửa ngay lập tức không cần log bug Jira nếu đó là các lỗi hiển nhiên.
2. **Chạy API Test / Unit Test trong CI/CD:**
   - Khi Dev push code, pipeline tự động chạy các bài test Automation đã viết.
- **Đầu ra:** Fix lỗi nhanh chóng, CI/CD Pipeline xanh (Passed). Đưa ticket sang trạng thái Ready for QA/Testing.

## BƯỚC 5: Giai đoạn Kiểm thử Chính thức (System/UAT Testing)
*Ở giai đoạn này khối lượng test tay luồng chính sẽ giảm đáng kể.*

1. **Exploratory Testing (Kiểm thử thăm dò):**
   - Do luồng chính đã được test tự động/Desk Check, QA dùng thời gian để "phá" hệ thống (Test bảo mật cơ bản, permission, UX, luồng dị).
2. **Hỗ trợ UAT:**
   - Hướng dẫn PO/End-User nghiệm thu dựa trên các AC đã chốt từ Bước 1.
- **Đầu ra:** Release Sign-off, Danh sách Known Issues.

---

## 🎯 CHECKLIST TRIỂN KHAI CHO TEST LEAD

Để đưa quy trình này vào team, Test Lead cần thực hiện các hành động sau:
- [ ] Lồng ghép bước **"QA Review Requirement"** và **"Desk Check"** vào Workflow của Jira.
- [ ] Yêu cầu/Thuyết phục Scrum Master hoặc PM cho QA tham gia mọi buổi Refinement.
- [ ] Tạo thói quen viết **Q&A Log** bắt buộc cho mỗi buổi review tài liệu.
- [ ] Hướng dẫn Dev hợp tác trong việc Desk Check.

---
*Tài liệu liên quan:*
- *[Cẩm nang Test Lead Master Guide](./TEST_LEAD_MASTER_GUIDE.md)*
- *[Chiến lược Shift-Left](./SHIFT_LEFT_STRATEGY.md)*
- *[Bộ Biểu Mẫu & Checklist Shift-Left Thực Chiến](./SHIFT_LEFT_TEMPLATES.md)*
