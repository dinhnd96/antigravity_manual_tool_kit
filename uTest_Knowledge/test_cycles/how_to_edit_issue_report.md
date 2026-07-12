# Cách chỉnh sửa Báo cáo lỗi (How to Edit an Issue Report)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Tại sao một báo cáo lỗi cần phải chỉnh sửa?
Sẽ có nhiều tình huống bạn cần chỉnh sửa báo cáo lỗi của mình, ví dụ như:
* Bạn nhận ra mình đã bỏ sót điều gì đó hoặc nhập sai thông tin sau khi nộp báo cáo lỗi.
* Trưởng nhóm kiểm thử (TTL) yêu cầu bạn chỉnh sửa và sửa lại báo cáo lỗi do bạn mắc lỗi hoặc thiếu thông tin cần thiết.

### Khi nào báo cáo lỗi có thể chỉnh sửa?
Báo cáo lỗi chỉ có thể chỉnh sửa được khi nó đang ở một trong các trạng thái sau:
* **New (Mới)**: Báo cáo lỗi mới được nộp và chưa được TTL kiểm tra.
* **Info Requested (Yêu cầu thông tin)**: Báo cáo lỗi đã được TTL xem xét và yêu cầu tester bổ sung thêm thông tin.
  * *Lưu ý:* Sau khi báo cáo lỗi đã được TTL hoặc Khách hàng kiểm tra, vui lòng tránh thay đổi toàn bộ lỗi cũ thành một lỗi mới hoàn toàn, vì điều này có thể bị coi là nộp lỗi giữ chỗ (placeholder issue).
* **Rejected (Bị từ chối)**: Báo cáo lỗi đã bị xem xét và từ chối.
  * *Lưu ý:* Bạn chỉ nên chỉnh sửa báo cáo lỗi bị từ chối khi bạn chuẩn bị thực hiện khiếu nại (dispute) vì cho rằng lỗi đó bị từ chối nhầm hoặc bạn không đồng ý với lý do từ chối. Trong trường hợp đó, bạn có thể chỉnh sửa báo cáo để làm rõ hơn và cung cấp thêm thông tin hoặc tệp đính kèm để hỗ trợ lý do khiếu nại của mình.

### Khi nào báo cáo lỗi KHÔNG THỂ chỉnh sửa?
Báo cáo lỗi không thể chỉnh sửa nếu nó ở các trạng thái sau:
* **Pending (Chờ duyệt)**: Báo cáo lỗi đã được TTL phê duyệt và đang chờ quyết định cuối cùng từ TE hoặc Khách hàng.
* **Approved (Đã phê duyệt)**: Báo cáo lỗi đã được xem xét và phê duyệt.

### Cách chỉnh sửa một báo cáo lỗi
Làm theo các bước dưới đây để chỉnh sửa báo cáo lỗi:
1. Đầu tiên, hãy mở báo cáo lỗi của bạn, xem lại nội dung và kiểm tra tin nhắn từ TTL trong tab **Messages** (nếu có).
2. Hiểu rõ những thay đổi cần thực hiện.
3. Nhấp vào nút **Actions** và chọn **Edit Issue**.
4. Sửa lại báo cáo lỗi của bạn và nhấp vào nút **Submit Issue** sau khi hoàn thành.
5. **Quan trọng:** Nếu TTL gửi yêu cầu bổ sung thông tin (info request) yêu cầu bạn sửa báo cáo, bạn phải nhấp vào **Confirm all requested info is added** (Xác nhận tất cả thông tin yêu cầu đã được thêm) hoặc **Actions > Send Requested Info** sau khi hoàn tất để chuyển trạng thái báo cáo lỗi trở lại **New**. Việc này giúp TTL biết báo cáo của bạn đã sẵn sàng để kiểm tra lại (họ sẽ nhận được thông báo sau khi bạn xác nhận).

### Cách cập nhật tệp đính kèm
Để thay đổi hoặc thêm tệp đính kèm vào báo cáo lỗi:
1. Mở báo cáo lỗi của bạn.
2. Cuộn xuống phần **Attachments** (Không cần phải nhấp vào *Actions > Edit Issue* khi bạn chỉ muốn tải lên các tệp đính kèm mới).
3. Tải tệp lên bằng cách nhấp vào nút **Choose Files** hoặc bạn có thể kéo và thả tệp vào vùng quy định.
4. Đợi cho đến khi thông báo **Upload Complete** (Tải lên hoàn tất) xuất hiện.
5. Nhấp vào tệp đính kèm mới tải lên để kiểm tra xem nó có thể mở được bình thường và không bị hỏng (corrupted) hay không.
6. *Lưu ý:* Hãy xóa bỏ các tệp đính kèm không cần thiết sau khi bạn đã thêm tệp mới. Ví dụ: nếu bạn được yêu cầu che thông tin cá nhân trong video, sau khi chỉnh sửa và tải lên video mới, hãy xóa video cũ đã tải lên trước đó.

