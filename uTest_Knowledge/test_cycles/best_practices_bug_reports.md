# Các khuyến nghị tốt nhất cho Báo cáo lỗi (Best Practices for Bug Reports)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Luôn tuân thủ "Hướng dẫn báo cáo lỗi" (Issue Reporting Instructions)
Bạn sẽ tìm thấy "Hướng dẫn báo cáo lỗi" trong tài liệu tổng quan chu kỳ (cycle overview). Trước khi báo cáo một lỗi (bug), hãy luôn đọc và đảm bảo tuân thủ nghiêm ngặt hướng dẫn này.

### Luôn tuân thủ quy tắc điền các trường trong báo cáo lỗi
Chúng ta đã thảo luận chi tiết về các quy tắc này trong bài học trước.

### Báo cáo các lỗi hợp lệ
Luôn đảm bảo rằng lỗi bạn đang báo cáo là hợp lệ, đáp ứng tất cả các yêu cầu của chu kỳ kiểm thử và không bị trùng lặp. Bằng cách này, bạn sẽ tránh được việc bị từ chối lỗi (rejections).

### Phản hồi đúng hạn
Khi TTL, TE hoặc khách hàng gửi yêu cầu bổ sung thông tin hoặc yêu cầu bạn sửa nội dung nào đó trong báo cáo lỗi của mình, hãy luôn phản hồi nhanh chóng. Việc không cập nhật báo cáo lỗi kịp thời có thể dẫn đến việc lỗi bị từ chối.

### Nộp báo cáo lỗi chất lượng cao
Luôn cố gắng nộp báo cáo lỗi đạt chất lượng cao. Một báo cáo chất lượng cao nghĩa là báo cáo đó phải chứa đầy đủ mọi thông tin, tất cả các tệp đính kèm theo yêu cầu và không mắc các lỗi ngữ pháp hay lỗi chính tả.

### Tính toàn vẹn của báo cáo lỗi (Bug Report Integrity)
Tính toàn vẹn của báo cáo lỗi (Bug Report Integrity) là một tính năng tùy chọn mà TTL/TE/TSM sử dụng để khen thưởng hoặc cảnh báo các tester dựa trên chất lượng báo cáo lỗi của họ. Có 3 mức độ đánh giá:
* **High Integrity** (Tính toàn vẹn cao)
* **Low Integrity** (Tính toàn vẹn thấp)
* **Unrated** (Không đánh giá) - Đây là tùy chọn mặc định áp dụng cho tất cả các lỗi.

* **High Integrity**: Một báo cáo lỗi chỉ được đánh giá là High Integrity nếu đó là một lỗi cực kỳ có giá trị (very valuable) và/hoặc báo cáo lỗi đó được viết rất tốt, cung cấp đầy đủ thông tin và các tệp đính kèm theo yêu cầu. Đánh giá này sẽ tác động tích cực đến điểm số xếp hạng (tester rating) của bạn.
* **Low Integrity**: Ngược lại với High Integrity, một báo cáo lỗi nhiều khả năng sẽ bị đánh giá là Low Integrity nếu bạn không tuân thủ các hướng dẫn báo cáo lỗi của chu kỳ, viết báo cáo cẩu thả, khiến TTL/TE hoặc khách hàng phải yêu cầu bổ sung thông tin nhiều lần, hoặc nếu bạn phản hồi với thái độ thiếu chuyên nghiệp. Đánh giá này sẽ tác động tiêu cực đến điểm xếp hạng của bạn. Do đó, hãy luôn tuân thủ nghiêm chỉnh các yêu cầu của chu kỳ, cố gắng nộp các báo cáo viết chỉnh chu và phản hồi tin nhắn kịp thời.
* *Lưu ý:* Tất cả các báo cáo lỗi ban đầu đều ở trạng thái mặc định là Unrated (Không đánh giá) trừ khi TTL/TE hoặc TSM quyết định chấm điểm báo cáo đó là High hoặc Low Integrity.

