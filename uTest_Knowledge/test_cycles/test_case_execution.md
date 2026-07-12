# Thực Thi Test Case (Test Case Execution)

> **Nguồn gốc**: uTest Academy - Test Case Execution
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### Giới thiệu

Giai đoạn kiểm thử phần mềm trong vòng đời phát triển phần mềm (SDLC) là một trong những thành phần quan trọng nhất của quy trình quản lý chất lượng. Kiểm thử cần bắt đầu **càng sớm càng tốt** trong quá trình phát triển và tiếp tục cho đến khi triển khai. Lỗi được tìm thấy càng sớm, rủi ro và chi phí mà công ty phải gánh chịu càng thấp.

Việc thực thi test case đúng cách là yếu tố then chốt đảm bảo thành công cho dự án kiểm thử. Do đó, một tester **được đào tạo, am hiểu, có thông tin và tận tâm** sẽ mang lại giá trị và sự xuất sắc vận hành cho sản phẩm của khách hàng.

#### Độ rộng và Độ sâu kiểm thử

| Khái niệm | Tiếng Anh | Mô tả | Ví dụ |
|-----------|-----------|-------|-------|
| **Độ rộng** | Testing Breadth | Phạm vi bao phủ trên toàn ứng dụng | Tính năng mới hoạt động chưa? Quá trình gỡ cài đặt có xóa đúng file? App mobile có đồng bộ với web? |
| **Độ sâu** | Testing Depth | Kiểm thử chi tiết một tính năng cụ thể | Biểu mẫu thanh toán có bị timeout? Nhấn nút Back trên mobile? Nhập mã khuyến mãi sau khi thêm sản phẩm vào giỏ hàng? |

> ⚠️ **Quan trọng**: Mỗi khách hàng sử dụng cách tiếp cận hoặc phương pháp kiểm thử khác nhau, do đó bạn cũng sẽ thấy các loại và phong cách tài liệu test case khác nhau. Tester cần **điền đầy đủ và chính xác** mọi bước của test case theo hướng dẫn.

#### Chuẩn bị trước khi thực thi

- Xem xét tất cả tài liệu liên quan do khách hàng cung cấp
- Hoàn thành các bài hướng dẫn (tutorial) bắt buộc
- Đảm bảo hiểu rõ yêu cầu kiểm thử
- Nắm rõ phạm vi (In Scope) và ngoài phạm vi (Out of Scope) - thường có trong cycle overview, slot instructions, hoặc test case instructions
- Nếu không tìm thấy thông tin cần thiết, liên hệ **TTL hoặc TE** để được làm rõ

---

### Định nghĩa Test Case

Mỗi test case có một loạt các bước giúp khách hàng xác định sản phẩm có hoạt động đúng hay không. Các trường thông tin thường gặp:

