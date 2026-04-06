# 📋 BÁO CÁO REVIEW TEST CASE – SA01: Đăng nhập
> **Tài liệu nguồn (URD):** `SA.01 – Đăng nhập .docx`
> **Bộ Test Case:** `SA01_Đăng nhập.xlsx`
> **Tổng TC:** 15 | **Người review:** Senior QA Lead (AI)
> **Ngày review:** 2026-04-06
> **Kết luận nhanh:** Bộ TC có chất lượng **KHÁ TỐT**, cấu trúc rõ ràng và đã bóc tách 4 lớp Expected Result. Tuy nhiên còn **7 phát hiện** cần xử lý trước khi release.

---

## I. TRACEABILITY MATRIX – Đối Soát BR vs TC

| BR_ID | Mô tả trong URD | TC Coverage | Trạng thái |
|:---|:---|:---|:---|
| **BR_01** | Một tài khoản tại 1 thời điểm chỉ đăng nhập ở 1 phiên | SA01-NEG-006, SA01-FLOW-011 | OK Đã cover |
| **BR_02** | Không đăng nhập được khi tài khoản Inactive | SA01-NEG-005 | OK Đã cover |
| **BR_03** | Tính năng "Ghi nhớ" đăng nhập nhanh lần sau | SA01-HAPPY-007 | WARN Cover nhưng thiếu case Negative |
| **BR_04** | Tích hợp EntraID, điều kiện theo nguyên tắc EntraID | SA01-HAPPY-009, SA01-NEG-010, SA01-NEG-013, SA01-NEG-015 | OK Cover đa luồng |
| **Chức năng Xem mật khẩu** | Cho phép hiển thị mật khẩu đã nhập | SA01-UI-008 | OK Đã cover |
| **Luồng nghiệp vụ chính** | Nhập user/pass > Xác thực > Vào trang chủ | SA01-HAPPY-001 | OK Đã cover |
| **Post-condition: Vào màn hình phiên trước** | Sau đăng nhập hướng đến màn hình phiên trước hoặc dashboard | SA01-HAPPY-001 | WARN Chưa kiểm tra nhánh "vào màn hình phiên trước" |
| **BR-SEC (Lockout)** | (Không có trong URD) | SA01-SECURITY-012 | ERROR Ngoài phạm vi URD |

---

## II. BẢNG PHÁT HIỆN CHI TIẾT

| # | BR_ID / TC_ID | Loại phát hiện | Mô tả sự cố / Mâu thuẫn | Mức độ | Đề xuất QA |
|:--|:---|:---|:---|:---|:---|
| 1 | **SA01-HAPPY-001** | **Format – Title** | Title "Đăng nhập thành công với thông tin hợp lệ (Luồng chính)" khá ổn nhưng thiếu mô tả hành vi điều hướng sau đăng nhập — một điểm quan trọng trong Post-condition của URD. | Low | Đổi title thành: *"Đăng nhập thành công → Hệ thống điều hướng về Dashboard hoặc màn hình phiên trước"* |
| 2 | **SA01-HAPPY-001** | **GAP – Logic** | Post-condition trong URD ghi rõ: *"Điều hướng người dùng đến màn hình ở phiên đăng nhập trước hoặc dashboard"*. TC hiện chỉ verify "vào Trang chủ" (1 nhánh), chưa có step kiểm tra nhánh "vào màn hình phiên trước" khi user đã có lịch sử đăng nhập. | **Medium** | Tách hoặc bổ sung Sub-step: *"Nếu user đã đăng nhập trước, hệ thống điều hướng đến màn hình phiên trước thay vì Dashboard"*. Cần làm rõ với BA về cơ chế session-restore. |
| 3 | **SA01-HAPPY-007** | **GAP – Thiếu Negative Case cho BR_03** | BR_03 quy định tính năng "Ghi nhớ". TC hiện cover Happy case (bật Ghi nhớ), nhưng **chưa có TC kiểm tra khi người dùng KHÔNG tích "Ghi nhớ"** – tức là sau khi đóng browser và mở lại, hệ thống phải **không** tự điền thông tin. | **Medium** | Thêm `SA01-NEG-007b`: Kiểm tra khi **không** tích "Ghi nhớ" → mở lại browser → trường Username phải trống, không tự đăng nhập. |
| 4 | **SA01-HAPPY-007** | **Format – Expected Result thiếu lớp** | Expected Result chỉ có 1 dòng duy nhất `(i) Nghiệp vụ/UI` gộp chung. Bộ chuẩn yêu cầu phân tách 4 lớp riêng biệt: (i) Logic, (ii) UI, (iii) Trạng thái, (iv) Output. | **Medium** | Tách thành: `(i) Nghiệp vụ: Cookie/Session được lưu phía client.` / `(ii) UI: Trường Username tự động điền khi mở lại trang login.` / `(iii) Trạng thái: Phụ thuộc config Cookie – ghi chú vào cột Note.` |
| 5 | **SA01-UI-008** | **Format – Expected Result thiếu lớp** | TC này chỉ có lớp `(ii) UI`, bỏ sót lớp `(i) Nghiệp vụ` (hành vi toggle show/hide không ảnh hưởng đến giá trị password thực tế). Tuy tính năng UI-only nhưng vẫn cần xác nhận không có side-effect nghiệp vụ. | **Low** | Bổ sung: `(i) Nghiệp vụ: Giá trị mật khẩu thực tế không bị thay đổi khi bật/tắt hiển thị.` |
| 6 | **SA01-FLOW-011** | **Duplicate + Flow Fragmentation** | TC này được gán Type=Happy và đặt tên là "End-to-End" nhưng **nội dung trùng hoàn toàn với BR_01** đã được cover tại `SA01-NEG-006`. Cả hai TC kiểm tra cùng một kịch bản: đăng nhập 2 browser cùng tài khoản. `SA01-FLOW-011` không phải là một E2E thực sự (không có flow xuyên màn hình hay Maker/Checker). | **High** | **Gộp hoặc xóa** `SA01-FLOW-011`. Nếu giữ lại, cần nâng cấp thành flow thật sự: *"Login → Thao tác nghiệp vụ → Bị kick session → Quay login lại"*. Hiện tại đây là Duplicate với `SA01-NEG-006`. |
| 7 | **SA01-SECURITY-012** | **Ngoài phạm vi URD – Chưa có BR tương ứng** | TC này kiểm tra cơ chế **Account Lockout sau 5 lần nhập sai**. Tính năng này **KHÔNG TỒN TẠI trong URD SA.01**. TC đã có note `[QA WARNING]` nhưng vẫn đang nằm trong bộ TC chính thức. | **High** | Chuyển TC này ra khỏi bộ TC chính thức (Backlog/Pending) và **yêu cầu BA confirm** trước. Nếu BA confirm có tính năng này → Thêm BR_05 vào URD → mới đưa TC vào. |

