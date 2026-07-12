# Tính năng Danh sách chờ Slot (Slot Waitlist Feature)

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Tính năng danh sách chờ slot (Slot Waitlist) cho phép các tester tham gia vào danh sách chờ đối với các slot đã đạt giới hạn nhận (claim limit). Tester khi tham gia vào danh sách chờ slot sẽ được thông báo qua email, thông báo đẩy (push notification) trên ứng dụng di động uTest, và một thông báo cũng sẽ được hiển thị trên nền tảng tester khi một slot được mở lại để nhận.

Bạn có thể tham gia danh sách chờ slot bằng cách nhấp vào nút **"Join Waitlist"** (Tham gia Danh sách chờ). Tuy nhiên, số lượng danh sách chờ mà một tester có thể tham gia là có giới hạn. Khi đã đạt đến giới hạn này, nút **"Join Waitlist"** sẽ bị vô hiệu hóa và làm mờ (grayed out). Một thông báo cho biết bạn đã đạt giới hạn số lượng danh sách chờ có thể tham gia sẽ hiển thị khi bạn cố gắng tham gia một danh sách chờ mới. Nếu muốn rời khỏi danh sách chờ, hãy nhấp vào nút **"Leave Waitlist"** (Rời khỏi Danh sách chờ).

Cũng có một giới hạn về số lượng tester cho mỗi danh sách chờ. Khi đã đạt giới hạn này, không tester mới nào có thể tham gia và nút **"Join Waitlist"** sẽ bị vô hiệu hóa. Nếu một tester rời khỏi danh sách chờ, một chỗ trống sẽ được mở ra và bất kỳ tester nào đủ điều kiện đều có thể tham gia.

Chỉ những tester chưa có suất kiểm thử test case (test case slot) mới được phép tham gia danh sách chờ slot. Nếu bạn đã nhận một test case slot, bạn sẽ không thể tham gia danh sách chờ và nút **"Join Waitlist"** sẽ bị vô hiệu hóa. Ngoài ra, nếu bạn đã tham gia danh sách chờ slot nhưng sau đó lại nhận một test case slot, bạn sẽ bị xóa khỏi tất cả các danh sách chờ đã tham gia trước đó.

Tester có suất kiểm thử thăm dò (Exploratory slot) vẫn đủ điều kiện để tham gia danh sách chờ slot vì suất kiểm thử thăm dò không liên kết với test case nào.

Khi một slot được mở lại để nhận (claim), các tester trong danh sách chờ sẽ có một khoảng thời gian giới hạn để nhận slot đó trước khi nó được mở công khai cho tất cả các tester đủ điều kiện trong cycle. Trong thời gian này, khi tester trong danh sách chờ quay lại uTest, dòng chứa slot đó sẽ được làm nổi bật để nhấn mạnh rằng slot đang khả dụng để nhận. Nếu không có tester nào trong danh sách chờ nhận slot trong thời gian độc quyền (exclusivity period) này, bất kỳ tester đủ điều kiện nào khác trong cycle cũng có thể nhận slot, bao gồm cả những người trước đó không nằm trong danh sách chờ.

### Một số lưu ý khác về tính năng Danh sách chờ Slot (Slot Waitlist):
- Các thiết lập danh sách chờ slot áp dụng cho tất cả các slot trong cycle và không thể tùy chỉnh riêng cho một slot cụ thể.
- Một tester tham gia danh sách chờ nhưng không nhận slot khác thì không được coi là đã chính thức tham gia cycle (trong trường hợp cycle yêu cầu phải nhận slot trước khi tham gia). Do đó, bạn sẽ cần nhận một Exploratory slot để tham gia cycle nếu trong cycle có sẵn Exploratory slots.
- Để đảm bảo tính công bằng, bạn không thể xem những tester nào đang nằm trong danh sách chờ slot. Tuy nhiên, bạn có thể xem có bao nhiêu tester đã tham gia danh sách chờ từ phần Available slots (Các suất khả dụng).
- Đội ngũ Dịch vụ Kiểm thử (Testing Services team) không thể lựa chọn một tester cụ thể từ danh sách chờ để nhận slot, vì điều này sẽ làm mất đi tính công bằng của tính năng này.
- Tiêu chí của slot được xem xét khi xác định điều kiện tham gia danh sách chờ. Trong trường hợp tiêu chí slot thay đổi, bất kỳ tester nào đang trong danh sách chờ không còn phù hợp với tiêu chí mới cập nhật sẽ bị xóa khỏi danh sách chờ và được thông báo.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Slot Waitlist | Danh sách chờ slot | Tính năng cho phép đăng ký chờ khi slot đầy |
| Join Waitlist | Tham gia Danh sách chờ | Nút bấm để tham gia danh sách chờ |
| Leave Waitlist | Rời khỏi Danh sách chờ | Nút bấm để hủy tham gia danh sách chờ |
| Exclusivity period | Khoảng thời gian độc quyền | Thời gian ưu tiên chỉ dành riêng cho tester trong waitlist |
