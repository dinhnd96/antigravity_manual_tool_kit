# Log thiết bị Android

> **Nguồn gốc**: uTest Academy - Android Device Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Bạn có thể thu thập log thiết bị Android bằng bất kỳ máy tính chạy Windows, macOS hoặc Linux nào. Hãy luôn sử dụng công cụ adb hoặc Android Studio để thu thập log, tuyệt đối không sử dụng các ứng dụng của bên thứ ba như Syslog hay CatLog.

### Điều kiện tiên quyết
Trước khi bắt đầu, hãy đảm bảo:
1.  Kích hoạt gỡ lỗi USB (USB Debugging) trên thiết bị của bạn bằng cách làm theo các bước sau:
    *   Trên thiết bị Android, tìm mục **Build number (Số bản dựng)**, mục này thường nằm trong trang **About device (Thông tin thiết bị)**.
    *   Nhấp liên tục 7 lần vào mục **Build number** để kích hoạt **Developer Options (Tùy chọn nhà phát triển)**.
    *   Mở **Developer Options** và bật **USB Debugging (Gỡ lỗi USB)**.
2.  Thiết bị di động của bạn không được khóa màn hình, phải đang hoạt động và kết nối trực tiếp với máy tính.
3.  Có thể bạn sẽ thấy một thông báo cảnh báo hiển thị trên thiết bị di động yêu cầu cho phép kết nối, hãy đảm bảo luôn tích chọn ô **Always allow from this computer (Luôn cho phép từ máy tính này)** và nhấn **Allow (Cho phép)**.
4.  Nếu bạn thấy cảnh báo về tệp `adb.exe` từ phần mềm diệt virus, hãy tạm thời tắt phần mềm diệt virus hoặc thêm `adb.exe` vào danh sách loại trừ (exception list).

---

### Các bước thu thập log trên các hệ điều hành

#### Windows

1.  Tải xuống bộ SDK Platform Tools dành cho Windows tại đây.
2.  Giải nén tệp tin và lưu trên ổ cứng máy tính của bạn.
3.  Mở thư mục **platform-tools** đã giải nén, gõ `cmd` vào thanh địa chỉ của thư mục rồi nhấn Enter. (Hoặc bạn cũng có thể mở Command Prompt, gõ `cd ` kèm theo một dấu cách, rồi kéo thả thư mục platform-tools vào cửa sổ CMD và nhấn Enter).
4.  Xóa sạch các log hiện tại đang lưu trữ trên thiết bị bằng cách chạy lệnh sau:
    `adb logcat -c`
5.  Tái hiện lỗi từ đầu đến cuối.
6.  Thu thập log bằng cách nhập lệnh:
    `adb logcat -d -v time > .\log.txt`
7.  Bạn sẽ thấy tệp `log.txt` xuất hiện trong thư mục platform-tools.
8.  Tải tệp `log.txt` này lên báo cáo lỗi của bạn.

##### Phương pháp thay thế (Được khuyến nghị)
1.  Thực hiện các bước từ 1 đến 4 được đề cập ở trên.
2.  Nhập lệnh sau để bắt đầu thu thập log:
    `adb logcat -v threadtime > .\log.txt`
3.  Tái hiện lỗi từ đầu đến cuối.
4.  Tại cửa sổ dòng lệnh, nhấn tổ hợp phím **Ctrl + C** để dừng quá trình ghi log.
5.  Tải tệp `log.txt` được tạo trong thư mục lên báo cáo lỗi.

**Lưu ý**:
*   Nếu tệp log quá lớn, hãy đóng tất cả các ứng dụng/trang web khác, chạy lệnh `adb logcat -c` để xóa log cũ trước khi mở ứng dụng và tái hiện lỗi.
*   Nếu bạn gặp bất kỳ lỗi nào khi thực thi lệnh adb, hãy chạy lệnh `adb kill-server` để dừng các tiến trình adb đang chạy ẩn, sau đó thực hiện lại các bước để thu thập log.

#### macOS

1.  Tải xuống bộ SDK Platform Tools dành cho macOS tại đây.
2.  Giải nén tệp tin và lưu trên ổ cứng của máy tính.
3.  Mở **Terminal** (nhấn **Cmd+Space**, gõ `terminal` và nhấn Enter).
4.  Nhập lệnh `cd ` kèm theo một dấu cách trong Terminal, sau đó kéo thư mục platform-tools đã giải nén thả vào Terminal và nhấn Enter.
5.  Xóa sạch các log đang lưu trữ trên thiết bị bằng cách chạy lệnh sau:
    `./adb logcat -c`
6.  Tái hiện lỗi từ đầu đến cuối.
7.  Thu thập log bằng cách nhập lệnh:
    `./adb logcat -d -v time > ./log.txt`
8.  Bạn sẽ thấy tệp `log.txt` xuất hiện trong thư mục.
9.  Tải tệp này lên báo cáo lỗi của bạn.

##### Phương pháp thay thế (Được khuyến nghị)
1.  Thực hiện các bước từ 1 đến 4 được đề cập ở trên.
2.  Nhập lệnh sau để bắt đầu thu thập log:
    `./adb logcat -v threadtime > ./log.txt`
