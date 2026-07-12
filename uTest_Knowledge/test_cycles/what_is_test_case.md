# Hướng dẫn về Test Case trên uTest

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Test Case là gì?
Test Case (Trường hợp kiểm thử) là một chuỗi các bước bắt buộc mà tester cần thực hiện để kiểm thử một sản phẩm. Mỗi bước có thể bao gồm các hướng dẫn cụ thể và kết quả mong đợi (Expected Results) tương ứng. Điều này giúp tester có thể kiểm thử sản phẩm một cách chính xác mà không cần có kiến thức trước về sản phẩm đó.

### Cách thực hiện (Execute) một Test Case?
Hãy làm theo các bước sau để thực thi một test case:

1. **Mở test case và đọc hiểu hướng dẫn**:
   - Nếu hướng dẫn không rõ ràng, hãy hỏi các TTL (Test Team Lead) trong phòng chat của test cycle và chờ xác nhận từ họ.
   - Tránh việc đoán mò hoặc đánh dấu Đạt (Pass) / Không đạt (Fail) một cách ngẫu nhiên chỉ để chuyển sang bước tiếp theo nếu bạn không chắc chắn về cách thực hiện.
   - Giao tiếp tốt là chìa khóa để thực thi test case thành công. Các TTL trong phòng chat của cycle luôn sẵn sàng hỗ trợ giải đáp mọi thắc mắc của bạn.

2. **Kiểm tra các điều kiện tiên quyết (Preconditions) trước khi thực hiện các bước tiếp theo**:
   - Nếu có, phần **Điều kiện tiên quyết của Test Case (Test Case Preconditions)** sẽ xuất hiện bên dưới phần Mô tả Slot (Slot Description). Nếu không có, phần này sẽ không được hiển thị trong test case.
   - Điều kiện tiên quyết có thể bao gồm các hướng dẫn cài đặt thiết bị, hướng dẫn ban đầu hoặc các thiết lập cụ thể bắt buộc phải tuân thủ trước khi bắt đầu.
   - Việc bỏ qua các hướng dẫn này có thể dẫn đến kết quả test case không hợp lệ, và bạn sẽ phải thực hiện lại các bước của test case sau khi đã hoàn thành đúng các điều kiện tiên quyết.

3. **Bắt đầu từ bước đầu tiên (từ trên xuống dưới) và không bỏ qua bất kỳ bước nào**:
   - Đọc và làm theo các hướng dẫn trong môi trường kiểm thử chính xác như được chỉ định trong Mô tả Slot (Slot Description).
   - Kiểm tra xem bước đó có kết quả mong đợi (Expected Results) hay không. Nếu có, hãy xác minh xem kết quả thực tế (Actual Results) sau khi thực hiện hướng dẫn có khớp với kết quả mong đợi hay không.
   - Đánh dấu bước đó là **Đạt (Pass)** nếu kết quả thực tế và kết quả mong đợi trùng khớp.
   - Đánh dấu bước đó là **Không đạt (Fail)** nếu có bất kỳ sự sai lệch nào so với kết quả mong đợi. Sau khi nhấp vào nút Fail, hãy làm theo các hướng dẫn sau trong cửa sổ pop-up hiển thị:
     - *Nếu lỗi đã được báo cáo*: Nhấp xác nhận (+1) cho lỗi đã báo cáo, thêm ID của lỗi (Issue ID) vào trường Kết quả thực tế (Actual Result) và chọn **Fail Step**.
     - *Nếu lỗi chưa được báo cáo*: Viết mô tả ngắn gọn về lỗi trong trường Kết quả thực tế (Actual Result) và báo cáo lỗi bằng cách nhấp vào nút **Fail & Report Issue**.
     - Đảm bảo xóa bỏ đoạn văn bản mẫu (prefilled text) trong các trường Hành động thực hiện (Action Performed), Kết quả mong đợi (Expected Result) và Kết quả thực tế (Actual Result).
     - Điền chính xác tất cả các trường bắt buộc theo lỗi vừa phát hiện, và tuân thủ các hướng dẫn trong phần Hướng dẫn báo cáo lỗi (Issue Reporting Instructions) của tài liệu tổng quan cycle (cycle overview).
     - Các lỗi được báo cáo theo cách này sẽ được liên kết trực tiếp với test case. Hãy chắc chắn sử dụng tính năng này nếu bạn phát hiện các lỗi liên quan đến các bước trong test case mà chưa được báo cáo trước đó.
   - Nếu bước đó không có kết quả mong đợi, hãy đánh dấu bước đó là **Hoàn tất (Done)** sau khi đã đọc và làm theo hướng dẫn.

