# Khái niệm cơ bản về Log

> **Nguồn gốc**: uTest Academy - Basics of Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Log là gì?
Log (nhật ký hoạt động) là các sự kiện hoặc bản ghi được tạo ra bởi trang web hoặc phần mềm khi chúng hoạt động. Lập trình viên (developer) sử dụng log để gỡ lỗi (debugging).

Có nhiều loại log khác nhau. Tại Academy, chúng tôi sẽ hướng dẫn bạn cách thu thập các loại log dưới đây:

*   **Browser console logs (Log console trình duyệt)**: Chứa thông tin liên quan đến trang web như các yêu cầu mạng (network requests), JavaScript, CSS, lỗi bảo mật và cảnh báo. Các log này là bắt buộc khi bạn kiểm thử một trang web.
*   **Mobile device logs (Log thiết bị di động)**: Chứa các sự kiện được gửi bởi hệ thống và các ứng dụng đang chạy trên thiết bị. Các log này là bắt buộc khi bạn kiểm thử ứng dụng di động.
*   **Network logs (Log mạng)**: Ghi lại lưu lượng truy cập HTTP(S) giữa máy tính của bạn và Internet, giúp chẩn đoán các sự cố về mạng. Các log này được yêu cầu trong một số chu kỳ kiểm thử (test cycle).

**Lưu ý**: Trong các khóa học tiếp theo, chúng tôi sẽ hướng dẫn bạn cách thu thập log console trình duyệt và log thiết bị di động. Sau đó, bạn sẽ được học cách thu thập log mạng.

### Những điều cần lưu ý
Dưới đây là một số điểm quan trọng bạn cần ghi nhớ khi thu thập log:

*   **Xóa log cũ**: Kiểm thử viên (tester) cần xóa các log cũ đã lưu trước khi bắt đầu thu thập log mới.
*   **Định dạng tệp**: Bạn phải luôn lưu log dưới định dạng `.txt`.
*   **Tái hiện lỗi trong quá trình thu thập log**: Bạn cần tái hiện lại lỗi (reproduce) trong lúc đang thu thập log. Tệp log phải chứa các hoạt động và lưu lượng truy cập của trang web hoặc ứng dụng mà bạn đang kiểm thử.
*   **Mốc thời gian (Timestamp)**: Đảm bảo tệp log của bạn có hiển thị mốc thời gian. Mốc thời gian hiển thị ở đầu mỗi dòng hoặc bản ghi. Dưới đây là ví dụ minh họa cho một dòng log console trình duyệt và log thiết bị di động. Phần được bôi đậm chính là mốc thời gian:
    *   Browser console log: **23:24:11.174** Navigated to https://www.utest.com/
    *   Mobile device log: **12-10 13:02:50.071** 1901-4229/com.uTest.android.gms

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Log / Logs | Log / Nhật ký hoạt động | Tệp ghi lại các sự kiện hoạt động của phần mềm/hệ thống |
| Browser console logs | Log console trình duyệt | Log ghi lại lỗi JS, CSS, network requests trên trình duyệt |
| Mobile device logs | Log thiết bị di động | Log ghi lại sự kiện hệ thống và app chạy trên thiết bị di động |
| Network logs | Log mạng | Log ghi lại lưu lượng HTTP(S) giữa máy tính và Internet |
| Timestamp | Mốc thời gian / Nhãn thời gian | Nhãn thời gian hiển thị ở đầu mỗi dòng log |
