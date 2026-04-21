---
description: Quy trình định hướng AI đóng vai trò Manager/Orchestrator để kích hoạt tuần tự các Skill phân tích yêu cầu và sinh Test Case.
---

# Quy Trình Orchestrator: Sinh Test Case Từ Tài Liệu Yêu Cầu

Workflow này đóng vai trò là "Người điều phối" (Orchestrator). Trách nhiệm của AI khi chạy Workflow này KHÔNG PHẢI là định nghĩa lại cách làm việc, mà là **GỌI ĐÚNG SKILL (Các Chuyên Gia)** và **TUÂN THỦ CÁC ĐIỂM DỪNG (Checkpoints)** để luân chuyển thông tin.

Để đảm bảo kết quả hoàn hảo, tại mỗi giai đoạn, AI BẮT BUỘC phải đọc nội dung hướng dẫn của `SKILL.md` tương ứng và làm ĐÚNG 100% sự chỉ đạo bên trong Skill đó. Không tự ý cắt xén, thêm thắt, hay thay đổi định dạng đầu ra của Skill.

## Giai Đoạn 1: Phân Tích Nhận Diện Lỗ Hổng & Cắm Chốt Q&A
**Chuyên gia (Skill) phụ trách:** `requirements_analyzer`

1. Khi được cung cấp URD/FSD, AI **gọi ngay** kỹ năng `requirements_analyzer` (đọc file `.agent/skills/requirements_analyzer/SKILL.md` nếu cần).
2. Áp dụng nghiêm ngặt các hướng dẫn phân tích 5 chiều, sinh Checklist ẩn (LOG-xxx) quy định trong Skill.
3. Thông báo nội dung Báo cáo phân tích và Danh sách Q&A cho User.

> [!STRICT_CHECKPOINT]
> **DỪNG LẠI CHỜ DUYỆT (WAIT):** Sau khi cung cấp Báo cáo & Q&A, AI BẮT BUỘC phải báo "Tôi đã xong Giai đoạn 1" và dừng lại hoàn toàn. Chỉ khi User cung cấp câu trả lời (từ BA) hoặc xác nhận "Đồng ý chuyển tiếp", AI mới được phép sang Giai Đoạn 2.

## Giai Đoạn 2: Sinh & Bàn Giao File Test Case Master
**Chuyên gia (Skill) phụ trách:** `qa_test_case_generator`

1. Lấy Tài liệu URD + Toàn bộ câu trả lời Q&A có được từ Giai đoạn 1 làm **Input đầu vào**.
2. AI **gọi** kỹ năng `qa_test_case_generator` (đọc file `.agent/skills/qa_test_case_generator/SKILL.md` nếu cần).
3. Thi hành trọn vẹn workflow nội tại của Skill này, đảm bảo:
   - Áp dụng triệt để Quy tắc Expected Result 4 lớp, No-Merge, Trace_ID.
   - Bỏ qua các bước làm vỡ luồng (Ví dụ: Không sinh file Test Case Markdown review unless user yêu cầu).
   - Đi thẳng tới bước Viết Script Python -> Chạy sinh file Excel `.xlsx` cuối cùng.

## Giai Đoạn 3: Dọn Dẹp (Cleanup Phase)
Sau khi quá trình sinh file Excel thành công:
1. Cung cấp đường dẫn file Test Case `.xlsx` cho User.
2. Chủ động tìm và xóa bỏ các script `.py` tạm thời (đã dùng để sinh file Excel) và các file log/debug rác (nếu có) tuân theo <RULE[user_global]>.
3. Báo cáo dọn dẹp và đóng quy trình.
