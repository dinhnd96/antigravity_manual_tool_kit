---
name: qa_test_case_generator
description: Kỹ năng Senior QA Lead phân tích URD/BRD để sinh bộ Test Case chuẩn Enterprise (Level B2) với kỹ thuật tách biệt kịch bản và Expected Result 4 lớp.
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
- **Giữ nguyên tên field/item**: Lấy đúng và đầy đủ tên các field, item, button... từ tài liệu. Tuyệt đối không cắt gọn, rút gọn hoặc tự ý thêm thắt.
- **Xử lý tài liệu DOCX**: Nếu tài liệu có ảnh (Mockup, Flowchart), ưu tiên sử dụng lệnh giải nél (truy cập `word/media/`) để lấy ảnh. Phân tích 2-3 hình ảnh cốt lõi (Vision/OCR) để hiểu sâu về thiết kế UI và Flow mà text không diễn đạt hết.
 **Xử lý Q&A hiện có (Nếu có)**:
   - Nếu tài liệu đã có mục **"PHẦN B: DANH SÁCH CẢNH BÁO & Q&A"** với cột "Câu trả lời của BA" đã được điền: AI **BẮT BUỘC** đọc kỹ các câu trả lời này để cập nhật vào logic nghiệp vụ tổng thể.


## 2. Mục Tiêu Sinh Test Case
Sinh đồng thời 3 tập TC, đảm bảo **không trùng nội dung**:
1. **(A) TC theo BR (Business Rules)**: 1–8 TC/BR (≥1 Happy + ≥1 Negative; thêm Boundary/Calculation nếu cần). Tập trung vào logic (mandatory, auto-code, hiệu lực, auto-status...).
2. **(B) TC theo Chức năng UI**: Mỗi chức năng UI sinh TC riêng, **chỉ kiểm hành vi bề mặt UI** (điều hướng, đóng/mở form, disabled/enabled, pagination...), KHÔNG lặp lại logic đã cover ở BR.
3. **(C) TC theo Luồng nghiệp vụ (End-to-End)**: Đi luồng xuyên suốt các chức năng. KHÔNG tách test lắt nhắt từng step để tránh trùng với TC-BR.

## 3. Quy Tắc "Tách Riêng Test Case" & "Không Trùng"
- **TÁCH RIÊNG TUYỆT ĐỐI**: Mỗi Test Case chỉ kiểm tra một điều kiện, một trạng thái hoặc một luồng cụ thể. 
- **CẤM GỘP**: Không gộp nhiều trường hợp hoặc nhiều trạng thái (Status/State) vào cùng một TC để tránh rủi ro sót case khi thực thi.
- **Note only**: Nếu một ý nghĩa đã được cover bởi TC khác, KHÔNG tạo TC mới; thay vào đó thêm 1 dòng Note: "Đã cover ở TC_ID=<<ID>> (Module=<<...>>, URD_Ref=<<...>>, BR_Ref=<<...>>)".

## 4. Hướng Dẫn Viết Test Case
- **Title (Tiêu đề)**: Rõ ràng, mô tả trực diện mục tiêu. Đọc vào hiểu ngay hành vi test và kỳ vọng.
- **Precondition**: Nêu rõ vai trò, tham số, ngày T, trạng thái đầu vào. **BẮT BUỘC** đánh số thứ tự (1, 2...) và ngắt dòng kể cả khi chỉ có 1 ý. Tên tính năng phân quyền phải lấy theo tên tính năng to/chính trong tài liệu.
- **Steps**: Đánh số rõ ràng, tối đa 4–8 bước. Gắn liền với kịch bản cụ thể, không dùng mẫu chung chung. **Test Data trong các step phải cụ thể**, trích xuất hoặc tự thiết kế mô phỏng trực tiếp từ đặc tả yêu cầu. Tuyệt đối không dùng placeholder hay từ ngữ chung chung kiểu `nhập dữ liệu hợp lệ`, mà phải diễn đạt rõ giá trị (vd: `nhập Mã = 'A123'`).
- **Expected Result**: Đảm bảo đủ 4 lớp dữ liệu (Bắt buộc xuống dòng từng ý):
  - (i) Nghiệp vụ/Logic: Kết quả xử lý tương ứng.
  - (ii) UI: Cập nhật màn hình (Toast, Popup, thông báo lỗi).
  - (iii) Trạng thái bản ghi: Trạng thái dữ liệu (vd: Chờ duyệt/Đã duyệt). **TUYỆT ĐỐI KHÔNG** đề cập đến Audit Log.
  - (iv) Output: Tập tin xuất ra hoặc thông báo đi kèm.

## 5. Quy Tắc Chống Lỗi Logic
- **Xem/Đóng**: Không làm thay đổi trạng thái bản ghi.
- **Trường tự sinh**: Không test Negative validation trên các trường hệ thống tự gán (ngày tạo, người tạo).
- **State Transition**: Phải có đủ kịch bản cho tất cả chiều chuyển đổi (xuôi/ngược) của trạng thái dữ liệu.
- **Trace_ID**: Sử dụng chuỗi ngắn (vd: `BR03-AUTOCODE`, `UI-FILTER-BASIC`).

