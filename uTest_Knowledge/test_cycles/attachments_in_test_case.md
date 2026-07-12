# Tệp đính kèm trong Test Case

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Tester cần đính kèm (các) tệp trong một bước của test case khi có yêu cầu để làm bằng chứng kiểm thử (proof of testing). Các tệp đính kèm phổ biến nhất bao gồm ảnh chụp màn hình (screenshots), video và tệp nhật ký (logs).

### Đính kèm cái gì và Khi nào cần đính kèm?
* Chỉ tải lên tệp đính kèm phù hợp nếu có yêu cầu. Không tải lên bất kỳ thứ gì khi không có yêu cầu.
* Chỉ tải lên những gì được yêu cầu trong bước kiểm thử. Bạn có thể xem số lượng tệp đính kèm bắt buộc ở ngay bên cạnh tiêu đề của bước.

### Các thực hành tốt nhất (Best Practices) với Tệp đính kèm
* **Nén video dung lượng lớn**: Nếu tệp video quá lớn, hãy sử dụng một công cụ tiện ích để nén nó. Các tệp video rất dễ có dung lượng vượt quá giới hạn tải lên. Cách đơn giản nhất để xử lý việc này là sử dụng một ứng dụng như Handbrake để nén video. Bạn có thể tham khảo hướng dẫn cách sử dụng tại đây: Handbrake.
* **Xác nhận tệp đính kèm**: Luôn đảm bảo rằng tất cả các tệp đính kèm của bạn đã được tải lên thành công. Hãy mở từng tệp đính kèm sau khi tải lên để chắc chắn rằng tệp không bị lỗi hoặc hỏng.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Proof of testing | Bằng chứng kiểm thử | Tài liệu/tệp đính kèm chứng minh quá trình kiểm thử |
| Screenshot | Ảnh chụp màn hình | Tệp đính kèm hình ảnh |
| Log | Tệp nhật ký (Log) | Tệp ghi lại hoạt động hệ thống |
| Handbrake | Handbrake | Ứng dụng nén video mã nguồn mở |
