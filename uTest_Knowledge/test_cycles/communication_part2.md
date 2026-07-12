# Giao Tiếp Trong Test Cycle (Phần 2)

> **Nguồn gốc**: uTest Academy — Communication
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Kênh Chat Dự Án (Project Chat Channel)

Kênh Chat Dự Án uTest cho phép đội Vận Hành Khách Hàng (Customer Operations) giao tiếp dễ dàng về công việc dự án với tester cộng đồng mà không cần phụ thuộc vào công cụ bên thứ ba.

### Mục đích của Project Chat là gì?

Các dự án kiểm thử thường trải dài qua nhiều test cycle hoặc cần phối hợp với tester trước khi bắt đầu. Kênh Chat Dự Án sẽ hỗ trợ giao tiếp về dự án **ngoài phạm vi** của một test cycle cụ thể.

### Làm sao để tìm Project Chat Channel?

Tester đã được mời tham gia Kênh Chat Dự Án sẽ tìm thấy kênh trong mục **Projects** phía trên phần Active Test Cycle trong thanh điều hướng bên trái của uTest Chat.

[Hình: Vị trí Project Chat Channel trong thanh điều hướng bên trái]

---

## Tab Tin Nhắn (Messages Tab)

Tab Messages có thể được sử dụng để giao tiếp với TTL, TE, TSM, hoặc khách hàng trong các báo cáo lỗi (issue reports), test case, và đánh giá (reviews).

TTL, TE, TSM, hoặc khách hàng có thể khởi tạo giao tiếp trong tab Messages bằng cách gửi tin nhắn cho tester. Tester sẽ nhận được **thông báo qua email** khi có tin nhắn mới trong báo cáo lỗi, test case, hoặc đánh giá.

> ⚠️ **Lưu ý quan trọng:** Hãy giao tiếp **chuyên nghiệp** với TTL, TE, TSM và khách hàng. Nếu muốn tranh luận một lỗi bị từ chối không chính xác, bạn **phải** sử dụng tính năng **Dispute** (không bao giờ dùng tab Messages để tranh luận hoặc yêu cầu khách hàng phê duyệt lỗi).

### Cách trả lời tin nhắn:

1. Đăng nhập vào nền tảng uTest
2. Mở báo cáo lỗi, test case, hoặc đánh giá đã nhận tin nhắn

[Hình: Giao diện mở issue report/test case/review trên uTest]

3. Nhấp vào tab **Messages** (Kiểm tra mục Messages đối với reviews)

[Hình: Vị trí tab Messages trong giao diện]

4. Nhấp nút **New Message**
5. Viết câu trả lời trong ô văn bản
6. Nhấp nút **Add** để gửi phản hồi

[Hình: Form gửi tin nhắn mới trong tab Messages]

---

## Thư Điện Tử (Email)

Email chỉ nên được sử dụng khi:
- Có vấn đề **khẩn cấp** (ví dụ: không truy cập được chat hoặc gặp lỗi khi nhận suất tham gia cycle)
- Vấn đề **nhạy cảm** (liên quan đến vi phạm hành vi của tester khác hoặc vấn đề thanh toán)
- Bạn **không nhận được phản hồi** trong cycle chat trong thời gian hợp lý
- Được hướng dẫn trong mục Thông Tin Liên Hệ Nhóm (Team Contact Information) để escalate lên TE hoặc TSM qua email

> **Lưu ý:** TE và TSM thường rất bận xử lý test cycle, và có thể mất thời gian để trả lời. Các câu hỏi liên quan đến cycle cần được gửi cho **TE trước**, nếu không nhận phản hồi trong thời gian quy định, bạn có thể escalate lên **TSM** bằng cách chuyển tiếp (forward) tin nhắn. Email TE và TSM có trong mục Team Contact Information của cycle overview.

### Khi nào liên hệ TE hoặc TSM:

- ✅ Nghi ngờ tester vi phạm hành vi:
  - Tester sao chép công việc của tester khác
  - Tester nộp bug giữ chỗ (placeholder)
  - Tester sử dụng nhiều tài khoản
- ✅ Vấn đề thanh toán (payout)
- ✅ Vấn đề giao tiếp với khách hàng (khi khách hàng gửi tin nhắn trong issue reports)
- ✅ Câu hỏi nhạy cảm về test cycle mà bạn muốn trao đổi riêng
- ✅ Câu hỏi trong chat không được trả lời **quá 24 giờ**
- ✅ Chưa nhận phản hồi trong thời gian quy định tại mục Team Contact Information

### KHÔNG liên hệ TE và TSM trong các trường hợp:

- ❌ Lỗi bị từ chối và muốn giải thích thêm → Dùng tùy chọn **"Dispute Rejection"** nếu bạn cho rằng lỗi hợp lệ
- ❌ Câu hỏi về phạm vi và hướng dẫn cycle → Dùng **cycle chat**
- ❌ Câu hỏi chung về uTest, như cách nộp báo cáo lỗi → Xem **các khóa học Academy**

### Hướng dẫn viết Email:

- **Tiêu đề email:** Ghi rõ **Test Cycle ID** kèm mô tả ngắn gọn vấn đề
- **Nội dung email:** Mô tả vấn đề/câu hỏi **ngắn gọn và chính xác**, bao gồm đầy đủ thông tin để giải quyết nhanh
- Luôn giữ giao tiếp **chuyên nghiệp** và **lịch sự**

---

## Thực Hành Tốt Nhất (Best Practices)

1. **Đọc tất cả hướng dẫn** được cung cấp trong cycle và hỏi trong cycle chat nếu có thắc mắc
2. **Tuân thủ Điều Khoản Sử Dụng** của uTest trước khi gửi tin nhắn và không vi phạm Quy tắc & Hướng dẫn
3. **Không tạo nhiễu** — Kiểm tra tất cả các chuỗi tin nhắn (threads) trước khi gửi câu hỏi để tránh lặp lại
4. **Không hỏi về thanh toán** trong cycle chat hoặc tab Messages (chuyển câu hỏi cho Project Manager)
5. Luôn **chuyên nghiệp** và **tôn trọng** mọi người

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Project Chat Channel | Kênh Chat Dự Án | Giao tiếp ngoài test cycle |
| Customer Operations | Vận Hành Khách Hàng | Đội quản lý khách hàng |
| Messages Tab | Tab Tin Nhắn | Trong issue reports/test cases/reviews |
| Dispute | Tranh luận / Khiếu nại | Tính năng phản đối kết quả review |
| Forward (email) | Chuyển tiếp | Khi cần escalate từ TE lên TSM |
| Placeholder Issue | Bug giữ chỗ | Bị cấm — phải nộp hoàn chỉnh |
| Multiple Accounts | Nhiều tài khoản | Vi phạm nghiêm trọng |
| Noise (in chat) | Nhiễu (trong chat) | Tin nhắn thừa, lặp lại |
| Escalation | Báo cáo lên cấp trên | Chuyển vấn đề từ TTL → TE → TSM |
