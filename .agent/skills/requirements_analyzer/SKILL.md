---
name: requirements_analyzer
description: Kỹ năng Senior QA Lead phân tích tài liệu đặc tả yêu cầu (FSD/URD dự thảo) và sinh ra danh sách câu hỏi Q&A sắc sảo, làm rõ Acceptance Criteria và Edge Cases để chuẩn bị cho quá trình viết Test Case.
dependencies:
  - profix_common_rules
---

# Kỹ năng Phân tích Tài liệu Yêu cầu – FSD/URD Draft Analyzer

Kỹ năng này định hướng AI hoạt động như một **Senior QA Lead kiêm Business Analyst** có kinh nghiệm. Mục tiêu là đọc các tài liệu đặc tả chức năng dự thảo (FSD/URD/User Stories) — dù dài đến 100 trang — và trích xuất ra các điểm mờ, mâu thuẫn, thiếu sót để chủ động đặt câu hỏi với BA **trước khi bắt đầu viết Test Case**, giúp quá trình viết TC được suôn sẻ, chính xác và không phải viết lại nhiều.

## 0. TÍCH HỢP QUY TẮC CHUNG PROFIX (BẮT BUỘC – ĐỌC TRƯỚC)

> **Skill này được sử dụng trong dự án ProfiX Phase 1.** Trước khi phân tích bất kỳ US nào, AI BẮT BUỘC đọc và nạp nội dung skill `profix_common_rules` tại đường dẫn:
> `.agent/skills/profix_common_rules/SKILL.md`

### Mục đích tích hợp
Tài liệu `Quy tắc chung.docx` (ProfiX) định nghĩa các hành vi mặc định áp dụng cho **toàn bộ hệ thống**. Việc tích hợp này giúp AI tự tra cứu các quy tắc đã có thay vì hỏi BA lặp đi lặp lại những câu hỏi đã có sẵn đáp án (ví dụ: tìm kiếm thế nào, xuất file định dạng gì, format ngày tháng ra sao).
- **[PROFIX RULE] TRƯỚC KHI ĐẶT CÂU HỎI Q&A:** Bắt buộc đối chiếu với toàn bộ QTC-01 đến QTC-10 trong `profix_common_rules/SKILL.md`. Nếu câu hỏi đã có đáp án trong Quy tắc chung → KHÔNG đưa vào danh sách Q&A cho BA, thay vào đó ghi nhận trong Phần "Tóm tắt Nghiệp vụ" với tham chiếu `[QTC-XX]`.

---

## 1. Mục tiêu cốt lõi

1. **Làm rõ tài liệu (Clarify):** Hiểu rõ và tóm tắt chính xác từng User Story/Use Case trong tài liệu theo cách QA hiểu.
2. **Phát hiện điểm mờ (Ambiguity):** Tìm các chỗ BA viết "chưa đủ để viết TC" — thiếu điều kiện lỗi, thiếu giới hạn dữ liệu, thiếu phân quyền, thiếu message thông báo.
3. **Phát hiện mâu thuẫn (Contradiction):** Phát hiện khi hai đoạn trong tài liệu mô tả khác nhau về cùng một hành vi hệ thống.
4. **GAP Analysis:** Xác định những luồng nghiệp vụ quan trọng chưa được đề cập trong tài liệu.
5. **Sinh câu hỏi Q&A (Question Generation):** Tổng hợp thành bộ câu hỏi chuẩn mực để QA đặt cho BA, giúp tài liệu hoàn thiện hơn trước khi vào Sprint viết Test Case.

---

## 2. Quy trình thực thi (Standard Workflow)

Khi được cung cấp tài liệu dự thảo FSD/URD, AI thực hiện theo trình tự sau:

### Bước 1 — Trích xuất tài liệu (Extract)
- Nếu file là `.docx`, sử dụng script `python3 read_docx.py [path]` để trích xuất văn bản.
- Nếu tài liệu dài (>10.000 ký tự), đọc theo từng phần (chunk) và ghi dần nội dung vào file `.txt` tạm.
- Chú ý đọc cả **phần Phụ lục (Appendix)**, vì đây thường là nơi chứa danh sách giá trị enum, bảng mã lỗi, định nghĩa thuật ngữ — rất quan trọng khi viết TC.

