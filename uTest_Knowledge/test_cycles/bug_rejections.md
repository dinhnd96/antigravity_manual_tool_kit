# Từ chối lỗi (Bug Rejections)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Khi một lỗi bị từ chối
Khi một lỗi (bug) nộp lên không đáp ứng các yêu cầu của chu kỳ kiểm thử, nó được coi là lỗi không hợp lệ và do đó sẽ bị từ chối (rejected) bởi TTL, TE hoặc khách hàng.

Mỗi lỗi bị từ chối sẽ đi kèm với một lý do từ chối rõ ràng. Việc bị từ chối lỗi vì bất kỳ lý do nào khác ngoài lý do Hoạt động đúng thiết kế (WAD) đều sẽ ảnh hưởng tiêu cực đến điểm số xếp hạng (tester rating) của bạn.

### Các lý do từ chối lỗi
* **Working as Designed (WAD) - Hoạt động đúng thiết kế**: Tính năng hoặc giao diện của sản phẩm hoạt động đúng như mong đợi của nhà phát triển. Lỗi bị từ chối vì lý do này không ảnh hưởng đến điểm xếp hạng của tester.
* **Duplicate (DUP) - Trùng lặp**: Lỗi đã được báo cáo trước đó bởi tester khác hoặc là một lỗi đã biết (known issue) được liệt kê sẵn.
* **Out of Scope (OOS) - Ngoài phạm vi**: Lỗi được báo cáo nằm trong phần tuyên bố Ngoài phạm vi (Out of Scope) được quy định rõ trong tài liệu tổng quan chu kỳ.
* **Did Not Follow Instructions (DNFI) - Không tuân thủ hướng dẫn**: Lỗi được báo cáo không tuân theo các hướng dẫn được nêu trong tài liệu tổng quan chu kỳ. Loại từ chối này ảnh hưởng tiêu cực gấp đôi (double negative impact) đến điểm xếp hạng của tester.
* **Need more info (INF) - Thiếu thông tin**: Tester không bổ sung thông tin được yêu cầu cho báo cáo lỗi sau khi nhận được yêu cầu bổ sung thông tin (info request).
* **Other - Lý do khác**: Lỗi báo cáo không thuộc các danh mục từ chối ở trên, ví dụ như lỗi đã không còn tái hiện được nữa.

### Khi nào nên khiếu nại quyết định từ chối lỗi?
Việc khiếu nại (dispute) chỉ nên được thực hiện khi thực sự phù hợp. Hãy nhớ rằng việc bị **Từ chối kép (Double Rejection)** (yêu cầu khiếu nại tiếp tục bị từ chối) sẽ ảnh hưởng rất xấu đến điểm xếp hạng tester của bạn.

Hãy luôn đọc và hiểu kỹ lý do từ chối lỗi. Trước khi sử dụng tính năng **Dispute Rejection** (Khiếu nại từ chối), bạn phải tìm hiểu rõ lý do bị từ chối và chỉ tiến hành khiếu nại khi thấy thực sự hợp lý. Bạn có thể khiếu nại lỗi bị từ chối khi:

* Bạn hoàn toàn chắc chắn mình đúng.
* Bạn đã tuân thủ tất cả các hướng dẫn trong chu kỳ kiểm thử.
* Bạn đã sử dụng kênh chat của chu kỳ để làm rõ các hiểu lầm về phạm vi kiểm thử (Tuyệt đối tránh thảo luận trực tiếp về lỗi bị từ chối của mình trong chat chung).
* Bạn đã không cung cấp đủ thông tin trong lần nộp đầu tiên và nay muốn bổ sung thêm bằng chứng để làm rõ.
* Lỗi của bạn bị từ chối do trùng lặp (Duplicate) nhưng bạn muốn giải thích tại sao lỗi của mình khác biệt với lỗi kia.
* Lỗi của bạn có vẻ giống với lỗi của người khác và bị từ chối nhầm do TTL/khách hàng nhầm lẫn. Hãy giải thích tính chất độc bản lỗi của bạn và cung cấp thêm các tệp đính kèm mới để chứng minh.

*Lưu ý:* Bạn chỉ có thể thực hiện khiếu nại khi chu kỳ kiểm thử đang ở trạng thái Hoạt động (Active) hoặc Đã khóa (Locked).

### Khi nào KHÔNG NÊN khiếu nại quyết định từ chối lỗi?
* Nếu đó thực sự là lỗi trùng lặp.
* Nếu lỗi đó nằm ngoài phạm vi (out of scope).
* Nếu lỗi không thể tái hiện được nữa.
* Nếu bạn đã không tuân thủ đúng các hướng dẫn trong chu kỳ kiểm thử.
* Nếu lỗi bị từ chối vì hoạt động đúng thiết kế (work as designed).

### Cách khiếu nại một lỗi bị từ chối
1. Mở báo cáo lỗi bị từ chối của bạn, nhấp vào **Actions**, sau đó chọn **Dispute Rejection**.
2. Bạn sẽ có **duy nhất một cơ hội** để cung cấp thêm thông tin cho khách hàng xem xét lại.
3. Giải thích lý do khiếu nại một cách rõ ràng và tải lên bất kỳ bằng chứng/tệp đính kèm nào cần thiết để chứng minh.
4. Kiểm tra kỹ lại nội dung khiếu nại và bấm gửi.