3.  Tái hiện lỗi từ đầu đến cuối.
4.  Tại cửa sổ Terminal, nhấn tổ hợp phím **Cmd + C** để dừng quá trình ghi log.
5.  Tải tệp `log.txt` được tạo lên báo cáo lỗi.

#### Linux

1.  Mở Terminal và nhập lệnh bên dưới tùy thuộc vào bản phân phối (distro) Linux của bạn:
    *   Hệ điều hành gốc Debian (Ubuntu, Linux Mint...): `sudo apt-get install adb`
    *   Hệ điều hành gốc Fedora/SUSE: `sudo yum install android-tools`
2.  Nhập mật khẩu máy tính của bạn và chờ quá trình cài đặt hoàn tất.
3.  Xóa sạch các log cũ bằng cách chạy lệnh sau:
    `adb logcat -c`
4.  Tái hiện lỗi từ đầu đến cuối.
5.  Thu thập log bằng cách nhập lệnh:
    `adb logcat -d -v time > log.txt`
6.  Tải tệp `log.txt` xuất hiện trong thư mục lên báo cáo lỗi của bạn.

##### Phương pháp thay thế (Được khuyến nghị)
1.  Thực hiện các bước từ 1 đến 3 được đề cập ở trên.
2.  Nhập lệnh sau để bắt đầu thu thập log:
    `adb logcat -v threadtime > log.txt`
3.  Tái hiện lỗi từ đầu đến cuối.
4.  Tại cửa sổ Terminal, nhấn tổ hợp phím **Ctrl + C** để dừng quá trình ghi log.
5.  Tải tệp `log.txt` được tạo lên báo cáo lỗi.

**Lưu ý**: Bạn cũng có thể tải xuống platform-tools tại đây và thực hiện theo các bước từ 2 đến 4 tương tự như hướng dẫn dành cho Windows.

---

### Sử dụng Android Studio để thu thập Log thiết bị Android

*Trước khi bắt đầu, hãy đảm bảo rằng bạn đã thực hiện các bước điều kiện tiên quyết nêu trên.*

1.  Tải xuống và cài đặt phần mềm Android Studio tại đây.
2.  Sau khi cài đặt thành công, mở ứng dụng Android Studio.
3.  Tại Trình hướng dẫn thiết lập (Setup Wizard), nhấn **Next**.
4.  Thay đổi tùy chọn thiết lập sang **Custom** để loại bỏ việc cài đặt các tệp tin không thực sự cần thiết.
5.  Lựa chọn giao diện (theme) phù hợp với sở thích của bạn.
6.  Bỏ tích chọn tất cả các thành phần tùy chọn và nhấn **Next**.
7.  Tại màn hình chào mừng của Android Studio, nhấp vào **New Project** và chọn **Empty Activity**.
8.  Nhấn **Next** rồi nhấn **Finish** mà không cần thay đổi bất cứ thông tin nào.
9.  Đợi cho đến khi quá trình đồng bộ (sync) hoàn tất, sau đó mở Logcat bằng cách vào **View** > **Tool Windows** > **Logcat** (Hoặc nhấp trực tiếp vào nút Logcat hiển thị ở thanh dưới cùng của màn hình).
10. Kết nối thiết bị Android của bạn với máy tính.
11. Trong cửa sổ Logcat, chọn thiết bị Android của bạn (nếu không tự động chọn) và xóa sạch log cũ bằng cách nhấp vào **biểu tượng Thùng rác**.
12. Tái hiện lỗi trên thiết bị Android của bạn.
13. Trên máy tính, nhấp vào **nút Tạm dừng (Pause)** để dừng việc thu thập thêm các log không liên quan.
14. Nhấn tổ hợp phím **Ctrl+A** để chọn toàn bộ log, nhấp chuột phải và chọn **Copy**.
15. Mở chương trình soạn thảo văn bản bất kỳ, tạo tệp tin mới và dán toàn bộ log đã sao chép vào.
16. Lưu tệp dưới định dạng `.txt`.

**Lưu ý**: Nếu tệp log quá lớn, hãy đóng các ứng dụng và/hoặc trang web khác, xóa sạch log cũ bằng cách nhấp vào biểu tượng Thùng rác trước khi mở ứng dụng và tái hiện lại lỗi.

---

### Gỡ lỗi không dây trong Android Studio (Chỉ dành cho Android 11 trở lên)

*Trước khi bắt đầu, hãy đảm bảo đã làm theo các bước điều kiện tiên quyết.*

