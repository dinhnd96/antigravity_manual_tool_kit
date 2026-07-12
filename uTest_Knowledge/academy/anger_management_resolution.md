# Quản lý sự giận dữ, Thấu hiểu và Giải quyết vấn đề

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

Chìa khóa để trở thành một kiểm thử viên (tester) giỏi là luôn giữ bình tĩnh và tự chủ. Tuy nhiên, điều này không có nghĩa là bạn không được phép tỏ ra khó chịu khi bị đối xử không công bằng.

Mục tiêu của khóa học này là đưa ra hướng dẫn về cách xử lý các tình huống kích hoạt sự giận dữ của bạn, nhằm tránh các hành vi bộc phát ngoài ý muốn có thể vi phạm Điều khoản Sử dụng (Terms of Use) của uTest, dẫn đến việc tài khoản bị đình chỉ (suspension) hoặc chấm dứt hoạt động (termination). Khi chúng ta có thể biểu đạt cảm xúc của mình mà không mất kiểm soát, các nhu cầu của chúng ta sẽ dễ được đáp ứng hơn và kết quả trong tương lai cũng sẽ được cải thiện hơn.

Một khi đã tham gia vào các chu kỳ kiểm thử (test cycles), với tư cách là một tester, bạn có thể rơi vào nhiều tình huống khác nhau do các yêu cầu khác nhau, gặp gỡ các thành viên nhóm khác nhau hoặc khách hàng mới, v.v. Có thể có lúc bạn đã nỗ lực hết mình nhưng kết quả lại không như mong đợi. Bạn có thể cảm thấy rằng một lỗi đáng lẽ phải bị từ chối do hoạt động đúng thiết kế (WAD) nhưng thay vào đó lại bị từ chối vì lý do Khác (Other), điều này ảnh hưởng tiêu cực đến điểm xếp hạng (rating) của bạn.

Cũng có thể có lúc bạn dành nhiều thời gian để hoàn thành test case nhưng nó lại bị từ chối (rejected) hoặc bị hủy nhận (unclaimed) mà không có lý do rõ ràng. Trong những thời điểm đó, bạn có thể cảm thấy bực bội và muốn mọi thứ được giải quyết càng sớm càng tốt theo kỳ vọng của mình. Chúng tôi hiểu cảm giác đó của bạn vì chúng tôi cũng từng gặp phải những vấn đề tương tự. Trong các tình huống như vậy, hãy bình tĩnh và làm theo các lời khuyên dưới đây.

### 1. Tránh làm bất cứ điều gì khi đang giận dữ
Nếu để sự giận dữ kiểm soát, bạn sẽ có xu hướng muốn hành động ngay lập tức để giải tỏa cảm xúc đó dù bạn có nhận thức được hay không, và hành động đó rất dễ khiến bạn hối hận cũng như làm tổn thương người khác. Nếu bạn nhận ra mình đang ở trong trạng thái này, hãy tránh làm bất cứ điều gì bạn định làm lúc đó. Bạn có thể bỏ tay ra khỏi bàn phím và đứng dậy nếu điều đó giúp bạn dừng lại và cảm thấy dễ chịu hơn.

### 2. Tạm dừng một lát (Take a Timeout)
Thời gian có thể giúp bạn lấy lại bình tĩnh, vì vậy hãy tạm nghỉ ngơi cho đến khi bạn cảm thấy khá hơn. Bạn cũng có thể thử các phương pháp khác giúp hạ hỏa, chẳng hạn như vận động thể chất, hít thở sâu, hoặc rửa mặt để giúp tinh thần sảng khoái và cải thiện tâm trạng.

### 3. Xác định và thấu hiểu vấn đề
Khi bạn đã cảm thấy dễ chịu hơn và đầu óc tỉnh táo hơn, hãy kiểm tra lại để tìm ra nguyên nhân của vấn đề:
- Bạn có tức giận sau khi đọc phản hồi từ TTL hoặc TE không?
- Bạn có không đồng ý với quyết định của TE không?
- Bạn có hiểu lầm hướng dẫn nào đó nhưng lại bực bội sau khi kiểm tra lại không?

