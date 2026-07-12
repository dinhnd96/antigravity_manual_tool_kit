# Thực thi Test Case (Executing Test Cases)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Xem Test Case và các bước kiểm thử
Một test case bao gồm một chuỗi các bước cần thiết để kiểm thử sản phẩm. Bạn có thể xem, thực thi và nộp kết quả các test case trực tiếp từ thiết bị di động bằng ứng dụng uTest.

1. Để bắt đầu, hãy mở trang của bất kỳ chu kỳ kiểm thử nào và chuyển đến tab **Test Cases**. Tại đây bạn sẽ thấy các test case khả dụng (available) và các test case bạn đã nhận (claimed).
2. Để xem chi tiết các bước của một test case cụ thể, hãy chạm vào tiêu đề của test case đó.
3. Ở phần đầu trang, bạn sẽ thấy thanh tiến trình (progress bar), thông tin về tester, phiên bản bản dựng (build) và môi trường kiểm thử (environment). Phía bên dưới là các hướng dẫn của test case và toàn bộ các bước cần thực thi.
4. Điều cực kỳ quan trọng là bạn phải thực thi test case bằng chính xác môi trường mà bạn đã đăng ký nhận (claim).

### Thực thi và nộp kết quả test case
Tester có trách nhiệm thực thi đầy đủ các bước trong test case và nộp kết quả đúng thời hạn yêu cầu. Hãy xem cách thực thi các bước trên ứng dụng di động uTest:

1. Để bắt đầu, mở trang chi tiết test case và chạm vào bất kỳ bước nào để bắt đầu thực hiện. Bạn nên bắt đầu từ bước số 1.
2. Đọc kỹ hướng dẫn và hoàn thành bước bằng cách đánh dấu trạng thái của bước là **Done** (Đã thực hiện) hoặc **Pass** (Đạt) / **Fail** (Không đạt). Nếu bước đó yêu cầu tải lên tệp đính kèm, bạn có thể chạm vào nút **+** dưới phần *Results attachments*. Bạn có thể vuốt màn hình sang ngang để chuyển nhanh giữa các bước.
3. Khi bạn đánh dấu một bước là **Pass** hoặc **Fail**, hệ thống sẽ yêu cầu bạn nhập bình luận (comment). Việc thêm bình luận là không bắt buộc khi bước đó Pass, nhưng là **bắt buộc** khi bước đó bị Fail.
4. Hệ thống sẽ yêu cầu bạn báo cáo lỗi (report an issue) nếu bạn đánh dấu một bước là Fail. Bạn nên đối chiếu các lỗi đã được báo cáo trong chu kỳ trước khi nộp lỗi mới. Trong trường hợp lỗi đó đã được báo cáo từ trước, hãy chạm vào **Cancel** (Hủy) trên cửa sổ popup.
5. Sau khi hoàn thành thực thi toàn bộ các bước, hãy nộp kết quả test case bằng cách chạm vào nút **Submit Test Case** (Nộp Test Case).
6. Điền thông tin về thời gian thực hiện (time spent), thêm các bình luận cần thiết và chạm vào **Submit** một lần nữa để chính thức nộp Test Case của bạn.

*Lưu ý:* Ứng dụng di động uTest cho phép bạn hủy nhận (unclaim) hoặc hủy nộp kết quả (**Unsubmit / Undo Submission**) test case của mình. Bạn cũng có thể xem tin nhắn hoặc phản hồi các yêu cầu bổ sung thông tin (info requests) trực tiếp từ ứng dụng uTest. Để thực hiện các hành động này, hãy làm theo các bước sau:

1. Mở ứng dụng uTest.
2. Trên tab **Home** (Trang chủ) hoặc **Projects** (Dự án), chạm vào biểu tượng **Notifications** (Thông báo) ở góc trên cùng bên phải.
3. Chạm vào tin nhắn hoặc yêu cầu mà bạn muốn phản hồi. Lưu ý rằng trang thông báo sẽ hiển thị tất cả các thông báo của bạn, bất kể đó là tin nhắn thông thường hay yêu cầu cung cấp thêm thông tin.
4. Nếu đó là tin nhắn thảo luận thông thường, bạn có thể xem nội dung, thực hiện các thay đổi nếu cần, và trả lời lại tin nhắn đó.
5. Nếu đó là yêu cầu bổ sung thông tin (info request), hãy tiếp tục thực hiện theo các bước sau:
   * Mở tin nhắn và đọc kỹ yêu cầu của TTL.
   * Chạm vào biểu tượng quay lại `<` để trở về trang test case, sau đó cuộn xuống dưới và chạm vào nút **Unsubmit Test Case** (Hủy nộp Test Case), và xác nhận để mở lại quyền chỉnh sửa test case.
   * Thực hiện sửa đổi và bổ sung thông tin cho test case theo đúng yêu cầu của TTL.
   * Sau khi hoàn tất các thay đổi, chạm vào biểu tượng quay lại `<` để về trang test case, sau đó cuộn xuống dưới và chạm vào nút **Submit Test Case**.
   * Nhập lại thời gian thực hiện (time spent) và thêm các bình luận bổ sung nếu có (tùy chọn).
   * Chạm vào nút **Submit**.
   * Chạm lại vào biểu tượng **Notification** ở góc trên cùng bên phải và chạm vào nút **Send Confirmation** (Gửi xác nhận) để xác nhận với TTL rằng toàn bộ thông tin yêu cầu đã được cung cấp đầy đủ.
6. Ngoài ra, bạn cũng có thể thực hiện xử lý yêu cầu bổ sung thông tin từ chính trang test case bằng cách mở nó ra và chạm vào biểu tượng **Notifications** ở góc trên cùng bên phải.

---

## Thuật ngữ quan trọng

*(Không có thuật ngữ mới cần bổ sung cho bài viết này)*
