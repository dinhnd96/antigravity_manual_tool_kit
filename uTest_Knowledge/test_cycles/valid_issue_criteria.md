# Lỗi Hợp Lệ Là Gì? (What is a valid issue?)

> **Nguồn gốc**: uTest Academy - What is a valid issue?
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### Lỗi hợp lệ là gì?

Chỉ những lỗi đáp ứng **tất cả** các yêu cầu của test cycle mới được coi là hợp lệ. Do đó, không phải mọi lỗi bạn phát hiện trong khi kiểm thử đều hợp lệ; bạn phải xem xét các yêu cầu và **chỉ báo cáo các lỗi hợp lệ**.

---

### Làm thế nào để đảm bảo một lỗi là hợp lệ?

Hãy xem các yếu tố xác định một lỗi có hợp lệ hay không:

#### 1. Hoạt động đúng thiết kế (Working as Designed - WAD)
Bạn có thể nghĩ rằng mình đã tìm thấy một lỗi, nhưng thực tế, đó không phải là lỗi mà đơn giản là cách hệ thống hoạt động - đây là những lỗi **không hợp lệ**. Tại uTest, chúng tôi phân loại những lỗi như vậy là **Working as Designed (WAD)**.

Hiểu rõ sản phẩm trước tiên sẽ giúp bạn tránh những lỗi như vậy. Tuy nhiên, đừng quá lo lắng về WAD, vì việc bị từ chối do lý do này **không có bất kỳ ảnh hưởng nào đến xếp hạng của bạn**. Đôi khi, WAD có thể gây nhầm lẫn, ngay cả với những tester có kinh nghiệm. Hãy sử dụng khả năng phán đoán tốt nhất của bạn.

**Ví dụ:**
- **Ví dụ 1:** Bạn đang kiểm thử một website và không thấy nút đăng xuất. Theo hướng dẫn, nút đăng xuất phải có trên trang chủ nên bạn đã báo cáo. Nhưng nút đăng xuất bị ẩn bên trong một menu thả xuống (dropdown menu) mà bạn không kiểm tra. Vậy đây là WAD. Phản hồi để nút đăng xuất dễ tìm hơn là một ý kiến hay, nhưng nó không phải là lỗi vì dev cố tình thiết kế như vậy.
- **Ví dụ 2:** Bạn sắp xếp giá từ thấp đến cao trên một website mua sắm. Sản phẩm có giá gốc và giá giảm, và website sắp xếp theo giá gốc. Lỗi sắp xếp bạn báo cáo là không hợp lệ vì tính năng đang hoạt động đúng thiết kế.

#### 2. Khu vực ngoài phạm vi (Out of Scope areas)
Lỗi bạn báo cáo phải nằm **trong phạm vi (In Scope)** của test cycle. Mỗi cycle đều có chi tiết về các khu vực trong và ngoài phạm vi (Out of Scope) trong phần Tổng quan (Overview). Bất kỳ lỗi nào nằm ngoài phạm vi đều **không hợp lệ**.
- **Ví dụ:** Nếu phần "Out of Scope" nêu rõ "Help page" (Trang trợ giúp) nằm ngoài phạm vi, bất kỳ lỗi nào bạn báo cáo trên trang này đều sẽ bị từ chối.

#### 3. Tiêu chí cấm báo cáo (Do not report criteria)
Tùy thuộc vào cycle, có thể có yêu cầu về **loại lỗi** tester được phép báo cáo. Thông tin này cũng nằm trong phần "Out of Scope".
- **Ví dụ:** Nếu phần "Out of Scope" nêu rằng lỗi giao diện (Visual issues) & lỗi bản địa hóa (Localization issues) không thuộc phạm vi, chúng sẽ bị từ chối nếu bạn báo cáo.

#### 4. Trùng lặp (Duplicate)
Mỗi lỗi **chỉ được báo cáo một lần** bởi một tester. Việc báo cáo lại cùng một lỗi sẽ dẫn đến bị từ chối. Luôn kiểm tra các lỗi đã được báo cáo trước khi nộp báo cáo mới.

#### 5. Lỗi đã biết (Known Issues)
Lỗi đã biết là những lỗi mà **khách hàng đã biết**, việc báo cáo lại sẽ bị coi là trùng lặp (Duplicate). Tùy thuộc vào cycle, có thể có hoặc không có danh sách lỗi đã biết. Bạn có thể tìm thấy chúng trong Overview hoặc tab Issues. Nếu cycle có lỗi đã biết, bạn **bắt buộc phải xem xét** trước khi báo cáo lỗi mới.

#### 6. Tuân thủ hướng dẫn (Following Instructions)
Bạn **luôn phải tuân theo hướng dẫn** khi kiểm thử và báo cáo lỗi. Nếu bạn không tuân thủ, dù lỗi có hợp lệ, nó vẫn có thể bị từ chối với lý do **DNFI** (Did Not Follow Instructions - Không tuân thủ hướng dẫn).
- **Ví dụ:** Báo cáo lỗi không rõ ràng, báo cáo lỗi giữ chỗ (placeholder issues), không dùng uTest VPN khi được yêu cầu...

> ⚠️ **Lưu ý**: Đây là những yêu cầu chính để báo cáo một lỗi hợp lệ. Tùy từng cycle, có thể có thêm yêu cầu khác, vì vậy bạn **phải đọc kỹ Overview và làm theo hướng dẫn**.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Valid Issue | Lỗi hợp lệ | Đáp ứng đủ mọi yêu cầu của cycle |
| In Scope | Trong phạm vi | Các khu vực được phép test |
| Out of Scope | Ngoài phạm vi | Các khu vực bị cấm test trong cycle |
| Duplicate | Trùng lặp | Lỗi đã được báo cáo trước đó |
| Known Issues | Lỗi đã biết | Lỗi khách hàng đã biết từ trước |
| DNFI (Did Not Follow Instructions) | Không tuân thủ hướng dẫn | Lý do bị từ chối (reject) lỗi |
| Visual Issue | Lỗi giao diện | Các lỗi về mặt hiển thị UI |
