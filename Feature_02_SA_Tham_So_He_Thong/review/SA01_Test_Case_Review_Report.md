# 📋 BÁO CÁO REVIEW TEST CASE — SA.01 Đăng nhập

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** SA.01 – Đăng nhập.docx
> **Bộ Test Case:** SA01_Đăng nhập.xlsx (14 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng | Đánh giá |
|:---|:---|:---|
| Tổng TC đã có | **14** | Phủ rộng từ Happy Path → Security |
| Lỗi Role/Luồng duyệt | **0** | ✅ Sạch bóng Maker/Checker |
| Expected Result thiếu Layer | **5/14 TC** | 🔴 Thiếu Layer (iii) và (iv) quan trọng |
| Gap nghiệp vụ | **2** | 🔴 Thiếu TC Ghi nhớ đăng nhập và xác thực EntraID |
| Lỗi Mockup Mismatch | **1** | 🟠 UI màn đăng nhập không có checkbox "Ghi nhớ" |
| Anti-pattern (Giả định BR không có URD) | **2** | 🟡 Thêm Lockout 30 phút và giới hạn 50 ký tự |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Đây là bộ TC có bộ khung tư duy chiều sâu tốt, bao gồm Security, EntraID Integration và Concurrent Session. Tuy nhiên **chất lượng Expected Result chưa đồng đều**: Nhiều TC chỉ có Layer (i) và (ii), thiếu hoàn toàn Layer (iii) Trạng thái/Audit và (iv) Output. Đây là điểm trừ lớn cần chấn chỉnh toàn bộ trước khi nghiệm thu.

---

## 2. PHÂN TÍCH MOCKUP UI

Màn hình đăng nhập thực tế (image1.png - PVcomBank) có các thành phần:
- Field: **"Tên đăng nhập"** (placeholder: "Nhập tên đăng nhập")
- Field: **"Mật khẩu"** (placeholder: "Nhập mật khẩu" + Icon Mắt hiện/ẩn mật khẩu)
- Button: **"Đăng nhập"** (màu xám khi rỗng field)

> [!WARNING]
> **Phát hiện Mockup Mismatch quan trọng:** URD có BR_03 quy định tính năng **"Ghi nhớ"** (Remember Me). Tuy nhiên, Mockup màn hình đăng nhập (image1.png) **KHÔNG hiển thị Checkbox "Ghi nhớ"** nào. Cần có `Assumption` hỏi BA/Designer trước khi viết TC. Hiện tại TC `SA01-HAPPY-007` đang giả định checkbox đó tồn tại nhưng không thể check được trên UI.

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | 1 tài khoản – 1 phiên làm việc duy nhất | SA01-NEG-006 | ✅ Có, nhưng Expected thiếu layer (iii)(iv) |
| BR_02 | Chặn tài khoản Inactive | SA01-NEG-005 | ✅ Đủ |
| BR_03 | Tính năng Ghi nhớ | SA01-HAPPY-007 | ⚠️ Có TC nhưng Mockup không có Checkbox |
| BR_04 | Tích hợp EntraID | SA01-HAPPY-009, SA01-NEG-010, SA01-NEG-013 | ✅ Phủ 3 case: Success, Cancel, Token Expired |
| General | Xem/Ẩn mật khẩu (Eye Icon) | SA01-UI-008 | ✅ Đủ |
| Security | Lockout sau sai 5 lần | SA01-SECURITY-012 | ⚠️ Giả định "30 phút" – chưa có trong URD |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI (FINDINGS)

| # | TC_ID | Loại phát hiện | Mô tả sự cố | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | SA01-NEG-002 | **Expected Result thiếu Layer** | Chỉ có Layer (i) và (ii). Thiếu `(iii) Trạng thái/Audit: Không tạo phiên làm việc (Session). (iv) Output: Không có.` | 🔴 High | Bổ sung đầy đủ 4 layer. |
| 2 | SA01-NEG-003 | **Expected Result thiếu Layer** | Chỉ có Layer (i) và (ii). Thiếu `(iii)` và `(iv)`. | 🔴 High | Bổ sung đầy đủ 4 layer. |
| 3 | SA01-NEG-004 | **Expected Result thiếu Layer + Sai cấu trúc** | Chỉ có Layer (ii). Thiếu hoàn toàn (i)(iii)(iv). Ngoài ra, Steps bỏ trống Tên đăng nhập nhưng không test case bỏ trống **cả hai cùng lúc**. | 🔴 High | Bổ sung layer (i)(iii)(iv). Thêm variant bỏ trống đồng thời cả 2 field. |
| 4 | SA01-NEG-006 | **Expected Result thiếu Layer** | Chỉ có (i) và (ii). Thiếu `(iii) Trạng thái/Audit: Phiên cũ bị ghi nhận bị terminate/kick (nếu thiết kế là Ngắt phiên cũ). (iv) Output: Không có.` | 🔴 High | Bổ sung. Đặc biệt Layer (iii) cực kỳ quan trọng cho Security của tính năng này. |
| 5 | SA01-HAPPY-007 | **Mockup Mismatch + Expected thiếu Layer** | Mockup màn đăng nhập không có Checkbox "Ghi nhớ". Expected chỉ có 1 layer (i+ii gộp chung cẩu thả). | 🟠 Medium | Ghi Note Assumption hỏi BA. Tách riêng rõ (i)(ii)(iii)(iv). |
| 6 | SA01-UI-008 | **Expected Result thiếu Layer** | Chỉ ghi Layer (ii). Thiếu `(i) Nghiệp vụ: Không gọi API lưu trạng thái nào. (iii) Trạng thái/Audit: Không đổi. (iv) Output: Không.` | 🟠 Medium | Bổ sung 3 layer còn lại (ngắn gọn cũng được). |
| 7 | SA01-HAPPY-009 | **Expected Result thiếu Layer** | Chỉ có (i)(ii). Thiếu `(iii) Trạng thái/Audit: Hệ thống nhận và lưu Token EntraID vào Session/Cookie. (iv) Output: Không có.` | 🔴 High | Bổ sung layer (iii)(iv). Layer này quan trọng để trace token khi Automation test. |
| 8 | SA01-SECURITY-012 | **Anti-Pattern (Giả định BR)** | TC tự chốt cứng `"bị tạm khóa 30 phút"` nhưng URD và các BR Table **không có rule nào quy định thời gian khoá là 30 phút**. Khoá tài khoản sau 5 lần sai thì đúng (BR của SA.03), nhưng `"30 phút"` là số tự nghĩ ra. | 🟡 Medium | Xóa cụm `"trong 30 phút"`. Thay bằng `"Tài khoản bị tạm khóa (Inactive). Cần Admin mở khóa."` theo đúng mô hình Inactive của SA.03. |
| 9 | SA01-NEG-014 | **Anti-Pattern (Giả định BR)** | TC giả định giới hạn là `"50 ký tự"` nhưng URD hoàn toàn không mention giới hạn độ dài field Tên đăng nhập. | 🟡 Medium | Xóa con số `"50 ký tự"` cụ thể. Thay bằng `"Vượt quá độ dài tối đa cho phép [cần BA xác nhận]"` và ghi Assumption vào cột Note. |
| 10 | SA01-FLOW-011 | **TC quá mơ hồ (Anti-Pattern: Vague TC)** | Steps rất tóm tắt: `"3. Kiểm tra các chức năng tại Dashboard"` — hoàn toàn không thể dùng làm checklist được. Expected chỉ có `(i)`, và phần (ii) UI không đề xuất verify gì cả trên màn Home (Dashboard). | 🟡 Low | Cụ thể hóa Step 3 thành kiểm tra các widget xuất hiện đúng (Phí định kỳ, Menu Tham số...). Bổ sung `(ii) UI: Dashboard hiển thị đúng các widget theo thiết kế (image2.png).` |

---

## 5. KẾT LUẬN & ACTION PLAN

**Ưu điểm nổi bật:**
- Bộ TC có tư duy Security rất tốt: Phủ được case Lockout, khóa Inactive, Concurrent Session và toàn bộ luồng EntraID.
- Hoàn toàn không có dấu vết Maker/Checker — rất chuyên nghiệp.

**Điểm trừ cốt lõi cần khắc phục:**
1. **5 TC thiếu Layer Expected Result** → Bổ sung đầy đủ (iii)(iv).
2. **2 TC Anti-Pattern** (giả định BR không có URD) → Xóa số liệu cụ thể, thêm Note Assumption.
3. **1 TC vague** (FLOW-011) → Cụ thể hóa Steps và UI Verification.
4. **1 TC Mockup Mismatch** (HAPPY-007 "Ghi nhớ") → Escalate cho BA để chốt thiết kế.

**📝 Tổng số TC cần sửa: 9/14** (64%)
