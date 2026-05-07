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

## 8. Tích Hợp RTK (Rust Token Killer) — BẮT BUỘC — KHÔNG NGOẠI LỆ

> **RTK đã cài sẵn** (`/Users/mac/.local/bin/rtk`, v0.37.2+).
> **Mục đích:** Lọc noise từ stdout/stderr → giảm 60-70% token tiêu thụ khi `run_command`.
> **Quy tắc tối thượng:** MỌI lệnh chạy qua `run_command` mà sinh output > 5 dòng **PHẢI** có prefix `rtk`.

### 8.1 Bảng Ánh Xạ Lệnh Bắt Buộc

| Lệnh GỐC (❌ CẤM) | Lệnh ĐÚNG (✅ BẮT BUỘC) | Ngữ cảnh |
|---|---|---|
| `python3 gen_xxx.py` | `rtk python3 gen_xxx.py` | Sinh file .docx/.xlsx |
| `python3 export_xxx.py` | `rtk python3 export_xxx.py` | Export báo cáo |
| `python3 us*_gen*.py` | `rtk python3 us*_gen*.py` | Sinh doc theo US |
| `python3 *_batch*.py` | `rtk python3 *_batch*.py` | Chạy batch data |
| `python3 merge_*.py` | `rtk python3 merge_*.py` | Merge file |
| `python3 update_*.py` | `rtk python3 update_*.py` | Update file có sẵn |
| `python3 read_*.py` | `rtk python3 read_*.py` | Đọc nội dung file |
| `python3 scripts/*.py` | `rtk python3 scripts/*.py` | Mọi script trong scripts/ |
| `pip install xxx` | `rtk pip install xxx` | Cài thư viện |
| `npm test` / `npx playwright test` | `rtk npm test` / `rtk npx playwright test` | Chạy test |
| `pytest` | `rtk pytest` | Chạy test Python |
| `git log` / `git diff` | `rtk git log` / `rtk git diff` | Git operations dài |
| `python3 -c "..."` | `rtk python3 -c "..."` | Inline Python script (đọc file, parse data) |

### 8.2 Quy Tắc Cứng (KHÔNG NGOẠI LỆ)

1. **MỌI lệnh `python3 *.py`** → PHẢI dùng `rtk python3 *.py`. Không có ngoại lệ.
2. **MỌI lệnh `python3 -c "..."`** (inline script) → PHẢI dùng `rtk python3 -c "..."`. Không có ngoại lệ, kể cả khi đã pipe qua `head`/`tail`.
3. **MỌI lệnh cài đặt** (`pip install`, `npm install`) → PHẢI dùng `rtk`.
4. **MỌI lệnh chạy test** (`pytest`, `playwright`, `npm test`) → PHẢI dùng `rtk`.
5. **Chuỗi lệnh (chain):** Mỗi lệnh trong chain đều phải có `rtk`:
   - ❌ `python3 batch1.py && python3 batch2.py`
   - ✅ `rtk python3 batch1.py && rtk python3 batch2.py`
6. **Lệnh với venv:** `rtk` đặt SAU `source activate`:
   - ✅ `source /tmp/venv/bin/activate && rtk python3 gen.py`
7. **Pipe KHÔNG miễn trừ rtk:** Kể cả khi đã pipe qua `head`/`tail`/`grep`, vẫn PHẢI có `rtk`:
   - ❌ `python3 -c "..." | head -50`
   - ✅ `rtk python3 -c "..." | head -50`
8. **Lệnh KHÔNG cần rtk** (output ngắn, < 5 dòng):
   - `which rtk`, `rtk --version`, `rtk gain`
   - `ls`, `cat file.txt | head -5`, `echo "done"`
   - `mkdir`, `cp`, `mv`, `rm` (thao tác file đơn)

### 8.3 Self-Check RTK (BẮT BUỘC trước MỖI `run_command`)

```
□ Lệnh có chứa "python" hoặc "python3"?      → THÊM rtk (kể cả python3 -c)
□ Lệnh có pipe head/tail nhưng gọi python3?  → VẪN THÊM rtk
□ Lệnh có chứa "pip" hoặc "npm"?              → THÊM rtk
□ Lệnh có chứa "pytest" hoặc "playwright"?    → THÊM rtk
□ Lệnh có chứa "git log" hoặc "git diff"?     → THÊM rtk
□ Output dự kiến > 5 dòng?                    → THÊM rtk
□ Đã gắn rtk ở ĐẦU lệnh (hoặc sau source activate)? → OK
```

### 8.4 Kiểm Tra Hiệu Quả

- Chạy `rtk gain` cuối mỗi phiên để báo cáo token đã tiết kiệm.
- Nếu Efficiency < 50% → xem xét thêm custom filter vào `.rtk/filters.toml`.