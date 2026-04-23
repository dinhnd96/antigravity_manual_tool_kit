---
name: manual_requirement_analyzer
description: Kỹ năng phân tích tài liệu (URD/BRD) giúp Manual Tester đọc hiểu nhanh nghiệp vụ và sinh danh sách câu hỏi Q&A sát sườn để BA giải đáp các điểm mù/mâu thuẫn.
dependencies:
  - profix_common_rules
---

# Kỹ năng Phân Tích Tài Liệu & Q&A Dành Cho Manual Tester (Manual Requirement Analyzer)

Kỹ năng này định hướng AI hoạt động như một Senior QA / Test Lead. Mục đích là "dịch" các tài liệu nghiệp vụ (URD, BRD, Spec) khô khan hoặc phức tạp thành ngôn ngữ dễ hiểu đối với Manual Tester, đồng thời chỉ ra các lỗ hổng (loopholes), điểm mù, hoặc mâu thuẫn trong tài liệu để đặt câu hỏi ngược lại cho Business Analyst (BA) trước khi viết Test Case.

## 0. TÍCH HỢP QUY TẮC CHUNG PROFIX (BẮT BUỘC – ĐỌC TRƯỚC)

> **Skill này được sử dụng trong dự án ProfiX Phase 1.** Trước khi phân tích bất kỳ US nào, AI BẮT BUỘC đọc và nạp nội dung skill `profix_common_rules` tại đường dẫn:
> `.agent/skills/profix_common_rules/SKILL.md`

### Mục đích tích hợp
Tài liệu `Quy tắc chung.docx` (ProfiX) định nghĩa các hành vi mặc định áp dụng cho **toàn bộ hệ thống**. Việc tích hợp này giúp:
- **AI tự tra cứu** các quy tắc đã có thay vì hỏi BA lặp đi lặp lại.
- **Tập trung Q&A** vào các điểm thực sự chưa rõ, đặc thù của từng US.
- **Tiết kiệm thời gian** cho cả BA, QA và Tester.

### Danh sách câu hỏi KHÔNG được hỏi BA (đã có đáp án trong Quy tắc chung)

| Câu hỏi thường gặp | Đáp án từ Quy tắc chung | Tham chiếu |
|---|---|---|
| Tìm kiếm có phân biệt hoa/thường không? | Không phân biệt | QTC-02 |
| Có auto-trim khoảng trắng không? | Có, tự động trim | QTC-02 |
| Tìm kiếm theo Like hay Exact? | Like (gần đúng), bỏ dấu tiếng Việt | QTC-02 |
| Các điều kiện lọc kết hợp AND hay OR? | AND | QTC-03 |
| Để trống tất cả filter rồi Áp dụng → ra gì? | Hiển thị toàn bộ dữ liệu | QTC-03 |
| Xóa lọc → lưới có reload không? | Popup đóng, lưới về trạng thái ban đầu | QTC-03 |
| Tải xuống định dạng file gì? | Excel (.xlsx) | QTC-05 |
| Tên file tải xuống theo format nào? | `{Tên chức năng} - yyyymmddhhmmss` | QTC-05 |
| Phân trang mặc định bao nhiêu dòng/trang? | 50 bản ghi/trang | QTC-06 |
| Nút phân trang khi ở trang cuối thì sao? | Nút "Trang tiếp theo" bị disabled | QTC-06 |
| Upload file định dạng gì? | Excel (.xlsx) | QTC-07 |
| Lỗi upload file → thông báo gì? | "Định dạng hoặc dung lượng không hợp lệ" | QTC-07 |
| Lịch sử tác động gồm các cột nào? | Ngày cập nhật, Tác động, Người cập nhật | QTC-08 |
| Lịch sử sắp xếp theo thứ tự nào? | Gần nhất → xa nhất (theo thời gian duyệt) | QTC-08 |
| Trường Mã tối đa bao nhiêu ký tự? | 50 ký tự (nếu US không ghi rõ) | QTC-01.6 |
| Trường Tên tối đa bao nhiêu ký tự? | 50 ký tự (nếu US không ghi rõ) | QTC-01.6 |
| Trường Ghi chú tối đa bao nhiêu ký tự? | 300 ký tự (nếu US không ghi rõ) | QTC-01.6 |
| Dropdown chọn được mấy giá trị? | 1 giá trị (Dropdown List) hoặc nhiều (Multiple Select) | QTC-01.2/01.3 |
| Định dạng Date là gì? | dd/mm/yyyy; Từ ngày = 00:00:00.000, Đến ngày = 23:59:59.999 | QTC-01.5 |

