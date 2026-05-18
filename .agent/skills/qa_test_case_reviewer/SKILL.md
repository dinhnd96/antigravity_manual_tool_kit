---
name: qa_test_case_reviewer
description: Kỹ năng chuyên sâu để review, đối soát bộ Test Case so với tài liệu yêu cầu (URD/BRD) và chuẩn đầu ra Enterprise, tìm lỗi logic, điểm thiếu hụt (Gap) và mâu thuẫn nghiệp vụ.
---

# Kỹ năng Review Test Case Đối Soát Nghiệp Vụ (QA Test Case Reviewer)

Kỹ năng này định hướng AI hoạt động như một **Senior QA / Test Lead**. Mục tiêu tối thượng là đảm bảo bộ Test Case không chỉ khớp với tài liệu đặc tả nguồn (URD, BRD, FSD, BA trả lời Q&A) mà còn **PHẢI TUÂN THỦ NGHIÊM NGẶT** tiêu chuẩn sinh Test Case B2 Enterprise.

## 1. Tiêu Chí Review Khắt Khe (Mandatory Checkpoints)

Khi thực hiện review, AI phải quét bộ Test Case qua các bộ lọc sau và **báo lỗi đỏ** nếu vi phạm:

### 1.1 Tính Bao Phủ & Kỹ Thuật (Coverage & Techniques)
- **Risk & Priority:** TC đã phản ánh đúng Priority dựa theo Risk Level của tính năng (High/Medium/Low) chưa?
- **Kỹ thuật thiết kế (Bắt lỗi thiếu case):** 
  - **BVA (Giá trị biên):** Đã test đủ ranh giới cận trên/dưới cho các trường tiền tệ, độ dài chưa? Thiếu case biên -> Báo lỗi GAP.
  - **Kiểm thử Business Rule (Ràng buộc so sánh):** Đối với các quy tắc so sánh (>, <, =), **BẮT BUỘC** phải có đủ 3 kịch bản kiểm thử. Bắt lỗi GAP nếu thiếu bất kỳ trường hợp nào trong bộ 3 này.
  - **Equivalence Partitioning:** Các input cùng nhóm đã được gom gọn chưa hay đang test thừa thãi (Redundant)?
  - **State Transition:** Đã test đủ các chiều khóa chặn chuyển đổi trạng thái (Status) sai logic chưa?
  - **Edge Cases:** Có test case nào cover Timeout, Mất mạng, Lỗi hệ thống không?

### 1.2 Độ Chi Tiết Của Test Data (Zero Placeholder)
- Khước từ và đánh dấu lỗi NGAY LẬP TỨC các Test Case dùng từ ngữ lấp lửng trong Step/Data như: *"chọn dữ liệu hợp lệ"*, *"nhập số tiền"*, *"điền form đúng format"*.
- Yêu cầu Test Data phải là giá trị cứng (Hardcoded/Mock) tương ứng: *"Nhập Tên = 'Sản Phẩm A'"*, *"Tiền = 10,000,000"*, *"Ngày = 28/02/2026"*.

