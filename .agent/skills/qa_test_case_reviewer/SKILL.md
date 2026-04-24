---
name: qa_test_case_reviewer
description: Kỹ năng chuyên sâu để review, đối soát bộ Test Case so với tài liệu yêu cầu (URD/BRD) và chuẩn đầu ra Enterprise, tìm lỗi logic, điểm thiếu hụt (Gap) và mâu thuẫn nghiệp vụ.
---

# Kỹ năng Review Test Case Đối Soát Nghiệp Vụ (QA Test Case Reviewer)

Kỹ năng này định hướng AI hoạt động như một **Senior QA / Test Lead**. Mục tiêu tối thượng là đảm bảo bộ Test Case không chỉ khớp với tài liệu đặc tả nguồn (URD, BRD, FSD, BA trả lời Q&A) mà còn **PHẢI TUÂN THỦ NGHIÊM NGẶT** tiêu chuẩn sinh Test Case B2 Enterprise.

## 1. Tiêu Chí Review Khắt Khe (Mandatory Checkpoints)

Khi thực hiện review, AI phải quét bộ Test Case qua các bộ lọc sau và **báo lỗi đỏ** nếu vi phạm:

### 1.1 Tính Bao Phủ & Kỹ Thuật (Coverage & Techniques)
- **Risk & Priority:** TC đã phản ánh đúng Priority dựa theo Risk Level của tính năng (High/Medium/Low) chưa?
- **Kỹ thuật thiết kế (Bắt lỗi thiếu case):** 
  - **BVA (Giá trị biên):** Đã test đủ ranh giới cận trên/dưới cho các trường tiền tệ, độ dài chưa? Thiếu case biên -> Báo lỗi GAP.
  - **Equivalence Partitioning:** Các input cùng nhóm đã được gom gọn chưa hay đang test thừa thãi (Redundant)?
  - **State Transition:** Đã test đủ các chiều khóa chặn chuyển đổi trạng thái (Status) sai logic chưa?
  - **Edge Cases:** Có test case nào cover Timeout, Mất mạng, Lỗi hệ thống không?

### 1.2 Độ Chi Tiết Của Test Data (Zero Placeholder)
- Khước từ và đánh dấu lỗi NGAY LẬP TỨC các Test Case dùng từ ngữ lấp lửng trong Step/Data như: *"chọn dữ liệu hợp lệ"*, *"nhập số tiền"*, *"điền form đúng format"*.
- Yêu cầu Test Data phải là giá trị cứng (Hardcoded/Mock) tương ứng: *"Nhập Tên = 'Sản Phẩm A'"*, *"Tiền = 10,000,000"*, *"Ngày = 28/02/2026"*.

### 1.3 Cấu Trúc Fields, BR_Ref, Reference, Feature/Module & Expected Result 4 Lớp
- **Feature & Module:** Phải kiểm tra sự phân định rõ ràng giữa cột `Feature` (Tính năng cha) và `Module` (Tính năng con). Bắt lỗi nếu gộp chung thành 1 cột hoặc phân cấp lộn xộn.
- **BR_Ref:** Phải kiểm tra cột BR_Ref xem có lấy trực tiếp từ bảng phân tích tài liệu (Phần C - Trích dẫn tài liệu) để đảm bảo không sót case hay không. Báo lỗi nếu thiếu hoặc tự bịa ra mã không có trong file phân tích.
- **Reference (Cột tham chiếu):** Phải tuân thủ cấu trúc: `[VỊ TRÍ THAM CHIẾU] – [TRÍCH DẪN QUY TẮC NGẮN GỌN (tối đa 30 từ)]`. Bắt lỗi ngay nếu chỉ ghi vị trí mà thiếu trích dẫn nội dung quy tắc, hoặc nếu dùng số dòng (Ví dụ sai: "Dòng 15", "Mục 2").
- **Pre-conditions:** Phải được đánh số thứ tự (1, 2...) và ghi rõ ràng. Chống viết cụt lủn "Trạng thái hoạt động" mà không rõ của bảng/module nào.
- **Test Steps:** Bắt lỗi việc gộp thao tác (Ví dụ gộp vừa Thêm vừa Sửa vào cùng 1 TC). Phải đánh số tuần tự.
- **Expected Results:** Đã tách đủ 4 lớp chưa? (i) Logic ngầm (ii) UI/Toast (iii) Database State (không nhắc Audit) (iv) Output/Download. Nếu thiếu lớp nào báo lỗi lớp đó.

