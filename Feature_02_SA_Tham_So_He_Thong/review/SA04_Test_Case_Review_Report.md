# 📋 BÁO CÁO REVIEW TEST CASE — SA.04 Quản lý phân quyền

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** SA.04- Quản lý phân quyền.docx
> **Bộ Test Case:** SA04_Quản lý phân quyền.xlsx (Sheet: TestCases — 25 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng | Đánh giá |
|:---|:---|:---|
| Tổng TC đã có | **25** | Đầy đủ và bao phủ sâu |
| Lỗi Role/Luồng duyệt | **0** | ✅ TUYỆT VỜI! Đã tuân thủ BR_05 (Không yêu cầu duyệt). |
| Gap nghiệp vụ / Thiếu TC | **0** | ✅ Phủ đủ CRUD, Search, Export và Phân quyền (All/Partial). |
| Điểm sáng QA | Rất nhiều | 🟢 Tác giả có tư duy Boundary & Security rất tốt (RBAC, Multi-select logic). |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Bộ TC SA.04 là một trong những bộ chuẩn nhất từ trước đến nay. Tác giả không những bám sát Table 1 (CRUD-Export) mà còn hiện thực hóa rất tốt các Business Rules phức tạp như **BR_04** (Toàn quyền/vài quyền) và **BR_05** (Luồng quản trị không duyệt).
> **Điểm cộng:** Các case Boundary như `SA04-BOUNDARY-010` (Nút sửa chỉ sáng khi chọn 1 bản ghi) chứng minh tư duy UI/UX rất cứng.

---

## 2. PHÂN TÍCH MOCKUP UI VÀ MATCHING TÀI LIỆU

URD mô tả Grid và Form Thêm mới với các nút chức năng tiêu chuẩn.
Mockup (image1.png) hiển thị giao diện Danh sách với các nút điều hướng và Filter.
Các TC đã khớp 100% với các nút: **Thêm mới, Sửa, Xem, Xóa, Tìm kiếm, Tải xuống**.

---

## 3. CHI TIẾT PHÁT HIỆN LỖI (FINDING GAPS & BUGS)

| # | TC_ID / Tính năng | Mô tả sự cố (Bug Insight) | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|
| 1 | `SA04-HAPPY-006` & `007` (BR_04) | Phân quyền nhóm chức năng là một Ma trận Checkbox (Tree-view). Tác giả đã viết case chọn "Toàn quyền" và "Chọn vài quyền". | 🟢 High | Giữ nguyên. Lưu ý khi Test thực tế cần check cả trường hợp **Deselect All** sau khi đã chọn All. |
| 2 | `SA04-BOUNDARY-010` | *"Nút Sửa chỉ sáng khi tick 1 bản ghi duy nhất"* -> Đây là logic cực kỳ quan trọng để tránh lỗi Update dữ liệu hàng loạt không kiểm soát. | 🟢 Highlight | Giữ nguyên. |
| 3 | `SA04-SECURITY-024` | Test phân quyền cho chính module Phân quyền (User View-only không được phép add/sửa quyền). | 🟢 High | Giữ nguyên. Tư duy Security này giúp bộ TC đạt chuẩn audit bảo mật. |
| 4 | **Định dạng file xuất** (Export) | TC `SA04-HAPPY-020` ghi Output là `.xlsx / .csv`. URD không quy định rõ format. | 🔵 Low | (Góp ý) Nên chốt cứng 1 format là `.xlsx` theo chuẩn chung của dự án để Tester dễ verify style/header. |

---

## 4. KẾT LUẬN & ACTION PLAN

**Ưu điểm:**
- Cấu trúc 4 lớp Expected Result cực kỳ rành mạch, chuyên nghiệp.
- Không vướng bẫy Maker/Checker.
- Bám sát URD đến từng BR nhỏ nhất.

**Nhược điểm:**
- Hầu như không có lỗi logic hay gap nghiệp vụ nào đáng kể.

**📝 Đề xuất Hành động:**
Bộ TC này **ĐẠT CHUẨN (PASS)**. Không cần chỉnh sửa logic hay chạy script update. Có thể đóng gói để chuyển sang giai đoạn Test Execution.
