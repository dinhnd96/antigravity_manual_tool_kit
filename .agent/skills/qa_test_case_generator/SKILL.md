---
name: qa_test_case_generator
description: Kỹ năng Senior QA Lead phân tích URD/BRD để sinh bộ Test Case chuẩn Enterprise (Level B2) với kỹ thuật tách biệt kịch bản và Expected Result 2 lớp (Logic & UI).
dependencies:
  - profix_common_rules
---

# Kỹ năng Tạo Test Case Chuẩn Enterprise (QA Test Case Generator)

Kỹ năng này định hướng AI hoạt động như một Senior QA Lead, phân tích tài liệu nguồn (URD/BRD/SRD) và sinh ra full bộ Test Case theo tiêu chuẩn Enterprise Level B2 (Chi tiết cao, Không dư, Không lặp).

## 0. TÍCH HỢP QUY TẮC CHUNG PROFIX (BẮT BUỘC – ĐỌC TRƯỚC)

> **Skill này được sử dụng trong dự án ProfiX Phase 1.** Trước khi sinh Test Case, AI BẮT BUỘC đọc và nạp nội dung skill `profix_common_rules` tại đường dẫn:
> `.agent/skills/profix_common_rules/SKILL.md`

### Mục đích tích hợp
Tài liệu `Quy tắc chung.docx` (ProfiX) định nghĩa các hành vi mặc định áp dụng cho toàn bộ hệ thống. 
- **[PROFIX RULE] TRONG QUÁ TRÌNH VIẾT TEST CASE:** Bắt buộc áp dụng các quy tắc xuất/nhập/tìm kiếm/hiển thị từ QTC-01 đến QTC-10 để hoàn thiện kịch bản, ngay cả khi URD gốc bỏ sót. Cần ghi vào cột Note ghi chú `[Theo QTC-XX]` để Test Lead biết Test Case có nguồn gốc từ đâu.

## 1. Yêu Cầu Chung & Xử Lý Hình Ảnh
- **Giữ nguyên tên field/item/button (BẮT BUỘC)**: Lấy đúng và đầy đủ tên các field, item, button... từ tài liệu hoặc mockup. Tuyệt đối không cắt gọn, rút gọn (vd: dùng "Lưu" thay vì "Lưu thông tin") hoặc tự ý đặt tên theo thói quen.
- **Xử lý tài liệu DOCX**: Nếu tài liệu có ảnh (Mockup, Flowchart), ưu tiên sử dụng lệnh giải nél (truy cập `word/media/`) để lấy ảnh. Phân tích 2-3 hình ảnh cốt lõi (Vision/OCR) để hiểu sâu về thiết kế UI và Flow mà text không diễn đạt hết.


## 2. Mục Tiêu Sinh Test Case
Sinh đồng thời các nhóm TC sau, đảm bảo **không trùng nội dung**:
1. **🟢 Happy Path (Positive Cases - Luồng cơ bản):** Kịch bản người dùng thao tác đúng, nhập dữ liệu chuẩn chỉnh và hệ thống xử lý thành công theo đúng luồng nghiệp vụ mong đợi.
2. **🔴 Negative Path & Exception Handling (Luồng ngoại lệ, báo lỗi):** Hệ thống phản hồi khi người dùng thao tác sai (bỏ trống trường, sai định dạng, dữ liệu trùng lặp). Hệ thống không crash mà phải có thông báo lỗi rõ ràng.
3. **📐 Boundary Value Analysis (Giá trị biên):** Kiểm tra điểm giới hạn của dữ liệu được phép nhập (Biên dưới, Biên trên, giá trị bằng 0, số âm, số tối đa).
4. **🎨 UI/UX & Field Validation (Giao diện & Xác thực):** Trạng thái component (disabled/enabled khi chưa đủ field), hành vi Dropdown, chống XSS/SQL Injection cơ bản, hành vi phím Enter, hành vi xác nhận chỉnh sửa khi không thay đổi dữ liệu.
5. **🧠 Business Logic & State Transition (Logic nghiệp vụ phức tạp):** Rẽ nhánh quy tắc kinh doanh (phân loại khách hàng) hoặc chuyển đổi trạng thái (Từ "Khởi tạo" sang "Chờ duyệt" và không thể quay ngược).
6. **🔗 Data Integrity & Integration (Tính toàn vẹn dữ liệu):** Tính toàn vẹn khi Xóa (Cascade delete hay block), và sự đồng bộ/tích hợp dữ liệu hiển thị giữa các màn hình khác nhau.
7. **⚡ NFR (Non-Functional Requirements):** Phân quyền (Authorization view/edit) và Concurrency/Spam click (chống tạo rác dữ liệu khi double-click nút Submit).

