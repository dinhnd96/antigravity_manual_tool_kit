# Hủy nhận suất tham gia (Unclaiming a Slot)

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Cách hủy nhận một Slot (How to Unclaim a Slot?)
Trong trường hợp bạn muốn hủy nhận một suất tham gia (unclaim a slot) vì bất kỳ lý do nào, hãy thực hiện các bước sau:

1. Điều hướng đến tab **Test Cases** của cycle.
2. Mở test case tương ứng với slot bạn muốn hủy nhận.
3. Nhấp vào nút **Unsubmit** (Hủy nộp) cho test case nếu bạn đã nộp (submit) trước đó.
4. Nếu slot được liên kết với nhiều test case, bạn cần hủy nộp (unsubmit) **tất cả** các test case liên kết với slot đó.
5. Điều hướng đến tab **Slots** của cycle.
6. Nhấp vào nút **Unclaim** (Hủy nhận).
7. Nêu rõ lý do hủy nhận slot.
8. Nhấp vào nút **Unclaim** để xác nhận hủy nhận slot.

### Lưu ý về việc hủy nhận Slot (Notes on Unclaiming a Slot)
- Việc hủy nhận một slot cũng sẽ đồng thời hủy nhận **tất cả** các test case được liên kết với slot đó.
- **Không thể** hủy nhận một slot nếu bất kỳ test case liên kết nào đã được nộp (submitted). Bạn cần hủy nộp (unsubmit) toàn bộ các test case đã nộp trước khi hủy nhận slot.
- Nếu một trong các test case liên kết với slot bị tự động hủy nhận do hết thời hạn (auto unclaimed due to time), tất cả các test case liên kết với slot đó cũng sẽ bị hủy nhận.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Unclaim | Hủy nhận / Bỏ suất | Hành động trả lại slot đã claim về hệ thống |
| Unsubmit | Hủy nộp | Rút lại kết quả test case đã submit trước đó |
| Auto unclaimed | Tự động hủy nhận | Hệ thống tự hủy khi tester không hoàn thành đúng hạn |
