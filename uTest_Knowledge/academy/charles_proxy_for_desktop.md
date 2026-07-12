# Charles Proxy trên máy tính

> **Nguồn gốc**: uTest Academy - Charles Proxy for Desktop
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Windows

*Trước khi bắt đầu, hãy đảm bảo đã tắt tất cả các kết nối VPN.*

Cấu hình Tường lửa (Firewall) và phần mềm Diệt virus (Antivirus) để cho phép Charles Proxy hoạt động. Nếu Charles bị chặn, bạn sẽ không thể sử dụng nó để thu thập log. Thay vì tắt toàn bộ Tường lửa và phần mềm Diệt virus, hãy thêm Charles vào danh sách ngoại trừ (exception list) để đảm bảo ứng dụng hoạt động bình thường trong khi vẫn duy trì bảo mật hệ thống.

1.  Tải xuống và cài đặt Charles Proxy phiên bản 64-bit tại đây.
    *   *Nếu bạn đang sử dụng hệ điều hành 32-bit, hãy tải phiên bản 32-bit tại đây.*
    *   *Để xác định máy tính của bạn đang chạy phiên bản Windows 32-bit hay 64-bit, hãy làm theo hướng dẫn sau: Nhấn nút Start, chọn Settings > System > About. Tại mục Device specifications, xem thông tin ở dòng System type. Đối với phiên bản 64-bit, vui lòng không cài bản 32-bit mà hãy cài đặt phiên bản 64-bit.*
2.  Mở ứng dụng Charles Proxy.
3.  **Cài đặt Chứng chỉ gốc Charles (Charles Root Certificate):**
    *   Nhấp chọn **Help** (Trợ giúp) > **SSL Proxying** > **Install Charles Root Certificate**.
    *   Cửa sổ chứng chỉ hiển thị, nhấp vào nút **Install Certificate...** (Cài đặt chứng chỉ) rồi chọn **Next**.
    *   Chọn tùy chọn **Place all certificates in the following store** và nhấp chọn **Browse...** (Duyệt).
    *   Chọn thư mục **Trusted Root Certification Authorities** rồi nhấp chọn **OK**.
    *   Nhấp chọn **Next** và cuối cùng nhấn **Finish** (Hoàn tất).
4.  Đóng phần mềm Charles và khởi động lại máy tính của bạn.
5.  Mở lại Charles, nhấp chọn mục **Proxy** và đảm bảo tùy chọn **Windows Proxy** đã được tích chọn bật.
6.  **Thiết lập cấu hình Proxy SSL:**
    *   Nhấp vào **Proxy** và chọn **SSL Proxy Settings**. Tích chọn **Enable SSL Proxying** (Bật proxy SSL) và nhấn nút **Add** (Thêm) nằm dưới phần **Include**.
    *   Tại hộp thoại Edit Location hiện lên, nhập ký tự `*` vào trường **Host** và nhập số `443` vào trường **Port**. *(Việc nhập dấu `*` ở ô Host cho phép giải mã toàn bộ lưu lượng truy cập HTTPS).*
7.  Xóa sạch các log cũ đang lưu bằng cách nhấp vào **biểu tượng cây chổi (Broom)** và đảm bảo chế độ ghi log đang được bật (biểu tượng nút ghi hình màu đỏ).
8.  Mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ.
9.  Sau khi hoàn tất, nhấp vào **File** > chọn **Save Session** (Lưu phiên) rồi lưu tệp dưới định dạng `.chls` hoặc `.chlz`.

---

### macOS

*Trước khi bắt đầu, hãy đảm bảo đã tắt tất cả các kết nối VPN.*

Cấu hình Tường lửa (Firewall) và phần mềm Diệt virus (Antivirus) để cho phép Charles Proxy hoạt động. Nếu Charles bị chặn, bạn sẽ không thể sử dụng nó để thu thập log. Thay vì tắt toàn bộ Tường lửa và phần mềm Diệt virus, hãy thêm Charles vào danh sách ngoại trừ để đảm bảo ứng dụng hoạt động bình thường trong khi vẫn duy trì bảo mật hệ thống.

