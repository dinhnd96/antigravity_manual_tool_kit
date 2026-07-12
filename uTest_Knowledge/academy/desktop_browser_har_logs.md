# Log HAR trình duyệt trên máy tính

> **Nguồn gốc**: uTest Academy - Desktop Browser HAR Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Trong khóa học này, chúng ta sẽ học cách thu thập log HAR trình duyệt. Các trình duyệt máy tính hoạt động giống nhau trên tất cả các hệ điều hành máy tính, vì vậy bạn có thể thực hiện theo các bước tương tự trên Windows, macOS hoặc Linux.

### Log HAR là gì?
HAR viết tắt của HTTP Archive (Kho lưu trữ HTTP). Log HAR chứa thông tin về các tương tác giữa trình duyệt và trang web mà bạn đang kiểm thử. Thông tin này giúp ích cho lập trình viên trong việc khắc phục sự cố và xác định nguyên nhân gốc rễ (root cause) của vấn đề.

Định dạng HAR được hỗ trợ bởi nhiều phần mềm khác nhau, chẳng hạn như:
*   Charles Proxy
*   Fiddler
*   Firebug
*   Firefox
*   Google Chrome
*   Microsoft Edge
*   OWASP ZAP

Trong khóa học này, chúng ta sẽ học cách thu thập và xem lại chúng thông qua các trình duyệt web phổ biến nhất.

### Những điều cần lưu ý
*   Hãy lưu ý rằng các tệp HAR có chứa dữ liệu nhạy cảm. Do đó, nếu lỗi bạn đang cố tái hiện có hiển thị Tên đăng nhập (Username), Mật khẩu (Password), mã PIN, mã CVV, Số tài khoản/IBAN, số thẻ hoặc bất kỳ thông tin cá nhân và nhạy cảm nào khác, hãy đảm bảo rằng tất cả các thông tin này đã được xóa khỏi tệp log HAR trước khi bạn tải lên báo cáo lỗi (Chúng tôi sẽ hướng dẫn bạn cách xóa các thông tin này khỏi log trong khóa học).
*   Đóng tất cả các tab khác đang mở trên trình duyệt của bạn khi bắt đầu ghi log HAR.
*   Chỉ tải lên log này nếu có yêu cầu từ TTL, TE hoặc TSM của chu kỳ kiểm thử.

### Cách thu thập log HAR

#### Google Chrome / Và các trình duyệt nhân Chromium

1.  Nhấn tổ hợp phím **CTRL+Shift+I** (Windows) / **Option+Command+I** (Mac) hoặc chọn **biểu tượng ba dấu chấm** > **Công cụ khác (More Tools)** > **Công cụ nhà phát triển (Developer Tools)**.
2.  Mở tab **Network** (nếu không thấy tab Network, hãy nhấp vào **biểu tượng >>** hoặc mở rộng cửa sổ Công cụ nhà phát triển).
3.  Tích chọn ô **Preserve log** (Giữ log).
4.  Xóa sạch các lưu lượng hiện tại bằng cách nhấp vào **biểu tượng Clear (Xóa)** 🚫.
5.  Mở trang web kiểm thử và tái hiện lỗi.
6.  Nhấp chuột phải hoặc nhấn **CTRL + nhấp chuột** (Mac) vào phần log và chọn **Save all as HAR with content** (Lưu tất cả dưới dạng HAR kèm nội dung).
7.  Hoặc bạn có thể nhấp vào **nút Export HAR** (biểu tượng tải xuống) ở đầu tab Network.
8.  Lưu tệp dưới định dạng `.har`.

**Lưu ý**: Thực hiện theo các bước tương tự để thu thập log HAR cho các trình duyệt nhân Chromium khác như Microsoft Edge mới, Opera, Brave, Yandex.

