---
trigger: always_on
---

# 🛡️ Token-Safe Execution Rule (Chống Vượt Token)

> **Mục đích:** Ngăn chặn TRIỆT ĐỂ lỗi "model's generation exceeded the maximum output token limit".
> **Chiến lược chính:** PHÂN RÃ CÔNG VIỆC trước → Thực thi từng phần nhỏ → Ghi file thay vì in chat.
> **Nguồn duy nhất (Single Source of Truth):** Toàn bộ quy tắc chống vượt token nằm TẠI ĐÂY. Các file khác (CLAUDE.md) chỉ pointer đến file này.

---

## 1. Nguyên Tắc Vàng (KHÔNG BAO GIỜ vi phạm)

1. **KHÔNG BAO GIỜ** cố làm hết 1 task lớn trong 1 response.
2. **KHÔNG BAO GIỜ** in bảng/data > 5 dòng trong chat. Ghi file.
3. **KHÔNG BAO GIỜ** viết script > 200 dòng trong 1 response. Chia nhỏ.
4. **KHÔNG BAO GIỜ** tóm tắt lại nội dung file vừa tạo. Chỉ báo path.
5. **KHÔNG BAO GIỜ** phân tích + sinh nội dung trong cùng 1 response.
6. **KHÔNG BAO GIỜ** lặp lại yêu cầu user, mở đầu/kết thúc thừa. Đi thẳng vào việc.

---

## 2. Quy Trình Bắt Buộc — 3 Bước

### Bước 1: Đánh Giá (Luôn làm đầu tiên)

Ước lượng output → phân loại level:

| Level | Output | Hành động |
|-------|--------|-----------|
| **S** | < 50 dòng | Làm trực tiếp |
| **M** | 50–200 dòng | Ghi file, chat tóm tắt |
| **L** | 200–500 dòng | **Lập kế hoạch → chia 2-3 phần** |
| **XL** | > 500 dòng | **Lập kế hoạch → chia 4+ phần** |

**Ước lượng nhanh theo loại task:**

| Loại task | Cách đếm |
|-----------|----------|
| Sinh Test Case | 1 TC ≈ 15-20 dòng → 10 TC = ~180 dòng (Level L) |
| Phân tích yêu cầu (Q&A) | 1 câu hỏi ≈ 5-8 dòng → 20 câu = ~140 dòng (Level M-L) |
| Report phân tích | 1 section ≈ 30-50 dòng → 5 section = ~200 dòng (Level L) |
| Script Python/Code | 1 function ≈ 20-40 dòng → script 300 dòng = Level L |
| Bảng Excel (qua script) | Data + script ≈ 50 dòng/10 rows → 50 rows = Level L-XL |

### Bước 2: Lập Kế Hoạch + Chọn Chế Độ (Bắt buộc cho Level ≥ L)

Tạo WBS và xác định chế độ thực thi:

```
📋 Task Level: [L/XL]
🔄 Chế độ: [AUTO / MANUAL]
📦 Chia thành [N] phần:
| # | Tên phần | Nội dung | Ước lượng |
|---|----------|----------|-----------|
| 1 | ... | ... | ~X dòng |
[AUTO]: AI tự chạy liên tiếp tất cả phần.
[MANUAL]: Nói "tiếp" sau mỗi phần.
```

**Bảng quyết định chế độ mặc định:**

| Loại task | Chế độ | Lý do |
|-----------|--------|-------|
| Sinh TC (spec đã confirm) | 🔄 AUTO | Cơ học, không cần review giữa chừng |
| Sinh TC (spec chưa confirm) | ✋ MANUAL | Cần user review logic trước |
| Phân tích yêu cầu / Q&A | ✋ MANUAL | Cần user confirm phân tích trước |
| Export / Convert format | 🔄 AUTO | Cơ học thuần túy |
| Script Python sinh Excel | 🔄 AUTO | Cơ học, chạy script liên tiếp |
| Report tổng hợp | ✋ MANUAL | Cần user review structure |

**Chuyển đổi chế độ:** User nói "auto"/"làm hết đi" → AUTO | "manual"/"cho tôi review" → MANUAL

### Bước 3: Thực Thi Từng Phần

- Mỗi response CHỈ làm 1 phần
- Ghi kết quả vào FILE
- Chat chỉ báo: path + 2 dòng tóm tắt + "nói tiếp"

---

## 3. Giới Hạn Cứng (Hard Limits)

