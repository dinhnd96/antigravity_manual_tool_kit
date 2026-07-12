# Tìm hiểu về Báo cáo lỗi (Understanding Issue Report)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Báo cáo lỗi (Issue Report) là gì?
Báo cáo lỗi (Issue Report) là một văn bản tóm tắt chi tiết về một lỗi (bug). Nó chứa tất cả các thông tin cần thiết để hiểu, tái hiện và sửa lỗi đó.

Để bắt đầu viết báo cáo lỗi, bạn chỉ cần nhấp vào nút **Report Issue** (Báo cáo vấn đề / Nộp lỗi) màu xanh lam ở phần đầu trang của chu kỳ kiểm thử. Giao diện biểu mẫu báo cáo lỗi sẽ mở ra.

### Các trường thông tin trong báo cáo lỗi
Một báo cáo lỗi gồm nhiều trường thông tin mà tester cần phải điền một cách chính xác và đầy đủ.

Dưới đây là các trường thông tin phổ biến trong một báo cáo lỗi:

* **Issue Title (Tiêu đề lỗi)**: Mô tả rõ ràng về lỗi phát sinh, tester nên tuân theo định dạng tiêu đề được quy định trong phần tổng quan chu kỳ (cycle overview).
* **Issue Type (Loại lỗi)**: Chọn loại lỗi mà bạn đang báo cáo (chúng ta đã thảo luận về các loại lỗi trong khóa học trước).
* **Frequency (Tần suất xuất hiện)**: Xác định số lần lỗi có thể tái hiện. Ví dụ: Mọi lúc (Everytime), thỉnh thoảng (Sometimes), v.v.
* **Priority (Mức độ ưu tiên)**: Chọn mức độ nghiêm trọng của lỗi (chúng ta sẽ thảo luận chi tiết về từng tùy chọn trong khóa học Mức độ nghiêm trọng so với Giá trị - Severity vs Value). Đôi khi khách hàng sẽ quy định cụ thể mức độ nghiêm trọng nào là nghiêm trọng (critical), cao (high), trung bình (medium) hoặc thấp (low) trong phần overview, vì vậy hãy đọc kỹ tài liệu tổng quan.
* **Source (Nguồn)**: Chọn nguồn phát hiện lỗi đến từ kiểm thử thăm dò (Exploratory testing) hay từ kiểm thử cấu trúc (Structured testing) trong quá trình thực thi test case.
* **Environment (Môi trường)**: Chọn môi trường phát sinh lỗi, hãy đảm bảo chọn đúng tổ hợp thiết bị, trình duyệt và hệ điều hành.
* **Actions Performed (Các bước thực hiện)**: Ghi lại toàn bộ các bước bạn đã thực hiện để tạo ra lỗi đó. Đảm bảo sử dụng các bước được đánh số thứ tự và bắt đầu từ bước mở trang web hoặc ứng dụng.
* **Expected Results (Kết quả mong đợi)**: Mô tả chính xác những gì người dùng mong đợi sẽ xảy ra khi thực hiện các bước trong phần Actions Performed.
* **Actual Results (Kết quả thực tế)**: Mô tả chính xác những gì thực sự xảy ra khi người dùng thực hiện các bước trong phần Actions Performed.
* **Error Messages (Thông báo lỗi)**: Ghi lại thông báo lỗi mà bạn nhận được (nếu có).
* **Additional Environment Info (Thông tin môi trường bổ sung)**: Sử dụng trường này để cung cấp thêm bất kỳ thông tin nào khác về môi trường, nếu không có hãy để trống.
* **Attachments (Tệp đính kèm)**: Tải lên tất cả các tệp đính kèm được yêu cầu, chẳng hạn như ảnh chụp màn hình (screenshots), video ghi màn hình (screen recordings), tệp nhật ký (logs), v.v.

Sau khi tất cả các trường thông tin được điền đầy đủ và chính xác, hãy kiểm tra lại báo cáo một lần nữa và nhấp vào nút **Submit** (Gửi) để nộp lỗi.

### Có giới hạn số lượng lỗi mà một tester có thể báo cáo không?
Các tester chưa có xếp hạng (Unrated) và đã có xếp hạng cơ bản (Rated) sẽ bắt đầu với giới hạn tối đa là **5 lỗi chưa được phê duyệt (unapproved issues)** trên mỗi chu kỳ kiểm thử. Khi một trong số các lỗi bạn nộp được phê duyệt (approved), bạn sẽ có thể nộp thêm một lỗi khác; và quy trình cứ tiếp tục như vậy. Hạn chế này sẽ được dỡ bỏ khi xếp hạng tester của bạn tăng lên mức cao hơn như Vàng (Gold), Bạc (Silver), Đồng (Bronze) hoặc Tester có năng lực (Proven rated tester).

### Có giới hạn số lượng lỗi được phép nộp trong một chu kỳ không?
Có, mọi chu kỳ kiểm thử đều có giới hạn tổng số lỗi có thể nộp. Mỗi chu kỳ kiểm thử có cấu hình riêng và có thể được điều chỉnh tùy theo yêu cầu của khách hàng. Lưu ý rằng khi chu kỳ đạt tới giới hạn này, nút **Report Issue** sẽ bị vô hiệu hóa và không thể nộp thêm lỗi được nữa.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Issue Report | Báo cáo lỗi / Báo cáo vấn đề | Văn bản chi tiết mô tả lỗi phần mềm |
| Actions Performed | Các bước thực hiện | Các bước thao tác để tái hiện lỗi |
| Unrated Tester | Tester chưa xếp hạng | Xếp hạng khởi đầu của tester mới |
| Rated Tester | Tester đã xếp hạng | Tester đã có điểm xếp hạng cơ bản |
| Proven Tester | Tester có năng lực | Hạng tester hoạt động tốt và ổn định |
