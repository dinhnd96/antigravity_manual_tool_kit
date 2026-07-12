---
name: system_mapping_synthesizer
description: Kỹ năng tổng hợp tài liệu dài (FSD/SRS/URD/Sách/Syllabus/Spec) thành bộ tài liệu Mapping trực quan dạng HTML, giúp Tester và Team Lead nắm bắt toàn bộ hệ thống trong thời gian ngắn nhất.
dependencies:
  - ai_deterministic_config
---

# Kỹ năng Tổng Hợp & Mapping Hệ Thống và Tri Thức (System & Knowledge Mapping Synthesizer)

Kỹ năng này định hướng AI hoạt động như một **Senior System Analyst / Knowledge Architect**. Mục đích là "cô đọng" các tài liệu dài (FSD, SRS, URD, Sách chuyên ngành, sách kỹ năng, giáo trình, Syllabus, Technical Spec) thành **bộ tài liệu Mapping trực quan dạng HTML**, giúp bất kỳ ai có thể nắm bắt toàn bộ nội dung chỉ trong vài giờ thay vì vài ngày.

---

## 0. TỔNG QUAN PHƯƠNG PHÁP

### 0.1 Vấn đề cần giải quyết
Tài liệu đầu vào thường dài hàng chục đến hàng trăm trang, thiếu cái nhìn tổng thể (Big Picture) và chứa nhiều thuật ngữ khó hiểu. 

### 0.2 Hai Chế độ Hoạt động (Dual-Mode)
Kỹ năng này cung cấp giải pháp sinh một file HTML tương tác hoạt động theo 2 chế độ:

| Chế độ | Tài liệu đầu vào | Bộ tài liệu Mapping đầu ra (Tích hợp trong HTML) | Đối tượng đọc |
|---|---|---|---|
| **System Mode**<br>(Hệ thống) | FSD, SRS, URD, Spec kỹ thuật | 1. Cây chức năng (Feature Tree)<br>2. Ma trận phân quyền (CRUD Matrix)<br>3. Vòng đời trạng thái (State Lifecycle)<br>4. Luồng nghiệp vụ cốt lõi (Core Workflows)<br>5. Kế hoạch kiểm thử (Test Plan) | Developer, Tester, BA, PM |
| **Knowledge Mode**<br>(Tri thức) | Sách, Tài liệu nghiên cứu, Giáo trình | 1. Sơ đồ tư duy & Học thuyết cốt lõi (Mermaid Mindmaps)<br>2. Bảng thuật ngữ chuyên ngành (Glossary)<br>3. Bản phân tích chi tiết từng Chương/Bài học (Chapter Cards)<br>4. Bài học & Ứng dụng thực tế (Actionable Takeaways) | Độc giả, Nghiên cứu viên, Học viên |

### 0.3 Nguyên tắc cốt lõi

- **Nguyên tắc 1: Đọc và lập bản đồ trước, viết sau.** Tuyệt đối không viết khi chưa nắm cấu trúc tổng thể. Với sách, bắt buộc phải quét mục lục và khoảng trang thực tế trước khi đi vào phân tích chi tiết.
- **Nguyên tắc 2: Trực quan hóa bằng Mermaid + HTML-first.** Ưu tiên sơ đồ, biểu đồ dòng chảy thay vì văn xuôi dài dòng. Sinh thẳng 1 file HTML duy nhất chứa toàn bộ nội dung và Mermaid.js live render.
- **Nguyên tắc 3: Tách biệt Dữ liệu và Logic (Data-Logic Separation).** Với sách/tài liệu dài (Level L/XL, > 15 chương):
  - **File dữ liệu**: Tách thành các file Python chứa data dict/list (`data_vol1.py`, `data_vol2.py`...) để kiểm soát token. Mỗi file `write_to_file` không quá 150 dòng.
  - **File logic**: `gen_html.py` import dữ liệu và xuất ra file `.html` hoàn chỉnh.
  - Sau khi sinh xong, chạy kiểm tra trực quan và xóa toàn bộ file `.py` tạm.