## 3. Quy Tắc "Tách Riêng Test Case" & "Không Trùng"
- **TÁCH RIÊNG TUYỆT ĐỐI**: Mỗi Test Case chỉ kiểm tra một điều kiện, một trạng thái hoặc một luồng cụ thể. 
- **CẤM GỘP**: Không gộp nhiều trường hợp hoặc nhiều trạng thái (Status/State) vào cùng một TC để tránh rủi ro sót case khi thực thi.
- **Note only**: Nếu một ý nghĩa đã được cover bởi TC khác, KHÔNG tạo TC mới; thay vào đó thêm 1 dòng Note: "Đã cover ở TC_ID=<<ID>> (Module=<<...>>, FSD_Ref=<<...>>, SC_Ref=<<...>>)".

## 4. Hướng Dẫn Viết Test Case
- **Title (Tiêu đề)**: Rõ ràng, mô tả trực diện mục tiêu. Đọc vào hiểu ngay hành vi test và kỳ vọng.
- **Precondition**: Nêu rõ vai trò, tham số, ngày T, trạng thái đầu vào. **BẮT BUỘC** đánh số thứ tự (1, 2...) và ngắt dòng kể cả khi chỉ có 1 ý. Tên tính năng phân quyền phải lấy theo tên tính năng to/chính trong tài liệu.
- **Steps**: Đánh số rõ ràng, tối đa 4–8 bước. Gắn liền với kịch bản cụ thể, không dùng mẫu chung chung. Sử dụng chính xác tên các button từ tài liệu (vd: click nút 'Xác nhận' thay vì 'Lưu'). Phải đầy đủ các bước của Maker và Checker đối với case End-to-End (E2E). **Test Data trong các step phải cụ thể**, trích xuất hoặc tự thiết kế mô phỏng trực tiếp từ đặc tả yêu cầu. Tuyệt đối không dùng placeholder hay từ ngữ chung chung kiểu `nhập dữ liệu hợp lệ`, mà phải diễn đạt rõ giá trị (vd: `nhập Mã = 'A123'`).
- **Expected Result**: Đảm bảo đủ 2 lớp dữ liệu (Bắt buộc xuống dòng từng ý), chỉ test theo hướng người dùng cuối (End-User Perspective):
 (i) Nghiệp vụ/Logic: [Mô tả xử lý logic/nghiệp vụ. VD: Hệ thống lọc đúng dữ liệu theo điều kiện, hoặc không cho phép lưu bản ghi khi có lỗi validation.]
    (ii) UI: [Mô tả hiển thị giao diện. VD: Hiển thị đúng kết quả trên lưới, hiển thị thông báo lỗi 'abc', hoặc highlight đỏ các trường nhập sai.]
  - **Dành cho luồng Thêm mới(end to end) :**
    ```
    --- TRƯỚC KHI DUYỆT (MAKER) ---
    (i) Nghiệp vụ/Logic: [Hệ thống ghi nhận lưu thành công. Bản ghi ở trạng thái 'Chờ duyệt', Mã chưa được sinh (đối với yêu cầu có sinh mã tự động).]
    (ii) UI: Toast 'Thêm mới thành công'. Bản ghi hiển thị tại màn hình Tác vụ Pending của tôi.

    --- SAU KHI LAST CHECKER DUYỆT ---
    (i) Nghiệp vụ/Logic: [Hệ thống lưu dữ liệu chính thức. Mã được sinh tự động theo quy tắc (đối với yêu cầu có sinh mã tự động). Bản ghi được cập nhật trạng thái là Đã duyệt.]
    (ii) UI: Toast 'Phê duyệt thành công'. Bản ghi tại màn hình Tác vụ chờ duyệt cập nhật trạng thái Đã duyệt. Bản ghi hiển thị trên lưới chính thức với Mã đã sinh (đối với yêu cầu có sinh mã tự động).
    ```
  - **Dành cho luồng Chỉnh sửa (Mã không đổi)(end to end):**
    ```
    --- TRƯỚC KHI DUYỆT (MAKER) ---
    (i) Nghiệp vụ/Logic: [Hệ thống ghi nhận lưu thành công. Bản ghi nháp ở trạng thái 'Chờ duyệt', Mã giữ nguyên không đổi.]
    (ii) UI: Toast 'Chỉnh sửa thành công'. Bản ghi hiển thị tại màn hình Tác vụ Pending của tôi.

    --- SAU KHI LAST CHECKER DUYỆT ---
    (i) Nghiệp vụ/Logic: [Hệ thống cập nhật dữ liệu chính thức. Mã giữ nguyên không đổi. Bản ghi đổi trạng thái thành Đã duyệt.]
    (ii) UI: Toast 'Phê duyệt thành công'. Bản ghi tại màn hình Tác vụ chờ duyệt cập nhật trạng thái Đã duyệt. Bản ghi hiển thị thông tin mới cập nhật trên lưới chính thức.
    ```


