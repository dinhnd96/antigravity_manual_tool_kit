# Fiddler cho Thiết bị Di động (Fiddler for Mobile)

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Điều kiện tiên quyết
* Cả máy tính và điện thoại di động đều phải được kết nối vào cùng một mạng nội bộ.
* Không có VPN nào đang hoạt động trên cả hai thiết bị.
* Cấu hình Tường lửa (Firewall) và phần mềm Diệt vi-rút (Antivirus) để cho phép Fiddler hoạt động. Nếu Fiddler bị chặn, tester sẽ không thể sử dụng nó để thu thập log. Vì vậy, thay vì tắt toàn bộ Tường lửa và phần mềm Diệt vi-rút, hãy thêm Fiddler làm danh sách ngoại lệ (exception) để đảm bảo phần mềm hoạt động bình thường trong khi vẫn duy trì bảo mật hệ thống.

### Android

1. Đầu tiên, thiết lập Fiddler trên máy tính của bạn bằng cách làm theo hướng dẫn (Bước 1-3) từ bài học trước.
2. Mở Fiddler trên máy tính:
   * Nhấp vào **Settings (Cài đặt)** và chọn mục **Connections (Kết nối)**.
   * Kích hoạt tùy chọn **Allow remote computers to connect (Cho phép máy tính từ xa kết nối)**.
   * Đảm bảo số cổng hiển thị trong tab Connections là **8866**.
   * Lưu các thiết lập bằng cách nhấp vào nút **Save**.
3. Tìm địa chỉ IP cục bộ (Local IP address) của máy tính và ghi lại. Thực hiện các bước sau tùy theo hệ điều hành của bạn:
   * **Windows**: Mở Command Prompt (gõ `cmd`), nhập lệnh `ipconfig /all` và ghi lại địa chỉ IPv4 của bộ điều hợp Ethernet hoặc WiFi đang hoạt động; cách khác là mở **Settings > Network and Internet > Ethernet Properties** và ghi lại địa chỉ IPv4.
   * **macOS**: Mở **Network Utility** > tab **Info**, chọn đúng giao diện mạng đang sử dụng, sau đó ghi lại địa chỉ IPv4 hiển thị.
4. Kết nối với Fiddler:
   * Trên thiết bị Android của bạn, mở cài đặt WiFi và chọn mạng WiFi mà bạn đang kết nối.
   * Mở các tùy chọn Nâng cao (Advanced options) của mạng WiFi đó, chuyển cài đặt proxy sang **Thủ công (Manual)** và chỉ điền vào các trường thông tin sau:
     * **Proxy hostname**: Nhập địa chỉ IP cục bộ của máy tính mà bạn đã ghi lại ở Bước 3.
     * **Proxy port**: Nhập số cổng là **8866**.
   * Lưu cài đặt proxy lại.
5. Cài đặt Chứng chỉ gốc Fiddler (Fiddler Root Certificate):
   * Trên thiết bị Android, sử dụng trình duyệt bất kỳ và truy cập địa chỉ: `http://ipv4.fiddler:8866/FiddlerRoot.cer`.
   * Xác thực nếu được yêu cầu, hãy đảm bảo chọn tùy chọn **VPN and apps** và nhấn **OK**.
6. Đóng toàn bộ trình duyệt và các chương trình không cần thiết trên máy tính, xóa sạch các log đã lưu bằng cách nhấp vào nút **Remove all**.
7. Tắt nút gạt **Live Traffic**.
   * Việc này giúp ngăn việc thu thập lưu lượng mạng của chính máy tính. Bạn nên bật lại nút này khi cần ghi log trên máy tính.
8. Trên thiết bị Android, mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ của trang web/ứng dụng kiểm thử.
9. Sau khi hoàn tất, trên máy tính, nhấp vào **File**, di chuột đến mục **Save Archive**, sau đó chọn **All Sessions** và lưu log dưới định dạng `.saz`. Lưu ý không chọn bất kỳ tùy chọn mã hóa nào.

### iOS

1. Đầu tiên, thiết lập Fiddler trên máy tính của bạn bằng cách làm theo hướng dẫn (Bước 1-3) từ bài học trước.
2. Mở Fiddler trên máy tính:
   * Nhấp vào **Settings (Cài đặt)** và chọn mục **Connections (Kết nối)**.
   * Kích hoạt tùy chọn **Allow remote computers to connect (Cho phép máy tính từ xa kết nối)**.
   * Đảm bảo số cổng hiển thị trong tab Connections là **8866**.
   * Lưu các thiết lập bằng cách nhấp vào nút **Save**.
