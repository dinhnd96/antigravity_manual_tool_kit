# Báo Cáo (Reporting)

> **Nguồn gốc**: uTest Academy – Reporting
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### Kiểm thử (Testing)

Như chúng ta đã biết, kiểm thử (testing) là quá trình đánh giá sản phẩm để tìm ra lỗi (defect). Trong phần trước, chúng ta đã thảo luận về kiểm thử. Khi bạn bắt đầu kiểm thử, bạn có thể phát hiện một bug cần báo cáo, hoặc bạn cần thực thi một test case đã được nhận — trong khóa học này, chúng tôi sẽ hướng dẫn cách thực hiện các việc đó.

### Báo cáo (Reporting)

Báo cáo là khi tester gửi thông tin về ứng dụng, trang web hoặc sản phẩm trong một chu kỳ kiểm thử (test cycle). Có **bốn phương thức** nộp báo cáo:

1. **Báo cáo lỗi (Bug Reports)**
2. **Trường hợp kiểm thử (Test Cases)**
3. **Đánh giá ứng dụng (App Reviews)**
4. **Nghiên cứu khả dụng (Usability Studies)**

---

### 1. Nộp Báo cáo lỗi (Submitting a Bug Report)

Thực hiện các bước sau khi viết báo cáo lỗi trong một test cycle:

1. **Tái hiện lỗi để xác minh** — Đảm bảo bạn có thể làm lại lỗi đó trước khi nộp.
2. **Xác minh lỗi là duy nhất** bằng cách kiểm tra danh sách các vấn đề đã được báo cáo (reported issues).

   > 💡 Tham khảo phần **Tổng quan (Overview)** của cycle để biết hướng dẫn báo cáo cụ thể.

3. **Chuẩn bị tệp đính kèm bắt buộc** — bao gồm: ảnh chụp màn hình (screenshot), log trình duyệt (browser logs), log Charles Proxy, v.v.
4. **Nhấn vào biểu tượng "Report Issue"** (Báo cáo vấn đề) trong thanh tiêu đề của test cycle.

   > [Hình: Biểu tượng Report Issue trên thanh tiêu đề test cycle]

5. **Điền biểu mẫu báo cáo lỗi**, kiểm tra lại nội dung và **nhấn Submit** (Gửi).

   > [Hình: Biểu mẫu báo cáo lỗi đã điền đầy đủ]

---

### 2. Nộp Trường hợp kiểm thử (Submitting a Test Case)

Thực hiện các bước sau khi nộp test case trong một test cycle:

1. **Thực hiện tất cả các bước trong test case** và tải lên các tệp đính kèm bắt buộc theo mô tả.

   > [Hình: Các bước test case với phần tải tệp đính kèm]

2. **Nhấn "Pass"** nếu bạn **không gặp lỗi** khi thực hiện bước đó.

   > [Hình: Nút Pass trong giao diện test case]

3. **Nhấn "Fail"** nếu bạn **gặp lỗi** khi thực hiện bước đó.

   > [Hình: Nút Fail trong giao diện test case]

4. **Nếu lỗi đã được tester khác báo cáo trước đó** → điền ID của lỗi đó vào trường **Actual Result** (Kết quả thực tế) rồi nhấn **Fail**.

   > [Hình: Điền Bug ID vào trường Actual Result]

5. **Nếu lỗi chưa được ai báo cáo** → nhấn **"Fail & Report Issue"** (Fail và Báo cáo vấn đề), sau đó điền biểu mẫu báo cáo lỗi và nhấn submit.

   > [Hình: Nút Fail & Report Issue và biểu mẫu]

6. **Kiểm tra lại tất cả các bước** — đảm bảo mọi thứ chính xác.
7. **Nhấn "Submit Results"** (Nộp kết quả), nhập thời gian đã dành (spent time) và nhấn **Finish** (Hoàn tất).

   > [Hình: Nút Submit Results và hộp thoại nhập thời gian]

8. **Đọc tin nhắn từ TTL** nếu test case của bạn có tin nhắn, và **phản hồi nhanh chóng**.

---

### 3. Nộp Đánh giá (Submitting a Review)

Thực hiện các bước sau khi viết đánh giá trong một test cycle:

1. Sau khi hoàn tất việc báo cáo lỗi, mở tab **Review** và viết đánh giá về sản phẩm.

   > [Hình: Tab Review trong giao diện test cycle]

2. **Đảm bảo phản hồi đầy đủ** — tất cả các trường phải có câu trả lời hoàn chỉnh, được viết rõ ràng, để đánh giá thực sự hữu ích cho khách hàng (customer).

   > [Hình: Biểu mẫu Review đã được điền đầy đủ]

---

### 4. Nộp Nghiên cứu khả dụng (Submitting a Usability Study)

Thực hiện các bước sau khi nộp nghiên cứu khả dụng (usability study):

1. **Đọc kỹ các yêu cầu** — có thể tìm thấy trong phần Overview, tab Slots hoặc mô tả Slot.

   > [Hình: Yêu cầu nghiên cứu khả dụng trong Overview]

2. **Cung cấp câu trả lời đầy đủ và chi tiết** cho tất cả các câu hỏi khảo sát (survey questions).

   > [Hình: Các câu hỏi khảo sát cần trả lời]

3. **Tường thuật (narration) đầy đủ** cho tất cả các video.
4. Khi hoàn tất, nhấn nút **"Study Complete"** để nộp bài.

   > [Hình: Nút Study Complete]

5. **Tải lên ảnh chụp màn hình hoặc video bắt buộc**.

   > [Hình: Giao diện tải lên tệp đính kèm]

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Reporting | Báo cáo | Quy trình nộp thông tin trong test cycle |
| Bug Report | Báo cáo lỗi | Một trong 4 loại báo cáo trên uTest |
| App Review | Đánh giá ứng dụng | Đánh giá tổng quan về sản phẩm |
| Usability Study | Nghiên cứu khả dụng | Loại test cycle đặc biệt |
| Narration | Tường thuật | Lời dẫn giải trong video usability study |
| Pass | Đạt | Bước test case không có lỗi |
| Fail | Không đạt | Bước test case phát hiện lỗi |
| Fail & Report Issue | Fail và Báo cáo vấn đề | Khi bug chưa được ai report trước |
| Submit Results | Nộp kết quả | Bước cuối khi hoàn tất test case |
| Spent Time | Thời gian đã dành | Nhập trước khi finish test case |
| Survey Questions | Câu hỏi khảo sát | Trong usability study |
| Study Complete | Hoàn tất nghiên cứu | Nút nộp bài usability study |
| Charles Proxy | Charles Proxy | Công cụ ghi log mạng, giữ nguyên |
| Browser Logs | Log trình duyệt | Tệp đính kèm khi báo lỗi |
