# Tính năng Thông tin đăng nhập của Slot (Slot Credentials Feature)

> **Nguồn gốc**: Tài liệu hướng dẫn uTest (uTest Academy / Course)
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

Tính năng thông tin đăng nhập của slot (Slot Credentials) cho phép các TE thêm thông tin đăng nhập kiểm thử vào slot khi mỗi tester cần sử dụng một tài khoản kiểm thử duy nhất hoặc cụ thể trong quá trình test. Chỉ tester đã nhận slot (claimed the slot) mới có quyền truy cập vào thông tin đăng nhập được gán cho slot đó.

### Khả năng hiển thị thông tin đăng nhập (Credential Visibility)

Thông tin đăng nhập **không hiển thị** cho đến khi slot được nhận (claimed). Sau khi nhận slot, bạn sẽ có thể xem thông tin đăng nhập tại:
- Cột **Credentials** (Thông tin đăng nhập) trên trang Slots
- Phần **Credentials** trên trang test case

Thông tin đăng nhập chỉ hiển thị khi test cycle đang ở trạng thái **Active** (Đang hoạt động).

Khi slot hoặc test case bị hủy nhận (unclaimed) hoặc cycle bị khóa (locked), bạn sẽ **không còn** nhìn thấy thông tin đăng nhập. Tuy nhiên, thông tin đăng nhập sẽ hiển thị trở lại khi một test case liên kết với slot đó ở trạng thái **Info Requested** (Yêu cầu bổ sung thông tin), bất kể test cycle đang ở trạng thái Active hay Locked.

**Lưu ý quan trọng**: Thông tin đăng nhập được cung cấp cho mỗi slot có thể khác nhau giữa các slot. Nếu bạn đã nhận nhiều slot, hãy đảm bảo sử dụng đúng thông tin đăng nhập tương ứng với slot bạn đang thực hiện.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Slot Credentials | Thông tin đăng nhập của slot | Tài khoản test riêng được gán cho từng slot |
| Credential Visibility | Khả năng hiển thị thông tin đăng nhập | Chỉ hiển thị sau khi claim và khi cycle Active |