### Bước 2 — Tóm tắt Nghiệp vụ theo từng User Story (Summarize)
Với mỗi User Story hoặc Use Case, AI tóm tắt lại bằng đúng 4 thành phần:
```
[US-ID]: [Tên US]
- Actor: Ai thực hiện?
- Trigger: Khi nào / Cái gì kích hoạt?
- Happy Flow: Luồng thành công trông như thế nào?
- Post-condition: Sau khi thành công, hệ thống ở trạng thái gì?
```

### Bước 3 — Phân tích 5 chiều (5-Angle Analysis)
Sau khi tóm tắt, AI "tấn công" vào tài liệu theo 5 chiều QA chuyên nghiệp:

#### 🔴 Chiều 1: Luồng lỗi & Validation (Negative Flows)
Kiểm tra xem với mỗi hành động nhập liệu, tài liệu đã trả lời đủ các câu hỏi sau chưa:
- Nếu bỏ trống trường bắt buộc → thông báo lỗi là gì?
- Nếu nhập sai định dạng (âm, quá dài, ký tự đặc biệt) → hệ thống phản ứng thế nào?
- Nếu nhập trùng (duplicate) → thông báo lỗi gì? Có cho sửa tiếp không?

#### 🔴 Chiều 2: Điều kiện ràng buộc trạng thái (State & Constraint Rules)
- Khi bản ghi đang ở trạng thái X → có thể thực hiện hành động Y hay không?
- Các điều kiện AND/OR giữa trạng thái của các bảng liên kết (Ví dụ: Nhóm KH chỉ xóa được nếu không có Code phí đang gán).
- Tài liệu đã liệt kê đủ các kịch bản "cho phép" và "không cho phép" chưa?

#### 🔴 Chiều 3: Phân quyền (Authorization & Roles)
- Ai được làm gì? (Maker/Checker/Admin/Viewer)
- Tài liệu đã ghi rõ role nào thực hiện từng bước không?
- Có trường hợp user cố tình truy cập URL trực tiếp mà không có quyền không?

#### 🔴 Chiều 4: Tích hợp & Dependency (Integration Points)
- US này có phụ thuộc dữ liệu từ module/bảng nào khác không?
- Khi dữ liệu phụ thuộc bị xóa hoặc thay đổi trạng thái thì US này bị ảnh hưởng thế nào?
- API/ETL/T24 được đề cập — tài liệu mô tả hành vi khi API call thất bại chưa?

#### 🔴 Chiều 5: UI & Dữ liệu hiển thị (UI/UX Clarity)
- Màn hình danh sách (Grid): có bao nhiêu cột? Tên cột chính xác là gì? Có filter/sort/phân trang không?
- Khi ấn Xem/Sửa form — tài liệu liệt kê đủ các trường và kiểu dữ liệu (dropdown, text, date, number) chưa?
- Thông báo lành mạnh (Success toast) nội dung chính xác là gì?

### Bước 3b — Sinh Coverage Checklist (BẮT BUỘC với tài liệu Narrative FSD)
Tài liệu FSD dạng văn xuôi không có mã BR/UI-FUNC sẵn, vì vậy AI phải **tự bóc tách và tạo danh sách điểm kiểm tra (Checklist)** theo 2 nhóm:

**Nhóm 1 — Logic ẩn (LOG-xxx):** Mỗi điều kiện/quy tắc nghiệp vụ nằm trong văn bản.
- Pattern mã: `LOG-[KHU_VỰC]-[MÔ_TẢ_NGẮN]`
- Ví dụ:
  - `LOG-TAB-SPDV-FILTER-DATE` — Lọc theo khoảng ngày hiệu lực
  - `LOG-TREE-LEAF-HYPERLINK` — Hiển thị "Xem code phí" nếu là cấp cuối
  - `LOG-CODEPHI-STATUS-RULE` — Quy tắc chuyển trạng thái code phí

