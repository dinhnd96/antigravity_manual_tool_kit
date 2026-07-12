# Xác Thực Đa Yếu Tố (MFA) Trên uTest

> **Nguồn gốc**: uTest Academy – Multi-Factor Authentication (MFA)  
> **Ngày dịch**: 2026-05-17  
> **Chủ đề**: platform

---

## Bản dịch

### MFA là gì?

Xác thực đa yếu tố (MFA - Multi-Factor Authentication) là quy trình bảo mật yêu cầu **hai hoặc nhiều yếu tố xác minh** khi đăng nhập vào ứng dụng hoặc trang web. Nhiều công ty trực tuyến hiện sử dụng MFA để cung cấp cho người dùng một **lớp bảo mật bổ sung** ngoài tên đăng nhập và mật khẩu thông thường.

Ngoài ra, MFA đảm bảo rằng chỉ bạn — người có quyền truy cập thiết bị — mới có thể truy cập tài khoản của mình. Việc sử dụng MFA giúp uTest cải thiện bảo mật bằng cách **bảo vệ dữ liệu khách hàng** và **bảo vệ tài khoản tester**.

Khi kích hoạt MFA, bạn cần cài đặt ứng dụng xác thực trên thiết bị di động, ví dụ: **Google Authenticator** hoặc **Microsoft Authenticator**. Trong quá trình cấu hình, bạn sẽ liên kết ứng dụng với tài khoản uTest. Sau đó, mỗi lần đăng nhập, bạn cần nhập một mã số gọi là **"Mật khẩu dùng một lần" (OTP - One-Time Password)**, ví dụ "987654", từ ứng dụng đã liên kết.

---

### MFA Trong Các Dự Án uTest

Để đảm bảo bảo mật và bảo vệ dữ liệu khách hàng, **tất cả thành viên uTest đều phải bật MFA** trên tài khoản.

**Nếu bạn không bật MFA:**

- Lời mời tham gia test cycle sẽ bị **ẩn thông tin** — bạn không thể xem tên cycle, công ty, sản phẩm, phạm vi, hướng dẫn, v.v.
- Bạn **không thể chấp nhận** lời mời cho đến khi bật và cấu hình MFA
- Email và thông báo đẩy (push notification) sẽ bị **che giấu** nội dung chi tiết

---

### Cách Bật MFA

1. Mở trang web uTest và đăng nhập
2. Nhấn vào mũi tên bên cạnh tên tester của bạn
3. Nhấn tab **"Account Security"** (Bảo mật tài khoản)
4. Đọc thông tin MFA trên trang này
5. Nhấn nút **"Enable MFA"** để kích hoạt
6. Nhấn nút **"Enable MFA and Sign Out"**
7. Nhấn **"Sign In"** để đăng nhập lại
8. Sau khi đăng nhập, bạn sẽ được chuyển đến trang **thiết lập MFA**
9. Tải và cài đặt một trong các ứng dụng xác thực sau:
   - **Google Authenticator**: Android hoặc iOS
   - **Microsoft Authenticator**: Android hoặc iOS
   - **FreeOTP**: Android hoặc iOS
10. Mở ứng dụng đã cài và bắt đầu thiết lập mục MFA mới

---

### Thiết Lập Qua Google Authenticator

#### Cách 1: Quét mã QR bằng Camera

1. Mở ứng dụng Google Authenticator
2. Nhấn nút **"+"**
3. Chọn **"Scan a QR Code"** (Quét mã QR)
4. Cấp quyền sử dụng camera
5. Hướng camera vào mã QR trên trang MFA Setup
6. Mục mới sẽ hiển thị với tên **Applause: [email của bạn]**
7. Nhập mã MFA từ ứng dụng vào trường **"One-time code"**
8. Đặt tên trong trường **"Device Name"**
9. Nhấn **"Submit"**

#### Cách 2: Nhập Setup Key thủ công

1. Nhấn liên kết **"My device is unable to scan QR codes"**
2. Mở Google Authenticator → nhấn **"+"** → chọn **"Enter a Setup Key"**
3. Nhập tên tài khoản
4. Nhập khóa (key) hiển thị ở bước 2 trên trang MFA Setup
5. Chọn loại khóa: **"Time based"**
6. Nhấn **"Add"**
7. Nhập mã MFA vào trường "One-time code" → đặt "Device Name" → nhấn **"Submit"**

---

### Thiết Lập Qua Microsoft Authenticator

#### Cách 1: Quét mã QR bằng Camera

1. Mở Microsoft Authenticator → đăng nhập hoặc bỏ qua
2. Nhấn **"Add account"** → chọn **"Personal account"**
3. Chọn **"Scan a QR Code"** → cấp quyền camera
4. Hướng camera vào mã QR trên trang MFA Setup
5. Xác nhận thông báo khóa ứng dụng
6. Nhấn vào mục Applause để hiển thị OTP
7. Nhập mã → đặt "Device Name" → nhấn **"Submit"**

#### Cách 2: Nhập mã thủ công

