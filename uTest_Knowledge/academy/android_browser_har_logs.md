# Log HAR trình duyệt trên Android

> **Nguồn gốc**: uTest Academy - Android Browser HAR Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Cách thu thập log HAR trên Android

#### Thiết lập thiết bị di động
1.  Bật **Tùy chọn nhà phát triển (Developer Options)** bằng cách nhấp 7 lần vào **Số bản dựng (Build Number)**.
    *   *Lưu ý: Cách bật tùy chọn này có thể khác nhau tùy theo từng dòng máy Android, bạn có thể tìm kiếm hướng dẫn trực tuyến cho dòng máy cụ thể của mình.*
2.  Mở Tùy chọn nhà phát triển.
3.  Bật tùy chọn **Gỡ lỗi USB (USB Debugging)**.
4.  Nhấn nút **OK** trên cửa sổ thông báo hiện ra.
5.  Kết nối điện thoại với máy tính qua cáp USB.
6.  Chọn bất kỳ tùy chọn kết nối nào hiển thị ở cửa sổ bật lên (popup) trên điện thoại (ví dụ: chuyển tệp, sạc...).

#### Mở DevTools và thu thập Log mạng (Network Logs)
1.  Nhập `chrome://inspect` vào thanh địa chỉ của trình duyệt Chrome trên máy tính và mở địa chỉ này.
2.  Mở trang web kiểm thử trên thiết bị di động của bạn.
3.  Nhấp vào liên kết **Inspect** hiển thị bên dưới phần **Remote Target**.
    *   *Bạn có thể đợi một lát nếu liên kết này chưa hiển thị.*
4.  Trong cửa sổ mới mở ra, chuyển sang tab **Network** (Nếu không thấy, nhấp vào biểu tượng **>>** và chọn tab **Network**).
5.  Tích chọn tùy chọn **Preserve log** (Giữ log) nếu chưa được bật.
6.  Tái hiện lỗi bằng cách tương tác qua màn hình truyền chiếu (screencast) hiển thị trên trang DevTools hoặc sử dụng trực tiếp thiết bị di động của bạn.

#### Lưu Log
1.  Nhấp chuột phải vào phần log đã được tạo ra trong tab Network.
2.  Chọn tùy chọn **Save all as HAR with content** (Lưu tất cả dưới dạng HAR kèm nội dung).
3.  Chọn vị trí lưu tệp tin mong muốn.
4.  Nhập tên tệp và nhấp vào nút **Save** (Lưu) để lưu tệp dưới định dạng `.har`.

#### Loại bỏ thông tin nhạy cảm (PII) khỏi Log
1.  Chỉnh sửa tệp log HAR để loại bỏ thông tin nhạy cảm (PII).
2.  Bạn có thể thực hiện theo các bước chỉnh sửa đã được hướng dẫn chi tiết trong khóa học này.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Screencast | Truyền hình ảnh màn hình (Screencast) | Tính năng phản chiếu màn hình thiết bị di động lên trình duyệt máy tính |
| Build Number | Số bản dựng (Build Number) | Số hiệu phiên bản hệ điều hành trên thiết bị di động |
