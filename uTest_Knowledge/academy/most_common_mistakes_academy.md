# Các lỗi phổ biến nhất trong các chu kỳ thực hành của Academy

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Dưới đây là danh sách các lỗi phổ biến nhất mà các kiểm thử viên (tester) thường mắc phải trong các chu kỳ kiểm thử của Academy. Nội dung này cũng hướng dẫn những việc tester nên làm để phòng tránh các lỗi đó khi tham gia vào các chu kỳ thực hành của Academy hay các chu kỳ kiểm thử thực tế, đồng thời tránh bị từ chối (rejection) trong các chu kỳ Thử thách Academy (Academy Challenge) do những sai sót trong báo cáo lỗi (bug report).

Khóa học này nhằm mục đích hướng dẫn các tester cách nộp các báo cáo lỗi hợp lệ, không có sai sót, và cách tuân thủ các hướng dẫn của chu kỳ kiểm thử.

### 1. Nhập sai phân vùng xảy ra lỗi trong tiêu đề lỗi (Incorrect area of the issue)
- Kiểm tra tên trang hiển thị trên tab của trình duyệt.
- Kiểm tra đường dẫn vị trí (breadcrumb) nếu có để xác định phân vùng bạn đang đứng.
- Tìm hiểu các trang và thành phần trang web phổ biến.
- Dưới đây là một số ví dụ khác về các phân vùng phổ biến: Đăng nhập (Login), Đăng ký (Register), Hồ sơ hoặc Tài khoản (Profile/Account), Giỏ hàng (Cart), Blog, Thanh toán (Checkout), Trợ giúp (Help), và Cài đặt (Settings).
- Kiểm tra menu điều hướng hoặc các tab để xác định phân vùng hiện tại trong ứng dụng.

### 2. Cung cấp mô tả lỗi sơ sài và mơ hồ trong tiêu đề (Inadequate and vague issue description)
- Giải thích rõ ràng lỗi sao cho người khác có thể hiểu được lỗi chỉ bằng cách đọc mô tả mà không cần phải mở báo cáo chi tiết.
- Khi mô tả lỗi, sự rõ ràng cần được ưu tiên hơn sự ngắn gọn.
- Nếu lỗi liên quan đến một liên kết, video hoặc sản phẩm cụ thể, hãy đề cập rõ tên. Ví dụ: *Một trang lỗi hiển thị sau khi nhấp vào liên kết "T-Shirt" trong phần mô tả sản phẩm*.

### 3. Xác định sai loại lỗi (Misidentifying the type of the issue)
- Tìm hiểu kỹ về các loại bug trên nền tảng.
- Nếu lỗi liên quan hoặc ảnh hưởng trực tiếp đến chức năng của sản phẩm, hãy chọn loại lỗi là **"Functional"** (Chức năng).

### 4. Viết nhiều hơn một hành động trong mỗi bước thực hiện (Actions performed)
- Đảm bảo chỉ viết duy nhất một hành động trong một bước để các bước rõ ràng và dễ làm theo hơn.
- Tốt nhất nên chia các hành động vuốt/cuộn xuống (swipe/scroll down) và chạm/nhấp (tap/click) thành hai bước riêng biệt.
- Để bổ sung thêm thông tin phụ trong một bước, hãy sử dụng dấu ngoặc đơn hoặc ngoặc vuông. Ví dụ: *Mở sản phẩm "Casual Jacket" (sản phẩm nằm ở hàng thứ hai của kết quả tìm kiếm)*.

### 5. Cung cấp URL không hợp lệ trong các bước thực hiện
- Sao chép đúng URL kiểm thử (test URL) được cung cấp trong phần tổng quan chu kỳ (overview).
- Không đặt URL trong bất kỳ ký tự đặc biệt nào (như ngoặc kép, ngoặc đơn, v.v.).

### 6. Không sử dụng điều kiện tiên quyết (Preconditions) trong các bước thực hiện
- Thêm các điều kiện cần thiết để tái hiện lỗi làm điều kiện tiên quyết trước bước 1. Ví dụ:
  - *Điều kiện tiên quyết (Precondition): Người dùng đã đăng nhập.*
  - *1. Mở ứng dụng uTest.*
- Không liệt kê tất cả các bước thao tác thành điều kiện tiên quyết, chỉ sử dụng khi thực sự cần thiết.

### 7. Kết quả thực tế (Actual result) và kết quả mong đợi (Expected result) không rõ ràng
- Cung cấp giải thích rõ ràng và dễ hiểu về những gì mong đợi sẽ xảy ra và những gì thực sự xảy ra sau khi thực hiện các bước tái hiện lỗi.
- Tránh sử dụng cụm từ chung chung như *"Không hoạt động bình thường" (Not working properly)* vì nó không giải thích đầy đủ được vấn đề lỗi.
- Xóa biểu mẫu (template) mặc định có sẵn từ test case (nếu báo lỗi từ một bước test case) và tự viết kết quả bằng cách tuân theo Hướng dẫn Báo cáo lỗi (Issue Reporting Instructions) của chu kỳ kiểm thử.

### 8. Thiếu các tệp đính kèm bắt buộc (Missing required attachments)
- Luôn kiểm tra phần Hướng dẫn Báo cáo lỗi (Issue Reporting Instructions) trước khi báo cáo lỗi.
- Đảm bảo cung cấp đầy đủ các tệp đính kèm bắt buộc trước khi gửi báo cáo lỗi.
- Trong trường hợp nghi ngờ hoặc hướng dẫn không rõ ràng, hãy hỏi TTL trong kênh chat của chu kỳ kiểm thử.
- Việc cố tình cung cấp tệp đính kèm không đầy đủ hoặc không chính xác để báo cáo lỗi nhanh hơn người khác là vi phạm Điều khoản Sử dụng (Terms of Use) của uTest, điều này có thể dẫn đến việc lỗi bị từ chối với lý do DNFI (Không tuân thủ hướng dẫn) và bị loại khỏi chu kỳ hiện tại cũng như các chu kỳ sắp tới.