4. **Hoàn thành tuần tự tất cả các bước và tải lên toàn bộ tệp đính kèm bắt buộc**:
   - Test case sẽ không thể nộp nếu có bất kỳ bước nào chưa hoàn thành.
   - Kiểm tra xem mỗi bước yêu cầu loại tệp đính kèm nào và tải lên đúng yêu cầu.
   - Nếu một bước yêu cầu tải lên ảnh chụp màn hình (screenshot), bạn bắt buộc phải tải lên ảnh chụp màn hình chứ không được dùng video.
   - Làm mờ (Blur) bất kỳ Thông tin nhận dạng cá nhân (PII - Personally Identifiable Information) nào xuất hiện trong các tệp đính kèm. Bạn có thể tham khảo khóa học để tìm hiểu cách làm mờ và hiểu rõ hơn về PII.
   - Nếu gặp lỗi dung lượng file quá lớn khi tải lên video, hãy giảm dung lượng video bằng Handbrake. Hãy xem khóa học để học cách sử dụng Handbrake.
   - Không phải bước nào cũng yêu cầu tệp đính kèm. Hãy đọc kỹ hướng dẫn trong từng bước và trong trường Tệp đính kèm kết quả (Result Attachments) nếu có.
   - Số lượng tệp đính kèm tối thiểu được yêu cầu sẽ hiển thị dưới trường Result Attachments (ví dụ: *Minimum 1*).
   - Nếu không thấy hiển thị thông tin này, nghĩa là tệp đính kèm cho bước đó là tùy chọn (optional). Bạn vẫn có thể tải lên tệp đính kèm nếu chúng liên quan đến bước test case đó. Tuy nhiên, nếu không có hướng dẫn cụ thể nào khác, bạn không cần phải tải lên.

5. **Nộp và hoàn tất test case**:
   - Sau khi hoàn thành tất cả các bước và tải lên đầy đủ tệp đính kèm bắt buộc, hãy nộp test case bằng cách nhấp vào nút **Submit Results**, nhập khoảng thời gian bạn đã dành để thực hiện test case (spent time), sau đó nhấp vào nút **Finished**.
   - Để chỉnh sửa test case đã nộp, bạn có thể hủy nộp bằng cách nhấp vào nút **Undo Submission**. Sau đó, bạn có thể chỉnh sửa test case của mình để sửa các sai sót và nộp lại bằng cách nhấp vào nút **Submit Results**.

### Các điểm lưu ý quan trọng về Test Case
* **Thanh toán cố định**: Test case có mức trả thưởng (payout) cố định. Số tiền có thể thay đổi tùy thuộc vào dự án, yêu cầu, độ phức tạp và thời gian cần thiết để hoàn thành.
  * *Lưu ý*: Các test case trong Academy không được thanh toán vì chúng chỉ phục vụ mục đích đào tạo.
* **Môi trường kiểm thử chính xác**: Tester bắt buộc phải thực thi các bước test case trên môi trường được chỉ định (sự kết hợp của Thiết bị, Hệ điều hành và Trình duyệt). Nếu không, test case sẽ bị từ chối (reject).
* **Liên kết ID lỗi**: Mỗi bước test case bị đánh dấu là Fail đều phải được liên kết với một ID lỗi (issue ID).
* **Chỉ nhận test case khi sẵn sàng**: Chỉ nhận (claim) các test case nếu bạn có thể thực thi chúng ngay lập tức và hoàn thành trong thời gian quy định.
* **Đặt tên tệp đính kèm rõ ràng**: Không tải lên nhiều tệp đính kèm có cùng tên cho một test case. Đảm bảo mỗi tệp đính kèm có tiêu đề rõ ràng và phù hợp, chẳng hạn như khu vực kiểm thử, tính năng hoặc vị trí xảy ra bug. Nếu có hướng dẫn cụ thể trong tài liệu tổng quan cycle hoặc trong chính test case, hãy làm theo quy ước đặt tên tệp đính kèm được đề xuất.
* **Vai trò của tester**: Tester không viết test case, tester chỉ thực thi chúng.

