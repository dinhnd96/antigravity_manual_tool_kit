# Lọc lưu lượng truy cập trên Charles Proxy

> **Nguồn gốc**: uTest Academy - Charles Proxy Filter Traffic
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Tại sao bạn cần lọc lưu lượng truy cập?
Trong một số dự án, bạn sẽ được yêu cầu lọc bỏ các host không mong muốn để thu được tệp log chỉ chứa thông tin liên quan đến lỗi hoặc tác vụ kiểm thử. Điều này sẽ giúp khách hàng và đội ngũ phát triển tìm kiếm thông tin họ cần một cách dễ dàng và nhanh chóng hơn.

Trong khóa học này, chúng ta sẽ tìm hiểu cách loại trừ (exclude) một số lưu lượng truy cập, chỉ giữ lại (include) lưu lượng cụ thể, hoặc lọc lưu lượng cụ thể trong log Charles.

Nhìn chung, bạn nên sử dụng hồ sơ cấu hình Charles Proxy được cung cấp hoặc thiết lập Charles theo đúng hướng dẫn trong chu kỳ kiểm thử. Nếu không có hồ sơ cấu hình hay hướng dẫn cụ thể nào, bạn nên xác nhận lại với TTL hoặc TE xem có yêu cầu đặc biệt nào không; nếu không, bạn có thể sử dụng cấu hình mặc định để thu thập toàn bộ lưu lượng mạng mà không cần thêm bất kỳ tùy chọn include hay exclude nào.

---

### Cách chỉ giữ lại (Include) lưu lượng truy cập cụ thể trong log Charles

Thiết lập này sẽ chỉ ghi lại lưu lượng truy cập từ tên miền (domain) bạn đã chỉ định và bỏ qua toàn bộ lưu lượng khác. Để thực hiện:

1.  Mở phần mềm Charles Proxy.
2.  Truy cập vào **Proxy** > **Recording Settings** (Cài đặt ghi).
3.  Chọn tab **Include**.
4.  Nhấn nút **Add** (Thêm).
5.  Nhập tên miền trang web giữa hai dấu sao `*` vào trường Host. Ví dụ: `*utest*` hoặc `*utest.com*`.
    *   *Nếu bạn chỉ sử dụng từ khóa như `*utest*`, Charles sẽ ghi lại tất cả các lưu lượng truy cập có chứa cụm từ 'utest' trong tên miền, ví dụ như utest.com, utest.net, utest.io...*
    *   *Nếu bạn nhập tên miền đầy đủ như `*utest.com*`, nó sẽ chỉ lưu trữ lưu lượng mạng từ tên miền đó và bỏ qua các tên miền khác như utest.net, utest.io...*
6.  Nhấp đúp chuột vào mục đã thêm để chỉnh sửa nếu cần.
7.  Nhấp chọn **OK** rồi chọn **OK** lần nữa để lưu các thay đổi.

---

### Cách loại trừ (Exclude) lưu lượng truy cập cụ thể trong log Charles

Thiết lập này sẽ ghi lại toàn bộ lưu lượng truy cập từ tất cả các tên miền ngoại trừ những tên miền bạn đã chỉ định. Để thực hiện:

1.  Mở phần mềm Charles Proxy.
2.  Truy cập vào **Proxy** > **Recording Settings**.
3.  Chọn tab **Exclude**.
4.  Nhấn nút **Add** (Thêm).
5.  Nhập tên miền trang web giữa hai dấu sao `*` vào trường Host. Ví dụ: `*utest*` hoặc `*utest.com*`.
    *   *Nếu bạn chỉ sử dụng từ khóa như `*utest*`, Charles sẽ loại trừ tất cả các lưu lượng truy cập chứa cụm từ 'utest' trong tên miền.*
    *   *Nếu bạn nhập tên miền đầy đủ như `*utest.com*`, nó sẽ chỉ loại trừ lưu lượng mạng từ tên miền đó.*
6.  Nhấp đúp chuột vào mục đã thêm để chỉnh sửa nếu cần.
7.  Nhấp chọn **OK** rồi chọn **OK** lần nữa để lưu các thay đổi.

---

### Cách gỡ bỏ các địa chỉ/yêu cầu đã thêm trong phần Include/Exclude

Sau khi hoàn thành kiểm thử và muốn xóa thiết lập lọc đã cài đặt, hãy thực hiện theo các bước sau:

1.  Mở phần mềm Charles Proxy.
2.  Truy cập vào **Proxy** > **Recording Settings**.
3.  Chọn tab **Include** hoặc **Exclude** tùy thuộc vào thiết lập bạn muốn gỡ bỏ.
4.  Nhấp chọn mục cần gỡ bỏ.
5.  Nhấp chọn nút **Remove** (Xóa).
6.  Nhấp chọn **OK** để lưu các thay đổi.

#### Lưu ý quan trọng về việc Include/Exclude lưu lượng truy cập
*   Có thể sử dụng đồng thời cả tính năng **Exclude** và **Include**.
*   Khi cùng một Host được thêm vào cả tab **Include** và **Exclude**, thiết lập loại trừ (Exclude) sẽ ghi đè lên thiết lập bao gồm (Include). Do đó, Charles sẽ loại trừ toàn bộ lưu lượng truy cập từ Host đó.
*   Hãy đảm bảo rằng tất cả các địa chỉ/yêu cầu đã được nhập chính xác và tệp log thu được tương ứng đúng với các thiết lập đã chọn.
*   Nếu bạn làm việc trong các dự án liên quan đến Charles, hãy nhớ cập nhật hoặc gỡ bỏ các tùy chọn này trước và sau mỗi phiên kiểm thử.

---

### Tính năng Focused Hosts (Máy chủ tập trung)

Với tính năng Focused Hosts, bạn có thể nhanh chóng ẩn đi các lưu lượng mạng mà khách hàng không quan tâm. Để kích hoạt và cấu hình:

1.  Mở phần mềm Charles Proxy.
2.  Truy cập vào **View** > **Focused Hosts** hoặc nhấn tổ hợp phím **Ctrl + Shift + O**.
3.  Nhấn nút **Add**.
4.  Nhập tên miền (domain) bạn muốn Charles tập trung hiển thị. Ví dụ: `*academybugs*` hoặc `academybugs.com`, và nhập cổng chính xác là `443` (cổng kết nối HTTPS).
5.  Nhấp chọn **OK** rồi chọn **OK** lần nữa để lưu các thay đổi.
6.  Lúc này, bạn sẽ thấy Charles chia lưu lượng mạng làm hai phần: phần thứ nhất là lưu lượng của host đã thêm và phần còn lại là của các host khác hiển thị dưới nhóm **"Other Hosts"** (Các host khác).
7.  Để gỡ một host ra khỏi danh sách Focused Hosts, hãy chọn host muốn gỡ rồi nhấp chọn nút **Remove** và lưu lại bằng nút **OK**.

*   **Focus Host có kèm dấu sao \*\***
*   **Focus Host không có dấu sao \*\***

*Lưu ý: Trong chu kỳ thực hành Charles Proxy của Academy, bạn cần phải tải lên toàn bộ log Charles gốc mà không được trích xuất hoặc sử dụng tính năng lọc lưu lượng include/exclude.*

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Recording Settings | Cài đặt ghi (Recording Settings) | Cấu hình ghi lại lưu lượng mạng trong Charles Proxy |
| Focused Hosts | Máy chủ tập trung (Focused Hosts) | Tính năng giúp làm nổi bật lưu lượng truy cập của các host được chỉ định trong Charles Proxy |
