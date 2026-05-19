---
name: manual_requirement_analyzer
description: Kỹ năng phân tích tài liệu (URD/BRD) giúp Manual Tester đọc hiểu nhanh nghiệp vụ và sinh danh sách câu hỏi Q&A sát sườn để BA giải đáp các điểm mù/mâu thuẫn.
dependencies:
  - profix_common_rules
  - ai_deterministic_config
---

# Kỹ năng Phân Tích Tài Liệu & Q&A Dành Cho Manual Tester (Manual Requirement Analyzer)

Kỹ năng này định hướng AI hoạt động như một Senior QC / Test Lead. Mục đích là "dịch" các tài liệu nghiệp vụ (URD, BRD, Spec) khô khan hoặc phức tạp thành ngôn ngữ dễ hiểu đối với Manual Tester, đồng thời chỉ ra các lỗ hổng (loopholes), điểm mù, hoặc mâu thuẫn trong tài liệu để đặt câu hỏi ngược lại cho Business Analyst (BA) trước khi viết Test Case.

## 0. CẤU HÌNH HỆ THỐNG & TÍCH HỢP (BẮT BUỘC ĐỌC TRƯỚC)

### 0.1 TÍCH HỢP QUY TẮC CHUNG PROFIX
> **Skill này được sử dụng trong dự án ProfiX Phase 1.** Trước khi phân tích bất kỳ US nào, AI BẮT BUỘC đọc và nạp nội dung skill `profix_common_rules` tại đường dẫn:
> `.agent/skills/profix_common_rules/SKILL.md`

### Mục đích tích hợp
Tài liệu `Quy tắc chung.docx` (ProfiX) định nghĩa các hành vi mặc định áp dụng cho **toàn bộ hệ thống**. Việc tích hợp này giúp:
- **AI tự tra cứu** các quy tắc đã có thay vì hỏi BA lặp đi lặp lại.
- **Tập trung Q&A** vào các điểm thực sự chưa rõ, đặc thù của từng US.
- **Tiết kiệm thời gian** cho cả BA, QC và Tester.

### 0.2 CHỐNG VƯỢT TOKEN
> Tuân thủ rule `rules/token_safe_output.md` (auto-load). Khi phân tích URD/BRD:
- **Bước đầu tiên:** Phân loại độ phức tạp (S/M/L/XL) dựa trên số lượng module, câu hỏi Q&A, và test case dự kiến.
- **Level ≥ L:** BẮT BUỘC lập WBS (Work Breakdown Structure) trước khi thực thi.
- **Chế độ thực thi mặc định:** ✋ **MANUAL** — luôn chờ user nói "tiếp" sau mỗi phần. Chỉ chuyển sang 🔄 AUTO khi user nói rõ "auto" / "tự chạy" / "làm hết đi".
- **Output:** Ghi file thay vì in chat. Chat chỉ báo path + 2 dòng highlight.

### QUY TẮC CHỐNG LẶP (ANTI-REDUNDANCY) - KHÔNG ĐƯỢC HỎI BA NHỮNG ĐIỀU SAU:
TUYỆT ĐỐI KHÔNG đưa các câu hỏi mang tính chất "xác nhận lại" vào Phần B (Ví dụ: "Mô tả có áp dụng giới hạn 300 ký tự theo QTC-01.6 không?"). Hệ thống MẶC ĐỊNH ÁP DỤNG, không cần BA xác nhận lại!

**CẤM HỎI VỀ THÔNG BÁO LỖI:** TUYỆT ĐỐI KHÔNG đặt bất kỳ câu hỏi nào liên quan đến mã lỗi (error codes), toast thông báo lỗi, hoặc nội dung của các message lỗi (error messages). Mặc định bỏ qua các điểm mù liên quan đến text/mã lỗi này.

| Câu hỏi thường gặp | Đáp án từ Quy tắc chung | Tham chiếu |
|---|---|---|
| Tìm kiếm có phân biệt hoa/thường không? | Không phân biệt | QTC-02 |
| Có auto-trim khoảng trắng không? | Có, tự động trim | QTC-02 |
| Tìm kiếm theo Like hay Exact? | Like (gần đúng), bỏ dấu tiếng Việt | QTC-02 |
| Các điều kiện lọc kết hợp AND hay OR? | AND | QTC-03 |
| Để trống tất cả filter rồi Áp dụng → ra gì? | Hiển thị toàn bộ dữ liệu | QTC-03 |
| Xóa lọc → lưới có reload không? | Drawer đóng, lưới về trạng thái ban đầu | QTC-03 |
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
- Trạng thái vòng đời (lifecycle status) của từng entity.
- Màu/style badge hiển thị các trạng thái.
- Mockup màn hình chi tiết (nếu US chưa cung cấp).

## 1. Mục Tiêu Phân Tích & Workflow 3 Giai Đoạn
Quá trình phân tích tài liệu được chia làm **tối đa 3 Giai Đoạn (Phase)** để đảm bảo chất lượng. Phase 1.5 chỉ kích hoạt khi BA update tài liệu đáng kể.
Hệ thống AI khi đọc tài liệu cần tuân thủ workflow sau:

**PHASE 1: Khởi tạo & Đặt Câu Hỏi (Sinh Phần A + B thành 2 file riêng biệt)**
- AI đọc tài liệu và xuất ra kết quả bao gồm 2 phần, **mỗi phần là 1 file `.docx` riêng biệt**:
  - **📄 File A — Tóm Tắt Nghiệp Vụ Chuyên Sâu (Dành cho Tester):** Trình bày lại luồng logic một cách trực quan, ngắn gọn, dễ hiểu. Tên file: `USxx_PartA_Summary.docx`.
  - **📄 File B — Danh Sách Cảnh Báo & Q&A (Dành cho BA):** Khai quật mọi điểm thiếu sót, luồng rẽ nhánh chưa rõ, hoặc giao diện không đồng nhất. Tên file: `USxx_PartB_QA.docx`.
- Tự động chạy script xuất **2 file báo cáo `.docx` riêng biệt** (File A và File B).
- **DỪNG LẠI (STOP):** Yêu cầu User gửi/import nội dung câu trả lời của BA. **TUYỆT ĐỐI KHÔNG SINH PHẦN C KHI CHƯA CÓ CÂU TRẢ LỜI CỦA BA.**

**PHASE 1.5: Delta Re-analysis (Khi BA Update Tài Liệu Đáng Kể)**
> *Phase này CHỈ kích hoạt khi User thông báo BA đã update tài liệu URD/BRD kèm theo câu trả lời. Nếu BA chỉ trả lời Q&A mà không sửa tài liệu → bỏ qua Phase 1.5, đi thẳng Phase 2.*

