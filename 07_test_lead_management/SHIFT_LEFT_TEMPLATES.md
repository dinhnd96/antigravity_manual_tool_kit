# 📋 BỘ BIỂU MẪU & CHECKLIST THỰC THI SHIFT-LEFT

Để áp dụng quy trình Shift-Left vào thực tế, Test Lead và QA team có thể sử dụng trực tiếp các biểu mẫu dưới đây trong công việc thiết kế và kiểm thử hàng ngày.

---

## 1. MẪU Q&A LOG (Cho Giai đoạn Review Requirement)
*Sử dụng file Excel, Google Sheets, hoặc trực tiếp trên Confluence trang tài liệu dự án.*

| ID | Ticket / Chức năng | Câu hỏi / Vấn đề của QA (Issue/Query) | Người trả lời (BA/PO) | Câu trả lời (Answer) | Trạng thái (Status) | Ngày giải quyết |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| Q01 | SE01 - Login | Mật khẩu nhập sai 5 lần thì có block tài khoản không? Nếu block thì bao lâu mở lại? | @BA_Name | Có, block 30 phút. Hoặc liên hệ Admin để mở ngay. | 🟢 Closed | 27/03 |
| Q02 | SE02 - API Thanh toán | API Partner lỗi 500 thì giao dịch ở trạng thái "Pending" hay "Failed"? Có cơ chế retry không? | @Technical_Lead | Trạng thái Failed, không auto retry. Cần báo User. | 🟢 Closed | 27/03 |
| Q03 | PR01 - Phí giao dịch | Nếu phí tính ra là số thập phân (VD: 10.55 VNĐ) thì làm tròn lên hay làm tròn xuống? | @PO_Name | Làm tròn lên theo chuẩn toán học (>=.5 lên). | 🟢 Closed | 28/03 |

> **💡 Mẹo cho Test Lead:** Dùng Q&A Log này để chứng minh với các bên rằng QA đã giúp ngăn chặn bao nhiêu "lỗ hổng" thiết kế trước khi code.

---

## 2. CHECKLIST HỌP "THE THREE AMIGOS" (QA + BA + DEV)
*Cuộc họp ngắn 15 phút, QA là người điều phối (Facilitator).*

**A. Chuẩn bị trước cuộc họp (QA):**
- [ ] Đọc kỹ ticket/User Story và Acceptance Criteria (AC).
- [ ] List sẵn các case Happy Path (Luồng chuẩn) và Unhappy Path (Ngoại lệ).
- [ ] Chuẩn bị sẵn vài câu hỏi "What if?".

**B. Kịch bản trong cuộc họp:**
1. **BA trình bày (3 phút):** Nhắc lại mục tiêu của ticket và luồng AC chính.
2. **QA & Dev thảo luận (10 phút):**
   - QA: *"Luồng chính chạy như thế này đúng không? Nếu mạng chập chờn lúc gọi API này thì sao?"*
   - Dev: *"Tôi sẽ handle lỗi timeout, trả về message X."*
   - QA: *"Data test cho case này tôi sẽ dùng account loại A. Anh nghĩ account loại B có bị ảnh hưởng không?"*
   - Dev: *"Không, logic chỉ rẽ nhánh với account A."*
3. **Chốt lại (2 phút):** Cả 3 thống nhất kết quả. Nếu có điểm mờ, cập nhật ngay vào ticket Jira/AC.

---

## 3. CHECKLIST "DESK CHECK" (CẶP QA - DEV)
*QA mang máy tính hoặc trực tiếp sang máy Dev để test ngay khi code vừa xong (hoặc lúc đang chạy máy ảo Local).*

**Thỏa thuận trước khi Pair-Testing:**
- [ ] Nhắc Dev: *"Anh/em code xong luồng happy path thì gọi em qua ngó thử nhé, khoan dồn cục lại đẩy 1 lần!"*

**Các bước Desk Check (5-10 phút):**
- [ ] **Mở Ticket/AC:** QA mở sẵn danh sách Acceptance Criteria.
- [ ] **Test Demo:** Dev demo trực tiếp trên máy luồng chức năng vừa code.
- [ ] **Luồng Ngoại Lệ Nhanh:** QA yêu cầu Dev nhập vài data sai cơ bản (VD: nhập chữ vào ô số, click 2 lần nút Submit, ngắt mạng thử).
- [ ] **Console/Log:** Yêu cầu Dev bật DevTools (F12) hoặc Log Server. *"Cho em xem log lúc API này bắn ra lỗi đi."*
- [ ] **Quyết định:**
  - Lỗi nhỏ / Hiển thị sai: Dev sửa luôn tại chỗ, không cần log bug Jira.
  - Lỗi logic nghiêm trọng cần sửa lâu: QA ghi chú, Dev tách ra sửa sau.
  - Pas: Đẩy code tiếp lên nhánh Test cho CI/CD chạy tiếp.

---

## 4. CHECKLIST REVIEW CODE/AUTOMATION (DÀNH CHO ĐỒNG NGHIỆP TRONG QA TEAM)
*Là Test Lead, bạn dùng checklist này để review script Automation của các bạn Junior.*

- [ ] Automation Script đã cover 100% P0 (Luồng chính/Happy Path) chưa?
- [ ] Khởi tạo data (Setup) và Xóa data (Teardown) có độc lập không, hay làm rác database?
- [ ] Selector/Locator có dùng thuộc tính ổn định (`id`, `data-testid`) thay vì cấu trúc lỏng lẻo (`XPath dài`) không?
- [ ] Assertions (Hàm kiểm tra kết quả) có verify cả status code (API) lẫn Dữ liệu database không, hay chỉ check UI hiển thị "Thành công"?
- [ ] Báo cáo (Report) có mô tả rõ ràng lỗi ở đâu để Dev đọc hiểu ngay không?

---
*Các tài liệu được liên kết: [Quy trình Shift-Left Thực Chiến](./SHIFT_LEFT_PROCESS.md) | [Chiến lược Shift-Left](./SHIFT_LEFT_STRATEGY.md)*
