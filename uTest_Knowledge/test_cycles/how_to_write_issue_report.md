# Cách viết Báo cáo lỗi (How to Write an Issue Report)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

[Hình: Video hướng dẫn cách viết báo cáo lỗi chất lượng cao theo từng bước]

Video trên sẽ hướng dẫn bạn cách viết một báo cáo lỗi (issue report) chất lượng cao theo từng bước. Dưới đây là các bước cơ bản mà một tester cần tuân theo:

1. Đầu tiên, tìm lỗi (bug) trên sản phẩm đang được kiểm thử và đảm bảo đó là lỗi hợp lệ.
2. Nhấp vào nút **Report Issue** (Báo cáo lỗi) trên thanh tiêu đề của chu kỳ kiểm thử.
3. Điền chính xác tất cả các trường thông tin trong biểu mẫu báo cáo lỗi.
4. Tải lên tất cả các tệp đính kèm được yêu cầu.
5. Sau khi hoàn tất, kiểm tra lại tất cả các trường thông tin và tệp đính kèm để đảm bảo chúng hoàn toàn chính xác theo lỗi đã phát hiện.
6. Nhấp vào nút **Submit Issue** (Gửi lỗi) để nộp báo cáo.
7. Cuối cùng, hãy kiểm tra lại các tệp đính kèm đã tải lên để đảm bảo chúng có thể mở được bình thường.

Việc báo cáo lỗi sẽ trở nên dễ dàng và nhanh chóng hơn khi bạn đã quen thuộc với quy trình. Hãy tuân thủ các quy tắc và hướng dẫn dưới đây cho từng trường trong báo cáo lỗi để điền thông tin chính xác.

### Quy tắc điền các trường trong Báo cáo lỗi

#### Tiêu đề lỗi (Issue Title)
* Tiêu đề lỗi phải khớp với định dạng được quy định trong phần tổng quan chu kỳ (cycle overview). Hãy đọc kỹ tài liệu tổng quan trước khi nộp bất kỳ báo cáo lỗi nào.
* Mô tả chính xác phân khu phát hiện lỗi trên ứng dụng hoặc trang web. Ví dụ: Trang chủ (Homepage), Hồ sơ của tôi (My Profile), Giỏ hàng (Cart).
* Mô tả chính xác lỗi đang được báo cáo.
* Không viết tiêu đề lỗi bằng chữ IN HOA HOÀN TOÀN.
* Không ghi tên trình duyệt vào tiêu đề trừ khi có hướng dẫn cụ thể trong tài liệu tổng quan. Lưu ý quy định này có thể thay đổi tùy theo từng chu kỳ kiểm thử khác nhau.
* Luôn viết hoa chữ cái đầu tiên của mỗi câu. Quy tắc này áp dụng cho tất cả các trường thông tin.