### Cách xóa một báo cáo lỗi
Nếu bạn nhận ra lỗi mình báo cáo không hợp lệ sau khi nộp, bạn có thể xóa báo cáo lỗi đó nếu TTL chưa xem xét nó. Làm theo các bước sau:
1. Mở báo cáo lỗi cần xóa.
2. Nhấp vào **Actions** và chọn **Discard** (Hủy bỏ/Bỏ qua).
3. Xác nhận lựa chọn của bạn.

*Lưu ý:*
* Nếu bạn nhận ra lỗi không còn tái hiện được nữa, trong khi hướng dẫn của chu kỳ chỉ yêu cầu báo cáo lỗi có thể tái hiện 100%, bạn nên hủy bỏ (discard) báo cáo đó để tránh bị từ chối, miễn là báo cáo chưa được duyệt trước đó. Quy định này cũng áp dụng nếu bạn nhận ra lỗi thuộc khu vực Ngoài phạm vi (OOS), ví dụ như lỗi nằm trong khu vực OOS hoặc đó là lỗi về trải nghiệm người dùng (usability) trong khi chu kỳ không yêu cầu test usability.
* Nếu báo cáo lỗi của bạn đã từng được TTL xem xét (đã từng chuyển sang trạng thái pending hoặc bị gửi yêu cầu bổ sung thông tin trước đó), ngay cả khi trạng thái hiện tại là **New**, bạn cũng không thể hủy bỏ (discard) nó được nữa. Việc cố gắng hủy bỏ báo cáo lỗi trong điều kiện đó sẽ dẫn đến thông báo lỗi hệ thống. Vì vậy, hãy chắc chắn lỗi đó hợp lệ trước khi báo cáo để tránh bị từ chối.

### Lưu ý quan trọng khi chỉnh sửa báo cáo lỗi
* Luôn báo cáo lỗi tuân thủ theo Hướng dẫn báo cáo lỗi (Issue Reporting Instructions) được nêu trong overview và cố gắng viết báo cáo thật mạch lạc, rõ ràng.
* Tuyệt đối không nộp báo cáo lỗi khi thiếu các tệp đính kèm bắt buộc hoặc không điền đúng thông tin vào các trường bắt buộc, vì hành vi này sẽ bị coi là nộp báo cáo lỗi giữ chỗ (placeholder issue).
* Tuyệt đối không thay đổi lỗi đã nộp sang một lỗi khác hoàn toàn, bất kể báo cáo đang ở trạng thái New hay Info Requested, vì hành vi này sẽ bị coi là nộp báo cáo lỗi giữ chỗ - vi phạm Điều khoản Sử dụng và Nguyên tắc của uTest.
* Hãy thoải mái trả lời tin nhắn của TTL và yêu cầu giải thích rõ hơn nếu bạn không hiểu những gì cần phải thay đổi trong báo cáo dựa trên tin nhắn của họ.
* Bạn không thể chỉnh sửa các tệp đính kèm đã tải lên tại giao diện Edit Issue (`Actions > Edit Issue`). Bạn chỉ có thể sửa đổi chúng trực tiếp trong phần Attachments trên trang báo cáo lỗi (`Mở báo cáo lỗi > Cuộn xuống phần Attachments`).
* Hãy nhớ rằng bạn phải đính kèm đầy đủ các tệp yêu cầu khi báo cáo lỗi. Như đã đề cập ở trên, nếu báo cáo không có tệp đính kèm hoặc chưa hoàn thiện, nó có thể bị coi là lỗi giữ chỗ. Bạn chỉ nên chỉnh sửa hoặc thay thế tệp đính kèm khi được yêu cầu bởi TTL. Tuyệt đối không tải lên các tệp đính kèm mang tính chất giữ chỗ hoặc không liên quan rồi sau đó mới đổi sang tệp chính xác, hành vi này vi phạm quy tắc uTest. Hãy chuẩn bị đầy đủ mọi bằng chứng trước khi bấm gửi báo cáo lỗi.
* Bạn có thể gỡ bỏ các tệp đính kèm cũ nếu được TTL yêu cầu làm mới hoặc chỉnh sửa chúng.

---

## Thuật ngữ quan trọng

*(Không có thuật ngữ mới cần bổ sung cho bài viết này)*
