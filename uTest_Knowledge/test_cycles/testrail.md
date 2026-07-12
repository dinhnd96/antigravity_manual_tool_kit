# Hướng dẫn sử dụng TestRail (TestRail Guide)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Giới thiệu
TestRail là một công cụ quản lý test case trực tuyến (web-based) được sử dụng để theo dõi và sắp xếp các hoạt động kiểm thử phần mềm theo thời gian thực. Một số khách hàng của Applause sử dụng TestRail để quản lý các bộ kiểm thử (test suites), thực thi các bài kiểm thử và theo dõi kết quả. Do đó, việc hiểu rõ các khái niệm cơ bản về TestRail và cách hoạt động của nó là vô cùng quan trọng.

Quy trình thực thi test case trên TestRail cũng tương tự như trên Nền tảng uTest. Tuy nhiên, nó có một số trạng thái lượt kiểm thử (test run statuses) khác nhau dựa trên kết quả kiểm thử thu được. Dưới đây là các trạng thái kết quả trong TestRail:

* **Passed (Đạt)**: Một test case được đánh dấu là Passed khi kết quả thực tế thu được ở các bước kiểm thử khớp hoàn toàn với kết quả mong đợi (expected results).
* **Failed (Không đạt)**: Một test case được đánh dấu là Failed nếu kết quả thực tế thu được ở một hoặc nhiều bước kiểm thử khác với kết quả mong đợi.
* **Blocked (Bị chặn)**: Trạng thái Blocked xác định rằng một bài kiểm thử không thể thực hiện được vì các lý do bên ngoài, ví dụ như một tính năng nào đó bị lỗi nghiêm trọng khiến tester không thể hoàn thành việc kiểm thử tính năng tiếp theo đang được kiểm tra.
* **Retest (Kiểm thử lại)**: Trạng thái retest được sử dụng khi test case cần phải được kiểm thử lại. Ví dụ: một test case đã bị Failed do có lỗi (bug), sau khi lỗi đó được sửa thì test case này cần được kiểm thử lại trên bản build mới.
* **Untested (Chưa kiểm thử)**: Cho biết test case chưa được kiểm thử và chưa có kết quả kiểm thử nào được gán cho tính năng đó.

### Các thuật ngữ phổ biến trong TestRail
* **Dashboard (Bảng điều khiển)**: Đây là trang đầu tiên người dùng nhìn thấy sau khi đăng nhập vào TestRail. Quản trị viên dự án (project Admin) có thể tùy chỉnh Dashboard để hiển thị bất kỳ thông tin nào của dự án.
* **Test Case (Trường hợp kiểm thử)**: Một tập hợp các bước được xác định trước và thực hiện trên sản phẩm để kiểm tra xem sản phẩm có hoạt động chính xác hay không.
* **Test Suite (Bộ kiểm thử / Bộ test case)**: Một nhóm các test case dùng để kiểm thử một tính năng cụ thể hoặc một phân mục của sản phẩm.
* **Test Run (Lượt chạy kiểm thử / Lượt kiểm thử)**: Hành động thực thi một test case trong một môi trường cụ thể. Một test case đơn lẻ có thể có nhiều lượt chạy kiểm thử (test runs) trong các môi trường và phiên bản sản phẩm khác nhau.
* **Test Plan (Kế hoạch kiểm thử)**: Một kế hoạch kiểm thử bao gồm nhiều lượt chạy kiểm thử trong các môi trường khác nhau. Kế hoạch kiểm thử cho phép tổ chức nhiều lượt chạy kiểm thử trong nhiều môi trường khác nhau một cách có hệ thống.
* **Milestone (Cột mốc)**: Đây là một giai đoạn hoặc mục tiêu trong dự án TestRail, ví dụ như lịch phát hành phần mềm dự kiến, việc hoàn thành kiểm thử nội bộ cho tất cả các tính năng sắp ra mắt, v.v.
* **Project (Dự án)**: Đây là đơn vị tổ chức cấp cao nhất trong TestRail. Tất cả dữ liệu kiểm thử như lượt chạy kiểm thử (test runs), kết quả kiểm thử (test results) và cột mốc (milestones) đều liên kết trực tiếp với một dự án cụ thể.

