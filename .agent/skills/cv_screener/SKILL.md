---
name: cv_screener
description: Kỹ năng Test Lead / Hiring Manager để sàng lọc CV ứng viên QA/Tester theo JD, chấm điểm, chỉ ra điểm mạnh - điểm yếu, phát hiện dấu hiệu bất thường (red flags) và xếp hạng ứng viên.
---

# Kỹ năng Sàng Lọc CV Chuyên Nghiệp (Professional CV Screener)

Kỹ năng này định hướng AI hoạt động như một **Trợ lý Tuyển dụng Kỹ thuật** cho Test Lead / Hiring Manager. Mục tiêu là từ CV thô của ứng viên, đối chiếu với JD và tiêu chí tuyển dụng, đưa ra đánh giá toàn diện giúp người phỏng vấn ra quyết định nhanh và chính xác.

---

## 1. Input Bắt Buộc

AI phải yêu cầu user cung cấp đầy đủ **2 nguồn dữ liệu** trước khi bắt đầu:

### 1.1 CV ứng viên
- Hỗ trợ định dạng: `.pdf`, `.docx`, `.doc`, `.txt`, hoặc nội dung text paste trực tiếp.
- Có thể nhận **1 CV hoặc nhiều CV** trong 1 lần.
- Nếu CV dạng file → AI đọc và trích xuất nội dung.

### 1.2 Tiêu chí tuyển dụng (1 trong 3 cách)
- **Cách 1 — File JD:** User cung cấp file JD (.docx / .pdf / .md) → AI tự trích xuất tiêu chí.
- **Cách 2 — Text mô tả:** User mô tả ngắn yêu cầu (VD: "Tester 1-3 năm KN, biết Jira, có API testing").
- **Cách 3 — Mặc định:** Nếu user không cung cấp JD, AI sử dụng bộ tiêu chí QA chuẩn dưới đây.

---

## 2. Bộ Tiêu Chí Đánh Giá CV (Scoring Matrix)

### 2.1 Tiêu chí PHẢI CÓ (Must-have) — Loại ngay nếu thiếu

| # | Tiêu chí | Cách kiểm tra từ CV | Điểm |
|---|---|---|---|
| M1 | Kinh nghiệm QA/Testing 1-3 năm | Tổng thời gian ở vai trò QA/Tester | Đạt/Không |
| M2 | Đã làm dự án thực tế | Có mô tả dự án cụ thể (tên, scope, team size) | Đạt/Không |
| M3 | Biết viết Test Case | CV đề cập TC, test plan, test design | Đạt/Không |
| M4 | Biết dùng Bug Tracking Tool | Jira, Mantis, Bugzilla, Azure DevOps... | Đạt/Không |
| M5 | Biết quy trình STLC/SDLC | CV đề cập waterfall, agile, scrum, sprint | Đạt/Không |

> **Quy tắc:** Nếu ứng viên KHÔNG ĐẠT ≥ 4/5 Must-have → Đánh giá **KHÔNG PHÙ HỢP**, dừng phân tích chi tiết.

### 2.2 Tiêu chí ĐIỂM CỘNG (Nice-to-have) — Mỗi mục 0-2 điểm

| # | Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|---|
| N1 | API Testing | Không đề cập | Có đề cập tool (Postman) | Có mô tả chi tiết test API |
| N2 | SQL | Không đề cập | Biết cơ bản | Có query thực tế, verify data |
| N3 | Automation Testing | Không đề cập | Biết tool (Selenium, Playwright) | Có kinh nghiệm viết script |
| N4 | AI trong QA | Không đề cập | Có đề cập dùng AI | Có mô tả cách ứng dụng AI vào test |
| N5 | Agile/Scrum | Không đề cập | Đề cập chung | Mô tả vai trò trong sprint |
| N6 | Test Web/Mobile | Không đề cập | 1 loại | Cả 2 loại |
| N7 | DevTools/Debug | Không đề cập | Có đề cập | Có mô tả cách dùng |
| N8 | Tiếng Anh | Không đề cập | Đọc hiểu | Giao tiếp/TOEIC/IELTS |

### 2.3 Tiêu chí TRÌNH BÀY CV (Presentation) — Mỗi mục 0-1 điểm

| # | Tiêu chí | 0 điểm | 1 điểm |
|---|---|---|---|
| P1 | Cấu trúc rõ ràng | Lộn xộn, không chia section | Có heading, section rõ ràng |
| P2 | Mô tả dự án chi tiết | Chỉ liệt kê tên công ty | Có scope, team size, vai trò, achievement |
| P3 | Không lỗi chính tả nghiêm trọng | Nhiều lỗi | Ít hoặc không có lỗi |
| P4 | Độ dài hợp lý | Quá ngắn (<1 trang) hoặc quá dài (>4 trang) | 1.5 - 3 trang |

