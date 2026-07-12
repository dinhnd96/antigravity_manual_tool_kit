# Lỗi đã biết (Known Issues)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Lỗi đã biết (Known Issue) là gì?
Lỗi đã biết (Known Issue - KI) là một lỗi hoặc khiếm khuyết phần mềm mà khách hàng đã ghi nhận từ trước, có thể nó đã được báo cáo trong một chu kỳ kiểm thử trước đó hoặc do chính khách hàng phát hiện ra trước khi quá trình kiểm thử bắt đầu.

Tester không được báo cáo lại các Lỗi đã biết trong chu kỳ kiểm thử hiện tại vì khách hàng đã nắm được các vấn đề này. Việc báo cáo lại sẽ bị coi là trùng lặp và dẫn đến việc lỗi của bạn bị từ chối (rejected).

### Kiểm tra các Lỗi đã biết ở đâu?
Các Lỗi đã biết có thể được đưa vào chu kỳ kiểm thử theo ba cách khác nhau:

#### 1. Trong mục Ngoài phạm vi (Out of Scope)
Nếu các lỗi này chưa từng được báo cáo trong các chu kỳ trước nhưng khách hàng đã biết trước một vài lỗi, chúng có thể được liệt kê trực tiếp trong mục **Out of Scope** thuộc tài liệu tổng quan chu kỳ (cycle overview).

#### 2. Trong Bảng lỗi đã biết bên ngoài (External Known Issue Sheet)
If there are many Known Issues that were not reported in previous cycles, they will be added to an external Known Issues file and the file attached to the cycle overview as an attachment or a link to an external Known Issue file will be provided. Also, a point about Known Issues will be added in the Out of Scope section on the cycle overview.
Nếu số lượng Lỗi đã biết quá nhiều và chưa được báo cáo trong các chu kỳ trước, chúng sẽ được tổng hợp vào một tệp danh sách Lỗi đã biết bên ngoài. Tệp này sẽ được đính kèm vào tài liệu tổng quan chu kỳ hoặc được chia sẻ qua một liên kết dẫn đến bảng tính ngoài. Đồng thời, một lưu ý nhắc nhở về Lỗi đã biết cũng sẽ được thêm vào phần Out of Scope trong overview.

#### 3. Trong danh sách Lỗi (Issues list) của chu kỳ
Nếu các Lỗi đã biết đã từng được báo cáo ở các chu kỳ trước đó, chúng sẽ được thêm trực tiếp vào danh sách lỗi của chu kỳ hiện tại trong tab **Issues** (Các lỗi). Khi một Lỗi đã biết xuất hiện trong tab Issues của chu kỳ, nó sẽ có một **cờ màu xanh lam (blue flag)** hiển thị ở phía bên phải tiêu đề lỗi.

### Những điều cần nhớ:
* Luôn đọc kỹ tài liệu tổng quan chu kỳ (cycle overview) trước khi bắt đầu kiểm thử.
* Không phải chu kỳ kiểm thử nào cũng có danh sách Lỗi đã biết, vì vậy hãy đọc kỹ yêu cầu riêng của từng chu kỳ.
* Bắt buộc phải đối chiếu danh sách Lỗi đã biết trước khi nộp bất kỳ báo cáo lỗi nào trong chu kỳ.
* Báo cáo lỗi sẽ bị từ chối nếu bạn nộp trùng lặp với lỗi nằm trong danh sách Lỗi đã biết.
* Liên hệ ngay với TTL của chu kỳ nếu bạn không hiểu rõ mô tả của một Lỗi đã biết.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Known Issue Sheet | Bảng lỗi đã biết | Tài liệu ngoài chứa danh sách các lỗi khách hàng đã biết trước |
| Blue Flag | Cờ màu xanh | Ký hiệu nhận diện lỗi đã biết hiển thị trên giao diện uTest |
