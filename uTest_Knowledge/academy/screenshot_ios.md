# Hướng dẫn chụp ảnh màn hình trên iOS

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Chụp ảnh màn hình (Taking the Screenshot)
Thực hiện theo các bước sau để chụp ảnh màn hình:

- **Các mẫu iPhone đời cũ (có nút Home vật lý)**: Nhấn đồng thời nút **Home** và nút **Nguồn/Sườn (Power/Side)**.
- **Các mẫu iPhone đời mới (không có nút Home)**: Nhấn đồng thời nút **Nguồn** và nút **Tăng âm lượng (Volume Up)**.

Quy trình này được mô tả chi tiết trên trang web của Apple, bạn có thể truy cập các liên kết hướng dẫn chính thức dưới đây:
- [Chụp ảnh màn hình trên iPhone](https://support.apple.com/vi-vn/102610)
- [Chụp ảnh màn hình trên iPad](https://support.apple.com/vi-vn/102507)

---

### Khoanh vùng nổi bật ảnh chụp màn hình (Highlighting the Screenshot)

#### Cách 1: Sử dụng công cụ vẽ hình Markup có sẵn trên iOS
Chúng ta sẽ sử dụng công cụ **Markup** được tích hợp sẵn trên hệ điều hành iOS để khoanh vùng nổi bật lỗi trên ảnh chụp màn hình.

- Mở ứng dụng **Ảnh (Photos)** và chọn ảnh chụp màn hình vừa chụp.
- Chạm vào biểu tượng **Sửa (Edit)**, sau đó chạm vào biểu tượng **Markup** hiển thị ở phía trên màn hình.
- Chạm vào nút dấu cộng **(+)** ở góc dưới cùng bên phải, sau đó chọn **Add Shape** (Thêm hình dạng): chọn hình chữ nhật hoặc hình tròn.
- Ở phía bên trái của thanh công cụ tùy chọn hiện ra, chạm vào biểu tượng **Fill** (Tô màu hình) và chọn **No Fill** (Không tô màu).
- Kế bên đó, chạm vào biểu tượng **Stroke** (Màu viền) và chọn màu Đỏ (Red) hoặc màu Vàng (Yellow).
- Vẽ hình dạng đã chọn bao quanh vị trí có lỗi (bug) để làm nổi bật lỗi đó.
- Sau khi hoàn thành, chạm vào chữ **Done** (Xong) ở góc trên bên phải màn hình hai lần để lưu ảnh chụp màn hình lại.

#### Cách 2: Sử dụng máy tính để khoanh vùng nổi bật
Thực hiện theo các bước sau:

- Chuyển ảnh chụp màn hình từ thiết bị iOS sang máy tính của bạn.
- Sử dụng một trong các phần mềm dưới đây để khoanh vùng nổi bật ảnh chụp màn hình:
  - **Paint** đối với máy tính chạy Windows.
  - **Preview** đối với máy tính chạy macOS.

*Lưu ý:* Chúng tôi giả định rằng bạn đã đọc các bài học trước đó và đã biết cách khoanh vùng nổi bật ảnh chụp màn hình bằng Paint và Preview.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Photos app | Ứng dụng Ảnh | Ứng dụng quản lý hình ảnh mặc định trên các thiết bị của Apple |
| Screenshot | Ảnh chụp màn hình | Bằng chứng dạng hình ảnh hiển thị lỗi phần mềm |
| Highlight | Khoanh vùng nổi bật | Vẽ hình/đánh dấu để chỉ rõ lỗi trên ảnh chụp màn hình |
| Paint | Paint | Ứng dụng vẽ và sửa ảnh cơ bản có sẵn trên Windows |
| Preview | Preview | Ứng dụng xem và sửa ảnh có sẵn trên macOS |