### Không nộp các lỗi giữ chỗ (placeholder bugs)
Khi bạn nộp một báo cáo lỗi, hãy đảm bảo hoàn thiện tất cả các nội dung của báo cáo trước khi nhấn nút Submit (Gửi). Mặc dù bạn có thể chỉnh sửa lại báo cáo sau đó để sửa các lỗi nhỏ, nhưng bạn tuyệt đối không được thực hiện các thay đổi lớn đối với báo cáo lỗi của mình - bao gồm tiêu đề lỗi, các bước thực hiện, kết quả mong đợi và kết quả thực tế.

Một lần nữa, không bao giờ gửi báo cáo lỗi khi thiếu các tệp đính kèm bắt buộc hoặc điền thông tin tạm bợ vào các trường thông tin. Hành vi đó sẽ bị coi là nộp lỗi giữ chỗ. Nộp lỗi giữ chỗ là hành vi vi phạm nghiêm trọng Điều khoản Sử dụng của uTest.

### Duy trì thái độ chuyên nghiệp
Hãy luôn chuyên nghiệp và lịch sự. Mọi khiếu nại (disputes) và tin nhắn trên hệ thống (tester messenger) đều được uTest và khách hàng giám sát chặt chẽ. Do đó, việc duy trì giao tiếp lịch sự và chuyên nghiệp mọi lúc là vô cùng quan trọng.

Dưới đây là các ví dụ so sánh giữa tin nhắn khiếu nại tốt (chuyên nghiệp) và tin nhắn khiếu nại tồi (thiếu lịch sự):

#### Ví dụ tin nhắn khiếu nại tốt:

* **Ví dụ 1:**
  > "Chào TTL, Cảm ơn bạn đã xem xét báo cáo lỗi này. Tuy nhiên, tôi vẫn tin rằng lỗi này hợp lệ và nằm trong phạm vi (in scope) vì [Viết lời giải thích chi tiết của bạn tại đây, hãy giải thích ngắn gọn, rõ ràng]. Tôi đã chỉnh sửa/cải thiện lại các bước thực hiện và tải lên các tệp đính kèm mới để thể hiện rõ hơn lỗi phát sinh. Bạn có thể vui lòng xem xét lại lỗi này giúp tôi không? Xin cảm ơn bạn."
* **Ví dụ 2:**
  > "Gửi TTL, Tôi luôn kiểm tra kỹ lưỡng xem có lỗi nào bị trùng lặp không trước khi nộp báo cáo. Tôi cũng đã kiểm tra lỗi số #....... mà bạn cho trạng thái trùng trước khi báo cáo lỗi này. Tuy nhiên, lý do từ chối hiện chưa rõ ràng đối với tôi, bởi vì [hãy giải thích ngắn gọn, rõ ràng và nêu ra sự khác biệt giữa lỗi của bạn và lỗi được tham chiếu]. Tôi cũng đã thêm một video mới để làm nổi bật sự khác biệt giữa hai báo cáo này. Liệu bạn có thể kiểm tra lại cả hai lỗi và đánh giá lại báo cáo lỗi này giúp tôi không? Trân trọng."

#### Ví dụ tin nhắn khiếu nại tồi (Tuyệt đối KHÔNG sử dụng văn phong này trong cộng đồng):

* **Ví dụ 1:**
  > "Bạn đang đùa tôi đấy à? Tôi không đồng ý với quyết định từ chối này, có ai khác có nhiều kinh nghiệm hơn xem lại lỗi này giúp tôi được không?"
* **Ví dụ 2:**
  > "Thật không hay chút nào. Bạn bị mù à? Lỗi của tôi hoàn toàn khác với lỗi số #..... Kiểm tra lại và duyệt báo cáo lỗi của tôi đi."

Các ví dụ tồi trên thể hiện sự thiếu chuyên nghiệp nghiêm trọng và sẽ khiến bạn gặp rắc rối trên nền tảng uTest.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Bug Report Integrity | Tính toàn vẹn của báo cáo lỗi | Thước đo đánh giá chất lượng của báo cáo lỗi trên uTest |
| High Integrity | Tính toàn vẹn cao | Đánh giá dành cho báo cáo lỗi xuất sắc, giúp tăng điểm xếp hạng |
| Low Integrity | Tính toàn vẹn thấp | Đánh giá dành cho báo cáo lỗi chất lượng kém, gây giảm điểm xếp hạng |
