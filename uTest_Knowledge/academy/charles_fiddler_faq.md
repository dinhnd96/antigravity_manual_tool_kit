# Câu hỏi thường gặp về Charles Proxy & Fiddler (Charles Proxy & Fiddler FAQ)

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Câu hỏi 1: Tôi gặp lỗi khi cài đặt Charles Proxy hoặc Fiddler; tôi nên làm gì?
**Trả lời**: Nếu bạn gặp bất kỳ sự cố nào trong quá trình cài đặt, hãy làm theo các bước dưới đây:
1. Đảm bảo bạn có quyền Quản trị viên (Admin permissions) trên máy tính của mình.
2. Nếu bạn đang sử dụng máy tính 32-bit, vui lòng tải xuống và cài đặt phiên bản cũ hơn của Charles Proxy hoặc Fiddler có hỗ trợ hệ thống 32-bit.
3. Cài đặt **JRE (Java Runtime Environment - Môi trường chạy Java)** trên máy tính của bạn [tại đây](https://www.oracle.com/java/technologies/downloads/).
4. Nếu bạn đang sử dụng máy tính Windows, hãy thử cài đặt **Visual C++** [tại đây](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist).

### Câu hỏi 2: Tại sao chúng ta cần cài đặt chứng chỉ gốc Charles (Charles root certificate) hoặc chứng chỉ gốc Fiddler (Fiddler root certificate)?
**Trả lời**: Việc cài đặt chứng chỉ gốc cho phép Charles Proxy hoặc Fiddler giải mã lưu lượng mạng HTTPS (decrypt HTTPS traffic).

### Câu hỏi 3: Định dạng tệp chính xác để tải lên log Charles Proxy và Fiddler là gì? Tôi nên tải lên toàn bộ log hay chỉ chọn các mục cụ thể rồi lưu lại?
**Trả lời**: Đối với Charles Proxy, định dạng tệp chính xác là `.chls` hoặc `.chlz`; đối với Fiddler, định dạng là `.saz`.
Bạn luôn luôn phải tải lên **toàn bộ log**.

### Câu hỏi 4: Tôi nhận được thông báo lỗi "Cài đặt thất bại, không thể đọc chứng chỉ" ("Installation failed, unable to read certificate") khi cài đặt chứng chỉ gốc trên thiết bị Android. Tôi nên làm gì?
**Trả lời**: Làm theo các bước sau:
1. Mở **Settings (Cài đặt)** và điều hướng đến mục **Security (Bảo mật)**.
2. Tìm mục **Credential Storage (Kho lưu trữ thông tin xác thực)** và chạm vào **Install a Certificate (Cài đặt chứng chỉ)**.
3. Chọn tệp chứng chỉ đã tải xuống và tiến hành cài đặt.

### Câu hỏi 5: Lỗi "Không tìm thấy trang" ("Page not found") hiển thị sau khi tôi cấu hình cài đặt proxy trên thiết bị di động. Tôi nên làm gì?
**Trả lời**: Vui lòng đảm bảo các yếu tố sau:
* Charles Proxy hoặc Fiddler đang chạy trên máy tính khi bạn thiết lập địa chỉ IP proxy thủ công trong cài đặt của thiết bị di động.
* Thiết bị di động và máy tính kết nối vào cùng một mạng không dây (WiFi).
* VPN đã được tắt (trên cả thiết bị di động và máy tính).
* Cấu hình Tường lửa (Firewall) và phần mềm Diệt vi-rút (Antivirus) để cho phép Charles Proxy hoạt động. Nếu Charles bị chặn, tester sẽ không thể sử dụng để thu thập log. Thay vì tắt toàn bộ Tường lửa và phần mềm Diệt vi-rút, hãy thêm Charles làm danh sách ngoại lệ (exception) để đảm bảo nó hoạt động bình thường trong khi vẫn duy trì bảo mật hệ thống.
* Kiểm tra để đảm bảo tùy chọn kết nối WiFi trên máy tính của bạn được đặt là **"Public" (Công cộng)**, không phải **"Private" (Riêng tư)**.

### Câu hỏi 6: Tôi nhận được thông báo "Kết nối của bạn không an toàn" ("Your connection is not secure") khi cài đặt chứng chỉ trên thiết bị di động. Tôi nên làm gì?
**Trả lời**: Dưới đây là một số mẹo để khắc phục vấn đề này:
* Chạm vào **Advanced (Nâng cao)** và chọn **Proceed (Tiếp tục)** rồi cài đặt chứng chỉ đúng cách.
* Thử nhập trực tiếp địa chỉ `chls.pro/ssl` HOẶC `charlesproxy.com/getssl` mà không thêm giao thức `http://` hoặc `https://`.
* Đóng trình duyệt di động, đóng phần mềm Charles và thử lại; hoặc khởi động lại cả máy tính và thiết bị di động của bạn rồi thử lại.
* Thử xóa chứng chỉ khỏi máy tính và thiết bị di động nếu chúng đã được cài đặt từ trước, sau đó tiến hành cài đặt lại chứng chỉ trên cả hai thiết bị.

### Câu hỏi 7: Làm thế nào để đảm bảo log Charles hoặc Fiddler của tôi đã được giải mã?
**Trả lời**: Đối với Charles trước, bạn cần kiểm tra các biểu tượng nhỏ trong log của mình. Ý nghĩa của chúng như sau:
* **Biểu tượng hình tròn màu xanh**: Lưu lượng đã giải mã từ các trang web sử dụng giao thức HTTP/1.1.
* **Biểu tượng hình tia sét**: Lưu lượng đã giải mã từ các trang web sử dụng giao thức HTTP/2.0.
* **Biểu tượng dấu X màu đỏ**: Nếu tất cả các mục đều có biểu tượng này, có nghĩa là chứng chỉ chưa được cài đặt hoặc cài đặt chưa đúng cách.
* **Biểu tượng hình khóa**: Dữ liệu chưa được giải mã và không thể đọc được (cấu hình SSL chưa được thiết lập chính xác, vui lòng xem lại Bước 8 trong bài học thứ hai [tại đây](file:///Users/mac/antigravity-testing-kit/uTest_Knowledge/academy/charles_proxy_for_desktop.md)).

Vì vậy, nếu log Charles Proxy của bạn chỉ chứa các biểu tượng hình khóa và dấu X màu đỏ, điều đó có nghĩa là dữ liệu chưa được giải mã. Xem hình minh họa bên dưới để biết log Charles khi đã giải mã và chưa giải mã trông như thế nào.

*[Hình: So sánh giao diện log Charles Proxy đã giải mã (chứa vòng tròn xanh, tia sét) và chưa giải mã (chứa biểu tượng ổ khóa và dấu X đỏ)]*

Đối với Fiddler, bạn sẽ nhận thấy biểu tượng ổ khóa đóng bên cạnh các mục khi Fiddler không giải mã được lưu lượng HTTPS.

### Câu hỏi 8: Không có thông tin lưu lượng mạng nào hiển thị theo yêu cầu. Tất cả chúng đều có biểu tượng ổ khóa. Tôi nên làm gì?
**Trả lời**: Điều này có nghĩa là thiết lập proxy SSL của bạn chưa được cấu hình đúng cách. Làm theo các bước sau:
1. Mở Charles Proxy, nhấp vào **Proxy** và chọn **SSL Proxy Settings**. Kích hoạt hộp kiểm **Enable SSL Proxying**, sau đó nhấp vào nút **Add** trong mục *Include*.
2. Trong cửa sổ popup *Edit Location*, nhập `*` cho trường **Host** và `443` cho trường **Port**.
   * Việc nhập `*` trong trường Host sẽ giải mã tất cả lưu lượng mạng.

### Câu hỏi 9: Làm thế nào để xóa chứng chỉ gốc đã cài đặt khỏi thiết bị của tôi?
**Trả lời**: Tên của các chứng chỉ đã cài đặt là:
* **Charles**: `Charles Proxy CA`
* **Fiddler**: `DO_NOT_TRUST_FiddlerRoot`

Để xóa chứng chỉ đã cài đặt, làm theo các bước dưới đây:
* **Windows**: Nhấn tổ hợp phím `Windows+R`, gõ `certmgr.msc` và nhấn Enter. Di chuyển đến mục **Trusted Root Certification Authorities** và tìm chứng chỉ gốc theo tên, nhấp chuột phải vào chứng chỉ đó và chọn **Delete**.
* **macOS**: Mở **Keychain Access (Trình quản lý chuỗi khóa)** và tìm kiếm theo tên chứng chỉ, nhấp chuột phải vào chứng chỉ và chọn xóa.
* **Android 10 trở lên**: Truy cập **Settings (Cài đặt) > Security & Lock Screen (hoặc Security - Bảo mật) > Encryption & Credentials (Mã hóa & Thông tin xác thực) > Trusted credentials (Thông tin xác thực đáng tin cậy)** > tab **User (Người dùng)** > Chạm vào chứng chỉ và chọn xóa.
* **Samsung Android 10 trở lên**: Truy cập **Settings (Cài đặt) > Biometrics and security (Sinh trắc học và bảo mật) > Other security settings (Cài đặt bảo mật khác) > User certificates (Chứng chỉ người dùng)** > Chạm vào chứng chỉ Charles > Chọn **Remove (Xóa)**.
* **Thiết bị Xiaomi**: Truy cập **Settings (Cài đặt) > Password & security (Mật khẩu & bảo mật) > Privacy (Bảo mật) > Encryption & credentials (Mã hóa & thông tin xác thực) > Trusted credentials (Thông tin xác thực đáng tin cậy)** > tab **User (Người dùng)** > Chạm vào chứng chỉ Charles > Chọn **Remove (Xóa)**.
* **Các phiên bản Android cũ**: Điều hướng đến **Settings (Cài đặt) > Security Settings (Cài đặt bảo mật) > View security certificates (Xem chứng chỉ bảo mật)** > Chạm vào chứng chỉ Charles hoặc chứng chỉ gốc Fiddler > Chọn **Remove (Xóa)**.
* **Thiết bị Huawei**: Truy cập **Settings (Cài đặt) > Security & Privacy (Bảo mật & Quyền riêng tư) > More (Thêm) > Trusted Credentials (Thông tin xác thực đáng tin cậy) > User (Người dùng)** > Chạm vào chứng chỉ Charles > Chọn **Remove (Xóa)**.
* **iOS 15 trở lên**: Điều hướng đến **Settings (Cài đặt) > General (Cài đặt chung) > VPN & Device Management (Quản lý VPN & Thiết bị)**, chọn cấu hình chứng chỉ gốc tương ứng và xóa nó.
* **Các phiên bản iOS cũ**: Điều hướng đến **Settings (Cài đặt) > General (Cài đặt chung) > Profile & Device Management (Quản lý cấu hình & Thiết bị)**, chọn cấu hình chứng chỉ gốc tương ứng và xóa nó.

### Câu hỏi 10: Tôi nhận được thông báo "Lỗi kết nối an toàn" ("Secure Connection Failed") hoặc "Kết nối không an toàn" ("Connection is not secure") và biểu tượng ổ khóa có vạch đỏ chéo trên thanh địa chỉ URL khi cố gắng truy cập trang web kiểm thử hoặc bất kỳ trang web nào. Tôi nên làm gì?
**Trả lời**:
Chứng chỉ gốc Charles có thể đã hết hạn. Để kiểm tra chứng chỉ đã cài đặt, thực hiện theo các bước sau:
* **Windows**: Nhấn tổ hợp phím `Windows+R`, gõ `certmgr.msc` và nhấn Enter. Di chuyển đến mục **Trusted Root Certification Authorities**, tìm chứng chỉ gốc theo tên, mở chứng chỉ đó ra và kiểm tra ngày hết hạn tại mục **"Not valid after" (Không hợp lệ sau ngày)**.
* **macOS**: Mở **Keychain Access (Trình quản lý chuỗi khóa)**, tìm kiếm theo tên chứng chỉ, mở ra và kiểm tra ngày hết hạn tại mục **"Not valid after"**.

Nếu chứng chỉ thực sự đã hết hạn, bạn sẽ phải đặt lại hoặc xóa nó khỏi các thiết bị của mình (cả Máy tính và Điện thoại).

#### Giải pháp 1: Đặt lại chứng chỉ gốc Charles (Reset Charles Root Certificate)
Làm theo các bước dưới đây để đặt lại chứng chỉ gốc Charles:
1. Mở Charles.
2. Nhấp vào menu **Help**.
3. Tại mục **SSL Proxying**, chọn **"Reset Charles Root Certificate"**.
4. Chọn **"Reset"** và sau đó đóng rồi mở lại phần mềm Charles.
5. Sau đó, làm theo hướng dẫn trong bài học [Charles Proxy cho Máy tính](file:///Users/mac/antigravity-testing-kit/uTest_Knowledge/academy/charles_proxy_for_desktop.md) và [Charles Proxy cho Thiết bị Di động](file:///Users/mac/antigravity-testing-kit/uTest_Knowledge/academy/charles_proxy_for_mobile.md) để cài đặt chứng chỉ mới trên Máy tính và Điện thoại di động của bạn.

#### Giải pháp 2: Xóa chứng chỉ gốc Charles (Remove Charles Root Certificate)
Làm theo hướng dẫn ở Câu hỏi số 9 để biết cách xóa chứng chỉ gốc, sau đó làm theo hướng dẫn cài đặt chứng chỉ mới trong bài học Charles Proxy cho Máy tính và Charles Proxy cho Thiết bị Di động.

*Lưu ý: Sau khi thử một trong các giải pháp trên, bạn có thể cần khởi động lại phần mềm Charles và trình duyệt trên điện thoại di động của mình. Ngoài ra, bạn có thể khởi động lại cả Máy tính và Điện thoại di động nếu cần thiết.*

### Câu hỏi 11: Tôi không thể tải xuống chứng chỉ bằng cách nhập URL (`chls.pro/ssl` hoặc `charlesproxy.com/getssl`) trên thiết bị di động của mình, do đó tôi không thể lấy log Charles và không thể truy cập bất kỳ trang web nào khi mở ứng dụng Charles. Tôi nên làm gì?
**Trả lời**: Trong trường hợp đó, bạn cần tải tệp chứng chỉ về máy tính, sau đó chuyển tệp này sang thiết bị di động để cài đặt thủ công. Vui lòng làm theo hướng dẫn dưới đây:
1. Mở phần mềm Charles trên máy tính của bạn.
2. Truy cập **Help > SSL Proxying > Save Charles Root Certificate**.
3. Thay đổi định dạng tệp từ mặc định là `.pem` thành `.cer` và lưu vào một thư mục trên máy tính mà bạn dễ nhớ.
4. Chuyển tệp `.cer` sang thiết bị di động của bạn (sử dụng thẻ nhớ SD, cáp USB, tự gửi email cho chính mình, hoặc chuyển qua mạng như Google Drive).
5. Mở tệp đó trên thiết bị di động.
   * *Lưu ý: Trên iOS, trước tiên bạn cần tải tệp chứng chỉ về thiết bị, sau đó chạm vào tệp chứng chỉ từ vị trí bạn đã tải xuống trên thiết bị.*
6. Xác nhận mã PIN của điện thoại.
   * Nếu thiết bị di động của bạn chưa cài mã PIN, hệ thống sẽ nhắc bạn thiết lập mã PIN mới.
7. Đặt tên cho chứng chỉ và chạm vào **Okay**.
8. Khởi động lại ứng dụng Charles và làm theo hướng dẫn từ Bước 5 của bài học liên quan.

### Câu hỏi 12: Tệp log Charles của tôi rất lớn và không thể tải lên báo cáo lỗi (bug report), tôi phải làm gì để giảm bớt dung lượng tệp log?
**Trả lời**: Đảm bảo xóa sạch lưu lượng mạng trước khi bạn bắt đầu tái hiện lỗi, hãy làm theo các bước sau:
1. Mở Charles Proxy.
2. Nhấp vào biểu tượng **Chổi quét (Broom)** để xóa toàn bộ lưu lượng mạng đã phát sinh từ trước.
3. Tái hiện lỗi.
4. Nhấp vào nút **Stop Recording (Dừng ghi)**.
5. Lưu phiên làm việc.

### Câu hỏi 13: Tôi không nhận được bất kỳ cửa sổ popup/thông báo/yêu cầu "cho phép kết nối" ("allow connection") nào trên phần mềm Charles khi đang cố mở một trang web trên điện thoại di động của mình. Tôi nên làm gì?
**Trả lời**:
* Kiểm tra để đảm bảo tùy chọn kết nối WiFi trên máy tính của bạn được đặt là **"Public" (Công cộng)**, không phải **"Private" (Riêng tư)**.
* Khởi động lại cả hai thiết bị, sau đó mở bất kỳ trang web nào trên điện thoại di động sau khi đã kết nối điện thoại với Charles.

### Câu hỏi 14: Tôi nên làm gì nếu không thể kết nối Internet sau khi thiết lập proxy Charles trên điện thoại?
**Trả lời**: Bạn có thể thêm địa chỉ IP của điện thoại vào danh sách cho phép của Charles bằng cách làm theo các bước sau:
1. Mở Charles Proxy.
2. Nhấp vào menu **Proxy**.
3. Chọn mục **Access Control Settings (Thiết lập kiểm soát truy cập)**.
4. Nhấp vào nút **Add**.
5. Nhập địa chỉ IP cục bộ của điện thoại (bạn có thể tìm thấy trong cài đặt Wi-Fi của điện thoại).
6. Nhấp vào nút **OK**.

### Câu hỏi 15: Làm thế nào để giải quyết lỗi bảo mật chứng chỉ ("Tệp này không hợp lệ để sử dụng làm: Chứng chỉ bảo mật" - "This file is invalid for use as the following:Security certificate") khi sử dụng phiên bản Charles Proxy mới nhất trên Windows 11?
**Trả lời**:
1. Mở Charles Proxy và đảm bảo tùy chọn Windows Proxy đã được kích hoạt (**Proxy > Windows Proxy**).
2. Khi phần mềm Charles Proxy đang mở, truy cập trang `chls.pro/ssl` từ trình duyệt của bạn để tải xuống chứng chỉ tự động.
   * Nếu trình duyệt cảnh báo về việc tải xuống, hãy chọn tiếp tục tải xuống.
3. Mở Trình quản lý chứng chỉ Windows (Windows Certificate Manager): Nhấn tổ hợp phím `Win + R`, gõ `certmgr.msc` and nhấn Enter.
4. Trong Certificate Manager, nhấp chuột phải vào thư mục **Trusted Root Certification Authorities (Cơ quan chứng nhận gốc đáng tin cậy)**, chọn **All Tasks > Import...**.
5. Nhấp **Next** rồi chọn **Browse** để tìm tệp chứng chỉ đã tải xuống.
   * Nếu bạn không tìm thấy tệp, hãy đổi bộ lọc định dạng tệp thành **All Files (*.*)**.
6. Chọn chứng chỉ, nhấp **Open**, sau đó nhấp **Next**, tiếp tục chọn **Next** và nhấn **Finish**.
7. Chọn **Yes** trên cửa sổ cảnh báo bảo mật hiện ra, sau đó nhấn **OK** trên cửa sổ thông báo thành công.
8. **Khởi động lại máy tính của bạn (bước này vô cùng quan trọng)**.
9. Tiến hành thiết lập SSL Proxying trong Charles Proxy.

### Câu hỏi 16: Tôi nên làm gì nếu có các lưu lượng mạng không liên quan từ máy tính xuất hiện khi đang ghi log trên thiết bị di động hoặc ngược lại?
**Trả lời**:

| Thu thập lưu lượng mạng từ | Kích hoạt tùy chọn này trong Charles |
|---|---|
| Trình duyệt Chrome hoặc Edge trên máy tính | `Proxy > Windows Proxy` |
| Safari trên macOS | `Proxy > macOS Proxy` |
| **Chỉ** thiết bị di động | 1. Thiết lập proxy thủ công trên thiết bị di động (Cài đặt Wi-Fi).<br>2. Trong Charles: **Vô hiệu hóa (Disable) Windows Proxy** |
