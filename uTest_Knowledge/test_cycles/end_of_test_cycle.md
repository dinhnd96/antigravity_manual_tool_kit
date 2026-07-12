# Kết Thúc Test Cycle (End of the Test Cycle)

> **Nguồn gốc**: uTest Academy — End of the Test Cycle
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: test_cycles

---

## Bản dịch

### Khóa Test Cycle (Test Cycle Lock)

Test cycle sẽ kết thúc khi **hết thời hạn** của cycle. Tại thời điểm này, test cycle sẽ chuyển sang trạng thái **Locked** (Đã khóa). Sau khi cycle bị khóa, **không thể nộp thêm** bug report hoặc test case nào nữa.

#### Tester có thể làm gì khi cycle đã khóa?

Tester vẫn có thể thực hiện các hành động sau:

- ✏️ **Chỉnh sửa** bug report đã nộp
- ✏️ **Chỉnh sửa** test case đã nộp
- 💬 **Đặt câu hỏi** trong chat của test cycle

---

### Đánh giá bài nộp (Review of Submissions)

- Các bug report, test case và review đã nộp sẽ được **đánh giá trong vòng 15 ngày** sau khi test cycle bị khóa
- Nếu đã quá **15 ngày** sau khi cycle khóa mà công việc của bạn **chưa được đánh giá**, bạn nên **liên hệ nhân sự** của test cycle bằng thông tin liên hệ trong tab **Overview**

---

### Đóng Test Cycle (Test Cycle Close)

Khi tất cả bài nộp đã được đánh giá và kết quả đã gửi cho khách hàng, test cycle sẽ chuyển sang trạng thái **Closed** (Đã đóng).

- Tester **không thể thực hiện bất kỳ hành động nào** trong cycle đã đóng
- Tester **chỉ có thể xem** thông tin chi tiết

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Test Cycle Lock | Khóa Test Cycle | Hết thời hạn, không nộp thêm được |
| Test Cycle Close | Đóng Test Cycle | Hoàn tất review, chỉ xem lại |
| Submission | Bài nộp | Bug report, test case, review đã gửi |
| Review Period | Thời gian đánh giá | Tối đa 15 ngày sau khi lock |
