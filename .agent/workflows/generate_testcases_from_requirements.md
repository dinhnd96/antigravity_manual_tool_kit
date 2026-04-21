---
description: Quy trình Senior QA Lead phân tích yêu cầu (URD/BRD) và sinh bộ Test Case chuẩn Enterprise Level B2.
---

# Quy Trình Sinh Test Case Chuyên Sâu (End-to-End Test Case Generation)

Workflow này hướng dẫn AI phối hợp 2 kỹ năng chuyên gia để đảm bảo chất lượng kiểm thử từ khâu đọc hiểu đến khâu bàn giao.

## Giai Đoạn 1: Phân Tích & Đặc Tả Câu Hỏi (Clarification Phase)
*Sử dụng skill: `manual_requirement_analyzer`*

1. **Trích xuất & Soi Ảnh**: 
   - Nếu URD là file `.docx`, thực hiện `unzip` để lấy ảnh từ `word/media/`.
   - Đối chiếu Flowchart/UI Mockup với nội dung Text để tìm sự sai lệch.
2. **Xử lý Q&A hiện có (Nếu có)**:
   - Nếu tài liệu đã có mục **"PHẦN B: DANH SÁCH CẢNH BÁO & Q&A"** với cột "Câu trả lời của BA" đã được điền: AI **BẮT BUỘC** đọc kỹ các câu trả lời này để cập nhật vào logic nghiệp vụ tổng thể.
3. **Khai quật lỗ hổng (Loopholes)**: 
   - Tìm các điểm thiếu luồng lỗi, mâu thuẫn trạng thái hoặc mơ hồ UI.
   - Kiểm tra xem các câu trả lời của BA ở bước trên có mâu thuẫn với các phần khác của tài liệu hay không.
4. **Tóm tắt & Q&A bổ sung**: 
   - Tổng hợp Business Value và Ma trận phân quyền (đã bao gồm các điểm BA đã chốt).
   - Nếu vẫn còn điểm mù chưa được trả lời, tiếp tục sinh bảng câu hỏi Q&A bổ sung.
   - **Output**: Xuất file `.docx` báo cáo phân tích và danh sách Q&A.

> [!STRICT_CHECKPOINT]
> **DỪNG LẠI (WAIT FOR CONFIRM):** Sau khi cung cấp file báo cáo phân tích, AI phải dừng lại để bạn review. Khi bạn xác nhận "Đồng ý" (nghĩa là logic đã thông suốt), AI mới chuyển sang Giai đoạn 2.

## Giai Đoạn 2: Thiết Kế Test Case Chuẩn B2 (Design Phase)
*Sử dụng skill: `qa_test_case_generator`*

1. **Lập Ma Trận Phủ**: Liệt kê toàn bộ `BR_xx` và `UI-FUNC.xx`.
2. **Tích hợp Logic đã Clarified**: Sử dụng cả nội dung URD gốc và các câu trả lời của BA ở Giai đoạn 1 để xây dựng kịch bản.
3. **Sinh Test Case 3 Mảng (Không Trùng)**:
   - **(A) TC-BR**: Tập trung logic, 1-8 TC/BR (Happy + Negative + Boundary).
   - **(B) TC-UI**: Chỉ kiểm hành vi bề mặt UI (Điều hướng, Disabled/Enabled...).
   - **(C) Luồng E2E**: Luồng nghiệp vụ xuyên suốt.
4. **Quy Tắc Vàng (Quality Gates)**:
   - **Cấm Gộp (No-Merge)**: Tách riêng từng kịch bản, từng trạng thái để tránh sót case.
   - **Expected Result 4 lớp**: (i) Logic nghiệp vụ, (ii) UI/Toast, (iii) Trạng thái bản ghi, (iv) Output.
   - **Precondition**: Đánh số dòng 1, 2... và nêu rõ Role/Menu.
5. **Xuất file Markdown Review**: Ngay khi thiết kế xong toàn bộ Test Case, AI **BẮT BUỘC** tạo một file `.md` chứa "Bảng Test Cases Markdown hoàn chỉnh" và lưu vào thư mục dự án.
6. Cung cấp đường dẫn file `.md` (Bảng Test Cases) cho user.

> [!STRICT_CHECKPOINT]
> **DỪNG LẠI (WAIT FOR CONFIRM):** Sau khi cung cấp link file `.md` chứa bản nháp Test Case, AI phải dừng lại để bạn review. Khi bạn xác nhận "Đồng ý", AI mới chuyển sang Giai Đoạn 3 (chạy Script xuất file Excel).

## Giai Đoạn 3: Bàn Giao (Delivery Phase)

1. **Kiểm tra Traceability**: Đảm bảo mỗi BR và UI-FUNC đều có ít nhất một TC kiểm chứng.
2. **Xuất File Master**:
   - Sử dụng Script Python để sinh file `.xlsx` gồm sheet **"Test Cases"**. (21 cột dữ liệu).
3. **Thông báo**: Trả lời bằng Tiếng Việt, cung cấp đường dẫn file Word và file Excel.

> [!IMPORTANT]
> **Lưu ý về Logic**: Tuyệt đối không copy-paste "Expected Result" chung chung. Phải bám sát logic của từng kịch bản cụ thể.

