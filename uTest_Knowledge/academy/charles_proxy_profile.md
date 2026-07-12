# Hồ sơ cấu hình Charles Proxy

> **Nguồn gốc**: uTest Academy - Charles Proxy Profile
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Hồ sơ cấu hình Charles Proxy (Charles Proxy Profile) là gì?
Hồ sơ cấu hình Charles Proxy là tập hợp tất cả các thiết lập hoặc cấu hình của ứng dụng Charles Proxy. Một hồ sơ cấu hình được thiết lập cụ thể để chỉ ghi lại và lưu log cho lưu lượng truy cập (traffic) được yêu cầu. Theo mặc định, Charles Proxy tạo và lưu tất cả các thiết lập này trong hồ sơ cấu hình mặc định (default profile).

Nếu chu kỳ kiểm thử (test cycle) yêu cầu sử dụng hồ sơ cấu hình tùy chỉnh (custom profile), hướng dẫn và tệp cấu hình có định dạng `.xml` sẽ được cung cấp trong chu kỳ đó. Việc thu thập log bằng hồ sơ cấu hình tùy chỉnh có nghĩa là bạn sẽ thu thập các log chứa thông tin chính xác phục vụ cho chu kỳ kiểm thử đang thực hiện. Ngoài ra, việc này còn giúp ẩn đi các thông tin không cần thiết mà khách hàng không thực sự quan tâm.

---

### Cách nhập (Import) một hồ sơ cấu hình Charles Proxy

1.  Đảm bảo Charles Proxy và Chứng chỉ đã được cài đặt và hoạt động bình thường.
2.  Truy cập vào **Tools** > **Import/Export Settings**.
3.  Chọn tab **Import**.
4.  Nhấp chọn **Choose File** (Chọn tệp).
5.  Chọn và mở tệp cấu hình đã tải xuống từ chu kỳ kiểm thử bạn đang làm việc.
6.  Đảm bảo tất cả các tùy chọn đều đã được tích chọn.
7.  Nhấp chọn **Import**.

---

### Cách chuyển đổi qua lại giữa các hồ sơ cấu hình Charles Proxy

Bạn có thể cài đặt nhiều cấu hình khác nhau và chuyển đổi qua lại giữa chúng tùy thuộc vào chu kỳ kiểm thử hiện tại đang làm việc. Bạn phải luôn sử dụng đúng cấu hình được yêu cầu cho chu kỳ đó. Trong trường hợp không có tệp cấu hình hoặc hướng dẫn thiết lập đặc biệt nào được cung cấp, bạn có thể sử dụng cấu hình mặc định (default profile) mà không cần chỉnh sửa gì thêm và cấu hình này sẽ ghi lại toàn bộ lưu lượng mạng.

Để chuyển đổi giữa các cấu hình Charles Proxy, hãy thực hiện theo các bước sau:
1.  Truy cập vào **Tools** > **Profiles**.
2.  Tìm cấu hình bạn muốn sử dụng.
3.  Tích chọn ô trong cột **Activate** (Kích hoạt).
4.  Đóng cửa sổ Profiles lại.

---

### Cách xóa một hồ sơ cấu hình Charles Proxy

Sau khi hoàn thành việc kiểm thử và muốn gỡ bỏ hồ sơ cấu hình tùy chỉnh đã cài đặt, hãy thực hiện theo các bước sau:
1.  Mở phần mềm Charles Proxy.
2.  Truy cập vào **Tools** > **Profiles**.
3.  Chuyển sang (kích hoạt) một hồ sơ cấu hình khác ngoài hồ sơ cấu hình mà bạn muốn xóa.
4.  Nhấp chọn vào tên của hồ sơ cấu hình bạn muốn xóa.
5.  Nhấp chọn nút **Remove** (Xóa).
6.  Nhấp chọn nút **OK** để lưu các thay đổi.

*Lưu ý: Trong chu kỳ thực hành Charles Proxy của Academy, chúng ta sẽ sử dụng hồ sơ cấu hình mặc định.*

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Charles Proxy Profile | Cấu hình Charles Proxy (Charles Proxy Profile) | Tệp cấu hình lưu trữ các thiết lập của Charles Proxy |
| Default Profile | Cấu hình mặc định (Default Profile) | Hồ sơ cấu hình thiết lập mặc định của Charles Proxy |
| Custom Profile | Cấu hình tùy chỉnh (Custom Profile) | Hồ sơ cấu hình được thiết lập theo yêu cầu riêng biệt của chu kỳ kiểm thử |
