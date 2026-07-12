# Kiến thức cơ bản về video quay màn hình

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Video quay màn hình (screen recording) là gì?
Video quay màn hình (screen recording), còn được gọi là screencast, là bản ghi kỹ thuật số kết quả hiển thị trên màn hình máy tính hoặc thiết bị di động. Video quay màn hình được sử dụng để hiển thị các bước thực hiện thực tế, giúp người xem hiểu và tái hiện lại được lỗi (bug).

Trước hết, hãy cùng tìm hiểu các quy tắc mà một video quay màn hình bắt buộc phải tuân theo. Sau đó, chúng ta sẽ học cách ghi lại màn hình thiết bị.

---

### Quy tắc quay màn hình (Screen recording rules)

- **Không lẫn tiếng ồn (No noise)**: Hãy chắc chắn tắt tiếng micro (mute microphone) để loại bỏ tiếng ồn xung quanh. Bạn chỉ nên ghi lại giọng nói của mình nếu điều đó được yêu cầu cụ thể bởi chu kỳ kiểm thử (test cycle).
- **Hiển thị toàn màn hình (Entire screen)**: Tương tự như ảnh chụp màn hình, hãy đảm bảo video quay màn hình của bạn hiển thị toàn bộ màn hình, bao gồm cả thanh chứa URL của trình duyệt nếu bạn đang kiểm thử một trang web.
- **Phải khớp với các bước thực hiện**: Video cần khớp với các bước được liệt kê trong phần Các bước thực hiện (actions performed) và bắt đầu từ trang web kiểm thử hoặc từ lúc mở ứng dụng.
- **Chỉ sử dụng định dạng mp4**: Tất cả video quay màn hình phải được lưu và tải lên ở định dạng **.mp4**. Không tải lên video quay màn hình ở bất kỳ định dạng nào khác.
- **Độ dài ngắn gọn**: Luôn cố gắng giữ cho video quay màn hình ngắn gọn và **dưới 1 phút**. Tuy nhiên, video có thể dài hơn 1 phút miễn là bạn chỉ hiển thị các bước bắt buộc cần thiết để tái hiện lỗi.

---

### Những điều cần lưu ý (Things to remember)

- **Một video cho mỗi báo cáo lỗi**: Không tải lên nhiều hơn một video quay màn hình trong một báo cáo lỗi trừ khi thực sự cần thiết.
- **Nén các tệp dung lượng lớn**: Đôi khi, dung lượng video có thể rất lớn, hãy luôn nén chúng trước khi tải lên. Chúng ta sẽ học cách nén video bằng phần mềm HandBrake trong bài học sắp tới.
- **Sử dụng camera ngoài để ghi hình**: Bạn chỉ nên sử dụng thiết bị bên ngoài như máy ảnh hoặc điện thoại thứ hai để quay lại màn hình thiết bị đang test nếu điều đó được yêu cầu cụ thể trong chu kỳ kiểm thử hoặc khi không thể thực hiện quay màn hình bằng phần mềm.
- **Xác nhận video có thể phát được**: Luôn xác minh video tải lên có thể phát được bình thường trên nền tảng.
- **Không lưu trữ trên đám mây (cloud)**: Video quay màn hình không được phép lưu trữ trên đám mây. Chúng chỉ được phép lưu trên máy cục bộ của tester và sau đó tải trực tiếp lên báo cáo lỗi trong chu kỳ kiểm thử.
- **Làm mờ thông tin nhận dạng cá nhân (PII)**: Không hiển thị thông tin PII trong video quay màn hình của bạn để tránh vi phạm quy định GDPR, trừ khi có hướng dẫn khác.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Screen Recording | Video quay màn hình | Bằng chứng dạng video ghi lại quá trình kiểm thử để chứng minh lỗi |
| Handbrake | Handbrake | Ứng dụng nén video mã nguồn mở |
| GDPR | Quy định Bảo vệ Dữ liệu Chung | Luật EU về bảo vệ dữ liệu cá nhân |
| PII (Personally Identifiable Information) | Thông tin nhận dạng cá nhân | Bất kỳ thông tin nào nhận dạng được một cá nhân |
| Actions Performed | Các bước thực hiện | Các bước thao tác của tester để tái hiện lỗi |
