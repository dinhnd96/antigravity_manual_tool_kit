# Các trường thông tin trong Báo cáo lỗi (Issue Report Information Fields)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Mục tiêu của bài học này là giải thích rõ ràng những thông tin cần đưa vào khi nộp báo cáo lỗi trong một chu kỳ kiểm thử trên uTest. Hãy luôn chắc chắn rằng bạn đã đọc và hiểu rõ tài liệu tổng quan chu kỳ (cycle overview) trước khi nộp lỗi, vì mỗi chu kỳ có thể có những yêu cầu cụ thể riêng.

[Hình: Ví dụ về một báo cáo lỗi chất lượng cao]

### 1. Tiêu đề lỗi (Issue Title)
Tiêu đề lỗi mô tả lỗi (bug) đang được báo cáo. Tiêu đề lỗi phải khớp với định dạng được quy định trong phần tổng quan chu kỳ. Hãy đọc kỹ tài liệu tổng quan trước khi nộp bất kỳ báo cáo lỗi nào.

* **1.1** Viết tiêu đề lỗi tuân thủ theo đúng định dạng được yêu cầu trong tài liệu tổng quan chu kỳ.
* **1.2** Mô tả chính xác phân khu/khu vực phát hiện lỗi trong ứng dụng (Ví dụ: Tìm kiếm - Search, Hồ sơ của tôi - My Profile, Thanh toán - Checkout).
* **1.3** Mô tả chính xác lỗi đang được báo cáo (Ví dụ: Ứng dụng bị sập sau khi tải ảnh lên - The app crashes after a photo is uploaded).
* **1.4** Khi tham gia một chu kỳ kiểm thử có trả phí, hãy đối soát kỹ để đảm bảo lỗi của bạn chưa được báo cáo bởi tester khác.
* **1.5** Không viết tiêu đề lỗi bằng chữ IN HOA HOÀN TOÀN.
* **1.6** Không ghi tên trình duyệt vào tiêu đề lỗi (Trừ khi có hướng dẫn cụ thể trong tài liệu tổng quan).
* **1.7** Viết hoa chữ cái đầu tiên ở mỗi dòng trong báo cáo của bạn (bao gồm Tiêu đề, Các bước thực hiện, Kết quả mong đợi và Kết quả thực tế).

### 2. Phân loại lỗi (Issue Classifications)
Chọn chính xác phân loại lỗi để làm rõ loại lỗi đang được báo cáo, tần suất xuất hiện, môi trường kiểm thử được sử dụng và mức độ ảnh hưởng của lỗi đối với người dùng.

* **2.1 Loại lỗi (Issue Type)**: Chức năng (Functional), Giao diện (Visual), Nội dung (Content), Hiệu năng (Performance) hoặc Sập ứng dụng (Crash).
* **2.2 Tần suất (Frequency)**: Mọi lúc (Every time), Hầu như không bao giờ (Hardly ever), Thỉnh thoảng (Occasionally) hoặc Một lần (Once).
* **2.3 Thiết bị và môi trường (Device and environment)**: Chọn chính xác thiết bị và môi trường đã sử dụng để phát hiện lỗi. Đảm bảo chọn đúng thiết bị, trình duyệt, hệ điều hành, v.v., và thông tin này phải khớp với các tệp đính kèm đã tải lên cũng như tên thiết bị trong tiêu đề lỗi. Bạn cũng có thể chọn thêm các môi trường bổ sung nếu lỗi đó tái hiện được trên nhiều môi trường.
* **2.4 Mức độ nghiêm trọng (Severity)**: Nghiêm trọng (Critical), Cao (High), Trung bình (Medium), Thấp (Low).
* **2.5 Nguồn (Source)**: Chọn nguồn chính xác. Chọn **Exploratory** cho các lỗi không liên quan đến các bước của test case, chọn **Structured** cho các lỗi được phát hiện trong quá trình chạy test case.
* **2.6 Thiết bị và môi trường (Web)**: Không chọn *Native (No mobile browser)* khi kiểm thử trang web hoặc khi sử dụng trình duyệt. Thay vào đó, bạn phải chọn đúng thiết bị và trình duyệt bạn đã dùng để phát hiện lỗi.
* **2.7 Thiết bị và môi trường (Mobile apps)**: Không chọn trình duyệt khi kiểm thử một ứng dụng di động gốc (native app). Thay vào đó, bạn phải chọn tùy chọn *Native (No mobile browser)*.