- **Nguyên tắc 4: Viết cho người chưa biết gì.** Giả định người đọc chưa từng đọc tài liệu gốc. Mọi thuật ngữ phải được giải thích ngay lần đầu xuất hiện trong bảng Glossary.

---

## 1. QUY TRÌNH THỰC HIỆN (WORKFLOW)

### Phase 1: Khảo sát & Phân rã tài liệu

**Bước 1.1 — Xác định Chế độ hoạt động:**
- Tài liệu phần mềm nghiệp vụ -> Kích hoạt **System Mode**.
- Sách, Ebook, Giáo trình -> Kích hoạt **Knowledge Mode**.

**Bước 1.2 — Quét cấu trúc thực tế:**
- **System Mode**: Đọc file URD/FSD, trích xuất danh sách User Story, Module lớn và mối quan hệ phụ thuộc.
- **Knowledge Mode**: Viết script Python ngắn sử dụng thư viện thích hợp (ví dụ: `pypdf`) quét các trang đầu để trích xuất mục lục (TOC) và tìm kiếm các mốc "Tập", "Phần", "Chương", "Bài" cùng khoảng trang thực tế.

**Bước 1.3 — Xây dựng Bảng Thuật ngữ (Glossary) — BẮT BUỘC:**
- Liệt kê toàn bộ thuật ngữ chuyên ngành, từ viết tắt. Giải thích ngắn gọn bằng Tiếng Việt dễ hiểu (1-2 câu).

---

### Phase 2: Thiết kế nội dung Mapping

#### Chế độ 1: System Mode (Thiết kế Hệ thống)

**Mục 2.1.1 — Feature Tree (Cây phân rã chức năng):**
- Sử dụng Mermaid `mindmap` hoặc `flowchart` để vẽ cây phân rã chức năng từ Module lớn đến từng mã User Story (US).

**Mục 2.1.2 — Role Mapping & CRUD Matrix:**
- Bảng ma trận với hàng là Entity/Chức năng, cột là Vai trò người dùng. Ô giao nhau ghi các quyền: C, R, U, D, A, E.

**Mục 2.1.3 — State Lifecycle (Vòng đời trạng thái):**
- Vẽ State Diagram bằng Mermaid `stateDiagram-v2` cho các thực thể chính.

**Mục 2.1.4 — Integration Map & Core Workflows:**
- Vẽ sơ đồ giao tiếp hệ thống ngoài và 3-5 luồng nghiệp vụ cốt lõi bằng Mermaid `sequenceDiagram`.

#### Chế độ 2: Knowledge Mode (Thiết kế Tri thức - Sách)

**Mục 2.2.1 — Sơ đồ Học thuyết cốt lõi (Core Concepts):**
- Sử dụng Mermaid.js (`mindmap`, `flowchart TD`, `stateDiagram-v2`) để trực quan hóa các mô hình lý thuyết của sách.
- Ví dụ: Sơ đồ dòng tiền (Cashflow), Kim Tự Đồ (Cashflow Quadrant) trong sách tài chính; hoặc Sơ đồ Phễu chuyển đổi trong sách Marketing.

**Mục 2.2.2 — Phân tích chi tiết từng Chương/Bài học (Chapter Cards):**
Với mỗi chương/bài học trong sách, bắt buộc phải phân tích và trích xuất đầy đủ 4 thông tin sau:
1. **Tóm tắt cốt lõi (Summary)**: 2-3 câu tóm tắt nội dung/bối cảnh câu chuyện trong chương.
2. **Bài học rút ra (Key Takeaway)**: Giá trị tư duy tài chính/học thuật cốt lõi của chương.
3. **Ứng dụng thực tế (Actionable Step)**: Hành động cụ thể mà người đọc có thể thực hành ngay trong đời thực.
4. **Trích dẫn đắt giá (Golden Quote)**: Câu nói nổi tiếng hoặc thông điệp mạnh mẽ nhất trong chương.

---

### Phase 2.5: Sinh file HTML Tổng hợp (OUTPUT CHÍNH — BẮT BUỘC)

