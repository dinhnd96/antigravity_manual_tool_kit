# 📋 BÁO CÁO REVIEW TEST CASE — SA.02 Đăng xuất

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** SA.02 – Đăng xuất.docx
> **Bộ Test Case:** SA02_Đăng xuất.xlsx (11 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng | Đánh giá |
|:---|:---|:---|
| Tổng TC đã có | **11** | Bao phủ rộng, bao gồm Security và Boundary |
| Lỗi Role/Luồng duyệt | **0** | ✅ Sạch bóng Maker/Checker |
| Expected Result thiếu Layer | **6/11 TC** | 🔴 Nhiều TC thiếu Layer (iii)(iv); TC thiếu cả Layer (i) |
| Precondition trống | **1/11 TC** | 🟠 `SA02-HAPPY-005` thiếu Precondition |
| Anti-pattern (Giả định ngoài URD) | **2 TC** | 🔴 2 TC giả định có Popup xác nhận — URD không thiết kế |
| Gap nghiệp vụ từ Mockup | **1** | 🟡 Chưa verify màn hình trung gian "Đăng xuất thành công" |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Bộ SA.02 có độ phủ chiều rộng rất tốt — đã nghĩ đến tận Boundary (SESSION_TIMEOUT=0, 1 phút) và Edge case mất mạng khi logout. Tuy nhiên, **cái bẫy lớn nhất** là 2 TC đang giả định thiết kế "Popup xác nhận khi Logout" (thậm chí tác giả đã tự note để xác nhận BA) — điều mà URD BR_02 **không hề thiết kế**. Bộ TC cần làm sạch các giả định này và bổ sung thêm TC verify màn hình trung gian "Đăng xuất thành công" từ Mockup.

---

## 2. PHÂN TÍCH MOCKUP UI VÀ MATCHING TÀI LIỆU

**Từ Mockup image1.png (Màn hình Dashboard):**
- Nút Đăng xuất nằm trong **dropdown menu** khi click icon User avatar góc trên phải.
- Menu gồm: **"Đổi mật khẩu"** / **"Thông tin NSD"** / **"Đăng xuất"**.
- **Lưu ý:** Không có bước hover vào "Tên người dùng", chỉ click thẳng icon Avatar.

**Từ Mockup image2.png (Màn hình sau Đăng xuất):**
- Hệ thống hiển thị một màn hình **trung gian riêng biệt** (Không phải chuyển thẳng về Login!):
  - Logo PVcomBank
  - Dòng tiêu đề: **"Đăng xuất thành công"**
  - Dòng phụ: **"Cảm ơn bạn đã sử dụng hệ thống ProfiX"**
  - Nút **"Đăng nhập"** để người dùng chủ động quay lại.

> [!WARNING]
> **Gap Mockup vs TC:** TC `SA02-HAPPY-001` ghi Expected: *"Chuyển hướng người dùng về màn hình Đăng nhập"* — nhưng thực tế Mockup không chuyển thẳng mà phải qua màn trung gian **"Đăng xuất thành công"** trước. Expected Result của TC này đang SAI so với thiết kế thực tế!

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | Auto Logout khi hết SESSION_TIMEOUT | SA02-SECURITY-002, SA02-BOUNDARY-006, SA02-BOUNDARY-010 | ✅ Phủ kỹ — có cả boundary & edge case |
| BR_02 | Dữ liệu chưa lưu bị mất khi Logout | SA02-NEG-003, SA02-UI-008 | ⚠️ Có, nhưng CẢ 2 TC đều giả định Popup không tồn tại trong URD |
| General | Điều hướng về màn login sau logout | SA02-HAPPY-001, SA02-HAPPY-005 | ⚠️ Expected sai — không khớp với Mockup trung gian |
| Security | Prevent Back-button attack | SA02-SECURITY-004 | ✅ Đủ |
| Security | Chặn truy cập URL nội bộ sau logout | SA02-NEG-009 | ✅ Đủ |
| Network | Mất mạng khi logout | SA02-NEGATIVE-011 | ✅ Edge case xuất sắc |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI (FINDINGS)

| # | TC_ID | Loại phát hiện | Mô tả sự cố | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | SA02-HAPPY-001 | **Expected Result sai + thiếu Layer** | Layer (ii) ghi *"Chuyển hướng về màn hình Đăng nhập"* nhưng Mockup image2 cho thấy hệ thống hiển thị màn trung gian **"Đăng xuất thành công"** trước. Layer (iv) Output cũng bị thiếu. | 🔴 High | Sửa (ii) thành: *"Hệ thống hiển thị màn hình Đăng xuất thành công ('Cảm ơn bạn đã sử dụng ProfiX') kèm nút Đăng nhập."* Bổ sung (iv). |
| 2 | SA02-SECURITY-002 | **Expected Result thiếu Layer (iii)(iv)** | Chỉ có Layer (i)(ii). Thiếu `(iii) Trạng thái/Audit: Session bị hủy trên Server. Token hết hạn. Ghi log Auto-logout event. (iv) Output: Không có.` | 🔴 High | Bổ sung đầy đủ 4 layer. |
| 3 | SA02-NEG-003 | **Anti-Pattern: Giả định Popup không có trong URD** | Step 2 ghi *"Xác nhận đăng xuất"* giả định có popup confirm. URD BR_02 chỉ nói "Dữ liệu không được lưu" — không thiết kế popup xác nhận. Tác giả đã tự note cờ đỏ. Layer (iii)(iv) cũng thiếu. | 🔴 Critical | Xóa Step 2. Giữ lại Step 1 (nhấn Đăng xuất) và Step 3 (check dữ liệu). Bổ sung Layer (iii)(iv). |
| 4 | SA02-HAPPY-005 | **Precondition trống + Expected thiếu Layer** | Precondition đang để `-` (trống). Expected chỉ có Layer (ii), thiếu (i)(iii)(iv). | 🟠 Medium | Bổ sung Precondition: *"Người dùng đã đăng nhập thành công và đang ở màn hình Dashboard."* Bổ sung đầy đủ 4 layer Expected. |
| 5 | SA02-BOUNDARY-006 | **Expected Result thiếu Layer (iii)(iv)** | Chỉ có (i)(ii) mơ hồ. Thiếu `(iii) Trạng thái/Audit: Session bị terminate, Token hủy. (iv) Output: Không có.` | 🔴 High | Bổ sung layer (iii)(iv). |
| 6 | SA02-FLOW-007 | **Expected Result thiếu Layer + Vague** | Chỉ có 1 layer (i) rất mơ hồ (*"luồng ... diễn ra liền mạch"* — không kiểm tra cụ thể gì). Steps step 2 *"vài thao tác tra cứu"* không specific. | 🟠 Medium | Cụ thể hóa Step 2 (VD: Mở menu Tra cứu code phí). Bổ sung (ii)(iii)(iv). Thêm verify màn *"Đăng xuất thành công"* ở Step 3. |
| 7 | SA02-UI-008 | **Anti-Pattern: Giả định Popup không có trong URD** | Toàn bộ TC này test một "Popup cảnh báo khi logout" chưa từng xuất hiện trong URD. Tác giả cũng đã tự note. Expected chỉ có Layer (ii). | 🔴 Critical | **Tạm thời đánh dấu TC này là `[PENDING-BA]`** và ghi Note rõ: *"TC ON HOLD — Chờ BA xác nhận có thiết kế Popup xác nhận Logout khi có unsaved data không. Nếu không có: Delete TC."* |
| 8 | SA02-BOUNDARY-010 | **Expected Result thiếu Layer + Anti-Pattern giá trị** | Expected thiếu Layer (iii)(iv). Ngoài ra ghi *"VD: 30p"* là default — giá trị này không có trong URD. | 🟡 Medium | Xóa cụm *"VD: 30p"*, thay bằng *"[cần BA xác nhận default value]"*. Bổ sung (iii)(iv). |
| 9 | SA02-NEGATIVE-011 | **Expected Result thiếu Layer (iii)(iv)** | Chỉ có (i)(ii). Thiếu `(iii) Trạng thái/Audit: Client-side Token/Cookie đã bị xóa khỏi LocalStorage dù API chưa phản hồi. (iv) Output: Không có.` | 🔴 High | Bổ sung layer (iii)(iv). |

---

## 5. KẾT LUẬN & ACTION PLAN

**Ưu điểm nổi bật:**
- Phủ Edge case mạng yếu/mất kết nối khi Logout (`SA02-NEGATIVE-011`) — Rất ít Tester nghĩ đến điều này.
- Boundary test SESSION_TIMEOUT (=1 phút, =0) là tư duy Tester chắc tay.

**Điểm trừ cốt lõi cần khắc phục:**
1. **2 TC Anti-Pattern Popup** (`SA02-NEG-003`, `SA02-UI-008`) — cần dọn dẹp khẩn cấp.
2. **Expected Result sai Mockup** (`SA02-HAPPY-001`) — Màn sau logout là trung gian "Đăng xuất thành công", không phải chuyển thẳng về Login.
3. **6/11 TC thiếu Layer (iii)(iv)** Expected Result.
4. **1 TC Precondition trống** (`SA02-HAPPY-005`).

**📝 Tổng số TC cần sửa: 9/11** (82%)

> [!NOTE]
> **Escalation cần thiết cho BA:**
> - Xác nhận hành vi sau khi nhấn Đăng xuất: Hiển thị màn trung gian "Đăng xuất thành công" hay chuyển thẳng về Login?
> - Có popup xác nhận khi logout với unsaved data không? (ảnh hưởng đến `SA02-NEG-003` và `SA02-UI-008`)
> - Default value của SESSION_TIMEOUT là bao nhiêu phút?