#### Phân loại lỗi (Issue Classifications)
* **Loại lỗi (Issue Type)**: Chọn đúng loại lỗi đang được báo cáo, chẳng hạn như Chức năng (Functional), Giao diện (Visual), Nội dung (Content), Hiệu năng (Performance), v.v. Tham khảo lại khóa học *Lỗi phần mềm là gì? (What is a Bug?)* để biết định nghĩa chi tiết của từng loại lỗi.
* **Tần suất (Frequency)**: Chọn mức độ thường xuyên xảy ra lỗi khi bạn thực hiện tái hiện lỗi đó.
* **Mức độ ưu tiên (Priority)**: Chọn mức độ ưu tiên chính xác dựa trên mức độ tác động của lỗi đối với người dùng. Ngoài ra, hãy xem phần tổng quan chu kỳ xem khách hàng có hướng dẫn về các lỗi ưu tiên hoặc tiêu chí ưu tiên cụ thể nào không. Xem khóa học *Mức độ nghiêm trọng so với Giá trị (Severity vs Value)* để hiểu rõ hơn về mức độ ưu tiên của lỗi.
* **Nguồn (Source)**: Chọn xem lỗi báo cáo đến từ kiểm thử thăm dò (Exploratory) hay từ kiểm thử cấu trúc (Structured) trong quá trình thực thi test case.
  * **Exploratory (Thăm dò)**: Chọn tùy chọn này cho những lỗi không liên quan đến các bước của test case và được phát hiện khi bạn tự do kiểm thử.
  * **Structured (Cấu trúc)**: Chọn tùy chọn này cho các lỗi được phát hiện trong quá trình chạy test case. Bạn cũng có thể chọn tùy chọn này nếu lỗi đó liên quan mật thiết đến các bước trong test case, ngay cả khi bạn phát hiện ra nó sau khi đã thực thi xong test case.
  * *Lưu ý:* Nếu bạn sử dụng tính năng **Fail & Report Issue** trực tiếp từ một bước kiểm thử, hệ thống sẽ tự động chọn nguồn là **Structured** và bạn không thể thay đổi nó thành Exploratory. Các báo cáo lỗi được tạo qua tính năng này sẽ tự động liên kết với bước kiểm thử mà bạn đã sử dụng tính năng đó.
  * Ngoài ra, nếu bạn phát hiện lỗi liên quan đến test case sau khi đã nộp test case nhưng trạng thái test case chưa chuyển sang pending/approved/rejected, bạn có thể thực hiện rút lại kết quả (undo submission) và báo cáo lỗi từ bước kiểm thử bằng tính năng **Fail & Report Issue**. Sau khi hoàn tất, hãy nộp lại test case.
* **Môi trường (Environment)**: Chọn môi trường bạn đã tìm thấy và tái hiện lỗi, đồng thời đảm bảo thông tin môi trường khớp với tiêu đề báo cáo.
  * *Lưu ý:* Khi sản phẩm cần kiểm thử là một ứng dụng di động gốc (mobile native app) trên iOS hoặc Android, hãy chắc chắn rằng bạn nhận slot và báo cáo lỗi với môi trường chính xác có chữ **"Native (No mobile browser)"** ở cuối. Tránh chọn các tùy chọn có tên trình duyệt vì bạn không kiểm thử trang web. Tuy nhiên, nếu bạn đang kiểm thử một trang web trên di động, hãy chọn đúng trình duyệt mà bạn phát hiện lỗi.

#### Các bước thực hiện (Actions Performed)
* Cung cấp đầy đủ và chi tiết các bước cần thiết để tái hiện lỗi.
* Sử dụng danh sách được đánh số và liệt kê các bước theo trình tự thời gian.
* Mỗi bước chỉ nên ghi lại một hành động/nhiệm vụ duy nhất.
* Bắt đầu bước số 1 bằng việc mở URL trang web kiểm thử hoặc ứng dụng (bao gồm tên ứng dụng) được ghi trong overview.
* Không viết các từ như sau ở bước cuối cùng:
  * Quan sát (Observe)
  * Kiểm tra (Check)
  * Xem kết quả (View results)
  * Tìm kiếm (Find)
  * Nhìn thấy (See)
  * Chú ý (Pay attention)
* Không ghi kết quả mong đợi hoặc kết quả thực tế như một bước thực hiện.
* Không ghi lại URL trong các bước tiếp theo (chỉ ghi ở bước đầu tiên) trừ khi có yêu cầu đặc biệt.
* Điền bản dịch tiếng Anh trong dấu ngoặc đơn `(English translation)` cho tất cả các từ không phải tiếng Anh khi bạn kiểm thử sản phẩm sử dụng ngôn ngữ khác.
* Sử dụng phần điều kiện tiên quyết để liệt kê các điều kiện cần có trước khi thực hiện bước 1 (Ví dụ: `Điều kiện tiên quyết: Người dùng đã đăng nhập tài khoản`).

#### Kết quả mong đợi (Expected Results)
* Mô tả chính xác những gì người dùng mong đợi sẽ xảy ra sau khi thực hiện các bước được liệt kê trong phần Actions Performed.

#### Kết quả thực tế (Actual Results)
* Mô tả chính xác những gì thực sự xảy ra sau khi thực hiện các bước được liệt kê trong phần Actions Performed.