- **Bước 1 — Phân loại mức độ thay đổi:**

| Mức độ | Dấu hiệu | Hành động |
|---|---|---|
| **Nhỏ** (<20% thay đổi) | BA sửa lỗi typo, bổ sung vài field, làm rõ mô tả | Bỏ qua Phase 1.5 → đi thẳng Phase 2 |
| **Trung bình** (20-50% thay đổi) | BA thêm/sửa module, bổ sung logic rẽ nhánh, thay đổi field đáng kể | **Kích hoạt Phase 1.5** |
| **Lớn** (>50% thay đổi) | BA viết lại gần như toàn bộ tài liệu | **Reset** — chạy lại Phase 1 từ đầu trên tài liệu mới |

- **Bước 2 — Rà soát Q&A cũ (Part B-v1):** Phân loại từng câu hỏi trong Part B-v1 vào 3 trạng thái:

| Trạng thái | Ý nghĩa | Hành động |
|---|---|---|
| ✅ `Resolved` | BA trả lời rõ ràng, tài liệu mới phản ánh đúng câu trả lời | Giữ nguyên, đánh dấu `Resolved` |
| ⚠️ `Conflict` | BA trả lời một đằng, tài liệu update một nẻo | Giữ lại + **escalate** → ghi rõ "Câu trả lời lần 1 nói X, nhưng tài liệu v2 viết Y" vào Part B-v2 |
| 🗑️ `Obsolete` | Tài liệu mới đã xóa/thay đổi hoàn toàn phần liên quan → câu hỏi không còn ý nghĩa | Đánh dấu `Obsolete`, không đưa vào Part C |

  > **QUY TẮC BẢO TOÀN NỘI DUNG GỐC (CONTENT PRESERVATION RULE):**
  > Khi merge/tổng hợp Q&A với phản hồi BA, **TẤT CẢ câu hỏi** (Resolved, Unresolved, Conflict) **BẮT BUỘC phải giữ nguyên 100% nội dung gốc** từ file Part B trước đó, bao gồm:
  > - **Trích xuất (Reference):** Giữ nguyên vị trí tham chiếu đầy đủ, KHÔNG tóm tắt/rút gọn.
  > - **Câu hỏi / Sự cố:** Giữ nguyên toàn bộ mô tả vấn đề, KHÔNG viết lại ngắn hơn.
  > - **Đề xuất từ QC:** Giữ nguyên đề xuất ban đầu.
  > - **Câu hỏi đã Resolved:** Giữ nguyên nội dung gốc + **BỔ SUNG** câu trả lời BA vào cột "Trả lời của BA". KHÔNG được xóa/thay thế nội dung câu hỏi hoặc đề xuất QC bằng câu trả lời BA.
  >
  > **VI PHẠM:** Rút gọn, tóm tắt, hoặc viết lại bất kỳ câu hỏi nào (kể cả đã resolved) khi merge sẽ gây **mất ngữ cảnh** cho Tester khi đọc lại và không trace được về tài liệu gốc.

- **Bước 3 — Sinh Part A-v2 & Part B-v2:**
  - **Part A-v2:** Sinh lại hoàn toàn dựa trên tài liệu mới (vì cấu trúc module có thể thay đổi).
  - **Part B-v2 (Supplementary Q&A):** Chỉ sinh câu hỏi **MỚI** phát sinh từ nội dung BA vừa thêm/sửa. **TUYỆT ĐỐI KHÔNG lặp lại** câu hỏi đã `Resolved` trong B-v1. Đánh ID tiếp nối B-v1 (VD: B-v1 kết thúc ở `US06-QA-04.5` → B-v2 bắt đầu từ `US06-QA-04.6` hoặc hạng mục mới).

- **Bước 4 — Xuất file tổng hợp:** File `.docx` đầu ra có cấu trúc:
  ```
  📄 USxx_Analysis_v2.docx
  ├── Phần A: Tóm tắt Nghiệp vụ (v2 — dựa trên tài liệu mới)
  ├── Phần B-v1: Q&A Round 1 (đã có câu trả lời BA, mỗi câu đánh dấu trạng thái Resolved/Conflict/Obsolete)
  └── Phần B-v2: Q&A Round 2 (câu hỏi bổ sung từ delta, cột "Trả lời của BA" để trống → chờ BA trả lời)
  ```

- **DỪNG LẠI (STOP):** Chờ BA trả lời Part B-v2. Chỉ chuyển sang Phase 2 khi B-v2 đã được trả lời.

**PHASE 2: Tổng Hợp Kịch Bản (Sinh Phần C)**
- *Chỉ kích hoạt khi User đã cung cấp nội dung câu trả lời của BA (bao gồm cả B-v1 và B-v2 nếu có).*
- AI đọc câu trả lời của BA, đối chiếu với tài liệu gốc (hoặc tài liệu v2 nếu đã qua Phase 1.5) để chốt lại các mâu thuẫn.
- **Khi tổng hợp Part B từ nhiều nguồn (file AI sinh + file BA phản hồi + file review bên ngoài):**
  - **Bước 1 — Đọc đầy đủ TẤT CẢ các file nguồn** trước khi bắt đầu tổng hợp. TUYỆT ĐỐI KHÔNG tổng hợp chỉ từ 1 file mà bỏ qua file khác.
  - **Bước 2 — Mapping câu hỏi:** Đối chiếu từng câu hỏi giữa các file, xác định trùng/thiếu/mới.
  - **Bước 3 — Áp dụng Content Preservation Rule:** Câu hỏi chưa resolved phải lấy **nguyên văn nội dung đầy đủ** từ file gốc (file có nội dung chi tiết nhất), KHÔNG được tóm tắt hay viết lại ngắn hơn.
  - **Bước 4 — Bổ sung câu hỏi mới** từ file BA phản hồi mà AI chưa phát hiện ở Phase 1.
- **Phần C: Bảng Tổng Hợp Test Case Đề Xuất (Test Case Coverage):** Sinh bảng danh sách test case bao phủ 100% tài liệu dựa trên cả URD và toàn bộ câu trả lời của BA từ mọi round Q&A (áp dụng Traceability như quy định). **LƯU Ý:** Trước khi sinh bảng, AI phải rà soát toàn bộ câu trả lời BA để phát hiện các QA có chỉ thị loại trừ (Dạng 6 — "Không xây test case cho QA này" hoặc tương đương). Các SC liên quan đến QA bị loại trừ **KHÔNG được đưa vào bảng chính**, mà phải liệt kê riêng thành **"Danh sách SC loại trừ theo phản hồi BA"** ở cuối Phần C.
- Cập nhật/sinh lại file `.docx` báo cáo tổng hợp (Gồm Phần A phiên bản mới nhất, Phần B tổng hợp tất cả round đã cập nhật câu trả lời, và Phần C).

