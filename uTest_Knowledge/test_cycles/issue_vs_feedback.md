# Khi Nào Một Lỗi Không Phải Là Lỗi? (When is an Issue Not an Issue?)

> **Nguồn gốc**: uTest Academy - When is an Issue Not an Issue?
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### Hoạt động đúng thiết kế? Hay Không được thiết kế như nó nên hoạt động?

Một trong những khía cạnh thách thức nhất đối với các tester mới là hiểu được ranh giới mong manh giữa một **lỗi hợp lệ (valid issue)** và một **phản hồi hữu ích (helpful feedback)**. Ngay cả những tester giàu kinh nghiệm đôi khi cũng gặp khó khăn với sự phân biệt này. Điều mà một developer có thể công nhận là một khiếm khuyết (defect), một người khác lại có thể bác bỏ nó là "WAD" - "hoạt động đúng thiết kế" (works as designed).

Theo nguyên tắc, một lỗi là "thứ gì đó không hoạt động theo đúng thiết kế". Tuy nhiên, nhiều tester mới rơi vào cái bẫy báo cáo "thứ gì đó không được thiết kế theo cách mà nó nên hoạt động". 
- Cái trước là một **khiếm khuyết rõ ràng (clear defect)**.
- Cái sau thường rơi vào lĩnh vực **phản hồi (feedback)**. 

Một bên mô tả một thứ gì đó bị hỏng, trong khi bên kia chỉ ra một thứ gì đó có thể được cải thiện. Thậm chí còn xa hơn một lỗi thực sự là báo cáo "không được thiết kế theo cách tôi thích". Mặc dù ý kiến của bạn có thể có giá trị, nhưng việc hiểu phạm vi (scope) của test cycle sẽ giúp bạn xác định loại ý kiến đóng góp nào là phù hợp.

---

### Các ví dụ thực tế

Hãy xem xét ba vấn đề được tìm thấy trên cùng một trang để hiểu rõ những sự khác biệt này:

#### 🔴 Lỗi rõ ràng: Không hoạt động đúng thiết kế
> Nút quay lại (back button) trên một trang web không hoạt động như mong đợi.

Đây là một lỗi hợp lệ vì chức năng dự định đã bị hỏng. Những phát hiện như vậy thường dẫn đến việc được phê duyệt (approval) và thanh toán (payment).

#### 🟡 Khu vực xám: Thiết kế kém nhưng vẫn hoạt động
> Một công cụ tìm kiếm không hỗ trợ các lỗi đánh máy nhỏ (ví dụ: người dùng tìm "Bryan" nhưng hệ thống không đề xuất kết quả cho 'Bryant').

Mặc dù thiết kế có thể được cải thiện, công cụ tìm kiếm vẫn hoạt động đúng như chức năng cơ bản. Việc này có được phê duyệt hay không phụ thuộc vào việc khách hàng có coi trọng loại phản hồi này trong cycle đó hay không.

#### 🟢 Hoạt động đúng thiết kế (WAD): Không có tác động chức năng
> Gửi một trường tìm kiếm trống sẽ tải lại trang mà không có thông báo lỗi.

Hành vi này phổ biến trên các công cụ tìm kiếm lớn và không làm gián đoạn tương tác của người dùng. Đó là vấn đề "kỳ vọng của người dùng" nhiều hơn là một khiếm khuyết chức năng.

---

### Hiểu các ưu tiên của khách hàng

Mỗi test cycle đi kèm với các hướng dẫn cụ thể nêu rõ những gì khách hàng coi trọng. Luôn điều chỉnh các báo cáo của bạn cho phù hợp với mục tiêu đã nêu. 

**Ví dụ, hãy xem xét yêu cầu sau:**
> *"Vui lòng đảm bảo rằng tất cả các liên kết và chức năng đang hoạt động bằng cách kiểm thử như một người dùng thông thường. Hãy cho chúng tôi biết nếu có bất cứ điều gì cản trở trải nghiệm người dùng."*

