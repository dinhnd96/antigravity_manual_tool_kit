# Slot là gì? (What is a slot?)

> **Nguồn gốc**: User cung cấp
> **Ngày dịch**: 2026-05-18
> **Chủ đề**: test_cycles

---

## Bản dịch

**Slot là gì?**
Một suất tham gia (slot) là sự đặt chỗ kiểm thử trong một test cycle, đi kèm với các yêu cầu cụ thể, chẳng hạn như vị trí, ngôn ngữ, thiết bị, hệ điều hành, phương thức thanh toán, hoặc một thiết lập cụ thể.
Khi một tester nhận một suất (claims a slot), họ bắt buộc phải hoàn thành việc kiểm thử của mình chính xác theo các yêu cầu được liệt kê cho suất đó.

**Quan trọng**: Luôn xem lại các yêu cầu được hiển thị trong slot trước khi claim nó. Nếu bạn không thể đáp ứng tất cả các yêu cầu đó, đừng claim slot.

Hầu hết các test cycle trên uTest đều sử dụng các slot. Nói một cách đơn giản, một slot hướng dẫn bạn về môi trường và các điều kiện mà bạn phải sử dụng và đáp ứng khi thực hiện kiểm thử trong một cycle hoặc khi thực thi test case nếu slot đó được liên kết với (các) test case.

**Sự khác biệt giữa một slot và một test case**
Một slot xác định các yêu cầu và môi trường cần thiết cho việc kiểm thử.
Một test case là một chuỗi các bước và hướng dẫn mà một tester phải tuân theo để xác minh xem ứng dụng hoặc trang web có hoạt động như mong đợi hay không.

Khi claim một slot, tester phải đáp ứng tất cả các yêu cầu của slot và sử dụng môi trường được chỉ định để hoàn tất việc kiểm thử của họ.

**Ví dụ**:
Nếu một slot yêu cầu:
- Một tester có vị trí tại Mỹ (US)
- sử dụng thiết bị iOS 17
Thì chỉ những tester đáp ứng cả hai điều kiện (vị trí và thiết bị) mới nên claim nó. Quá trình kiểm thử cũng phải được thực hiện nghiêm ngặt trên thiết bị iOS 17.

Tùy thuộc vào cycle, slot có thể bao gồm Kiểm thử thăm dò (Exploratory Testing) hoặc Kiểm thử Test Case (nếu slot được claim có liên kết với một hoặc nhiều test case).

**Có ba loại slot:**
- **Test Case slots (Suất kiểm thử Test Case)**: Các slot này được liên kết với một hoặc nhiều Test Case, nghĩa là nếu bạn claim loại slot này, bạn sẽ được giao một hoặc nhiều Test Case.
  - *Single Test Case linked to a single slot* (Một Test Case duy nhất liên kết với một slot): Các slot này được liên kết với một Test Case, nghĩa là nếu claim loại slot này, bạn sẽ được giao một Test Case duy nhất.
  - *Multiple Test Cases linked to a single slot* (Nhiều Test Case liên kết với một slot): Các slot này được liên kết với nhiều Test Case, nghĩa là nếu claim loại slot này, bạn sẽ được giao toàn bộ các test case liên kết với slot đó, và bạn sẽ phải hoàn thành cũng như nộp (submit) chúng trong thời gian cho phép.

- **Exploratory slots (Suất kiểm thử thăm dò)**: Các suất kiểm thử thăm dò cho phép tester tham gia một test cycle khi không có Test Case slot nào phù hợp để claim. Các slot này không cung cấp test case. Thay vào đó, bạn được yêu cầu chỉ thực hiện kiểm thử thăm dò trong cycle. Bạn có thể dễ dàng phân biệt exploratory slots với test case slots nhờ hai yếu tố:
  - Cột Test Case sẽ hiển thị chữ *Exploratory*.
  - Cột Payout (Thanh toán) sẽ không liệt kê một mức trả cố định. Thay vào đó, nó sẽ hiển thị *Per Bug* (Theo lỗi), nghĩa là bạn sẽ chỉ được trả tiền cho các lỗi mà bạn báo cáo và được phê duyệt (approved).

- **Usability Studies (Nghiên cứu khả dụng)**: Các slot này được sử dụng trong một Usability cycle và cho phép bạn tham gia vào đó.

**Các điểm quan trọng về Slots**
- Slot có số lượng giới hạn và dựa trên nguyên tắc "ai đến trước phục vụ trước" (first come first serve basis).
- Slot thường có các yêu cầu khác nhau như thiết bị cụ thể, vị trí, ngôn ngữ, phương thức thanh toán, v.v.
- Trước khi claim một slot, hãy đảm bảo bạn mở rộng và đọc toàn bộ mô tả của slot, đồng thời đảm bảo rằng bạn đáp ứng các yêu cầu của slot và sử dụng môi trường được chỉ định.
- Không claim một slot nếu bạn không có môi trường phù hợp, và không thêm các môi trường giả mạo chỉ vì mục đích claim một slot.
- Xin nhớ rằng khi bạn claim một slot có test case, toàn bộ các test case trong slot đó phải được hoàn thành đúng hạn.
- Nếu không, ngay cả khi bạn nộp hầu hết các test case nhưng không nộp một trong số chúng, slot của bạn sẽ không được phê duyệt (approved), dẫn đến việc không có test case nào được tính.
- Hãy thoải mái claim một Exploratory slot và thực hiện Kiểm thử thăm dò nếu không có test case slot nào khả dụng.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Slot | Suất tham gia | Vị trí đặt chỗ kiểm thử trong cycle |
| Test cycle | Chu kỳ kiểm thử | Đơn vị dự án trên uTest |
| Claim a Slot | Nhận suất tham gia | Hành động đăng ký tham gia vào một slot |
| Test Case slot | Suất kiểm thử Test Case | Slot được liên kết với một hoặc nhiều test case |
| Exploratory slot | Suất kiểm thử thăm dò | Slot không có test case, chỉ trả tiền theo bug |
| Per Bug | Theo lỗi | Hình thức trả tiền cho từng lỗi được phê duyệt |
| Usability Studies | Nghiên cứu khả dụng | Loại cycle tập trung vào đánh giá trải nghiệm người dùng |