## 2. Phần A: Tóm Tắt Nghiệp Vụ (Requirements Breakdown)
AI cần bóc tách tài liệu gốc theo chiều dọc (top-down) đúng như bố cục tài liệu để đảm bảo trace 2 chiều với FSD, và trình bày dưới dạng:
1. **Thông điệp cốt lõi (Core Business Value):** Tính năng này sinh ra để làm gì? Ai là người dùng cuối?
2. **Cấu trúc Luồng Nghiệp Vụ & Phân Bổ Module (Flow Structure & Module Mapping):** Đọc tài liệu từ trên xuống dưới, đánh dấu số thứ tự các module tính năng từ 1, 2, 3 đến n. Tên module luồng (Flow module) phải map chính xác với tên module trong tài liệu để phục vụ việc trace test case. Gom nhóm các luồng rẽ nhánh và ngoại lệ thành tập con.
   - **Module 1: [Tên Chức năng/Module 1]**
     - **Luồng chính (Happy Path):** Mô tả flow chuẩn dạng gạch đầu dòng ngắn gọn.
     - *Các Luồng Rẽ Nhánh / Ngoại lệ:* Liệt kê lỗi cơ bản, hành vi Hủy (Cancel), xung đột trạng thái, ràng buộc dữ liệu... trực tiếp thuộc Module 1.
   - **Module 2: [Tên Chức năng/Module 2]**
     - **Luồng chính (Happy Path):** Tương tự...
     - *Các Luồng Rẽ Nhánh / Ngoại lệ:* Tương tự...
3. **Bảng Điều Kiện Tiên Quyết & Cấu Hình (Pre-conditions & Settings):** Liệt kê các cờ (flags), phân quyền (roles), hoặc dữ liệu mồi (master data) cần chuẩn bị trước khi Test.
4. **Ma trận Phân Quyền/Dữ Liệu (Nếu có):** Ai có quyền làm gì? Trạng thái nào đi với hành động nào? Mọi thứ cần được làm phẳng hóa (flattened) để Tester không bị rối.

## 3. Phần B: Danh Sách Cảnh Báo & Q&A (Loopholes Discovery & BA Queries)
Đây là kỹ năng quan trọng nhất. AI phải đọc tài liệu với "Tư duy Phản biện" (Critical Thinking), áp dụng phương pháp phân tích đa tầng bên dưới, sau đó **gom nhóm tất cả câu hỏi/cảnh báo vào đúng 4 Hạng mục bắt buộc**.

### 3.1 Phương Pháp Phân Tích (Analysis Methodology)

**A. Phân Tích Hình Ảnh Thực Tế (Flowchart & UI Mockup):**
   - **BẮT BUỘC:** Tài liệu .docx thường ẩn chứa hình vẽ luồng (BPMN) và Mockup UI cực kỳ quan trọng. AI phải DÙNG bash command để `unzip` file `.docx` ra một file folder tạm, sau đó tìm vào đường dẫn `word/media/` để lấy các file ảnh (`.png`, `.jpeg`).
   - Dùng tool `view_file` để **nhìn trực tiếp các hình ảnh này**.
   - Đối chiếu chéo (Cross-check): Hình vẽ màn hình (UI) có khớp với các trường (Field) được liệt kê trong bảng mô tả Text hay không? Luồng Flowchart vẽ có thiếu nhánh so với text không? Nếu "Râu ông nọ cắm cằm bà kia" -> Đưa ngay vào danh sách Q&A Bắt BA giải trình.

**B. Định Hướng Test Case (Test Case Facilitation):**
   - Đặt câu hỏi sao cho làm rõ được Định nghĩa Hoàn thành (Acceptance Criteria) bao gồm: Input, Action, và Expected Result cụ thể.
   - Tập trung bóc tách các giá trị biên (Boundary values) và điều kiện dữ liệu mồi (Test data). Qua đó, các câu trả lời của BA sẽ trực tiếp trở thành đầu vào thiết kế Test Case sau này, tiết kiệm tối đa nỗ lực phân tích lại.
   - **Lưu ý Mapping 2 chiều:** Bất cứ điểm mù nào phát hiện cũng phải gắn nhãn nó thuộc "Module [n]" nào theo chiều dọc của tài liệu để Tester dễ dàng bổ sung Test Case vào đúng vị trí sau khi nhận được câu trả lời từ BA.

**C. Chiến Thuật Phân Tích Đa Tầng & Tổng Hợp (Layered Review & Master Consolidation):**
   - **Tầng 1 (Cử động):** Đối chiếu Logic Text với Flowchart. Tìm các nhánh cụt, vòng lặp vô tận, hoặc Action bị thiếu nhánh (VD: Nhấn "Lưu" nhưng Flowchart không vẽ nhánh "Validate Lỗi").
   - **Tầng 2 (Giao diện):** Đối chiếu Cấu trúc Text với Hình ảnh UI Mockup. Tìm sự lệch pha về Tên cột, Tên field, Nút bấm (VD: Text bảo có trường A, Mockup biến mất trường A).
   - **Tầng 3 (Dữ liệu & Biên):** Đóng vai Tester thực hiện Test Case Facilitation như ở mục B. Suy nghĩ về Boundary, Format, và Job Batch Timing.
   - **Master Consolidation:** Đảm bảo bản báo cáo cuối cùng vơ hết được (1) Lỗi copy-paste tài liệu, (2) Lỗi logic Data, và (3) Lỗi UX, không bỏ sót bất kỳ điểm nào để phải thao tác 2 lần.

### 3.2 Phân Loại Đầu Ra Bắt Buộc — 4 Hạng Mục (Mandatory Output Grouping)

> **QUY TẮC CỨNG VỀ PHÂN LOẠI:** Bảng Q&A đầu ra phải bám sát 4 Hạng mục dưới đây. **TÁCH BẠCH TỪNG CÂU HỎI RA CÁC DÒNG RIÊNG BIỆT**, tuyệt đối không gom chung nhiều câu hỏi vào cùng 1 dòng (không dùng danh sách a, b, c trong 1 ô). Mỗi dòng tương ứng với 1 vấn đề cụ thể để BA tiện trả lời. Không được bỏ trống Hạng mục nào nếu có vấn đề.

