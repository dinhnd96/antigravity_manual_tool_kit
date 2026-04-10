# 📋 BÁO CÁO REVIEW TEST CASE — SA.10 Quản lý danh sách Job sinh dữ liệu phí định kỳ

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** I.1.1.1. SA.10- Quản lý danh sách Job sinh dữ liệu phí định kỳ.docx
> **Bộ Test Case:** SA10_Quan_Ly_Job_Phi_Final_Standard.xlsx (Sheet: TestCases — 15 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng |
|:---|:---|
| Tổng TC đã có | **15** |
| Số lượng TC bị lỗi Role/Luồng duyệt | **15/15** (Sai mindset Maker/Checker) |
| Lỗi Copy-Paste (Anti-pattern) | **1** (Nghiêm trọng - Bê nguyên từ SA09 sang) |
| Lỗi Tên trường sai so với mockup | **2** |
| Gap nghiệp vụ (Thiếu kịch bản biên) | **1** |

> [!IMPORTANT]
> **Đánh giá sơ bộ:** Bộ TC SA.10 có chất lượng nội dung nền rất tốt, phân rã 4 lớp Expected Result rõ ràng và cover được các logic phức tạp đặc thù của Job (tận thu, sweep tài khoản thay thế, chạy tay/đình chỉ). Tuy nhiên, mắc phải **Lỗi Copy-Paste nghiêm trọng** ở TC bắt lỗi Mandatory và việc sử dụng ám chỉ role `Maker` trong khi **đây là tính năng quản lý nội bộ 1 bước, KHÔNG PHÊ DUYỆT**.

---

## 2. PHÂN TÍCH MOCKUP UI

Tài liệu cung cấp **màn hình Danh sách** (image1.png). Các cột Grid thực tế bao gồm:
`Mã số job` | `Thứ chạy job` | `Tên job` | `Nhóm code phí` | `Mô tả job` | `Kiểu job` | `Từ thời điểm` | `Đến thời điểm` | `Tần suất` | `Ngày thu` | `Ngày thực thi tiếp theo` | `Lệnh thực thi` | `Trạng thái` | `Hành động` (Sửa/Xem/Run thủ công/Ngừng)

*(Do Form Thêm mới bị thiếu mockup chi tiết trong docx, thao tác reference tên trường bắt buộc phải bám chặt vào tên các cột đã được chốt trên Grid danh sách nhằm giữ độ nhất quán).*

---

## 3. TRACEABILITY MATRIX

| BR_ID | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| BR_01 | Nhập đủ trường (*) trước khi "Xác nhận" | SA10-BR01-HAP-001, SA10-BR01-NEG-002 | ❌ **Lỗi Copy-Paste nguyên xi từ SA.09** |
| BR_02 | Chọn "Đóng" → không lưu | SA10-BR02-UI-001 | ✅ Đủ |
| BR_03 | Unique Mã số/Thứ chạy job/Nhóm | SA10-BR03-NEG-001 | ✅ Đủ |
| BR_04 | Gửi Email nếu Job thất bại | SA10-BR04-HAP-001 | ✅ Đủ |
| BR_05 | Ràng buộc Tận thu | SA10-BR05-NEG-001, SA10-BR05-HAP-001 | ✅ Đủ |
| General | Chạy thủ công, Đình chỉ, Tải file | SA10-UI-FUNC-001, 002, EXPORT-001 | ✅ Đủ |
| General | Tự tìm TK thay thế nếu TK mặc định lỗi | SA10-LOG-HAP-001 | ⚠️ Thiếu negative boundary case |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI (FINDINGS)

| # | TC_ID / BR_ID | Loại phát hiện | Mô tả sự cố | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | Toàn bộ 15 TCs | **Logic Mismatch (Role/Mindset)** | Toàn bộ TC đều có Precondition ghi *"Đăng nhập Maker"* hoặc *"User Maker có quyền"*. Tuy nhiên, yêu cầu đã nêu rõ: đây là **tính năng thao tác trực tiếp, KHÔNG CẦN CHỜ DUYỆT**. Việc áp dụng role Maker ám chỉ mô hình 4-eyes (Maker/Checker) là sai hoàn toàn cho Context này. | 🔴 High | Sử dụng Replace All: Đổi hàng loạt chữ **"Maker"** thành **"Người dùng"** / **"Admin"** trên toàn bộ 15 TCs (tại Precondition và Expected Result). |
| 2 | SA10-BR01-NEG-002 | **Anti-Pattern (Copy-Paste Error)** | Test case bắt Mandatory rỗng này copy hệt từ tính năng *SA09 (Nhóm Code Phí)*. Step 1 ghi: *"Để trống trường: **[Mã nhóm], [Tên nhóm], [Mức độ ưu tiên]**...*" Trong khi Data Entity của Job phải là `Mã số job`, `Thứ chạy job`, `Lệnh thực thi`... Đây là lỗi râu ông nọ cắm cằm bà kia (False test scenario). | 🔴 High | Sửa Step 1 thành: *"Để trống một trong các trường bắt buộc của Job: [Mã số job], [Thứ chạy job], [Tên job], [Nhóm code phí], [Lệnh thực thi]..."*, đồng thời update lại Note các Variant. |
| 3 | SA10-BR01-HAP-001 | **Tên Trường Sai (UI Match)** | Sử dụng thuật ngữ tự chế `"Mã Job"`, `"Thứ tự chạy"`. Đối chiếu hình ảnh Mockup Danh sách (image1.png), tên hiển thị chính xác phải là **"Mã số job"** và **"Thứ chạy job"**. | 🟠 Medium | Sửa lại đúng từ khóa theo thiết kế UI đã có nhằm đảm bảo Automation Script chạy được sau này. |
| 4 | SA10-UI-01-ADD-001 | **UI Format Lỏng lẻo** | `(ii) UI` ghi qua loa bằng dấu ba chấm: *"Các trường: Mã Job, Thứ tự, Nhóm code phí... dạng Edit"*. Dùng biểu tượng "..." trong Test Case UI Validation là điều cấm kỵ vì Tester thủ công sẽ không biết check bao nhiêu trường là đủ. | 🟠 Medium | Xóa dấu ba chấm, liệt kê tường minh 100% field lấy rà soát đối xứng từ Grid List (Mã số job, Thứ chạy job, Kiểu job, Từ thời điểm, Đến thời điểm, Tần suất, Ngày thu...). |
| 5 | SA10-LOG-HAP-001 | **GAP (Thiếu Luồng Edge Case)** | TC Happy kiểm tra xuất sắc việc Hệ thống tự switch thu sang TK thay thế số 3 có Số dư lớn nhất. Tuy nhiên **Thiếu luồng Negative (Boundary Fallback)**: Nếu hệ thống quét 100% mọi TK thay thế, nhưng *tất cả* đều dưới số dư hoặc bị khóa, hệ thống xử lý ra sao? Job có ghi log Error và trigger Email không? | 🟡 Low | Thêm mới 1 TC: `SA10-LOG-NEG-001`. Tiền điều kiện: "Cả TK chính và mọi TK phụ đều chỉ có 0 VNĐ". Expected: *"Job ghi nhận log Failed, trigger bắn Email theo BR_04 do không trích thu được"*. |

---

## 5. ƯU TIÊN XỬ LÝ SỬA CHỮA (ACTION PLAN)

```text
🔴 CRITICAL ACTION (Thực hiện Replace All):
  - Xóa bỏ mọi khái niệm về "Maker", đổi toàn bộ thành "Người dùng" trong toàn bộ file SA10.xlsx.
  - Sửa ngay nội dung dở khóc dở cười của SA10-BR01-NEG-002 do copy nhầm từ SA09 sang.
  - Đảm bảo trong Expected sẽ KHÔNG xuất hiện trạng thái "Chờ duyệt" hay "Đã duyệt" nào cả.

🟠 MEDIUM/LOW ACTION (Chuẩn hóa Format):
  - Sửa những chỗ đang gọi "Mã Job" thành "Mã số job" và "Thứ tự" thành "Thứ chạy job".
  - Liệt kê đầy đủ tham số cho SA10-UI-01-ADD-001.
  - Bổ sung 1 TC SA10-LOG-NEG-001 để đảm bảo logic Tìm TK thay thế không bị lỗi crash ngầm khi toàn bộ TK khách hàng đều nghèo.
```

> **Review Complete.**
