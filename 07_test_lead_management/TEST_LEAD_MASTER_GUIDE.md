# 📘 CẨM NANG QUẢN LÝ ĐỘI NGŨ KIỂM THỬ (TEST LEAD MASTER GUIDE)
*Dành riêng cho Test Leader (Quy mô 20+ Testers) — Chiến lược Agile/DevOps & AI*

---

## 🚀 TÓM TẮT DÀNH CHO QUẢN LÝ (EXECUTIVE SUMMARY)
Trong thế giới Testing thay đổi chóng mặt, vai trò của bạn đã dịch chuyển:
- **TỪ:** Người giao việc, viết test case, đếm lỗi.
- **SANG:** Người quản trị rủi ro, tối ưu hóa công cụ (AI/Automation) và lãnh đạo chiến lược.

**Nguyên tắc "Vàng":** Chất lượng là trách nhiệm tập thể. Công việc của bạn là thiết lập sân chơi (Chiến lược, Quy trình) để Quality được đảm bảo tự nhiên.

---

## 🏛️ PHẦN 1: CHIẾN LƯỢC & QUẢN TRỊ RỦI RO (STRATEGY & RISK)

### 1. Phân biệt 3 tầng tài liệu:
- **Test Policy:** Tầm nhìn ("Chất lượng là trên hết").
- **Test Strategy:** Cách làm cho dự án ("Dùng Katalon, chạy Auto mỗi đêm").
- **Test Plan:** Thực thi chi tiết ("Huy làm tính năng A, thời hạn thứ 6").

### 2. Risk-Based Testing (RBT) — "Lá bùa" sinh tồn:
Khi thiếu người/thời gian, hãy dùng công thức: **Risk Score = Khả năng xảy ra × Mức độ ảnh hưởng.**
- Tập trung 80% nguồn lực vào các luồng P0 (Ví dụ: tính phí ngân hàng, bảo mật).
- Sẵn sàng buông bỏ các rủi ro thấp (P3) để cứu vãn tiến độ.

---

## 🏃 PHẦN 2: QUY TRÌNH AGILE/DEVOPS & CHỈ SỐ (PROCESS & METRICS)

### 1. Chiến lược "Shift-Left":
QA phải tham gia từ lúc thảo luận yêu cầu để bắt lỗi "ngay từ trong trứng nước".
- **Review Requirements sớm:** Loại bỏ 80% lỗi logic trước khi dòng code đầu tiên được viết.
- **The Three Amigos:** QA + BA + Dev thống nhất kịch bản Acceptance trước khi code.
- **Chi tiết:** Xem thêm tại [Shift-Left Strategy](./SHIFT_LEFT_STRATEGY.md) và [Quy trình Shift-Left Thực Chiến](./SHIFT_LEFT_PROCESS.md).

### 2. Chỉ số đo lường (Metrics that Matter):
Các chỉ số không chỉ để báo cáo, mà là để ra quyết định và chứng minh giá trị QA.
- **Defect Leakage Rate:** Lỗi lọt ra ngoài là chỉ số đánh giá team QA thực chiến nhất.
- **Test Coverage:** Độ bao phủ rủi ro/nghiệp vụ (P0/P1 phải đạt 100%).
- **MTTR (Mean Time To Repair):** Tốc độ Dev sửa lỗi quan trọng không kém tốc độ QA tìm lỗi.
- **Chi tiết:** Xem thêm tại [QA Metrics Guide](./QA_METRICS_GUIDE.md).

### 3. Definition of Done (DoD) chuẩn Ngân hàng:
- 0 lỗi Nghiêm trọng (P0/P1).
- 100% P0 kịch bản Auto (Katalon) pass.
- Release Note có chữ ký xác nhận của PO.
- **Chi tiết:** Đọc phân tích sâu tại [Banking DoD Guide](./BANKING_DOD_GUIDE.md)

---

## 👥 PHẦN 3: QUẢN TRỊ CON NGƯỜI (PEOPLE MANAGEMENT)

### 1. Lãnh đạo team 20+ Tester:
- **Gaps Analysis:** Luôn biết ai giỏi Manual, ai giỏi Kỹ thuật để phân chia "trận địa" đúng người đúng việc.
- **Nghệ thuật Review:** Review đúng thời điểm (Daily, 30%, 80%) và tùy biến theo năng lực (Junior vs Senior). Xem chi tiết tại [Task Review Guide](./TASK_REVIEW_GUIDE.md).
- **Feedback:** Hãy đóng góp ý kiến mang tính xây dựng, tập trung vào giải pháp thay vì lỗi lầm cá nhân.
- **Coaching:** Dành 20% thời gian để đào tạo Junior lên Senior để giảm tải cho chính bạn.

### 2. Quản trị Stakeholders:
- Biết cách nói "KHÔNG" một cách khéo léo thông qua Báo cáo Rủi ro (Risk Report).
- Luôn có bằng chứng (số liệu) khi thảo luận với Dev Lead hoặc Project Manager.

---

## 🤖 PHẦN 4: CÔNG NGHỆ & TƯƠNG LAI (AI/AUTOMATION)

### 1. Chiến lược Automation "Bậc thang":
- **P0 (Smoke):** Auto 100%, chạy mọi lúc code thay đổi.
- **P1 (Regression):** Auto 80%, chạy hàng đêm.
- **Manual:** Dành cho thăm dò (Exploratory) và tính năng mới thay đổi liên tục.

### 2. Cuộc cách mạng AI trong Testing:
- Dùng AI để **sinh dữ liệu khổng lồ** (Data Generation).
- Dùng AI để **Audit chất lượng bộ Test Case**.
- **Test cho AI:** Học cách kiểm thử độ tin cậy của các hệ thống AI.

---

## 🚨 CHECK-LIST XL KHỦNG HOẢNG (DÀNH CHO BẠN NGAY BÂY GIỜ)

1. [ ] **Dừng viết Test Case chi tiết:** Chuyển sang Check-list/Mindmap.
2. [ ] **Họp nhanh PO/Dev:** Làm rõ các điểm mập mờ của tài liệu ngay lập tức.
3. [ ] **Chốt kịch bản release tối thiểu:** Thuyết phục sếp chỉ release những gì đã ổn định.
4. [ ] **Phó thác cho Katalon:** Để nó tự chạy các bài test quy trình cũ (Regression).
5. [ ] **Báo cáo rủi ro ngay:** Đừng im lặng chịu trận, hãy phát đi tín hiệu cảnh báo sớm.

---
*Chúc bạn (Test Lead) vững tay lái vượt qua mọi "bão" dự án!*