**Hạng mục 1: 🔶 Vấn đề Nghiệp vụ / Luồng xử lý (Business Logic & Flow Issues)**
   - Thiếu luồng lỗi / ngoại lệ (Missing Negative Flows): Tài liệu mô tả luồng thành công nhưng không nói khi thất bại thì sao?
   - Mâu thuẫn nghiệp vụ (Business Conflicts): Trạng thái A chỉ cho phép Hành động X, nhưng đoạn khác lại cho phép Hành động Y?
   - Luồng rẽ nhánh bị thiếu trong Flowchart so với Text (Nhánh cụt, thiếu validate).
   - Hành vi khi User thao tác đặc biệt: Chỉnh sửa mà không thay đổi, Concurrent edit, Thêm con khi cha ở trạng thái đặc biệt.
   - *Ví dụ: Quy định sửa Tên/Mô tả, luồng không hỗ trợ hủy bỏ, Batch Job xung đột với quyết định admin.*

**Hạng mục 2: 🔴 Giới hạn hệ thống & Exception Handling (System Limits & Exceptions)**
   - Giới hạn số lượng (VD: Mã tự tăng > 99 → lỗi xảy ra ở bước nào?).
   - Tham số hệ thống thay đổi (VD: tham số n tăng/giảm → ảnh hưởng gì?).
   - Edge cases khi đạt ngưỡng giới hạn: overflow, timeout, concurrency.
   - Hành vi hệ thống khi gặp lỗi không mong đợi (unexpected exception handling).
   - *Ví dụ: Giới hạn số 99, tham số n giảm rồi tăng lại, Batch Job fail giữa chừng.*

**Hạng mục 3: 🟠 Toàn vẹn dữ liệu & Ràng buộc (Data Integrity & Constraints)**
   - Ràng buộc Cascade cha-con (VD: Cha hết hiệu lực → con có bị ảnh hưởng?).
   - Ràng buộc Unique (VD: Tên/Mã có cần unique không? Scope unique ở đâu?).
   - Ràng buộc ngày tháng giữa các cấp (Ngày hiệu lực cha <= con <= cháu).
   - Soft delete vs Hard delete, xử lý khi xóa bản ghi có reference.
   - *Ví dụ: SPDV bị vô hiệu hóa khi giảm n, ràng buộc ngày cha-con, cascade trạng thái.*

**Hạng mục 4: 🔵 UI/UX & Giao diện (UI/UX & Interface Issues)**
   - Không nhất quán giữa Mockup UI và Bảng mô tả trường (tên field, thứ tự, dấu bắt buộc).
   - Thiếu trường trên Mockup so với yêu cầu nghiệp vụ (hoặc ngược lại).
   - Thiếu thông tin về giới hạn ký tự, placeholder, tooltip, trạng thái enabled/disabled.
   - Hành vi UI chưa rõ: Dropdown lấy data từ đâu? Readonly hay editable? Label chính xác?
   - *Ví dụ: Mockup hiển thị dấu (*) ở trường readonly, thiếu trường hiển thị cấp hiện tại, label không thống nhất.*

## 4. Phần C: Tổng Hợp Bảng Test Case Đề Xuất (Test Case Coverage) - CHỈ CHẠY Ở PHASE 2
*Lưu ý: Chỉ thực hiện bước này sau khi User đã cung cấp câu trả lời của BA cho Phần B.*

### QUY TẮC PHÂN TÍCH CÂU TRẢ LỜI BA (BA RESPONSE INTERPRETATION RULE) — BẮT BUỘC

> **NGUYÊN TẮC TỐI THƯỢNG:** Câu trả lời của BA là **nguồn chân lý cuối cùng (Final Source of Truth)** để chốt logic sinh Test Case. Đề xuất của QC trong Part B chỉ là **gợi ý ban đầu**, KHÔNG PHẢI quyết định cuối cùng. AI **BẮT BUỘC** phải đọc kỹ từng câu trả lời của BA và phân loại chính xác trước khi sinh SC.

**Bước 1 — Đọc kỹ và phân loại từng câu trả lời BA vào 1 trong 5 dạng:**

| Dạng | Dấu hiệu nhận biết | Hành động của AI |
|---|---|---|
| **✅ Dạng 1: BA đồng ý theo đề xuất QC** | BA **đề cập trực tiếp** đến đề xuất QC và đồng ý: "Đồng ý **đề xuất**", "Làm theo **đề xuất** QC", "OK **theo hướng QC đề xuất**" | → Lấy **đề xuất của QC** làm logic chốt để sinh SC. **CHÚ Ý:** Chỉ áp dụng Dạng 1 khi BA **nhắc đến đề xuất QC**. Nếu BA chỉ "xác nhận" một thông tin mà không đề cập đề xuất → xem Dạng 5. |
| **📝 Dạng 2: BA giải thích chi tiết (khác đề xuất QC)** | BA trả lời dài, nêu logic riêng, giải thích cách xử lý khác so với đề xuất QC | → **BỎ QUA đề xuất QC**, lấy **chính xác nội dung giải thích của BA** làm logic chốt để sinh SC. |
| **📄 Dạng 3: BA yêu cầu đọc US / tài liệu update** | BA trả lời: "Đã update US", "Xem lại tài liệu mới", "Tham khảo US đã cập nhật" | → AI **BẮT BUỘC đọc lại tài liệu US** (phiên bản mới nhất) để hiểu logic đã thay đổi, lấy **nội dung US update** làm logic chốt. KHÔNG được dùng đề xuất QC cũ. |
| **❌ Dạng 4: BA từ chối / bác bỏ đề xuất QC** | BA trả lời: "Không", "Không áp dụng", "Không cần", "Chưa cần", "Ngoài phạm vi" | → **LOẠI BỎ hoàn toàn đề xuất QC**. KHÔNG sinh SC dựa trên đề xuất bị bác bỏ. Nếu BA có nêu logic thay thế → lấy logic thay thế. Nếu BA chỉ bác bỏ mà không nêu logic thay thế → KHÔNG sinh SC cho vấn đề này. |
| **📌 Dạng 5: BA xác nhận / cung cấp thông tin cụ thể (KHÔNG đề cập đề xuất QC)** | BA trả lời bằng cách nêu thẳng thông tin hoặc quyết định mà **không nhắc đến đề xuất QC**: "Cột Ngày thu định dạng Text", "Sử dụng mã X", "Giá trị mặc định là Y" | → Lấy **chính xác thông tin BA cung cấp** làm logic chốt. **KHÔNG suy diễn** rằng BA đang đồng ý với đề xuất QC. Nếu thông tin BA cung cấp **khác** đề xuất QC → bỏ qua đề xuất QC, dùng thông tin của BA. |
| **🚫 Dạng 6: BA chỉ thị KHÔNG xây test case** | BA trả lời: "Không xây test case cho QA này", "Không cần test case", "Bỏ qua QA này", "Không cần kiểm thử" hoặc ý tương đương | → **LOẠI TRỪ HOÀN TOÀN.** KHÔNG sinh bất kỳ SC nào liên quan đến QA đó trong Phần C. Ghi nhận rõ ràng trong báo cáo: `"Loại trừ theo phản hồi BA — QA-XX: Không xây test case"`. Các SC bị loại trừ vẫn phải được liệt kê riêng (dạng danh sách loại trừ) ở cuối Phần C để đảm bảo traceability. |
| **🔗 Dạng 7: BA tham chiếu chéo US khác** | BA trả lời: "Tương tự US35", "Pending tương tự USxx", "Xử lý giống USxx", "Áp dụng logic của USxx" hoặc ý tương đương | → AI **BẮT BUỘC** tìm và đọc bộ phân tích (Part B/C) của US được tham chiếu để lấy logic chốt tương đương. Sinh SC dựa trên logic đã chốt ở US tham chiếu. Ghi Note trong SC: `"Theo phản hồi BA — tương tự USxx (QA-YY)"`. Nếu **không tìm được** bộ phân tích US tham chiếu → đánh dấu QA là `Pending` (xử lý như Dạng 8) và cảnh báo User. |
| **⏳ Dạng 8: BA chưa chốt / Pending** | BA trả lời: "Sẽ trao đổi với BE và cập nhật lại sau", "Đang xác nhận", "Sẽ cập nhật sau", "Chưa chốt", "Đang chờ confirm" hoặc ý tương đương | → **TẠM HOÃN — KHÔNG sinh SC.** Đánh dấu QA trạng thái `Pending`. Liệt kê riêng vào **"Danh sách QA chờ BA cập nhật"** ở cuối Phần C (tách biệt với danh sách loại trừ). Khi BA cập nhật sau → User cung cấp câu trả lời mới → AI sinh bổ sung SC vào bộ test case đã có. |