1.  Tải xuống và cài đặt Charles Proxy dành cho macOS tại đây.
2.  Mở ứng dụng Charles Proxy.
3.  **Cài đặt Chứng chỉ gốc Charles (Charles Root Certificate):**
    *   Nhấp chọn **Help** (Trợ giúp) > **SSL Proxying** > **Install Charles Root Certificate**.
    *   Ứng dụng **Keychain Access** (Trình quản lý chuỗi khóa) sẽ tự động mở ra. Hãy tìm kiếm từ khóa `Charles` và nhấp đúp vào chứng chỉ có tên **Charles Proxy CA**.
    *   Nhấp vào mũi tên bên cạnh mục **Trust** (Tin cậy) và thay đổi giá trị của dòng **When using this certificate** thành **Always Trust** (Luôn tin cậy).
    *   Đóng cửa sổ Keychain Access lại. Hệ thống sẽ yêu cầu bạn nhập mật khẩu của máy Mac để xác nhận thay đổi, hãy nhập mật khẩu của thiết bị.
4.  Đóng phần mềm Charles và khởi động lại máy tính của bạn.
5.  Mở lại Charles, nhấp chọn mục **Proxy** và đảm bảo tùy chọn **macOS Proxy** đã được tích chọn bật.
6.  **Thiết lập cấu hình Proxy SSL:**
    *   Nhấp vào **Proxy** và chọn **SSL Proxy Settings**. Tích chọn **Enable SSL Proxying** và nhấn nút **Add nằm dưới phần Include**.
    *   Tại hộp thoại Edit Location hiện lên, nhập ký tự `*` (hoặc để trống) ở ô **Host** và nhập số `443` ở ô **Port**. *(Việc nhập dấu `*` ở ô Host cho phép giải mã toàn bộ lưu lượng truy cập).*
7.  Xóa sạch các log cũ đang lưu bằng cách nhấp vào **biểu tượng cây chổi (Broom)** và đảm bảo chế độ ghi log đang được bật.
8.  Mở trình duyệt và tái hiện lỗi bắt đầu từ trang chủ.
9.  Sau khi hoàn tất, nhấp vào **File** > chọn **Save Session** (Lưu phiên) rồi lưu tệp dưới định dạng `.chls` hoặc `.chlz`.

---

### Trình duyệt Firefox

Đối với trình duyệt Firefox, bạn cần thực hiện thêm các bước sau sau khi đã cấu hình các bước trên:
1.  Mở Firefox, nhấp vào **menu hamburger (ba sọc ngang)** ở góc trên bên phải và chọn **Settings** (Cài đặt).
2.  Cuộn xuống phần **Network Settings** (Cài đặt mạng) và nhấp chọn nút **Settings...** (Cài đặt).
3.  Thay đổi cấu hình thành **Use system proxy settings** (Sử dụng cài đặt proxy hệ thống).

---

### Ghi chú quan trọng

*   Nếu bạn chỉ muốn giải mã lưu lượng truy cập từ một trang cụ thể, hãy nhập tên miền của trang đó nằm giữa hai dấu sao (ví dụ: `*utest*`) vào ô Host trong phần cấu hình SSL Proxy Settings.
*   Hãy lưu ý rằng đôi khi bạn sẽ được yêu cầu giải mã toàn bộ lưu lượng truy cập, lúc khác chỉ yêu cầu lưu lượng truy cập cụ thể. Tốt nhất là bạn nên biết cả hai phương pháp này, và hãy luôn làm theo đúng hướng dẫn được cung cấp trong phần tổng quan của từng chu kỳ kiểm thử (test cycle overview).
*   Ứng dụng này yêu cầu mua giấy phép sử dụng (license) nếu bạn dùng quá 30 phút cho mỗi phiên làm việc. Mỗi người dùng chịu trách nhiệm đảm bảo việc sử dụng phần mềm tuân thủ các quy định bản quyền.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Charles Root Certificate | Chứng chỉ gốc Charles (Charles Root Certificate) | Chứng chỉ gốc cần cài đặt để Charles Proxy có thể giải mã lưu lượng HTTPS |
| Keychain Access | Trình quản lý chuỗi khóa (Keychain Access) | Ứng dụng quản lý chứng chỉ và thông tin bảo mật mặc định trên macOS |
| SSL Proxy Settings | Thiết lập proxy SSL (SSL Proxy Settings) | Cấu hình cho phép Charles giải mã dữ liệu của các cổng và máy chủ SSL cụ thể |
