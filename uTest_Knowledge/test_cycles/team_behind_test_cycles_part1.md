# Đội ngũ Đứng sau Chu kỳ Kiểm thử - Phần 1/2 (The Team Behind Test Cycles)

> **Nguồn gốc**: uTest Academy / Courses
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles
> **Ghi chú**: Phần 1/2 — Vai trò các thành viên (Testers, TTL, TE, TSM)

---

## Bản dịch

Các thành viên đứng sau mỗi chu kỳ kiểm thử đóng vai trò thiết yếu trong việc đảm bảo chu kỳ đạt kết quả tốt nhất và vượt xa kỳ vọng. Dưới đây là vai trò của họ trong mỗi chu kỳ:

### Tester (Người kiểm thử)

Tester là vai trò quan trọng nhất trong chu kỳ kiểm thử. Họ tìm lỗi, thực thi test case, cung cấp phản hồi và báo cáo mọi vấn đề liên quan đến sản phẩm được kiểm thử.

#### Trách nhiệm / Nhiệm vụ

* Hiểu rõ sản phẩm đang được kiểm thử
* Báo cáo lỗi, thực thi test case, nộp đánh giá và các tác vụ kiểm thử khác trong chu kỳ
* Phản hồi mọi yêu cầu thông tin (info request) càng sớm càng tốt
* Viết báo cáo lỗi chất lượng cao
* Hoàn thành test case trong thời hạn
* Xem lại tổng quan và báo cáo các vấn đề chặn (blocking issues) cho TTL
* Hỗ trợ các tester đồng nghiệp trong phòng chat nếu bạn biết câu trả lời

#### Tester nên làm gì

* Tuân thủ Điều khoản Sử dụng uTest và Hướng dẫn AI
* Chuyên nghiệp và lịch sự khi giao tiếp
* Tuân theo hướng dẫn chu kỳ kiểm thử
* Sử dụng chat chu kỳ đúng cách
* Hoàn thành các tác vụ được giao một cách kỹ lưỡng và trung thực
* Chấp nhận chu kỳ khi có cam kết với chu kỳ đó
* Báo cáo lỗi trong phạm vi (in scope)
* Nhận slot phù hợp với môi trường của bạn
* Nộp test case sau khi đã thực thi xong
* Cung cấp phản hồi kỹ lưỡng trong phần đánh giá (review)
* Xem thêm Điều khoản Sử dụng uTest để biết các điểm khác

#### Tester không nên làm gì

* Vi phạm Điều khoản Sử dụng uTest và Hướng dẫn AI
* Gian dối
* Công khai thông tin khách hàng
* Thảo luận về thanh toán trước mặt khách hàng
* Tạo nhiều hơn một tài khoản uTest
* Giả mạo bất kỳ thông tin nào
* Sử dụng VPN
* Yêu cầu duyệt công việc đã nộp
* Báo cáo lỗi không hợp lệ — luôn kiểm tra lỗi đã báo, danh sách Known Issues và phần OOS
* Nhận slot đến giới hạn tối đa để ngăn tester khác nhận
* Nhận slot rồi không làm gì (sit on them)
* Thực thi test case không đúng cách
* Hủy nhận test case rồi không hoạt động trong chu kỳ
* Cung cấp tệp đính kèm không hợp lệ
* Sử dụng add-on, script... để cố ý tìm lỗi
* Phản đối (dispute) lỗi bị từ chối mà không có lý do
* Thô lỗ và thiếu chuyên nghiệp
* Không viết TOÀN BỘ CHỮ IN HOA để thu hút sự chú ý
* Xem thêm Điều khoản Sử dụng uTest và Hướng dẫn AI

---

### Trưởng nhóm Kiểm thử (Test Team Lead — TTL)

