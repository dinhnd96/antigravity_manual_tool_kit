# Chỉnh sửa và Cập nhật Test Case

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Tại sao cần phải chỉnh sửa Test Case?
Việc chỉnh sửa một test case có thể cần thiết vì một số lý do sau:
* Tester nhận ra họ đã bỏ sót thông tin, tải lên sai tệp đính kèm sau khi nộp test case, hoặc chọn sai trạng thái của các bước kiểm thử.
* TTL, TE hoặc khách hàng yêu cầu tester cung cấp thêm thông tin và sửa lại test case nếu họ phát hiện sai sót hoặc thiếu sót.

### Khi nào có thể chỉnh sửa Test Case?
Test case chỉ có thể chỉnh sửa khi đang ở các trạng thái sau:

#### 1. Test Case Chờ duyệt (Pending):
Đây là các test case đã được nộp nhưng chưa được TTL xem xét, phê duyệt hoặc từ chối. Bạn (tester) có thể chỉnh sửa và sửa đổi test case đang chờ duyệt này theo các bước sau:
* Mở test case đã nộp.
* Nhấp vào nút **Undo Submission** (Hủy nộp kết quả).
* Chỉnh sửa/sửa đổi nội dung test case.
* Nộp lại test case bằng cách nhấp vào nút **Submit Results** (Nộp kết quả). Nếu bạn để test case ở trạng thái chưa nộp (unsubmitted), TTL sẽ không biết rằng test case đã hoàn thành và sẵn sàng để TTL cùng khách hàng xem xét.

#### 2. Test Case Yêu cầu thông tin (Info Requested):
TTL đã xem xét test case và yêu cầu tester bổ sung thêm thông tin. Khi test case được TTL hoặc Khách hàng yêu cầu thông tin, hãy đảm bảo kiểm tra ngay những gì cần sửa. Các bước sau sẽ hướng dẫn bạn quy trình thực hiện:
* Khi TTL hoặc khách hàng yêu cầu thông tin bổ sung, nền tảng uTest sẽ gửi thông báo đến địa chỉ email của tester. Ngoài ra, trên Bảng điều khiển (uTest Dashboard), tester có thể nhận biết các test case nào đang cần phản hồi qua một hộp thoại có tiêu đề **More Information Requested on Test Case** (Yêu cầu thêm thông tin về Test Case). Nhấp vào nút **View test case** sẽ đưa tester đến thẳng test case cần cập nhật hoặc phản hồi.
* Hoặc, tester có thể mở test cycle từ uTest Dashboard, chọn tab **Test Cases** và mở test case đó ra.
* Khi test case được mở, tester sẽ được dẫn đến tab Mô tả (**Description**). Tại đây, bạn sẽ thấy khung thông báo **Info Requested** (được đánh dấu bằng một thanh màu đỏ ở phía bên trái). Phần này chứa tin nhắn từ TTL giải thích những gì cần phải chỉnh sửa.
* Đọc kỹ và hiểu rõ các hướng dẫn trong phần này để đảm bảo rằng bạn sửa đổi test case của mình chính xác trước khi nộp lại.
* Để bắt đầu sửa và cập nhật test case, bạn cần nhấp vào nút **Undo Submission** (Hủy nộp kết quả).
* Tiến hành sửa đổi và cung cấp đầy đủ thông tin theo yêu cầu.
* Khi hoàn thành việc cung cấp thông tin, hãy nộp lại test case bằng cách nhấp vào nút **Submit Results** (Nộp kết quả). Nếu không nộp lại, TTL sẽ không biết rằng bạn đã bổ sung thông tin cần thiết và hoàn thành test case, dẫn đến việc test case không thể được phê duyệt.
* Nhập tổng thời gian bạn đã dành để thực hiện test case (spent time).
* Nhấp vào nút **Finished** (Hoàn thành).
* Cuối cùng, mở lại test case của bạn, nhấp vào liên kết **"Confirm all requested information is added"** (Xác nhận đã bổ sung đầy đủ thông tin yêu cầu) ở dưới cùng của phần Info Requested để xác nhận rằng bạn đã cung cấp đầy đủ thông tin, thông báo cho TTL và khách hàng, đồng thời chuyển trạng thái của test case từ *Info Requested* sang *Pending*.

### Tin nhắn trong Test Case (Test Case's Messages)
Ngoài các trường hợp trên, TTL hoặc khách hàng có thể gửi tin nhắn trực tiếp vào test case của tester để đặt câu hỏi hoặc yêu cầu làm rõ. Khi có tin nhắn mới, nền tảng uTest sẽ thông báo cho tester qua email. Đồng thời, tester có thể nhìn thấy các test case có tin nhắn mới trên uTest Dashboard thông qua một thông báo pop-up có nhãn **New Message on Test Case** (Tin nhắn mới về Test Case) hiển thị nội dung tin nhắn.
* Bằng cách nhấp vào nút **Reply** (Phản hồi), tester sẽ được chuyển đến test case tương ứng và đi thẳng vào tab **Messages**, nơi họ có thể xem và trả lời tin nhắn của TTL hoặc khách hàng.
* Hoặc, tester có thể mở test cycle từ uTest Dashboard, chọn tab **Test Cases** và mở test case để kiểm tra xem có tin nhắn mới nào trong tab **Messages** hay không. Nếu tab này không xuất hiện, điều đó có nghĩa là chưa có tin nhắn nào được gửi bởi TTL.

### Khi nào KHÔNG THỂ chỉnh sửa Test Case?
* **Bị hủy nhận (Unclaimed)**: Tester hoặc TTL đã hủy nhận slot vì một lý do cụ thể, hoặc slot tự động bị hủy nhận nếu tester không hoàn thành và nộp test case đúng hạn.
* **Chờ phê duyệt hoặc từ chối (Pending for approval or rejection)**: Test case đã được TTL xem xét và thiết lập ở trạng thái chờ duyệt phê duyệt hoặc chờ duyệt từ chối.
* **Bị từ chối (Rejected)**: Test case đã được xem xét và bị từ chối.
* **Đã phê duyệt (Approved)**: Test case đã được xem xét và phê duyệt.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Undo Submission | Hủy nộp kết quả | Rút lại test case đã nộp để chỉnh sửa |
| Info Requested | Yêu cầu thông tin | Trạng thái TTL yêu cầu tester bổ sung/chỉnh sửa |
| Confirm all requested information is added | Xác nhận đã bổ sung đầy đủ thông tin yêu cầu | Liên kết xác nhận đã sửa xong lỗi theo yêu cầu của TTL |
| Pending for approval or rejection | Chờ duyệt phê duyệt hoặc từ chối | Trạng thái trung gian khi test case đang được đánh giá |
| Messages tab | Tab Tin nhắn | Tab chứa các thảo luận trực tiếp về test case |
| Dashboard | Bảng điều khiển | Trang tổng quan chính của uTest |
