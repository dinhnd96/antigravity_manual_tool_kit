# 📊 QA METRICS THAT MATTER: ĐO LƯỜNG CHẤT LƯỢNG THỰC CHUYẾN

> "Bạn không thể cải thiện những gì bạn không đo lường được." (Peter Drucker)

Dành cho Test Lead, các chỉ số không chỉ để báo cáo, mà là để **ra quyết định** và **chứng minh giá trị** của team QA với Ban Giám đốc (Management).

---

## 1. CÁC CHỈ SỐ VỀ HIỆU QUẢ KIỂM THỬ (CORE QA METRICS)

### 🚀 A. Defect Leakage Rate (Tỷ lệ lỗi lọt ra ngoài) - QUAN TRỌNG NHẤT
- **Công thức:** `(Lỗi tìm thấy trên Prod / Tổng số lỗi) x 100%`
- **Ý nghĩa:** Đánh giá năng lực thực chiến của QA.
- **Mục tiêu:** Càng thấp càng tốt (Dưới 5% là xuất sắc). Nếu chỉ số này cao, cần xem xét lại bộ Test Case hoặc môi trường Test.

### 🎯 B. Test Coverage (Độ bao phủ)
- **Không chỉ là số lượng Test Case.** Nó phải là bao phủ:
    - **Risk Coverage:** Bao nhiêu % rủi ro cao (P0) đã được test?
    - **Requirement Coverage:** Bao nhiêu % yêu cầu nghiệp vụ đã có kịch bản test?
- **Mục tiêu:** 100% đối với các yêu cầu P0/P1.

### 🧪 C. Defect Rejection Rate (Tỷ lệ lỗi bị từ chối)
- **Công thức:** `(Số lỗi Dev reject / Tổng số lỗi QA log) x 100%`
- **Ý nghĩa:** Đánh giá chất lượng log bug của QA. Nếu quá cao (>15%), QA đang tốn thời gian log những lỗi không phải lỗi, hoặc mô tả không rõ ràng.

---

## 2. CÁC CHỈ SỐ VỀ VẬN HÀNH (OPERATIONAL METRICS)

### 🛠️ D. MTTR (Mean Time To Repair - Thời gian sửa lỗi trung bình)
- **Ý nghĩa:** Đo lường sự phối hợp giữa QA và Dev. Bug được sửa càng nhanh, vòng lặp Release càng ngắn.
- **Mục tiêu:** Giảm dần theo từng Sprint.

### 🤖 E. Automation Coverage (Độ bao phủ tự động hóa)
- **Công thức:** `(Số test case đã Auto / Tổng số test case có thể Auto) x 100%`
- **Mục tiêu:** Đừng cố đạt 100%. Hãy tập trung Auto 100% cho Regression (Kiểm thử hồi quy) và Smoke Test.

---

## 3. CÁCH BÁO CÁO (FOR STAKEHOLDERS)

| Đối tượng | Họ cần xem gì? |
| :--- | :--- |
| **Project Manager** | Tiến độ (Progress), Các lỗi "Blocker" gây chậm trễ. |
| **Product Owner** | Độ bao phủ nghiệp vụ, Các lỗi ảnh hưởng đến trải nghiệm người dùng. |
| **CTO / Director** | Tỷ lệ lỗi Prod (Leakage), Hiệu quả đầu tư vào Automation (ROI). |

---

## 💡 CHIẾN LƯỢC CỦA TEST LEAD XỊN

1.  **Đừng đo lường để trừng phạt:** Hãy dùng chỉ số để tìm ra lỗ hổng quy trình.
2.  **Dashboard hóa:** Thay vì gửi file Excel nhàm chán, hãy dùng Jira Dashboard hoặc PowerBI để hiển thị chỉ số trực quan.
3.  **Tập trung vào "Actionable Metrics":** Chỉ số đó giúp bạn thay đổi điều gì? (Ví dụ: MTTR cao -> Cần họp lại với Dev Lead để tối ưu quy trình fix bug).

---
*Tài liệu thuộc bộ kỹ năng [Test Lead Master Guide](./TEST_LEAD_MASTER_GUIDE.md)*