> **⚠️ CẢNH BÁO CHỐNG NHẦM LẪN DẠNG 1 vs DẠNG 5:**
> - BA nói *"Xác nhận cột Ngày thu là Text"* → Đây là **Dạng 5** (BA tự nêu thông tin), KHÔNG phải Dạng 1. BA đang confirm **quyết định của họ**, không phải confirm **đề xuất của QC**.
> - BA nói *"Đồng ý theo đề xuất QC, dùng định dạng Date cho cột Ngày thu"* → Đây mới là **Dạng 1** (BA đề cập và đồng ý đề xuất QC).
> - **Quy tắc phân biệt:** Nếu trong câu trả lời BA **KHÔNG xuất hiện** cụm từ "đề xuất", "theo QC", "theo hướng QC" → mặc định phân loại là **Dạng 5**, không phải Dạng 1.

> **⚠️ CẢNH BÁO CHỐNG NHẦM LẪN DẠNG 4 vs DẠNG 8:**
> - BA nói *"Không áp dụng"* → Đây là **Dạng 4** (bác bỏ dứt khoát). KHÔNG sinh SC.
> - BA nói *"Sẽ trao đổi với BE và cập nhật lại sau"* → Đây là **Dạng 8** (chưa chốt). TẠM HOÃN, chờ BA cập nhật.
> - **Quy tắc phân biệt:** Nếu BA dùng từ chỉ **thời gian tương lai** ("sẽ", "sau", "đang", "chờ") → mặc định phân loại là **Dạng 8**. Nếu BA dùng từ **phủ định dứt khoát** ("không", "không cần", "ngoài phạm vi") → **Dạng 4**.

> **🔀 XỬ LÝ CÂU TRẢ LỜI PHỨC HỢP (COMPOUND RESPONSE):**
> Một câu trả lời BA có thể chứa **nhiều dạng kết hợp** (VD: vừa bác bỏ đề xuất QC + vừa nêu logic riêng + vừa update tài liệu). Khi gặp trường hợp này:
>
> **Bước 1 — Tách (Decompose):** Phân tách câu trả lời BA thành từng thành phần riêng biệt.
> **Bước 2 — Ưu tiên:** Áp dụng logic chốt theo thứ tự ưu tiên:
>   1. Nếu BA có **update tài liệu** → BẮT BUỘC đọc tài liệu mới để lấy logic đầy đủ nhất (Dạng 3)
>   2. Nếu BA **nêu logic cụ thể** trong câu trả lời → lấy logic đó làm cơ sở (Dạng 2/5)
>   3. Đề xuất QC bị **loại bỏ** nếu BA đã bác bỏ hoặc nêu hướng xử lý khác (Dạng 4)
>
> **Ví dụ thực tế:**
> - *QC đề xuất:* "Cần có popup xác nhận khi thay đổi 'Loại tính phí'"
> - *BA trả lời:* "Xác nhận không có popup. Khi tham số 'Loại tính phí' được thay đổi thì các điều kiện tính phí sẽ bị clear → Đã bổ sung vào yêu cầu nghiệp vụ của trường Loại tính phí"
> - *Phân tích:* Câu trả lời này chứa **3 thành phần**: ❌ Bác bỏ popup (Dạng 4) + 📌 Nêu logic clear dữ liệu (Dạng 5) + 📄 Update tài liệu (Dạng 3)
> - *Hành động đúng:* (1) Bỏ đề xuất popup của QC, (2) Đọc tài liệu US mới nhất để lấy logic "clear điều kiện tính phí khi thay đổi Loại tính phí", (3) Sinh SC dựa trên logic từ tài liệu update + giải thích của BA. **TUYỆT ĐỐI KHÔNG** sinh SC về popup.

**Bước 2 — Self-Check bắt buộc trước khi sinh mỗi SC:**

```
□ Câu hỏi QC gốc đề xuất gì?
□ BA trả lời thuộc Dạng nào (1/2/3/4/5/6/7/8)?
□ Nếu phân loại Dạng 1: BA có nhắc đến "đề xuất" / "theo QC" không? Nếu KHÔNG → chuyển sang Dạng 5.
□ Nếu phân loại Dạng 6: BA có chỉ thị "Không xây test case" không? → NẾU CÓ → LOẠI TRỪ SC, KHÔNG sinh test case.
□ Nếu phân loại Dạng 7: Đã tìm và đọc bộ phân tích US tham chiếu chưa? → NẾU CHƯA → ĐỌC TRƯỚC khi sinh SC.
□ Nếu phân loại Dạng 8: BA có dùng từ chỉ thời gian tương lai ("sẽ", "sau", "đang chờ") không? → NẾU CÓ → TẠM HOÃN, đưa vào danh sách Pending.
□ Logic chốt cuối cùng lấy từ đâu? (Đề xuất QC / Giải thích BA / US update / Loại bỏ / Loại trừ TC / Tham chiếu US khác / Tạm hoãn / Thông tin BA cung cấp)
□ SC đang sinh có phản ánh đúng logic chốt cuối cùng không?
□ Có đang dùng đề xuất QC trong khi BA đã bác bỏ/giải thích khác/cung cấp thông tin khác không? → NẾU CÓ → SỬA NGAY
□ Có đang sinh SC cho QA mà BA đã chỉ thị "Không xây test case" không? → NẾU CÓ → XÓA NGAY
□ Có đang sinh SC cho QA mà BA chưa chốt (Dạng 8) không? → NẾU CÓ → CHUYỂN VÀO DANH SÁCH PENDING
```