| Trường | Tiếng Anh | Mô tả |
|--------|-----------|-------|
| 📝 **Mô tả bước** | Step Description | Giải thích ngắn gọn mục đích - tính năng/hành vi nào đang được xác thực |
| ⚙️ **Điều kiện tiên quyết** | Preconditions | Thiết lập cần thiết trước khi bắt đầu (ví dụ: tài khoản đã tồn tại, app đã mở) |
| 🔢 **Các bước** | Steps | Hướng dẫn từng bước chính xác cần làm |
| ✅ **Kết quả mong đợi** | Expected Result | Điều gì sẽ xảy ra nếu hệ thống hoạt động đúng |
| 📊 **Kết quả thực tế** | Actual Result | Điều gì thực sự xảy ra khi thực thi |
| 🏷️ **Trạng thái** | Status | Pass, Fail, Blocked, Not Executed, Skipped... |
| 💬 **Ghi chú/Nhận xét** | Observations/Comments | Ghi chú, bug liên kết, bằng chứng (ảnh/video) |
| 🔗 **Mã Bug** | Bug ID | Liên kết bug với bước test case (ví dụ: Bug ID #451178) |

> ℹ️ Trên nền tảng uTest, test case bao gồm: **Steps, Expected Results, Status, Comment, và Attachments**.

---

### Cách tiếp cận và Mẹo thực thi Test Case

> 💰 Test case thường đi kèm **đảm bảo thanh toán (guaranteed compensation)**, nên có thể hấp dẫn hơn so với kiểm thử thăm dò (exploratory testing) thuần túy.

Chìa khóa thành công: **Tuân thủ chặt chẽ test case** và làm theo tất cả các bước. TTL, TE và Khách hàng sẽ xem xét tất cả test case và có thể nhận ra kết quả không được hoàn thành một cách trung thực, chính xác và kỹ lưỡng.

#### 1. Điều kiện tiên quyết (Preconditions)
Khi bắt đầu thực thi test case, trước tiên hãy đảm bảo tất cả điều kiện tiên quyết đã được đáp ứng. Nếu không đáp ứng, bạn sẽ **không thể thực thi** test case đúng cách.

#### 2. Hoàn thành các bước theo thứ tự
Các bước test case phải được thực hiện **theo thứ tự** được chỉ định. Mỗi bước thường phụ thuộc vào bước trước đó. Ví dụ: bước 2 yêu cầu bạn thực hiện bước 1 trước.

#### 3. Xác minh (Verification)
Xác minh **từng bước** một cách cẩn thận. Đảm bảo rằng mỗi điểm xác minh (verification point) được kiểm tra đúng theo kết quả mong đợi (expected results).

#### 4. Trạng thái (Status)

| Trạng thái | Khi nào dùng | Hành động tiếp theo |
|-----------|-------------|-------------------|
| ✅ **PASS** | Kết quả thực tế **khớp** với kết quả mong đợi | Chuyển sang bước tiếp theo |
| ❌ **FAIL** | Kết quả thực tế **không khớp** với kết quả mong đợi | Kiểm tra xem bug đã được báo cáo chưa hoặc có phải Known Issue không. Nếu chưa, báo cáo bug. Sau đó tiếp tục các bước tiếp theo. Nếu các bước sau phụ thuộc vào bước bị FAIL mà không có cách giải quyết, hỏi TTL/TE |

#### 5. Nhận xét/Quan sát (Comments/Observations)
Nhận xét rất **thiết yếu** trong test case. Tester có thể ghi lại những hiểu biết (insight) thu thập được khi hoàn thành một bước cụ thể. Thông tin này giúp khách hàng khắc phục sự cố hoặc hiểu rõ hơn về sự nhầm lẫn tiềm ẩn cho người dùng cuối. Nhận xét có thể được cung cấp cho **cả bước PASS và FAIL**.

#### 6. Hoàn thành đầy đủ Test Case
- Đảm bảo **điền tất cả các bước** khi thực thi test case
- Nếu không thể hoàn thành một bước nào đó, liên hệ **TTL hoặc TE** để được hỗ trợ
- **Chú ý kỹ lưỡng** khi thực hiện từng bước

#### 7. Báo cáo Bug/Issue
Khi gặp bug tại một bước FAIL:
1. Cố gắng **tái hiện (reproduce)** và hiểu nguyên nhân gốc (root cause)
2. Kiểm tra xem bug đã được báo cáo chưa trong cycle
3. Kiểm tra danh sách **Known Issues** (nếu có)
4. Khi nộp bug report, bao gồm **hướng dẫn từng bước** để tái hiện dễ dàng, cùng với các tệp đính kèm cần thiết
5. Mỗi bước FAIL nên có một bug được đính kèm. Nhập **Bug ID** vào cột Bug ID

> 💡 **Best practice**: Viết nhận xét và báo cáo như thể người đọc **KHÔNG** quen thuộc với sản phẩm. Điều này đảm bảo bất kỳ ai cũng có thể tái hiện những gì bạn trải nghiệm.

---

### Đặt tên file Test Case

Tester có thể được yêu cầu lưu file test case với thông tin giúp nhận dạng test case và người hoàn thành. Cách đặt tên tốt:

```
[Tên khách hàng/Test case]_[Hệ điều hành]_[Trình duyệt]
```

**Ví dụ:** `uTest_Registration_macOS_Safari`

Nếu nhiều tester cùng tham gia cycle với cùng OS và Browser, thêm **họ của tester** để phân biệt.

---

### Kiểm thử Thăm dò (Exploratory Testing)

Kiểm thử thăm dò có thể được thực hiện **song song** với test case. Tuy nhiên:
- Bạn thường được yêu cầu **hoàn thành test case trước** khi thực hiện kiểm thử thăm dò mở rộng
- Đảm bảo kiểm thử thăm dò có **độ sâu đầy đủ** đối với các khu vực trọng tâm trong phạm vi (In Scope Focus Areas)
- Hoàn thành và nộp test case trước khi tiến hành kiểm thử thăm dò bổ sung

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Test Case Execution | Thực thi Test Case | Quá trình chạy và ghi nhận kết quả |
| Testing Breadth | Độ rộng kiểm thử | Phạm vi bao phủ toàn ứng dụng |
| Testing Depth | Độ sâu kiểm thử | Kiểm thử chi tiết một tính năng |
| Preconditions | Điều kiện tiên quyết | Thiết lập cần thiết trước khi test |
| Expected Result | Kết quả mong đợi | Kết quả đúng theo thiết kế |
| Actual Result | Kết quả thực tế | Kết quả thực sự khi thực thi |
| Verification Point | Điểm xác minh | Tiêu chí để đánh giá PASS/FAIL |
| Root Cause | Nguyên nhân gốc | Nguyên nhân cốt lõi gây ra lỗi |
| Exploratory Testing | Kiểm thử thăm dò | Tự do khám phá ứng dụng để tìm lỗi |
| Guaranteed Compensation | Đảm bảo thanh toán | Test case thường có mức trả cố định |
| Ad hoc Testing | Kiểm thử tùy hứng | Kiểm thử không theo kịch bản chuẩn |