1. Nhấn liên kết **"My device is unable to scan QR codes"**
2. Mở Microsoft Authenticator → nhấn **"+"** → chọn **"Other account"**
3. Nhấn **"OR ENTER CODE MANUALLY"** ở cuối
4. Nhập tên tài khoản và khóa từ trang MFA Setup
5. Nhấn **"Finish"**
6. Nhập mã OTP → đặt "Device Name" → nhấn **"Submit"**

---

### Thiết Lập Qua FreeOTP

1. Mở FreeOTP → đọc thông tin chào mừng → nhấn **"Get Started"**
2. Tạo mật khẩu ban đầu và ghi nhớ
3. Nhấn **"+"** → nhấn biểu tượng mã QR
4. Cấp quyền camera → quét mã QR trên trang MFA Setup
5. Nhấn vào mục Applause để hiển thị OTP
6. Nhập mã → đặt "Device Name" → nhấn **"Submit"**

---

### Khuyến Nghị Khi Thiết Lập MFA

- **Đăng nhập vào ứng dụng xác thực bằng email** để MFA được liên kết với tài khoản — có thể khôi phục nếu mất thiết bị hoặc cài lại ứng dụng
- **Xuất (export) MFA sang thiết bị khác** nếu muốn chuyển đổi thiết bị hoặc muốn truy cập MFA từ nhiều thiết bị

---

### Đăng Nhập Sau Khi Bật MFA

1. Mở trang web hoặc ứng dụng uTest
2. Nhập email và mật khẩu → nhấn **"Sign In"**
3. Hệ thống yêu cầu nhập OTP
4. Mở ứng dụng xác thực và ghi nhận mã OTP
5. Nhập mã OTP **không có dấu cách**

> ⚠️ **Lưu ý:** Mã OTP có **giới hạn thời gian** và thay đổi (ví dụ: mỗi 30 giây). Hãy nhập nhanh trước khi hết hạn. Google Authenticator hiển thị đồng hồ đếm ngược cho biết thời gian còn lại của mã hiện tại.

---

### Vô Hiệu Hóa MFA

Một khi MFA đã được bật, **không thể tắt** — nhằm đảm bảo tất cả tester đều đủ điều kiện tham gia dự án yêu cầu MFA.

---

### Chuyển MFA Sang Thiết Bị Khác / Mất Cấu Hình

1. Kiểm tra xem cài ứng dụng OTP trên thiết bị mới có **tự động nhập** cấu hình MFA không
2. Nếu không → sử dụng nút **"Reset MFA"** hoặc liên hệ Tester Support
3. Sau khi reset, **xóa cấu hình MFA cũ** trong ứng dụng OTP để tránh nhầm lẫn
4. Cấu hình MFA mới khi đăng nhập lần tiếp theo

**Nếu mất quyền truy cập thiết bị MFA:** liên hệ [uTest Tester Support — Login Help](https://support.utest.com). Nhớ cung cấp **Tester ID**. Có thể cần xác minh danh tính bổ sung.

**Cách Reset MFA trên trang web:**

1. Đăng nhập tài khoản uTest
2. Nhấn mũi tên bên cạnh tên tester → tab **"Account Security"**
3. Nhấn nút **"Reset MFA"** → xác nhận trong popup
4. Cấu hình MFA mới trên thiết bị mới
5. Xóa cấu hình cũ khỏi ứng dụng OTP

---

### Lưu Ý Quan Trọng

- MFA chỉ có thể bật trên **trang web uTest** (không phải app)
- Sau khi bật MFA, **cập nhật ứng dụng uTest Mobile lên phiên bản mới nhất** — nếu không sẽ không đăng nhập được
- Bật MFA **trước** khi nhận lời mời để tránh chậm trễ
- Nếu cycle yêu cầu MFA mà bạn chưa bật → **mất quyền truy cập** cycle, bug report và test case đã nộp cho đến khi bật MFA
- **uTest và Applause sẽ KHÔNG BAO GIỜ** yêu cầu mã OTP của bạn. Nếu ai đó yêu cầu, hãy báo cáo tại [support.utest.com](https://support.utest.com)

---

### Hỗ Trợ & FAQ

- Liên hệ **uTest Tester Support** → danh mục **"Login Help"** tại [support.utest.com](https://support.utest.com)
- Cung cấp **uTest ID** khi liên hệ
- Xem thêm chi tiết về MFA trong **Tester Knowledge Base** (Kho kiến thức Tester)

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Multi-Factor Authentication (MFA) | Xác thực đa yếu tố | Bắt buộc trên uTest |
| One-Time Password (OTP) | Mật khẩu dùng một lần | Mã số từ ứng dụng xác thực |
| Authenticator App | Ứng dụng xác thực | Google/Microsoft Authenticator, FreeOTP |
| Account Security | Bảo mật tài khoản | Tab cài đặt trên uTest |
| Setup Key | Khóa thiết lập | Dùng khi không quét được QR |
| Reset MFA | Đặt lại MFA | Khi chuyển thiết bị hoặc mất cấu hình |
| Device Name | Tên thiết bị | Đặt tên khi cấu hình MFA |
| Tester Knowledge Base | Kho kiến thức Tester | Tài liệu tham khảo chính thức |
| Redacted | Bị ẩn / Bị che | Thông tin bị ẩn khi chưa bật MFA |
| Push Notification | Thông báo đẩy | Thông báo từ ứng dụng |