### 9. Tải lên tệp đính kèm sai định dạng (Wrong format)
- Kiểm tra phần Hướng dẫn Báo cáo lỗi để biết các yêu cầu về định dạng tệp. Tại Academy, các yêu cầu chuẩn như sau:
  - Ảnh chụp màn hình (screenshots) ở định dạng **.jpg** hoặc **.png**.
  - Video quay màn hình (screen recording) ở định dạng **.mp4**.
  - Log bảng điều khiển/thiết bị (console/device logs) ở định dạng **.txt**.
- Nếu bạn nhận thấy mình đã tải lên sai định dạng, hãy sửa lại sớm nhất có thể.
- Luôn kiểm tra lại các tệp đính kèm đã tải lên để phòng trường hợp xảy ra lỗi không mở được tệp.
- Nếu bạn gặp lỗi khi tải tệp lên, hãy thử sử dụng một trình duyệt khác và xóa bộ nhớ đệm (cache) cùng cookie.

### 10. Video quay màn hình không bắt đầu từ trang chủ hoặc không khớp với các bước thực hiện
- Đọc kỹ hướng dẫn về quay màn hình trong phần Hướng dẫn Báo cáo lỗi.
- Nếu yêu cầu hiển thị toàn bộ các bước tái hiện, hãy bắt đầu ghi hình từ trang chủ (homepage) và đảm bảo khớp với các bước thực hiện thực tế.
- Tránh thực hiện các bước không cần thiết trong quá trình quay màn hình.
- **Không hiển thị nền tảng uTest trong video quay** để tránh vi phạm quy định GDPR, vì nó có thể chứa thông tin nhận dạng cá nhân (PII).
- Không hiển thị các dự án hoặc sản phẩm khác không liên quan đến phạm vi kiểm thử của chu kỳ bạn đang làm việc.
- Đảm bảo micro được tắt tiếng để loại bộ tiếng ồn xung quanh (trừ khi bạn cần thực hiện thuyết minh/tường thuật).

---

### Chu kỳ thực hành Thử thách Academy (Academy Challenge)
Có một số khuyến nghị và mẹo khác có thể giúp bạn tránh bị từ chối trong các chu kỳ thử thách Academy do các sai sót trong báo cáo lỗi (Lưu ý: Trong các chu kỳ Thử thách Academy, các báo cáo lỗi có sai sót sẽ bị từ chối thẳng):

- **Các bước thực hiện (Action Performed)**: Đảm bảo số thứ tự các bước được ghi chính xác và liên tục theo đúng thứ tự.
- **Nguồn (Source)**: Hãy báo cáo lỗi từ test case nếu lỗi đó liên quan đến các bước của test case và chọn **"Structured"** (Có cấu trúc) cho tùy chọn nguồn trong trường hợp bạn không báo cáo qua luồng thực thi test case.
- **Log mạng (Logs)**: Chỉ tải lên log Charles khi có yêu cầu. Tránh tải lên khi không thực sự cần thiết.
- **Cách lấy log**: Bắt đầu thu thập log trong quá trình tái hiện lỗi và đảm bảo bắt đầu từ trang chủ.
- **Trường tùy chỉnh (Custom Fields)**: Điền thông tin vào các trường tùy chỉnh theo đúng hướng dẫn và tuân thủ bất kỳ định dạng quy định nào.
- **Lỗi trùng lặp và Lỗi đã biết (Duplicates & Known issues)**: Luôn kiểm tra các lỗi đã được báo cáo và các lỗi đã biết để tránh trùng lặp, đồng thời kiểm tra xem có tệp lỗi đã biết (known issues file) nào đính kèm trong chu kỳ kiểm thử hay không.
- **Định nghĩa trùng lặp**: Lưu ý rằng các lỗi có cùng một nguyên nhân gốc (root cause) sẽ bị coi là trùng lặp. Ví dụ: kết quả hiển thị không chính xác sau khi tìm kiếm một từ khóa sẽ được coi là cùng một lỗi ngay cả khi hiện tượng xảy ra với các từ khóa khác nhau.
- **Ngoài phạm vi (Out Of Scope)**: Xem xét kỹ lưỡng phần OOS. Mỗi chu kỳ kiểm thử có các yêu cầu riêng biệt, vì vậy tốt nhất bạn nên kiểm tra kỹ trước khi bắt đầu kiểm thử.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Academy Challenge | Thử thách Academy | Chu kỳ kiểm thử cuối cùng để tốt nghiệp uTest Academy |
| Practice Cycle | Chu kỳ thực hành | Chu kỳ kiểm thử phục vụ học tập tại uTest Academy |
| Screen Recording | Video quay màn hình | Bằng chứng dạng video ghi lại quá trình kiểm thử |
| Custom Field | Trường tùy chỉnh | Các trường thông tin bổ sung cần điền theo yêu cầu riêng của từng cycle |
| Breadcrumb | Đường dẫn vị trí | Hiển thị vị trí người dùng trên website |
| Out Of Scope (OOS) | Ngoài phạm vi | Các khu vực bị cấm test trong cycle |
| Actual Result | Kết quả thực tế | Kết quả thực sự khi thực thi test case |
| Expected Result | Kết quả mong đợi | Kết quả mong muốn xảy ra theo đặc tả |
| Precondition | Điều kiện tiên quyết | Thiết lập cần thiết trước khi thực hiện các bước kiểm thử |
| Actions Performed | Các bước thực hiện | Các bước thao tác của tester để tái hiện lỗi |