TTL là các thành viên được tuyển chọn kỹ từ cộng đồng uTest, làm việc sát cánh với TSM và TE để điều phối luồng công việc và kết quả chu kỳ. Dù nhiệm vụ mỗi chu kỳ có thể khác nhau, mục tiêu luôn giống: tăng giá trị mà uTest mang lại cho khách hàng bằng cách tối đa hóa đầu ra và giảm thiểu nhiễu.

TTL là đầu mối liên hệ chính cho tester qua chat chu kỳ. Họ chịu trách nhiệm hỗ trợ tester, duyệt tất cả báo cáo lỗi, test case và chuyển vấn đề lên TE khi cần.

#### Trách nhiệm / Nhiệm vụ

* Giao tiếp với tester trong suốt chu kỳ
* Phân loại (triage) báo cáo lỗi và test case kịp thời
* Hỗ trợ TE với các nhiệm vụ được giao
* Xem lại tổng quan chu kỳ và chuyển vấn đề lên TE
* Kiểm thử nhanh sản phẩm để đảm bảo không có vấn đề chặn
* Theo dõi tiến độ chung và chat chu kỳ
* Hỗ trợ tester giải quyết câu hỏi và vấn đề
* Xem xét tranh chấp lỗi và đưa ra khuyến nghị

#### Tester kỳ vọng gì từ TTL

* Hữu ích, lịch sự, kiên nhẫn và phản hồi nhanh khi giao tiếp
* Lỗi và test case được duyệt kịp thời
* Trả lời các câu hỏi liên quan đến chu kỳ theo Điều khoản Sử dụng
* Chat riêng chỉ dùng cho chủ đề cá nhân không thể thảo luận công khai

#### Tester không nên kỳ vọng từ TTL

* Câu hỏi về thanh toán nên hỏi TE hoặc TSM, không phải TTL
* Lỗi và test case không được duyệt/phê duyệt theo yêu cầu của tester
* Câu hỏi cho TTL chỉ nên hỏi trong chat chu kỳ, phương thức liên hệ khác chỉ khi TE/TSM cho phép

---

### Kỹ sư Kiểm thử (Test Engineer — TE)

TE xây dựng và quản lý chu kỳ kiểm thử, tập hợp đội kiểm thử và chịu trách nhiệm cho toàn bộ quá trình thực thi. Họ đảm bảo đội đạt kết quả tốt nhất cho khách hàng.

#### Trách nhiệm / Nhiệm vụ

* Thiết lập chu kỳ kiểm thử
* Theo dõi tiến độ chu kỳ
* Tuyển dụng đội kiểm thử từ cộng đồng
* Đảm bảo kiểm thử và phân loại tiến hành đúng lịch
* Giải quyết vấn đề của tester và chuyển lên TSM nếu cần
* Giải quyết tranh chấp lỗi
* Viết và điều chỉnh test case
* Viết Khảo sát Yêu cầu Đặc biệt (SRS)
* Thực hiện các hành động để đưa chu kỳ trở lại đúng hướng
* Làm việc trực tiếp với TSM để đạt mục tiêu chiến lược
* Đóng vai trò TTL cho một số dự án

---

### Quản lý Dịch vụ Kiểm thử (Testing Services Manager — TSM)

TSM làm việc trực tiếp với khách hàng và quản lý đội TTL và TE để cung cấp giải pháp phù hợp cho nhu cầu kiểm thử, phản hồi hoặc nghiên cứu. Họ cũng chịu trách nhiệm ra quyết định tài chính trong chu kỳ.

#### Trách nhiệm / Nhiệm vụ

* Phối hợp với TE phát triển chiến lược kiểm thử
* Quản lý đội TE, TTL, DT và TCW
* Giám sát tài chính tài khoản và xử lý thanh toán
* Đảm bảo kiểm thử đáp ứng kỳ vọng khách hàng
* Cung cấp chỉ đạo cho TE
* Giám sát chi tiêu tài khoản
* Xử lý và phê duyệt thanh toán

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Blocking Issue | Vấn đề chặn | uTest |
| Tester Support | Hỗ trợ Tester | uTest |