## 5. Quy Tắc Chống Lỗi Logic
- **Xem/Đóng**: Không làm thay đổi dữ liệu bản ghi.
- **Trường tự sinh**: Không test Negative validation trên các trường hệ thống tự gán (ngày tạo, người tạo).
- **State Transition**: Phải có đủ kịch bản cho tất cả chiều chuyển đổi (xuôi/ngược) của trạng thái bản ghi.
- **Hiển thị sau khi thao tác (Pending/Checker)**: Tuyệt đối không được expect bản ghi "biến mất" khỏi màn hình Tác vụ chờ duyệt/Pending sau khi phê duyệt/từ chối. Thay vào đó, bản ghi phải được cập nhật trạng thái mới (VD: Đã duyệt, Từ chối) và hiển thị đúng tại màn hình/tab tương ứng.
- **Kiểm thử Business Rule (Ràng buộc dữ liệu)**: Đối với các quy tắc so sánh (VD: Ngày hiệu lực <= Ngày hết hạn), **BẮT BUỘC** phải có đủ 3 kịch bản kiểm thử cho các trường hợp: Lớn hơn (>), Nhỏ hơn (<), và Bằng (=). Tuyệt đối không được bỏ sót bất kỳ trường hợp nào trong bộ 3 này để đảm bảo tính bao phủ.

## 6. Định Dạng TC_ID (BẮT BUỘC)
- Định dạng Test Case theo số thứ tự tăng dần liên tục xuyên suốt toàn bộ Module.
- Không nhúng mã rule (BR01, BR02), phân loại (HAP/NEG/UI) hay số Step vào ID.
- Cấu trúc chung: `<<MOD>>-TC-001`, `<<MOD>>-TC-002`, `<<MOD>>-TC-003`...
*(Ví dụ: SA14-TC-001, SA14-TC-002, SA14-TC-003)*

## 7. Chiến Lược Traceability Khi Tài Liệu KHÔNG Có Mã BR/UI-FUNC

Nhiều FSD hiện đại viết theo dạng Narrative (văn xuôi + bảng diễn giải bước) mà **không có mã BR_xx hay UI-FUNC.xx**. Trong trường hợp này, áp dụng chiến lược sau:

### 7.1. Cột SC_Ref — Traceability 100% từ Bảng Phân Tích
Giá trị cột SC_Ref **BẮT BUỘC** phải lấy trực tiếp từ cột "Mã Kịch Bản (ID)" trong Bảng Tổng Hợp Test Case (Phần C) của file báo cáo phân tích yêu cầu (do AI `manual_requirement_analyzer` sinh ra). Việc này đảm bảo tính kế thừa, bao phủ 100% tài liệu và không bị sót kịch bản.
Nếu phát sinh thêm case mới chưa có trong bảng phân tích, AI phải tự tạo thêm Mã Kịch Bản (VD: SC-99) và ghi chú rõ ràng.

### 7.2. Cột Reference — Tham chiếu vị trí + trích dẫn quy tắc trong tài liệu
Nội dung Cột Reference **BẮT BUỘC** phải lấy trực tiếp từ cột "Trích dẫn tài liệu (Traceability Ctrl+F)" trong Bảng Tổng Hợp Test Case (Phần C) của file báo cáo phân tích yêu cầu (do AI `manual_requirement_analyzer` sinh ra). Việc này đảm bảo tính kế thừa, bao phủ 100% tài liệu và không bị sót kịch bản.
Nếu trong quá trình sinh Test Case mà phát sinh thêm case mới chưa có trong bảng phân tích, AI phải tự động đối chiếu và lấy trích dẫn theo đúng cấu trúc từ tài liệu gốc.

**Mục tiêu:** Reviewer đọc cột này phải hiểu ngay TC đang kiểm tra quy tắc gì, từ đâu — mà KHÔNG cần mở tài liệu gốc.

**Cấu trúc bắt buộc (2 phần ngăn cách bởi dấu ` – `):**
```
[VỊ TRÍ THAM CHIẾU] – [TRÍCH DẪN QUY TẮC NGẮN GỌN (tối đa 1-2 câu)]
```