| Metric | Giới hạn | Vi phạm → Hậu quả |
|--------|----------|-------------------|
| Dòng chat response | ≤ 150 dòng | Bị cắt, mất nội dung |
| Test cases / response | ≤ 8 TC | Vượt token chắc chắn |
| Q&A items / response | ≤ 10 câu | Vượt token chắc chắn |
| Script Python | ≤ 200 dòng | Tách data hoặc chia script |
| Bảng in trong chat | ≤ 5 dòng | Ghi file thay vì in |

---

## 4. Chiến Lược Script-First (Cho Bảng/Excel/Data)

Khi cần sinh dữ liệu có cấu trúc (TC, report, bảng):

```
1. KHÔNG soạn nội dung trong chat rồi convert
2. Viết SCRIPT trực tiếp (Python + openpyxl)
3. Script dùng pattern data-driven: 
   - data = [(...), (...), ...]  ← gọn nhất có thể
   - 1 hàm loop ghi tất cả
4. Chạy script → báo path file output
5. Chat KHÔNG in lại nội dung file
```

Nếu data quá lớn cho 1 script:
- Script 1: Tạo file + ghi batch 1
- Script 2: Mở file đã tạo + append batch 2
- Mỗi script ≤ 200 dòng

---

## 5. Self-Check (BẮT BUỘC trước mỗi response)

```
□ Task level gì? ≥ L thì đã lập WBS chưa?
□ Response > 150 dòng? → Cắt, ghi file
□ Đang nhồi > 8 TC hoặc > 10 Q&A? → Chia batch
□ Đang tóm tắt lại file vừa tạo? → Xóa, chỉ giữ path
□ Script > 200 dòng? → Tách hoặc chia script
```

---

## 6. Khi Bị Cắt (Fallback)

Nếu response vẫn bị truncate:
1. **KHÔNG** bắt đầu lại từ đầu
2. Xác định điểm bị cắt → tiếp tục từ đó
3. Append phần còn lại vào file đã tạo
4. **Giảm batch size** cho các phần tiếp theo

---

## 7. Chiến Lược Tách File (Data-Logic Separation) — CRITICAL

> **Bài học thực tế:** Tool call (`write_to_file`, `run_command`) cũng bị tính vào output token limit. Một script Python 300 dòng trong `write_to_file` sẽ vượt limit dù chat response chỉ có 5 dòng.

### 7.1 Khi nào áp dụng
- Script sinh file `.docx`/`.xlsx` có **data array ≥ 30 rows**
- Tổng script (data + logic) ước tính **> 150 dòng**
- Đã bị lỗi "exceeded max tokens" ở lần thử trước

### 7.2 Pattern bắt buộc: 2-File Split

```
File 1: {task}_data.py     ← CHỈ chứa data (list/dict)
File 2: {task}_docx.py     ← CHỈ chứa logic (import data từ File 1)
```

**File 1 — Data only (write_to_file lần 1):**
```python
DATA = [
    ("SC-01", "Feature", "Module", "Type", "Description", 1, "Trace"),
    ("SC-02", ...),
    ...
]
```

**File 2 — Logic only (write_to_file lần 2):**
```python
from {task}_data import DATA
# ... docx/xlsx generation logic
```

### 7.3 Quy tắc cứng

| Metric | Giới hạn |
|--------|----------|
| Mỗi file `write_to_file` | **≤ 150 dòng** |
| Data array > 50 rows | **BẮT BUỘC tách file** |
| Data array > 100 rows | **Chia thành 2+ data files** (batch) |

### 7.4 Nếu vẫn bị lỗi sau khi tách

1. **Giảm tiếp:** Data file chia thành `_data_part1.py`, `_data_part2.py`
2. **Logic file import cả 2:** `from x_data_part1 import DATA as D1`
3. **Tuyệt đối KHÔNG** cố nhồi lại vào 1 file
4. **Chat response phải cực ngắn:** Chỉ gọi tool, không giải thích dài

### 7.5 Self-Check bổ sung (trước mỗi `write_to_file`)

```
□ File này bao nhiêu dòng? > 150 → TÁCH
□ Có data array không? > 30 rows → TÁCH ra file riêng
□ Chat response + tool call content có vượt ~60K tokens? → TÁCH
□ Đã bị lỗi token ở turn trước? → GIẢM 50% content mỗi file
```

---

## 8. Tích Hợp RTK (Rust Token Killer) — BẮT BUỘC

> **Để giảm thiểu token tiêu thụ và tránh context overflow khi gọi công cụ `run_command`:**
1. AI **phải luôn luôn** gắn tiền tố `rtk` trước các lệnh bash/terminal sinh ra nhiều log (VD: chạy script Python, pytest, playwright, npm test).
2. **Ví dụ đúng:** `rtk python scripts/gen_report.py`
3. **Ví dụ sai:** `python scripts/gen_report.py`
