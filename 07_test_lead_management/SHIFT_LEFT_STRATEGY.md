# 🛡️ CHIẾN LƯỢC SHIFT-LEFT: CHẤT LƯỢNG TỪ "TRỨNG NƯỚC"

> "Phát hiện lỗi ở giai đoạn Yêu cầu (Requirements) rẻ hơn 10-100 lần so với khi đã đi vào Sản xuất (Production)."

---

## 1. SHIFT-LEFT LÀ GÌ?
**Shift-Left** là triết lý đưa các hoạt động kiểm thử (Testing) về phía **bên trái** của vòng đời phát triển phần mềm (SDLC) - tức là thực hiện sớm nhất có thể.

Thay vì đợi Code xong mới Test (Truyền thống), chúng ta Test ngay từ khi:
- Thảo luận yêu cầu (URD/BRD).
- Thiết kế hệ thống (Architecture/Design).
- Đang viết Code (Unit Test/Peer Review).

---

## 2. TẠI SAO PHẢI SHIFT-LEFT? (LỢI ĐỐI VỚI TEST LEAD)

1.  **Tiết kiệm chi phí (Cost Efficiency):** Sửa lỗi khi còn trên giấy chỉ mất vài phút thảo luận. Sửa lỗi trên Production mất hàng tuần và ảnh hưởng uy tín.
2.  **Giảm áp lực cuối Sprint:** QA không còn bị "dồn toa" vào 2 ngày cuối cùng của Sprint.
3.  **Cải thiện chất lượng Code:** Khuyến khích Dev viết Code dễ kiểm thử hơn (Testable Code).
4.  **Rút ngắn Time-to-Market:** Phát hiện lỗi sớm giúp chu kỳ Release diễn ra trơn tru.

---

## 3. CÁC HOẠT ĐỘNG TRỌNG TÂM (CORE PRACTICES)

### 📂 A. Kiểm thử Tĩnh (Static Testing) - Quan trọng nhất!
- **Review Requirements:** QA đọc tài liệu nghiệp vụ cùng BA/PO. Tìm các mâu thuẫn ngay từ đầu.
- **Review Design:** Đảm bảo kiến trúc hỗ trợ tốt cho Automation và Performance.

### 🤝 B. Quy tắc "The Three Amigos"
- QA + BA + DEV ngồi lại trước khi bắt đầu Code bất kỳ tính năng nào để thống nhất kịch bản Acceptance.

---

## 🚀 TÓM TẮT CHO BẠN
Shift-Left không đơn thuần là một kỹ thuật, nó là một **Văn hóa**. Với vai trò Test Lead, bạn là người cầm lái để dịch chuyển văn hóa này.

---
*Tài liệu thuộc bộ kỹ năng [Test Lead Master Guide](./TEST_LEAD_MASTER_GUIDE.md)*
