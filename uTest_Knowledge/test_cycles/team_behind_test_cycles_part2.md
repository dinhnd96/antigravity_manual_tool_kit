# Đội ngũ Đứng sau Chu kỳ Kiểm thử - Phần 2/2 (The Team Behind Test Cycles)

> **Nguồn gốc**: uTest Academy / Courses
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles
> **Ghi chú**: Phần 2/2 — Tình huống & Giải pháp cho các vấn đề tiềm ẩn

---

## Bản dịch

### Tình huống & Giải pháp cho các Vấn đề Tiềm ẩn (Scenarios & Solutions)

#### Tester không nhận được trả lời từ TTL đúng thời hạn

Nếu bạn không nhận được trả lời kịp thời hoặc trong khung thời gian được nêu trong phần Team Contact Information của tổng quan chu kỳ, bạn có thể gửi email cho TE. Email TE cũng nằm trong phần Team Contact Information. Sau đó, hãy chờ TE phản hồi.

#### TE không phản hồi tester

Nếu bạn không nhận được phản hồi từ TE trong khung thời gian quy định tại phần Team Contact Information, bạn có thể liên hệ TSM. Email TSM cũng nằm trong phần Team Contact Information.

Hãy đảm bảo cung cấp giải thích rõ ràng và đầy đủ thông tin cần thiết như Cycle ID, Cycle name, Tester ID, Bug report ID, Test Case ID... khi gửi email cho TE hoặc TSM.

#### TSM không phản hồi tester