Bạn cần loại bỏ những suy nghĩ tiêu cực đổ thêm dầu vào lửa cho sự giận dữ của mình, chỉ khi đó bạn mới có thể nhìn nhận vấn đề một cách bao quát hơn và có được góc nhìn khách quan hơn. Nếu bạn cứ giữ tư tưởng *"Mọi chuyện đáng lẽ phải thế này hoặc bắt buộc phải thế kia"* thì cuộc hội thoại sẽ không đi đến đâu, bởi bạn sẽ rất dễ nổi giận khi thực tế không khớp với kỳ vọng của mình. Hãy học cách thay đổi cách suy nghĩ và tự hỏi bản thân xem những gì mình sắp nói ra có đúng sự thật, có giá trị, có liên quan và có thực sự cần thiết hay không.

Nếu bạn đã sẵn sàng chuyển sang bước tiếp theo, hãy chuẩn bị tinh thần để chấp nhận bất kỳ kết quả nào bất kể những nỗ lực đã bỏ ra, và hãy tin rằng nỗ lực đó sẽ không lãng phí. Bước tiếp theo là cố gắng hiểu thông điệp hoặc quyết định được đưa ra. Điều đầu tiên nên làm là kiểm tra kỹ lưỡng và cẩn thận tài liệu tổng quan chu kỳ (cycle overview), cũng như hướng dẫn test case và slot, hoặc bất kỳ thông tin nào khác đã được cung cấp, rồi đánh giá lại chúng. Bằng cách kiểm tra lại các hướng dẫn, bạn sẽ hiểu rõ hơn về mục tiêu của chu kỳ kiểm thử và có thể nhìn nhận vấn đề từ góc nhìn của người khác.

Sau khi đã hiểu rõ thông điệp hoặc đưa ra quyết định, bạn sẽ dễ dàng đi đến kết luận và tập trung vào công việc của mình hơn. Bạn cũng sẽ hiểu rõ hơn về sở thích/yêu cầu của khách hàng và chuẩn bị tốt hơn cho các dự án trong tương lai. Bạn cũng có thể thấy các điều sau đây là hữu ích để ghi nhớ:
- Mỗi chu kỳ kiểm thử hoặc dự án có thể có các yêu cầu và điều kiện riêng biệt.
- Việc kiểm thử lại (redo) là cần thiết nếu bạn thực hiện sai hướng dẫn vì nó ảnh hưởng trực tiếp đến kết quả.
- Việc hủy nhận suất (unclaim slot) là bắt buộc nếu bạn lỡ nhận sai slot vì nó sẽ tạo ra các kết quả không hợp lệ.
- Tuân thủ Điều khoản Sử dụng uTest là bắt buộc và vi phạm có thể dẫn đến việc bị chấm dứt tài khoản.
- Bạn cần đối xử tôn trọng với tất cả mọi người, luôn chuyên nghiệp và lịch sự khi giao tiếp.

**Hạn chế thảo luận căng thẳng:** Tránh thảo luận về những lo ngại hoặc bất đồng của bạn đối với thông điệp hoặc quyết định trong phòng chat của chu kỳ (cycle chat room), hoặc tab tin nhắn (messages tab) trong báo cáo lỗi, test case, hoặc phần đánh giá. Ngoài ra, hãy kiềm chế việc tìm kiếm sự đồng tình từ những người khác trong cộng đồng hoặc tự ý báo cáo vượt cấp (escalate) trực tiếp lên TSM hoặc cấp cao hơn khi chưa thấu hiểu rõ vấn đề. Những hành động này có thể làm phức tạp tình huống một cách không cần thiết mà không mang lại giải pháp cụ thể, và bạn thậm chí có thể vi phạm Điều khoản Sử dụng của uTest mà không nhận ra trong các cuộc thảo luận căng thẳng.

Chìa khóa để giải quyết vấn đề là giao tiếp hiệu quả, và giao tiếp hiệu quả chỉ có thể đạt được nếu bạn kiểm soát được sự giận dữ của mình, chấp nhận các góc nhìn của người khác và thảo luận vấn đề một cách chuyên nghiệp, đúng mực.

