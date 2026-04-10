# 📋 BÁO CÁO REVIEW TEST CASE — SA.03 Quản lý người dùng (Lần 2)

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** SA.03- Quản lý người dùng.docx
> **Bộ Test Case:** SA03_Quản lý người dùng.xlsx
> **Ngày review:** Lần 2 - 2026-04-07

---

## 1. TÓM TẮT ĐÁNH GIÁ (SAU KHI CẬP NHẬT)

Ở lần review trước, bộ Test Case SA03 bị lỗi rất nặng do thiếu toàn bộ luồng **Thêm mới** và **Import danh sách**. Ở phiên bản file hiện tại, tôi thấy các TC này đã được bổ sung đầy đủ (`SA03-HAPPY-016` đến `SA03-NEG-019` có Note `[QA THÊM MỚI]`). Đây là một sự chuyển biến cực kỳ dứt khoát!

Tuy nhiên, soi chiếu kỹ lưỡng lại toàn bộ file, bộ SA03 vẫn còn tồn tại các **Anti-pattern** (giả định ngoài luồng thiết kế) và **Băm nhỏ luồng** (Duplicate):

| Hạng mục | Rủi ro | Chi tiết |
|:---|:---|:---|
| **Lỗi Role / Maker-Checker** | ✅ Pass | Đã áp dụng `BR_05` ở chức năng Thêm mới / Sửa, không vướng bẫy luồng duyệt PENDING. |
| **Bao phủ URD** | ✅ Pass | Đã bao phủ đủ 6 chức năng (Thêm, Import, Sửa, Xem, Tìm kiếm, Kết xuất). |
| **Giả định ngoài URD (Anti-Pattern)** | 🔴 High | 2 TC tự vẽ thêm Business Rule mà URD không hề cấm. |
| **Trùng lặp (Duplicate/Băm nhỏ)** | 🔴 High | Luồng Check Đăng nhập (Active/Inactive) bị lặp lại vô ích ở quá nhiều dòng. |

---

## 2. CHI TIẾT TỪNG LỖI CÒN TỒN ĐỌNG (ACTIONABLE FINDINGS)

### Lỗi #1: Vẽ thêm quy tắc System chưa có (Anti-Pattern)
- **`SA03-SECURITY-011`**: *Security: Chặn Admin tự khóa tài khoản của chính mình (Self-Lockout).*
  - **Lỗi:** URD hoàn toàn KHÔNG CÓ quy định cấm Admin đổi State của chính mình thành Inactive. Việc này có rủi ro thực tế (khóa chết Admin Root), nhưng nếu URD không Design tức là Hệ thống có thể không chặn. Chặn cứng ở TC sẽ báo Fake Bug.
  - **Khắc phục:** Mark tag `[PENDING BA]` để Confirm. Yêu cầu BA bổ sung BR này vào tài liệu, nếu BA từ chối bổ sung thì CẦN XÓA TEST CASE NÀY.

- **`SA03-BOUNDARY-009`**: *Tìm kiếm với từ khóa dài (>100 ký tự) hoặc chứa ký tự đặc biệt (!@#$).*
  - **Lỗi:** URD chưa có quy định giới hạn Textbox tìm kiếm bao nhiêu ký tự. Nếu test kiểu này thường 100% rớt do validate của Front-end không có, và báo Bug dev sẽ từ chối vì "Không có spec".
  - **Khắc phục:** Cần Note hỏi BA giới hạn ký tự chuẩn của khung Search là bao nhiêu, đặc biệt các ký tự Injection.

### Lỗi #2: Băm nhỏ luồng Nghiệp vụ một cách lãng phí (Duplicate)
- **`SA03-FLOW-010`**: *Flow: Đổi sang Inactive và kiểm tra chặn đăng nhập*
- **Sự cố:** Hành vi "Tài khoản Inactive thì đăng nhập bị chặn" thực chất đã được bao phủ trong bộ **SA.01 - Đăng nhập** rồi. Ở Module SA.03 (Quản lý User), ta chỉ cần check: `Edit trạng thái Inactive -> Lưu thành công -> Trạng thái trên lưới (Grid) hiển thị là Inactive` là đủ. Không nên test end-to-end bắt Dev cày lại luồng Login trong tính năng Quản trị.
- **Khắc phục:** Cần Merge/Gộp hành vi sửa Active/Inactive vào một TC Update bình thường (VD gom vào TC Sửa trạng thái thành công). Không nên tách ra thành một bộ Flow riêng cồng kềnh.

---

## 3. KẾT LUẬN & HƯỚNG BƯỚC TIẾP THEO

Bộ Test Case hiện tại (đã chứa các TC Thêm mới/Import) là khá chắc tay về mặt độ phủ.
Tuy nhiên, để đạt độ "Clean" của mức Senior:
1. Bạn hãy check với BA ngay lập tức vụ **"Admin có được tự Inactive bản thân không?"**.
2. File này vẫn nên chạy một lượt Script "Dọn dẹp" để gộp phần Inactive dư thừa và thêm tag `[PENDING BA]` vào các case Anti-pattern.

Bạn có muốn tôi viết script đi qua lượt cuối để Clean dứt điểm lỗi dư thừa này cho SA.03 không?
