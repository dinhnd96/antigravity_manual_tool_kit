---
name: test_case_management_sync
description: Kỹ năng đồng bộ hóa, quản trị tập trung và dọn dẹp (Clean-up) bộ Test Case chuyên nghiệp cho dự án ProfiX.
---

# Test Case Management Sync Skill

## Giới thiệu
Kỹ năng này hoạt động như một **Test Data / Process Engineer**, chuyên xử lý, chuẩn hóa và quản trị bộ Test Case từ nhiều nguồn độc lập vào một Master File (`ProfiX_Master_Test_Cases.xlsx`) và ngược lại. Khả năng lõi bao gồm:
- **Đồng bộ hai chiều (Two-way Sync):** Gộp các file nhỏ thành Master hoặc bơm ngược (Backpropagate) dữ liệu đã chỉnh sửa từ Master về lại các file module độc lập.
- **Dashboard thống kê tổng hợp:** Tự động sinh bảng Dashboard đếm số lượng TC theo từng US, tỷ lệ Pass/Fail/Blocked.
- **Daily Tracking theo từng người:** Theo dõi số TC test xong mỗi ngày theo từng tester (Định, Vân, Vân Anh, Thương).
- **Dọn rác & Sửa lỗi Logic (Anti-pattern Clean-up):** Tự động phát hiện và cắt bỏ các cụm Steps/Expected Results bị copy-paste sai ngữ cảnh.
- **Định dạng & Bảo toàn Công thức (Formatting & Formula Preservation):** Dùng `openpyxl` để bảo toàn nguyên vẹn cấu trúc file, Dashboard công thức (`COUNTIF`, `COUNTA`, `COUNTIFS`), thêm viền (Borders), căn dòng (Wrap Text) cho các ô chữ dài.

## Cấu trúc Master File

Master File gồm 3 loại sheet:

### 1. Sheet `📊 Dashboard` — Tổng hợp số lượng TC
| Cột | Header | Mô tả |
|-----|--------|-------|
| A | STT | Số thứ tự |
| B | Module | Tên sheet US (US01, US02, ...) |
| C | Total TC | `=COUNTA('USxx'!A:A)-1` |
| D | Passed | `=COUNTIF('USxx'!<status_col>,"Pass")` |
| E | Failed | `=COUNTIF('USxx'!<status_col>,"Fail")` |
| F | Blocked | `=COUNTIF('USxx'!<status_col>,"Blocked")` |
| G | N/A | `=COUNTIF('USxx'!<status_col>,"N/A")` |
| H | Execution % | `=IF(C>0,(D+E+F)/C,0)` |
| I | Pass Rate % | `=IF(C>0,D/C,0)` |

**Lưu ý:** `<status_col>` phụ thuộc vào format của sheet US:
- **Format Round (US01):** `Status R1` = cột M (col 13)
- **Format Single (US02):** `Kết quả` = cột O (col 15)

Dòng cuối cùng sau tất cả US là dòng **TOTAL** dùng `=SUM()`.

### 2. Sheet `📅 Daily Tracking` — Theo dõi tiến độ hàng ngày
| Cột | Header | Mô tả |
|-----|--------|-------|
| A | Date | Ngày test (datetime) |
| B | Định | Số TC do Định test xong ngày đó |
| C | Vân | Số TC do Vân test xong ngày đó |
| D | Vân Anh | Số TC do Vân Anh test xong ngày đó |
| E | Thương | Số TC do Thương test xong ngày đó |
| F | Total/Day | `=SUM(B:E)` tổng TC cả team trong ngày |
| G | Tổng lũy kế | `=SUM(F$3:F<row>)` tổng tích lũy |

**Công thức đếm:** Dùng `COUNTIFS` tham chiếu tới cột `Tester` và `Date` trên tất cả US sheets.
- Format A (Round): Tester col = `N`, Date col = `O`
- Format B (Single): Tester col = `M`, Date col = `N`

### 3. Các sheet US (US01, US02, ...) — Test Case chi tiết
Mỗi US 1 sheet riêng, **header ở dòng 1**, data từ dòng 2. Có 2 format:

> **Lưu ý:** Cả 2 format đều có 12 cột chung (A-L), khác nhau ở cột tracking phía sau.

#### Format A — Round-based (ví dụ US01): 15 cột
| Col | Header | Mô tả |
|-----|--------|-------|
| A | TC_ID | Mã test case (SA01-TC-001, ...) |
| B | SC_Ref | Mã scenario (SC-01, ...) |
| C | Reference | Tham chiếu tài liệu gốc |
| D | Feature | Tính năng (Khai báo SPDV, ...) |
| E | Module | Module con (Thêm mới NV, ...) |
| F | Title | Tiêu đề TC |
| G | Type | Happy Path / Negative Path / BVA / NFR / ... |
| H | Priority | High / Medium / Low |
| I | Precondition | Điều kiện tiên quyết |
| J | Steps | Các bước thực hiện |
| K | Expected | Kết quả mong đợi |
| L | Note | Ghi chú |
| M | Status R1 | Trạng thái test |
| N | Tester R1 | Người test |
| O | Date R1 | Ngày test |

