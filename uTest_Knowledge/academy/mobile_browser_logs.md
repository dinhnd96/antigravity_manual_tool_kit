# Log trình duyệt trên di động

> **Nguồn gốc**: uTest Academy - Mobile Browser Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Thu thập log trình duyệt trên di động có phần phức tạp hơn và cần sử dụng máy tính; quy trình này được gọi là Gỡ lỗi từ xa (Remote Debugging).

Các trình duyệt nhân Chromium và Firefox chỉ hỗ trợ Gỡ lỗi từ xa (Remote Debugging) qua cổng USB đối với thiết bị Android. Hệ điều hành iOS chỉ hỗ trợ gỡ lỗi từ xa trên trình duyệt Safari.

### Mục lục
1.  [Điều kiện tiên quyết đối với thiết bị Android](#điều-kiện-tiên-quyết-đối-với-thiết-bị-android)
2.  [Gỡ lỗi từ xa trên Google Chrome/ trình duyệt nhân Chromium bất kỳ [Chỉ áp dụng Android]](#gỡ-lỗi-từ-xa-trên-google-chrome-trình-duyệt-nhân-chromium-bất-kỳ-chỉ-áp-dụng-android)
3.  [Gỡ lỗi từ xa trên Firefox [Chỉ áp dụng Android]](#gỡ-lỗi-từ-xa-trên-firefox-chỉ-áp-dụng-android)
4.  [Log Safari trên iOS qua máy Mac](#log-safari-trên-ios-qua-máy-mac)
5.  [Log Safari trên iOS qua máy tính Windows [Không còn hoạt động]](#log-safari-trên-ios-qua-máy-tính-windows)
6.  [Log Chrome trên iOS qua máy Mac](#log-chrome-trên-ios-qua-máy-mac)
7.  [Log Firefox trên iOS qua máy Mac](#log-firefox-trên-ios-qua-máy-mac)

---

### Điều kiện tiên quyết đối với thiết bị Android

1.  Bật **Tùy chọn nhà phát triển (Developer Options)** 📱 trên thiết bị Android bằng cách nhấp 7 lần vào **Số bản dựng (Build Number)**. Nếu gặp khó khăn, hãy tìm hiểu thêm trực tuyến về thiết bị của bạn.
2.  Mở Tùy chọn nhà phát triển và bật **Gỡ lỗi USB (USB Debugging)**.
3.  Kết nối trực tiếp thiết bị Android với máy tính bằng cáp USB.
4.  Trên máy tính 💻 của bạn, tải xuống bộ công cụ SDK platform-tools tại đây.
5.  Giải nén tệp tin và mở thư mục đó ra.
6.  Mở **Command Prompt** (Windows) hoặc **Terminal** (macOS hoặc Linux).
7.  Nhập lệnh `cd` kèm theo một khoảng trắng, sau đó kéo và thả thư mục platform-tools đã giải nén vào cửa sổ Command Prompt hoặc Terminal, rồi nhấn Enter.
8.  Hiện tại bạn đã ở trong thư mục platform-tools, ví dụ: `cd c:\users\john\desktop\platform-tools`.
9.  Đối với Windows, nhập `adb start-server` và đối với macOS hoặc Linux, nhập `./adb start-server`, sau đó cho phép mọi yêu cầu cấp quyền trên thiết bị di động 📱 của bạn.

**Lưu ý**: Bạn cần khởi động adb server bằng cách thực hiện các bước từ 6 đến 9 mỗi lần trước khi thu thập log, nếu không thiết bị của bạn có thể không được trình duyệt nhận diện.

---

### Gỡ lỗi từ xa trên Google Chrome/ trình duyệt nhân Chromium bất kỳ [Chỉ áp dụng Android]

*Trước khi bắt đầu, hãy đảm bảo bạn đã thực hiện các bước trong phần điều kiện tiên quyết.*

1.  Mở trình duyệt Google Chrome trên máy tính 💻 và truy cập địa chỉ `chrome://inspect#devices`.
2.  Không quan trọng bạn đang sử dụng trình duyệt nhân Chromium nào trên thiết bị Android để kiểm thử; bạn vẫn có thể sử dụng Google Chrome trên máy tính để kiểm tra (inspect) các tab của trình duyệt đó.
3.  Đảm bảo rằng ô tích chọn **Discover USB devices** đã được bật, thiết bị của bạn đã được kết nối với máy tính và đã được mở khóa.
4.  Nếu bạn thấy tên kiểu máy (model name) của thiết bị Android hiển thị, điều đó có nghĩa là DevTools đã kết nối thành công với thiết bị của bạn.
5.  Nếu thiết bị hiển thị trạng thái Offline, hãy chấp nhận thông báo yêu cầu cấp quyền Cho phép gỡ lỗi USB (Allow USB Debugging) trên thiết bị Android 📱 của bạn.
6.  Tất cả các tab đang mở trên trình duyệt di động sẽ hiển thị bên trong trình duyệt Chrome trên máy tính của bạn, chúng tôi khuyên bạn nên đóng tất cả các tab khác.
7.  Mở trang web kiểm thử trên thiết bị Android 📱 của bạn.
8.  Nhấp vào nút **Inspect** (Kiểm tra) trong trình duyệt Chrome trên máy tính bên cạnh URL trang web kiểm thử, một cửa sổ DevTools mới sẽ mở ra. (Nếu cửa sổ DevTools mới hiển thị lỗi, hãy thử nhấp vào tùy chọn **Inspect fallback** để thay thế).
9.  Tại tab **Console**, nhấp vào biểu tượng bánh răng ở góc trên bên phải.
10. Cuộn xuống phần **Console preferences** > tích chọn **Show Timestamps** (Hiển thị mốc thời gian) và **Preserve Log Upon Navigation** (Giữ log khi chuyển trang/điều hướng).
11. Đóng cửa sổ cài đặt.
12. Xóa sạch console bằng cách nhấp vào biểu tượng **Clear Console** hoặc nhấp chuột phải vào bên trong cửa sổ console và chọn **Clear console** (Xóa console).
13. Tải lại trang và tái hiện lỗi bắt đầu từ trang chủ.
14. Nhấp chuột phải vào phần log và chọn **Save As** (Lưu dưới dạng).
15. Lưu tệp dưới định dạng `.txt`.
16. Mở tệp log console lên và đảm bảo rằng có mốc thời gian (timestamp) và dòng chữ 'Navigated to' cùng địa chỉ trang web đang kiểm thử (Ví dụ: `18:32:30.854 Navigated to https://www.utest.com`).

---

### Gỡ lỗi từ xa trên Firefox [Chỉ áp dụng Android]

1.  Mở trình duyệt Firefox trên máy tính 💻, nhấp vào menu hamburger và chọn **Web Developer** > **Remote Debugging** (Gỡ lỗi từ xa).
2.  Nhấp vào nút **Enable USB devices** (Bật thiết bị USB).
3.  Mở Firefox trên thiết bị Android 📱 của bạn, nhấn vào menu 3 chấm và bật **Remote debugging via USB** (Gỡ lỗi từ xa qua USB) từ phần cài đặt.
4.  Bạn sẽ thấy tên thiết bị của mình hiển thị trên trình duyệt Firefox của máy tính, nhấp vào **Connect** (Kết nối) ở bên cạnh.
5.  Nhấp vào tên thiết bị để xem tất cả các tab đang mở, chúng tôi khuyên bạn nên đóng tất cả các tab khác.
6.  Mở trang web kiểm thử trên ứng dụng Firefox (thiết bị Android).
7.  Nhấp vào nút **Inspect** trong trình duyệt Firefox của máy tính bên cạnh URL trang web kiểm thử.
8.  Một cửa sổ Toolbox mới sẽ mở ra, chọn tab **Console** rồi nhấp vào biểu tượng bánh răng ở góc trên cùng bên phải và chọn **Persist Logs** (Giữ log) và **Show Timestamps** (Hiển thị mốc thời gian).
9.  Nhấp vào biểu tượng thùng rác để xóa sạch các log cũ.
10. Tải lại trang và tái hiện lỗi bắt đầu từ trang chủ.
11. Để ghi lại log, nhấp chuột phải vào console > chọn **Export Visible Messages To** > **File**.
12. Lưu tệp dưới định dạng `.txt`.
13. Mở tệp log console lên và đảm bảo rằng có mốc thời gian (timestamp) và dòng chữ 'Navigated to' cùng địa chỉ trang web đang kiểm thử.

---

### Log Safari trên iOS qua máy Mac

1.  Mở phần cài đặt 📱 trên iOS, cuộn xuống và chọn **Apps** > **Safari** > **Advanced** (Nâng cao) và bật **Web Inspector** (Trình kiểm tra web).
2.  Kết nối trực tiếp thiết bị iOS 📱 với máy Mac bằng cáp; hãy đảm bảo bạn chọn Tin cậy (Trust) máy Mac này.
3.  Trên thiết bị iOS 📱 của bạn, mở Safari và duy trì một tab mở.
4.  Trên máy Mac 💻 của bạn, mở Safari và chọn **Settings** (Cài đặt).
5.  Chọn tab **Advanced** (Nâng cao) và bật tùy chọn **Show features for web developers** (Hiển thị các tính năng cho nhà phát triển web).
6.  Đóng lại cài đặt và nhấp chọn mục **Develop** (Phát triển) > [Tên thiết bị iOS của bạn] > [Tùy chọn tab Safari đang mở].
7.  Trình kiểm tra web (Web Inspector) sẽ mở ra; chuyển đến tab **Console**.
8.  Tại cửa sổ console, từ menu hamburger chọn **Preserve Log** (Giữ log), và ở góc trên bên phải của trình kiểm tra web, nhấp vào biểu tượng bánh răng, mở tab Console và bật tùy chọn **Show: Timestamps** (Hiển thị mốc thời gian).
9.  Quay lại tab Console và nhấp vào biểu tượng thùng rác để xóa sạch các log.
10. Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ trên thiết bị iOS 📱 của bạn.
11. Để lưu log, nhấn tổ hợp phím **Command+S** (hoặc nhấn **Command+A** để chọn tất cả các log, nhấp chuột phải và chọn **Save Selected**).
12. Lưu tệp dưới định dạng `.txt`.
13. Mở tệp log console lên và đảm bảo rằng có mốc thời gian và dòng chữ 'Navigated to' cùng địa chỉ trang web đang kiểm thử.

---

### Log Safari trên iOS qua máy tính Windows

*Phương pháp này hiện không còn hoạt động, chúng tôi sẽ sớm tìm phương án thay thế.*

#### Điều kiện tiên quyết
Tải xuống và cài đặt các phần mềm dưới đây trên máy tính Windows 💻 của bạn:
*   iTunes
*   Node.js

#### Các bước thiết lập ban đầu
1.  Mở CMD trên máy tính của bạn (Mở Start Menu > Tìm kiếm **CMD**).
2.  Sao chép lệnh dưới đây, dán vào CMD và nhấn Enter:
    `npm i safari-console-logs-windows -g`
3.  Trên thiết bị iOS 📱 của bạn, mở **Settings** (Cài đặt), cuộn xuống chọn **Apps** > **Safari** > **Advanced** và bật **Web Inspector** (Trình kiểm tra web).

#### Các bước thu thập Log
1.  Kết nối thiết bị iOS với máy tính Windows bằng cáp USB.
2.  Mở CMD và chạy lệnh dưới đây:
    `remotedebug_ios_webkit_adapter --port=9222`
3.  Mở trình duyệt Google Chrome trên máy tính 💻 và truy cập địa chỉ `chrome://inspect/#devices`.
4.  Trên thiết bị iOS 📱 của bạn, mở trình duyệt Safari và truy cập vào trang web đang kiểm thử.
5.  Trên máy tính 💻 của bạn, đợi thiết bị hiển thị trong mục **Remote Target** (Nhìn trang web bạn đã mở thay vì tên thiết bị thực tế).
6.  Nhấp vào tùy chọn **Inspect** (Kiểm tra) để mở cửa sổ console.
7.  Trên cửa sổ console, nhấp vào menu ba chấm ở góc trên bên phải, chọn **Settings** (Cài đặt).
8.  Tại phần **Console**, tích chọn **Show Timestamps** và **Preserve logs upon navigation**.
9.  Đóng cửa sổ cài đặt bằng cách nhấn phím **Escape (ESC)**.
10. Trên thiết bị di động 📱 của bạn, tải lại trang chủ của trang web kiểm thử rồi tái hiện lỗi từ đầu đến cuối.
11. Trên máy tính 💻 của bạn, lưu log bằng cách nhấp chuột phải và chọn **Save as** (Lưu dưới dạng), hoặc sao chép toàn bộ log dán vào ứng dụng ghi chú rồi lưu lại dưới dạng `.txt`.
12. Tải các tệp log lên báo cáo lỗi (issue report).

**Lưu ý**:
*   Bạn cần bật các thiết lập Show Timestamps và Preserve logs mỗi lần mở menu inspect để thu thập log.
*   Nếu không thể lưu log từ cửa sổ Console, hãy thử tắt tùy chọn **"Group Similar Messages"** tại Console > Bánh răng Settings > Preferences.

---

### Log Chrome trên iOS qua máy Mac

1.  Trên thiết bị iOS 📱 của bạn, mở Chrome, nhấn vào biểu tượng 3 chấm ở góc dưới cùng bên phải và chọn **Settings** > **Content Settings** > **Web Inspector**, sau đó bật **Web Inspector**.
2.  Kết nối trực tiếp thiết bị iOS 📱 của bạn với máy Mac bằng cáp, đảm bảo chọn Tin cậy máy Mac này.
3.  Trên thiết bị iOS 📱 của bạn, mở Chrome và duy trì một tab mở.
4.  Trên máy Mac, mở Safari và chọn **Settings**.
5.  Mở tab **Advanced** (Nâng cao) và tích chọn **Show features for web developers**.
6.  Đóng cửa sổ cài đặt lại, chọn **Develop** (Phát triển) > [Tên thiết bị iOS của bạn] > [Tùy chọn tab Chrome đang mở].
7.  Trình kiểm tra web (Web Inspector) sẽ mở ra; chuyển đến tab **Console**.
8.  Tại cửa sổ console, từ menu hamburger chọn **Preserve Log**, và nhấp vào biểu tượng thùng rác để xóa sạch các log.
9.  Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ trên thiết bị iOS 📱 của bạn.
10. Để lưu log, nhấn tổ hợp phím **Command+S** (hoặc nhấn **Command+A** để chọn tất cả các log, nhấp chuột phải và chọn **Save Selected**).
11. Lưu tệp dưới định dạng `.txt`.

**Lưu ý**: Nếu bạn không thấy tab Chrome đang mở được liệt kê dưới tên thiết bị iOS của mình trong menu Develop sau bước 5, hãy thử đóng và mở lại ứng dụng Chrome trên iPhone của bạn. Việc này sẽ làm mới phiên làm việc và giúp máy Mac phát hiện tab đang mở.

---

### Log Firefox trên iOS qua máy Mac

1.  Kết nối trực tiếp thiết bị iOS của bạn với máy Mac bằng cáp, đảm bảo chọn Tin cậy máy Mac này.
2.  Trên thiết bị iOS 📱 của bạn, mở Firefox và duy trì một tab mở.
3.  Trên máy Mac của bạn, mở Safari và chọn **Settings** (Cài đặt).
4.  Mở tab **Advanced** (Nâng cao) và tích chọn tùy chọn **Show features for web developers**.
5.  Đóng lại cài đặt, chọn **Develop** (Phát triển) > [Tên thiết bị iOS của bạn] > [Tùy chọn tab Firefox đang mở].
6.  Trình kiểm tra web (Web Inspector) sẽ mở ra; chuyển đến tab **Console**.
7.  Tại cửa sổ console, từ menu hamburger chọn **Preserve Log**, và nhấp vào biểu tượng thùng rác để xóa sạch các log.
8.  Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ trên thiết bị iOS 📱 của bạn.
9.  Để lưu log, nhấn tổ hợp phím **Command+S** (hoặc nhấn **Command+A** để chọn tất cả các log, nhấp chuột phải và chọn **Save Selected**).
10. Lưu tệp dưới định dạng `.txt`.

**Lưu ý**: Nếu bạn không thấy tab Firefox đang mở được liệt kê dưới tên thiết bị iOS của mình trong menu Develop sau bước 5, hãy thử đóng và mở lại ứng dụng Firefox trên iPhone của bạn. Việc này sẽ làm mới phiên làm việc và giúp máy Mac phát hiện tab đang mở.
