---
name: qa_test_case_generator
description: Kỹ năng Senior QA Lead phân tích URD/BRD để sinh bộ Test Case chuẩn Enterprise (Level B2) với kỹ thuật Dedup & Merge.
---

# Kỹ năng Tạo Test Case Chuẩn Enterprise (QA Test Case Generator)

Kỹ năng này định hướng AI hoạt động như một Senior QA Lead, phân tích tài liệu nguồn (URD/BRD/SRD) và sinh ra full bộ Test Case theo tiêu chuẩn Enterprise Level B2 (Chi tiết cao, Không lặp, Dễ maintain).

## 1. Mục Tiêu Sinh Test Case
Hệ thống Test Case cần được chia làm 3 tập (nhưng tuyệt đối **KHÔNG TRÙNG** nội dung):
1. **(A) Luồng nghiệp vụ (Business Flow):** End-to-End TCs.
2. **(B) TC theo BR (Business Rules):** 1-3 TC/BR (≥1 Happy + ≥1 Negative; Boundary/Calculation nếu cần). Tập trung vào điều kiện/logic (mandatory, auto-code, hiệu lực, auto-status, audit...).
3. **(C) TC theo Chức năng UI:** Mỗi chức năng UI sinh TC riêng (Happy/Negative/Boundary), **chỉ kiểm hành vi bề mặt UI**, KHÔNG lặp lại validation/logic đã cover ở BR.

## 2. Quy Tắc "Không Trùng" & Gộp (Dedup & Merge Engine)
- **Không trùng:** TC-BR tập trung logic ngầm. TC-UI chỉ kiểm UI (điều hướng, đóng/mở form, disabled/enabled, hiển thị...).
- **Gộp kiểm thử (Merge):** Nếu nhiều trường hợp là "biến thể tương tự", tạo **1 TC duy nhất** và mô tả các biến thể ở phần Steps (Ví dụ: Step 3a, 3b, 3c). Chỉ tách khi khác BR, khác luồng, hoặc setup data khác nhau.
- **Note only:** Nếu một ý nghĩa đã được cover bởi TC khác, KHÔNG viết TC mới, chỉ ghi Note: "ĐÃ COVER ở TC_ID=<<ID>>...".

## 3. Tiêu Chuẩn Viết Test Case
- **Precondition:** Rõ ràng về Vai trò (Maker/Checker), Data setup, cờ phân quyền, Ngày T.
- **Steps:** 4–8 bước. Cụ thể hành động. Đánh số 3a/3b nếu gộp biến thể.
- **Expected Result:** Bao gồm tối đa 4 lớp: (i) Logic/Nghiệp vụ DB, (ii) UI (Toast/Grid), (iii) Status/Audit Log, (iv) File/Email nếu có.
- **Phân loại:**
  - *Type:* Happy, Boundary, Negative, Integration, Calculation, Security...
  - *Category:* Smoke (Đường găng/Trọng yếu) vs Regression.
  - *Priority:* P1, P2, P3.

## 4. Định Dạng File Schema Xuất Ra
Kỹ năng yêu cầu xuất dữ liệu ra bảng Markdown hoặc CSV/Excel theo cấu trúc sau:
`TC_ID | Module | Feature | Title | Type | Category | Priority | Precondition | Steps | Expected | URD_Ref | BR_Ref | Trace_ID | Note`

### Gợi ý TC_ID:
- BR: `<<MODULE>>-BRxx-<TYPE>-NNN` (vd: FEE01-BR01-NEG-001)
- UI: `<<MODULE>>-UI-<FUNCNO>-<KEY>-NNN` (vd: FEE01-UI-01-LAYOUT-001)
- Flow: `<<MODULE>>-FLOW-<TYPE>-NNN`

## 5. Output Phụ Bắt Buộc
Bên cạnh bảng Test Case, AI phải cung cấp 2 Sheet / Phần báo cáo phụ:
1. **Sheet "Coverage":**
   - Đếm TC theo BR (Covered / GAP).
   - Đếm TC theo UI-FUNC (Covered / GAP).
2. **Sheet "Dedup_Log":**
   - Liệt kê các kịch bản có nguy cơ trùng lặp được phát hiện lúc phân tích.
   - Nêu rõ quyết định gộp vào TC_ID nào, lý do gộp.

## 6. Luồng Thực Thi Khuyến Nghị (Workflow)
1. Xác định và list toàn bộ BR_xx và UI-FUNC có trong scope.
2. Sinh **TC-FLOW** (Luồng E2E) trước.
3. Sinh **TC-BR** (Logic/API bề dưới).
4. Sinh **TC-UI** (Giao diện bề mặt) - đối chiếu kỹ để không lặp lại logic của 2 bước trên.
5. Review lại bộ TC qua bộ lọc **Merge Engine**.
6. Xuất Schema Table, Coverage và Dedup_Log.