> **VI PHẠM NGHIÊM TRỌNG:** Sinh SC dựa trên đề xuất QC trong khi BA đã từ chối, bác bỏ, hoặc giải thích logic khác. Đây là lỗi **sai logic nghiệp vụ** gây ra Test Case không hợp lệ, lãng phí effort của Tester.

AI sử dụng câu trả lời của BA (đã phân loại theo quy tắc trên) để chốt logic, sau đó sinh ra một bảng tổng hợp danh sách các Test Case nhằm bao phủ 100% nội dung tài liệu. Các Test Case này không cần viết bước chi tiết (Test Steps) nhưng phải nêu rõ tiêu đề (Test Case Title) đủ ý và bắt buộc chia thành 7 nhóm sau:
1. **🟢 Happy Path (Positive Cases - Luồng cơ bản):** Kịch bản người dùng thao tác đúng, nhập dữ liệu chuẩn chỉnh và hệ thống xử lý thành công theo đúng luồng nghiệp vụ mong đợi.
2. **🔴 Negative Path & Exception Handling (Luồng ngoại lệ, báo lỗi theo QTC-11):** Cần bao phủ 2 cấp độ xử lý lỗi:
   - **Cấp độ 1 (FE Validation):** Người dùng thao tác sai cơ bản (bỏ trống trường, sai định dạng). FE chặn không cho thao tác tiếp hoặc không cho lưu hoặc hiển thị thông báo lỗi thân thiện.
   - **Cấp độ 2 (BE Exception - Edge cases FE chưa chặn):** Kịch bản bypass validation hoặc vi phạm ràng buộc dữ liệu sâu. Hệ thống phải xử lý an toàn: **không crash, không sai lệch dữ liệu**, hiển thị thông báo lỗi từ BE (có thể dạng mã lỗi kỹ thuật) và ngăn lưu thành công.
3. **📐 Boundary Value Analysis (Giá trị biên):** Kiểm tra điểm giới hạn của dữ liệu được phép nhập (Biên dưới, Biên trên, giá trị bằng 0, số âm, số tối đa).
4. **🎨 UI/UX & Field Validation (Giao diện & Xác thực):** Trạng thái component (disabled/enabled khi chưa đủ field), hành vi Dropdown, chống XSS/SQL Injection cơ bản, hành vi phím Enter, hành vì xác nhận khi không chỉnh sửa.
5. **🧠 Business Logic & State Transition (Logic nghiệp vụ phức tạp):** Rẽ nhánh quy tắc kinh doanh (phân loại khách hàng) hoặc chuyển đổi trạng thái (Từ "Khởi tạo" sang "Chờ duyệt" và không thể quay ngược).
6. **🔗 Data Integrity & Integration (Tính toàn vẹn dữ liệu):** Tính toàn vẹn khi Xóa (Cascade delete hay block), và sự đồng bộ/tích hợp dữ liệu hiển thị giữa các màn hình khác nhau.
7. **⚡ NFR (Non-Functional Requirements):** Phân quyền (Authorization view/edit) và Concurrency/Spam click. **BẮT BUỘC** phải sinh Test Case chống spam click (double-click) cho **từng hành động submit riêng biệt** trong US, bao gồm nhưng không giới hạn:
     - Nút **Xác nhận** khi Thêm mới (từng loại entity)
     - Nút **Xác nhận** khi Chỉnh sửa (từng loại entity)
     - Nút **Xóa** tại Tác vụ Pending (Maker)
     - Nút **Phê duyệt** tại Tác vụ chờ duyệt (Checker)
     - Nút **Từ chối** tại Tác vụ chờ duyệt (Checker)
     Mỗi hành động trên phải là 1 TC riêng biệt (không gộp).

### QUY TẮC PHÂN LOẠI TEST CASE (BẮT BUỘC):
Khi phân loại Test Case, Agent phải tuân thủ thứ tự ưu tiên sau:
1. Nếu case liên quan đến giới hạn số lượng (Min/Max), số thứ tự bản ghi, hoặc độ dài chuỗi: BẮT BUỘC phân loại là "Boundary Value". Tuyệt đối không để là Business Logic.
2. Nếu case liên quan đến luồng phê duyệt (Maker-Checker) hoặc trạng thái dữ liệu (Active/Inactive): Phân loại là "Business Logic".
3. Nếu case liên quan đến định dạng hoặc thông báo lỗi nhập liệu: Phân loại là "Field Validation".

=> Lưu ý: Case "Bản ghi thứ 100 báo lỗi" phải được định danh là "Boundary Value".

### QUY TẮC 1 SC = 1 TC (BẮT BUỘC):
> **Mỗi Mã Kịch Bản (SC-xx) tương ứng CHÍNH XÁC 1 Test Case.** TUYỆT ĐỐI KHÔNG gộp nhiều kịch bản vào 1 SC, và KHÔNG tách 1 SC thành nhiều TC.
> - Nếu 1 kịch bản có nhiều biến thể (VD: bỏ trống 7 trường bắt buộc), vẫn viết thành **1 SC duy nhất** với tiêu đề mô tả đầy đủ (VD: "Bỏ trống từng trường bắt buộc → FE chặn").
> - **KHÔNG tách riêng** từng trường/giá trị thành SC riêng biệt. Giữ nguyên 1 SC bao quát cho cùng 1 nhóm hành vi.

**Định Dạng Bảng Tổng Hợp Test Case:**
`[Mã Kịch Bản (ID)] | [Feature] | [Module] | [Loại Test Case (1 trong 7 nhóm)] | [Tên Test Case / Kịch bản] | [Trích dẫn tài liệu (Traceability)]`
*Lưu ý:* Cột 'Mã Kịch Bản (ID)' dùng để đặt định danh duy nhất (VD: SC-01, SC-02), mỗi SC = 1 TC. Cột 'Feature' là Tính năng lớn, 'Module' là tính năng con. Cột 'Tên Test Case / Kịch bản' phải mô tả đầy đủ kịch bản chính muốn test. Cột 'Trích dẫn tài liệu' phải **trích dẫn nguyên văn** từ tài liệu gốc (Vị trí + nội dung quy tắc, đủ để hiểu, **≤ 200 ký tự**) — KHÔNG suy diễn, KHÔNG viết lại — để Tester có thể dùng Ctrl+F tìm lại đúng đoạn đó trong tài liệu gốc.