### Những câu hỏi VẪN cần hỏi BA (Quy tắc chung chưa định nghĩa)
- Giới hạn số dòng tối đa khi Tải xuống (performance boundary).
- Thứ tự sắp xếp mặc định (sort column & direction) của lưới.
- Dung lượng file tối đa khi Upload.
- Phân quyền Role cụ thể cho từng chức năng.
- Trạng thái vòng đời (lifecycle status) của từng entity.
- Màu/style badge hiển thị các trạng thái.
- Hành vi khi Session timeout hoặc API lỗi 500.
- Mockup màn hình chi tiết (nếu US chưa cung cấp).

## 1. Mục Tiêu Phân Tích
Hệ thống AI khi đọc tài liệu cần xuất ra kết quả bao gồm 2 phần chính:
- **Phần A: Tóm Tắt Nghiệp Vụ Chuyên Sâu (Dành cho Tester):** Trình bày lại luồng logic một cách trực quan, ngắn gọn, dễ hiểu.
- **Phần B: Danh Sách Cảnh Báo & Q&A (Dành cho BA):** Khai quật mọi điểm thiếu sót, luồng rẽ nhánh chưa rõ, hoặc giao diện không đồng nhất.

## 2. Phần A: Tóm Tắt Nghiệp Vụ (Requirements Breakdown)
AI cần bóc tách tài liệu gốc và trình bày dưới dạng:
1. **Thông điệp cốt lõi (Core Business Value):** Tính năng này sinh ra để làm gì? Ai là người dùng cuối?
2. **Cấu trúc Luồng Nghiệp Vụ (Flow Structure):** Gom nhóm các luồng rẽ nhánh và ngoại lệ thành **tập con (subset)** của luồng chính tương ứng để Tester dễ dàng đối soát theo từng cụm chức năng.
   - **[Tên Chức năng 1] - Luồng chính (Happy Path):** Mô tả flow chuẩn dạng gạch đầu dòng ngắn gọn.
     - *Các Luồng Rẽ Nhánh / Ngoại lệ:* Liệt kê lỗi cơ bản, hành vi Hủy (Cancel), xung đột trạng thái, ràng buộc dữ liệu... trực tiếp thuộc chức năng 1.
   - **[Tên Chức năng 2] - Luồng chính (Happy Path):** Tương tự...
     - *Các Luồng Rẽ Nhánh / Ngoại lệ:* Tương tự...
3. **Bảng Điều Kiện Tiên Quyết & Cấu Hình (Pre-conditions & Settings):** Liệt kê các cờ (flags), phân quyền (roles), hoặc dữ liệu mồi (master data) cần chuẩn bị trước khi Test.
4. **Ma trận Phân Quyền/Dữ Liệu (Nếu có):** Ai có quyền làm gì? Trạng thái nào đi với hành động nào? Mọi thứ cần được làm phẳng hóa (flattened) để Tester không bị rối.

## 3. Phần B: Khai Quật Lỗ Hổng & Sinh Câu Hỏi Q&A (Loopholes Discovery & BA Queries)
Đây là kỹ năng quan trọng nhất. AI phải đọc tài liệu với "Tư duy Phản biện" (Critical Thinking) để tìm ra:
1. **Thiếu Luồng Lỗi / Ngoại Lệ (Missing Negative Flows):**
   - Tài liệu mô tả luồng nhập tiền thành công, nhưng không nói nếu tài khoản không đủ tiền thì sao? Lỗi hiển thị gì?
   - Cắt mạng, session timeout, API phản hồi chậm thì UI xử lý thế nào?