#### Format B — Single-test (ví dụ US02): 19 cột
| Col | Header | Mô tả |
|-----|--------|-------|
| A-L | (Giống Format A) | TC_ID → Note |
| M | Tester | Người test |
| N | Ngày test | Ngày thực hiện |
| O | Kết quả | Pass / Fail / Blocked / N/A |
| P | Bug ID | Mã bug nếu Fail |
| Q | Retest | Retest sau fix bug |
| R | Retest Result | Kết quả retest |
| S | Ghi chú TL | Ghi chú Team Lead |

## Cách sử dụng
Gọi skill khi bạn cần:
1. **Gộp file TC** từ nhiều file rời vào Master (mỗi file → 1 sheet US).
2. **Thêm sheet US mới** vào Master có sẵn (append thêm US sheet + cập nhật Dashboard).
3. **Sinh/Cập nhật Dashboard** đếm TC và công thức COUNTIF chính xác.
4. **Sinh/Cập nhật Daily Tracking** với COUNTIFS theo tester và ngày.
5. **Dọn rác** Test Case bị dính lỗi Copy-Paste dập khuôn.
6. **Format lại** Master File (border, wrap text, column width).

## Quy trình hành động (Workflow)

### Bước 1: Quét (Scan)
- Đọc file Master hiện tại hoặc các file TC rời.
- Xác định danh sách US sheets và format (Round-based hay Single-test) dựa vào header row 1.

### Bước 2: Làm sạch (Cleanse)
- Quét cột Steps (J) và Expected (K).
- Apply bộ lọc Anti-pattern: cấm 'Lưu thành công' hay 'Nhấn xác nhận' đối với giao diện View-Only/Close.

### Bước 3: Đồng bộ (Sync)
- Map dữ liệu theo `TC_ID` và ghi đè nội dung sạch.
- Nếu gộp file mới → tạo sheet US mới, copy data giữ nguyên format 19 cột.

### Bước 4: Dashboard & Daily Tracking
- **Dashboard:** Sinh công thức COUNTIF/COUNTA tự động. Xác định cột status chính xác theo format của mỗi US.
  - Format A (Round): Status col = `M` (Status R1)
  - Format B (Single): Status col = `O` (Kết quả)
- **Daily Tracking:** Sinh công thức COUNTIFS tham chiếu tới cột Tester + Date trên tất cả US sheets.
  - Format A: Tester col = `N` (Tester R1), Date col = `O` (Date R1)
  - Format B: Tester col = `M` (Tester), Date col = `N` (Ngày test)

### Bước 5: Trang điểm (Format)
- Chỉnh lại độ rộng cột: `Steps (50)`, `Expected (50)`, `Title (40)`, `Precondition (40)`, các cột khác `18`.
- Bật `Wrap Text=True` cho tất cả cells.
- Alignment: `vertical=top`.
- Zebra striping (xen kẽ màu nền cho dễ đọc).
- Border mỏng cho tất cả cells.

### Bước 6: Báo cáo (Report)
- Đảm bảo Sheet `📊 Dashboard` có công thức thống kê chuẩn xác.
- Đảm bảo Sheet `📅 Daily Tracking` có header tester đúng tên.
- Print tóm tắt: số US, tổng TC, file output path.

## Danh sách Tester mặc định (ProfiX)
| Tên | Ghi chú |
|-----|---------|
| Định | |
| Vân | |
| Vân Anh | |
| Thương | |

## Dropdown Validation
- **Status:** `Pass, Fail, Blocked, Doing, N/A`
- **Tester:** `Định, Vân, Vân Anh, Thương`

## Yêu cầu môi trường
- **Ngôn ngữ:** Python 3.8+
- **Thư viện Engine bắt buộc:** Bắt buộc dùng `openpyxl` để tránh mất Format. Không bao giờ dùng thư viện chỉ đọc Data như `pandas` thuần khi thao tác lưu đè.
- **Đọc data input:** Có thể dùng `pandas` hoặc `openpyxl` để đọc file source.

## Gợi ý Prompts lệnh gọi cho User
- *"Hãy dùng skill test_case_management_sync để gộp các file US01, US02 vào Master File và sinh Dashboard + Daily Tracking."*
- *"Cập nhật Dashboard trong file Master, đếm lại TC và tính Pass Rate cho từng US."*
- *"Thêm sheet US03 từ file `US03_TestCases.xlsx` vào Master hiện tại và cập nhật Dashboard."*
- *"Sinh lại Daily Tracking cho team Định, Vân, Vân Anh, Thương từ ngày 01/04/2026."*
- *"Format lại file Master, kẻ bảng cho dễ nhìn và fix công thức Dashboard."*
