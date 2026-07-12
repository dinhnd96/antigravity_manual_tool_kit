# Cài Đặt Ứng Dụng Trên Thiết Bị Di Động

> **Nguồn gốc**: uTest Academy - Installing Apps on Mobile Devices
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Android

### Cách 1: Cài từ Google Play Store

1. Mở Overview của test cycle trên thiết bị Android → cuộn xuống phần **Attachments**
2. Nhấn vào liên kết Google Play Store
3. Nhấn **Install** khi Play Store mở
4. Xác minh **phiên bản app** khớp với phiên bản trong Overview
5. Vào **Settings → Apps** → chọn app đã cài để xem phiên bản

> ⚠️ **Lỗi thường gặp:**
> - App không khả dụng tại quốc gia của bạn
> - Thiết bị không tương thích với app
> - Phiên bản cài đặt không khớp với phiên bản trong Overview
> 
> → Liên hệ **TTL** qua chat của test cycle nếu gặp sự cố

---

### Cách 2: Cài file APK

1. Mở trình duyệt trên thiết bị Android → vào Overview của test cycle
2. Tải file **APK** từ phần Attachments
3. Mở file APK sau khi tải xong
4. Android mặc định không cho cài app không rõ nguồn gốc → nhấn **Settings** trên pop-up xuất hiện
5. Bật toggle **"Allow from this source"** (Cho phép từ nguồn này) → quay lại
6. Nhấn **Install** và đợi hoàn tất

---

### Cách 3: Cài APK qua QR Code

1. Mở Overview trên **máy tính** → phần Attachments
2. Nhấn vào biểu tượng **QR code** dưới file APK (hoặc nút "Open Scannable QR code")
3. Trên thiết bị Android:
   - **Android 8+**: Mở ứng dụng **Camera** (camera sau) hoặc **Google Lens**
   - **Android 7 trở xuống**: Cài app quét QR code (Google Lens hoặc QR Code Reader)
4. Hướng camera vào QR code → nhấn vào link tải xuống
5. Nhấn vào file APK đã tải để cài đặt
6. Bật toggle **"Allow from this source"** nếu được yêu cầu
7. Nhấn **Install** và đợi hoàn tất

---

## iOS

### Cách 1: Cài từ App Store

1. Mở Overview trên thiết bị iOS → cuộn xuống phần **Attachments**
2. Nhấn vào link tải app
3. Nhấn **Install** khi App Store mở
4. Xác minh phiên bản app khớp với Overview
5. Vào **Settings → General → iPhone Storage** → chọn app để xem phiên bản

---

### Cách 2: Cài từ TestFlight

1. Mở **App Store** → tải và cài đặt app **TestFlight**
2. Mở Overview của test cycle → nhấn vào link **TestFlight**
3. Chọn đúng phiên bản và cài đặt app

---

### Cách 3: Cài file IPA trực tiếp

1. Mở Overview trên thiết bị iOS → phần Attachments
2. Tìm nút **"Download on Mobile Device"**
   - Hoặc nhấn **"Open Scannable QR code"** và quét bằng iOS device
3. Nhấn **Install** và đợi hoàn tất
4. Sau khi cài xong, vào **Settings → General**:
   - iOS 15+: **VPN and Device Management**
   - iOS cũ hơn: **Profiles and Device Management**
5. Chọn app đã cài và nhấn **Trust** (Tin cậy) → app đã sẵn sàng sử dụng

> ℹ️ Nếu cycle không có nút "Download on Mobile Device", bạn cần dùng iTunes hoặc iMazing (xem bên dưới).

---

### Cách 4: Cài IPA qua iTunes

| Hệ điều hành | Cách thực hiện |
|-------------|----------------|
| **Windows** | Tải và cài iTunes |
| **macOS < 10.15** | iTunes đã cài sẵn |
| **macOS ≥ 10.15** | Dùng **Apple Configurator 2** thay thế (kéo thả file IPA) |

**Các bước cho iTunes:**
1. Mở Overview trên máy tính → tải file **IPA** từ Attachments
2. Copy file IPA (Ctrl+C trên Windows / Command+C trên macOS)
3. Kết nối iOS device với máy tính → nhấn **Trust** (Tin cậy) trên thiết bị
4. Mở iTunes → đảm bảo thiết bị iOS hiển thị → click phải vào tên thiết bị → **Paste**
5. Đợi quá trình hoàn tất
6. Vào **Settings → General → VPN and Device Management** (hoặc Profiles and Device Management)
7. Chọn app → nhấn **Trust**

> 💡 **Lưu ý**: Chọn phần **Library** trên iTunes trước khi paste file IPA.

**Cho macOS ≥ 10.15:**
1. Mở **Apple Configurator 2**
2. Kéo thả file IPA lên thiết bị → xác nhận cài đặt

---

### Cách 5: Cài IPA qua iMazing

1. Tải và cài **iMazing** trên máy tính
2. Mở Overview trên máy tính → tải file IPA
3. Mở iMazing
4. Kết nối iOS device → nhấn **Trust** trên thiết bị
5. Trong iMazing nhấn **Manage Apps**
6. Nhấn mũi tên thả xuống ở góc dưới phải
7. Chọn **Install .IPA File**
8. Chọn file IPA đã tải → nhấn **Open**
9. Đợi hoàn tất
10. Vào **Settings → General → VPN and Device Management** → Trust app

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| APK (Android Package Kit) | Gói cài đặt Android | File cài app cho Android |
| IPA (iOS App Store Package) | Gói cài đặt iOS | File cài app cho iOS |
| TestFlight | TestFlight | App của Apple để phân phối bản beta |
| QR Code | Mã QR | Quét để tải app nhanh |
| Trust (Device Management) | Tin cậy (Quản lý thiết bị) | Bắt buộc cho app từ nguồn ngoài App Store |
| Apple Configurator 2 | Apple Configurator 2 | Thay thế iTunes trên macOS ≥ 10.15 |
| iMazing | iMazing | Phần mềm bên thứ ba quản lý iOS |