## 5. Định Dạng File Đầu Ra & Traceability Rule
### 5.1 Định Dạng Bảng Q&A (Phần B)
Bảng Q&A hiển thị mỗi câu hỏi trên **một dòng riêng biệt** (+ 1 hàng header). Cấu trúc mỗi hàng:

| Cột | Quy tắc | Ví dụ |
|---|---|---|
| **ID** | `[Mã tính năng]-QA-[01 đến 04].[STT]`. Trong đó 01-04 tương ứng Hạng mục 1-4, STT là số thứ tự câu hỏi trong hạng mục đó. | `US01-QA-01.1`, `US01-QA-01.2`, `US01-QA-02.1` |
| **Trích xuất** | Ghi rõ vị trí + **trích dẫn nguyên văn nội dung quy tắc** từ tài liệu gốc. Đủ để hiểu ngữ cảnh (≥ 10 từ), không vượt **200 ký tự**. CẤM số dòng, CẤM suy diễn. | `Mục "3.2 Thêm mới", Bảng "Mô tả trường" STT 7 "Mã phí" – *"Bắt buộc nhập, tối đa 50 ký tự, không trùng"*` |
| **Câu hỏi / Sự cố** | Mô tả một vấn đề logic duy nhất, ngắn gọn, súc tích. TUYỆT ĐỐI KHÔNG gom nhiều vấn đề vào 1 ô. | `Flowchart thiếu nhánh khi User không thay đổi dữ liệu.` |
| **Phân loại** | Một trong 4 giá trị cố định: `Nghiệp vụ` / `Giới hạn` / `Toàn vẹn dữ liệu` / `UI-UX`. | `Nghiệp vụ` |
| **Đề xuất từ QC** | Nêu rõ phương án xử lý theo chuẩn cho vấn đề ở cột Câu hỏi. | `Đề xuất: FE hiển thị cảnh báo, không cho submit.` |
| **Trả lời của BA** | **Để trống** — BA sẽ điền sau. | _(trống)_ |

**QUY TẮC TRÍCH XUẤT (TRACEABILITY RULE) BẮT BUỘC:**

> **NGUYÊN TẮC TỐI THƯỢNG:** Mọi nội dung trong cột **Trích xuất** phải được **sao chép nguyên văn (verbatim)** từ tài liệu gốc, **đủ nội dung để người đọc hiểu ngữ cảnh** mà không cần mở tài liệu gốc, nhưng **KHÔNG vượt quá 200 ký tự**. TUYỆT ĐỐI KHÔNG suy diễn, KHÔNG paraphrase, KHÔNG viết lại bằng ngôn ngữ của AI. Nếu tài liệu gốc viết *"Hệ thống kiểm tra tính hợp lệ của dữ liệu trước khi lưu vào cơ sở dữ liệu"* thì cột Trích xuất phải ghi đúng nguyên văn câu đó, KHÔNG được rút gọn thành *"Validate dữ liệu"* hay kéo dài thêm nội dung AI tự bịa.

**CẤM TUYỆT ĐỐI:**
1. **CẤM dùng số dòng** (Line 15, Line 20...) làm tham chiếu — vì tài liệu AI đọc là file text trích xuất từ Word gốc, số dòng sẽ KHÔNG khớp với file của BA.
2. **CẤM suy diễn nội dung** — KHÔNG được tự diễn giải, tóm tắt, hoặc viết lại nội dung tài liệu bằng từ ngữ riêng.
3. **CẤM ghi tham chiếu chung chung** — KHÔNG được viết kiểu "Theo tài liệu..." hoặc "Dựa trên mô tả..." mà không chỉ rõ vị trí cụ thể.
4. **CẤM trích dẫn cụt lủn** — KHÔNG được chỉ ghi tên mục/bảng mà thiếu nội dung quy tắc. Phải trích dẫn **đủ ngữ cảnh** (≥ 10 từ) để người đọc hiểu vấn đề.
5. **CẤM vượt 200 ký tự** — Mỗi ô trích xuất tối đa **200 ký tự** (kể cả vị trí tham chiếu + trích dẫn). Nếu nội dung gốc dài hơn, cắt ở vị trí có nghĩa và thêm `[...]` cuối.

**CẤU TRÚC BẮT BUỘC:** `[VỊ TRÍ THAM CHIẾU] – [TRÍCH DẪN NỘI DUNG NGUYÊN VĂN (đủ hiểu, ≤ 200 ký tự tổng)]`

**4 PHƯƠNG PHÁP TRÍCH DẪN HỢP LỆ (Bắt buộc dùng 1 hoặc kết hợp):**

| # | Phương pháp | Cách ghi | Ví dụ ĐÚNG ✅ |
|---|---|---|---|
| 1 | **Tên Mục / Tên Heading** | Ghi chính xác tên heading + trích dẫn nội dung quy tắc | `Mục "3.2. Khai báo Nghiệp vụ" – *"Mã sản phẩm là duy nhất, không được trùng trong toàn hệ thống"*` |
| 2 | **Tên Bảng & STT dòng** | Ghi tên bảng + STT + trích dẫn mô tả trường | `Bảng "Mô tả chi tiết các trường", STT 5 "Mã phí" – *"Bắt buộc nhập, tối đa 50 ký tự, không trùng"*` |
| 3 | **BPMN / Flowchart** | Ghi tên Flowchart + bước số + mô tả hành động | `Flowchart "Thêm mới SPDV", Bước 6.b – *"Nếu dữ liệu không hợp lệ, hiển thị thông báo lỗi"*` |
| 4 | **Trích dẫn trực tiếp Text** | Copy nguyên văn đoạn text đủ ngữ cảnh (≥ 10 từ, ≤ 200 ký tự) để BA dùng Ctrl+F tìm được | `Đoạn: *"Hệ thống cần thực hiện kiểm tra tính duy nhất của Mã trước khi lưu bản ghi vào CSDL"*` |

**Bảng Ví Dụ ĐÚNG / SAI:**

