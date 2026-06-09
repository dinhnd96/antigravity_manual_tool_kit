---
trigger: always_on
---

# 📋 Quy Tắc Sinh Test Case Phối Hợp Model (Gemini Flash & Claude Opus)

> **Trạng thái: TẮT (DISABLED)**
>
> Để BẬT rule này, user nói: `"Bật rule multi-model"` hoặc `"Enable multi-model workflow"`.
> Để TẮT rule này, user nói: `"Tắt rule multi-model"` hoặc `"Disable multi-model workflow"`.
>
> **KHI TRẠNG THÁI LÀ "TẮT":** AI **BỎ QUA TOÀN BỘ** nội dung bên dưới và sử dụng workflow đơn model như bình thường (1 model xử lý tất cả).

---

## 0. Điều Kiện Kích Hoạt (Activation)

Rule này CHỈ có hiệu lực khi:
1. User đã nói rõ "Bật rule multi-model" trong conversation.
2. Nhiệm vụ hiện tại là **sinh Test Case** từ tài liệu spec/URD (sử dụng skill `manual_requirement_analyzer` → `qa_test_case_generator` → `qa_test_case_reviewer`).

Nếu không thỏa cả 2 điều kiện → bỏ qua rule, chạy bình thường.

---

## 1. Nguyên Tắc Phân Chia Tác Vụ (BẮT BUỘC)

### 1.1 Tác vụ xử lý thô — Sử dụng Gemini 3.5 Flash
Ưu tiên dùng Gemini Flash cho các tác vụ **cơ học, tốn token đầu vào, ít cần suy luận sâu**:

| Tác vụ | Skill liên quan | Output |
|---|---|---|
| Đọc tài liệu spec/URD gốc, trích xuất Feature List & Business Rules | `manual_requirement_analyzer` (Phần A) | `docs/temp_business_rules.md` |
| Sinh bộ test case Happy Path cơ bản và Validation UI thô | `manual_requirement_analyzer` (Phần C sơ bộ) | `docs/temp_draft_testcases.md` |
| Định dạng bảng, gộp file, đánh lại ID | `qa_test_case_generator` (Bước 5-6) | File `.xlsx` hoặc `.md` |
| Tối ưu câu chữ tiếng Việt, format output cuối | — | File deliverable cuối |

> **Mục tiêu:** Tiết kiệm tối đa quota input cho Claude Opus bằng cách để Gemini Flash "nhai" tài liệu thô trước.

### 1.2 Tác vụ tư duy logic — Khuyên dùng Claude Opus 4
Ưu tiên dùng Claude Opus cho các tác vụ **cần suy luận sâu, phân tích biên, tìm gap**:

| Tác vụ | Skill liên quan | Output |
|---|---|---|
| Phân tích Edge Cases, Race Conditions, bảo mật | `manual_requirement_analyzer` (Phần B — Hạng mục 2, 3) | `docs/temp_edge_cases.md` |
| Rà soát chéo (Review) bộ test case do Gemini sinh | `qa_test_case_reviewer` | Báo cáo GAP + lỗi logic |
| Tinh chỉnh kịch bản Integration Flow | `qa_test_case_generator` (Nhóm 5, 6) | SC bổ sung |
| Phân loại phản hồi BA (Dạng 1-8) phức tạp | `manual_requirement_analyzer` (Phần C — BA Response) | Logic chốt |

---

## 2. Quy Trình Thực Thi 3 Bước (BẮT BUỘC)

Mỗi khi nhận nhiệm vụ sinh Test Case **VÀ** rule này đang BẬT, AI phải tuân thủ nghiêm ngặt 3 bước sau:

### Bước 1: Trinh Sát (🔵 Gemini Flash)

**Input:** File spec/URD gốc (`.docx` hoặc `.md`).

**Hành động:**
1. Đọc file spec thô, trích xuất theo workflow `manual_requirement_analyzer`:
   - Phần A (Tóm tắt Nghiệp vụ): Luồng chính, module, pre-conditions.
   - Phần B sơ bộ: Các điểm mù/mâu thuẫn **CƠ BẢN** (Hạng mục 1 & 4).
2. Sinh bản thảo test case thô:
   - Happy Path cho từng module.
   - Negative Path cơ bản (FE Validation).
   - Field Validation (UI/UX).

**Output (2 file tạm):**
- `docs/temp_business_rules.md` — Tóm tắt nghiệp vụ + Feature List + Business Rules.
- `docs/temp_draft_testcases.md` — Bảng SC sơ bộ (Happy + Negative + UI cơ bản).

**DỪNG:** Chuyển sang Bước 2.

### Bước 2: Thẩm Định (🟠 Claude Opus)

**Input:** 2 file `temp_business_rules.md` và `temp_draft_testcases.md`.

> ⚠️ **QUAN TRỌNG:** Claude Opus **KHÔNG đọc spec gốc** ở bước này. Chỉ làm việc trên 2 file tóm tắt để tiết kiệm token.

