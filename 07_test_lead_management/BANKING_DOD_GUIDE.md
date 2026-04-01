# 🏦 DEFINITION OF DONE (DoD) CHUẨN NGÂN HÀNG
*Khắt khe - Chặt chẽ - Bảo vệ rủi ro tối đa*

Trong các dự án Fintech hoặc Ngân hàng (như ProfiX), **Definition of Done (DoD)** không chỉ là một checklist hoàn thành công việc, mà là một **"Hợp đồng bảo hiểm"** bảo vệ hệ thống khỏi những thảm họa tài chính và mất mát dữ liệu. 

Dưới đây là phân tích sâu về 3 tiêu chí cốt lõi của DoD ngân hàng và cách Test Lead thực thi chúng.

---

## 1. TIÊU CHÍ 1: 0 LỖI NGHIÊM TRỌNG (P0/P1)
Khác với các ứng dụng thương mại điện tử có thể chấp nhận lỗi nhỏ ở một vài luồng, trong Ngân hàng, rủi ro về tiền bạc (Core Banking, Phí, Chuyển khoản) và bảo mật là **Zero-Tolerance (Không khoan nhượng)**.

### a. Thế nào là lỗi P0/P1 trong Ngân hàng?
- **P0 - Blocker (Chết hệ thống / Thất thoát tiền / Mất bảo mật):**
  - Khách hàng giao dịch thành công nhưng tài khoản không trừ tiền.
  - Sai công thức tính phí hoặc lãi suất (VD: Làm tròn sai gây thất thoát hàng tỷ đồng nếu nhân theo số lượng).
  - Không có mã OTP, hoặc có thể bypass bước nhập OTP.
  - Lộ thông tin nhạy cảm của khách hàng (PII - Personally Identifiable Information).
- **P1 - Critical (Tắc nghẽn luồng nghiệp vụ chính, không có đường vòng - Workaround):**
  - Lỗi API khi truy vấn lịch sử giao dịch.
  - Không xuất/in được báo cáo chốt sổ cuối ngày cho Giao dịch viên.

### b. Cách Test Lead đảm bảo tiêu chí này:
- Quản lý chặt chẽ chu kỳ **Bug Triage**: Sàng lọc chính xác priority của bug cùng BA/PO.
- Nếu dự án bị ép tiến độ và Dev không kịp sửa hệ thống? 
  👉 **Quy tắc Waiver (Đặc cách):** Bất cứ lỗi P0/P1 nào muốn mang lên Production đều phải lập biên bản (Waiver), có kèm rủi ro thiệt hại, và đích thân Giám đốc khối (hoặc C-Level) ký duyệt chấp nhận rủi ro thì QA mới cho qua.

---

## 2. TIÊU CHÍ 2: 100% P0 KỊCH BẢN AUTO (KATALON) PASSED
Test tay chỉ đảm bảo được các tính năng *mới*, còn hệ thống Core thì hàng ngàn tính năng *cũ* hoạt động song song. Automation (Katalon Studio) lúc này đóng vai trò là "Người Gác Cổng" (Gatekeeper).

### a. Tại sao phải pass 100% cho P0?
- Các kịch bản P0 bao gồm: Đăng nhập, Vấn tin tài khoản, Chuyển tiền, Bắn API đối soát.
- Nếu kịch bản Auto P0 fail, điều đó đồng nghĩa luồng mạch máu của ngân hàng đã bị chặn. 

### b. Thực thi và Xử lý sự cố cho Auto Test P0:
- **Flaky Tests (Lỗi do kịch bản Auto bị chập chờn):** Đôi khi kịch bản Katalon fail không phải do Bug code mà do: Network chậm, Test data bị đổi, Element UI tải chậm.
  - **Hành động:** Test Lead tuyệt đối không được tự ý "Ignore" test case fail. Phải chạy kỹ lại (Re-run) kịch bản đó bằng tay để xác nhận đây là do "Tài nguyên Test" hay là do "Bug của Dev".
- **Pipeline CI/CD Tự Động:** Tích hợp bộ Katalon P0 vào Pipeline. Bất cứ bản build nào Dev đẩy lên mà Katalon báo fail 1 case P0, Pipeline tự động `Reject` (từ chối bản build), Dev phải fix ngay lập tức.

---

## 3. TIÊU CHÍ 3: RELEASE NOTE CÓ CHỮ KÝ XÁC NHẬN CỦA PO (UAT SIGN-OFF)
QA (Quality Assurance) đánh giá chất lượng phần mềm có đúng theo "Tài liệu thiết kế" hay không. Nhưng **PO (Product Owner) hoặc Business User** mới là người ra quyết định xem chất lượng đó có "Bán được" hoặc "Đem lại lợi ích kinh doanh" hay không.

### a. Bảo chứng pháp lý (Shift-Liability)
- Chữ ký xác nhận trên **UAT Sign-off** (hay Release Note) là sự đồng thuận từ Khối Nghiệp Vụ (Business) rằng: *"Tôi đã tự tay dùng thử sản phẩm này. Tôi chấp nhận cấu hình tính phí này. Tôi đồng ý chịu trách nhiệm khi nó lên Production"*.
- Nếu không có chữ ký này, khi sản phẩm ra mắt và tính sai phí, **trách nhiệm 100% đổ lên đầu QA/IT**.

### b. Một Release Note chuẩn Ngân hàng có gì?
Để PO dám ký, bạn phải cung cấp cho họ bức tranh hoàn chỉnh:
1. **Summary Scope:** Lần này hệ thống Release các tính năng nào (VD: Module Công thức tính phí PR.02).
2. **Quality Status:** Trạng thái kết quả Test (Passed 300/300 cases, Automation coverage 100%).
3. **Known Issues (Lỗi tồn đọng rủi ro thấp P2/P3):** "Hệ thống vẫn còn lỗi hiển thị sai màu nút bấm ở màn hình A, lỗi chữ tràn viền trên màn hình B. Lỗi này không ảnh hưởng tính phí." 
4. **Workaround:** "Nếu user gặp lỗi màn hình B, xin vui lòng bấm F5 (Refresh)."
5. **Approval:** Phần ký số phê duyệt (Sign-off) của PO / Trưởng phòng nghiệp vụ. Minh bạch mọi sự thật để họ quyết định.

---
*Thuộc hệ thống tài liệu [Cẩm nang Test Lead Master Guide](./TEST_LEAD_MASTER_GUIDE.md)*
