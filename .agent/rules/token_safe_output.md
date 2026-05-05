# 🛡️ Token-Safe Output Rule (Anti-Truncation)

> **Mục đích:** Ngăn chặn lỗi "model's generation exceeded the maximum output token limit" bằng cách buộc AI tự động chia nhỏ output và ghi ra file thay vì in trong chat.

---

## 1. Phân loại Task theo Output Size

Trước khi bắt đầu bất kỳ task sinh nội dung nào, AI **BẮT BUỘC** phải ước lượng kích thước output:

| Level | Ước lượng | Ví dụ | Chiến lược |
|-------|-----------|-------|------------|
| **S** | < 50 dòng | Trả lời câu hỏi ngắn, fix 1 bug | Chat trực tiếp |
| **M** | 50–150 dòng | Phân tích 1 module, Q&A 1 feature | Ghi file `.md` |
| **L** | 150–400 dòng | Sinh test case 1 module, report phân tích | Ghi file `.md` + chia 2 phần |
| **XL** | > 400 dòng | Full test suite, phân tích toàn bộ US | Ghi file `.md` + chia theo module |

**Quy tắc vàng:** Nếu level ≥ M → **BẮT BUỘC** ghi ra file, KHÔNG in trong chat.

---

## 2. Chiến lược File-First (Bắt buộc cho Level ≥ M)

### 2.1. Quy trình chuẩn

```
Bước 1: AI ước lượng size → thông báo level (S/M/L/XL)
Bước 2: AI ghi kết quả vào file .md (hoặc .xlsx nếu là bảng)
Bước 3: Chat chỉ hiển thị:
   - ✅ Đường dẫn file
   - 📊 Tóm tắt 3-5 dòng (số lượng items, highlights)
   - ❓ Câu hỏi mở cần user quyết định (nếu có)
```

### 2.2. Cấm in trong chat

Các loại nội dung sau **TUYỆT ĐỐI KHÔNG** được in trong chat:
- Bảng test case (> 5 rows)
- Bảng Q&A (> 5 rows)
- Report phân tích đầy đủ
- Code block > 80 dòng
- JSON/data > 30 dòng

---

## 3. Chiến lược Chunking (Bắt buộc cho Level L, XL)

### 3.1. Nguyên tắc chia nhỏ

| Loại task | Đơn vị chia | Max items/chunk |
|-----------|-------------|-----------------|
| Phân tích yêu cầu | Theo category (Business Logic, Boundary, UI/UX) | 1 category/response |
| Sinh Test Case | Theo nhóm chức năng (Add, Edit, Delete, Search...) | 8-10 test cases/response |
| Q&A Report | Theo category | 1 category/response |
| Code generation | Theo file/component | 1 file/response |

### 3.2. Quy trình Chunking

```
Response 1:
  - Thông báo: "Task level XL. Chia thành N phần."
  - Liệt kê N phần (Table of Contents)
  - Thực hiện Phần 1 → ghi file
  - Kết thúc: "✅ Phần 1/N hoàn tất. Nói 'tiếp' để sang Phần 2."

Response 2 (sau khi user nói "tiếp"):
  - Thực hiện Phần 2 → APPEND vào cùng file hoặc ghi file mới
  - Kết thúc: "✅ Phần 2/N hoàn tất. Nói 'tiếp' để sang Phần 3."

... lặp lại đến hết.

Response cuối:
  - Tổng hợp: "✅ Hoàn tất N/N phần. File tổng hợp tại: <path>"
  - Thống kê tổng: số items, coverage summary
```

### 3.3. Append vs New File

- **Append vào cùng file** khi: các phần cùng loại (VD: test cases của các module khác nhau)
- **Ghi file mới** khi: các phần khác loại (VD: Q&A report vs Test Case)

---

## 4. Self-Check Trước Mỗi Response (CRITICAL)

AI **BẮT BUỘC** tự kiểm tra 4 câu hỏi trước khi submit response:

```
□ 1. Nội dung tôi sắp output có > 50 dòng không?
      → Có: Ghi file, KHÔNG in chat.
      
□ 2. Tôi có đang cố nhồi > 10 test cases vào 1 response không?
      → Có: Dừng lại, chia chunk.
      
□ 3. Tôi có đang lặp lại nội dung đã ghi vào file không?
      → Có: Cắt bỏ, chỉ báo đường dẫn file.
      
□ 4. Response chat của tôi có > 100 dòng không?
      → Có: Rút gọn xuống còn < 80 dòng.
```

---

## 5. Template Thông Báo Chuẩn

### 5.1. Khi bắt đầu task lớn
```
📋 **Task Level: [L/XL]**
Chia thành [N] phần:
1. [Tên phần 1] — ~[X] items
2. [Tên phần 2] — ~[X] items
...
Bắt đầu Phần 1. Nói "tiếp" sau mỗi phần để tiếp tục.
```

### 5.2. Khi hoàn thành 1 phần
```
✅ **Phần [X]/[N] hoàn tất**
📄 File: `<đường dẫn>`
📊 Tóm tắt: [2-3 dòng highlights]
👉 Nói "tiếp" để sang Phần [X+1].
```

### 5.3. Khi hoàn thành toàn bộ
```
✅ **Hoàn tất [N]/[N] phần**
📄 File tổng hợp: `<đường dẫn>`
📊 Tổng: [X] items | Coverage: [Y]%
🔄 Cần chỉnh sửa? Cho tôi biết phần nào cần update.
```

---

## 6. Quy tắc đặc biệt cho Excel Output

Khi user yêu cầu xuất Excel:
1. **Luôn ghi `.md` trước** → để user review nội dung
2. **Sau khi user confirm** → viết script Python (`openpyxl`) để convert `.md` → `.xlsx`
3. **Script phải gọn** (< 100 dòng), dùng data-driven pattern (list of dicts)
4. **KHÔNG** in nội dung Excel trong chat

---

## 7. Fallback: Khi vẫn bị cắt

Nếu response bị truncate:
1. AI **KHÔNG** bắt đầu lại từ đầu
2. AI xác định điểm bị cắt → tiếp tục từ điểm đó
3. Append phần còn lại vào file đã tạo
