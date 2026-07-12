# Mức độ nghiêm trọng so với Giá trị (Severity vs Value)

> **Nguồn gốc**: uTest Academy / Test Cycles
> **Ngày dịch**: 2026-05-24
> **Chủ đề**: test_cycles

---

## Bản dịch

### Mức độ nghiêm trọng/Mức độ ưu tiên của một lỗi là gì?
Mức độ nghiêm trọng/ưu tiên (severity/priority) thể hiện sự ảnh hưởng của một lỗi (bug) đối với sản phẩm xét về khía cạnh mức độ tác động. Tester có thể tự đánh giá và chọn mức độ nghiêm trọng thích hợp nếu thông tin này không được đề cập trong tài liệu tổng quan chu kỳ (cycle overview).

Tại uTest, chúng tôi chia lỗi thành 4 mức độ nghiêm trọng:

* **Mức độ nghiêm trọng Thấp (Low severity)**: Một sự cố nhỏ ảnh hưởng đến khả năng sử dụng của sản phẩm, nhưng không cản trở các tính năng hoặc chức năng cốt lõi.
  * Ví dụ: Lỗi lệch hàng của trang hoặc hình ảnh.
  * Lỗi nội dung, lỗi chính tả, ngữ pháp hoặc dấu câu.
* **Mức độ nghiêm trọng Trung bình (Medium severity)**: Một sự cố nhỏ có mức độ tác động trung bình, có thể ảnh hưởng đến các tính năng hoặc chức năng cốt lõi, nhưng có phương án thay thế (workaround) và không làm gián đoạn quá trình kiểm thử tiếp theo hoặc việc phát hành sản phẩm.
  * Ví dụ: Hiệu năng hệ thống bị suy giảm rõ rệt.
  * Sự bất tiện nhỏ đối với khách hàng nhưng đã có sẵn phương án thay thế tạm thời.
* **Mức độ nghiêm trọng Cao (High severity)**: Một sự cố lớn có tác động đáng kể, cản trở các tính năng và chức năng cốt lõi, đồng thời có thể làm dừng các hoạt động kiểm thử tiếp theo hoặc làm chậm trễ việc phát hành sản phẩm.
  * Ví dụ: Chức năng cốt lõi bị ảnh hưởng nghiêm trọng.
  * Một dịch vụ không khả dụng đối với một nhóm khách hàng cụ thể.
* **Mức độ nghiêm trọng Nghiêm trọng (Critical severity)**: Một sự cố cực kỳ nghiêm trọng có tác động rất lớn, làm tê liệt các tính năng và chức năng cốt lõi, bắt buộc phải dừng mọi hoạt động kiểm thử và phải được khắc phục trước khi phát hành sản phẩm.
  * Ví dụ: Ứng dụng bị sập (crash) hoặc bị treo (freeze).
  * Vi phạm bảo mật hoặc rò rỉ thông tin cá nhân/quyền riêng tư.

### Giá trị của một lỗi (Bug Value) là gì?
Giá trị của lỗi (Bug Value) thể hiện mức độ hữu ích của lỗi đó đối với khách hàng. Khách hàng là người duy nhất quyết định giá trị lỗi của bạn. Mức thanh toán cho lỗi (bug payout rates) phụ thuộc hoàn toàn vào giá trị của lỗi, chứ không phụ thuộc vào mức độ nghiêm trọng của lỗi.

Có 4 mức giá trị lỗi:

* **Somewhat Valuable (Won't Fix) - Có giá trị phần nào (Không sửa)**: Lỗi này hợp lệ nhưng khách hàng không quan tâm hoặc không có kế hoạch sửa chữa nó.
* **Somewhat Valuable - Có giá trị phần nào**: Lỗi này có một số tác động nhất định đến sản phẩm và mang lại một phần giá trị cho khách hàng.
* **Very Valuable - Rất có giá trị**: Lỗi này có tác động đáng kể đến sản phẩm và rất có giá trị đối với khách hàng.
* **Exceptionally Valuable - Cực kỳ có giá trị**: Lỗi này có tác động cực kỳ nghiêm trọng đến sản phẩm và bắt buộc phải sửa chữa. Những lỗi này mang lại giá trị đặc biệt lớn cho khách hàng.

### Lưu ý quan trọng:
* **Mức độ nghiêm trọng không đồng nghĩa với Giá trị.** Quyết định hoàn toàn nằm ở phía khách hàng. Ví dụ, một lỗi mà tester xếp loại là Thấp (Low) vẫn có thể cực kỳ có giá trị đối với khách hàng.
* Các lỗi mà tester cho là Nghiêm trọng (Critical) hoặc Cao (High) không nhất thiết là có giá trị cao đối với khách hàng. Ví dụ:
  * Lỗi phát sinh ngoài phạm vi (out of scope) của chu kỳ kiểm thử.
  * Lỗi mà người dùng cuối gần như không bao giờ gặp phải trong thực tế.
  * Lỗi chỉ xảy ra trên môi trường phát triển (development) hoặc môi trường thử nghiệm (staging) mà không xuất hiện trên môi trường vận hành thực tế (production / live).
  * Lỗi là kết quả của việc kiểm thử áp lực (stress test) hoặc kiểm thử ngẫu nhiên phá hoại (monkey test).

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Bug Value | Giá trị của lỗi | Đánh giá của khách hàng quyết định mức thanh toán |
| Stress Testing | Kiểm thử áp lực | Kiểm thử khả năng chịu tải cực hạn của hệ thống |
| Monkey Testing | Kiểm thử ngẫu nhiên | Kiểm thử bằng cách nhập dữ liệu ngẫu nhiên phá hoại |
