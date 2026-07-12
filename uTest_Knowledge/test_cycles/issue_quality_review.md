# Kiểm duyệt chất lượng lỗi (Issue Quality Review)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Các báo cáo lỗi sẽ được tự động kiểm tra bởi tính năng **Kiểm duyệt chất lượng lỗi (Issue Quality Review)** ngay sau khi được nộp lên nền tảng, nếu tính năng này được kích hoạt trong chu kỳ kiểm thử. Tính năng này được thiết kế để cải thiện chất lượng tổng thể và tính nhất quán của các báo cáo lỗi, giảm thiểu việc phải chỉnh sửa thủ công cho cả tester và TTL.

Tính năng Kiểm duyệt chất lượng lỗi đánh giá chất lượng của báo cáo lỗi dựa trên các tiêu chí sau:

* **Ngôn ngữ**: Kiểm tra các lỗi đánh máy, lỗi ngữ pháp và ngôn từ không chuyên nghiệp.
* **Lời khuyên tốt nhất (uTest Best Practices)**: Đánh giá báo cáo lỗi dựa trên các tiêu chuẩn trong các khóa học của uTest Academy.
* **Hướng dẫn của chu kỳ**: Kiểm tra tính tuân thủ đối với các yêu cầu đặc thù trong tài liệu tổng quan chu kỳ (cycle overview).

Kết quả sau khi đánh giá:

* **Nếu không phát hiện lỗi nào**: Tính năng này sẽ giữ nguyên báo cáo lỗi ban đầu của bạn.
* **Nếu phát hiện một vài lỗi nhỏ**: Tính năng này tự động sửa đổi báo cáo để khắc phục các lỗi được phát hiện. Trạng thái báo cáo lỗi vẫn là **New** (Mới) và bạn sẽ không nhận được thông báo nào về các thay đổi tự động này.
* **Nếu phát hiện nhiều lỗi lớn**: Tính năng này sẽ tự động gửi yêu cầu bổ sung thông tin (info request) vào báo cáo lỗi của bạn. Bạn sẽ nhận được thông báo yêu cầu sửa các lỗi đó, tương tự như các yêu cầu bổ sung thông tin thông thường khác.

#### Cách xử lý yêu cầu bổ sung thông tin (Info Request) từ hệ thống Kiểm duyệt chất lượng lỗi:
1. Mở báo cáo lỗi của bạn và xem nội dung yêu cầu bổ sung thông tin.
2. Nhấp vào liên kết **Edit Issue** (Chỉnh sửa báo cáo lỗi).
3. Bạn sẽ thấy giao diện **So sánh song song (side-by-side comparison)** cho từng trường thông tin, với cột bên trái hiển thị phiên bản hiện tại của bạn và cột bên phải hiển thị các thay đổi được đề xuất bởi hệ thống Kiểm duyệt chất lượng lỗi.
   * *Lưu ý:* Không phải trường thông tin nào cũng có đề xuất chỉnh sửa. Các trường có đề xuất chỉnh sửa sẽ được in đậm (bolded), trong khi các trường không có đề xuất sẽ không được in đậm.
4. Bạn có thể chọn một trong các phương án sau:
   * **Chấp nhận toàn bộ đề xuất**: Nhấp vào nút **Submit New Version** (Nộp phiên bản mới) mà không cần thực hiện thêm thay đổi nào.
   * **Điều chỉnh một số đề xuất**: Sửa đổi một số nội dung theo ý bạn từ các đề xuất đó, sau đó nhấp vào nút **Submit New Version**.
   * **Từ chối toàn bộ đề xuất**: Giữ nguyên phiên bản báo cáo ban đầu bằng cách nhấp vào nút **Re-Submit Original Version** (Nộp lại phiên bản gốc).
5. Sau khi thực hiện, trạng thái của báo cáo lỗi sẽ chuyển lại thành **New** (Mới) và TTL sẽ nhận được thông báo để kiểm tra lại.

#### Cách hủy bỏ báo cáo lỗi (discard) sau khi Kiểm duyệt chất lượng lỗi:
Bạn vẫn có thể hủy bỏ báo cáo lỗi của mình sau khi hệ thống Kiểm duyệt chất lượng lỗi gửi yêu cầu bổ sung thông tin. Các bước thực hiện tương tự như hướng dẫn trong khóa học *Cách chỉnh sửa Báo cáo lỗi*:

1. Mở báo cáo lỗi của bạn.
2. Nhấp vào nút **Actions**.
3. Chọn **Discard** (Hủy bỏ/Bỏ qua).
4. Xác nhận lựa chọn của bạn.

*Lưu ý:* Bạn vẫn có thể thực hiện hủy bỏ báo cáo này ngay cả sau khi bạn đã chỉnh sửa và chấp nhận, điều chỉnh hoặc từ chối các thay đổi được đề xuất bởi hệ thống.

#### Lưu ý quan trọng liên quan đến Kiểm duyệt chất lượng lỗi (Issue Quality Review):
* Việc đánh giá tự động này chỉ diễn ra **duy nhất một lần** khi bạn nộp báo cáo. Nếu bạn chỉnh sửa báo cáo lỗi và gửi lại, hệ thống sẽ không thực hiện đánh giá tự động thêm lần nào nữa.
* Nếu TTL, TE hoặc Khách hàng trực tiếp chỉnh sửa báo cáo lỗi của bạn, các đề xuất chỉnh sửa của hệ thống tự động sẽ bị vô hiệu hóa, và bạn sẽ không còn nhìn thấy giao diện so sánh các thay đổi đề xuất khi mở báo cáo lỗi nữa.
* Nếu bạn không phản hồi và xử lý yêu cầu bổ sung thông tin này, báo cáo lỗi của bạn sẽ **tự động bị từ chối (rejected)** khi chu kỳ kiểm thử đóng lại.
* Tính năng Kiểm duyệt chất lượng lỗi tự động bằng AI vẫn có những hạn chế và đôi khi có thể làm giảm chất lượng báo cáo lỗi hoặc dịch sai nghĩa. Khuyến nghị bạn nên kiểm tra kỹ các đề xuất thay đổi trước khi áp dụng chúng.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Issue Quality Review | Kiểm duyệt chất lượng lỗi | Tính năng tự động đánh giá và sửa lỗi báo cáo bằng AI |
| Submit New Version | Nộp phiên bản mới | Chấp nhận sửa đổi tự động của hệ thống để nộp lại báo cáo |
| Re-Submit Original Version | Nộp lại phiên bản gốc | Từ chối sửa đổi tự động của hệ thống để giữ nguyên báo cáo cũ |