**Quy tắc định vị (KHÔNG dùng số dòng):**
- **Tên Mục**: `Mục "Khai báo Nghiệp vụ"`
- **Tên Bảng + STT**: `Bảng "Mô tả các trường" - STT 3 cột Ngày hiệu lực`
- **Bước Lưu đồ**: `Lưu đồ Thêm mới NV - Bước 4 Kiểm tra ràng buộc`

**Quy tắc trích dẫn:**
- Trích nguyên văn hoặc diễn đạt lại **phần điều kiện/quy tắc cốt lõi** mà TC đang kiểm tra.
- Giới hạn **tối đa 30 từ**. Cắt bỏ phần diễn giải dài dòng, giữ lại mệnh đề điều kiện.
- Nếu quy tắc đã rõ từ tên mục, có thể bỏ trích dẫn.

**Ví dụ điền vào cột Reference:**

| Trường hợp | Reference mẫu |
|:---|:---|
| Validation ngày | `Mục "Khai báo Nghiệp vụ" - P13: "Ngày HLực, Ngày HHLực đều phải >= Ngày hệ thống và HHLực >= HLực"` |
| Mã tự sinh | `Bảng Table 2 - STT Mã NV: "số duy nhất, tự tăng 2 chữ số từ 01 đến 99"` |
| Lưu đồ | `Lưu đồ Thêm mới NV - Bước 5: "Lưu thành công ở trạng thái Chờ duyệt"` |
| Ràng buộc cascade | `Mục "Khai báo SPDV chi tiết" - P32: "Ngày HLực cha <= Ngày HLực con <= Ngày HLực SPDV cấp con"` |

### 7.3. Tổng hợp quy tắc mapping
| Loại tài liệu | TC_ID | SC_Ref | Reference |
|---|---|---|---|
| FSD có mã | `SA09-TC-001` | `SC-01` | `Mục I.2.1` |
| FSD Narrative | `SA14-TC-001` | `SC-02` | `Tab SPDV - STT 14` |

## 8. Xuất File Excel (BẮT BUỘC)
Không in bảng ra Chat. Phải chạy Script Python (`pandas`, `openpyxl`) tạo file `.xlsx` gồm 1 sheet **"Test Cases"** với đúng 19 cột sau:
- A=TC_ID | B=SC_Ref | C=Reference | D=Feature | E=Module | F=Title
- G=Type | H=Priority | I=Precondition
- J=Steps | K=Expected | L=Note
- M-S: Các cột thực thi (để trống).

*Lưu ý:* 
- **Feature (Tính năng cha):** Là tên tính năng lớn (Ví dụ: Khai báo Nghiệp vụ).
- **Module (Tính năng con):** Là tên tính năng phụ, màn hình con hoặc luồng rẽ nhánh cụ thể (Ví dụ: Thêm mới Nghiệp vụ).

## 9. Luồng Thực Thi (Workflow)
1. Parse tài liệu: Liệt kê **Logic điều kiện ẩn (LOG-xxx)** và **Chức năng UI (UI-xxx)**.
   - Nếu tài liệu Narrative → tự bóc tách và đặt mã `LOG-` theo Mục 7.1.
2. Kiểm tra quy tắc **Tách riêng** (Không gộp trạng thái).
3. Viết và chạy Script Python tạo file.
4. Thông báo đường dẫn file cho User bằng Tiếng Việt.

## Anti-Patterns 

- ❌ Gộp nhiều bước chạy 1 lần  (PHẢI tuần tự)
- ❌ Tự đoán business logic khi chưa hỏi user 
- ❌ Bỏ qua bước phân tích Ambiguity 
- ❌ Sinh test data chung chung / placeholder
- ❌ Rút gọn hoặc bỏ sót test case khi mapping sang bảng
- ❌ Sinh tất cả test cases 1 lần cho hệ thống lớn (phải chia module)
- ❌ Chỉ có Happy Path, thiếu Negative/Boundary cases (QUICK)
- ❌ Test Steps mơ hồ, không ghi rõ dữ liệu nhập
- ❌ Sử dụng tên button chung chung (OK, Confirm, Lưu) thay vì tên chính xác trong tài liệu.
- ❌ Expect bản ghi "biến mất" khỏi màn hình Chờ duyệt/Pending sau khi thao tác (phải là cập nhật trạng thái).
- ❌ Thiếu kịch bản kiểm thử cho bộ 3 giá trị (>, <, =) đối với các quy tắc so sánh nghiệp vụ.