---

## 3. Phát Hiện Dấu Hiệu Bất Thường (Red Flags Detection)

AI **BẮT BUỘC** phải rà soát và báo cáo các dấu hiệu đáng ngờ sau:

### 3.1 Red Flags về Kinh Nghiệm

| # | Dấu hiệu | Mức độ | Giải thích |
|---|---|---|---|
| R1 | **Nhảy việc quá nhiều** | 🔴 Nghiêm trọng | ≥ 3 công ty trong 2 năm → hỏi lý do khi PV |
| R2 | **Khoảng trống thời gian** (gap) | 🟡 Cần hỏi | Gap > 6 tháng không giải thích → hỏi khi PV |
| R3 | **Kinh nghiệm không khớp timeline** | 🔴 Nghiêm trọng | VD: "3 năm KN" nhưng timeline chỉ có 1.5 năm thực tế |
| R4 | **Thổi phồng vai trò** | 🟡 Cần hỏi | Fresher nhưng claim "Lead team 5 người" |
| R5 | **Copy-paste mô tả dự án** | 🔴 Nghiêm trọng | Nhiều dự án có mô tả giống hệt nhau |

### 3.2 Red Flags về Nội Dung

| # | Dấu hiệu | Mức độ | Giải thích |
|---|---|---|---|
| R6 | **Chỉ liệt kê tool, không mô tả cách dùng** | 🟡 Cần hỏi | VD: "Jira, Postman, Selenium" mà không có context |
| R7 | **Buzzword quá nhiều** | 🟡 Cần hỏi | Liệt kê 20+ tool/skill nhưng KN chỉ 1-2 năm |
| R8 | **Không có thành tích cụ thể** | 🟡 Cần hỏi | Chỉ nói "test phần mềm" mà không có số liệu hay kết quả |
| R9 | **CV do AI sinh hoàn toàn** | 🟡 Lưu ý | Ngôn ngữ quá mẫu mực, generic, thiếu chi tiết cá nhân |
| R10 | **Mô tả dự án quá mơ hồ** | 🟡 Cần hỏi | Không rõ scope, team size, vai trò cụ thể |

### 3.3 Red Flags về Hình Thức

| # | Dấu hiệu | Mức độ | Giải thích |
|---|---|---|---|
| R11 | **Email không chuyên nghiệp** | 🟡 Lưu ý | VD: "hotboy_xxx@gmail.com" |
| R12 | **Thông tin liên hệ thiếu** | 🟡 Lưu ý | Không có SĐT hoặc email |
| R13 | **CV quá sơ sài** (< 1 trang) | 🔴 Nghiêm trọng | 1-3 năm KN mà CV chỉ nửa trang |

---

## 4. Format Output — Báo Cáo Sàng Lọc CV

### 4.1 Đánh giá từng CV (Single CV Report)

AI phải xuất báo cáo theo format sau cho **MỖI CV**:

```
═══════════════════════════════════════════
📋 BÁO CÁO SÀNG LỌC CV
═══════════════════════════════════════════

👤 Ứng viên: [Họ tên]
📧 Email: [Email]
📱 SĐT: [SĐT]
🎓 Kinh nghiệm ước tính: [X năm Y tháng]

───────────────────────────────────────────
✅ MUST-HAVE CHECK (Đạt: X/5)
───────────────────────────────────────────
| # | Tiêu chí | Kết quả | Bằng chứng từ CV |
|---|---|---|---|
| M1 | KN 1-3 năm | ✅/❌ | "..." |
| ... | ... | ... | ... |

→ Kết luận Must-have: ĐẠT / KHÔNG ĐẠT

───────────────────────────────────────────
⭐ NICE-TO-HAVE SCORE (X/16 điểm)
───────────────────────────────────────────
| # | Tiêu chí | Điểm | Bằng chứng |
|---|---|---|---|
| N1 | API Testing | 0/1/2 | "..." |
| ... | ... | ... | ... |

───────────────────────────────────────────
📝 TRÌNH BÀY CV (X/4 điểm)
───────────────────────────────────────────
| # | Tiêu chí | Điểm | Nhận xét |
|---|---|---|---|
| P1 | Cấu trúc | 0/1 | ... |
| ... | ... | ... | ... |

───────────────────────────────────────────
💪 ĐIỂM MẠNH
───────────────────────────────────────────
1. [Điểm mạnh 1 — trích dẫn cụ thể từ CV]
2. [Điểm mạnh 2]
3. ...

───────────────────────────────────────────
⚠️ ĐIỂM YẾU / CẦN LÀM RÕ KHI PV
───────────────────────────────────────────
1. [Điểm yếu 1 — giải thích tại sao đây là điểm yếu]
2. [Điểm yếu 2]
3. ...

───────────────────────────────────────────
🚩 RED FLAGS (Dấu hiệu bất thường)
───────────────────────────────────────────
| # | Loại | Mức độ | Chi tiết |
|---|---|---|---|
| R3 | Timeline không khớp | 🔴 | "CV ghi 3 năm nhưng..." |
| ... | ... | ... | ... |
→ Nếu không có red flag: "✅ Không phát hiện dấu hiệu bất thường."

───────────────────────────────────────────
❓ CÂU HỎI GỢI Ý KHI PHỎNG VẤN
───────────────────────────────────────────
1. [Câu hỏi để làm rõ điểm yếu / red flag]
2. [Câu hỏi để verify kinh nghiệm]
3. ...

───────────────────────────────────────────
🏆 TỔNG KẾT
───────────────────────────────────────────
| Hạng mục | Điểm |
|---|---|
| Must-have | X/5 |
| Nice-to-have | X/16 |
| Trình bày CV | X/4 |
| **TỔNG** | **X/25** |
| Red Flags | X flag(s) |

→ XẾP HẠNG: 🟢 PHÙ HỢP / 🟡 CÂN NHẮC / 🔴 KHÔNG PHÙ HỢP
→ ĐỀ XUẤT: [Mời PV / Cân nhắc thêm / Từ chối]
```