#### Thông báo lỗi (Error Message)
* Chỉ sử dụng trường này nếu có thông báo lỗi hiển thị trên màn hình sau khi thực hiện các bước. Nếu không có, hãy để trống.
* Ghi lại toàn bộ nội dung thông báo lỗi hiển thị nếu có thể.
* Không điền các từ như "None", "N/A", hoặc dấu gạch ngang "-" khi không có thông báo lỗi.

#### Thông tin môi trường bổ sung (Additional Environment Info)
* Cung cấp thông tin bổ sung về thiết bị và môi trường bị ảnh hưởng bởi lỗi.
* Để trống trường này nếu không có thông tin bổ sung cần cung cấp và không có hướng dẫn yêu cầu điền thông tin này trong overview.

#### Tệp đính kèm (Attachments)

##### Ảnh chụp màn hình (Screenshots)
* Tải lên ảnh chụp màn hình dưới định dạng `.jpg` hoặc `.png`.
* Không sử dụng công cụ vẽ chuột tự do để khoanh vùng vị trí lỗi trên màn hình. Thay vào đó, hãy vẽ các ô vuông, hình tròn màu đỏ hoặc vàng, hoặc sử dụng mũi tên chỉ trực tiếp vào lỗi.
* Khi kiểm thử trang web, ảnh chụp phải hiển thị toàn bộ màn hình, bao gồm cả thanh URL của trình duyệt.
* Đảm bảo ảnh chụp màn hình có thể mở được bình thường và không bị lỗi sau khi gửi báo cáo.
* Không tải lên quá hai ảnh chụp màn hình cho mỗi báo cáo lỗi.
* Không chụp màn hình bằng thiết bị chụp ngoài trừ khi trang web/ứng dụng được bảo vệ chống sao chép bản quyền (DRM-protected) và bắt buộc phải có ảnh chụp, hoặc khi overview yêu cầu rõ ràng.
* Làm mờ hoặc che đi các thông tin cá nhân nhạy cảm (PII) hiển thị trên ảnh chụp màn hình.

##### Video
* Tải lên video dưới định dạng `.mp4`.
* Video phải tương ứng hoàn toàn với các bước được liệt kê trong phần Actions Performed và phải thể hiện rõ ràng lỗi phát sinh.
* Khi kiểm thử trang web, video phải hiển thị toàn bộ màn hình, bao gồm cả thanh URL.
* Không ghi lại âm thanh nền trừ khi có yêu cầu tường thuật (narration).
* Đảm bảo video có thể phát được bình thường sau khi gửi báo cáo lỗi.
* Không tải lên quá một video cho mỗi báo cáo lỗi. Hãy ghi lại toàn bộ các bước tái hiện trong một video duy nhất trừ khi có yêu cầu khác.
* Không quay lại giao diện nền tảng uTest, chu kỳ của khách hàng hoặc các dự án khác trừ khi được yêu cầu.
* Không tải lên các video có dung lượng quá lớn, hãy nén video trước khi tải lên.
* Làm mờ hoặc che đi các thông tin cá nhân nhạy cảm (PII) xuất hiện trong video.

##### Logs (Nhật ký lỗi)
* Tải lên các tệp log theo đúng định dạng được quy định trong tài liệu tổng quan.
* Thu thập tệp log trong quá trình tái hiện lỗi.
* Đảm bảo tệp log có thể mở được và không bị hỏng (corrupted) sau khi gửi báo cáo.
* Tuân thủ tất cả các yêu cầu về log được nêu trong tài liệu tổng quan.

#### Tính hiển thị của tệp đính kèm (Attachment Visibility)
Tính năng hiển thị tệp đính kèm (Attachment Visibility) cho phép tester (người báo cáo lỗi) ẩn các tệp đính kèm của họ đối với các tester khác trong cùng chu kỳ kiểm thử. Đây là tính năng rất hữu ích và quan trọng khi các tài liệu đính kèm chứa thông tin nhạy cảm không nên hiển thị công khai. Tính năng này được quản lý và bật/tắt bởi Kỹ sư kiểm thử (TE) của chu kỳ. Khi được bật, dưới mỗi tệp đính kèm tải lên sẽ hiển thị một nút bật/tắt để bạn ẩn tệp đính kèm đối với các tester khác.