### 4. Các vấn đề có thể xảy ra và giải pháp
Sau khi hiểu rõ thông điệp hoặc quyết định, nếu bạn nghĩ chúng không đúng với hướng dẫn hoặc bất kỳ thông tin nào được cung cấp, bạn có thể tiến hành bước tiếp theo:
- **Khiếu nại (dispute)** báo cáo lỗi nếu vấn đề liên quan đến báo cáo lỗi đó. Hãy nhớ rằng bạn nên kiểm tra kỹ lý do từ chối (rejection reason) cụ thể ghi trong báo cáo lỗi của mình chứ không chỉ nhìn vào loại từ chối (rejection type).
- **Báo cáo lên TE (escalate)** nếu liên quan đến các vấn đề khác, chẳng hạn như test case hoặc phần đánh giá bị từ chối/bị hủy nhận mà không có lý do rõ ràng hoặc do TTL có hành vi sai trái (misconduct), v.v. Việc báo cáo lên TE cần tuân theo đúng quy tắc báo cáo vượt cấp (escalation rules) được đề cập trong phần Thông tin Liên hệ của Nhóm (Team Contact Information). Lưu ý rằng tốt nhất nên tránh việc báo cáo vượt cấp trừ khi đó là vấn đề khẩn cấp hoặc cần sự chú ý và trợ giúp từ cấp cao hơn để giải quyết.

Tiếp theo, hãy chuẩn bị nội dung bạn muốn gửi đi. Thu thập bất kỳ thông tin hữu ích nào có thể hỗ trợ cho khiếu nại của bạn và cung cấp ảnh chụp màn hình (screenshots) nếu cần thiết. Kiểm tra lại trang web/ứng dụng kiểm thử, các tài liệu được cung cấp và các thông tin liên quan khác.

Khi đã chuẩn bị xong ý kiến và bằng chứng, hãy bắt đầu soạn email nháp gửi cho TE của chu kỳ kiểm thử (email của TE được cung cấp trong phần tổng quan chu kỳ). Không sử dụng email của các TE ở các chu kỳ khác vì họ không chịu trách nhiệm cho tất cả các chu kỳ kiểm thử.

Khi viết email, hãy lưu ý những điều sau:
- Ghi rõ mã định danh chu kỳ (Cycle ID) trong tiêu đề email.
- Đảm bảo viết nội dung bày tỏ lo ngại một cách lịch sự và chuyên nghiệp.
- Giải thích rõ ràng mối bận tâm của bạn và tập trung thẳng vào vấn đề lỗi.
- Tránh viết email quá dài dòng mà không có luận điểm rõ ràng.
- Kiểm tra lại bài viết của bạn để đảm bảo thông điệp rõ ràng và dễ hiểu.
- Không CC hoặc BCC email cho các TE khác hoặc các TSM khác.

*Lưu ý:* Chỉ nên liên hệ với TSM nếu có vấn đề liên quan đến việc thanh toán tiền thưởng (payout), trường hợp khẩn cấp, hoặc nếu bạn chưa nhận được phản hồi từ TE sau thời gian phản hồi dự kiến được quy định trong quy tắc báo cáo vượt cấp.

Hãy yên tâm rằng nhóm dự án luôn cam kết giải quyết vấn đề một cách nhanh chóng. Phản hồi của bạn rất có giá trị đối với nhóm vì nó có thể giúp cải thiện quy trình làm việc.

### 5. Các kết quả có thể xảy ra
Kết quả có thể xảy ra theo ba hướng: được chấp nhận (accepted), bị từ chối (rejected), hoặc ghi nhận để xem xét và cải tiến trong tương lai (future consideration and improvement). Hãy hiểu rằng không phải ý kiến nào cũng được chấp nhận và một số phản hồi cần thời gian để áp dụng. Tại thời điểm này, bạn cần giữ sự bình tĩnh và lý trí, không còn tư tưởng *"tôi luôn luôn đúng"* hoặc coi các góc nhìn khác là sai trái. Nếu bạn không thể vượt qua cảm giác này, bạn nên quay lại điểm thứ nhất và thứ hai, hoặc tốt nhất là dừng lại tại đây vì nó có thể ảnh hưởng đến sức khỏe tinh thần của bạn.

