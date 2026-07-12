# Các Thực Hành Tốt Nhất (Best Practices)

> **Nguồn gốc**: uTest Academy - Best Practices
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### 1. Luôn đọc Overview

Luôn đọc Overview **trước khi** bắt đầu kiểm thử. Điều này **cực kỳ quan trọng**. Đọc Overview nhiều lần và đảm bảo bạn hiểu mọi thứ. Nếu có điều gì gây nhầm lẫn hoặc bạn cần biết thêm thông tin, hãy liên hệ **TTL** (Test Team Lead) qua chat của test cycle.

---

### 2. Chuẩn bị hệ thống trước khi kiểm thử

| # | Việc cần làm | Lý do |
|---|-------------|-------|
| ❌ | Tắt các **tiện ích mở rộng** trình duyệt (ad-blockers...) | Tránh can thiệp vào hoạt động của app |
| 🧹 | Xóa **cookies và cache** trình duyệt | Đảm bảo trạng thái sạch |
| 🔒 | Tắt **VPN** (nếu đang bật) | Tránh ảnh hưởng đến kết nối và định vị |
| 🗂️ | Đóng các **app và tab** không cần thiết | Tối ưu hiệu suất và tránh nhiễu |

---

### 3. Sử dụng sản phẩm như một người dùng thực

Bạn nên luôn cố gắng sử dụng sản phẩm kiểm thử **như một người dùng thực** chứ không phải như một "thợ săn bug". Làm như vậy sẽ giúp bạn tìm được những lỗi mà người dùng thực **có khả năng gặp phải nhất**. Do đó, bạn sẽ tìm được những lỗi **có giá trị hơn**.

---

### 4. Tái hiện lỗi nhiều lần

Khi bạn tìm thấy một lỗi, **đừng vội báo cáo ngay**. Thay vào đó, hãy tái hiện (reproduce) lỗi đó **nhiều lần** để chắc chắn rằng lỗi có thể tái hiện được. Nếu không được yêu cầu cụ thể, các lỗi **không thể tái hiện (non-reproducible)** thường sẽ bị từ chối.

---

### 5. Báo cáo lỗi chất lượng cao

Báo cáo lỗi chất lượng rất **quan trọng**. Tránh những điều sau:

| ❌ Tránh | ✅ Nên làm |
|---------|-----------|
| Lỗi chính tả và ngữ pháp | Kiểm tra kỹ trước khi nộp |
| Báo cáo **placeholder issues** (lỗi giữ chỗ) — vi phạm Điều Khoản Sử Dụng | Chỉ nộp báo cáo hoàn chỉnh |
| Không cung cấp đủ thông tin hoặc tệp đính kèm | Cung cấp đầy đủ ảnh chụp, video, log |

---

### 6. Tái hiện lỗi của tester khác (+1)

Tái hiện (reproduce) các lỗi đã được báo cáo bởi tester khác hoặc làm **+1** với tệp đính kèm mang lại lợi ích cho cả bạn và khách hàng:

| Lợi ích | Chi tiết |
|---------|---------|
| 📋 **Nắm bắt lỗi đã báo cáo** | Giúp bạn hiểu những lỗi nào đã được báo cáo → tránh trùng lặp |
| 📈 **Tăng xếp hạng** | Làm +1 giúp tăng điểm xếp hạng (rating) của bạn |
| 📱 **Hỗ trợ khách hàng** | Giúp khách hàng hiểu lỗi nào có thể tái hiện trên các thiết bị khác |

---

### 7. Tính chuyên nghiệp

Luôn cố gắng **chuyên nghiệp** khi làm việc trên uTest:

| # | Nguyên tắc | Chi tiết |
|---|-----------|---------|
| 📖 1 | **Đọc kỹ mọi thứ** | Hiểu trước khi hành động |
| 🤫 2 | **Không gây ồn ào trong chat** | Không hỏi câu hỏi đã được hỏi, câu hỏi trùng lặp hoặc câu hỏi không liên quan |
| ✍️ 3 | **Viết chuyên nghiệp** | Khi trả lời tin nhắn, tranh luận vấn đề hoặc gửi email cho thành viên nhóm |
| 🤝 4 | **Tôn trọng đồng nghiệp** | Nói chuyện lịch sự với các tester khác |
| 📜 5 | **Tuân thủ Điều Khoản Sử Dụng** | Bao gồm cả AI Guidelines — đây là bộ quy tắc bắt buộc khi làm việc với uTest |

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Best Practices | Các thực hành tốt nhất | Nguyên tắc vàng cho tester |
| Browser Extension | Tiện ích mở rộng trình duyệt | Ad-blocker, VPN extension... |
| Non-reproducible | Không thể tái hiện | Lỗi thường bị từ chối |
| Placeholder Issue | Lỗi giữ chỗ | Bị cấm theo Điều Khoản Sử Dụng |
| +1 / Reproduce | Tái hiện / Xác nhận lỗi | Tăng rating, hỗ trợ khách hàng |
| AI Guidelines | Hướng dẫn sử dụng AI | Quy tắc mới về sử dụng AI trên uTest |
