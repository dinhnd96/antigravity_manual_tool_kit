# Các Bước Kiểm Thử Website Hoặc Ứng Dụng

> **Nguồn gốc**: uTest Academy - How to test a website or an application
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

Hãy cùng thảo luận về cách kiểm thử một website hoặc ứng dụng. Dưới đây là các bước tổng quan bạn nên làm theo. 

### 1. Đọc hướng dẫn (Read the instructions)
Đây là phần **quan trọng nhất**. Bạn phải **luôn đọc phần Tổng quan (Overview)** và hiểu các hướng dẫn trước khi bắt đầu kiểm thử. Việc bỏ qua Overview và không tuân thủ hướng dẫn đúng cách có thể khiến công việc của bạn bị từ chối.

**Tại sao điều này quan trọng?**
- Giúp bạn hiểu sản phẩm đang được kiểm thử
- Giúp bạn hiểu **loại lỗi nào** khách hàng đang tìm kiếm
- Overview thường bao gồm thông tin về cách truy cập trang web/ứng dụng kiểm thử
- Chứa thông tin về các phần **Trong phạm vi (In Scope)** và **Ngoài phạm vi (Out Scope)**
- Overview thường bao gồm **Các lỗi đã biết (Known issues)**. Lỗi đã biết sẽ bị từ chối nếu báo cáo lại
- Cung cấp hướng dẫn báo cáo lỗi
- Bất kỳ thông tin quan trọng bổ sung nào khác

### 2. Hiểu sản phẩm (Understand the product)
Bạn nên nắm được mình đang kiểm thử cái gì và nó hoạt động như thế nào. Điều này giúp bạn hiểu những khu vực và tính năng nào của sản phẩm là quan trọng và nên được kiểm thử trước. Ngoài ra, trong phần Overview, bạn sẽ tìm thấy chi tiết về các **Khu vực trọng tâm (Focus areas)**. Khi đã hiểu sản phẩm, bạn đã sẵn sàng bắt đầu test.

### 3. Sử dụng sản phẩm (Use the product)
Mở trang web hoặc cài đặt ứng dụng và bắt đầu sử dụng. Kiểm thử chính là đánh giá một sản phẩm để tìm xem điều gì hoạt động và điều gì không. Hãy **sử dụng nó như một người dùng thực sự**, kiểm tra tất cả các tính năng (features) và chức năng (functionalities), và các lỗi sẽ bắt đầu xuất hiện. 

> 💡 **Mẹo cho người mới**: Là một tester mới, bạn có thể thấy khó tìm lỗi ban đầu, nhưng đừng mất hy vọng và hãy kiên trì tiếp tục kiểm thử.

### 4. Báo cáo lỗi (Report the bug)
Khi bạn tìm thấy một lỗi (issue), đã đến lúc báo cáo nó. Nhưng trước tiên, hãy **đảm bảo lỗi đó là hợp lệ (valid)**. 
Khi đã tự tin lỗi hợp lệ, hãy:
- Tạo tất cả các **tệp đính kèm (attachments)** được yêu cầu (ảnh chụp màn hình, video, log...)
- Điền đầy đủ chi tiết vào biểu mẫu báo cáo lỗi
- Nộp báo cáo lỗi

### 5. Phản hồi các yêu cầu (Respond to requests)
Công việc của bạn **chưa kết thúc** sau khi báo cáo lỗi. TTL, TE, hoặc khách hàng có thể yêu cầu thêm thông tin. Bạn **phải phản hồi tin nhắn** của họ và cung cấp thông tin được yêu cầu **đúng hạn**.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Overview | Tổng quan | Tài liệu quan trọng nhất cần đọc trước khi test |
| Focus Area | Khu vực trọng tâm | Các khu vực của sản phẩm cần ưu tiên test |
| Attachment | Tệp đính kèm | Ảnh chụp màn hình, video, log đính kèm theo bug |
| Feature / Functionality | Tính năng / Chức năng | Khía cạnh hoạt động của sản phẩm |
| Respond to requests | Phản hồi yêu cầu | Trách nhiệm của tester sau khi nộp bug |
