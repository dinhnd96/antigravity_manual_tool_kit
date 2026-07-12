# Xác minh sửa lỗi (Bug Fix Verification)

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Bug Fix Verification (BFV) là gì?
Bug Fix Verification (BFV) — Xác minh sửa lỗi — là quy trình xác minh xem một lỗi (issue) đã được báo cáo có thực sự được sửa hay chưa khi bản sửa lỗi hoặc bản build mới của sản phẩm được phát hành. Applause cho phép khách hàng chạy kiểm thử lại (re-test) khi có bản build mới chứa các bản sửa cho những lỗi đó, nhằm xác minh hiệu quả rằng lỗi đã được khắc phục.

Khi bạn nhận được yêu cầu xác minh xem một lỗi (issue) cụ thể đã được sửa hay chưa:

1. Đảm bảo nhận (claim) và thực thi test case BFV với **cùng môi trường** đã báo cáo lỗi.
2. Xem xét hướng dẫn BFV và các tệp đính kèm có sẵn.
3. Kiểm tra xem lỗi (issue) vẫn còn tồn tại trong phiên bản build mới hay đã được sửa.
4. Nếu lỗi **đã được sửa**: Đánh dấu bước đó là **Pass** và cung cấp tệp đính kèm cần thiết để chứng minh.
5. Nếu lỗi **vẫn còn tái hiện được**: Đánh dấu bước đó là **Fail** và viết giải thích rõ ràng kèm theo tệp đính kèm theo yêu cầu.

### Cách nhận (claim) một BFV Test Case
1. Đọc kỹ tổng quan cycle (cycle overview) và chấp nhận lời mời.
2. Nhấp vào tab **Test Cases**.
3. Cuộn xuống phần **Available Test Cases** (Các Test Case khả dụng).
4. Nhấp vào liên kết **Claim** cho BFV bạn muốn nhận.

### Lưu ý:
- Bạn cũng có thể xem trước BFV trước khi nhận bằng cách nhấp vào liên kết **Preview** (Xem trước).
- Nếu bạn không thể thấy tab **Test Cases** hoặc BFV trong tab đó, điều đó có nghĩa là bạn không đủ điều kiện cho BFV này — hãy kiểm tra với TTL/TE nếu đây là điều ngoài dự kiến.
- Khi khách hàng yêu cầu xác minh issue bằng tính năng Bug Fix Verification, một cột mới có tên **Verification** (Xác minh) sẽ được thêm vào trang danh sách issues. Trạng thái **Requested** (Đã yêu cầu) cho biết issue đã được chọn để xác minh và một BFV test case đã được tạo cho nó, hiện đang khả dụng cho tester trong tab **Test Cases**.
- Các BFV test case có thể được liên kết với slot. Trong trường hợp này, bạn có thể nhận chúng từ tab **Slots** nếu bạn đáp ứng các yêu cầu.

Khi một tester nhận BFV test case, trạng thái trong cột **Verification** sẽ chuyển thành **Started** (Đã bắt đầu), cho biết rằng một tester đã nhận và bắt đầu thực hiện.

### Những điều cần ghi nhớ
- Trong hầu hết các trường hợp, BFV test case sẽ có tên cụ thể như **"Fix Verification for bug: ____"** bao gồm ID lỗi đã báo cáo cần được xác minh.
- Các BFV test case đã nhận sẽ bị **tự động hủy nhận** nếu không được nộp trong vòng **2 giờ**, sau đó bất kỳ tester nào đủ điều kiện đều có thể nhận lại.
- Các BFV test case bị **Fail** sẽ yêu cầu bình luận (comment) trước khi nộp — tester sẽ không thể nộp mà không bao gồm bình luận. Điều này giúp TTL/TE dễ dàng hiểu lý do BFV bị Fail.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Bug Fix Verification (BFV) | Xác minh sửa lỗi | Quy trình kiểm tra lại lỗi đã được sửa chưa |
| Verification (column) | Xác minh (cột) | Cột trạng thái BFV trên trang danh sách issues |
| Requested (status) | Đã yêu cầu | Trạng thái BFV: issue đã được chọn để xác minh |
| Started (status) | Đã bắt đầu | Trạng thái BFV: tester đã nhận và bắt đầu thực hiện |
| Re-test | Kiểm thử lại | Thực thi lại test trên bản build mới |
| Build | Phiên bản (bản build) | Version sản phẩm đang được kiểm thử |