## 6. Định Dạng TC_ID (BẮT BUỘC)
- Không nhúng mã rule (BR01, BR02) hay số Step vào ID.
- **TC-BR**: Cấu trúc: `<<MOD>>-BR-HAP-001`, `<<MOD>>-BR-NEG-001`.
- **TC-UI**: Cấu trúc: `<<MOD>>-UI-001`, `002`...
*(Ví dụ: SA14-BR-HAP-001, SA14-UI-001)*

## 7. Chiến Lược Traceability Khi Tài Liệu KHÔNG Có Mã BR/UI-FUNC

Nhiều FSD hiện đại viết theo dạng Narrative (văn xuôi + bảng diễn giải bước) mà **không có mã BR_xx hay UI-FUNC.xx**. Trong trường hợp này, áp dụng chiến lược sau:

### 7.1. Cột BR_Ref — Đặt mã Logic tự định nghĩa
Bóc tách từng "điều kiện logic ẩn" trong văn bản và đặt mã theo pattern:
`LOG-[KHU_VỰC]-[MÔ_TẢ_NGẮN]`

Ví dụ:
- `LOG-TAB-SPDV-FILTER-DATE` — Logic lọc theo ngày hiệu lực ở Tab SPDV
- `LOG-TREE-HYPERLINK-LEAF` — Logic hiển thị hyperlink khác nhau theo cấp cuối/trung gian
- `LOG-CODEPI-STATUS` — Logic trạng thái Code phí (Chờ gán/Hủy/Ngừng)

### 7.2. Cột URD_Ref — Tham chiếu vị trí trong tài liệu
Tuyệt đối KHÔNG dùng số dòng. Tham chiếu theo:
- **Tên Mục**: `Mục "Xem thông tin SPDV - Tab SPDV"`
- **Tên Bảng + STT**: `Bảng "Mô tả các trường" - STT 5 cột Code phí`
- **Bước Lưu đồ**: `Lưu đồ SPDV - Bước 6.2 Lọc nâng cao`

Ví dụ điền vào cột URD_Ref:
`Tab SPDV - Bảng Mô tả trường - STT 2 (Mã SPDV)`
`Lưu đồ Tra cứu cây - Bước 8.1, 8.2`

### 7.3. Cột Trace_ID — Từ khóa ngắn để lọc nhanh
Dùng pattern ngắn gọn để filter/search trong Excel:
`[MODULE]-[TÍNH_NĂNG]-[LOẠI]`

Ví dụ: `SA14-TAB1-FILTER`, `SA14-TREE-NAV`, `SA14-DETAIL-SPDV`

### 7.4. Tổng hợp quy tắc mapping
| Loại tài liệu | TC_ID | BR_Ref | URD_Ref | Trace_ID |
|---|---|---|---|---|
| FSD có mã | `SA09-BR-HAP-001` | `BR_01` | `Mục I.2.1` | `BR01-VALIDATE` |
| FSD Narrative | `SA14-BR-HAP-001` | `LOG-TAB-FILTER-DATE` | `Tab SPDV - STT 14` | `SA14-TAB1-FILTER` |
| TC-UI | `SA14-UI-001` | `UI-SPDV-GRID` | `Bảng Mô tả trường - STT 2` | `SA14-UI-GRID-MA` |

## 8. Xuất File Excel (BẮT BUỘC)
Không in bảng ra Chat. Phải chạy Script Python (`pandas`, `openpyxl`) tạo file `.xlsx` gồm 1 sheet **"Test Cases"** với đúng 21 cột sau:
- A=TC_ID | B=BR_Ref | C=URD_Ref | D=Module | E=Feature | F=Title
- G=Type | H=Category | I=Priority | J=Precondition
- K=Steps | L=Expected | M=Trace_ID | N=Note
- O-U: Các cột thực thi (để trống).

## 9. Luồng Thực Thi (Workflow)
1. Parse tài liệu: Liệt kê **Logic điều kiện ẩn (LOG-xxx)** và **Chức năng UI (UI-xxx)**.
   - Nếu tài liệu có mã BR/UI-FUNC → dùng trực tiếp.
   - Nếu tài liệu Narrative → tự bóc tách và đặt mã `LOG-` theo Mục 7.1.
2. Sinh **TC-BR** trước (1-8 TC/LOG).
3. Sinh **TC-UI** sau, không lặp lại logic đã cover ở TC-BR.
4. Kiểm tra quy tắc **Tách riêng** (Không gộp trạng thái).
5. Viết và chạy Script Python tạo file.
6. Thông báo đường dẫn file cho User bằng Tiếng Việt.

## Anti-Patterns 

- ❌ Gộp nhiều bước chạy 1 lần  (PHẢI tuần tự)
- ❌ Tự đoán business logic khi chưa hỏi user 
- ❌ Bỏ qua bước phân tích Ambiguity 
- ❌ Sinh test data chung chung / placeholder
- ❌ Rút gọn hoặc bỏ sót test case khi mapping sang bảng
- ❌ Sinh tất cả test cases 1 lần cho hệ thống lớn (phải chia module)
- ❌ Chỉ có Happy Path, thiếu Negative/Boundary cases (QUICK)
- ❌ Test Steps mơ hồ, không ghi rõ dữ liệu nhập