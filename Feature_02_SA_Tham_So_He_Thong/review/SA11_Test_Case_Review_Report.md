# 📋 BÁO CÁO REVIEW TEST CASE — SA.11 Tra cứu lịch sử hoạt động job sinh dữ liệu

> **Reviewer:** Senior QA Lead (AI-Assisted)
> **Tài liệu nguồn:** I.1.1.1. SA.11- Tra cứu lịch sử hoạt động job sinh dữ liệu.docx
> **Bộ Test Case:** SA11_Tra_Cuu_Lich_Su_Final.xlsx (Sheet: TestCases — 7 TC)
> **Ngày review:** 2026-04-07

---

## 1. TÓM TẮT TỔNG QUAN

| Hạng mục | Số lượng |
|:---|:---|
| Tổng TC đã có | **7** (Module nhỏ gọn) |
| Số lượng TC bị lỗi Role/Luồng duyệt | **7/7** (Sai mindset Maker/Checker) |
| Lỗi Tên cột Grid sai lệch so với mockup | **2/7 TC bị dính lỗi hiển thị Label** |
| Gap nghiệp vụ | **0** (Cover rất đủ các luồng tìm kiếm và xem lịch sử) |

---

## 2. PHÂN TÍCH MOCKUP UI

Dựa vào hình ảnh màn hình thiết kế **Lịch sử hoạt động job sinh dữ liệu hàng ngày** (image1.png) đính kèm trong URD, lưới danh sách thực tế có các cột siêu chi tiết bao gồm 15 trường:
`Ngày chạy job`, `Mã job`, `Số thứ tự job`, `Tên job`, `Nhóm Code phí`, `Mô tả`, `Kiểu job`, `Từ thời điểm`, `Đến thời điểm`, `Lệnh thực thi`, `Ngày thực thi`, `Trạng thái vận hành`, `Lần thực thi`, `Thời gian thực hiện`, `Người thực hiện`.

---

## 3. TRACEABILITY MATRIX

| Nhóm Chức năng | Mô tả BR | TC tương ứng | Đánh giá |
|:---|:---|:---|:---|
| UI/Chức năng | Tìm kiếm (Filter) | SA11-UI-01, SA11-UI-02, SA11-UI-03 | ✅ Đủ các luồng Normal text, Date range và Not Found |
| UI/Chức năng | Xem chi tiết log | SA11-UI-04-VIEW-HAP | ✅ Đủ |
| UI/Chức năng | Tải xuống Excel | SA11-UI-05-EXPORT-HAP | ✅ Đủ |
| UI/Chức năng | Phân trang grid | SA11-UI-06-PAGING | ✅ Đủ |
| Luồng Nghiệp vụ | Đối soát Cross-module (Real-time push) | SA11-LOG-01-INTEGRATION | ✅ Rất xuất sắc (Bảo chứng được data nhất quán với SA.10) |

---

## 4. CHI TIẾT PHÁT HIỆN LỖI (FINDINGS & RECOMMENDATIONS)

| # | TC_ID | Loại phát hiện | Mô tả sự cố (Bug Insight) | Mức độ | Đề xuất QA |
|:---|:---|:---|:---|:---|:---|
| 1 | Toàn bộ 7 TCs | **Logic Mismatch (Role/Mindset)** | Tất cả Precondition của 7 dòng đều bắt đầu bằng *"Đăng nhập Maker"*. Do tính năng Tra cứu Log là dạng Report View, **hoàn toàn không có thao tác Phê duyệt nghiệp vụ**, việc gán nhãn Role "Maker" dễ gây hiểu lầm rằng chức năng này đi cùng 1 tab "Duyệt" nào đó. | 🔴 High | Sử dụng Find & Replace All: Đổi hàng loạt cụm "Đăng nhập Maker" thành **"Người dùng"** (hoặc "Admin") trên toàn bộ file. |
| 2 | SA11-UI-01-SEARCH-HAP | **Tên Cột Sai (Mockup Mismatch)** | Trong kết quả `(ii) UI` đang liệt kê tự do: *"dữ liệu hiển thị đúng các cột: **Thời gian chạy, Tên job, Kết quả**"*. Đối chiếu với file Mockup, hoàn toàn không có cột nào tên là "Thời gian chạy" hay "Kết quả". Label thực tế trên hệ thống là **"Ngày chạy job"** và **"Trạng thái vận hành"**. | 🔴 High | Sửa lại chính xác tên Text Label theo thiết kế (`Ngày chạy job`, `Trạng thái vận hành`). Nên bổ sung đủ chuỗi cột quan trọng thay vì chỉ ghi 3 cột tượng trưng, vì nếu làm Automation sẽ thiếu Validation Point. |
| 3 | SA11-UI-05-EXPORT-HAP | **Tên Cột File Excel Lệch Dữ Liệu** | Trong `(iv) File/Email` cũng vướng lỗi tương tự: *"hiển thị đúng các cột Tên job, Thời gian chạy, Trạng thái"*. Gây cản trở nếu cần soi file Excel sinh ra so với Data chuẩn của Dev. | 🟠 Medium | Khớp chặt chẽ với Data Model ở Lỗi 2: File Excel export ra phải chứa cột `"Ngày chạy job"`, `"Trạng thái vận hành"`... theo đúng Mockup Grid. |

---

## 5. KẾT LUẬN

Bộ Test Case **SA.11 cực kỳ tinh gọn, logic rất thông minh**, nhất là việc tác giả bộ TC sinh ra được chiếc case mã số `SA11-LOG-01-INTEGRATION` liên thông chặt chẽ trực tiếp với tính năng kích hoạt Job phí (từ SA.10). Điều này cho thấy người thiết kế có tư duy E2E (System Integration) tốt. 

Điểm trừ di truyền duy nhất vẫn là **"lười" thay thế Keyword Maker** và **chuẩn hóa Label các cột (Grid Headers) theo dân dã chứ chưa Hard-code dính liền với Mockup spec**. Chỉ cần thay đổi 2 text gợn nhỏ này, bản Excel sẽ sẵn sàng Release!