### 1.3 Cấu Trúc Fields, SC_Ref, Reference, TC_ID & Expected Result 2 Lớp
- **TC_ID:** Bắt lỗi nếu định dạng ID không tuân thủ cấu trúc `<<MOD>>-TC-XXX` (vd: SA14-TC-001). Tuyệt đối khước từ ID có nhúng mã rule hoặc phân loại (vd: SA14-BR-HAP-001).
- **Feature & Module:** Phải kiểm tra sự phân định rõ ràng giữa cột `Feature` (Tính năng cha) và `Module` (Tính năng con). Bắt lỗi nếu gộp chung thành 1 cột hoặc phân cấp lộn xộn.
- **SC_Ref:** Phải kiểm tra cột SC_Ref xem có lấy trực tiếp từ bảng phân tích tài liệu (Mã Kịch Bản) để đảm bảo không sót case hay không. Báo lỗi nếu thiếu hoặc tự bịa ra mã không có trong file phân tích.
- **Reference (Cột tham chiếu) — QUY TẮC TRÍCH XUẤT (TRACEABILITY RULE) BẮT BUỘC:**
  
  Phải tuân thủ cấu trúc: `[VỊ TRÍ THAM CHIẾU] – [TRÍCH DẪN QUY TẮC NGẮN GỌN (tối đa 1-2 câu)]`.
  
  > **NGUYÊN TẮC TỐI THƯỢNG:** Mọi nội dung trong cột Reference phải được **sao chép nguyên văn (verbatim)** từ tài liệu gốc. TUYỆT ĐỐI KHÔNG suy diễn, KHÔNG paraphrase, KHÔNG viết lại bằng ngôn ngữ của AI.
  
  **CẤM TUYỆT ĐỐI:**
  1. **CẤM dùng số dòng** (Line 15, Dòng 20...) làm tham chiếu — vì tài liệu AI đọc là file text trích xuất từ Word gốc, số dòng sẽ KHÔNG khớp với file của BA/Tester.
  2. **CẤM suy diễn nội dung** — KHÔNG được tự diễn giải, tóm tắt, hoặc viết lại nội dung tài liệu bằng từ ngữ riêng.
  3. **CẤM ghi tham chiếu chung chung** — KHÔNG được viết kiểu "Theo tài liệu...", "Dựa trên mô tả...", hoặc "Mục 2" mà không chỉ rõ tên heading cụ thể.
  
  **4 PHƯƠNG PHÁP TRÍCH DẪN HỢP LỆ (Bắt buộc dùng 1 hoặc kết hợp):**
  
  | # | Phương pháp | Cách ghi | Ví dụ ĐÚNG ✅ |
  |---|---|---|---|
  | 1 | **Tên Mục / Tên Heading** | Ghi chính xác tên heading/mục trong tài liệu | `Mục "3.2. Khai báo Nghiệp vụ", phần "Giao diện Thêm mới"` |
  | 2 | **Tên Bảng & STT dòng** | Ghi tên bảng + số thứ tự (STT) hoặc tên trường trong bảng | `Bảng "Mô tả chi tiết các trường", dòng STT 5 — trường "Mã phí"` |
  | 3 | **BPMN / Flowchart** | Ghi tên Flowchart + bước số cụ thể | `Flowchart "Thêm mới Sản phẩm dịch vụ", Bước 6.b` |
  | 4 | **Trích dẫn trực tiếp Text** | Copy nguyên văn một đoạn text đủ ngắn để dùng Ctrl+F tìm được | `Đoạn: *"Hệ thống cần thực hiện kiểm tra tính duy nhất của Mã"*` |
  
  **Bảng Ví Dụ ĐÚNG / SAI khi Review cột Reference:**
  
  | ❌ SAI (Bắt lỗi ngay) | ✅ ĐÚNG (Chấp nhận) | Loại lỗi |
  |---|---|---|
  | `Dòng 15` / `Line 45` | `Mục "3.1 Danh sách", Bảng "Các trường hiển thị", STT 3` | Dùng số dòng |
  | `Theo tài liệu, trường Mã phải unique` | `Mục "3.2 Thêm mới" – *"Mã sản phẩm không được trùng trong hệ thống"*` | Suy diễn, thiếu vị trí |
  | `Phần mô tả trường Tên` | `Bảng "Mô tả chi tiết các trường thông tin", STT 2 — trường "Tên SPDV"` | Quá chung chung |
  | `Flowchart có nhánh validate` | `Flowchart "Chỉnh sửa SPDV", Bước 5 — Gateway "Dữ liệu hợp lệ?"` | Thiếu tên Flowchart & bước số |
  | `Hệ thống validate dữ liệu` (AI tự viết) | `*"Hệ thống kiểm tra tính hợp lệ của dữ liệu nhập vào"*` (nguyên văn) | AI paraphrase |
  | `Mục 2` (chỉ ghi số mục) | `Mục "2. Quản lý Sản phẩm dịch vụ"` (ghi tên đầy đủ) | Thiếu tên heading |
  
  **SELF-CHECK khi Review cột Reference:**
  ```
  □ Reference có dùng số dòng (Line XX / Dòng XX) không? → BẮT LỖI
  □ Reference chỉ ghi vị trí mà thiếu trích dẫn nội dung quy tắc? → BẮT LỖI
  □ Nội dung trích dẫn có khớp nguyên văn với tài liệu gốc không? Hay AI/Tester tự viết lại? → BẮT LỖI nếu paraphrase
  □ BA/Tester có thể dùng Ctrl+F tìm được đoạn text này trong file Word gốc không? → BẮT LỖI nếu không tìm được
  □ Tên Heading/Bảng/Flowchart có khớp CHÍNH XÁC với tài liệu gốc không? → BẮT LỖI nếu sai tên
  ```
- **Pre-conditions:** Phải được đánh số thứ tự (1, 2...) và ghi rõ ràng. Chống viết cụt lủn "Trạng thái hoạt động" mà không rõ của bảng/module nào.
- **Test Steps:** Bắt lỗi việc gộp thao tác (Ví dụ gộp vừa Thêm vừa Sửa vào cùng 1 TC). Phải đánh số tuần tự.
- **Expected Results:** 
  - Đã tách đủ 2 lớp chưa? (i) Nghiệp vụ/Logic (ii) UI. Nếu thiếu lớp nào báo lỗi lớp đó.
  - Đối với luồng E2E (Maker-Checker), **BẮT BUỘC** kiểm tra có phân định rõ `--- TRƯỚC KHI DUYỆT (MAKER) ---` và `--- SAU KHI LAST CHECKER DUYỆT ---` không.
  - **Kiểm tra lỗi biến mất bản ghi:** Tuyệt đối khước từ các Expected Result ghi là bản ghi "biến mất" khỏi màn hình Tác vụ chờ duyệt/Pending sau khi phê duyệt/từ chối. Yêu cầu sửa thành cập nhật trạng thái mới.

