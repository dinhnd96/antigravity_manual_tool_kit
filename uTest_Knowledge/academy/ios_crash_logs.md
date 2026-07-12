# Log sập ứng dụng trên iOS

> **Nguồn gốc**: uTest Academy - iOS Crash Logs
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Log sập ứng dụng trên iOS (iOS Crash Logs) là gì?
Log sập ứng dụng (Crash logs) ghi lại cách ứng dụng kiểm thử trên iOS bị chấm dứt hoạt động đột ngột và hiển thị mã nguồn đang chạy trên mỗi luồng (thread) tại thời điểm xảy ra sự cố sập ứng dụng.

Các lập trình viên sẽ sử dụng các log này khi chẩn đoán lỗi sập ứng dụng để hiểu rõ những vấn đề mà ứng dụng đang gặp phải.

---

### Cách thu thập log sập ứng dụng trên iOS

Có hai phương pháp để thu thập log sập ứng dụng trên iOS.

#### Phương pháp 1: Trực tiếp trên thiết bị iPhone hoặc iPad
1.  Tái hiện lỗi sập ứng dụng bắt đầu từ thời điểm khởi chạy ứng dụng.
2.  Truy cập vào **Settings (Cài đặt)** trên điện thoại của bạn.
3.  Chọn **Privacy (Quyền riêng tư)** (hoặc **Privacy & Security (Quyền riêng tư & Bảo mật)** trên các phiên bản iOS mới hơn).
4.  Cuộn xuống dưới cùng và chọn **Analytics & Improvements (Phân tích & Cải tiến)**.
5.  Chọn **Analytics Data (Dữ liệu Phân tích)**.
6.  Nhấp chọn bản báo cáo có chứa tên của ứng dụng bị lỗi và mốc thời gian xảy ra sự cố (Danh sách này được sắp xếp theo thứ tự bảng chữ cái).
7.  Chia sẻ tệp báo cáo này qua bất kỳ ứng dụng nào bạn có (ví dụ: Gmail, AirDrop, hoặc lưu vào Tệp).
8.  Tải tệp log định dạng `.ips` này lên báo cáo của bạn.

#### Phương pháp 2: Sử dụng iTunes (Hệ điều hành Windows hoặc macOS phiên bản trước Catalina)
1.  Tải xuống, cài đặt và mở phần mềm iTunes.
2.  Kết nối thiết bị iOS với máy tính qua cổng USB (Quá trình tự động đồng bộ hóa sẽ bắt đầu. Nếu không, hãy thực hiện thủ công).
3.  Tái hiện lỗi sập ứng dụng bắt đầu từ lúc khởi chạy ứng dụng.
4.  Truy cập vào thư mục báo cáo tương ứng trên máy tính của bạn (Hãy đảm bảo bạn đã chọn cài đặt **"Hiển thị các mục ẩn" - show hidden items**):
    *   **macOS**: `~/Library/Logs/CrashReporter/MobileDevice/<TÊN_THIẾT_BỊ>`
    *   **Windows**: `C:\Users\<TÊN_NGƯỜI_DÙNG>\AppData\Roaming\Apple Computer\Logs\CrashReporter\MobileDevice\<TÊN_THIẾT_BỊ>`
5.  Tìm đúng tệp tin định dạng `.log`, `.crash` hoặc `.ips` có chứa tên ứng dụng và mốc thời gian xảy ra lỗi.
6.  Tải tệp log định dạng `.log`, `.crash` hoặc `.ips` đó lên báo cáo của bạn.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Crash Logs | Log sập ứng dụng (Crash Logs) | Log ghi lại hoạt động của mã nguồn tại thời điểm ứng dụng bị sập |