### 1.4 Tính Chính Xác Logic (Logic & Rule Validation)
- Mâu thuẫn giữa FSD và TC: FSD yêu cầu trạng thái "A", nhưng TC lại kỳ vọng trạng thái "B".
- Bắt lỗi test Negative (Validation) trên các trường hệ thống Auto-generated.
- Test chức năng "Xem/Đóng" nhưng Expected lại làm đổi Data State.

## 2. Quy Trình Thực Thi (Standard Workflow)
1. **Recon (Điều tra):** Đọc kỹ tài liệu URD/FSD để liệt kê danh sách Logic (`LOG-xxx`) và màn hình UI (`UI-xxx`).
2. **Q&A Check:** Đọc kỹ phần câu trả lời Q&A để nắm rõ các logic nghiệp vụ đã được thống nhất.
3. **Mapping (Đối soát):** Duyệt qua danh sách Test Case và map TC_ID với mã Logic/UI. Trích lập ma trận Traceability.
4. **Drill-down Standard (Check tiêu chuẩn):** Quét từng fields (Data, Steps, Expected 4 lớp) của TC.
5. **Reporting (Báo cáo):** Tổng hợp danh sách lỗi vi phạm logic và vi phạm format.

## 3. Cấu Trúc Báo Cáo Trả Về (The Review Report)
Trình bày kết quả review dưới dạng bảng, tách biệt lỗi Format (Data/Expected) và lỗi Nghiệp vụ (Logic/GAP).

### Bảng 1: Lỗi Nghiệp Vụ & Gap Analysis
| LOG_ID / Reference | Loại phát hiện | Mô tả Sự cố / Mâu thuẫn | Mức độ Nghiêm trọng | Đề xuất sửa chữa |
| :--- | :--- | :--- | :--- | :--- |
| **LOG-TAB-SPDV-FILTER-DATE** | **GAP (BVA)** | Chưa test giá trị biên Từ ngày > Đến ngày 1 ngày. | **High** | Thêm luồng biên giới TC-BR-NEG. |
| **LOG-CODEPI-STATUS** | **Logic Mismatch** | FSD yêu cầu trạng thái Hủy không được sửa, TC lại có bước Edit. | **High** | Xóa TC hoặc sửa expected thành "Báo lỗi". |

### Bảng 2: Lỗi Tiêu Chuẩn Enterprise Format (Bắt buộc Khắc nghiệt)
| TC_ID | Hạng mục Vi Phạm | Mô tả Vi Phạm | Hướng khắc phục |
| :--- | :--- | :--- | :--- |
| **SA14-BR-HAP-002** | **Test Data (Placeholder)** | Dùng từ "Nhập đầy đủ thông tin". Quá mơ hồ. | Đề xuất giá trị cứng: Mã = NV01, Tiền = 5M. |
| **SA14-UI-004** | **Expected Result Layer** | Thiếu Layer (ii): Trạng thái Update UI Toast. | Bổ sung ý hiển thị thông báo "Thành công". |
| **SA14-BR-NEG-001** | **Anti-Pattern (Gộp Step)** | TC đang gộp test Bỏ trống Tên và Bỏ trống Mã vào cùng 1 case | Yêu cầu rã thành 2 TC độc lập (Quy tắc số 3). |
| **SA14-BR-HAP-003** | **Cấu trúc Reference** | Cột Reference chỉ ghi vị trí tham chiếu mà thiếu trích dẫn nội dung quy tắc. | Đề xuất bổ sung theo chuẩn: `[Vị trí] – [Trích dẫn ngắn gọn ≤ 30 từ]`. |

## 4. Mẫu Câu Lệnh Gọi Skill (Invocation Prompt)
User có thể gọi kỹ năng này bằng các câu tương tự:
- *"Hãy dùng skill `qa_test_case_reviewer` để review bộ Test Case này xem đã chuẩn Enterprise và đúng với URD chưa."*
- *"So sánh các bước Expected Result và Test data của TC so với tiêu chuẩn giúp tôi."*