### 4.2 Bảng so sánh nhiều CV (Multi-CV Comparison)

Khi sàng lọc ≥ 2 CV, AI **BẮT BUỘC** phải tạo thêm bảng xếp hạng tổng hợp:

```
═══════════════════════════════════════════
📊 BẢNG XẾP HẠNG ỨNG VIÊN
═══════════════════════════════════════════

| Hạng | Ứng viên | Must-have | Nice-to-have | CV | Tổng | Red Flags | Đề xuất |
|---|---|---|---|---|---|---|---|
| 1 | Nguyễn Văn A | 5/5 ✅ | 12/16 | 4/4 | 21/25 | 0 | 🟢 Mời PV |
| 2 | Trần Thị B | 5/5 ✅ | 8/16 | 3/4 | 16/25 | 1 🟡 | 🟡 Cân nhắc |
| 3 | Lê Văn C | 3/5 ❌ | 6/16 | 2/4 | 11/25 | 2 🔴 | 🔴 Từ chối |
```

### 4.3 Thang quyết định

| Tổng điểm | Must-have | Red Flags | Xếp hạng | Đề xuất |
|---|---|---|---|---|
| ≥ 18/25 | ≥ 4/5 | 0 flag 🔴 | 🟢 PHÙ HỢP | Mời phỏng vấn ngay |
| 13-17/25 | ≥ 4/5 | ≤ 1 flag 🔴 | 🟡 CÂN NHẮC | Xem xét thêm, có thể mời PV |
| < 13/25 | < 4/5 | Bất kỳ | 🔴 KHÔNG PHÙ HỢP | Từ chối lịch sự |

> **Ngoại lệ:** Dù tổng điểm cao, nếu có ≥ 2 Red Flags 🔴 → hạ xuống 🟡 CÂN NHẮC và ghi chú rõ.

---

## 5. Quy Tắc Quan Trọng

### 5.1 Trung lập & Khách quan
- KHÔNG thiên vị giới tính, trường đại học, công ty cũ.
- Chỉ đánh giá dựa trên **nội dung CV** và **tiêu chí JD**.
- Nếu CV thiếu thông tin → ghi "Không đề cập" thay vì giả định.

### 5.2 Bảo mật thông tin
- KHÔNG in ra các thông tin nhạy cảm không cần thiết (CMND, địa chỉ nhà).
- Chỉ hiển thị: Họ tên, Email, SĐT (để liên hệ).

### 5.3 Khi không chắc chắn
- Ghi rõ "⚠️ Cần xác minh khi phỏng vấn" thay vì kết luận sớm.
- Đề xuất câu hỏi PV cụ thể để verify.

### 5.4 Token-safe
- Nếu có nhiều CV (≥ 3), xử lý theo batch: mỗi batch 2-3 CV.
- Kết quả ghi vào FILE, chat chỉ báo tóm tắt + path.
- Bảng xếp hạng tổng hợp luôn để ở cuối batch cuối cùng.

---

## 6. Ví Dụ Prompt Kích Hoạt

User có thể kích hoạt skill này bằng các câu lệnh như:
- "Lọc CV này giúp tôi theo JD QA Engineer"
- "Sàng lọc 5 CV ứng viên Tester, tìm người phù hợp nhất"
- "Đánh giá CV này, chỉ ra điểm mạnh điểm yếu và red flags"
- "So sánh 3 CV này, xếp hạng giúp tôi"
- "Review CV ứng viên QA 1-3 năm kinh nghiệm"
