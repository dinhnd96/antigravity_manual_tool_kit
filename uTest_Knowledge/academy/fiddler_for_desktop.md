# Fiddler cho Máy tính (Fiddler for Desktop)

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Fiddler Classic và Fiddler Everywhere
* **Fiddler Classic**: Chỉ hoạt động trên hệ điều hành Windows và đi kèm đầy đủ tất cả các tính năng cũng như tùy chọn của Fiddler.
* **Fiddler Everywhere**: Được thiết kế để chạy đa nền tảng (Windows, macOS và Linux), cung cấp giao diện người dùng (UI) hiện đại, trực quan hơn cùng các tính năng nâng cao phục vụ kiểm thử hiệu năng và gỡ lỗi web (web debugging).

Fiddler Everywhere không phải phần mềm miễn phí. Bạn chỉ có thể sử dụng miễn phí trong thời gian dùng thử 10 ngày. Sau khi hết hạn dùng thử, ứng dụng sẽ không thể được sử dụng để ghi (capture), kiểm tra (inspect), chỉnh sửa (edit) hoặc tạo (compose) các yêu cầu HTTP/HTTPS.

Hãy nhớ kiểm tra kỹ tài liệu tổng quan chu kỳ (cycle overview) để biết cần sử dụng phần mềm nào. Nếu không có thông tin đó, bạn có thể xác nhận lại với đội ngũ quản lý dự án để chọn công cụ phù hợp với yêu cầu của dự án. Nếu bạn được yêu cầu sử dụng phần mềm khác không có trong danh sách này, hãy sử dụng phần mềm chính xác theo hướng dẫn.

*\*Để sử dụng thương mại Fiddler Everywhere, bạn cần phải mua giấy phép (license). Bằng việc sử dụng phần mềm này, bạn đồng ý chấp thuận các điều khoản và điều kiện được nêu trong thỏa thuận cấp phép người dùng cuối (EULA). Mỗi cá nhân người dùng tự chịu trách nhiệm đảm bảo việc sử dụng phần mềm của mình tuân thủ đúng các điều khoản trong thỏa thuận cấp phép.*

### Cách ghi log bằng Fiddler Everywhere

### Cách ghi log bằng Fiddler Classic

