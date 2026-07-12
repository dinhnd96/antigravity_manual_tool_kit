# Hướng dẫn quay màn hình trên Android

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Hệ điều hành Android từ phiên bản 11 trở đi đã được tích hợp sẵn tính năng quay màn hình, cho phép bạn ghi lại các lỗi (bugs) của hệ thống mà không cần sử dụng ứng dụng bên thứ ba. Ngoài ra, nhiều nhà sản xuất thiết bị (như Samsung hoặc Xiaomi) cũng trang bị sẵn công cụ quay màn hình riêng của họ trên các dòng máy khác nhau, bạn có thể tìm thấy tính năng này trong bảng thông báo (notification panel) hoặc trong mục cài đặt.

Nếu thiết bị Android của bạn có sẵn công cụ quay màn hình tích hợp, bạn có thể sử dụng nó, chỉ cần đảm bảo:
- Các video được lưu ở định dạng **.mp4**.
- Các video không chứa bất kỳ tiếng ồn nền (background noise) nào.

Nếu thiết bị Android của bạn không có công cụ quay màn hình tích hợp sẵn, có rất nhiều ứng dụng quay màn hình bên thứ ba trên cửa hàng ứng dụng mà bạn có thể trải nghiệm, chẳng hạn như **AZ Screen Recorder**, **Mobizen Screen Recorder**.

---

### Cách sử dụng ứng dụng AZ Screen Recorder

- Tải xuống và cài đặt ứng dụng **AZ Screen Recorder** từ cửa hàng ứng dụng Google Play.
- Mở ứng dụng lên và cấp đầy đủ các quyền truy cập hệ thống mà ứng dụng yêu cầu.
- Mở trang cài đặt (settings) của ứng dụng và tắt tính năng **Record audio** (Ghi âm thanh).
- Quay lại giao diện chính và bắt đầu quay bằng cách chạm vào biểu tượng ghi hình (record icon).
- Dừng quay màn hình bằng cách chạm vào nút dừng ghi hình (stop recording button).
- Bạn có thể tìm thấy các video đã quay trong thư mục `AZRecorderFree` bên trong trình quản lý tệp tin (file manager) của thiết bị.

---

### Mẹo: Bật tính năng hiển thị vị trí chạm màn hình (Show Taps)
Chúng tôi khuyên bạn nên bật tùy chọn **Show Taps** (Hiển thị số lần nhấn/chạm) từ trang Tùy chọn nhà phát triển (developer options). Thực hiện theo các bước sau để kích hoạt tính năng này:

- Mở phần **Cài đặt (Settings)** trên thiết bị của bạn và tìm mục **Số bản dựng (Build number)**, mục này thường nằm trong phần *Giới thiệu về thiết bị (About device)*.
- Chạm vào **Số bản dựng** 7 lần liên tiếp để kích hoạt **Tùy chọn nhà phát triển (Developer Options)**. Nếu được yêu cầu, hãy nhập mật khẩu/mã khóa mở màn hình của thiết bị.
- Mở **Tùy chọn nhà phát triển** trong cài đặt hệ thống và bật tính năng **Hiển thị số lần nhấn/chạm (Show Taps / Show touches)** lên.

*Lưu ý:* Nếu dung lượng bản ghi của bạn quá lớn, bạn có thể thử giảm độ phân giải (resolution) và tốc độ khung hình (frame rate) trong trang cài đặt của ứng dụng AZ Screen Recorder. Trong trường hợp AZ Screen Recorder không khả dụng, bạn có thể sử dụng bất kỳ công cụ ghi màn hình nào khác. Các bước thực hiện cũng sẽ tương tự.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Developer Options | Tùy chọn nhà phát triển | Cài đặt nâng cao trên Android dành cho lập trình viên và tester |
| Screen Recording | Video quay màn hình | Bằng chứng dạng video ghi lại quá trình kiểm thử |
| Gallery | Thư viện ảnh | Ứng dụng quản lý hình ảnh và video mặc định trên thiết bị di động |