Là một tester, trước tiên bạn cần hiểu rõ tính chất của chu kỳ kiểm thử và các tệp đính kèm cần cung cấp trước khi tải lên:

**Khi tính năng hiển thị tệp đính kèm được BẬT (Enabled):**
* Nếu tệp đính kèm của bạn chứa thông tin nhạy cảm, bạn nên ẩn chúng bằng cách tắt nút **"Visible to testers"** sau khi tải tệp lên.
* Bạn có thể để tệp đính kèm hiển thị với mọi tester trong chu kỳ nếu chúng không chứa bất kỳ thông tin nhạy cảm nào.

**Khi tính năng hiển thị tệp đính kèm bị TẮT (Disabled):**
* Tất cả tệp đính kèm sẽ hiển thị công khai với mọi tester trong chu kỳ và bạn không có tùy chọn để ẩn chúng.

**Lưu ý:**
* Không phải mọi chu kỳ yêu cầu đính kèm tệp đều bật chức năng này. Nó chỉ được thiết kế để bảo vệ các tệp chứa thông tin cá nhân nhạy cảm (PII).
* Tùy chọn ẩn/hiện tệp đính kèm chỉ xuất hiện nếu tính năng này được kích hoạt trong chu kỳ kiểm thử.
* Sau khi tải tệp đính kèm lên báo cáo lỗi, bạn có thể thay đổi trạng thái ẩn/hiện bất kỳ lúc nào.
* Chỉ ẩn các tệp đính kèm thực sự chứa thông tin nhạy cảm.
* Các tệp đính kèm tải lên trong phần Tái hiện lỗi của Cộng đồng (Community Reproductions) không được hỗ trợ tính năng này.
* Các mục lỗi đã biết (Known Issues) và kịch bản kiểm thử BFV sẽ không hiển thị tệp đính kèm nếu báo cáo lỗi gốc đã ẩn tệp đính kèm.
* Các tệp đính kèm bị ẩn vẫn hiển thị đầy đủ đối với TTL, TE, TSM, CM và Khách hàng trong chu kỳ.
* Các TTL của chu kỳ có thể ẩn tệp đính kèm của bạn nhưng không thể chuyển chúng về trạng thái hiển thị lại.
* Khi cần thiết, TE, TSM và CM có thể thay đổi trạng thái của tệp đính kèm từ "Riêng tư" (Private) thành "Hiển thị" (Visible) hoặc ngược lại.

### Các tính năng hữu ích
Ở đầu và cuối biểu mẫu báo cáo lỗi, bạn có thể tìm thấy hai nút: **Configure Template** (Cấu hình biểu mẫu) và **Save as Template** (Lưu làm biểu mẫu). Cả hai nút này đều được sử dụng để tạo biểu mẫu mẫu (template) cho các báo cáo lỗi trong chu kỳ.

#### Lưu làm biểu mẫu (Save as Template)
Nhấp vào nút **Save as Template** sẽ mở ra cửa sổ popup "Issue Report Template" với tất cả các trường thông tin được điền sẵn giống hệt thông tin bạn vừa nhập trong báo cáo lỗi hiện tại chuẩn bị nộp.

Nhấp vào nút **Save Template** để lưu lại. Biểu mẫu báo cáo lỗi tiếp theo của bạn sẽ tự động điền sẵn các thông tin chi tiết chính xác như trong template đã lưu.

#### Cấu hình biểu mẫu (Configure Template)
Nhấp vào nút **Configure Template** sẽ mở biểu mẫu đã lưu trước đó trong cửa sổ popup "Issue Report Template". Bạn có thể chỉnh sửa template này nếu cần thiết. Sau khi chỉnh sửa xong, hãy nhấp vào nút **Save Template** để áp dụng các thay đổi. Lưu ý rằng nếu bạn chưa từng lưu template nào trước đó trong chu kỳ, nút này sẽ hoạt động giống như nút **Save as Template**.

