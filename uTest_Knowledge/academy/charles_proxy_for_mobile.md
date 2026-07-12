# Charles Proxy trên thiết bị di động

> **Nguồn gốc**: uTest Academy - Charles Proxy for Mobile
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Điều kiện tiên quyết (Cả Android và iOS)
*   Cả máy tính và thiết bị di động phải kết nối chung một mạng Wi-Fi.
*   Không có bất kỳ kết nối VPN nào được bật trên cả hai thiết bị.
*   Cấu hình Tường lửa (Firewall) và phần mềm Diệt virus (Antivirus) để cho phép Charles Proxy hoạt động. Nếu Charles bị chặn, kiểm thử viên sẽ không thể sử dụng nó để thu thập log. Thay vì tắt toàn bộ Tường lửa và phần mềm Diệt virus, hãy thêm Charles vào danh sách ngoại trừ để đảm bảo ứng dụng hoạt động bình thường trong khi vẫn duy trì bảo mật hệ thống.
*   Ứng dụng Charles Proxy phải đang chạy trên máy tính của bạn.

---

### Android

1.  Đầu tiên, hãy thiết lập Charles Proxy trên máy tính bằng cách làm theo các hướng dẫn (Bước 1-8) trong khóa học trước.
2.  Mở Charles Proxy trên máy tính:
    *   Nhấp chọn **Help** (Trợ giúp) > **Local IP Address** (Địa chỉ IP cục bộ) và ghi lại địa chỉ IP đang hoạt động trong mạng của bạn, ví dụ: `192.168.8.111`.
    *   Nhấp chọn **Proxy** > **Proxy Settings** (Cài đặt proxy) và đảm bảo cổng (port) của **HTTP Proxy** là `8888`.
3.  **Kết nối thiết bị di động với Charles Proxy:**
    *   Trên thiết bị Android, mở cài đặt Wi-Fi và chọn mạng Wi-Fi bạn đang kết nối.
    *   Mở cài đặt **Nâng cao (Advanced)** hoặc **Chi tiết** của mạng Wi-Fi đó, thay đổi thiết lập proxy thành **Thủ công (Manual)** và điền thông tin vào các trường sau:
        *   **Proxy hostname** (Tên máy chủ proxy): Nhập địa chỉ IP bạn đã ghi lại ở bước 2 (IP của máy tính).
        *   **Proxy port** (Cổng proxy): Nhập số cổng `8888`.
    *   Lưu lại các thiết lập proxy.
4.  Bạn sẽ thấy một thông báo yêu cầu cho phép kết nối hiển thị bên trong Charles Proxy trên máy tính khi bạn truy cập một trang web bất kỳ trên điện thoại. Bạn bắt buộc phải nhấn chọn **Allow** (Cho phép) để đồng ý.
5.  **Cài đặt Chứng chỉ gốc Charles (Charles Root Certificate):**
    *   Trên thiết bị Android, sử dụng trình duyệt bất kỳ (khuyên dùng Chrome) truy cập địa chỉ: `chls.pro/ssl` hoặc `charlesproxy.com/getssl`.
    *   Xác thực khóa bảo mật màn hình điện thoại nếu được yêu cầu, sau đó đặt tên bất kỳ cho chứng chỉ.
    *   Đảm bảo chọn mục sử dụng cho **VPN and apps** (hoặc ứng dụng và VPN) rồi nhấn **OK**.
6.  Đối với phiên bản Android 11 trở lên, bạn cần thực hiện thêm các bước sau để thiết lập chứng chỉ CA (các bước có thể hơi khác nhau tùy thuộc vào dòng máy):
    *   **Cách 1:**
        1.  Mở cài đặt thiết bị (**Settings**).
        2.  Chọn **Security** (Bảo mật).
        3.  Chọn **Encryption & Credentials** (Mã hóa và thông tin xác thực).
        4.  Chọn **Install a certificate** (Cài đặt chứng chỉ).
        5.  Chọn **CA Certificate** (Chứng chỉ CA).
        6.  Chấp nhận cảnh báo bằng cách nhấn chọn **Install anyway** (Vẫn cài đặt).
        7.  Tìm đến tệp chứng chỉ đã tải xuống trên thiết bị và mở nó ra.
        8.  Xác nhận cài đặt chứng chỉ.
    *   **Cách 2:**
        1.  Mở cài đặt thiết bị (**Settings**).
        2.  Chọn **Biometrics and security** (Sinh trắc học và bảo mật).
        3.  Chọn **Other security settings** (Cài đặt bảo mật khác).
        4.  Chọn **Install from device storage** (Cài đặt từ bộ nhớ thiết bị).
        5.  Chọn **CA Certificate** (Chứng chỉ CA).
        6.  Chấp nhận cảnh báo bằng cách nhấn chọn **Install anyway** (Vẫn cài đặt).
        7.  Xác thực khóa màn hình nếu được yêu cầu.
        8.  Tìm đến tệp chứng chỉ đã tải xuống trên thiết bị và mở nó ra.
        9.  Xác nhận cài đặt chứng chỉ.
