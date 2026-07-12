# Giao Tiếp Trong Test Cycle (Phần 1)

> **Nguồn gốc**: uTest Academy — Communication
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

Khi bạn kiểm thử trong các test cycle trên uTest, đôi khi bạn sẽ có câu hỏi hoặc thắc mắc. Chúng tôi hiểu điều đó, nên chúng tôi cung cấp cho tester nhiều cách dễ dàng và đa dạng để giao tiếp với đội kiểm thử bên trong một test cycle.

Có **4 phương thức giao tiếp chính** trong một test cycle:

1. **Test Cycle Chat** — Chat trong Chu kỳ kiểm thử
2. **uTest Project Chat Channel** — Kênh Chat Dự Án uTest
3. **Tester Messenger** — Tin nhắn Tester
4. **E-mail** — Thư điện tử

---

## Test Cycle Chat (Chat Chu kỳ Kiểm thử)

Test Cycle Chat là **phương thức giao tiếp chính** để tester tìm câu trả lời cho các câu hỏi liên quan đến dự án uTest. Bạn có thể truy cập bằng cách nhấp vào biểu tượng chat trên Thanh Điều Hướng Trên Cùng (Top Navigation Bar) hoặc truy cập trực tiếp tại https://chat.utest.com/

[Hình: Giao diện truy cập Test Cycle Chat từ thanh điều hướng và trang chat.utest.com]

### Những việc NÊN làm trong Cycle Chat

- Chỉ hỏi các câu hỏi **liên quan đến test cycle đó**, ví dụ:
  - Phạm vi test cycle (Test cycle scope)
  - Các bước test case (Test case steps)
  - Vấn đề liên quan đến cycle
  - Các trở ngại (Blockers)
- Duy trì **giọng điệu chuyên nghiệp** (khách hàng có thể đọc được tin nhắn chat)
- **Kiểm tra các tin nhắn trước** để tìm câu trả lời trước khi gửi tin mới
- Đảm bảo sử dụng **chỉ tiếng Anh** để giao tiếp
- Tuân thủ Điều Khoản Sử Dụng (Terms of Use) và Hướng Dẫn (Guidelines) của uTest trước khi gửi tin nhắn

### Những việc KHÔNG NÊN làm trong Cycle Chat

- ❌ Hỏi về thanh toán (payouts)
- ❌ Yêu cầu TTL/TE hoặc khách hàng xem xét hay phê duyệt lỗi của bạn
- ❌ Tranh luận (dispute) về lỗi bị từ chối
- ❌ Thảo luận về các lỗi đã bị từ chối
- ❌ Thô lỗ và thiếu chuyên nghiệp
- ❌ Sử dụng VIẾT HOA TOÀN BỘ để thu hút sự chú ý

> **Lưu ý:** Nếu bạn lo ngại về quyền riêng tư cho câu hỏi hoặc nếu câu hỏi phức tạp, bạn có thể yêu cầu TTL gửi tin nhắn riêng cho bạn. Hoặc, nếu muốn báo cáo lên TE (escalate), hãy xem mục Thông Tin Liên Hệ Nhóm (Team Contact Information) để biết quy tắc leo thang.

---

## Gắn Thẻ Trong Phòng Chat (Tagging)

- Tester và TTL có thể dùng `@testername` trong phòng chat để đề cập ai đó. Chỉ tester hoặc TTL được đề cập mới thấy tên mình được tô sáng và nhận thông báo.
- Tester có thể dùng `@ttl` để đề cập các TTL. Chỉ các TTL được phân công cho cycle đó mới thấy thẻ được tô sáng và nhận thông báo.
- TTL có thể dùng `@all` để đề cập tất cả người dùng. Chỉ những người đã tham gia cycle mới thấy thẻ được tô sáng và nhận thông báo. Cách này hữu ích để thu hút sự chú ý của tất cả mọi người trong phòng chat.

[Hình: Ví dụ về biểu tượng thông báo chat màu đỏ khi được tag]

### Biểu tượng thông báo Chat đỏ khi bị đề cập

Khi `@yourname` (tên bạn) được đề cập trong phòng chat, một con số sẽ hiển thị trong chấm đỏ cho biết bạn đã bị đề cập trong tin nhắn.

---

## Tìm Kiếm (Search)

Chức năng tìm kiếm cho phép tester tìm các tin nhắn cụ thể được gửi bởi người dùng trong phòng chat bằng từ khóa. Thực hiện các bước sau:

1. Mở phòng chat của cycle
2. Nhấp vào ô Tìm kiếm (Search) ở phần header bên cạnh tên cycle
3. Nhập từ hoặc cụm từ bạn muốn tìm, sau đó nhấn Enter hoặc nhấp nút Search
4. Số lượng kết quả sẽ hiển thị nếu có ít nhất 2 kết quả khớp
5. Kết quả khớp sẽ được **tô sáng màu cam** trong Chat để dễ nhận diện
6. Nút **Next/Previous** (Tiếp/Trước) cho phép bạn di chuyển đến kết quả tiếp theo/trước đó
7. Nếu không có kết quả, dòng chữ "No messages found" sẽ hiển thị bên dưới ô tìm kiếm

[Hình: Giao diện tìm kiếm tin nhắn trong phòng chat với kết quả được tô sáng]

> **Lưu ý:** Chỉ các kết quả **khớp chính xác** mới được tô sáng màu cam trong ô tìm kiếm. Các kết quả này có thể cuộn bằng nút next/previous. Các kết quả **khớp một phần** sẽ hiển thị in đậm xuyên suốt phòng chat, nhưng không được tô sáng màu cam.

---

## Tin Nhắn Theo Chuỗi (Threaded Messages)

