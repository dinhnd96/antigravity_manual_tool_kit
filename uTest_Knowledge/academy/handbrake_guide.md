# Hướng dẫn sử dụng phần mềm HandBrake

> **Nguồn gốc**: uTest Academy
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: academy

---

## Bản dịch

### Giới thiệu chung (Introduction)
HandBrake là một trình chuyển mã video (video transcoder) mã nguồn mở mạnh mẽ được thiết kế để chuyển đổi và tối ưu hóa các tệp video. Hỗ trợ trên cả Windows, macOS và Linux, phần mềm này tương thích với nhiều định dạng và codec khác nhau, làm cho nó trở thành một công cụ đa năng cho việc nén video, chuyển đổi định dạng và điều chỉnh chất lượng. Với các tính năng như xử lý hàng loạt (batch processing), cấu hình mẫu tùy chỉnh (presets) và các tùy chọn mã hóa video nâng cao, HandBrake được sử dụng rộng rãi để cải thiện tính tương thích của video, giảm kích thước tệp và nâng cao chất lượng phát lại trên các thiết bị khác nhau.

Có năm mục đích chính mà phần mềm HandBrake có thể đáp ứng khi bạn làm việc trong các dự án uTest:
1. Thay đổi định dạng tệp tin (Changing File Format)
2. Nén dung lượng video (Compressing Videos)
3. Loại bỏ tiếng ồn nền / âm thanh (Removing Background Noise)
4. Điều chỉnh hướng xoay của video (Adjusting the Video's Orientation)
5. Sửa lỗi méo hình (Fixing Anamorphic Video Issues)

---

### Cài đặt HandBrake (Installing HandBrake)
Thực hiện theo các bước sau để bắt đầu sử dụng HandBrake:
- Tải xuống và cài đặt HandBrake từ trang chủ chính thức của ứng dụng.
- Đối với macOS, hãy tham khảo hình ảnh hướng dẫn cài đặt phần mềm đi kèm trên uTest Academy.

---

### Thay đổi định dạng tệp tin (Change File Format)
- Mở HandBrake và kéo thả tệp video vào phần mềm.
- Cách thay đổi thư mục lưu trữ và định dạng đầu ra mặc định:
  - **Trên Windows**:
    - Nhấp chọn **Tools** và chọn **Preferences**.
    - Tại tab **Output Files**:
      - Thay đổi đường dẫn mặc định (**Default Path**) thành Desktop hoặc thư mục bất kỳ bạn muốn lưu tệp.
      - Thiết lập **MP4 File Extension** thành **Always use MP4** (Luôn sử dụng đuôi .mp4).
  - **Trên macOS**:
    - Nhấp chọn **HandBrake** trên thanh Menu và chọn **Settings...** (Cài đặt).
    - Tại tab **Output Files**, thiết lập **Default MP4 Extension** thành **.mp4**.

---

### Nén dung lượng video (Compress the Video File)
- Để nén tệp video, nhấp vào menu **Preset** (Cấu hình mẫu) và chọn một cấu hình mẫu phù hợp.
- Lựa chọn này tùy thuộc vào video của bạn, dung lượng video và yêu cầu của chu kỳ kiểm thử. Nếu dung lượng video đã nhỏ (dưới 5 MB), bạn không cần nén tệp trừ khi bạn không thể tải tệp lên báo cáo lỗi hoặc test case do giới hạn tải của chu kỳ kiểm thử (tùy thuộc vào thiết lập của chu kỳ).
- Chúng tôi khuyên bạn nên chọn cấu hình **Very Fast 720p 30** hoặc **Very Fast 1080p**.

---

### Loại bỏ âm thanh khỏi tệp video (Remove Audio from the Video)
Để loại bỏ âm thanh (tiếng ồn nền) khỏi video, hãy làm theo các bước sau:
- **Trên Windows**:
  - Chuyển sang tab **Audio** (Âm thanh) và nhấp chọn nút **Clear** (Xóa) hoặc biểu tượng **X** ở phía bên phải của track âm thanh cần xóa.
- **Trên macOS**:
  - Mở tab **Audio**.
  - Nhấp chọn track âm thanh hiển thị trong danh sách (ví dụ: *0: Unknown (AAC LC)*).
  - Chọn **None** (Không chọn).

---

### Điều chỉnh hướng xoay của video (Fix Video Orientation)
Để sửa lại hướng xoay của video nếu bản ghi bị ngược hoặc xoay sai hướng, hãy thực hiện theo các bước sau:
- Mở tab **Dimensions** (Kích thước).
- Điều chỉnh góc xoay (**Rotation**) để video đầu ra hiển thị đúng hướng mong muốn.
- *Ví dụ:* Nếu video bị ghi ngược đầu xuống đất, bạn có thể thiết lập xoay **180** độ.

---

### Sửa lỗi méo hình Anamorphic (Fix Anamorphic Video Issues)
Video méo hình (Anamorphic video) là định dạng video có tỷ lệ khung hình rộng hơn nhưng bị bóp méo theo chiều ngang để vừa với định dạng ghi tiêu chuẩn. Hãy tưởng tượng nó giống như việc bạn kéo dài một dải dây cao su theo chiều ngang và ghi lại hình ảnh bị kéo giãn đó. Loại video này có thể do một số thiết bị iOS và các công cụ khác tạo ra, do đó việc sửa lỗi biến dạng này là rất quan trọng để đảm bảo video hiển thị bình thường trên nền tảng.

Để sửa lỗi video méo hình bằng HandBrake, làm theo các bước sau:
- Mở tab **Dimensions**.
- Tại mục **Resolutions & Scaling** (Độ phân giải & Tỷ lệ), thiết lập tùy chọn **Anamorphic** thành **None** hoặc **Off** (Tắt).
- Điều chỉnh độ phân giải nếu cần thiết.

---

### Kết xuất video (Encoding the Video)
Quá trình mã hóa/kết xuất (encoding) chuyển đổi tệp video dựa trên các cài đặt và cấu hình mẫu đã chọn, đảm bảo tối ưu hóa dung lượng nén, độ phân giải, loại bỏ lỗi méo hình và tính tương thích định dạng.
- Nhấp vào nút **Start** hoặc **Start Encode** (Bắt đầu mã hóa) trên thanh công cụ.
- Thời gian kết xuất video sẽ khác nhau tùy thuộc vào dung lượng tệp tin, cài đặt chất lượng và hiệu năng hệ thống của bạn.
- Video thành phẩm sẽ được lưu ngoài màn hình nền (desktop) hoặc thư mục lưu trữ mà bạn đã thay đổi trong mục **Save As** (Lưu dưới dạng).
- Sau khi kết xuất xong, hãy kiểm tra lại video đầu ra để đảm bảo đáp ứng đúng các yêu cầu kiểm thử.
- Hãy mở phát thử video để xác nhận độ nén, định dạng, việc sửa lỗi méo hình và chất lượng hình ảnh đã chuẩn chưa.
- Nếu cần thiết, hãy lặp lại quá trình mã hóa với các tùy chỉnh được điều chỉnh lại.

---

### Cấu hình tùy chỉnh thiết lập sẵn (Handbrake Custom Presets)
HandBrake Custom Presets là các thiết lập được cấu hình sẵn bởi người dùng nhằm tự động hóa quy trình chuyển đổi tệp video. Thay vì phải điều chỉnh các tùy chọn một cách thủ công mỗi lần kết xuất video, bạn chỉ cần chọn một cấu hình sẵn có mà bạn đã tạo, và hệ thống sẽ tự động tải các thiết lập bạn đã định nghĩa.

Việc tạo các cấu hình tùy chỉnh thiết lập sẵn cho các thông số bạn sử dụng thường xuyên sẽ giúp tiết kiệm tối đa thời gian cấu hình phần mềm mỗi khi bạn cần xuất video cho báo cáo lỗi hoặc test case.

#### Lưu cấu hình tùy chỉnh thiết lập sẵn
Thực hiện các bước sau để tạo một cấu hình tùy chỉnh thiết lập sẵn trên HandBrake:
1. Mở HandBrake và nhập một video bất kỳ để thiết lập các cài đặt mẫu.
2. Chọn một cấu hình mẫu cơ bản (base preset) phù hợp với nhu cầu của bạn (ví dụ: *Very Fast 720p 30* hoặc *Very Fast 1080p 30*).
3. Thực hiện các thay đổi đối với tùy chọn theo nhu cầu của bạn, chẳng hạn như xóa bỏ âm thanh, sửa lỗi méo hình, v.v.
4. Nhấp chọn **Presets** từ thanh menu, sau đó chọn **Add Preset...** hoặc **New Preset...** (Thêm cấu hình mẫu mới).
5. Nhập Tên (Name) và Mô tả (Description) cho cấu hình mẫu đó, nên đặt tên trùng khớp với các cài đặt cấu hình để dễ nhận biết.
6. Thiết lập loại bỏ âm thanh khỏi cấu hình mẫu để mặc định loại bỏ âm thanh trong video:
   - Tại trường **Audio** (Âm thanh), nhấp chọn **Selection Behavior...** (Hành vi lựa chọn).
   - Trong mục *Audio encoder settings for each selected track:* (Cấu hình bộ mã hóa âm thanh cho mỗi track đã chọn), nhấp chọn track âm thanh hiển thị và xóa nó đi:
     - **Trên Windows**: Nhấp vào nút **Clear** (Xóa) ở bên phải.
     - **Trên macOS**: Nhấp vào nút dấu trừ **(-)**.
   - Nhấp chọn **Save** hoặc **OK**.
7. Nhấp chọn nút **Add** (Thêm) để lưu cấu hình mẫu này lại.
8. Lặp lại các bước trên để tạo thêm các cấu hình mẫu tùy chỉnh khác nếu bạn có nhu cầu.

#### Thiết lập cấu hình tùy chỉnh làm mặc định (Default Preset)
Với các cấu hình tùy chỉnh sẵn có, bạn sẽ không cần phải điều chỉnh lại thiết lập cho mỗi lần mã hóa hoặc chuyển đổi. Bạn có thể tiết kiệm thời gian hơn nữa bằng cách đặt một cấu hình tùy chỉnh cụ thể làm mặc định, tránh việc phải chuyển đổi liên tục giữa các cấu hình mẫu.

Để đặt một cấu hình tùy chỉnh làm mặc định, hãy làm theo các bước sau:
1. Mở HandBrake và kéo thả một video vào.
2. Từ mục **Preset**, chọn cấu hình tùy chỉnh bạn muốn cài làm mặc định.
3. Nhấp chọn **Presets** trên thanh menu và chọn **Make Default** (Đặt làm mặc định) hoặc **Set Current as Default** (Đặt cấu hình hiện tại làm mặc định).
4. Đóng phần mềm HandBrake và mở lại.
5. Kiểm tra mục cấu hình đã chọn trong phần **Presets** để xác nhận nó đã trở thành cấu hình mặc định.

---

### Lưu ý quan trọng:
- Bỏ qua bước **Nén dung lượng video** nếu video của bạn không cần nén (dung lượng nhỏ và không bị giới hạn).
- Bỏ qua bước **Loại bỏ âm thanh** nếu video của bạn không chứa bất kỳ tiếng ồn nền nào.
- Bỏ qua bước **Điều chỉnh hướng xoay** nếu video đã được quay đúng hướng.
- Bỏ qua bước **Sửa lỗi méo hình Anamorphic** nếu video của bạn không gặp hiện tượng méo hình.
- Luôn đảm bảo tệp video đầu ra được lưu ở định dạng **.mp4**.

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Handbrake | Handbrake | Ứng dụng nén video mã nguồn mở |
| Anamorphic | Hiện tượng méo hình | Hiện tượng video bị bóp méo chiều ngang trên một số thiết bị |
| Encoding | Mã hóa video / Kết xuất video | Quy trình chuyển đổi định dạng và nén tệp video |
| Preset | Cấu hình mẫu | Các thiết lập được cấu hình sẵn để sử dụng nhanh |
| Screen Recording | Video quay màn hình | Bằng chứng dạng video ghi lại quá trình kiểm thử |
| Terms of Use | Điều khoản Sử dụng | Quy chế và chính sách bắt buộc tuân thủ của uTest |
| Desktop | Màn hình nền | Giao diện màn hình chính của hệ điều hành máy tính |
| PII (Personally Identifiable Information) | Thông tin nhận dạng cá nhân | Bất kỳ thông tin nào nhận dạng được một cá nhân |