##### Kiểm tra Mã trạng thái (Status code) và lọc Log
Bạn có thể được yêu cầu kiểm tra mã trạng thái (Status code) của một số bản ghi log nhất định. Để thực hiện:
1.  Nhấp chọn bản ghi log mong muốn.
2.  Tại tab **Headers** -> phần **General**, kiểm tra giá trị của trường **Status code** (ví dụ: `200 OK`, `400 Bad Request`).

Bạn có thể nhanh chóng tìm thấy các bản ghi log cụ thể bằng cách sử dụng bộ lọc (filter):
1.  Nhấp vào **biểu tượng hình phễu** ở đầu tab Network.
2.  Nhập từ khóa vào hộp văn bản xuất hiện.

#### Firefox

1.  Nhấn tổ hợp phím **CTRL+Shift+E** (Windows) / **Option+Command+I** (Mac) hoặc mở **Menu** > **More Tools** > **Web Developer Tools**.
2.  Mở tab **Network** (nếu không thấy tab Network, hãy nhấp vào **biểu tượng >>** hoặc mở rộng cửa sổ Công cụ nhà phát triển).
3.  Nhấp vào **biểu tượng bánh răng** và chọn **Persist Logs** (Giữ log).
4.  Xóa sạch các lưu lượng hiện tại bằng cách nhấp vào **biểu tượng Thùng rác**.
5.  Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ.
6.  Nhấp chuột phải hoặc nhấn **CTRL + nhấp chuột** (Mac) vào phần log và chọn **Save All As HAR** (Lưu tất cả dưới dạng HAR).
7.  Hoặc bạn có thể nhấp vào **biểu tượng bánh răng** và chọn tùy chọn **Save All As HAR**.
8.  Lưu tệp dưới định dạng `.har`.

##### Cách lọc và xác minh mã trạng thái (Status code) trong log HAR trên Chrome
Trong một số chu kỳ kiểm thử, bạn có thể được yêu cầu lọc các bản ghi log cụ thể và xác minh mã trạng thái trong log HAR. Để làm điều đó, hãy làm theo các bước dưới đây:
1.  Mở cửa sổ console và thu thập log HAR theo hướng dẫn ở phần Cách thu thập log HAR.
2.  Nhấp vào trường **Filter** (Bộ lọc) và nhập chuỗi ký tự hoặc mã code được cung cấp trong phần tổng quan chu kỳ (cycle overview) hoặc kịch bản kiểm thử (test case).
3.  Nhấp chọn bản ghi log bạn vừa lọc.
4.  Trên cửa sổ mở ra, chuyển sang tab **Headers**.
5.  Kiểm tra **Status code** tại phần **General** và xác minh xem nó đã chính xác như hướng dẫn trong chu kỳ kiểm thử chưa.
6.  Lưu ý rằng mã trạng thái (Status code) có thể thay đổi tùy thuộc vào phản hồi từ máy chủ. Hãy xác minh xem nó có khớp với yêu cầu không, và làm theo hướng dẫn của chu kỳ/kịch bản kiểm thử nếu có sự khác biệt.

#### Safari

1.  Nhấp chọn **Safari** trên thanh menu và chọn **Settings** (Cài đặt/Thiết lập).
2.  Mở tab **Advanced** (Nâng cao) > tích chọn **Show features for web developers** (Hiển thị các tính năng cho nhà phát triển web).
3.  Đóng cửa sổ cài đặt lại và nhấn tổ hợp phím **Option+Command+I** hoặc nhấp vào **Develop** (Phát triển) trên thanh menu phía trên > chọn **Show Web Inspector** (Hiển thị Trình kiểm tra Web).
4.  Mở tab **Network** (nếu không thấy tab Network, hãy nhấp vào **biểu tượng >>** hoặc mở rộng cửa sổ Công cụ nhà phát triển).
5.  Từ menu hamburger ở góc trên bên trái tab Network, chọn **Preserve Log** (Giữ log) (nếu không thấy tùy chọn Preserve Log, hãy mở rộng cửa sổ Công cụ nhà phát triển).
6.  Xóa sạch tab bằng cách nhấp vào **biểu tượng Thùng rác**.
7.  Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ.
8.  Nhấp chuột phải hoặc nhấn **CTRL + nhấp chuột** vào cột **Name** của log và chọn **Export HAR**.
9.  Hoặc bạn có thể nhấp vào **nút Export** ở góc trên cùng bên phải.
10. Lưu tệp dưới định dạng `.har`.

