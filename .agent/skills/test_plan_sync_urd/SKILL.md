---
name: test_plan_sync_urd
description: Skill chuyên sâu để đối soát và đồng bộ hóa danh mục tính năng (Feature List) từ tài liệu URD (docx) vào Test Plan (xlsx).
---

# Test Plan Sync from URD Skill

## Giới thiệu
Kỹ năng này giúp Senior QA/Test Lead duy trì sự nhất quán giữa tài liệu yêu cầu (URD) và kế hoạch kiểm thử (Test Plan). Nó giải quyết các vấn đề:
- **Thiếu sót tính năng:** Tự động phát hiện các Module/Feature mới trong URD nhưng chưa có trong Test Plan.
- **Sai lệch mã hóa (Code Mapping):** Phát hiện và sửa lỗi ánh xạ mã chức năng (như SA.01, PR.02, RP.03) khi URD thay đổi thứ tự.
- **Bóc tách chi tiết (Granularity):** Tự động phân rã các danh sách như danh mục API, danh mục tham số từ bảng trong URD vào các dòng chi tiết trong Test Plan.

## Cách sử dụng
Sử dụng kỹ năng này khi:
1. Có bản cập nhật URD mới (ví dụ từ v0.7 lên v0.9).
2. Cần kiểm tra xem Test Plan hiện tại đã bao phủ (cover) hết các yêu cầu trong URD chưa.
3. Cần khởi tạo cấu trúc Test Plan từ một tài liệu URD thô.

### Quy trình hành động (Workflow)
1. **Trích xuất (Extract):** Sử dụng `python-docx` để quét Layout/Heading/Table trong URD nhằm lấy danh sách Module và Feature Code (PR, SA, RP, SE...).
2. **Phân tích (Analyze):** So sánh danh sách trích xuất được với cột `Feature` hoặc `Sub-Feature` trong file `Test Plan (.xlsx)`.
3. **Báo cáo sai lệch (Reporting):** Liệt kê các điểm thiếu, các mã bị sai lệch hoặc bị nhảy số (shift).
4. **Cập nhật (Update):** Sử dụng `pandas/openpyxl` để chèn thêm dòng, cập nhật tên chức năng và duy trì định dạng cho file Test Plan.

## Yêu cầu môi trường
- **Python:** 3.8+
- **Thư viện:** `python-docx`, `pandas`, `openpyxl`

## Kịch bản (Prompts) gợi ý cho User
- *"Hãy đối soát file Test Plan v1.0 với URD v0.9 xem tôi có thiếu feature nào không."*
- *"Cập nhật danh sách API từ bảng trong phụ lục URD vào sheet Test Plan giúp tôi."*
- *"Kiểm tra và sửa lại mã SA.xx trong Test Plan cho khớp với mục II.5.4 của URD mới nhất."*

## Lưu ý quan trọng
- Luôn kiểm tra cấu trúc cột của Test Plan trước khi thực hiện ghi đè (thường là Feature, Sub-Feature, Sub-sub-feature).
- Khi có sự thay đổi thứ tự (như chèn Module vào giữa), cần cập nhật lại toàn bộ mã số phía sau để đảm bảo tính nhất quán.
