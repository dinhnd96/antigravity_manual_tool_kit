# Hướng dẫn chụp ảnh màn hình trên Windows

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Cách 1: Sử dụng các công cụ có sẵn (Built-in tools)

#### A. Tổ hợp phím Windows + PrintScreen
Bạn có thể chụp ảnh màn hình hiện tại bằng cách nhấn đồng thời tổ hợp phím **Windows + PrintScreen**. Sau đó, bạn có thể khoanh vùng nổi bật lỗi trên ảnh bằng ứng dụng Paint.

Theo mặc định, ảnh chụp màn hình được lưu trong thư mục `Screenshots` nằm trong thư mục `Pictures`.

Thực hiện theo các bước sau để đẩy nhanh quá trình:
- Nhấn phím **PrintScreen** trên bàn phím của bạn, hành động này sẽ sao chép ảnh chụp màn hình vào khay nhớ tạm (clipboard) thay vì tự động tạo ra một tệp mới.
- Mở ứng dụng **Paint** và nhấn tổ hợp phím **Ctrl + V** trên bàn phím để dán ảnh.
- Chọn hình dạng hình chữ nhật hoặc hình tròn, và chọn màu đỏ hoặc màu vàng.
- Vẽ hình dạng đã chọn bao quanh vị trí có lỗi (bug) để khoanh vùng nổi bật lỗi đó.
- Sau khi đã khoanh vùng ưng ý, hãy lưu ảnh chụp màn hình lại bằng cách nhấn tổ hợp phím **Ctrl + S** trên bàn phím, hoặc nhấn vào **File** rồi chọn **Save**.

#### B. Tổ hợp phím Windows + Shift + S (Snipping Tool)
Một cách khác để chụp ảnh màn hình là nhấn tổ hợp phím **Windows + Shift + S**. Cách làm này sẽ không lưu ảnh chụp trực tiếp thành tệp ngay, mà sẽ sao chép nó vào khay nhớ tạm (clipboard) của bạn, vì vậy bạn vẫn cần dán ảnh vào một ứng dụng chỉnh sửa ảnh như Paint.

Làm theo các bước dưới đây để chụp ảnh bằng phương pháp này và khoanh vùng nổi bật lỗi:
- Nhấn tổ hợp phím **Windows + Shift + S** trên bàn phím của bạn.
- Chọn chế độ cắt hình (snipping mode) ở thanh công cụ phía trên màn hình:
  - Chọn **Window Snip** (biểu tượng thứ 3) nếu bạn muốn loại bỏ thanh tác vụ (taskbar) khỏi ảnh chụp.
  - Chọn **Fullscreen Snip** (biểu tượng thứ 4) nếu bạn muốn chụp toàn bộ màn hình.
- Nếu bạn chọn Window Snip, hãy nhấp chuột vào cửa sổ ứng dụng bạn muốn chụp.
- Mở ứng dụng **Paint** và dán ảnh bằng cách nhấn tổ hợp phím **Ctrl + V**.
- Chọn hình dạng hình chữ nhật hoặc hình tròn, và chọn màu đỏ hoặc màu vàng.
- Đánh dấu trên ảnh để khoanh vùng nổi bật vấn đề lỗi.
- Sau khi hoàn thành, nhấn tổ hợp phím **Ctrl + S** hoặc nhấn vào **File > Save** để lưu ảnh chụp màn hình.
- Đổi tên tệp.
- Chọn thư mục lưu mong muốn và nhấp vào nút **Save** để lưu lại.

---

### Cách 2: Sử dụng phần mềm ShareX

Sử dụng Cách 1 có thể giúp bạn hoàn thành công việc, nhưng bạn có thể trải nghiệm phần mềm này, vốn được phát triển chuyên biệt để chụp và chú thích ảnh chụp màn hình.