Dựa trên tình huống thực tế và bằng chứng bạn cung cấp, lỗi của bạn có thể được chấp nhận hoặc tiếp tục bị từ chối lần nữa.

### Lời khuyên dành cho tester mới hoặc khi gặp khách hàng mới:

#### Bạn là một Tester mới?
* Ngay cả những tester có thứ hạng cao đôi khi cũng có lúc là người mới: có thể do thiếu kinh nghiệm kiểm thử cơ bản hoặc kinh nghiệm cụ thể với ứng dụng/trang web đó.
* Hãy cố gắng làm chậm lại thay vì vội vã nộp lỗi. Hãy quan sát xung quanh, học hỏi xem các tester khác báo cáo những gì, và những lỗi nào được phê duyệt hay bị từ chối.
* Xem các nội dung thảo luận trong chat của chu kỳ. Đừng ngần ngại đặt câu hỏi. Thời điểm và không gian thích hợp để yêu cầu làm rõ thông tin là trong chat của chu kỳ trước khi bạn bấm nộp lỗi.

#### Khách hàng mới tham gia nền tảng?
* Ngay cả những uTester giỏi nhất đôi khi cũng gặp phải khách hàng mới. Có thể khách hàng chưa quen với nền tảng uTest hoặc chỉ tìm kiếm một số loại lỗi nhất định nhưng lại quên ghi rõ điều đó trong phần Out of Scope.
* Có thể khách hàng mới quên chia sẻ danh sách lỗi đã biết (known issues) của riêng họ, dẫn đến việc họ từ chối lỗi của bạn vì những lý do không rõ ràng.
* Trong trường hợp này, việc liên hệ với TE (Kỹ sư kiểm thử) quản lý chu kỳ sẽ thích hợp hơn là tranh cãi trực tiếp với khách hàng - những người vừa mới lựa chọn cộng đồng của chúng ta để cải tiến quy trình kiểm thử của họ. Lỗi của bạn có thể không được duyệt, nhưng TTL, TE và TSM sẽ ghi nhận phong cách làm việc chuyên nghiệp của bạn và có thể họ sẽ đền bù xứng đáng cho công sức bạn bỏ ra.

### Lưu ý quan trọng:
* Mọi khiếu nại bắt buộc phải được gửi thông qua tính năng **Dispute Rejection** trên hệ thống.
* Tuyệt đối không yêu cầu khách hàng hoặc TTL không từ chối lỗi của bạn hoặc thương lượng về việc này dưới bất kỳ hình thức nào trong chat. Mọi khiếu nại và thảo luận đều được giám sát chặt chẽ, các tester vi phạm quy tắc này sẽ bị xem xét kỷ luật và có thể bị tạm ngưng tài khoản.
* Mỗi tester chỉ có duy nhất **một lần** khiếu nại cho mỗi lỗi bị từ chối.
* Mỗi tester có giới hạn số lượt khiếu nại tối đa mỗi tháng. Chúng tôi khuyên bạn nên sử dụng tính năng này một cách chọn lọc và hợp lý.

### Best practices khi khiếu nại lỗi
* Trình bày lý do khiếu nại một cách rõ ràng, súc tích.
* Luôn đọc kỹ lý do từ chối và cân nhắc xem việc khiếu nại có thực sự hợp lý hay không.
* Luôn duy trì thái độ làm việc chuyên nghiệp khi khiếu nại lỗi.
* Kiểm tra kỹ phần in scope, out of scope và các hướng dẫn chu kỳ để đảm bảo lỗi của bạn nằm trong phạm vi được cho phép.
* Kiểm tra danh sách lỗi đã biết (Known issues) và danh sách lỗi đã nộp trước đó xem lỗi của bạn có thực sự trùng lặp hay không. Lý do từ chối lỗi phổ biến nhất trên uTest là do lỗi trùng lặp.
* Kiểm tra phần Chat và các thông báo (Announcements) xem lỗi của bạn đã từng được thảo luận hay làm rõ chưa. Có thể TTL/TE đã thông báo với các tester rằng lỗi này nằm ngoài phạm vi.
* Xem xét kỹ lại báo cáo lỗi bị từ chối của bạn: Bạn đã viết mô tả lỗi rõ ràng, ngắn gọn giúp khách hàng dễ dàng tái hiện lại và đi kèm đầy đủ bằng chứng (ảnh chụp màn hình, video, log) chưa? Nếu chưa, bạn có thể hiểu được tại sao lỗi bị từ chối. Vì vậy, hãy chắc chắn bổ sung đầy đủ thông tin và bằng chứng thuyết phục khi bạn thực hiện khiếu nại.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Dispute Rejection | Khiếu nại từ chối | Tính năng cho phép tester khiếu nại quyết định từ chối lỗi |
| Double Rejection | Từ chối kép | Việc khiếu nại thất bại và lỗi bị từ chối lần thứ hai |