Dựa trên hướng dẫn này, hãy phân tích 2 báo cáo của tester:

1. **Nhập quá nhiều ký tự vào biểu mẫu:** Tester phát hiện ra rằng việc nhập hàng trăm ký tự đã làm hỏng trang. Tuy nhiên, phát hiện này không phù hợp với việc "kiểm thử như một người dùng thông thường". Những phát hiện **"kiểm thử tiêu cực" (negative testing)** như vậy thường bị từ chối trừ khi chúng gây ra sự cố nghiêm trọng.
2. **Liên kết điều hướng bị hỏng:** Nếu một liên kết quan trọng như "Back to NBA.com" không hoạt động, nó trực tiếp cản trở trải nghiệm người dùng. Đây là một khiếm khuyết rõ ràng và nên được phê duyệt.

Mặc dù một số cycle khuyến khích tester vượt qua giới hạn và "phá vỡ" sản phẩm, nhưng **hầu hết** đều tập trung vào trải nghiệm người dùng thực tế.

---

### Lỗi "Ngày Xửa Ngày Xưa" (The "Once Upon a Time" Issue)

Đôi khi, một lỗi xuất hiện nhưng **không thể tái hiện một cách nhất quán**. Những lỗi này hiếm khi được ưu tiên trừ khi chúng gây ra lỗi hệ thống nghiêm trọng (critical failure). Nếu bạn gặp sự cố chỉ xảy ra một lần, hãy làm như sau:

1. Xóa bộ nhớ cache của trình duyệt (Clear browser cache).
2. Khởi động lại trình duyệt.
3. Cố gắng tái hiện lại lỗi (Reproduce).

Nếu sự cố vẫn tiếp diễn và có tác động tiêu cực rõ rệt, hãy báo cáo. Nếu không, nó có khả năng bị bác bỏ vì là một sự cố biệt lập.

---

### Những câu hỏi quan trọng cần tự hỏi

Khi không chắc chắn có nên báo cáo hay không, hãy tự hỏi:

1. Có thứ gì đó không hoạt động đúng thiết kế không?
2. Khách hàng có nhấn mạnh đây là khu vực trọng tâm cần test không?
3. Nó có cản trở khả năng sử dụng của người dùng không?
4. Bạn có thể tái hiện lỗi một cách nhất quán không?
5. Nếu chỉ xảy ra một lần, nó có gây ra hậu quả tiêu cực nghiêm trọng không?
6. Nó có làm giảm sự hài lòng của người dùng không?
7. Việc triển khai có khác thường hoặc không nhất quán không?
8. Có cách nào tối ưu hơn để đạt được chức năng này không?
9. *Bạn đang báo cáo dựa trên sở thích cá nhân thay vì một khiếm khuyết chức năng?*

Phát hiện của bạn **càng gần với đầu danh sách**, thì càng có khả năng đó là một lỗi hợp lệ. Những phát hiện **ở gần cuối danh sách** thường rơi vào danh mục Phản hồi (Feedback).

> 💡 **Suy nghĩ cuối cùng:** Bị từ chối (Rejection) không có nghĩa là bạn sai. Nó chỉ có nghĩa là phát hiện của bạn không phù hợp với ưu tiên hiện tại của khách hàng. Hãy tập trung vào những gì quan trọng nhất đối với khách hàng để trở thành một tester giá trị.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Defect / Flaw | Khiếm khuyết / Lỗi | Một lỗi rõ ràng của hệ thống |
| Feedback | Phản hồi / Góp ý | Đề xuất cải thiện, không phải là lỗi chức năng |
| Negative Testing | Kiểm thử tiêu cực | Nhập dữ liệu sai/vượt giới hạn để thử phá hệ thống |
| Clear cache | Xóa bộ nhớ đệm | Bước bắt buộc khi gặp lỗi khó tái hiện |
| Reproduce consistently | Tái hiện nhất quán | Có thể làm lại lỗi đó theo cùng một kịch bản |
