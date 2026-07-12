# Thuật Ngữ & Vai Trò Chính Trên uTest

> **Nguồn gốc**: uTest Academy – Key Terms & Roles  
> **Ngày dịch**: 2026-05-17  
> **Chủ đề**: test_cycles

---

## Bản dịch

### Khách hàng (Client / Customer)

Công ty đã hợp tác với Applause và Cộng đồng uTest để kiểm thử sản phẩm của họ.

---

### Chu kỳ kiểm thử (Test Cycle)

Một đợt kiểm thử cụ thể cho sản phẩm của công ty. Mỗi chu kỳ kiểm thử bao gồm nhiều tester và có thể khác biệt rất lớn so với các chu kỳ khác tùy thuộc vào cài đặt, loại hình chu kỳ, v.v. Trong chu kỳ kiểm thử, tester phải tuân thủ nghiêm ngặt hướng dẫn trong phần Tổng quan (Overview) của chu kỳ để tìm lỗi trên sản phẩm thuộc phạm vi, thực thi test case, gửi đánh giá (review), hoặc thực hiện nghiên cứu khả dụng (usability study) nếu có.

> **Lưu ý:** Không phải tất cả các chu kỳ kiểm thử đều bao gồm slot, test case, review hoặc khảo sát khả dụng. Điều này khác nhau tùy từng chu kỳ.

---

### Báo cáo lỗi (Bug Report)

Báo cáo lỗi là bản tóm tắt bằng văn bản về một lỗi hoặc khiếm khuyết (bug) cụ thể trong tính năng hoặc chức năng của sản phẩm. Một báo cáo lỗi cần chứa đầy đủ thông tin cần thiết để **hiểu, tái hiện và sửa** lỗi đó.

Để nộp báo cáo lỗi, tester chỉ cần nhấn nút **"Report Issue"** (màu xanh) ở phần đầu chu kỳ kiểm thử. Biểu mẫu báo cáo lỗi chứa nhiều trường mà tester cần điền đầy đủ và đúng theo hướng dẫn báo cáo lỗi của chu kỳ. Bạn sẽ tìm hiểu thêm trong khóa học **Bug Reports**.

---

### Test Case (Trường hợp kiểm thử)

Test Case là một tập hợp các bước được định nghĩa sẵn mà tester phải tuân theo và thực thi để kiểm thử các tính năng và chức năng cụ thể của sản phẩm — ví dụ như kiểm tra một luồng chương trình cụ thể hoặc xác minh sự tuân thủ với một yêu cầu nhất định. Test case chủ yếu được sử dụng trong hai giai đoạn:

- **Trong giai đoạn phát triển**: để đảm bảo tính năng được xây dựng đúng theo thiết kế
- **Định kỳ trong quy trình QA chung**: để đảm bảo mức độ bao phủ kiểm thử mong muốn (test coverage)

Bạn sẽ tìm hiểu thêm trong khóa học **Slots, Test Cases, and Reviews**.

---

### Tester (Kiểm thử viên)

Thành viên của cộng đồng uTest tham gia vào các chu kỳ kiểm thử bằng cách tìm lỗi, cung cấp phản hồi, hoặc thực hiện test case.

---

### Trưởng nhóm kiểm thử — TTL (Test Team Lead)

TTL là **đầu mối liên hệ chính** của tester. TTL hỗ trợ tester trong các chu kỳ kiểm thử và review tất cả báo cáo lỗi cũng như test case đã nộp.

---

### Kỹ sư kiểm thử — TE (Test Engineer)

TE là người xây dựng chu kỳ kiểm thử, tập hợp đội ngũ kiểm thử và chịu trách nhiệm về **toàn bộ quá trình thực thi** của chu kỳ kiểm thử.

---

### Quản lý Dịch vụ Kiểm thử — TSM (Testing Service Manager)

> *Chức danh cũ: Test Architect (TA) — đã được thay thế bằng TSM.*

TSM làm việc trực tiếp với khách hàng (client). Họ quản lý một đội ngũ gồm các TTL và TE để xác định và cung cấp giải pháp phù hợp cho nhu cầu kiểm thử, phản hồi hoặc nghiên cứu của khách hàng.

---

### Quản lý Cộng đồng — CM (Community Manager)

Quản lý Cộng đồng là thành viên của **Đội Quản lý Cộng đồng (CM Team)**. Mục tiêu của đội là giúp cộng đồng toàn cầu:

- **Học cách trở thành tester xuất sắc**
- **Nhận cơ hội tham gia dự án trả phí**
- **Kết nối với các tester đồng nghiệp** trên khắp cộng đồng và toàn cầu

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Client / Customer | Khách hàng | Công ty thuê Applause/uTest kiểm thử |
| Test Cycle | Chu kỳ kiểm thử | Đơn vị công việc chính trên uTest |
| Bug Report | Báo cáo lỗi | Phải đầy đủ để hiểu, tái hiện, sửa lỗi |
| Test Case | Trường hợp kiểm thử | Bước kiểm thử được định nghĩa sẵn |
| Tester | Kiểm thử viên / Tester | Thành viên cộng đồng uTest |
| Test Team Lead (TTL) | Trưởng nhóm kiểm thử | Đầu mối chính, review bug & test case |
| Test Engineer (TE) | Kỹ sư kiểm thử | Xây dựng cycle, tập hợp team |
| Testing Service Manager (TSM) | Quản lý Dịch vụ Kiểm thử | Thay thế chức danh Test Architect (TA) |
| Community Manager (CM) | Quản lý Cộng đồng | Hỗ trợ tester học hỏi và kết nối |
| Test Coverage | Độ bao phủ kiểm thử | Phạm vi đã được test case bao phủ |
| Usability Study | Nghiên cứu khả dụng | Loại test cycle đặc biệt |
| Report Issue | Báo cáo vấn đề / Nộp lỗi | Nút chính để nộp bug report |
| Slot | Suất tham gia | Vị trí được phân bổ trong test cycle |
| Review | Đánh giá / Xem xét | Kết quả review của TTL |
| In Scope | Trong phạm vi | Khu vực sản phẩm được phép test |