### Kết quả của Test Case (Test Case Results) là gì?
Kết quả của Test Case biểu thị tiến độ thực hiện test case (nếu chưa nộp) hoặc kết quả kiểm thử (nếu đã nộp).

Dưới đây là các loại kết quả của test case trên nền tảng uTest dựa trên tiến trình hoàn thành của chúng:

* **Mới (New)**:
  - Cho biết test case chưa có tiến triển nào. Điều này cũng có nghĩa là chưa có trạng thái của bước nào (Pass, Fail hoặc Done) được chọn trong toàn bộ các bước.
* **Đã bắt đầu (Started)**:
  - Cho biết test case đang được thực hiện nhưng chưa được nộp. Điều này cũng có nghĩa là một hoặc một vài bước trong test case đã được chọn trạng thái (Pass, Fail hoặc Done).
  - *Lưu ý*: Hãy đảm bảo nộp test case sau khi đã hoàn thành tất cả các bước. Nếu không, test case sẽ giữ nguyên ở trạng thái này và bạn có thể sẽ không được thanh toán cho công việc đã làm, vì TTL không thể chuyển các test case ở trạng thái này sang trạng thái Chờ duyệt (Pending), Phê duyệt (Approved) hoặc Từ chối (Rejected). Nếu bạn phớt lờ tin nhắn của TTL và để test case ở trạng thái này, test case có thể bị hủy nhận (unclaimed).
* **Đạt (Passed)**:
  - Cho biết test case đã được nộp và tất cả các bước trong đó đều được đánh dấu là Pass. Trạng thái này cũng có thể đồng nghĩa với việc không phát hiện lỗi nào trong quá trình thực thi test case.
* **Không đạt (Failed)**:
  - Cho biết test case đã được nộp và có một hoặc nhiều bước được đánh dấu là Fail.
  - *Lưu ý*: Kết quả "Failed" ở đây không có nghĩa là bạn đã làm hỏng test case hay test case của bạn sẽ bị từ chối, mà nó chỉ phản ánh kết quả thực tế của việc kiểm thử vì bạn đã đánh dấu Fail ở một hoặc nhiều bước.
* **Hoàn tất (Completed)**:
  - Cho biết test case đã được nộp và tất cả các bước đều được đánh dấu là Done. Nhắc lại rằng, trạng thái "Done" sẽ hiển thị thay thế cho "Pass" và "Fail" khi một bước không yêu cầu kết quả mong đợi. Điều này cũng có nghĩa là không có bước nào trong test case này có kết quả mong đợi.
* **Bị hủy nhận (Unclaimed)**:
  - Cho biết test case đã bị hủy nhận bởi tester hoặc TTL. Một danh mục lý do sẽ được hiển thị trong dấu ngoặc đơn bên cạnh nhãn "Unclaimed" tùy theo lý do hủy nhận được chọn. Ví dụ: *Unclaimed (Time)* khi chọn lý do "Không thể hoàn thành đúng hạn" hoặc *Unclaimed (Blocked)* khi chọn lý do "Bị chặn".
  - Một test case tự động bị hủy nhận bởi hệ thống do quá hạn chót sẽ chỉ hiển thị nhãn "Unclaimed". Tránh nhận test case nếu bạn không thể hoàn thành nó trước khi hết hạn.
  - Ngoài ra, lý do hủy nhận do tester hoặc TTL cung cấp sẽ được hiển thị trong trường Bình luận (Comments).
  - Nếu bạn quyết định hủy nhận một test case, hãy chắc chắn cung cấp lý do rõ ràng. Bằng cách này, TTL hoặc TE có thể theo dõi và hỗ trợ bạn theo lý do được cung cấp nếu cần.
  - Việc cung cấp lý do không rõ ràng hoặc không hoàn thành test case đúng hạn có thể ảnh hưởng đến các lời mời tham gia cycle trong tương lai của bạn. Hãy báo cho team trong phòng chat nếu có việc khẩn cấp đột xuất xảy ra khiến bạn không thể hoàn thành test case.
* **Bị đóng bởi chu kỳ kiểm thử (Closed By TestCycle)**:
  - Cho biết test case đã bị hệ thống tự động hủy nhận vì chưa được nộp và cycle kiểm thử đó đã được đóng lại.

