# Quy Trình Chu Kỳ Kiểm Thử Trên uTest

> **Nguồn gốc**: uTest Academy – Test Cycle Process at uTest  
> **Ngày dịch**: 2026-05-17  
> **Chủ đề**: test_cycles

---

## Bản dịch

### Tổng quan quy trình

Hãy cùng tìm hiểu tổng quan về cách chu kỳ kiểm thử (test cycle) hoạt động trên uTest.

---

### 1. Lời mời (Invitation)

Khi một chu kỳ kiểm thử mới sẵn sàng, uTest sẽ gửi lời mời đến các tester phù hợp — cách uTest lựa chọn tester cho mỗi chu kỳ đã được thảo luận trước đó. Tester cần **đọc kỹ phần Tổng quan (Overview)** rồi mới chấp nhận lời mời tham gia.

### 2. Kiểm thử & Báo cáo (Testing & Reporting)

Tester nắm rõ yêu cầu và bắt đầu quá trình kiểm thử. Một chu kỳ kiểm thử thường kéo dài **2–3 ngày**. Trong giai đoạn này, tester có thể nộp bug và hoàn thành test case.

### 3. Kết thúc chu kỳ (End of Test Cycle)

Khi giai đoạn kiểm thử kết thúc, chu kỳ sẽ bị **khóa (locked)**. Không thể nộp thêm báo cáo lỗi hay test case nào nữa. Đội ngũ uTest và khách hàng sẽ tiếp tục review tất cả bug đã báo cáo và test case đã nộp.

> Trong các khóa học tiếp theo, chúng ta sẽ thảo luận chi tiết từng bước.

---

## Các Trạng Thái Của Chu Kỳ Kiểm Thử (Test Cycle Statuses)

Một chu kỳ kiểm thử trên uTest có **4 trạng thái**:

### 🟡 Chờ kích hoạt (Pending Activation)

- Chu kỳ đã được **lên lịch kích hoạt**
- Tester có thể đọc Tổng quan và nắm hướng dẫn
- Tester có thể **nhận suất (claim a slot)**
- Tester **KHÔNG ĐƯỢC** kiểm thử sản phẩm, báo cáo lỗi, thực thi test case hay nộp review

### 🟢 Đang hoạt động (Active)

- Chu kỳ đang hoạt động, tester **có thể kiểm thử** sản phẩm
- Tester có thể báo cáo/chỉnh sửa bug, thực thi test case và nộp review

### 🔒 Đã khóa (Locked)

- Tester **KHÔNG THỂ** báo cáo thêm bug hay nộp test case mới
- Báo cáo lỗi và test case **có thể chỉnh sửa** nếu đang ở trạng thái **"Info Requested"** (yêu cầu bổ sung thông tin)
- Tester vẫn có thể trao đổi trong chat
- Các bài nộp sẽ được **review**

### ⚫ Đã đóng (Closed)

- Chu kỳ kiểm thử **hoàn tất**, mọi bài nộp đã được review xong
- **Không thể thực hiện bất kỳ hành động nào** trong chu kỳ ở giai đoạn này
- Tester chỉ có thể xem lại chi tiết chu kỳ và review bài nộp của mình

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Pending Activation | Chờ kích hoạt | Trạng thái đầu tiên của test cycle |
| Active | Đang hoạt động | Tester được phép test và nộp bug |
| Locked | Đã khóa | Không nộp thêm được, chỉ sửa nếu Info Requested |
| Closed | Đã đóng | Hoàn tất, chỉ xem lại |
| Claim a Slot | Nhận suất tham gia | Đăng ký vị trí trong cycle khi Pending |
| Info Requested | Yêu cầu bổ sung thông tin | TTL cần tester cung cấp thêm dữ liệu |
| Testing Phase | Giai đoạn kiểm thử | Khoảng thời gian cycle Active |