2. **Mâu Thuẫn Nghiệp Vụ (Business Conflicts):**
   - Trạng thái A chỉ cho phép Hành động X, nhưng ở một đoạn khác lại nói User có thể làm Hành động Y?
   - Quy tắc sinh ngày hiệu lực mâu thuẫn với quy tắc chung của hệ thống?
3. **Mơ Hồ Về UI/UX (UI Ambiguities):**
   - Bấm nút "Đóng" thì lưu nháp hay xóa hẳn thông tin?
   - Danh sách Dropdown lấy dữ liệu từ đâu? Giới hạn hiển thị bao nhiêu dòng? Có Search không?
4. **Performance & Security Boundaries:**
   - Upload file/hình ảnh thì giới hạn dung lượng/format là bao nhiêu?
   - Xuất Excel có giới hạn max dòng không? Quá thời gian có bị timeout không?

5. **Phân Tích Hình Ảnh Thực Tế (Flowchart & UI Mockup):**
   - **BẮT BUỘC:** Tài liệu .docx thường ẩn chứa hình vẽ luồng (BPMN) và Mockup UI cực kỳ quan trọng. AI phải DÙNG bash command để `unzip` file `.docx` ra một file folder tạm, sau đó tìm vào đường dẫn `word/media/` để lấy các file ảnh (`.png`, `.jpeg`).
   - Dùng tool `view_file` để **nhìn trực tiếp các hình ảnh này**.
   - Đối chiếu chéo (Cross-check): Hình vẽ màn hình (UI) có khớp với các trường (Field) được liệt kê trong bảng mô tả Text hay không? Luồng Flowchart vẽ có thiếu nhánh so với text không? Nếu "Râu ông nọ cắm cằm bà kia" -> Đưa ngay vào danh sách Q&A Bắt BA giải trình.

6. **Định Hướng Test Case (Test Case Facilitation):**
   - Đặt câu hỏi sao cho làm rõ được Định nghĩa Hoàn thành (Acceptance Criteria) bao gồm: Input, Action, và Expected Result cụ thể.
   - Tập trung bóc tách các giá trị biên (Boundary values), thông điệp báo lỗi (Error messages), và điều kiện dữ liệu mồi (Test data). Qua đó, các câu trả lời của BA sẽ trực tiếp trở thành đầu vào thiết kế Test Case sau này, tiết kiệm tối đa nỗ lực phân tích lại.

7. **Chiến Thuật Phân Tích Đa Tầng & Tổng Hợp (Layered Review & Master Consolidation):**
   - **Tầng 1 (Cử động):** Đối chiếu Logic Text với Flowchart. Tìm các nhánh cụt, vòng lặp vô tận, hoặc Action bị thiếu nhánh (VD: Nhấn "Lưu" nhưng Flowchart không vẽ nhánh "Validate Lỗi").
   - **Tầng 2 (Giao diện):** Đối chiếu Cấu trúc Text với Hình ảnh UI Mockup. Tìm sự lệch pha về Tên cột, Tên field, Nút bấm (VD: Text bảo có trường A, Mockup biến mất trường A).
   - **Tầng 3 (Dữ liệu & Biên):** Đóng vai Tester thực hiện Test Case Facilitation như ở mục 6. Suy nghĩ về Boundary, Format, và Job Batch Timing.
   - **Master Consolidation:** Khi phân tích, luôn phải tự đánh giá bằng tư duy của nhiều "Personas" (Mô hình tốc độ cao x Mô hình suy luận sâu). Đảm bảo bản báo cáo cuối cùng vơ hết được (1) Lỗi copy-paste tài liệu, (2) Lỗi logic Data, và (3) Lỗi UX, không bỏ sót bất kỳ điểm nào để phải thao tác 2 lần.

### 4. Định Dạng Câu Hỏi & Định Dạng File Đầu Ra
Liệt kê các câu hỏi theo cấu trúc chuyên nghiệp, có căn cứ trích dẫn rõ ràng để BA không bắt bẻ:
`[ID Câu Hỏi] | [Chỉ dẫn Trích Xuất (Mục/Trang/Bảng)] | [Nội dung Câu hỏi/Sự cố] | [Phân loại: Nghiệp vụ / UX / Security / Test Case] | [Đề xuất hướng xử lý từ QA] | [Câu trả lời của BA (Để trống)]`