- **Về việc khiếu nại (dispute)**: Nếu khiếu nại bị từ chối, hãy đảm bảo đọc kỹ lý do từ chối. Bạn sẽ nhận được lý do chi tiết hơn cho việc từ chối sau khi tiến hành khiếu nại. Nếu lý do từ chối đó là hợp lý, bạn cần chấp nhận nó và tiếp tục công việc của mình. Việc chấp nhận sẽ giúp chúng ta trở thành một tester tốt hơn và tránh báo cáo các lỗi tương tự cho khách hàng đó trong tương lai.
- **Về email gửi TE**: Nếu bạn nhận được phản hồi từ TE, hãy đọc kỹ tin nhắn. Nếu có yêu cầu cần bạn thực hiện và bạn sẵn lòng hỗ trợ, hãy giúp TE để vấn đề có thể được giải quyết. Nếu họ tự giải quyết ở phía họ, bạn có thể chờ đợi xem lỗi có được xử lý trong thời gian diễn ra chu kỳ kiểm thử đó hay ghi nhận xử lý trong tương lai.

Trong mọi trường hợp, hãy đảm bảo giữ giao tiếp một cách chuyên nghiệp. Nếu cảm xúc nóng nảy trỗi dậy, hãy cố gắng hạ hỏa trước khi trả lời tin nhắn. Ngoài ra, hãy giữ việc giao tiếp trong cùng một chuỗi email (thread) và tránh tạo một chuỗi email mới để phản hồi tin nhắn của TE.

*Lưu ý:* Nếu vấn đề của bạn là khẩn cấp và bạn chưa nhận được phản hồi sau thời gian phản hồi dự kiến từ TE hoặc TSM, bạn có thể tìm kiếm sự trợ giúp từ bộ phận Hỗ trợ Tester (Tester Support). Bạn có thể mở Cổng thông tin hỗ trợ Tester (Tester Support Portal) > Chọn Gửi yêu cầu hỗ trợ (Request Support) > Chọn Các vấn đề về Chu kỳ kiểm thử (Test Cycle Issues) cho danh mục yêu cầu và hoàn thành biểu mẫu tương ứng.

### Hãy tự hào về bản thân
Nếu bạn có thể xử lý cơn giận của mình một cách thích hợp khi đối mặt với những vấn đề đầy thử thách, hãy cho phép chúng tôi chúc mừng bạn. Giận dữ là một cảm xúc khó vượt qua, tuy nhiên làm được việc đó là một thành tựu quan trọng trong cuộc sống. Bạn không chỉ thể hiện sự chuyên nghiệp mà còn đang góp phần xây dựng cộng đồng tốt đẹp hơn.

Chúng tôi hy vọng những lời khuyên này sẽ giúp bạn duy trì một thói quen tốt để có thể phản ứng một cách tự nhiên, bình tĩnh và chuyên nghiệp trong tương lai. Đồng thời, bạn có thể xử lý các tình huống thách thức một cách hiệu quả, đạt được kết quả tối ưu nhất và đóng góp vào sự tiến bộ của hoạt động kiểm thử sau này.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Dispute | Khiếu nại | Quy trình khi không đồng ý với kết quả duyệt lỗi của TTL |
| Escalation | Báo cáo vượt cấp | Chuyển vấn đề từ TTL lên các cấp cao hơn (TE, TSM) |
| Cycle ID | Mã định danh chu kỳ | Số ID duy nhất để xác định một chu kỳ kiểm thử |
| WAD (Working As Designed) | Hoạt động đúng thiết kế | Trạng thái lỗi bị từ chối do hệ thống hoạt động đúng đặc tả thiết kế |
| Rejection | Từ chối | Trạng thái báo cáo lỗi không được chấp nhận |
| Misconduct | Vi phạm hành vi / Hành vi sai trái | Các hành vi vi phạm quy định hoặc giao tiếp thiếu chuẩn mực |
| Account Suspension | Đình chỉ tài khoản | Hình phạt khóa tài khoản tạm thời khi vi phạm quy tắc |
