# Tổng quan về trang Slots (Slots Page Overview)

> **Nguồn gốc**: User cung cấp
> **Ngày dịch**: 2026-05-18
> **Chủ đề**: test_cycles

---

## Bản dịch

**Tổng quan về trang Slots**

Sau khi được mời tham gia một test cycle, trước tiên bạn cần chấp nhận lời mời tham gia cycle trước khi có thể truy cập trang Slots.

1. Đọc tổng quan về cycle (cycle overview).
2. Cuộn xuống dưới cùng và sau đó nhấp vào nút **Accept Cycle & Claim a Slot** (Chấp nhận Chu kỳ & Nhận Suất).
3. Trang slots sau đó sẽ tự động mở ra.

Lưu ý rằng nếu bạn điều hướng đến tab slots trước khi chấp nhận lời mời cycle, bạn sẽ không thể nhận suất (claim a slot). Bạn sẽ cần phải quay lại trang tổng quan cycle, đọc các hướng dẫn và sau đó chấp nhận lời mời cycle để có thể nhận suất.

Nếu bạn đã chấp nhận lời mời cycle, bạn có thể truy cập trang Slots bằng cách nhấp vào tab **Slots** của cycle.

- **Slot Instructions (Hướng dẫn Slot)**: Phần này chứa các hướng dẫn chung về slot cho toàn bộ cycle. Trước khi bạn có thể claim một slot, hãy đảm bảo rằng bạn đã đọc và hiểu các hướng dẫn này.
- **Available Slots (Các suất khả dụng)**: Phần này chứa các slot có thể claim trong cycle.
- **Claimed Slots (Các suất đã nhận)**: Phần này chứa tất cả các slot mà bạn đã claim trong cycle.
- **Unclaimed Slots (Các suất đã hủy)**: Phần này chứa các slot đã bị hủy bỏ mà bạn đã claim trước đó.

Bạn có thể mở rộng (expand) hoặc thu gọn (collapse) các phần Available Slots, Claimed Slots và Unclaimed Slots bằng cách nhấp vào tiêu đề tương ứng của chúng.

Trường **Search** (Tìm kiếm) cho phép bạn lọc một slot theo mô tả.

**Các cột trên bảng slots**
- **Slot Description (Mô tả Slot)**: Chứa thông tin về slot. Nhấp vào mô tả để mở rộng và xem toàn bộ mô tả, cũng như các test case được liên kết với slot.
  - Liên kết **Preview** (Xem trước) cho phép bạn xem trước test case. Hãy sử dụng nó để xác nhận rằng bạn hoàn toàn hiểu các yêu cầu và có thể thực tế hoàn thành nhiệm vụ trong thời gian cho phép trước khi claim nó.
- **Deadline (Hạn chót)**: Hiển thị giới hạn thời gian để hoàn thành và nộp tất cả các test case trong slot.
- **Test Case(s)**: Con số chỉ ra có bao nhiêu test case được liên kết với slot.
  - Các suất kiểm thử thăm dò (Exploratory slots) không có test case liên kết với slot, và nó sẽ chỉ hiển thị “0 Exploratory” trong cột Test Case.
- **Payout (Thanh toán)**: Hiển thị tổng số tiền thanh toán cho tất cả các test case trong slot.
  - Các suất kiểm thử thăm dò không có thanh toán cố định, thay vào đó, tester được trả tiền theo các báo cáo lỗi đã được phê duyệt (approved bug reports) mà họ tìm thấy khi kiểm thử. Phần này sẽ hiển thị dòng chữ “Per Bug” (Theo lỗi) trong cột thanh toán.
- **Effort (Thời gian yêu cầu)**: Hiển thị thời gian yêu cầu để hoàn thành tất cả các test case liên kết với slot.
- **Slots Remaining (Số suất còn lại)**: Cho biết còn bao nhiêu suất trống so với tổng số lượt claim khả dụng cho slot.
- **Waitlist Available (Danh sách chờ khả dụng)**: Hiển thị số lượng chỗ trong danh sách chờ còn trống so với số lượng cho phép đối với các slot đã đạt đến giới hạn claim của chúng.
  - Lưu ý rằng danh sách chờ sẽ chỉ khả dụng nếu tính năng này được kích hoạt (enabled) trong cycle.

**Bảng Claimed Slots (Các suất đã nhận)**
Sau khi claim một slot, phần Claimed Slots sẽ được mở rộng với tất cả các slot mà bạn đã claim, nhấp vào mỗi slot để mở rộng nhằm hiển thị thêm chi tiết.

- Nút **Start Testing** (Bắt đầu Kiểm thử) cho biết bạn chưa thực hiện bất kỳ tiến độ nào trong test case được liên kết. Nhấp vào nút để mở test case hoặc test case đầu tiên trong trường hợp slot được liên kết với nhiều test case.
- Nếu bạn đã bắt đầu làm test case và có tiến độ, nút sẽ thay đổi thành **Resume Testing** (Tiếp tục Kiểm thử), và sẽ mở test case mà bạn đang thực hiện khi được nhấp.
- Nếu các test case đã được hoàn thành và nộp, nút sẽ bị làm mờ (grayed out) và vô hiệu hóa (disabled).
- Cột **Credentials** (Thông tin đăng nhập) hiển thị thông tin đăng nhập cho tài khoản kiểm thử được cung cấp để bạn sử dụng khi test.
  - Nếu không có thông tin đăng nhập nào được cung cấp, trường này sẽ để trống.
- **Environments** (Môi trường) là môi trường được chọn khi claim slot.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Available Slots | Các suất khả dụng | Danh sách các slot có thể nhận trong cycle |
| Claimed Slots | Các suất đã nhận | Danh sách các slot tester đã đăng ký nhận |
| Credentials | Thông tin đăng nhập | Tài khoản được cấp để dùng trong quá trình test |
| Effort | Thời gian yêu cầu / Nỗ lực | Ước tính thời gian cần thiết để hoàn thành các test case |
| Resume Testing | Tiếp tục kiểm thử | Nút để tiếp tục test case đang thực hiện dở |
| Slot Instructions | Hướng dẫn Slot | Yêu cầu chung cho các slot trong cycle |
| Slots Remaining | Số suất còn lại | Số lượng slot trống có thể nhận |
| Start Testing | Bắt đầu kiểm thử | Nút để bắt đầu thực thi test case trong slot |
| Unclaimed Slots | Các suất đã hủy | Danh sách các slot tester đã nhận nhưng sau đó bỏ (unclaim) |
| Waitlist Available | Danh sách chờ khả dụng | Số chỗ trống trong danh sách chờ của slot |