7.  Trong Charles Proxy trên máy tính, nhấp vào **Proxy** và tắt tùy chọn **Windows Proxy** hoặc **macOS Proxy** đi. (Hành động này giúp tránh thu thập lưu lượng truy cập của máy tính. Bạn nên bật lại khi muốn thu thập log trên máy tính).
8.  Xóa sạch các log cũ đang lưu bằng cách nhấp vào **biểu tượng cây chổi (Broom)** và đảm bảo chế độ ghi log đang được bật.
9.  Trên thiết bị Android, mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ.
10. Sau khi hoàn tất, nhấp vào **File** > chọn **Save Session** (Lưu phiên) rồi lưu tệp dưới định dạng `.chls` hoặc `.chlz`.

---

### iOS

1.  Đầu tiên, hãy thiết lập Charles Proxy trên máy tính bằng cách làm theo các hướng dẫn (Bước 1-8) trong khóa học trước.
2.  Mở Charles Proxy trên máy tính:
    *   Nhấp chọn **Help** (Trợ giúp) > **Local IP Address** (Địa chỉ IP cục bộ) và ghi lại địa chỉ IP đang hoạt động trong mạng của bạn, ví dụ: `192.168.8.111`.
    *   Nhấp chọn **Proxy** > **Proxy Settings** (Cài đặt proxy) và đảm bảo cổng (port) của **HTTP Proxy** là `8888`.
3.  **Kết nối thiết bị di động với Charles Proxy:**
    *   Trên thiết bị iOS, mở **Settings** (Cài đặt) > **Wi-Fi**, nhấp vào **biểu tượng chữ 'i'** bên cạnh mạng Wi-Fi bạn đang kết nối.
    *   Cuộn xuống chọn **Configure Proxy** (Cấu hình Proxy) và chọn **Manual** (Thủ công):
        *   **Server** (Máy chủ): Nhập địa chỉ IP bạn đã ghi lại ở bước 2 (IP của máy tính).
        *   **Port** (Cổng): Nhập số cổng `8888`.
    *   Lưu lại các thiết lập proxy.
4.  Bạn sẽ thấy một thông báo yêu cầu cho phép kết nối hiển thị bên trong Charles Proxy trên máy tính khi bạn truy cập một trang web bất kỳ trên điện thoại. Bạn bắt buộc phải nhấn chọn **Allow** (Cho phép) để đồng ý.
5.  **Cài đặt Chứng chỉ gốc Charles (Charles Root Certificate):**
    *   Trên thiết bị iOS, mở trình duyệt **Safari** và truy cập địa chỉ: `chls.pro/ssl` hoặc `charlesproxy.com/getssl`.
    *   Nhấn chọn **Allow** (Cho phép) khi có thông báo tải về hồ sơ cấu hình.
    *   Mở **Settings** (Cài đặt), chọn **General** (Cài đặt chung) > **VPN & Device Management** (Quản lý VPN & Thiết bị - đối với iOS 15 trở lên) hoặc **Profiles & Device Management** (đối với các phiên bản iOS cũ hơn). Chọn cấu hình **Charles Proxy CA** và nhấn **Install** (Cài đặt).
    *   Quay lại **Settings** > **General** > **About** (Giới thiệu) > cuộn xuống dưới cùng chọn **Certificate Trust Settings** (Cài đặt tin cậy chứng chỉ). Gạt bật nút bật/tắt (toggle) tại mục **Enable Full Trust For Root Certificates** cho chứng chỉ Charles.
6.  Trong Charles Proxy trên máy tính, nhấp vào **Proxy** và tắt tùy chọn **Windows Proxy** hoặc **macOS Proxy** đi. (Hành động này giúp tránh thu thập lưu lượng truy cập của máy tính. Bạn nên bật lại khi muốn thu thập log trên máy tính).
7.  Xóa sạch các log cũ đang lưu bằng cách nhấp vào **biểu tượng cây chổi (Broom)** và đảm bảo chế độ ghi log đang được bật.
8.  Trên thiết bị iOS, mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ.
9.  Sau khi hoàn tất, nhấp vào **File** > chọn **Save Session** (Lưu phiên) rồi lưu tệp dưới định dạng `.chls` hoặc `.chlz`.

---

### Trình duyệt Firefox trên điện thoại

Nếu bạn đang sử dụng trình duyệt Firefox trên thiết bị di động, bạn cần thực hiện thêm các bước sau sau khi đã hoàn thành cấu hình trên:
1.  Vào phần cài đặt (**Settings**) của Firefox trên điện thoại.
2.  Chọn **About Firefox** (Giới thiệu Firefox).
3.  Nhấp vào biểu tượng logo của Firefox liên tục **năm (5) lần**.
4.  Quay trở lại màn hình cài đặt chính.
5.  Mở mục **Secret Settings** vừa xuất hiện bên dưới phần About Firefox.
6.  Gạt bật tùy chọn **Use third party CA certificates** (Sử dụng chứng chỉ CA của bên thứ ba).
7.  Khởi động lại cả trình duyệt Firefox và phần mềm Charles trên máy tính, sau đó mở trang web kiểm thử.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Local IP Address | Địa chỉ IP cục bộ (Local IP Address) | Địa chỉ IP của thiết bị trong mạng nội bộ |
| Proxy Hostname | Tên máy chủ proxy (Proxy Hostname) | Địa chỉ tên miền hoặc IP của máy chủ proxy |
| Proxy Port | Cổng proxy (Proxy Port) | Cổng giao tiếp được cấu hình trên máy chủ proxy |
