# Tính năng Xác nhận lỗi (Confirm Issue Feature)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Tính năng xác nhận lỗi +1 là gì?
Tính năng xác nhận lỗi (confirm issue report) hoặc tính năng "+1" cho phép các tester xác nhận lại một lỗi (bug) đã được báo cáo bởi tester khác nếu họ cũng tái hiện được lỗi đó trên thiết bị của mình.

### Khi nào bạn nên sử dụng tính năng +1?
* Khi bạn có thể tái hiện được lỗi của tester khác và bạn chắc chắn rằng báo cáo lỗi đó là chính xác và nằm trong phạm vi (in scope) của chu kỳ.
* Khi bạn phát hiện ra một lỗi nhưng nhận ra tester khác đã báo cáo lỗi đó sớm hơn bạn, bạn nên chuyển sang xác nhận báo cáo lỗi đó thay vì nộp lỗi trùng lặp.

### Lợi ích của việc sử dụng tính năng +1
* Nếu báo cáo lỗi bạn xác nhận được phê duyệt (approved), bạn sẽ được cộng một số điểm nhỏ vào điểm xếp hạng (tester rating) của mình.
* Việc xác nhận báo cáo lỗi giúp khách hàng nhanh chóng xác minh mức độ ảnh hưởng của lỗi.

### Cách sử dụng tính năng +1
Làm theo các bước sau:
1. Mở trang chu kỳ kiểm thử và chuyển đến tab **Issues** (Các lỗi).
2. Tìm lỗi mà bạn muốn xác nhận.
3. Nhấp vào nút **+1**.
4. Chọn môi trường kiểm thử của bạn, cung cấp bình luận (comment) và tải lên tệp đính kèm.
   * Nếu đó là lỗi giao diện (visual bug), thông thường bạn chỉ cần tải lên ảnh chụp màn hình.
   * Nếu đó là bất kỳ loại lỗi nào khác không thể thể hiện rõ ràng chỉ qua ảnh chụp màn hình, bạn nên tải lên video.
5. Nhấp vào nút **+1 Confirm Issue Reproduction** (Xác nhận tái hiện lỗi +1) và đợi thông báo xác nhận thành công từ hệ thống.

*Lưu ý:* Tuyệt đối không sử dụng tính năng +1 nếu bạn không tái hiện được lỗi đó. Mọi lượt xác nhận (+1) đều bắt buộc phải đính kèm tệp chứng minh lỗi xuất hiện rõ ràng. Đừng lạm dụng tính năng này vì TTL sẽ giám sát chặt chẽ mọi hoạt động của bạn.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Confirm Issue Feature | Tính năng xác nhận lỗi | Cho phép tester xác nhận lỗi của người khác nếu tái hiện được |
| Confirm Issue Reproduction | Xác nhận tái hiện lỗi | Nút chức năng hoàn thành việc xác nhận lỗi của người khác |