### Thực thi các Test Case trên TestRail
Các nguyên tắc khi thực thi test case trên TestRail bao gồm:
* Tài khoản TestRail thuộc quyền sở hữu của khách hàng, vì vậy hãy cực kỳ cẩn thận khi sử dụng.
* Bạn nên đăng xuất khỏi tài khoản TestRail ngay sau khi hoàn thành việc kiểm thử.
* Không cố gắng đăng nhập sai nhiều lần. Nếu có bất kỳ sự cố nào, hãy liên hệ ngay với TTL của chu kỳ.
* Không thay đổi mật khẩu hoặc cài đặt tài khoản TestRail.
* Chỉ thực thi đúng (các) Test Case mà bạn đã đăng ký tham gia.
* Nếu bạn có bất kỳ thắc mắc hoặc câu hỏi nào, hãy liên hệ với TTL của chu kỳ.

Để thực thi một test case hoặc test run trên TestRail, vui lòng làm theo các bước dưới đây:
1. Truy cập liên kết TestRail được cung cấp và đăng nhập bằng thông tin đăng nhập (credentials) theo hướng dẫn trong chu kỳ.
2. Trên menu điều hướng bên trái, nhấp vào thư mục chứa các test case được giao cho bạn. (Bạn có thể bỏ qua bước này nếu liên kết TestRail được cung cấp mở trực tiếp test case được giao).
3. Mở bước đầu tiên và làm theo hướng dẫn được cung cấp để thực thi bước đó.
4. Sau khi thực thi các hướng dẫn, hãy nhấp vào nút **Add Result** (Thêm kết quả).
5. Nhấp vào menu thả xuống **Status** và chọn trạng thái thích hợp dựa trên kết quả thu được:
   * **Passed**: Nếu kết quả thu được khớp với kết quả mong đợi.
   * **Failed**: Nếu kết quả thu được không khớp với kết quả mong đợi.
   * **Blocked**: Nếu không thể chạy bài kiểm thử vì tính năng không khả dụng hoặc do một lỗi hiện có khiến việc hoàn thành kiểm thử trở nên bất khả thi.
6. Nhấp vào biểu tượng hình ảnh phía trên trường bình luận để tải lên ảnh chụp màn hình (screenshot) nếu được yêu cầu.
7. Nhấp vào trường **Comment** (Bình luận) và nhập mô tả về kết quả hoặc bất kỳ thông tin nào theo hướng dẫn trong chu kỳ.
   * *Lưu ý:* Không phải khách hàng nào cũng yêu cầu thêm tệp đính kèm hoặc bình luận trên TestRail. Vì vậy, hãy đọc kỹ hướng dẫn trong phần tổng quan chu kỳ hoặc các bước của test case để thực hiện đúng yêu cầu. Không thêm bất kỳ bình luận hay tệp đính kèm nào nếu chúng không bắt buộc.
8. Nếu một bước bị fail trong quá trình thực thi do có bug, hãy nhấp vào trường **Defects** (Lỗi) và thêm ID của lỗi đó theo hướng dẫn của chu kỳ. Để trống trường này nếu không yêu cầu ID lỗi.
9. Sau khi hoàn thành bước kiểm thử, hãy nhấp vào nút **Add Result** để thêm kết quả cho bước đó.
10. Chuyển sang các bước tiếp theo cho đến khi hoàn thành tất cả các bước trong test case và các kết quả đã được thêm đầy đủ.
11. Sau khi thực thi (các) Test Case và thêm kết quả thành công, hãy quay lại nền tảng uTest và nộp kết quả Test Case (Submit Test Case).

Dưới đây là một số liên kết để tìm hiểu thêm về TestRail:
* [Introduction to TestRail](https://www.gurock.com/testrail/docs/user-guide/getting-started/introduction)
* [Getting started with TestRail](https://www.gurock.com/testrail/docs/user-guide/getting-started/walkthrough)

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| TestRail | TestRail | Công cụ quản lý test case trực tuyến của bên thứ ba |
| Test Run | Lượt chạy kiểm thử / Lượt kiểm thử | Quá trình thực thi test case trong một môi trường cụ thể |
| Test Suite | Bộ kiểm thử / Bộ test case | Nhóm các test case kiểm thử một tính năng hoặc phân mục |
| Milestone | Cột mốc | Một giai đoạn hoặc mục tiêu trong dự án kiểm thử |
| Blocked | Bị chặn | Trạng thái test không thể thực hiện do nguyên nhân bên ngoài |
| Untested | Chưa kiểm thử | Trạng thái test case chưa được chạy và chưa có kết quả |