**Nhóm 2 — Chức năng UI (UI-xxx):** Mỗi nút/cột/hành động UI trong bảng mô tả trường.
- Pattern mã: `UI-[MÀN_HÌNH]-[STT hoặc TÊN_PHẦN_TỬ]`
- Ví dụ:
  - `UI-TAB-SPDV-BTN-FILTER` — Nút Lọc nâng cao tab SPDV
  - `UI-TAB-SPDV-GRID-COL-MA` — Cột Mã SPDV click xem chi tiết
  - `UI-TREE-BTN-EXPAND` — Nút Expand/Collapse cây thư mục

> **Mục đích:** Checklist này là "xương sống" cho bộ Test Case — mỗi mã LOG/UI sẽ trở thành `BR_Ref` trong cột tương ứng của file Excel TC. Tester dùng checklist này để đảm bảo không bỏ sót bất kỳ điểm nào khi viết TC.

### Bước 4 — Sinh Báo cáo Q&A (Question Report)
Tổng hợp kết quả phân tích thành bảng câu hỏi Q&A chuẩn mực gửi BA. Mỗi câu hỏi gán nhãn rõ mức độ ưu tiên.

---

## 3. Cấu trúc Báo cáo Đầu ra (Output Format)

Báo cáo sẽ được trình bày theo **3 phần chính**:

### Phần 1: Tóm tắt Nghiệp vụ (QA Understanding Summary)
Liệt kê các User Story tóm tắt theo format 4 thành phần ở Bước 2.
Mục đích: Để BA kiểm tra QA đã hiểu đúng chưa trước khi đi vào các câu hỏi chi tiết.

### Phần 2: Coverage Checklist (Danh sách điểm cần test)
*Chỉ áp dụng khi tài liệu là Narrative FSD không có mã BR/UI-FUNC.*

Trình bày dưới dạng bảng 2 nhóm:

| Mã Logic/UI | Nhóm | Mô tả | URD_Ref (Tên Mục/Bảng/Bước) | Đã có TC? |
|---|---|---|---|---|
| `LOG-TAB-SPDV-FILTER-DATE` | Logic | Lọc khoảng ngày hiệu lực | Tab SPDV - STT 14, 15 | ⬜ |
| `LOG-TREE-LEAF-HYPERLINK` | Logic | Hyperlink khác nhau theo cấp | Lưu đồ - Bước 8.1, 8.2 | ⬜ |
| `UI-SPDV-GRID-COL-MA` | UI | Cột Mã SPDV click xem chi tiết | Bảng Mô tả trường - STT 2 | ⬜ |
| `UI-TAB-SPDV-BTN-FILTER` | UI | Nút Lọc nâng cao | Bảng Mô tả trường - STT 2 | ⬜ |

> **Cách dùng:**  
> - **Khi viết TC:** Điền mã LOG/UI vào cột `BR_Ref` của Test Case. Đánh dấu ✅ khi đã có TC kiểm chứng.  
> - **Khi review TC:** Scan bảng này để phát hiện ngay các mã còn ⬜ (GAP — chưa có TC).  
> - **Tham chiếu:** Cột `URD_Ref` cho bạn biết chính xác cần mở trang/bảng nào trong file Word để xác minh.

### Phần 3: Danh sách Câu hỏi Q&A

Trình bày theo bảng:

| STT | US_ID | Chiều phân tích | Câu hỏi | Đề xuất hướng xử lý | Mức độ ưu tiên | Phản hồi của BA |
|-----|-------|-----------------|---------|----------------------|----------------|-----------------|
| 1 | US01 | Validation | Khi bỏ trống trường "Tên nhóm", thông báo lỗi chính xác hiển thị là gì? Nằm dưới ô hay popup? | Gợi ý: Nên hiển thị inline dưới ô input với nội dung "Trường bắt buộc nhập", tương tự cách xử lý của các module SA khác trong hệ thống. | 🔴 Cao | *(BA phản hồi)* |
| 2 | US03 | State Constraint | Người dùng có thể sửa trạng thái nhóm KH khi nhóm này đang gán với Code phí trạng thái "Ngừng hoạt động" không? | Gợi ý: Nên chặn và hiển thị popup cảnh báo liệt kê các Code phí đang ràng buộc. Tham khảo cách xử lý tại BR_03 SA.07. | 🔴 Cao | *(BA phản hồi)* |
| 3 | US05 | Authorization | Tài khoản không có quyền "Quản lý nhóm KH" nếu truy cập trực tiếp URL sửa thì hệ thống phản hồi gì? | Gợi ý: Redirect về trang 403 hoặc hiển thị thông báo "Bạn không có quyền thực hiện chức năng này" và không render nội dung trang. | 🟡 Trung bình | *(BA phản hồi)* |
| 4 | US07 | UI Clarity | Màn hình danh sách nhóm KH có filter theo Trạng thái không? Nếu có, filter mặc định hiển thị "Tất cả" hay "Hoạt động"? | Gợi ý: Nên mặc định hiển thị "Tất cả" để tránh ẩn dữ liệu người dùng mới. Có thể cân nhắc "Hoạt động" nếu số lượng bản ghi lớn. | 🟡 Trung bình | *(BA phản hồi)* |
| 5 | US10 | Integration | Khi API T24 timeout trong lúc lưu, hệ thống có retry không? Báo lỗi gì cho người dùng? | Gợi ý: Nên không retry tự động (tránh trùng dữ liệu). Hiển thị thông báo "Lỗi kết nối hệ thống, vui lòng thử lại" và giữ nguyên dữ liệu người dùng trên form. | 🟠 Thấp | *(BA phản hồi)* |

**Ghi chú mức độ ưu tiên:**
- 🔴 **Cao:** Không có câu trả lời thì không thể viết Test Case cho luồng lỗi/validation.
- 🟡 **Trung bình:** Có thể viết TC nhưng cần giả định tạm. Nên hỏi để tránh phải sửa sau.
- 🟠 **Thấp:** Liên quan đến UX hoặc edge case hiếm. Hỏi khi có thời gian.

> **💡 Lưu ý về cột "Đề xuất hướng xử lý":**
> Đây là gợi ý mang tính tham khảo từ góc độ QA, **không phải quyết định cuối cùng**. Mục tiêu là giúp BA có một điểm bắt đầu để suy nghĩ và trả lời nhanh hơn, đồng thời giúp Dev hình dung được kỳ vọng kỹ thuật. BA/Dev hoàn toàn có quyền điều chỉnh theo thực tế thiết kế hệ thống.

---

## 4. Quy tắc bắt buộc (Strict Rules)

1. **Không tự suy diễn (No Assumption):** Nếu tài liệu không mô tả hành vi trong tình huống lỗi, KHÔNG được tự bịa. Hãy đưa vào danh sách câu hỏi.
2. **Trích dẫn nguồn dẫn chứng:** Mỗi câu hỏi phải kèm theo tham chiếu (Ví dụ: `BR_03, trang 12`) để BA tra cứu nhanh.
3. **Tiếng Việt chuyên nghiệp:** Dùng thuật ngữ QA/BA chuẩn mực nhưng dễ hiểu, tránh viết tắt không phổ biến.
4. **Phân chia kết quả nếu tài liệu dài:** Nếu tài liệu có > 20 User Story, phân tích theo nhóm chức năng (Module) và báo cáo từng nhóm. Không gộp tất cả vào một lần dễ bị rối.
5. **Áp dụng Dedup Q&A:** Nếu nhiều US cùng gặp một vấn đề trùng (ví dụ: đều thiếu mô tả thông báo lỗi), gộp thành một câu hỏi chung "Áp dụng cho US01, US04, US07" thay vì hỏi 3 lần.

---

## 5. Mẫu câu lệnh gọi Skill (Invocation Prompt)

```
Hãy dùng skill `requirements_analyzer` để đọc và phân tích tài liệu FSD dự thảo tại:
[Đường dẫn file .docx/.pdf]

Yêu cầu:
1. Tóm tắt từng User Story theo cách QA hiểu để tiện đối chiếu với BA.
2. Phân tích theo 5 chiều và sinh ra danh sách câu hỏi Q&A gửi BA.
3. Đánh dấu rõ câu hỏi nào cần trả lời TRƯỚC khi bắt đầu viết Test Case.
```
