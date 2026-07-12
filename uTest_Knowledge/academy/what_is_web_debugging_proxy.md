# Proxy gỡ lỗi web là gì?

> **Nguồn gốc**: uTest Academy - What is a Web Debugging Proxy?
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Proxy gỡ lỗi web (Web Debugging Proxy) là gì?
Proxy gỡ lỗi web là một chương trình hoạt động như một máy chủ proxy (proxy server), cho phép người dùng xem và ghi lại toàn bộ lưu lượng truy cập HTTP/HTTPS giữa thiết bị của người dùng và trang web/ứng dụng kiểm thử trên Internet.

Các tệp log này giúp các lập trình viên chẩn đoán và khắc phục bất kỳ sự cố nào liên quan đến mạng.

Trong khóa học này, chúng ta sẽ tìm hiểu về hai công cụ proxy gỡ lỗi web được sử dụng phổ biến nhất là:
*   Charles Proxy
*   Fiddler

Các chương trình Charles Proxy và Fiddler cho phép người dùng giám sát toàn bộ lưu lượng truy cập HTTP và SSL / HTTPS giữa máy tính của bạn và Internet, giả lập yêu cầu (mock requests), cũng như chẩn đoán các sự cố về mạng.

---

### Yêu cầu đối với log của proxy gỡ lỗi web

*   **Log đã giải mã (Decrypted log)**: Tất cả các lưu lượng truy cập phải được giải mã trong tệp log tải lên.
*   **Trang web/ứng dụng kiểm thử**: Tệp log phải chứa lưu lượng truy cập đến trang web/ứng dụng mà bạn đang kiểm thử.
*   **Định dạng tệp chính xác**: Đảm bảo lưu tệp log đúng định dạng. Định dạng chính xác cho:
    *   **Charles Proxy**: `.chls` hoặc `.chlz`
    *   **Fiddler**: `.saz`

Trong các khóa học tiếp theo, bạn sẽ được học cách thiết lập các chương trình này.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Web Debugging Proxy | Proxy gỡ lỗi web (Web Debugging Proxy) | Chương trình trung gian giúp ghi lại lưu lượng HTTP/HTTPS giữa thiết bị và Internet |
| Proxy Server | Máy chủ proxy (Proxy Server) | Máy chủ trung gian kết nối thiết bị của người dùng với Internet |
| Decrypted Log | Log đã giải mã | Log trong đó dữ liệu HTTPS đã được giải mã thành văn bản thuần túy |
| Mock Requests | Giả lập yêu cầu (Mock requests) | Kỹ thuật giả lập các phản hồi và yêu cầu mạng để kiểm thử |