Đây là tình huống hiếm gặp khi bạn không nhận được phản hồi từ TTL, TE hay TSM. Bạn có thể kiểm tra lại yêu cầu xem có tuân thủ Điều khoản Sử dụng không. Nếu yêu cầu đã đúng và vẫn không có phản hồi, hãy liên hệ **Tester Support** (https://support.utest.com/csp > Request Support > Test Cycle Issues cho Request Category) và họ sẽ hỗ trợ bạn.

Đảm bảo cung cấp giải thích rõ ràng và đầy đủ thông tin (Cycle ID, Cycle name, Tester ID, Bug report ID, Test Case ID...) khi nộp phiếu hỗ trợ.

#### Khách hàng từ chối lỗi công bằng hoặc không công bằng

Lỗi không hợp lệ sẽ bị khách hàng từ chối một cách hợp lý. Bạn có thể kiểm tra lý do từ chối và có quyền phản đối (dispute) một cách lịch sự nếu bạn không đồng ý.

Trong trường hợp lỗi bị từ chối **không công bằng**, hãy kiểm tra lý do từ chối trước khi chuyển vấn đề lên. Sau khi xác nhận tình huống, bạn có thể thu thập bằng chứng dưới dạng ảnh chụp màn hình hoặc video, rồi gửi email cho TE để chuyển vấn đề lên. Như đã đề cập, nếu không nhận được phản hồi, hãy tiếp tục chuyển lên TSM. Họ sẽ thảo luận và đưa ra giải pháp.

#### Lỗi nghiêm trọng cao được duyệt với giá trị thấp

Xin lưu ý rằng **khách hàng quyết định** giá trị của lỗi đối với họ và đây là điều chúng ta không kiểm soát được. Tuy nhiên, bạn có thể chuyển vấn đề lên TE. Trước tiên, hãy kiểm tra lại báo cáo và đảm bảo lỗi được phân loại đúng mức nghiêm trọng cao và nằm trong trọng tâm chu kỳ (VD: lỗi crash). Thu thập bằng chứng hỗ trợ, gửi email cho TE kèm tệp đính kèm. Họ sẽ thực hiện các hành động cần thiết và phản hồi.

#### Lỗi được duyệt là Won't Fix (WNF)

Won't Fix nghĩa là lỗi hợp lệ, tuy nhiên khách hàng không phân bổ thời gian và công sức để sửa mà tập trung vào các loại lỗi khác. Nếu nhiều lỗi bị chấp nhận là WNF dù nằm trong trọng tâm kiểm thử hoặc liên quan đến bước test case hoặc là vấn đề chặn, bạn có thể hỏi TE xác nhận việc đánh giá đã đúng chưa.

#### Lỗi không được duyệt hoặc từ chối sau thời gian dài

Nếu lỗi chưa được duyệt/từ chối sau khi chu kỳ khóa, bạn có thể chờ đến **15 ngày** vì chu kỳ sẽ tự động đóng và lỗi sẽ được duyệt/từ chối tự động theo khuyến nghị của TTL. Điều này cũng áp dụng cho test case. Với review, tất cả sẽ được chấp nhận nếu chưa được kiểm tra khi chu kỳ đóng.

Nếu lỗi vẫn chưa được kiểm tra hoặc ở trạng thái New ngay cả sau khi chu kỳ khóa, bạn có thể thông báo cho TE.

#### Test Case bị hủy nhận/từ chối không có lý do

Nếu test case bị hủy nhận/từ chối mà không có lý do, dù bạn đã có tiến độ hoặc hoàn thành đúng hướng dẫn, bạn có thể email TE. Các lý do có thể bao gồm:

* Slot bị tự động hủy vì không nộp trong thời hạn cho phép
* Hủy nhận hoặc từ chối nhầm
* Test case thực thi kém nhưng nhóm quên ghi lý do khi hủy/từ chối
* Test case được cập nhật và TE/TSM quyết định hủy tất cả test case mà không ghi rõ lý do. Bạn có thể nhận thông báo về việc này và được yêu cầu nhận test case mới

#### Bị chặn kiểm thử do vấn đề sản phẩm

Bạn có thể thông báo TTL khi gặp vấn đề chặn và họ sẽ chuyển lên TE/TSM. Đồng thời, hãy thử tìm cách giải quyết tạm thời (workaround) và thông báo cho nhóm.

#### Về lỗi xảy ra một lần (One-time issues)

Nếu bạn thu thập được bằng chứng (video và log), bạn có thể báo cáo lỗi dù khó tái hiện. Ví dụ: khi cố tái hiện lỗi trong lúc quay video, ứng dụng bất ngờ crash — vì bạn có video và log, bạn có thể báo cáo. Trước đó, hãy đảm bảo lỗi không tái hiện được không nằm trong phần OOS, và có thể hỏi TTL xác nhận.

#### Lỗi tự sửa hoặc lỗi tạm thời

Nếu lỗi được sửa khi kiểm tra lại hoặc là lỗi tạm thời:
* Nếu lỗi **chưa được duyệt** → bạn có thể hủy bỏ (discard) báo cáo
* Nếu bạn **đã được yêu cầu tái hiện** → thông báo TTL rằng lỗi không còn tái hiện được qua tab Messages của báo cáo

#### Bị yêu cầu hủy báo cáo dù lỗi vẫn tái hiện được

Nếu lỗi tái hiện được khi bạn báo cáo nhưng không còn khi được yêu cầu tái hiện lại, và bạn bị yêu cầu hủy:

* Bạn có thể thông báo TE xem xét lại vì lỗi hợp lệ và tái hiện được tại thời điểm báo cáo
* Tuy nhiên, lỗi có thể bị từ chối vì là vấn đề tạm thời hoặc liên quan đến thiết bị/trình duyệt của bạn
* Nếu bạn tin chắc không phải như vậy, hãy thu thập bằng chứng và báo cáo cho TE điều tra

Bạn cũng có thể thông báo TE khi khách hàng cung cấp build sai hoặc yêu cầu test build mới trong khi lỗi đã báo không còn tái hiện trên build mới. Vì đây không phải lỗi của bạn, bạn có thể phản đối nếu lỗi bị từ chối.

#### Xác minh email hợp lệ

Để xác nhận email đến từ uTest, kiểm tra địa chỉ email người gửi. uTest chỉ gửi email từ các domain sau:

* **uTest.com**
* **m.uTest.com**
* **Applause.com**
* **Applausemail.com**

Ví dụ: email từ `us@utest.com` có domain `utest.com` → hợp lệ. Nếu email không sử dụng các domain trên → không hợp lệ. Bạn có thể báo cáo tại https://support.utest.com/csp > Request Support > Potential Cheating/Fraud/Misbehaviour.

---

### Các Khóa học Hữu ích nên Xem lại

* uTest Basics (Kiến thức cơ bản uTest)
* Testing Basics (Kiến thức cơ bản Kiểm thử)
* uTest Cycle Process (Quy trình Chu kỳ uTest)
* Slots, Test Cases and Reviews (Slot, Test Case và Đánh giá)
* Bug Reports (Báo cáo Lỗi)

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Blocking Issue | Vấn đề chặn | uTest |
| Tester Support | Hỗ trợ Tester | uTest |
| Dispute | Phản đối / Tranh chấp | uTest |
| Workaround | Cách giải quyết tạm thời | QA |
| Discard | Hủy bỏ (báo cáo) | uTest |
