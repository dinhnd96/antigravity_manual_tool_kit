# Quy Định Bảo Vệ Dữ Liệu Chung (GDPR)

> **Nguồn gốc**: uTest Academy - General Data Protection Regulation (GDPR)
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: platform

---

## Bản dịch

### GDPR và Thông tin nhận dạng cá nhân (PII) là gì?

**GDPR** (General Data Protection Regulation) là luật chuẩn hóa về **bảo vệ dữ liệu và quyền riêng tư** tại Liên minh Châu Âu. Luật này điều chỉnh việc xử lý dữ liệu cá nhân nhằm bảo vệ chúng.

- **"Dữ liệu cá nhân"** (Personal Data): Bất kỳ thông tin nào giúp **nhận dạng được** một người (còn gọi là PII - Personally Identifiable Information)
- **"Xử lý"** (Processing): Bất kỳ thao tác nào như lưu trữ, chia sẻ, thu thập dữ liệu cá nhân

#### Ví dụ về dữ liệu cá nhân được GDPR bảo vệ:

| Loại | Ví dụ |
|------|-------|
| 👤 Danh tính | Tên, số CMND/hộ chiếu |
| 🏦 Tài chính | Chi tiết ngân hàng |
| 🌐 Kỹ thuật | Địa chỉ IP |
| 📧 Liên lạc | Địa chỉ email (nếu chứa tên bạn) |
| 📸 Hình ảnh | Ảnh cá nhân |
| 🧬 Sinh học | Dữ liệu di truyền (DNA), dữ liệu sinh trắc học (vân tay) |
| 🏳️ Nhạy cảm | Chủng tộc, dân tộc, quan điểm chính trị, tín ngưỡng tôn giáo, xu hướng tính dục |

> ⚠️ **Lưu ý**: GDPR bảo vệ không chỉ dữ liệu cá nhân **của bạn**, mà còn cả dữ liệu của **bạn bè, gia đình, đồng nghiệp và bên thứ ba**.

---

### Vi phạm GDPR phổ biến của tester

Tại uTest, các vi phạm GDPR thường gặp trong **video ghi hình** bao gồm:

| # | Vi phạm | Mức độ |
|---|---------|--------|
| ❌ 1 | Ghi hình **nền tảng uTest** | Nghiêm trọng |
| ❌ 2 | Ghi hình **chat uTest** với tên khách hàng và tester khác hiển thị | Nghiêm trọng |
| ❌ 3 | Nhận **tin nhắn/thông báo** khi đang ghi hình (WhatsApp, Facebook, email, thông báo uTest của dự án khác) | Phổ biến |
| ❌ 4 | Nhận **cuộc gọi** khi đang ghi hình với tên và số điện thoại hiển thị | Phổ biến |
| ❌ 5 | Hiển thị **hộp thư email** với địa chỉ email và người gửi | Phổ biến |
| ❌ 6 | **Ghi hình bản thân** qua webcam | Thường gặp |
| ❌ 7 | **Đọc to** tên, địa chỉ, số CMND và dữ liệu nhạy cảm | Nghiêm trọng |
| ❌ 8 | Hình ảnh **người thân** làm hình nền thiết bị | Thường gặp |
| ❌ 9 | Chức năng **tự điền (autofill)** của trình duyệt hiển thị địa chỉ, tên, số điện thoại | Phổ biến |
| ❌ 10 | Gõ **mật khẩu hoặc PII** mà không làm mờ bàn phím điện thoại trong video | Nghiêm trọng |

---

### Hướng dẫn tránh vi phạm GDPR

> Applause cam kết tôn trọng quyền riêng tư trực tuyến của bạn. Khi chấp nhận test cycle, bạn đồng ý cho Applause sử dụng thông tin cá nhân cho mục đích tuyển dụng và thực hiện test cycle. Dữ liệu này có thể được chia sẻ với bên thứ ba nếu cần để truy cập môi trường kiểm thử.

**Đặc biệt cẩn thận khi ghi video.** Tuân thủ các hướng dẫn sau:

| # | Hướng dẫn | Chi tiết |
|---|-----------|---------|
| ✅ 1 | **Tạo email riêng cho kiểm thử** | Không chứa tên thật, ví dụ: `testing@gmail.com` |
| ✅ 2 | **Không ghi hình bản thân** qua webcam | Trừ khi được yêu cầu cụ thể |
| ✅ 3 | **Không ghi hình nền tảng uTest**, chat, hoặc PII | Vì tên khách hàng và tester khác hiển thị ở đó |
| ✅ 4 | **Không hiển thị profile uTest** | Tên, dự án khác, thông tin thanh toán |
| ✅ 5 | **Tắt thông báo** khi ghi hình | Tránh hiển thị tên, email, tin nhắn riêng |
| ✅ 6 | **Tránh chuyển tab** không cần thiết | Nếu cần xem tài liệu, dùng thiết bị thứ hai |
| ✅ 7 | **Tắt chức năng tự điền (autofill)** của trình duyệt | Tránh hiển thị thông tin cá nhân |
| ✅ 8 | **Làm mờ bàn phím** khi gõ tên, mật khẩu, PIN hoặc PII trong video | Bảo vệ thông tin nhạy cảm |

> ℹ️ **Ngoại lệ**: Một số test cycle có thể yêu cầu bạn ghi hình quá trình đăng ký với dữ liệu thật (tên, địa chỉ, email, số điện thoại, thẻ tín dụng, mật khẩu...). Trong trường hợp này, **TTL sẽ xem xét và chỉnh sửa/làm mờ** tất cả video để ẩn thông tin nhạy cảm trước khi gửi cho khách hàng.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| GDPR | Quy định Bảo vệ Dữ liệu Chung | Luật EU về bảo vệ dữ liệu |
| PII (Personally Identifiable Information) | Thông tin nhận dạng cá nhân | Bất kỳ thông tin nào nhận dạng được người |
| Personal Data | Dữ liệu cá nhân | Được GDPR bảo vệ |
| Processing | Xử lý (dữ liệu) | Lưu trữ, chia sẻ, thu thập |
| Autofill | Tự điền | Chức năng trình duyệt, phải tắt khi ghi video |
| Blur | Làm mờ | Bắt buộc khi gõ PII trong video |
| Biometric Data | Dữ liệu sinh trắc học | Vân tay, nhận diện khuôn mặt |