Việc tạo template sẽ rất hữu ích nếu khách hàng yêu cầu định dạng tiêu đề cụ thể với tiền tố chung, hoặc nếu các lỗi có chung điều kiện tiên quyết, chung các bước thao tác ban đầu trước khi lỗi xuất hiện, hoặc khi bạn cần nhập cùng một thông tin cho phần Additional Environment Info hoặc các trường tùy chỉnh, vì chúng sẽ tự động được điền sẵn cho các báo cáo lỗi tiếp theo.

### Lưu ý quan trọng
* Hãy đảm bảo tất cả các trường được điền chính xác và phù hợp với chu kỳ kiểm thử trước khi nộp. Nếu bạn tham gia nhiều dự án, hãy chắc chắn báo cáo lỗi ở đúng chu kỳ để tránh bị từ chối (rejections).
* Tránh nộp các lỗi giữ chỗ (placeholder issues). Bạn bắt buộc phải điền đầy đủ và chính xác tất cả các trường thông tin ngay từ đầu dựa trên lỗi thực tế. Tuyệt đối không điền các ký tự tạm thời như "1. 2. 3." hay "..." vào các trường bắt buộc. Hành vi nộp lỗi giữ chỗ bị nghiêm cấm trên uTest, và việc vi phạm Điều khoản Sử dụng cùng Nguyên tắc uTest có thể dẫn đến việc tài khoản của bạn bị tạm ngưng hoặc chấm dứt vĩnh viễn.
* Không gửi báo cáo lỗi nếu bạn chưa thu thập đủ các tệp đính kèm theo yêu cầu. Tuyệt đối không dùng các tệp đính kèm không liên quan để nộp lỗi nhanh hơn người khác, hành vi này sẽ bị coi là nộp lỗi giữ chỗ và báo cáo lỗi của bạn sẽ bị từ chối.
* Hãy liên hệ với TTL trong chat của chu kỳ nếu bạn thấy hướng dẫn báo cáo lỗi (Issue Reporting Instructions) chưa rõ ràng. Tránh tự ý suy diễn và hãy hỏi ngay nếu có điểm chưa rõ.
* Báo ngay cho TTL trong chat của chu kỳ nếu bạn gặp lỗi không thể tải lên tệp đính kèm hoặc do tệp đính kèm quá dung lượng (kể cả sau khi đã nén, ví dụ như video ghi màn hình).
* Hãy kiểm tra lại danh sách lỗi sau khi nộp để đảm bảo báo cáo của bạn không bị trùng lặp do lỗi hệ thống (nếu trùng, hãy thực hiện hủy bỏ - discard các bản trùng lặp ngay lập tức).
* Vui lòng kiểm tra kỹ các tệp đính kèm khi hủy bỏ báo cáo lỗi để tránh nhầm lẫn, hãy đảm bảo giữ lại báo cáo có đầy đủ tệp đính kèm chính xác.
* Kiểm tra danh sách lỗi để tránh trùng lặp với tester khác. Nếu tester khác đã nộp lỗi đó trước bạn, hãy chủ động hủy (discard) báo cáo của mình để tránh bị từ chối.
* Tuyệt đối không sao chép báo cáo lỗi của tester khác. Hãy tự viết báo cáo lỗi của riêng mình dựa trên đúng lỗi thực tế bạn phát hiện.
* Không chỉnh sửa báo cáo lỗi đã nộp sang một lỗi hoàn toàn khác, vì hành vi này vi phạm Điều khoản Sử dụng và Nguyên tắc của uTest. Nếu lỗi của bạn không còn đúng hoặc bạn nhận ra đó không phải là lỗi hợp lệ, hãy chủ động hủy bỏ (discard) nó thay vì sửa thành một lỗi khác.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Attachment Visibility | Tính hiển thị của tệp đính kèm | Tính năng ẩn/hiện tệp đính kèm với các tester khác |
| Save as Template | Lưu làm biểu mẫu | Lưu báo cáo hiện tại làm mẫu cho các lần sau |
| Configure Template | Cấu hình biểu mẫu | Chỉnh sửa biểu mẫu báo cáo đã lưu trước đó |
