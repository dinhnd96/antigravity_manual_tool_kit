# 🗓️ NGHỆ THUẬT REVIEW CÔNG VIỆC DÀNH CHO TEST LEAD

> "Quản lý vi mô (Micromanagement) giết chết sự sáng tạo. Bỏ bê (Negligence) sinh ra rủi ro. Chìa khóa là Review đúng thời điểm."

Một trong những trăn trở lớn nhất của Test Lead là: *Khi nào nên kiểm tra tiến độ của team để không mang tiếng là "soi mói", nhưng vẫn đảm bảo chất lượng dự án?*

Thay vì review tùy hứng, hãy áp dụng mô hình Review theo vòng đời Agile/Scrum dưới đây:

---

## 1. 🌅 DAILY REVIEW (REVIEW HÀNG NGÀY - TÍNH BẰNG PHÚT)

**Mục tiêu:** Nắm bắt tình hình tổng quan, tháo gỡ khó khăn (Blockers). **Không phải để bắt bẻ.**

*   **Thời điểm:** Trong buổi họp Daily Standup (10-15 phút mỗi sáng).
*   **Trọng tâm Câu hỏi:**
    *   Hôm qua em làm được gì? (VD: Đã viết xong khung Test Case cho API Đăng nhập).
    *   Hôm nay em định làm gì? (VD: Tiếp tục viết Test Case cho API Thanh toán).
    *   **Quan trọng nhất:** Em có đang bị kẹt (block) ở đâu không? (VD: Dev chưa xong API, BA chưa chốt requirement).
*   **Hành động của Lead:** Ghi nhận và đi giải quyết các "Blockers" cho team (liên hệ Dev, ép BA chốt tài liệu). *Tuyệt đối không đi sâu vào chi tiết kỹ thuật ở bước này.*

---

## 2. ⏳ MILESTONE/PHASE REVIEW (REVIEW THEO GIAI ĐOẠN - TÍNH BẰNG GIỜ)

**Mục tiêu:** Kiểm soát chất lượng thực tế của công việc trước khi nó đi quá xa. Đây là lúc bạn cần "nhúng tay" vào.

*   **Thời điểm:**
    *   **Khoảng 30% tiến độ:** (VD: Khi bạn Junior vừa viết xong 10 Test Case đầu tiên).
        *   *Tại sao?* Để kiểm tra xem bạn đó có hiểu sai tư duy, sai format tài liệu không. Chỉnh sửa ngay lúc này rất dễ. Đừng đợi đến khi viết xong 100 Test Case mới bắt sửa lại từ đầu.
    *   **Khoảng 80% tiến độ:** (VD: Chuẩn bị chốt bộ Test Case, hoặc chuẩn bị kết thúc đợt test).
        *   *Tại sao?* Để rà soát lại các rủi ro (Risk-Based Testing). Đảm bảo các luồng P0/P1 không bị bỏ sót.
*   **Hành động của Lead:** Đọc lướt tài liệu, comment trực tiếp vào tài liệu (Jira/Excel/Confluence). Nếu thấy sai lệch nghiêm trọng, gọi điện/họp nhanh 15 phút để định hướng lại.

---

## 3. 🏁 FINAL & RETROSPECTIVE REVIEW (REVIEW TỔNG KẾT - TÍNH BẰNG BUỔI)

**Mục tiêu:** Đánh giá kết quả cuối cùng, đúc rút kinh nghiệm (Lessons Learned).

*   **Thời điểm:** Cuối Sprint hoặc sau khi Release tính năng.
*   **Trọng tâm:**
    *   **Defect Leakage:** Có lỗi nào lọt ra ngoài không? Tại sao? Quá trình test đã bỏ sót ở đâu?
    *   **Chất lượng Log Bug:** Bug viết đã rõ ràng chưa? (Tỷ lệ Rejection Rate là bao nhiêu?)
    *   **Test Coverage:** Đã cover đủ rủi ro chưa?
*   **Hành động của Lead:** Khen ngợi những điểm tốt trước toàn team. Phân tích lỗi sai dưới góc độ *Quy trình* (Tại sao quy trình của chúng ta để lọt lỗi này?) thay vì chỉ trích cá nhân.

---

## 💡 KỸ NĂNG NHÌN NGƯỜI (TÙY CHỈNH THEO NHÂN SỰ)

Sự khác biệt của một Lead giỏi nằm ở chỗ bạn **không review ai cũng giống ai**:

1.  **Với Junior/Fresher (Người mới):**
    *   *Mức độ Review:* Xát sao (Tight/Micromanage hợp lý).
    *   *Chiến thuật:* Review chia nhỏ (30% - 60% - 90%). Bắt buộc họ phải đưa ra bản nháp/outline trước khi làm chi tiết.
2.  **Với Mid-level (Người đã có kinh nghiệm):**
    *   *Mức độ Review:* Vừa phải (Moderate).
    *   *Chiến thuật:* Tập trung vào Review ở mức 80% tiến độ để kiểm tra độ Cover Rủi ro (Edge Cases). Giao cho họ nhiều không gian tự quyết.
3.  **Với Senior (Chuyên gia/Key Member):**
    *   *Mức độ Review:* Trao quyền (Empowerment).
    *   *Chiến thuật:* Chỉ cần quản lý kết quả đầu ra (Final Review) và định hướng chiến thuật lúc giao việc. Thi thoảng nhờ họ Review chéo (Peer Review) cho các bạn Junior để giảm tải cho Lead.

---

**Tóm lại:** Bí quyết là áp dụng **"Review sớm (Shift-Left), Review theo điểm rơi (Milestones), và Review tùy theo đối tượng (Nhân sự)"**.

---
*Tài liệu thuộc bộ kỹ năng [Test Lead Master Guide](./TEST_LEAD_MASTER_GUIDE.md)*