##### Kiểm tra Mã trạng thái (Status code) và lọc Log
Bạn có thể được yêu cầu kiểm tra mã trạng thái (Status code) của một số bản ghi log nhất định. Để thực hiện:
1.  Nhấp chọn bản ghi log mong muốn.
2.  Tại tab **Headers** > phần **Summary**, kiểm tra giá trị của trường **Status** (ví dụ: `200 OK`, `400 Bad Request`).

Bạn có thể nhanh chóng tìm thấy các bản ghi log cụ thể bằng cách sử dụng bộ lọc (filter):
1.  Trong hộp văn bản **Filter Full URL** ở đầu tab Network, nhập từ khóa cần tìm.

---

### Cách chỉnh sửa tệp log HAR

#### Windows 10

1.  Mở tệp HAR bằng chương trình soạn thảo văn bản như Notepad hoặc Notepad++.
2.  Sử dụng tính năng thay thế (Replace) của trình soạn thảo văn bản để tìm kiếm thông tin bạn muốn xóa.
3.  Ví dụ: Tìm kiếm họ tên đầy đủ, địa chỉ, số an sinh xã hội (SSN), ngày sinh, số điện thoại, số tài khoản ngân hàng, số thẻ, mã CVV hoặc bất kỳ thông tin nhạy cảm nào bạn đã cung cấp khi kiểm thử trang web.
4.  Thay thế thông tin đó bằng ký tự `****` hoặc sử dụng bất kỳ văn bản giữ chỗ nào khác để biểu thị rằng nó đã được ẩn đi (redacted).
5.  Lưu tệp.
6.  Chỉ tải tệp log HAR lên báo cáo lỗi hoặc kịch bản kiểm thử của bạn khi được yêu cầu.

#### macOS

1.  Mở tệp HAR bằng ứng dụng **TextEdit** mặc định.
2.  Di chuột qua mục **Find** (Tìm kiếm) và chọn tùy chọn **Find and Replace** (Tìm kiếm và Thay thế).
3.  Tìm kiếm thông tin bạn muốn xóa khỏi log HAR và thay thế bằng ký tự `****` hoặc văn bản giữ chỗ khác để biểu thị rằng nó đã được ẩn đi.
4.  Ví dụ: Tìm kiếm họ tên đầy đủ, địa chỉ, số an sinh xã hội (SSN), ngày sinh, số điện thoại, số tài khoản ngân hàng, số thẻ, mã CVV hoặc bất kỳ thông tin nhạy cảm nào khác mà bạn đã cung cấp trong lúc kiểm thử trang web, và sau đó thay thế nó.
5.  Lưu tệp.
6.  Chỉ tải tệp log HAR lên báo cáo lỗi hoặc kịch bản kiểm thử của bạn khi được yêu cầu.

**Lưu ý**: Bạn cũng có thể sử dụng Notepad++ hoặc bất kỳ trình soạn thảo văn bản nào khác và làm theo các bước tương tự như hướng dẫn dành cho Windows.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| HAR Logs | Log HAR (HTTP Archive) | Log ghi lại các tương tác HTTP/HTTPS giữa trình duyệt và trang web |
| Status Code | Mã trạng thái (Status Code) | Mã phản hồi từ máy chủ (ví dụ: 200 OK, 400 Bad Request) |
| Sensitive Data | Dữ liệu nhạy cảm | Thông tin cá nhân cần bảo mật (như mật khẩu, số thẻ ngân hàng, PIN) |