---

## III. PHÂN TÍCH BỔ SUNG

### 3.1 Điểm mạnh của bộ TC

- **Cấu trúc Expected Result 4 lớp** được áp dụng nhất quán ở phần lớn TC.
- **Traceability Column (OldID/Trace_ID)** giúp truy vết lịch sử tốt.
- Cover tốt các luồng lỗi EntraID (3 TC: Cancel, Timeout, Authorization).
- TC có **Note column** để ghi chú merge và design-decision còn mở.
- SA01-NEG-014 (XSS/injection validation) là điểm bảo mật chủ động, được đánh giá cao.
- SA01-NEG-015 (Authorization after Authentication) phân biệt rõ AuthN vs AuthZ — rất tốt.

### 3.2 Rủi ro tiềm ẩn chưa có TC cover

| Rủi ro | Mô tả | Khuyến nghị |
|:---|:---|:---|
| **Ambiguity BR_04** | URD chỉ ghi "điều kiện theo nguyên tắc EntraID" — rất mơ hồ. Nếu EntraID thay đổi policy (MFA, SSPR, Conditional Access) thì TC có thể lỗi thời. | Làm rõ với BA: Liệt kê cụ thể các điều kiện EntraID cần test. |
| **Session Timeout tự nhiên** | Không có TC kiểm tra hết session sau khoảng thời gian không hoạt động (Idle Timeout). | Cân nhắc thêm nếu hệ thống có cấu hình Timeout. |
| **Đăng nhập trên Mobile Browser** | Không rõ hệ thống có hỗ trợ responsive. Nếu có, cần coverage cho mobile. | Xác nhận với BA phạm vi test platform. |

---

## IV. TỔNG KẾT & ACTION PLAN

| Ưu tiên | Hành động | TC liên quan | Người thực hiện |
|:---|:---|:---|:---|
| 🔴 High | Quyết định giữ/xóa/chuyển Backlog cho SA01-SECURITY-012 sau khi BA confirm | SA01-SECURITY-012 | QA Lead + BA |
| 🔴 High | Gộp/xóa SA01-FLOW-011 do trùng với SA01-NEG-006 | SA01-FLOW-011 | QA Writer |
| 🟡 Medium | Thêm TC Negative cho BR_03 (khi không tích Ghi nhớ) | BR_03 | QA Writer |
| 🟡 Medium | Bổ sung Sub-case kiểm tra "vào màn hình phiên trước" cho SA01-HAPPY-001 | SA01-HAPPY-001 | QA Writer + BA confirm |
| 🟡 Medium | Tách Expected Result 4 lớp cho SA01-HAPPY-007 | SA01-HAPPY-007 | QA Writer |
| 🟢 Low | Bổ sung lớp (i) Nghiệp vụ cho SA01-UI-008 | SA01-UI-008 | QA Writer |
| 🟢 Low | Cải thiện Title cho SA01-HAPPY-001 để mô tả rõ hành vi điều hướng | SA01-HAPPY-001 | QA Writer |

> **Kết luận tổng thể:** Bộ TC SA01 thể hiện tư duy QA tốt, cấu trúc rõ ràng. Cần ưu tiên xử lý ngay 2 phát hiện High (Duplicate Flow và TC ngoài URD) và bổ sung 1 TC Negative cho BR_03 để đảm bảo coverage đầy đủ trước khi đưa vào regression.
