# 🛡️ CHIẾN LƯỢC KIỂM THỬ DỰA TRÊN RỦI RO (RISK-BASED TESTING - RBT)

Tài liệu này hướng dẫn cách áp dụng RBT để tối ưu hóa nguồn lực cho Team Test tinh nhuệ, giúp tăng chất lượng và đảm bảo dự án thành công để nhận thưởng cuối năm.

---

## 1. TỔNG QUAN VỀ RBT
RBT là phương pháp kiểm thử tập trung vào những phần có nguy cơ lỗi cao nhất và gây thiệt hại lớn nhất cho hệ thống. Thay vì test dàn trải 100% mọi thứ một cách bằng nhau, chúng ta dành 80% thời gian cho 20% những tính năng quan trọng nhất.

### 📐 Công thức tính điểm rủi ro (Risk Score):
> **Risk Score = Khả năng xảy ra lỗi (Probability) x Mức độ ảnh hưởng (Impact)**

### 📊 Ma trận ưu tiên (Risk Matrix):
| | **Impact Thấp** | **Impact Cao** |
|---|---|---|
| **Probability Cao** | Ưu tiên 3 (Tự động hóa/AI) | **Ưu tiên 1 (Test kỹ nhất)** |
| **Probability Thấp** | Ưu tiên 4 (Test khi còn thời gian) | Ưu tiên 2 (Test luồng chính) |

---

## 2. NHẬN DIỆN RỦI RO TRONG DỰ ÁN
Hãy rà soát dự án dựa trên các tiêu chí sau:
*   **Kỹ thuật:** Phức tạp không? Dùng công nghệ mới hay cũ? Đã từng lỗi ở đây chưa?
*   **Nghiệp vụ:** Tính năng này có liên quan đến Tiền (Financial)? Có ảnh hưởng đến Bảo mật (Security)? Có phải tính năng cốt lõi (Core) không?

---

## 3. CÁCH PHỐI HỢP VỚI ANTIGRAVITY (AI) TRONG RBT
Bạn có thể ra lệnh cho AI để hỗ trợ phân tích:
1.  **Phân tích URD tìm điểm mù:** *"Đọc đoạn nghiệp vụ này và tìm ra những 'lỗ hổng' hoặc các kịch bản hiếm gặp (Edge cases) có thể làm hệ thống treo."*
2.  **Đánh giá mức độ phức tạp:** *"Dựa trên Business Rules này, hãy xếp hạng độ khó khi code và test từ 1-10."*
3.  **Tối ưu bộ Test:** *"Tôi có 100 test case. Hãy chọn ra 20 case quan trọng nhất dựa trên tiêu chí rủi ro thanh toán để tôi chạy Regression."*

---

## 4. KẾ HOẠCH HÀNH ĐỘNG CHO TEST LEAD
1.  **Bước 1 (Planning):** Cùng BA xác định chỉ số Impact cho từng module.
2.  **Bước 2 (Risk Assessment):** Cùng Dev Lead đánh giá chỉ số Probability.
3.  **Bước 3 (Test Design):** Dùng AI sinh Test Case tập trung cho các vùng Đỏ (High Risk).
4.  **Bước 4 (Reporting):** Báo cáo cho Sếp về tiến độ test dựa trên độ phủ rủi ro (Risk Coverage).

---
> *"Làm ít nhưng đúng chỗ, dự án mới ổn định và phần thưởng mới cao!"*