Tải xuống và cài đặt Fiddler Classic [tại đây](https://www.telerik.com/fiddler/fiddler-classic) hoặc Fiddler Everywhere [tại đây](https://www.telerik.com/fiddler/fiddler-everywhere).

#### Fiddler Everywhere
Bạn phải Đăng nhập (Sign In) hoặc Đăng ký (Sign Up) nếu chưa có tài khoản, hoặc sử dụng thông tin đăng nhập (credentials) nếu được cung cấp trong tài liệu tổng quan chu kỳ hoặc test case.

#### Kích hoạt tính năng ghi lưu lượng HTTPS (HTTPS Traffic capture)

##### Fiddler Everywhere
1. Nhấp vào biểu tượng **Cài đặt (Settings)** hình bánh răng ở góc trên bên phải.
2. Tại tab **HTTPS**, nhấp vào nút **Trust Fiddler CA**.
   * **Windows**: Chọn **Yes** trong cửa sổ popup mở ra để xác nhận cài đặt.
   * **macOS**: Nhập thông tin đăng nhập quản trị viên (administrative credentials) của máy tính trong cửa sổ popup để tin cậy chứng chỉ.
3. Kích hoạt tùy chọn **Capture HTTPS traffic**.
4. Nhấp vào nút **Save** để lưu các thay đổi và đóng cửa sổ Cài đặt bằng cách nhấp vào nút **X**.

##### Fiddler Classic
1. Nhấp vào menu **Tools**.
2. Chọn **Options**.
3. Tại tab **HTTPS**, kích hoạt tùy chọn **Decrypt HTTPS traffic**.
4. Chọn **Yes** trong cửa sổ popup mở ra để tin cậy chứng chỉ gốc Fiddler Classic Root.
5. Xác nhận **Yes** để cài đặt chứng chỉ trong các cửa sổ tiếp theo.
6. Chọn **Yes** để xác nhận thêm chứng chỉ vào Danh sách chứng chỉ gốc tin cậy (Trusted Root List) của máy tính.
7. Chọn **Yes** để cho phép thay đổi và nhấp **OK** để đóng cửa sổ xác nhận thành công.
8. Nhấp vào nút **OK** để đóng cửa sổ Options.

#### Đóng các tab trình duyệt và ứng dụng chạy nền không cần thiết

#### Xóa các log đã lưu

##### Fiddler Everywhere
1. Mở khung **Traffic** ở thanh bên trái.
2. Nhấp vào nút **Remove All**.

##### Fiddler Classic
* Nhấp vào biểu tượng **X** trên thanh công cụ > Chọn **Remove all** hoặc nhấn tổ hợp phím `CTRL + X` trên bàn phím.

#### Bật chế độ Ghi lưu lượng hệ thống (System Capturing)

##### Fiddler Everywhere
* Trên khung **Traffic**, hãy đảm bảo nút chuyển **System Proxy** đang ở trạng thái **ON**.
* Nếu đang ở trạng thái **OFF**, hãy gạt sang **ON** để kích hoạt chế độ ghi lưu lượng hệ thống.

##### Fiddler Classic
* Nhấp vào menu **File** và đảm bảo tùy chọn **Capture Traffic** đã được kích hoạt.
* Nếu chưa kích hoạt, nhấp chọn để bật.

#### Xóa cache trình duyệt trước khi bắt đầu ghi log để đảm bảo mọi yêu cầu đều được gửi đi và ghi lại (Đối với kiểm thử web)

#### Tái hiện lỗi trên ứng dụng hoặc trang web kiểm thử bắt đầu từ trang chủ

#### Nếu bạn được yêu cầu loại bỏ các lưu lượng không mong muốn hiển thị trong danh sách phiên mạng, hãy làm theo các bước dưới đây:

##### Fiddler Everywhere
1. Trên khung **Traffic**, nhấp vào nút **Filters**.
2. Nhấp vào nút **Add Condition**.
   * Bạn có thể thêm số lượng điều kiện tùy ý. Trong ví dụ này, chúng tôi sẽ chỉ hiển thị các mục của Academybugs.
3. Thêm URL hoặc tên miền bạn muốn lọc (ví dụ: `academybugs`).
4. Nhấp vào nút **Apply**.
   * Bạn có thể tắt các bộ lọc đã áp dụng bằng cách bỏ chọn hộp kiểm (checkbox) tương ứng trong cửa sổ Filters và nhấp vào nút **Apply**.

##### Fiddler Classic
1. Mở tab **Filters**.
2. Kích hoạt hộp kiểm **Use Filters**.
   * Lọc lưu lượng theo hướng dẫn. Trong ví dụ này, chúng tôi sẽ chỉ hiển thị host `Academybugs.com` trong danh sách.
3. Nhấp vào menu thả xuống **No Host Filter** và đổi thành **Show only the following Hosts**.
4. Thêm host vào trường dữ liệu (ví dụ: `academybugs.com`).
5. Nhấp vào **Actions > Run Filterset now**.
   * Bạn có thể tắt bộ lọc bằng cách bỏ chọn hộp kiểm **Use Filters**.

#### Xuất phiên làm việc (Export)

##### Fiddler Everywhere
1. Nhấp vào một mục trong lưới danh sách phiên mạng (sessions grid).
2. Nhấn `CTRL + A` để chọn tất cả các mục.
3. Nhấp chuột phải vào một trong các mục đã chọn.
4. Chọn **Export**.
5. Chọn định dạng **Fiddler Archive (SAZ)** > Nhấp vào nút **Next**.
6. Nhấp vào nút ba chấm (`...`).
7. Chọn thư mục lưu trữ mong muốn và đổi tên tệp.
8. Nhấp vào nút **Save**.
9. Nhấp vào nút **Save** một lần nữa để xuất các phiên làm việc.

##### Fiddler Classic
1. Nhấp vào menu **File**.
2. Chọn **Save > All Sessions**.
3. Chọn thư mục lưu trữ mong muốn và đổi tên tệp.
4. Nhấp vào nút **Save**.

### Trình duyệt Firefox
Đối với trình duyệt Firefox, bạn cần thực hiện thêm các bước sau đây sau khi hoàn tất các bước trên:

1. Mở Firefox và nhấp vào menu Hamburger (Menu ứng dụng) ở góc trên bên phải.
2. Chọn **Settings (Cài đặt)**.
3. Tìm kiếm **Network Settings (Cài đặt mạng)** và mở nó.
4. Chọn tùy chọn **Use system proxy settings (Sử dụng cài đặt proxy hệ thống)**.
5. Nhấp vào nút **OK** để lưu các thay đổi.
   * Sau khi hoàn tất việc thu thập log, bạn có thể chuyển thiết lập này trở lại thành **No proxy**.

Đối với Fiddler Classic (Windows), hãy đảm bảo tin cậy Chứng chỉ gốc Fiddler (Fiddler Root Certificate). Thực hiện theo các bước dưới đây:
1. Mở Firefox và nhập `about:config` vào thanh địa chỉ.
2. Nhấp vào nút **Accept the Risk and Continue (Chấp nhận rủi ro và tiếp tục)**.
3. Tìm kiếm từ khóa `security.enterprise_roots.enabled`.
   * Nếu hiển thị giá trị là `true`, bạn có thể tiến hành ghi log.
   * Nếu hiển thị giá trị là `false`, nhấp vào biểu tượng mũi tên hai chiều hoặc nút chuyển đổi để đổi giá trị thành `true`.

### Fiddler Cap
Fiddler Cap là phiên bản rút gọn của Fiddler Classic, chỉ dùng cho mục đích ghi vết lưu lượng mạng (trace capture). Nó không yêu cầu các bước thiết lập phức tạp như hai phiên bản trên. Phần mềm này hiện chỉ khả dụng cho hệ điều hành Windows. Bạn chỉ được sử dụng công cụ này nếu có hướng dẫn cụ thể trong tài liệu tổng quan chu kỳ hoặc được yêu cầu trực tiếp bởi TTL hoặc TE của chu kỳ kiểm thử. Thực hiện theo hướng dẫn dưới đây để sử dụng:

1. Tải xuống và cài đặt Fiddler Cap [tại đây](https://www.telerik.com/fiddler/fiddlercap).
2. Mở **FiddlerCap**.
3. Kích hoạt tùy chọn **Decrypt HTTPS traffic**.
4. Nhấp vào **OK** và sau đó chọn **Yes** để cài đặt chứng chỉ.
5. Nhấp vào nút **Clear Cookies** và tiếp theo là nút **Clear Cache**.
6. Nhấp vào nút **1. Start Capture**.
7. Tái hiện lỗi trên trang web kiểm thử bắt đầu từ trang chủ.
8. Nhấp vào nút **2. Stop Capture** sau khi hoàn tất việc tái hiện lỗi.
9. Nhấp vào nút **3. Save Capture**.
10. Chọn thư mục lưu trữ mong muốn và đổi tên tệp.
11. Nhấp vào nút **Save**.
    * Khi bạn đóng ứng dụng, hệ thống sẽ nhắc bạn có muốn xóa chứng chỉ đã cài đặt hay không. Bạn có thể chọn **Yes** để xóa, và tiến hành cài đặt lại chứng chỉ mới khi sử dụng ứng dụng vào lần tiếp theo.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Fiddler Classic | Fiddler Classic | Phiên bản Fiddler truyền thống chỉ chạy trên hệ điều hành Windows |
| Fiddler Everywhere | Fiddler Everywhere | Phiên bản Fiddler đa nền tảng (Windows, macOS, Linux) với giao diện hiện đại |
| Fiddler Cap | Fiddler Cap | Phiên bản rút gọn của Fiddler Classic chuyên dùng để ghi vết lưu lượng mạng |
| Fiddler Archive (SAZ) | Fiddler Archive (SAZ) | Định dạng tệp lưu trữ các phiên làm việc của Fiddler |
| System Proxy | Proxy hệ thống (System Proxy) | Cấu hình định tuyến toàn bộ lưu lượng mạng của hệ điều hành qua máy chủ proxy |
| System Capturing | Ghi lưu lượng hệ thống (System Capturing) | Chế độ ghi lại toàn bộ lưu lượng mạng của hệ điều hành trên Fiddler |
| Traffic pane | Khung lưu lượng (Traffic pane) | Giao diện hiển thị danh sách các phiên mạng trên Fiddler |
| Run Filterset | Chạy bộ lọc (Run Filterset) | Hành động áp dụng bộ lọc lưu lượng đã thiết lập trên Fiddler |
