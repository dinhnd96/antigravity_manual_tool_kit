---
name: qa_test_case_generator
description: Kỹ năng Senior QA Lead phân tích URD/BRD để sinh bộ Test Case chuẩn Enterprise (Level B2) với kỹ thuật tách biệt kịch bản và Expected Result 4 lớp.
---

# Kỹ năng Tạo Test Case Chuẩn Enterprise (QA Test Case Generator)

Kỹ năng này định hướng AI hoạt động như một Senior QA Lead, phân tích tài liệu nguồn (URD/BRD/SRD) và sinh ra full bộ Test Case theo tiêu chuẩn Enterprise Level B2 (Chi tiết cao, Không dư, Không lặp).

## 1. Yêu Cầu Chung & Xử Lý Hình Ảnh
- **Giữ nguyên tên field/item**: Lấy đúng và đầy đủ tên các field, item, button... từ tài liệu. Tuyệt đối không cắt gọn, rút gọn hoặc tự ý thêm thắt.
- **Xử lý tài liệu DOCX**: Nếu tài liệu có ảnh (Mockup, Flowchart), ưu tiên sử dụng lệnh giải nél (truy cập `word/media/`) để lấy ảnh. Phân tích 2-3 hình ảnh cốt lõi (Vision/OCR) để hiểu sâu về thiết kế UI và Flow mà text không diễn đạt hết.

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
- **Steps**: Đánh số rõ ràng, tối đa 4–8 bước. Gắn liền với kịch bản cụ thể, không dùng mẫu chung chung.
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
- Không nhúng mã rule (BR01, BR02) vào ID.
- **TC-BR**: Bỏ số "0x", giữ chữ "BR". Cấu trúc: `<<MOD>>-BR-HAP-001`, `<<MOD>>-BR-NEG-001`.
- **TC-UI**: Cấu trúc: `<<MOD>>-UI-001`, `002`...
*(Ví dụ: SA09-BR-HAP-001, SA09-UI-001)*

## 7. Xuất File Excel (BẮT BUỘC)
Không in bảng ra Chat. Phải chạy Script Python (`pandas`, `openpyxl`) tạo file `.xlsx` gồm 1 sheet **"Test Cases"** với đúng 21 cột sau:
- A=TC_ID | B=BR_Ref | C=URD_Ref | D=Module | E=Feature | F=Title
- G=Type | H=Category | I=Priority | J=Precondition
- K=Steps | L=Expected | M=Trace_ID | N=Note
- O-U: Các cột thực thi (để trống).

## 8. Luồng Thực Thi (Workflow)
1. Parse URD: Liệt kê danh sách **BR_xx** và **UI-FUNC.01..0n**.
2. Sinh **TC-BR** trước (1-8 TC/BR).
3. Sinh **TC-UI** sau (Check rà soát Ma trận để mỗi UI-FUNC đều có ít nhất 1 TC).
4. Kiểm tra quy tắc **Tách riêng** (Không gộp trạng thái).
5. Viết và chạy Script Python tạo file.
6. Thông báo đường dẫn file cho User bằng Tiếng Việt.