**Hành động:**
1. Đọc `temp_business_rules.md` → xác định các quy tắc nghiệp vụ phức tạp, ràng buộc ẩn.
2. Đọc `temp_draft_testcases.md` → rà soát chéo theo tiêu chí `qa_test_case_reviewer`:
   - Tìm **5-10 Edge Cases nâng cao** mà Gemini bỏ sót:
     - Race conditions (concurrent edit, spam click).
     - Cascade constraints (cha-con, trạng thái phụ thuộc).
     - Boundary values bị thiếu (overflow, max length + 1).
     - Security edge cases (XSS, SQL Injection nâng cao).
     - State transition gaps (chiều chuyển đổi bị thiếu).
   - Kiểm tra **logic mâu thuẫn** giữa các SC đã sinh.
   - Kiểm tra **tính bao phủ** theo 7 nhóm TC (Happy, Negative, BVA, UI/UX, Business Logic, Data Integrity, NFR).

**Output (1 file tạm):**
- `docs/temp_edge_cases.md` — Danh sách 5-10 Edge Cases + đề xuất SC bổ sung + báo cáo GAP.

**DỪNG:** Chuyển sang Bước 3.

### Bước 3: Tổng Hợp (🔵 Gemini Flash)

**Input:** 3 file: `temp_draft_testcases.md`, `temp_edge_cases.md`, và spec gốc (nếu cần cross-check).

**Hành động:**
1. Merge `temp_draft_testcases.md` + `temp_edge_cases.md`:
   - Bổ sung các SC từ Edge Cases vào bảng tổng hợp.
   - Đánh lại ID liên tục (SC-01, SC-02, ...).
   - Phân loại lại nhóm TC theo đúng 7 nhóm chuẩn.
2. Sinh file deliverable cuối cùng:
   - Nếu đang ở Phase 1 (`manual_requirement_analyzer`): Xuất `USxx_PartA_Summary.docx` + `USxx_PartB_QA.docx`.
   - Nếu đang ở Phase 2 (`manual_requirement_analyzer` Phần C): Xuất file tổng hợp gồm Part A + B + C.
   - Nếu đang sinh TC chi tiết (`qa_test_case_generator`): Xuất file `.xlsx` theo đúng format 19 cột.
3. **Xóa bỏ các file tạm:**
   - `docs/temp_business_rules.md`
   - `docs/temp_draft_testcases.md`
   - `docs/temp_edge_cases.md`

**Output:** File deliverable chính thức (`.docx` hoặc `.xlsx`).

---

## 3. Quy Tắc Bổ Sung

### 3.1 Tương thích ngược với Skill gốc
- Rule này **KHÔNG thay thế** nội dung 3 skill gốc. Tất cả các quy tắc trong `manual_requirement_analyzer`, `qa_test_case_generator`, `qa_test_case_reviewer` **VẪN ÁP DỤNG ĐẦY ĐỦ**.
- Rule này chỉ thêm **lớp phân chia tác vụ** giữa 2 model.

### 3.2 Fallback khi chỉ có 1 model
- Nếu user đang dùng **1 model duy nhất** (VD: chỉ có Gemini hoặc chỉ có Claude), workflow vẫn chạy đúng 3 bước nhưng **cùng 1 model xử lý cả 3 bước**.
- Lợi ích: Vẫn giữ được cơ chế "sinh thô → review → tổng hợp" ngay cả khi không phối hợp multi-model.

### 3.3 Tuân thủ Token-Safe
- Mỗi bước vẫn tuân thủ `token_safe_output.md`:
  - Ghi file thay vì in chat.
  - Chat chỉ báo path + 2 dòng tóm tắt.
  - Phân batch nếu output > 200 dòng.

### 3.4 Thư mục file tạm
- Tất cả file tạm (`temp_*`) được lưu tại `docs/` trong workspace.
- **BẮT BUỘC** xóa file tạm ở cuối Bước 3.
- Nếu workflow bị gián đoạn, file tạm vẫn giữ lại để user có thể resume.

---

## 4. Self-Check Trước Mỗi Bước

```
□ Rule multi-model có đang BẬT không? → NẾU TẮT → bỏ qua, chạy bình thường.
□ Bước hiện tại là bước mấy (1/2/3)?
□ Model hiện tại có phù hợp với bước không? (Flash → Bước 1,3 | Opus → Bước 2)
□ File input cho bước này đã sẵn sàng chưa?
□ Output của bước trước có đầy đủ không?
□ Đã tuân thủ token-safe chưa?
```

---

## 5. Ví Dụ Luồng Thực Tế

```
User: "Bật rule multi-model. Phân tích US40.docx và sinh test case."

→ AI (Gemini Flash - Bước 1):
  1. Đọc US40.docx
  2. Sinh docs/temp_business_rules.md
  3. Sinh docs/temp_draft_testcases.md
  4. Báo: "✅ Bước 1 hoàn tất. 2 file tạm đã tạo. Chuyển sang Bước 2."

→ AI (Claude Opus - Bước 2):
  1. Đọc 2 file tạm
  2. Tìm 8 Edge Cases
  3. Sinh docs/temp_edge_cases.md
  4. Báo: "✅ Bước 2 hoàn tất. 8 Edge Cases đã bổ sung. Chuyển sang Bước 3."

→ AI (Gemini Flash - Bước 3):
  1. Merge 3 file
  2. Xuất testcases/US40_testcases.xlsx
  3. Xóa 3 file temp_*
  4. Báo: "✅ Hoàn tất. File: testcases/US40_testcases.xlsx (45 TC)."
```