> **Chiến lược HTML-first:** Toàn bộ nội dung được gộp vào **1 file HTML duy nhất** có tên `{TenDuAn}_SystemMapping.html` hoặc `{TenSach}_SystemMapping.html`.

**Bước 2.5.1 — Giao diện thiết kế (Premium Dark Theme):**
- **Bảng màu tối sang trọng**: Background `#0b0f19`, Cards `#151f32`, Borders `#1f2d44`, Glowing Accents: Neon Cyan (`#00adb5`) và Neon Pink/Red (`#ff2e63`).
- **Thanh điều hướng Sticky**: Sử dụng hiệu ứng kính mờ (`backdrop-filter: blur(12px)`) chứa các nút chuyển Tab mượt mà.
- **Bố cục Tab tương tác (Tabbed Layout)**:
  - **Tab 1**: 📊 Sơ đồ tư duy (Chứa các sơ đồ Mermaid.js).
  - **Các Tab tiếp theo**: Chia theo từng "Tập", "Phần" hoặc nhóm chương của sách (giúp giao diện gọn gàng, không bị quá tải thông tin).
  - **Tab cuối**: 📖 Bảng thuật ngữ (Glossary) dạng bảng tối ưu.
- **Thanh tìm kiếm thời gian thực (Real-time Search)**: Tích hợp ô tìm kiếm bằng Javascript phía máy khách để lọc nhanh các card chương học theo từ khóa tiêu đề hoặc nội dung tóm tắt.

---

### Phase 3: Kiểm tra trực quan & Dọn dẹp

1. **Kiểm tra trực quan (Visual Verification)**:
   - Sử dụng công cụ `browser_subagent` mở file HTML trên trình duyệt để kiểm tra khả năng chuyển tab, tính năng lọc tìm kiếm và đảm bảo các sơ đồ Mermaid.js render thành công.
2. **Dọn dẹp tài nguyên tạm (System Cleanup)**:
   - Xóa bỏ toàn bộ các file Python dữ liệu tạm (`data_*.py`), script sinh HTML (`gen_html.py`) và các file txt nháp. Chỉ bàn giao duy nhất file `.html` thành phẩm cho người dùng.

---

## 2. CHECKLIST CHẤT LƯỢNG (QUALITY GATE)

Trước khi bàn giao bộ tài liệu, AI tự kiểm tra:
```
□ Cấu trúc chương học có bao phủ 100% mục lục thực tế của tài liệu/sách không?
□ Mỗi chương trong phần phân tích có đầy đủ: Tóm tắt, Bài học, Ứng dụng, Trích dẫn không?
□ Glossary có bao phủ tất cả thuật ngữ chuyên ngành trong sách không?
□ Sơ đồ Mermaid.js có hoạt động bình thường trên trình duyệt không?
□ Giao diện HTML có hỗ trợ chuyển Tab và Tìm kiếm thời gian thực không?
□ Toàn bộ các file Python tạm và file nháp đã được dọn dẹp sạch sẽ chưa?
```

---

## 3. QUY TẮC NGHIÊM NGẶT (STRICT RULES)

1. **KHÔNG sáng tạo nghiệp vụ/nội dung sách.** Chỉ tổng hợp và trình bày lại những kiến thức có trong tài liệu gốc. Nếu sách thiếu thông tin -> ghi nhận vào danh sách lưu ý, không tự bịa.
2. **KHÔNG dùng thuật ngữ không giải thích.** Mọi từ viết tắt, thuật ngữ chuyên ngành phải được định nghĩa trong bảng Glossary.
3. **ƯU TIÊN sơ đồ hơn văn xuôi.** Nếu có thể vẽ thành Mermaid Diagram -> vẽ. Chỉ dùng văn xuôi khi không thể trực quan hóa.
4. **HTML-first: Sinh thẳng 1 file HTML từ đầu.** Không sinh nhiều file `.md` rồi render ảnh rồi gộp lại. Sinh thẳng 1 file HTML với Mermaid.js live render. Tiết kiệm 3-4x token, người đọc mở 1 file là hiểu hết.