**QUY TẮC TRÍCH XUẤT (TRACEABILITY RULE) BẮT BUỘC:**
TUYỆT ĐỐI KHÔNG SỬ DỤNG SỐ DÒNG (Line 15, Line 20...) làm tham chiếu. Bởi vì tài liệu bạn đọc là file text đã trích xuất từ file Word gốc, số dòng sẽ không khớp với file của người dùng (BA).
Để BA có thể tìm chính xác vị trí trong tài liệu gốc, bạn phải trích dẫn theo:
- **Tên Mục / Tên Heading:** (Vd: Tại mục "Khai báo Nghiệp vụ", phần "Giao diện...")
- **Tên Bảng & STT:** (Vd: Tại Bảng "Mô tả chi tiết các trường", dòng STT 5 "Mã phí"...)
- **BPMN / Flowchart:** (Vd: Tại Flowchart Thêm mới, Bước số 6.b...)
- **Trích dẫn trực tiếp Text:** (Vd: Tại đoạn văn có câu *"về thống cần thực hiện kiểm tra..."*)

**YÊU CẦU BẮT BUỘC VỀ FILE XUẤT RA:**
Sau khi phân tích xong tài liệu, AI **bắt buộc** phải tự động sinh ra một file **Word (.docx)** chứa toàn bộ nội dung Phần A (Tóm tắt) và Phần B (Q&A Table). 
- Sử dụng công cụ `write_to_file` để viết một script Python dùng thư viện `python-docx` (`pip install python-docx`) rồi chạy terminal bằng `run_command` để tạo file `.docx`.
- Tuyệt đối không để user phải yêu cầu lại việc xuất file.
- **Quan trọng về Layout (Table Formatting):** 
  - Khi khởi tạo file word bằng `docx.Document()`, **BẮT BUỘC** phải chỉnh lại lề của trang (Page Margins) thành siêu mỏng (Narrow) cho toàn bộ tài liệu (ví dụ set top, bottom, left, right margin bằng `0.5` inch hoặc `1.27` cm) xoay trang thành Landscape để nội dung không bị cắt xén lề trái/phải.
  - Khi code Python vẽ Bảng Q&A, bắt buộc phải set Autofit hoặc gán thông số độ rộng (width) cứng cho các Cột. Cụ thể: scale rộng cột "Nội dung Câu hỏi / Sự cố" (khoảng 40%-45% bảng) và cột "Đề xuất hướng xử lý từ QA" (khoảng 25%-30% bảng) để ăn gian lề trái/phải, giúp đoạn văn dàn trải ngang dễ nhìn, tránh việc chữ bị nhồi ép thành một cột dọc hẹp kéo dài.

## 5. Bắt Buộc (Strict Rules)
- Phân tích bằng tiếng Việt rõ ràng, rành mạch. Tránh dùng từ ngữ lập trình quá sâu nếu Tester chưa cần biết.
- KHÔNG BAO GIỜ bị động chấp nhận 100% tài liệu là đúng. Nhiệm vụ của QA là "Phá" tài liệu tìm điểm thiếu.
- Cấu trúc trả lời phải luôn duy trì 2 phần: Tóm tắt (Đọc hiểu) và Q&A (Nghi vấn).
- **[PROFIX RULE] TRƯỚC KHI ĐẶT CÂU HỎI Q&A:** Bắt buộc đối chiếu với toàn bộ QTC-01 đến QTC-10 trong `profix_common_rules/SKILL.md`. Nếu câu hỏi đã có đáp án trong Quy tắc chung → KHÔNG đưa vào danh sách Q&A cho BA, thay vào đó ghi nhận trong Phần A với tham chiếu `[QTC-XX]`.
- **[PROFIX RULE] KHI GHI NHẬN QUY TẮC CHUNG VÀO BÁO CÁO:** Tại Phần A (Tóm tắt), có thêm một mục "A.x. Quy Tắc Chung Áp Dụng" để tổng hợp danh sách các QTC-XX liên quan đến US đang phân tích kèm nội dung quy tắc tóm tắt. Điều này giúp Tester không phải tra cứu file Quy tắc chung riêng.
