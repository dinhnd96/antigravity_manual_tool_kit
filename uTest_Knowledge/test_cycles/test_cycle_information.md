# Thông Tin Test Cycle (Test Cycle Information)

> **Nguồn gốc**: uTest Academy — Test Cycle Information
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

Khi bạn chấp nhận (accept) một test cycle, bạn có thể truy cập toàn bộ thông tin liên quan đến cycle đó. uTest tổ chức tất cả thông tin thành **nhiều tab**. Hãy cùng tìm hiểu từng tab.

---

### 1. Overview (Tổng quan)

Chúng ta đã thảo luận về tab Overview trước đó. Tab này chứa **toàn bộ thông tin** liên quan đến test cycle, bao gồm các mục sau:

| Mục | Mô tả |
|-----|-------|
| **Description** (Mô tả) | Mô tả ngắn gọn về sản phẩm cần kiểm thử |
| **In Scope** (Trong phạm vi) | Thông tin về thiết bị, môi trường được phép sử dụng; những gì cần test; khách hàng mong đợi gì; và các thông tin quan trọng khác |
| **Out Of Scope** (Ngoài phạm vi) | Thông tin về những gì **không cần** test, những gì khách hàng **không** tìm kiếm |
| **Setup Instructions** (Hướng dẫn cài đặt) | Hướng dẫn cách thiết lập hoặc truy cập sản phẩm cần test |
| **Issue Reporting Instructions** (Hướng dẫn báo cáo lỗi) | Quy cách báo cáo lỗi: format tiêu đề, tệp đính kèm bắt buộc |
| **Test Case Instructions** (Hướng dẫn test case) | Hướng dẫn về test case: thời gian hoàn thành (turnaround time), cách claim |
| **Special Instructions** (Hướng dẫn đặc biệt) | Các hướng dẫn bổ sung quan trọng mà tester **bắt buộc** phải tuân thủ |
| **Attachments** (Tệp đính kèm) | Các tệp đính kèm liên quan đến cycle: bản build sản phẩm, ảnh chụp, video |
| **Team Contact Information** (Thông tin liên hệ nhóm) | Thông tin về TTL, TE, TA của cycle; cách liên hệ; giờ làm việc |
| **Payouts** (Thanh toán) | Mức trả cho Test Case, Bug, và Tester Review |
| **Specified Environment** (Môi trường chỉ định) | Thông tin về môi trường bạn có thể sử dụng trong cycle cụ thể |
| **Special Requirements** (Yêu cầu đặc biệt) | Yêu cầu đặc biệt của cycle — bạn **phải đáp ứng** để được tham gia |
| **Bonus Instructions** (Hướng dẫn thưởng) | Thông tin về yêu cầu nhận thưởng và cách đạt được |

> **Lưu ý:** Một số mục có thể không hiển thị, tùy thuộc vào cài đặt cycle, loại cycle, v.v.

---

### 2. Slots (Suất tham gia)

Tab này chứa tất cả các **suất tham gia** (slot) có sẵn cho cycle. Slot **đảm bảo cho bạn một vị trí** trong nhóm kiểm thử.

Bạn có thể **claim** (nhận) hoặc **unclaim** (bỏ) slot từ đây.

> ⚠️ Luôn nhớ **đọc kỹ mô tả slot** và đảm bảo bạn đã **đáp ứng tất cả yêu cầu** của slot trước khi claim.

*(Sẽ thảo luận chi tiết hơn về slot trong các khóa học tiếp theo.)*

---

### 3. Announcements (Thông báo)

Announcements là các **thông điệp quan trọng** được TTL, TE hoặc TSM gửi đến cả tester đã chấp nhận lẫn tester được mời tham gia cycle.

- Tester **bắt buộc phải đọc hiểu** và **tuân thủ** nội dung thông báo
- **Bỏ qua thông báo** có thể dẫn đến việc **công việc bị từ chối** (rejected)
- Một số thông báo yêu cầu **xác nhận** (Acknowledge) — nếu không xác nhận, bạn **không thể tiếp tục test**
- Nhấn nút **"Acknowledge"** trên thông báo để xác nhận

---

### 4. Builds (Phiên bản)

Chứa thông tin về **phiên bản** (version) và **các thay đổi mới** của bản build sản phẩm đang được kiểm thử.

---

### 5. Issues (Lỗi)

Tab Issues hiển thị **danh sách các bug** đã được báo cáo trong cycle.

- Tester có thể **tìm kiếm, sắp xếp và lọc** lỗi từ trang này
- Một số cycle có thể chứa **Known Issues** (lỗi đã biết) — được đánh dấu bằng **biểu tượng bookmark màu xanh dương** 🔖

---

### 6. Test Cases (Trường hợp kiểm thử)

Tab Test Cases chứa các test case **có sẵn** và **đã được claim**.

- Tester có thể mở từng test case và hoàn thành từ trang này
- Hỗ trợ **tìm kiếm, sắp xếp và lọc** test case

---

### 7. Reviews (Đánh giá)

Biểu mẫu đánh giá để bạn nộp bài. Tùy thuộc vào test cycle, tab này **có thể có hoặc không**.

---

### 8. My Earnings (Thu nhập của tôi)

Hiển thị thông tin về **thu nhập** của bạn trong test cycle đó.

---

### 9. Tester Scorecard (Bảng điểm Tester)

Chứa bảng điểm hiển thị các tester tham gia cycle, **xếp hạng theo thứ tự**.

- Thứ hạng được tính dựa trên **tổng điểm** mà tester nhận được từ công việc của mình

---

### 10. Cycle Feedback (Phản hồi Cycle)

Từ đây tester có thể **gửi phản hồi** về test cycle:

- Khảo sát gồm **5 câu hỏi đánh giá theo thang điểm**
- Một **ô bình luận mở** để bổ sung thông tin
- Tính năng này giúp tester **chia sẻ quan điểm** và cung cấp cho TSM cái nhìn có giá trị về cách cycle được thiết lập và vận hành
- Khảo sát cũng có trên **uTest Mobile App**

> **Lưu ý:** Chỉ có TSM mới có quyền truy cập các báo cáo phản hồi.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Announcement | Thông báo | Tin nhắn quan trọng từ TTL/TE/TSM |
| Acknowledge | Xác nhận | Nút bắt buộc nhấn trên một số thông báo |
| Build | Phiên bản (bản build) | Version sản phẩm đang test |
| Cycle Feedback | Phản hồi Cycle | Khảo sát 5 câu hỏi cuối cycle |
| Known Issues | Lỗi đã biết | Đánh dấu bookmark xanh trong tab Issues |
| My Earnings | Thu nhập của tôi | Tab xem thu nhập trong cycle |
| Slot | Suất tham gia | Đảm bảo vị trí trong nhóm test |
| Tester Scorecard | Bảng điểm Tester | Xếp hạng theo tổng điểm |
| Turnaround Time | Thời gian hoàn thành | Thời hạn để finish test case |
| Unclaim | Bỏ suất | Hủy claim slot đã nhận |