### 3. Các bước thực hiện (Actions Performed)
Mô tả cách tái hiện lỗi bằng cách viết các bước được đánh số trong trường Actions Performed.

* **3.1** Ghi lại toàn bộ các bước cần thiết để hướng dẫn cách tái hiện lỗi.
* **3.2** Sử dụng danh sách được đánh số và chỉ viết một hành động/nhiệm vụ duy nhất trong mỗi bước.
* **3.3** Bắt đầu bước số 1 bằng việc mở URL trang chủ của trang web hoặc mở ứng dụng kiểm thử (bao gồm tên ứng dụng kiểm thử) được nêu trong tài liệu tổng quan.
  * *Ví dụ:* `1. Open the testing website https://www.utest.com` hoặc `1. Open the "Tên ứng dụng kiểm thử tại đây" testing app`.
* **3.4** Không sử dụng các từ như "observe, check, view result, find, see, or pay attention" (quan sát, kiểm tra, xem kết quả, tìm kiếm, nhìn thấy, hoặc chú ý) trong các bước được đánh số.
* **3.5** Không viết kết quả mong đợi hoặc thực tế vào các bước được đánh số.
* **3.6** Không ghi lại URL trong các bước tiếp theo (chỉ ghi ở bước đầu tiên).
* **3.7** Dùng từ **Click** (Nhấp chuột) khi bạn kiểm thử trên máy tính và dùng từ **Tap** (Chạm/Gõ) khi kiểm thử trên thiết bị di động.
* **3.8** Thêm bản dịch tiếng Anh cho tất cả các từ không phải tiếng Anh trong báo cáo khi bạn kiểm thử sản phẩm sử dụng ngôn ngữ khác.

### 4. Kết quả mong đợi (Expected Results)
Mô tả chính xác những gì người dùng mong đợi sẽ xảy ra khi thực hiện các bước được liệt kê trong phần Actions Performed.

### 5. Kết quả thực tế (Actual Results)
Mô tả chính xác những gì thực sự xảy ra khi người dùng thực hiện các bước được liệt kê trong phần Actions Performed.

### 6. Thông báo lỗi (Error Message)
Chỉ điền trường này nếu xuất hiện thông báo lỗi khi tái hiện vấn đề. Hãy ghi lại toàn bộ thông báo lỗi hiển thị trên màn hình.

### 7. Ảnh chụp màn hình (Screenshots)
Đính kèm ảnh chụp màn hình vào mỗi báo cáo lỗi và khoanh vùng làm nổi bật lỗi xuất hiện trên màn hình.

* **7.1** Thêm một ô vuông, hình tròn hoặc mũi tên màu đỏ hoặc vàng để làm nổi bật vị trí lỗi xuất hiện (không sử dụng công cụ vẽ chuột tự do).
* **7.2** Tải lên ảnh dưới định dạng `.jpg` hoặc `.png`.
* **7.3** Chụp toàn bộ màn hình (bao gồm cả thanh URL đối với kiểm thử web).
* **7.4** Xác minh rằng ảnh chụp màn hình có thể mở được trên nền tảng sau khi nộp báo cáo.
* **7.5** Không tải lên quá 2 ảnh chụp màn hình cho mỗi báo cáo lỗi.

### 8. Video
Đính kèm video ghi lại tất cả các bước cần thiết để tái hiện lỗi. Video phải tương ứng hoàn toàn với các bước được liệt kê trong phần Actions Performed.

* **8.1** Tải lên video dưới định dạng `.mp4`.
* **8.2** Video phải tương khớp với các bước được ghi trong phần Actions Performed.
* **8.3** Quay toàn bộ màn hình (bao gồm cả thanh URL đối với kiểm thử web).
* **8.4** Tắt micro để loại bỏ tạp âm nền (Trừ khi có yêu cầu thuyết minh/tường thuật).
* **8.5** Xác minh rằng video có thể phát được bình thường trên nền tảng sau khi nộp báo cáo.
* **8.6** Lỗi đang báo cáo bắt buộc phải xuất hiện rõ ràng trong video.
* **8.7** Không dùng điện thoại di động để quay màn hình máy tính, hãy sử dụng phần mềm quay màn hình.
* **8.8** Không đính kèm quá một video cho mỗi báo cáo lỗi (thể hiện tất cả các bước tái hiện trong 1 video duy nhất).

### 9. Log trên máy tính (Computer Logs)
Đính kèm tệp log console trình duyệt vào mỗi báo cáo lỗi. Hãy đảm bảo tuân thủ các hướng dẫn dưới đây:

* **9.1** Lưu log dưới định dạng `.txt` hoặc `.log` và xác minh rằng tệp log có thể mở được trên nền tảng.
* **9.2** Thu thập log trong quá trình tái hiện lỗi và kiểm tra xem URL kiểm thử có hiển thị trong các dòng dữ liệu của log hay không.
* **9.3** Kích hoạt tính năng "Preserve (or Persist) log" (Giữ lại log) và "Show Timestamps" (Hiển thị mốc thời gian) trên Chrome, Firefox và Edge mới.

### 10. Log trên di động (Mobile Logs)
Đính kèm tệp log thiết bị hoặc log console Android qua Chrome vào mỗi báo cáo lỗi. Hãy đảm bảo tuân thủ các hướng dẫn dưới đây:

* **10.1** Lưu log dưới định dạng `.txt` hoặc `.log` và xác minh rằng tệp log có thể mở được trên nền tảng.
* **10.2** Thu thập log trong quá trình tái hiện lỗi và xác nhận rằng tên ứng dụng kiểm thử/URL kiểm thử có hiển thị trong các dòng dữ liệu của log.
* **10.3** Log trình duyệt di động Android (sử dụng trình duyệt nhân Chromium và Firefox) và log trình duyệt di động iOS (sử dụng Safari - yêu cầu có máy Mac) phải được thu thập khi kiểm thử trang web trên di động.
* **10.4** Bật tính năng “Preserve (or Persist) Log” và “Show Timestamps” trong công cụ nhà phát triển của trình duyệt di động.

### 11. Log Charles Proxy (Charles Proxy Logs)
Đính kèm tệp log Charles Proxy đã được giải mã vào mỗi báo cáo lỗi khi được yêu cầu.

* **11.1** Tất cả dữ liệu trong log Charles Proxy bắt buộc phải được giải mã (chỉ truy cập trang web kiểm thử khi đang thu thập log Charles Proxy để tránh lẫn tạp âm dữ liệu khác).
* **11.2** Chứng chỉ gốc (root certificate) phải được cài đặt chính xác trên máy tính và thiết bị di động (nếu chứng chỉ chưa được cài đặt đúng, các mục mở rộng trong log sẽ hiển thị thông báo `< unknown >`).
* **11.3** Cấu hình các cài đặt SSL được yêu cầu (host `*` và port `443`) - thêm vào hoặc để trống tùy theo hướng dẫn.
* **11.4** Tải lên toàn bộ tệp log Charles Proxy. Sau khi tái hiện lỗi, nhấp vào File, chọn "Save session as".
* **11.5** Xác minh rằng URL trang web kiểm thử hiển thị rõ ràng trong các dòng dữ liệu của log Charles Proxy.
* **11.6** Tải lên log Charles Proxy với phần mở rộng là `.chls` hoặc `.chlz`.
* **11.7** Đảm bảo thu thập log Charles Proxy trực tiếp từ chính thiết bị mà bạn tái hiện lỗi.

### 12. Tùy chọn - Thông tin môi trường bổ sung (Additional Environment Information)
* **12.1** Trường Additional Environment Info có thể chứa thông tin về các thiết bị và môi trường bị ảnh hưởng bởi lỗi này.
* **12.2** Trường này không phải lúc nào cũng bắt buộc, hãy kiểm tra tài liệu tổng quan chu kỳ để xem đây có phải là yêu cầu bắt buộc hay không. Nếu thông tin này không cần thiết, bạn không cần điền.

### Yêu cầu bổ sung thông tin (Information Request) - bước tiếp theo là gì?
Sau khi TTL gửi yêu cầu bổ sung thông tin (information request) cho một báo cáo lỗi, hãy chỉnh sửa các nội dung được yêu cầu và lưu lại các thay đổi. Sau đó, nhấp vào nút **"Confirm all requested info was added"** (Xác nhận tất cả thông tin yêu cầu đã được thêm) để hoàn thành yêu cầu bổ sung thông tin.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Browser Console Log | Log console trình duyệt | Nhật ký ghi lại lỗi JavaScript và mạng trên trình duyệt |
| Decrypted Charles Proxy Log | Log Charles Proxy đã giải mã | Log Charles Proxy đã giải mã HTTPS để hiển thị dạng văn bản rõ |
| SSL Settings | Cấu hình SSL | Cài đặt giao thức bảo mật SSL trong công cụ bắt gói tin |
| Root Certificate | Chứng chỉ gốc | Chứng chỉ bảo mật cao nhất cần cài để giải mã HTTPS |