3. Tìm địa chỉ IP cục bộ (Local IP address) của máy tính và ghi lại. Thực hiện các bước sau tùy theo hệ điều hành của bạn:
   * **Windows**: Mở Command Prompt, nhập lệnh `ipconfig /all` và ghi lại địa chỉ IPv4 của bộ điều hợp Ethernet hoặc WiFi đang hoạt động; cách khác là mở **Settings > Network and Internet > Ethernet Properties** và ghi lại địa chỉ IPv4.
   * **macOS**: Mở **Network Utility** > tab **Info**, chọn đúng giao diện mạng đang sử dụng, sau đó ghi lại địa chỉ IPv4 hiển thị.
4. Kết nối với Fiddler:
   * Trên thiết bị iOS, mở **Settings (Cài đặt)**, điều hiện đến cài đặt **WiFi** và chạm vào nút **i** bên cạnh mạng WiFi đang kết nối.
   * Chạm vào mục **Configure Proxy (Cấu hình Proxy)** và chọn **Manual (Thủ công)**:
     * **Proxy hostname**: Nhập địa chỉ IP cục bộ của máy tính mà bạn đã ghi lại ở Bước 3.
     * **Proxy port**: Nhập số cổng là **8866**.
   * Lưu cài đặt proxy lại.
5. Cài đặt Chứng chỉ gốc Fiddler (Fiddler Root Certificate):
   * Trên thiết bị iOS, sử dụng trình duyệt bất kỳ và truy cập địa chỉ: `http://ipv4.fiddler:8866/FiddlerRoot.cer`.
   * Chạm vào **Allow (Cho phép)**.
   * Mở **Settings (Cài đặt)**, chạm vào **General (Cài đặt chung)**, sau đó chọn **VPN & Device Management (Quản lý VPN & Thiết bị)** (đối với iOS 15 trở lên) HOẶC **Profiles & Device Management (Quản lý Cấu hình & Thiết bị)** (đối với các phiên bản iOS cũ hơn), chọn cấu hình **DO_NOT_TRUST_FiddlerRoot** và nhấn cài đặt.
   * Mở lại **Settings (Cài đặt)**, truy cập **General (Cài đặt chung) > About (Giới thiệu)**, chọn mục **Certificate Trust Settings (Cài đặt tin cậy chứng chỉ)** và bật nút gạt **Enable Full Trust For Root Certificates (Kích hoạt độ tin cậy hoàn toàn cho chứng chỉ gốc)** cho chứng chỉ Fiddler.
6. Đóng toàn bộ trình duyệt và các chương trình không cần thiết trên máy tính, xóa sạch các log đã lưu bằng cách nhấp vào nút **Remove all**.
7. Tắt nút gạt **Live Traffic**.
   * Việc này giúp ngăn việc thu thập lưu lượng mạng của chính máy tính. Bạn nên bật lại nút này khi cần ghi log trên máy tính.
8. Trên thiết bị iOS, mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ của trang web/ứng dụng kiểm thử.
9. Sau khi hoàn tất, trên máy tính, nhấp vào **File**, di chuột đến mục **Save Archive**, sau đó chọn **All Sessions** và lưu log dưới định dạng `.saz`. Lưu ý không chọn bất kỳ tùy chọn mã hóa nào.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Fiddler Root Certificate | Chứng chỉ gốc Fiddler (Fiddler Root Certificate) | Chứng chỉ gốc cần thiết để thiết bị tin cậy và cho phép Fiddler giải mã HTTPS |
| Live Traffic | Lưu lượng trực tiếp (Live Traffic) | Chế độ ghi nhận lưu lượng mạng theo thời gian thực |
| Network Utility | Công cụ mạng (Network Utility) | Ứng dụng hỗ trợ kiểm tra thông tin mạng mặc định trên macOS |
| Ethernet Properties | Thuộc tính Ethernet (Ethernet Properties) | Giao diện cấu hình và hiển thị chi tiết kết nối mạng dây trên Windows |
| Certificate Trust Settings | Cài đặt tin cậy chứng chỉ (Certificate Trust Settings) | Trang cấu hình quyền tin cậy hoàn toàn đối với các chứng chỉ gốc tự cài trên iOS |
| VPN and Device Management | Quản lý VPN & Thiết bị (VPN and Device Management) | Mục cài đặt quản lý cấu hình và thiết bị trên hệ điều hành iOS 15 trở lên |
| Profiles and Device Management | Quản lý Cấu hình & Thiết bị (Profiles and Device Management) | Mục cài đặt quản lý cấu hình và thiết bị trên hệ điều hành iOS cũ |