Tin nhắn theo chuỗi cho phép tester và TTL trả lời trực tiếp vào một tin nhắn đã gửi trong phòng chat. Chi tiết:

1. Bạn có thể trả lời một tin nhắn bằng cách nhấp vào **biểu tượng ba chấm** rồi chọn **Reply** (Trả lời) từ menu
2. Phần chuỗi (thread) sẽ xuất hiện ở **phía bên phải** của phòng chat
3. Nhập câu trả lời vào ô reply, sau đó nhấn Enter hoặc nhấp nút Reply để gửi
4. Liên kết **Reply/Replies** sẽ xuất hiện ngay bên dưới tin nhắn gốc để cho biết có phản hồi
5. Bạn có thể nhấp vào liên kết đó để mở phần chuỗi tương ứng

---

## Biểu Cảm Chat (Chat Reactions)

Tester có thể "phản ứng" với tin nhắn Chat bằng các biểu cảm có sẵn: 👍👎✔ ✖ 👀 +1. Tính năng này giúp đội kiểm thử xác nhận hoặc ghi nhận tin nhắn mà không cần gõ phản hồi đầy đủ, thực hiện khảo sát nhanh, và tránh gửi các tin nhắn trùng lặp.

### Cách sử dụng tính năng Chat Reactions:

1. Trên một tin nhắn trong phòng chat, nhấp vào **ba chấm** ở phía bên phải
2. Chọn một trong các tùy chọn phản ứng: 👍👎✔ ✖ 👀 +1
3. Phản ứng của bạn sẽ hiển thị trong **bong bóng màu xanh**, phản ứng của người khác sẽ hiển thị **màu xám**

[Hình: Giao diện chọn và hiển thị reaction trên tin nhắn chat]

**Quy tắc:**
- Nếu bạn chọn lại reaction từ menu → reaction sẽ bị **xóa**
- Nếu muốn react vào reaction mà tester khác đã thêm → nhấp trực tiếp vào biểu tượng reaction → số đếm tăng thêm 1. Nhấp lại lần nữa để xóa.
- Bạn có thể thấy **số lượng** người đã react, nhưng **không** thấy tên họ. Chỉ TTL, TE, hoặc TSM mới thấy tên và thời gian của từng reaction.

> **Lợi ích chính:** Giảm sự lộn xộn (clutter) trong chat — bạn có thể ghi nhận câu hỏi hoặc thông báo mà không cần lặp lại cùng một câu hỏi hoặc gõ phản hồi đầy đủ.

---

## Tin Nhắn Riêng (Private Message)

Tính năng tin nhắn riêng cho phép TTL và tester giao tiếp riêng tư trong cycle chat. Người dùng đang trực tuyến được hiển thị ở đầu danh sách với biểu tượng nguồn điện màu xanh lá bên cạnh ảnh đại diện.

> **Lưu ý:** Tính năng này chủ yếu được tester sử dụng để **báo cáo lên TTL** (escalate issues).

### Khi nào dùng Private Message

Bạn nên yêu cầu quyền gửi tin nhắn riêng trước. Thực hiện bằng cách gửi tin nhắn cho TTL trong phòng questions/general, và TTL sẽ giúp bạn khởi tạo cuộc trò chuyện.

> **Quan trọng:** Luôn sử dụng phòng chat chung để đặt câu hỏi. Chỉ yêu cầu PM cho các **vấn đề nhạy cảm** không thể thảo luận công khai.

**Ví dụ các trường hợp nhạy cảm:**
- Báo cáo tester khác **vi phạm hành vi**: nộp bug giữ chỗ (placeholder), sao chép bug của tester khác
- Cố ý không đính kèm đầy đủ tài liệu bắt buộc
- Ghi tên mình vào tất cả các ô trong sheet để giữ suất
- Tiết lộ tên khách hàng ra ngoài test cycle
- Các hành vi khác vi phạm Hướng dẫn uTest

### Các bước gửi tin nhắn riêng cho TTL:

1. Mở phòng chat của cycle
2. Dùng thẻ `@TTL` và xin phép gửi tin nhắn riêng
3. Nếu TTL đồng ý, họ sẽ yêu cầu thêm bạn vào danh bạ (contact)
4. Để chấp nhận yêu cầu kết bạn:
   - Mở mục **Contacts** dưới phần Pending Test Cycles
   - Nhấp biểu tượng **dấu tích xanh** bên cạnh tên TTL
5. Chờ cho đến khi TTL khởi tạo cuộc trò chuyện với bạn
6. Để mở tin nhắn riêng do TTL gửi, nhấp tên TTL trong mục Contacts hoặc phần In Room
7. Nhập tin nhắn, nhấn Enter hoặc nhấp nút Send để gửi

> **Lưu ý:** Người nhận cần **đang trực tuyến** (online) thì bạn mới có thể gửi tin nhắn.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Test Cycle Chat | Chat Chu kỳ Kiểm thử | Phương thức giao tiếp chính |
| Tagging / Mention | Gắn thẻ / Đề cập | Dùng @ để tag người |
| Threaded Messages | Tin nhắn theo chuỗi | Reply trực tiếp vào tin nhắn |
| Chat Reactions | Biểu cảm Chat | 👍👎✔ ✖ 👀 +1 |
| Private Message (PM) | Tin nhắn riêng | Chỉ dùng cho vấn đề nhạy cảm |
| Clutter | Sự lộn xộn | Tin nhắn thừa trong chat |
| Escalate | Báo cáo lên / Leo thang | Chuyển vấn đề lên cấp cao hơn |
| Blocker | Trở ngại / Chặn | Vấn đề ngăn cản tiến trình test |
| Contact Request | Yêu cầu kết bạn | Bước bắt buộc trước khi PM |
| Misconduct | Vi phạm hành vi | Hành vi trái quy tắc uTest |