| ❌ SAI (CẤM) | ✅ ĐÚNG (BẮT BUỘC) | Lý do |
|---|---|---|
| `Line 45 của file text` | `Mục "3.1 Danh sách", Bảng "Các trường hiển thị", STT 3 – *"Cột Trạng thái hiển thị giá trị Hoạt động/Ngừng hoạt động"*` | Số dòng không khớp file Word gốc |
| `Theo tài liệu, trường Mã phải unique` | `Mục "3.2 Thêm mới" – *"Mã sản phẩm là duy nhất, không được trùng trong toàn hệ thống"*` | Suy diễn từ "unique", thiếu nguyên văn |
| `Bảng mô tả trường, STT 2` (cụt lủn, thiếu nội dung) | `Bảng "Mô tả chi tiết các trường", STT 2 "Tên SPDV" – *"Bắt buộc nhập, tối đa 100 ký tự Unicode"*` | Chỉ ghi vị trí, thiếu trích dẫn nội dung quy tắc |
| `Flowchart có nhánh validate` | `Flowchart "Chỉnh sửa SPDV", Bước 5 Gateway "Dữ liệu hợp lệ?" – *"Nếu không hợp lệ, quay lại bước nhập liệu"*` | Thiếu tên Flowchart, bước số, và nội dung |
| `Hệ thống validate dữ liệu` (AI tự viết) | `*"Hệ thống kiểm tra tính hợp lệ của dữ liệu nhập vào trước khi cho phép lưu"*` (nguyên văn) | AI paraphrase thay vì copy nguyên văn |

**SELF-CHECK BẮT BUỘC — Trước mỗi lần ghi cột Trích xuất:**
```
□ Nội dung trích xuất có được copy nguyên văn từ tài liệu gốc không? Hay AI đang tự viết lại?
□ Có dùng số dòng (Line XX) không? → NẾU CÓ → XÓA, thay bằng tên mục/bảng/flowchart.
□ Trích dẫn có ĐỦ NỘI DUNG để người đọc hiểu ngữ cảnh không? (≥ 10 từ trích dẫn nội dung quy tắc)
□ Tổng ký tự ô Trích xuất có VƯỢT 200 ký tự không? → NẾU CÓ → Cắt ở vị trí có nghĩa + thêm [...]
□ BA có thể dùng Ctrl+F để tìm được đoạn text này trong file Word gốc không?
□ Tên Heading/Bảng/Flowchart có khớp CHÍNH XÁC với tài liệu gốc không? (kể cả dấu ngoặc kép, số thứ tự)
```

> **VI PHẠM NGHIÊM TRỌNG:** Ghi cột Trích xuất bằng nội dung AI tự suy diễn/viết lại sẽ khiến BA **không thể trace** về đúng vị trí trong tài liệu gốc, gây mất thời gian đối chiếu và giảm uy tín bộ Q&A.

**YÊU CẦU BẮT BUỘC VỀ FILE XUẤT RA:**
Quá trình xuất file diễn ra như sau:
- **Phase 1:** Sinh **2 file Word (.docx) RIÊNG BIỆT**:
  - **File A** (`USxx_PartA_Summary.docx`): Chỉ chứa Phần A — Tóm tắt Nghiệp vụ (dành cho Tester đọc hiểu).
  - **File B** (`USxx_PartB_QA.docx`): Chỉ chứa Phần B — Q&A Table với cột "Trả lời của BA" rỗng (dành cho BA trả lời).
- **Phase 2:** Sau khi nhận câu trả lời BA, tự động sinh lại **1 file Word (.docx) tổng hợp** chứa Phần A, Phần B (đã update câu trả lời) và Phần C (Bảng Test Case).

- Sử dụng công cụ `write_to_file` để viết một script Python dùng thư viện `python-docx` (`pip install python-docx`) rồi chạy terminal bằng `run_command` để tạo file `.docx`.
- Tuyệt đối không để user phải yêu cầu lại việc xuất file ở cuối mỗi Phase.
- **Quan trọng về Layout (Table Formatting):** 
  - Khi khởi tạo file word bằng `docx.Document()`, **BẮT BUỘC** phải chỉnh lại lề của trang (Page Margins) thành siêu mỏng (Narrow) cho toàn bộ tài liệu (ví dụ set top, bottom, left, right margin bằng `0.5` inch hoặc `1.27` cm) xoay trang thành Landscape để nội dung không bị cắt xén lề trái/phải.
  - Khi code Python vẽ Bảng Q&A và Bảng Test Case, bắt buộc phải set Autofit hoặc gán thông số độ rộng (width) cứng cho các Cột để ăn gian lề trái/phải, giúp đoạn văn dàn trải ngang dễ nhìn, tránh việc chữ bị nhồi ép thành một cột dọc hẹp kéo dài.

## 6. Bắt Buộc (Strict Rules)
- Phân tích bằng tiếng Việt rõ ràng, rành mạch. Tránh dùng từ ngữ lập trình quá sâu nếu Tester chưa cần biết.
- KHÔNG BAO GIỜ bị động chấp nhận 100% tài liệu là đúng. Nhiệm vụ của QC là "Phá" tài liệu tìm điểm thiếu.
- Cấu trúc trả lời phải luôn duy trì 2 phần: Tóm tắt (Đọc hiểu) và Q&A (Nghi vấn).
- **[PROFIX RULE - TUYỆT ĐỐI KHÔNG HỎI LẠI] TRƯỚC KHI ĐẶT CÂU HỎI Q&A:** Bắt buộc đối chiếu với toàn bộ QTC-01 đến QTC-12 trong `profix_common_rules/SKILL.md`. 
  - Nếu một vấn đề (độ dài, định dạng ngày, maker-checker...) đã có trong Quy tắc chung → **MẶC ĐỊNH ÁP DỤNG, KHÔNG ĐƯỢC ĐƯA VÀO DANH SÁCH Q&A ĐỂ "XÁC NHẬN LẠI".**
  - Hành vi hỏi xác nhận (Ví dụ: *"Trường tên có áp dụng giới hạn 50 ký tự theo QTC-01.6 không?"*) là **VI PHẠM NGHIÊM TRỌNG**. Chỉ đặt câu hỏi nếu tài liệu US có ghi chú **mâu thuẫn trực tiếp** với QTC.
- **[PROFIX RULE] KHI GHI NHẬN QUY TẮC CHUNG VÀO BÁO CÁO:** Tại Phần A (Tóm tắt), có thêm một mục "A.4. Quy Tắc Chung Áp Dụng" để tổng hợp danh sách các QTC-XX liên quan đến US đang phân tích. Mọi giả định mặc định phải nằm ở Phần A, không được tràn xuống Phần B.
- **[CẤM HỎI VỀ MESSAGE LỖI]:** TUYỆT ĐỐI KHÔNG đặt câu hỏi yêu cầu BA làm rõ mã lỗi (error codes), toast hiển thị lỗi, hay nội dung message lỗi (error messages). Các thành phần này không thuộc phạm vi cần Q&A.
