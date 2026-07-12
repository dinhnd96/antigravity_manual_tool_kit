# Thu thập log Charles Proxy không cần bộ định tuyến Wi-Fi

> **Nguồn gốc**: uTest Academy - Collecting Charles Proxy Logs without a WiFi Router
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Thu thập log Charles Proxy không cần bộ định tuyến Wi-Fi (WiFi Router)
Là một phương án thế, nếu bạn không có quyền truy cập vào bộ định tuyến Wi-Fi (WiFi Router) để kết nối cả máy tính và điện thoại di động, bạn có thể thu thập log Charles Proxy bằng cách sử dụng một thiết bị phụ làm điểm phát sóng di động (mobile hotspot) để kết nối máy tính và thiết bị di động dùng để kiểm thử. Trong khóa học này, bạn sẽ học cách cấu hình Charles Proxy và thu thập log Charles không cần bộ định tuyến Wi-Fi.

#### Yêu cầu:
*   Máy tính đã được cài đặt phần mềm Charles Proxy.
*   Thiết bị di động chính dùng để kiểm thử.
*   Thiết bị di động phụ dùng làm điểm phát sóng (Hotspot).

#### Các bước thu thập Log:

1.  **Trên thiết bị phụ, hãy kích hoạt tính năng Điểm phát sóng di động (Mobile Hotspot):**
    *   **Đối với thiết bị Android:**
        1.  Mở ứng dụng Cài đặt (**Settings**).
        2.  Chọn **Network & Internet** (Mạng & Internet).
        3.  Chọn **Mobile Hotspot** hoặc **Hotspot & tethering** (Điểm phát sóng & chia sẻ kết nối).
        4.  Bật **Wi-Fi hotspot / Mobile hotspot** và ghi lại Tên (Name) cũng như Mật khẩu (Password) của mạng này. *(Lưu ý: Tên gọi các mục có thể hơi khác nhau tùy thuộc vào phiên bản Android và dòng máy).*
    *   **Đối với thiết bị iOS (iPhone/iPad):**
        1.  Mở ứng dụng Cài đặt (**Settings**).
        2.  Chọn **Mobile Data** (Dữ liệu di động).
        3.  Chọn **Personal Hotspot** (Điểm truy cập cá nhân).
        4.  Bật tùy chọn **Allow Others to Join** (Cho phép người khác kết nối) và ghi lại mật khẩu mạng. *(Lưu ý: Không phải nhà mạng hoặc gói cước di động nào cũng hỗ trợ chia sẻ mạng di động. Nếu bạn gặp lỗi không thể bật Hotspot, hãy thử sử dụng một nhà mạng hoặc gói cước dữ liệu khác hỗ trợ tính năng này).*
2.  Kết nối máy tính của bạn vào điểm phát sóng di động vừa kích hoạt ở bước 1.
3.  Cài đặt và cấu hình Charles Proxy theo đúng hướng dẫn trong khóa học **Charles Proxy trên máy tính (Charles Proxy for Desktop)**.
4.  Kết nối thiết bị di động dùng để kiểm thử (thiết bị chính) vào cùng một điểm phát sóng di động ở Bước 1.
5.  Làm theo các hướng dẫn để kết nối và thu thập log Charles theo đúng chỉ dẫn trong khóa học **Charles Proxy trên thiết bị di động (Charles Proxy for Mobile)**.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Mobile Hotspot | Điểm phát sóng di động (Mobile Hotspot) | Tính năng chia sẻ kết nối Internet từ thiết bị di động này sang thiết bị khác |
| Personal Hotspot | Điểm truy cập cá nhân (Personal Hotspot) | Tính năng phát sóng Wi-Fi từ dữ liệu di động trên thiết bị iOS |