### Trạng thái của Test Case (Test Case Status) là gì?
Trạng thái của test case thể hiện quyết định phê duyệt cuối cùng đối với kết quả của test case đó. Trạng thái của test case được hiển thị trong cột Phê duyệt (Approval) trên tab Test Cases của cycle, hoặc trong mục Trạng thái (Status) sau khi mở test case ra. Dưới đây là các trạng thái của test case trên nền tảng uTest:

* **Chờ duyệt (Pending)**:
  - Trạng thái này cho biết test case vẫn chưa được phê duyệt hay từ chối. Các test case bị hủy nhận (unclaimed) cũng sẽ có trạng thái này vì chúng không còn có thể nộp để kiểm tra thêm được nữa.
  - Nếu test case bạn đã nộp không thể chỉnh sửa, điều đó có nghĩa là nó đã được xem xét bởi một TTL và được đặt sang trạng thái Pending (chờ phê duyệt hoặc chờ từ chối). Trong trường hợp này, bạn chỉ cần đợi cho đến khi có quyết định cuối cùng (Approved hoặc Rejected).
* **Yêu cầu thông tin (Info Requested)**:
  - Trạng thái này cho biết test case đã được xem xét bởi một TTL và họ cần bạn cung cấp thêm thông tin hoặc có các sai sót cần phải chỉnh sửa. Bạn phải sửa lại test case theo yêu cầu và cung cấp thông tin được yêu cầu.
  - Việc phớt lờ tin nhắn của TTL và để test case ở trạng thái này có thể dẫn đến việc bị từ chối, và bạn sẽ không được trả tiền cho công việc đã làm. Hãy đảm bảo phản hồi các yêu cầu thông tin một cách kịp thời.
  - Sau khi sửa đổi và cung cấp đầy đủ thông tin được yêu cầu, bạn phải xác nhận bằng cách nhấp vào liên kết **"Confirm all requested info is added"** (Xác nhận đã bổ sung đầy đủ thông tin yêu cầu). Hành động này sẽ chuyển trạng thái của test case trở lại Pending và thông báo cho TTL biết test case đã sẵn sàng cho một đợt duyệt tiếp theo.
* **Đã phê duyệt (Approved)**:
  - Test case đã được xem xét và chấp thuận. Bạn sẽ nhận được khoản thanh toán cho test case khi nó được duyệt sang trạng thái Approved.
  - *Lưu ý*: Các test case trong Academy không được thanh toán vì chúng chỉ phục vụ mục đích đào tạo.
* **Bị từ chối (Rejected)**:
  - Test case đã được xem xét và bị từ chối. Các test case bị từ chối sẽ không đủ điều kiện để nhận thanh toán. Hãy kiểm tra lý do từ chối trong trường Bình luận (Comments) và tránh lặp lại sai sót tương tự trong tương lai.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Test Case | Trường hợp kiểm thử / Test Case | Thuật ngữ cốt lõi trong QA |
| Precondition | Điều kiện tiên quyết | Thiết lập bắt buộc trước khi test |
| Expected Result | Kết quả mong đợi | Kết quả mong muốn theo thiết kế |
| Actual Result | Kết quả thực tế | Kết quả thực tế khi chạy thử |
| Fail Step | Đánh dấu bước lỗi | Bước test case có lỗi |
| Fail & Report Issue | Không đạt và báo cáo lỗi | Fail bước kiểm thử đồng thời nộp lỗi mới |
| Submit Results | Nộp kết quả | Hành động hoàn tất test case |
| Spent Time | Thời gian thực hiện | Thời gian thực tế làm test case |
| Undo Submission | Hủy nộp kết quả | Rút lại test case đã nộp để chỉnh sửa |
| Unclaimed | Hủy nhận | Slot test case bị trả lại hệ thống |
| Closed By TestCycle | Bị đóng bởi chu kỳ kiểm thử | Cycle đóng, test case chưa nộp tự động bị hủy |
| Pending | Chờ duyệt | Trạng thái test case đang chờ TTL review |
| Info Requested | Yêu cầu thông tin | Yêu cầu sửa đổi/bổ sung từ TTL |
| Approved | Đã phê duyệt | Test case được duyệt thành công |
| Rejected | Bị từ chối | Test case bị bác bỏ |
