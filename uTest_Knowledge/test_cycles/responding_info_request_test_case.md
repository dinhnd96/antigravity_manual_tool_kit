# Phản hồi Yêu cầu thông tin (Info Request) trong Test Case

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Khi một test case được TTL, TE hoặc khách hàng xem xét và yêu cầu bổ sung thông tin, điều quan trọng là bạn cần đọc kỹ phản hồi và xử lý các cập nhật được yêu cầu càng sớm càng tốt.

Khi có yêu cầu bổ sung thông tin, bạn sẽ được thông báo qua:
* **Email thông báo**
* **Tin nhắn trên uTest Dashboard** trong phần "More Information Requested" (Yêu cầu thêm thông tin) ở mục Test Cases
* **Thông báo trên ứng dụng di động** (nếu bạn đã cài đặt ứng dụng uTest)

Hãy đảm bảo kiểm tra kỹ phản hồi và cập nhật test case kịp thời theo những thay đổi được yêu cầu.

Trong email, việc nhấp vào liên kết **"Sign in to uTest to add the requested information to the test case result"** (Đăng nhập vào uTest để bổ sung thông tin yêu cầu vào kết quả test case) sẽ mở trực tiếp test case đó trên nền tảng uTest.

Trên uTest Dashboard, nhấp vào nút **View test case** (Xem test case) cũng sẽ mở test case đó. Tester có thể nhận biết các test case nào cần phản hồi thêm thông qua một hộp thoại có nhãn **More Information Requested on Test Case** (Yêu cầu thêm thông tin về Test Case). Nhấp vào nút **View test case** sẽ đưa tester đến thẳng test case cần cập nhật hoặc phản hồi.

### Cách phản hồi Yêu cầu thông tin (Info Request)
Để phản hồi một yêu cầu thông tin trong test case, hãy thực hiện các bước sau:

1. Mở test cycle từ uTest Dashboard, chọn tab **Test Cases**.
2. Mở test case có yêu cầu bổ sung thông tin (more info requested).
3. Ở phần đầu của test case, đọc kỹ và hiểu rõ thông tin nào đang được yêu cầu.
4. Đọc cẩn thận các hướng dẫn được cung cấp trong phần này để đảm bảo bạn chỉnh sửa test case chính xác trước khi nộp lại.
5. Để bắt đầu sửa và cập nhật test case, nhấp vào nút **Undo Submission** (Hủy nộp kết quả).
6. Cuộn đến bước cần sửa hoặc bổ sung thông tin theo yêu cầu.
7. Cập nhật (các) bước kiểm thử cho phù hợp.
8. Nhấp vào nút **Submit Results** (Nộp kết quả).
9. Nhập tổng thời gian bạn đã dành để thực hiện test case (spent time).
10. Nhấp vào nút **Finished** (Hoàn thành).
11. Mở lại test case của bạn, sau đó nhấp vào liên kết **"Confirm all requested information is added"** (Xác nhận đã bổ sung đầy đủ thông tin yêu cầu) ở dưới cùng của phần Info Requested để:
    - Xác nhận rằng bạn đã cung cấp đầy đủ thông tin yêu cầu
    - Thông báo cho TTL và khách hàng
    - Chuyển trạng thái của test case từ **Info Requested** sang **Pending**
12. Trong trường bình luận (comment field), viết tin nhắn phản hồi cho yêu cầu thông tin mà bạn đã nhận được.
13. Nhấp vào nút **Send Response** (Gửi phản hồi).

**Cách thay thế**: Tester cũng có thể mở test cycle từ uTest Dashboard, chọn tab **Test Cases** và mở test case đó. Khi test case được mở, tester sẽ được dẫn đến tab **Description** (Mô tả). Tại tab này, bạn sẽ thấy khung thông báo **Info Requested** (được đánh dấu bằng một thanh màu đỏ ở phía bên trái). Phần này chứa tin nhắn từ TTL giải thích những gì cần được chỉnh sửa.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Info Request | Yêu cầu thông tin | Trạng thái TTL/TE/khách hàng yêu cầu tester bổ sung |
| More Information Requested | Yêu cầu thêm thông tin | Nhãn hộp thoại hiển thị trên Dashboard |
| Send Response | Gửi phản hồi | Nút gửi tin nhắn phản hồi cho yêu cầu thông tin |
| Description tab | Tab Mô tả | Tab chứa thông tin mô tả và Info Requested panel |
| Confirm all requested information is added | Xác nhận đã bổ sung đầy đủ thông tin yêu cầu | Liên kết bắt buộc nhấp sau khi sửa xong |