- Tải xuống và cài đặt phần mềm **ShareX** từ trang chủ của ứng dụng.
- Mở ShareX và nhấp vào **After capture tasks** (Các tác vụ sau khi chụp), tại đó:
  - Bỏ chọn tùy chọn **Upload image to host** (Tải hình ảnh lên máy chủ lưu trữ).
  - Chọn tùy chọn **Open in image editor** (Mở trong trình chỉnh sửa ảnh).
- Sau đó, tiến hành chụp ảnh màn hình bằng cách:
  - Nhấp vào **Capture** và chọn **Fullscreen**.
  - Hoặc nhấn phím **PrintScreen** trên bàn phím của bạn.
- Trình chỉnh sửa ảnh sẽ tự động mở ra. Hãy vẽ một hình chữ nhật hoặc hình tròn để khoanh vùng nổi bật lỗi rồi nhấn phím **Enter** để lưu.

Theo mặc định, ShareX sẽ lưu trữ toàn bộ ảnh chụp màn hình của bạn trong thư mục `ShareX\Screenshots` nằm trong thư mục `Documents`.

*Lưu ý:* Hãy chắc chắn rằng tùy chọn "Upload image to host" đã được tắt trong phần mềm ShareX để tránh việc tải trái phép hình ảnh của khách hàng lên mạng.

---

### Cách 3: Sử dụng công cụ Xbox Game Bar

Xbox Game Bar cho phép bạn chụp ảnh màn hình ngay cả khi không chơi game. Để sử dụng tính năng này, trước tiên bạn phải bật Xbox Game Bar. Làm theo các bước dưới đây để bật tính năng này:

- Nhấn tổ hợp phím **Windows + S** để mở thanh tìm kiếm và nhập `Xbox Game Bar`.
- Chọn **Enable Xbox Game Bar** từ kết quả tìm kiếm và bật nó lên.
- Ngoài ra, bạn có thể vào **Settings > Gaming > Xbox Game Bar** và gạt công tắc để kích hoạt.

Sử dụng phương pháp này sẽ lưu ảnh chụp màn hình dưới dạng tệp và tự động loại bỏ thanh tác vụ (taskbar) khỏi ảnh chụp.

Thực hiện theo các bước sau để sử dụng cách này:
- Nhấn tổ hợp phím **Windows + G** trên bàn phím của bạn để mở Xbox Game Bar.
- Nhấp vào biểu tượng **Máy ảnh (Camera)** để chụp ảnh màn hình.
- Hoặc bạn có thể nhấn trực tiếp tổ hợp phím **Windows + Alt + PrintScreen** trên bàn phím để chụp ảnh trực tiếp mà không cần mở giao diện Xbox Game Bar.
- Một thông báo sẽ xuất hiện. Nhấp vào thông báo đó để xem ảnh chụp màn hình.
- Nhấp vào **Open file location** (Mở thư mục lưu tệp) rồi chọn **Continue** để mở thư mục lưu trữ.
- Đổi tên và di chuyển tệp đến thư mục mong muốn.
- Mở tệp ảnh bằng một Trình chỉnh sửa ảnh như Paint để khoanh vùng nổi bật lỗi.
- Chọn hình chữ nhật hoặc hình tròn, chọn màu đỏ hoặc màu vàng để đánh dấu.
- Đánh dấu trên ảnh để khoanh vùng nổi bật vấn đề lỗi.
- Sau khi hoàn thành, nhấn tổ hợp phím **Ctrl + S** hoặc chọn **File > Save** để lưu các thay đổi.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Clipboard | Khay nhớ tạm | Vùng bộ nhớ đệm lưu trữ tạm thời dữ liệu được copy |
| Snipping Tool | Công cụ cắt ảnh màn hình | Công cụ chụp và cắt màn hình mặc định của Windows |
| Taskbar | Thanh tác vụ | Thanh chứa các nút ứng dụng ở cạnh dưới màn hình |
| Highlight | Khoanh vùng nổi bật | Vẽ hình/đánh dấu để chỉ rõ lỗi trên ảnh chụp màn hình |
| Screenshot | Ảnh chụp màn hình | Bằng chứng dạng hình ảnh hiển thị lỗi phần mềm |
