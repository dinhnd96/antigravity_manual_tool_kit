# 🛸 LÀM CHỦ GOOGLE ANTIGRAVITY CHO ĐỘI NGŨ TEST & BA

Antigravity không đơn thuần là một Chatbot; đây là một **AI Agent** có khả năng thay bạn hành động trực tiếp trên file, thư mục và trình duyệt. Tài liệu này giúp đội ngũ Test và BA tối ưu hóa quy trình làm việc hàng ngày.

---

## 📋 1. DÀNH CHO BUSINESS ANALYST (BA)
*BA tập trung vào yêu cầu (Requirement), logic và tài liệu hệ thống.*

### 🛠️ Các Prompt (Câu lệnh) Gợi Ý:
*   **Phân tích URD chuyên sâu:** 
    > *"Đọc file URD đính kèm. Hãy trích xuất danh sách các Business Rule chính và cảnh báo nếu có điểm nào mâu thuẫn hoặc thiếu sót logic (ví qua các case biên)."*
*   **Xây dựng User Story & AC:** 
    > *"Dựa trên module [X] trong URD, hãy soạn bộ User Stories chuẩn kèm theo Acceptance Criteria (AC) chi tiết cho từng luồng nghiệp vụ."*
*   **Tham chiếu thị trường:** 
    > *"Hãy dùng trình duyệt tìm hiểu cách các hệ thống ERP hàng đầu xử lý logic [Y]. Sau đó đề xuất phương án tối ưu cho dự án của chúng ta."*

---

## 🧪 2. DÀNH CHO ĐỘI NGŨ TEST (QA/QC)
*Tester tập trung vào độ bao phủ (Coverage), tự động hóa và báo cáo lỗi.*

### 🛠️ Các Prompt (Câu lệnh) Gợi Ý:
*   **Sinh Test Case tự động:** 
    > *"Đọc URD version 0.9. Hãy tạo bộ Test Case (Positive & Negative) cho module mới. Lưu kết quả thành bảng Markdown hoặc file CSV."*
*   **Cập nhật hồi quy (Regression Update):** 
    > *"Đây là URD bản mới so với bản cũ. Hãy quét bộ Test Case hiện có tại [Đường dẫn] và chỉ ra chính xác các Case nào cần cập nhật hoặc xóa bỏ."*
*   **Hỗ trợ Automation:** 
    > *"Hãy viết script Playwright (Javascript) cho luồng đăng ký tài khoản. Yêu cầu tuân thủ cấu trúc Page Object Model đã có trong folder `/tests/`."*
*   **Phân tích nguyên nhân lỗi:** 
    > *"Dựa trên file log/ảnh màn hình đính kèm, hãy phân tích luồng dữ liệu và đề xuất các bước tái hiện lỗi (Steps to Reproduce)."*

---

## 🤝 3. CÁCH CỘNG TÁC HIỆU QUẢ (COLLABORATION)

1.  **Sử dụng Knowledge Items (KIs):** Khi AI đúc kết được một quy trình hay hoặc giải quyết được một bài toán khó, hãy ra lệnh: *"Lưu kinh nghiệm này vào KI 'Logic_Tinh_Phi_BHYT' để cả team cùng tham khảo sau này."*
2.  **Quản lý Artifacts:** Yêu cầu AI lưu bản vẽ Mermaid, bảng so sánh hoặc code vào folder chung của dự án thay vì chỉ chat qua lại.
3.  **Hỏi về "Context":** Thay vì giải thích lại, chỉ cần nói: *"Dựa trên những gì chúng ta đã làm ở File X và Buổi họp Y, hãy thực hiện bước tiếp theo..."*

---

## 💡 MẸO TỐI ƯU TÀI NGUYÊN (RESOURCES)
*   **Chỉ định cụ thể:** Chỉ định rõ tên file và số dòng cần đọc để AI xử lý nhanh hơn.
*   **Lập kế hoạch trước:** Đối với tác vụ lớn, hãy bảo AI: *"Hãy lập kế hoạch (Implementation Plan) trước, tôi duyệt xong bạn mới làm."*
*   **Dùng Browser Subagent:** Khi cần dữ liệu thực tế từ internet thay vì dữ liệu cũ trong "não bộ" của AI.

---
> *"Antigravity không chỉ trả lời câu hỏi, nó cùng bạn xây dựng sản phẩm."*
