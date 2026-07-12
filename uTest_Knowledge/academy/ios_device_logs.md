# Log thiết bị iOS

> **Nguồn gốc**: uTest Academy - iOS Device Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Bạn có thể thu thập log thiết bị iOS bằng bất kỳ máy tính chạy Windows hoặc macOS nào.

Có nhiều phần mềm quản lý thiết bị iOS có tính năng hiển thị log console, nhưng bạn nên thử sử dụng **iMazing** vì công cụ này hoạt động trên cả Windows và macOS. Nếu bạn sở hữu máy Mac (macOS), bạn cũng có thể thử phương pháp thứ hai.

---

### Phương pháp 1: iMazing (Windows và macOS)

1.  Mở trang web: https://imazing.com/download
2.  Tải xuống phiên bản phần mềm tương ứng với hệ điều hành của bạn (Windows hoặc macOS) và cài đặt nó.
3.  Mở phần mềm iMazing và kết nối thiết bị iOS với máy tính.
4.  Nhấp vào tùy chọn **Show Device Console** bên trong giao diện iMazing.
5.  Xóa sạch console và bắt đầu quá trình tái hiện lỗi.
6.  Sau khi hoàn tất, nhấp vào **Pause** (Tạm dừng), sau đó nhấp vào **Save** (Lưu).
7.  Lưu tệp tin dưới định dạng mở rộng `.txt`.
8.  Tải tệp log này lên báo cáo lỗi của bạn.

*Lưu ý: Ứng dụng này được sử dụng miễn phí cho mục đích cá nhân và giáo dục, nhưng không miễn phí cho mục đích thương mại. Tùy thuộc vào trường hợp sử dụng cụ thể của mình, bạn có thể cần phải mua giấy phép bản quyền. Mỗi người dùng chịu trách nhiệm đảm bảo việc sử dụng phần mềm này tuân thủ các điều khoản trong thỏa thuận cấp phép người dùng cuối (EULA).*

*Mẹo: Hai ứng dụng thay thế khác cho iMazing là 3uTools và iTools, nhưng hãy nhớ rằng những ứng dụng này chỉ hỗ trợ trên hệ điều hành Windows. Bạn có thể sử dụng phương pháp thứ hai dưới đây nếu bạn đang sử dụng hệ điều hành macOS và phương pháp đầu tiên không hoạt động.*

---

### Phương pháp 2: Ứng dụng Console (Chỉ dành cho macOS)

1.  Kết nối thiết bị iOS với máy tính chạy macOS của bạn bằng cáp kết nối.
2.  Trên máy Mac, mở ứng dụng **Console** (Ứng dụng giám sát hệ thống).
3.  Chọn thiết bị iOS của bạn từ danh sách thiết bị hiển thị ở cột bên trái.
4.  Đảm bảo bạn đang ở tab **All messages** (Tất cả tin nhắn), xóa sạch các log cũ bằng cách nhấp vào nút **Clear** (Xóa) ở thanh công cụ phía trên.
5.  Tái hiện lỗi trên thiết bị iOS của bạn.
6.  Nhấn tổ hợp phím **Command+A** để chọn toàn bộ log, sau đó nhấn **Command+C** để sao chép.
7.  Mở ứng dụng **TextEdit** trên máy Mac, truy cập Preferences (Cài đặt) của nó và thay đổi định dạng mặc định sang **plain text** (văn bản thuần túy).
8.  Tạo một tài liệu mới và nhấn tổ hợp phím **Command+V** để dán toàn bộ log đã sao chép vào.
9.  Lưu tệp dưới định dạng `.txt` và tải tệp lên báo cáo lỗi của bạn.

---

### Phương pháp 3: libimobiledevice (Chỉ dành cho Linux)

1.  Tải xuống và cài đặt công cụ **libimobiledevice** trên hệ thống của bạn.
2.  Sử dụng cáp USB để kết nối thiết bị iOS với máy tính chạy Linux.
3.  Nhấp chuột phải vào thư mục Desktop và chọn **Open terminal here** (Mở Terminal tại đây).
4.  Sử dụng lệnh `tee` để ghi và lưu log vào tệp:
    `idevicesyslog | tee uTest_log.txt`
5.  Trên thiết bị iOS, tái hiện lỗi từ đầu đến cuối.
6.  Nhấn tổ hợp phím **Ctrl + C** để dừng quá trình ghi log hoặc đóng cửa sổ Terminal.
7.  Tải tệp log `uTest_log.txt` này lên báo cáo lỗi của bạn.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Console App | Ứng dụng Console (Console App) | Ứng dụng quản lý hệ thống và xem log mặc định trên macOS |