### 1.4 Tính Chính Xác Logic (Logic & Rule Validation)
- Mâu thuẫn giữa FSD và TC: FSD yêu cầu trạng thái "A", nhưng TC lại kỳ vọng trạng thái "B".
- Bắt lỗi test Negative (Validation) trên các trường hệ thống Auto-generated.
- Test chức năng "Xem/Đóng" nhưng Expected lại làm đổi Data State.

## 2. Quy Trình Thực Thi (Standard Workflow)
1. **Recon (Điều tra):** Đọc kỹ tài liệu URD/FSD để liệt kê danh sách Logic (`LOG-xxx`) và màn hình UI (`UI-xxx`).
2. **Q&A Check:** Đọc kỹ phần câu trả lời Q&A để nắm rõ các logic nghiệp vụ đã được thống nhất.
3. **Mapping (Đối soát):** Duyệt qua danh sách Test Case và map TC_ID với mã Logic/UI. Trích lập ma trận Traceability.
4. **Drill-down Standard (Check tiêu chuẩn):** Quét từng fields (Data, Steps, Expected 2 lớp) của TC.
5. **Reporting (Báo cáo):** Tổng hợp danh sách lỗi vi phạm logic và vi phạm format.

## 3. Cấu Trúc Báo Cáo Trả Về (The Review Report)
Trình bày kết quả review dưới dạng bảng, tách biệt lỗi Format (Data/Expected) và lỗi Nghiệp vụ (Logic/GAP).

### Bảng 1: Lỗi Nghiệp Vụ & Gap Analysis
| LOG_ID / Reference | Loại phát hiện | Mô tả Sự cố / Mâu thuẫn | Mức độ Nghiêm trọng | Đề xuất sửa chữa |
| :--- | :--- | :--- | :--- | :--- |
| **LOG-TAB-SPDV-FILTER-DATE** | **GAP (BVA)** | Chưa test giá trị biên Từ ngày > Đến ngày 1 ngày. | **High** | Thêm luồng biên giới TC-BR-NEG. |
| **LOG-CODEPI-STATUS** | **Logic Mismatch** | FSD yêu cầu trạng thái Hủy không được sửa, TC lại có bước Edit. | **High** | Xóa TC hoặc sửa expected thành "Báo lỗi". |

### Bảng 2: Lỗi Tiêu Chuẩn Enterprise Format (Bắt buộc Khắc nghiệt)
| TC_ID | Hạng mục Vi Phạm | Mô tả Vi Phạm | Hướng khắc phục |
| :--- | :--- | :--- | :--- |
| **SA14-TC-002** | **Test Data (Placeholder)** | Dùng từ "Nhập đầy đủ thông tin". Quá mơ hồ. | Đề xuất giá trị cứng: Mã = NV01, Tiền = 5M. |
| **SA14-TC-004** | **Expected Result Layer** | Thiếu Layer (ii): Trạng thái Update UI Toast. | Bổ sung ý hiển thị thông báo "Thành công". |
| **SA14-TC-005** | **Expected Result (Maker-Checker)** | Expect bản ghi "biến mất" khỏi lưới Pending. | Sửa thành: Bản ghi tại màn hình Tác vụ chờ duyệt cập nhật trạng thái Đã duyệt. |
| **SA14-TC-010** | **Anti-Pattern (Gộp Step)** | TC đang gộp test Bỏ trống Tên và Bỏ trống Mã vào cùng 1 case | Yêu cầu rã thành 2 TC độc lập (Quy tắc số 3). |
| **SA14-TC-011** | **Cấu trúc Reference** | Cột Reference chỉ ghi vị trí tham chiếu mà thiếu trích dẫn nội dung quy tắc. | Đề xuất bổ sung theo chuẩn: `[Vị trí] – [Trích dẫn ngắn gọn 1-2 câu]`. |
| **SA14-TC-015** | **Reference (Số dòng)** | Cột Reference dùng "Dòng 45" / "Line 20" — số dòng từ file text không khớp file Word gốc. | Thay bằng tên Heading/Bảng/Flowchart cụ thể. VD: `Mục "3.2 Thêm mới", Bảng "Mô tả trường" STT 5`. |
| **SA14-TC-018** | **Reference (Suy diễn)** | Cột Reference ghi "Hệ thống validate dữ liệu" — AI tự paraphrase, không phải nguyên văn tài liệu. | Thay bằng trích dẫn nguyên văn: `*"Hệ thống kiểm tra tính hợp lệ của dữ liệu nhập vào"*`. |

## 4. Mẫu Câu Lệnh Gọi Skill (Invocation Prompt)
User có thể gọi kỹ năng này bằng các câu tương tự:
- *"Hãy dùng skill `qa_test_case_reviewer` để review bộ Test Case này xem đã chuẩn Enterprise và đúng với URD chưa."*
- *"So sánh các bước Expected Result và Test data của TC so với tiêu chuẩn giúp tôi."*
