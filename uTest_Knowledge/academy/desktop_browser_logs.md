# Log trình duyệt trên máy tính

> **Nguồn gốc**: uTest Academy - Desktop Browser Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Trong khóa học này, chúng ta sẽ học cách thu thập log console trình duyệt (browser console logs). Các trình duyệt máy tính hoạt động giống nhau trên tất cả các hệ điều hành máy tính, vì vậy bạn có thể thực hiện theo các bước tương tự trên Windows, macOS hoặc Linux.

### Google Chrome / Và các trình duyệt nhân Chromium

1.  Nhấn tổ hợp phím **CTRL+Shift+I** hoặc **F12**, hoặc chọn **biểu tượng ba dấu chấm** > **Công cụ khác (More Tools)** > **Công cụ nhà phát triển (Developer Tools)**.
2.  Chọn **Console** > **biểu tượng bánh răng** ở góc trên cùng bên phải.
3.  Cuộn xuống phần **Console preferences** > tích chọn **Show Timestamps** (Hiển thị mốc thời gian) và **Preserve Log Upon Navigation** (Giữ log khi chuyển trang/điều hướng).
4.  Đóng cửa sổ cài đặt.
5.  Xóa sạch console bằng cách nhấp vào **biểu tượng Clear Console** hoặc nhấp chuột phải vào bên trong cửa sổ console và chọn **Clear console** (Xóa console).
6.  Tải lại trang (Refresh) và tái hiện lỗi (reproduce) bắt đầu từ trang chủ.
7.  Nhấp chuột phải vào phần log và chọn **Save As** (Lưu dưới dạng).
8.  Hoặc bạn cũng có thể sao chép (copy) log từ console và dán chúng vào bất kỳ chương trình soạn thảo văn bản nào.
9.  Lưu tệp dưới định dạng `.txt`.
10. Mở tệp log console lên và đảm bảo rằng có mốc thời gian (timestamp) và dòng chữ 'Navigated to' cùng địa chỉ trang web đang kiểm thử (Ví dụ: `18:32:30.854 Navigated to https://www.utest.com`).

**Lưu ý**: Thực hiện theo các bước tương tự để thu thập log console cho các trình duyệt nhân Chromium khác, chẳng hạn như Microsoft Edge mới, Opera, Brave, Yandex.

### Firefox

1.  Nhấn tổ hợp phím **CTRL+Shift+K** hoặc **F12**, hoặc chọn **biểu tượng menu hamburger (ba sọc ngang)** ở góc trên cùng bên phải và chọn **Web Developer** > **Web Developer Tools** (Công cụ nhà phát triển web).
2.  Trên màn hình console, chọn **biểu tượng bánh răng** ở góc trên bên phải và chọn **Persist Logs** (Giữ log khi chuyển trang) và **Show Timestamps** (Hiển thị mốc thời gian).
3.  Nhấp vào **biểu tượng thùng rác** để xóa sạch các log cũ.
4.  Tải lại trang và tái hiện lỗi bắt đầu từ trang chủ.
5.  Để ghi lại log, nhấp chuột phải vào console > chọn **Save all Messages to File** (Lưu tất cả tin nhắn vào tệp).
6.  Lưu tệp dưới định dạng `.txt`.
7.  Mở tệp log console lên và đảm bảo rằng có mốc thời gian và dòng chữ 'Navigated to' cùng địa chỉ trang web đang kiểm thử (Ví dụ: `18:32:30.854 Navigated to https://www.utest.com`).

**Lưu ý**: Nếu bạn không thấy bất kỳ mốc thời gian nào trong console, hãy thử thay đổi kích thước (resize) khung console cho đến khi mốc thời gian xuất hiện.

### Safari

1.  Nhấp chọn **Safari** trên thanh menu và chọn **Preferences** (Tùy chọn/Thiết lập).
2.  Chọn **tab Advanced (Nâng cao) có biểu tượng bánh răng** > tích chọn **Show Develop menu in menu bar** (Hiển thị menu Phát triển trên thanh menu).
3.  Đóng cửa sổ cài đặt lại và nhấp vào mục **Develop** (Phát triển) thả xuống > chọn **Show Web Inspector** (Hiển thị Trình kiểm tra Web).
4.  Trên cửa sổ console, tích chọn **Preserve Log** (Giữ log khi chuyển trang) và nhấp vào **biểu tượng thùng rác** để xóa sạch các log cũ.
5.  Tải lại trang chủ và tái hiện lỗi bắt đầu từ trang chủ.
6.  Nhấp vào tab **Console** rồi nhấn tổ hợp phím **Command+S** để lưu log.
7.  Khi lưu log, điều quan trọng là bạn phải nhấp chuột vào vùng console trước khi nhấn **Command+S**.
8.  Lưu tệp dưới định dạng `.txt`.

**Lưu ý**: Log do Safari tạo ra không chứa mốc thời gian.

---

### Cách hiển thị phần mở rộng (đuôi tệp) và thay đổi nó

#### Windows 10

1.  Mở **File Explorer** trong Windows 10 hoặc bất kỳ thư mục nào trên máy tính của bạn.
2.  Chuyển sang tab **View** (Hiển thị/Xem) ở menu phía trên để hiển thị thanh ribbon.
3.  Tích chọn tùy chọn **File name extensions** (Phần mở rộng tên tệp) để hiển thị đuôi tệp tin.
4.  Quay lại tệp log mà bạn muốn thay đổi phần mở rộng.
5.  Nhấp đúp chuột vào tên tệp rồi sửa phần mở rộng thành `.txt`. Hoặc bạn có thể nhấp chuột phải vào tệp, sau đó chọn **Rename** (Đổi tên) từ menu ngữ cảnh.

#### macOS

1.  Nhấp chuột phải vào tệp, sau đó chọn **Rename** (Đổi tên) từ menu ngữ cảnh.
2.  Thay đổi phần mở rộng tệp thành `.txt` rồi nhấn phím **Enter** hoặc nhấp chuột ra ngoài vùng tệp tin.
3.  Xác nhận đổi đuôi tệp.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Developer Tools | Công cụ nhà phát triển (Developer Tools) | Bộ công cụ phát triển tích hợp trong trình duyệt web |
| Preserve Log | Giữ log khi chuyển trang (Preserve Log) | Tùy chọn giữ lại các bản ghi log khi chuyển đổi trang web |
| Web Inspector | Trình kiểm tra web (Web Inspector) | Bộ công cụ nhà phát triển trên trình duyệt Safari |
| File Explorer | Trình quản lý tệp (File Explorer) | Trình quản lý tệp tin mặc định trên hệ điều hành Windows |
