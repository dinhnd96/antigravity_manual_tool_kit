# Các Thực Hành Tốt Nhất cho Slots và Test Cases

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### 1. Hoàn thành test case đúng hạn
- Xem xét kỹ hướng dẫn của cycle và slot trước khi nhận suất (claim a slot).
- Chỉ nhận slot khi bạn đáp ứng đầy đủ các yêu cầu của slot. Các slot được nhận với thiết lập hoặc môi trường không đúng có nguy cơ bị từ chối (rejected) hoặc bị TTL hủy nhận (unclaim).
- Chỉ nhận slot khi bạn có đủ thời gian để hoàn thành. **Không** nhận slot nếu bạn muốn để dành test case cho sau.
- Hoàn thành các test case liên kết trong khoảng thời gian quy định, nếu không, slot sẽ bị hủy nhận và mở lại cho tester khác.
- Hủy nhận slot ngay lập tức nếu có sự cố bất ngờ xảy ra hoặc nếu bạn không thể hoàn thành trong thời gian quy định. Đồng thời, hãy đảm bảo thông báo cho TTL trong chat của cycle.
- Không hoàn thành test case đúng hạn sẽ **ảnh hưởng tiêu cực** đến xếp hạng (rating) của bạn và có thể ảnh hưởng đến các lời mời tham gia cycle trong tương lai. Ví dụ: giữ test case quá lâu rồi hủy nhận trước khi cycle kết thúc, hoặc TTL phải tự hủy nhận slot vì tester không bắt đầu làm việc trong thời gian dài.

### 2. Không để test case ở trạng thái nhàn rỗi
- Bắt đầu thực hiện test case **càng sớm càng tốt**.
- Điều này giúp bạn có thời gian xử lý nếu gặp khó khăn kỹ thuật hoặc cần trao đổi và làm rõ thông tin.
- Trong một số trường hợp, kết quả test case cần được giao cho khách hàng nhanh chóng. Việc trì hoãn thực thi có thể ảnh hưởng đến tiến độ giao hàng và làm giảm sự tin tưởng của khách hàng đối với chúng ta.

### 3. Luôn sử dụng đúng môi trường
- Chỉ nhận slot hoặc test case khi bạn có môi trường phù hợp.
- Chọn đúng môi trường khi nhận slot.
- **Không** nhận slot nếu bạn không có môi trường phù hợp, và **không** thêm các môi trường giả mạo chỉ vì mục đích nhận slot.
- Thực thi test case chỉ trên môi trường được chỉ định.
- Test case sẽ bị **từ chối** nếu bạn thực thi trên môi trường không đúng.

### 4. Thực thi
- Luôn thực hiện **đầy đủ và trung thực** từng bước của test case và cung cấp các tệp đính kèm (attachment) theo yêu cầu.
- Sử dụng bình luận (comment) nếu bạn muốn ghi chú điều gì đó liên quan đến một bước.
- Đảm bảo mỗi bước bị **Fail** đều có một bug được liên kết (associated) với nó.

### 5. Thông tin bổ sung
- Luôn phản hồi các tin nhắn yêu cầu thông tin (info request) **một cách nhanh chóng**.
- **Không** đính kèm các tệp quá lớn — hãy nén chúng trước khi đính kèm.
- Luôn nộp test case sau khi hoàn thành bằng cách nhấp nút **Submit Results** (Nộp kết quả). Các test case chưa được nộp không thể được TTL chuyển sang trạng thái Pending, Approved hoặc Rejected, và chỉ những test case đã được phê duyệt (approved) mới đủ điều kiện được thanh toán (payout).
- Cung cấp thông tin **thời gian đã dành** (time spent) chính xác.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Idle | Nhàn rỗi | Trạng thái test case không được thực thi trong thời gian dài |
| Fake environments | Môi trường giả mạo | Thêm thiết bị/OS không thật để nhận slot — bị cấm |
| Compress | Nén | Giảm dung lượng file trước khi đính kèm |
| Payout | Thanh toán | Chỉ áp dụng cho test case đã được phê duyệt |
| Time spent | Thời gian đã dành | Nhập chính xác khi nộp kết quả test case |