1.  Thực hiện theo các bước từ 1 đến 7 của phần trên để tạo một dự án mới trong Android Studio.
2.  Đợi cho đến khi quá trình đồng bộ hoàn tất. Sau đó, nhấp vào menu thả xuống **No Device**.
3.  Nhấp chọn **Pair device using Wi-Fi** và chuyển sang tab **Pair using pairing code**.
4.  Trên thiết bị di động, truy cập **Settings (Cài đặt)** > **Developer options (Tùy chọn nhà phát triển)**.
5.  Nhấn vào **Wireless debugging (Gỡ lỗi không dây)** và bật tính năng này lên.
6.  Nhấn chọn **Pair device with pairing code** (Hoặc chọn Pair device with QR code để quét mã QR).
7.  Nhấp vào nút **Pair** bên cạnh địa chỉ IP tương ứng trên giao diện Android Studio.
8.  Nhập mã kết nối **Wi-Fi Pairing Code** hiển thị trên điện thoại vào máy tính và nhấn **Pair**.
9.  Khi thiết bị đã kết nối, nhấp vào nút **Logcat** ở thanh dưới cùng của màn hình và xóa mọi bộ lọc (filter) nếu có.
10. Xóa sạch log cũ bằng cách nhấp vào **biểu tượng Thùng rác**.
11. Tái hiện lỗi trên thiết bị Android của bạn.
12. Trên máy tính, nhấp vào **nút Tạm dừng (Pause)** để dừng thu thập thêm log.
13. Nhấn tổ hợp phím **Ctrl+A** để chọn tất cả log, nhấp chuột phải và chọn **Copy**.
14. Mở trình soạn thảo văn bản bất kỳ, tạo tệp tin mới và dán toàn bộ log vào, sau đó lưu dưới định dạng `.txt`.

**Lưu ý**: Khi thiết bị đã được ghép đôi thành công, mỗi lần mở Android Studio sau này, thiết bị Android sẽ tự động kết nối và tạo log nếu tính năng gỡ lỗi không dây đang được bật trên điện thoại.

---

### Gỡ lỗi không dây bằng Command Prompt (CMD) [Chỉ dành cho Android 11 trở lên]

#### Điều kiện tiên quyết
1.  Tải xuống và giải nén thư mục platform-tools trên máy tính của bạn, sau đó mở thư mục platform-tools.
2.  Bật tùy chọn nhà phát triển trên thiết bị Android của bạn.
3.  Đảm bảo rằng máy tính và thiết bị Android của bạn đang kết nối chung một mạng Wi-Fi.

#### Các bước thực hiện
1.  Truy cập **Settings** > **Developer options** trên thiết bị Android của bạn.
2.  Chọn **Wireless debugging** và bật lên. Một thông báo xác nhận sẽ xuất hiện trên điện thoại. Hãy tích chọn **"Always allow on this network"** (Luôn cho phép trên mạng này) và nhấn **Allow (Cho phép)**.
3.  Nhấn vào mục **Pair device with pairing code**.
4.  Trên máy tính, truy cập thư mục platform-tools và mở CMD bằng cách gõ `cmd` vào thanh địa chỉ của thư mục rồi nhấn Enter.
5.  Nhập địa chỉ IP, số cổng (port) và mã kết nối Wi-Fi pairing code hiển thị trên điện thoại theo cú pháp sau:
    `adb pair <Địa_chỉ_IP>:<Cổng> <Mã_kết_nối>`
6.  Sau khi ghép đôi thành công, kết nối thiết bị với máy tính bằng cách nhập địa chỉ IP và số cổng mới (New Port) hiển thị trên màn hình điện thoại theo cú pháp sau:
    `adb connect <Địa_chỉ_IP>:<Cổng_mới>`
7.  Sau khi kết nối thành công, bạn có thể thu thập log bằng lệnh adb mà không cần kết nối điện thoại qua cổng USB nữa.
8.  Xóa sạch các log đang lưu trữ trên thiết bị bằng cách chạy lệnh:
    `adb logcat -c`
9.  Tái hiện lỗi từ đầu đến cuối.
10. Thu thập log bằng cách nhập lệnh:
    `adb logcat -d -v time > log.txt` hoặc `adb logcat -v threadtime > log.txt`
11. Bạn sẽ thấy tệp `log.txt` xuất hiện trong thư mục platform-tools.
12. Tải tệp `log.txt` này lên báo cáo lỗi của bạn.

**Lưu ý**:
*   Để hiển thị hộp thoại xác nhận cho phép gỡ lỗi không dây lần đầu tiên, bạn nên nhấn vào tùy chọn **Revoke USB debugging authorizations (Thu hồi ủy quyền gỡ lỗi USB)** trên điện thoại để xóa sạch các thiết bị đã lưu từ trước, sau đó thực hiện lại các bước hướng dẫn.
*   Nếu tệp log quá lớn, hãy đóng các ứng dụng/trang web khác và chạy lệnh `adb logcat -c` trước khi mở ứng dụng kiểm thử để xóa sạch log cũ và tái hiện lỗi.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Wireless Debugging | Gỡ lỗi không dây (Wireless Debugging) | Tính năng gỡ lỗi thiết bị di động qua kết nối mạng WiFi |
| IP Address | Địa chỉ IP (IP Address) | Địa chỉ định danh thiết bị trong mạng Internet hoặc mạng nội bộ |
| Port | Cổng (Port) | Điểm cuối truyền thông hoặc giao tiếp kết nối phần mềm |
