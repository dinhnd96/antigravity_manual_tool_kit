# ProfiX Phase 1 - System Architecture & Feature Map

> [!NOTE]
> Tài liệu này tổng hợp cấu trúc chức năng cấp cao (High-level) của toàn bộ hệ thống ProfiX Phase 1, dựa trên 40 User Stories. Giúp bạn nắm được "Bức tranh toàn cảnh" trước khi đi vào chi tiết nghiệp vụ.

## 1. Bản đồ Phân rã Chức năng (Feature Tree)

Hệ thống được chia thành 4 phân hệ (Module) cốt lõi:

```mermaid
mindmap
  root((ProfiX System))
    Quản trị Tham số
      Quản lý SPDV
        US01 Khai báo cây phân cấp SPDV
        US10 Chuyển đổi code phí giữa các SPDV
      Quản lý Code phí
        US02 Khai báo mới code phí
        US03 Nhân bản code phí
        US04 Tự động sinh mã code phí
        US05 Định nghĩa quy tắc tính phí
        US09 Chuyển đổi code phí giữa biểu phí
      Quản lý Biểu phí
        US06 Khai báo biểu phí theo Quyết định
        US07 Khai báo bằng file Excel
        US08 Sao chép biểu phí
      Chương trình ưu đãi
        US11 Khai báo CTƯĐ định kỳ
        US12 CTƯĐ theo danh sách KH
        US13 CTƯĐ không xác định sẵn KH
    Tra cứu và Báo cáo
      Tra cứu danh mục
        US14 Xem danh mục SPDV
        US15 Lịch sử Biểu phí
        US16 Lịch sử CTƯĐ
      Tra cứu Khách hàng
        US17 Code phí áp dụng cho KH
        US18 Lịch sử thu phí KH
        US19 Lịch thu phí dự kiến
        US20 CTƯĐ áp dụng cho KH
        US28 Sao kê chi tiết giao dịch
      Báo cáo quản trị
        US29 Khách hàng nợ phí
        US30 Dự thu phí kỳ tiếp theo
        US31 Báo cáo tổng doanh thu
        US32 Dashboard tổng quan hoạt động
    Quản trị Hệ thống
      Cơ bản
        US21 Đăng nhập
        US22 Đăng xuất
      Phân quyền
        US23 Quản lý Người dùng
        US24 Quản lý Nhóm quyền
        US25 Cấu hình ma trận phê duyệt
      Cấu hình Quy tắc
        US26 Quy tắc điều kiện tính phí
        US27 Quy tắc xác định nhóm KH
    Engine Xử lý Tự động
      Tính phí giao dịch
        US33 Tính phí Kênh Online
        US34 Tính phí Kênh Quầy
        US39 Phí trả nợ trước hạn
      Thu phí định kỳ
        US35 Thu các loại phí định kỳ
        US36 Truy thu nợ phí
        US38 Thu phí bảo lãnh định kỳ
      Tiện ích tự động
        US37 Khởi tạo CTƯĐ từ HT duyệt
        US40 Xử lý phát sinh khác
```

## 2. Bản đồ Người dùng & Phân quyền (Role Mapping)

Dựa trên các User Stories, hệ thống có 3 nhóm đối tượng (Actors) chính:

| Actor | Vai trò | Các Module tiếp cận |
| --- | --- | --- |
| **Quản trị viên (System Admin)** | Quản lý hệ thống, phân quyền và thiết lập các quy tắc nền tảng. | - Quản trị Hệ thống (US21-US27) |
| **Người dùng Khai báo (Maker/Checker)** | Nhân viên nghiệp vụ thực hiện thiết lập cấu hình phí, biểu phí, khuyến mãi. Cần tuân thủ ma trận phê duyệt (US25). | - Quản trị Tham số (US01-US13)<br>- Tra cứu & Báo cáo |
| **Hệ thống lõi (Core Engine / Batch)** | Xử lý các tác vụ ngầm định, tính toán và thu phí dựa trên quy tắc đã cấu hình. | - Engine xử lý tự động (US33-US40) |

> [!TIP]
> Các User Story từ US33 đến US40 thuộc dạng **System Cases** (hệ thống tự chạy ngầm). Khi tiếp cận nhóm này để viết Test Case hoặc tích hợp, bạn cần tập trung vào việc kích hoạt (trigger) các tiến trình Batch/Cronjob hoặc API giả lập các giao dịch từ hệ thống ngoài (Core Banking) đổ về.

---

## 3. Vòng đời Trạng thái (State Lifecycle) — BỔ SUNG

Hầu hết các đối tượng cốt lõi trong ProfiX đều tuân thủ chu trình trạng thái (State) Maker-Checker. Hiểu vòng đời này giúp bạn biết **tại bước nào thì dữ liệu có hiệu lực**, từ đó viết Test Case chính xác hơn.

### 3.1 Vòng đời Code phí / Biểu phí / CTƯĐ

```mermaid
stateDiagram-v2
    [*] --> Draft : Maker tạo mới
    Draft --> PendingApproval : Maker gửi duyệt
    PendingApproval --> Active : Checker duyệt
    PendingApproval --> Rejected : Checker từ chối
    Rejected --> Draft : Maker sửa & gửi lại
    Active --> PendingUpdate : Maker yêu cầu sửa
    PendingUpdate --> Active : Checker duyệt sửa
    PendingUpdate --> Active : Checker từ chối sửa (giữ nguyên)
    Active --> Inactive : Hết hiệu lực / Hủy
    Inactive --> [*]
    
    note right of Active : CHỈ bản ghi Active mới được\nEngine sử dụng để tính phí
    note left of PendingApproval : Maker KHÔNG thể sửa\nkhi đang chờ duyệt
```

> [!IMPORTANT]
> **Quy tắc vàng:** Engine tự động (US33-US40) **CHỈ ĐƯỢC** đọc các bản ghi có trạng thái `Active`. Nếu Code phí đang `Draft`, `PendingApproval`, hoặc `Inactive` thì Engine phải bỏ qua, không được dùng để tính phí cho khách hàng.

### 3.2 Vòng đời Giao dịch Thu phí

```mermaid
stateDiagram-v2
    [*] --> Pending : GD phát sinh từ Core Banking
    Pending --> Calculated : ProfiX tính toán xong phí
    Calculated --> Collected : Thu tiền thành công
    Calculated --> Failed : Thu tiền thất bại (không đủ số dư)
    Failed --> Debt : Chuyển vào Nợ phí
    Debt --> Collected : Truy thu thành công (US36)
    Debt --> WrittenOff : Tận thu / Xóa nợ (US36)
    Collected --> [*]
    WrittenOff --> [*]
```

---

## 4. Bản đồ Tích hợp Hệ thống Ngoài (Integration Map) — BỔ SUNG

ProfiX không hoạt động độc lập. Nó giao tiếp với nhiều hệ thống bên ngoài. Hiểu rõ các "cửa giao tiếp" này cực kỳ quan trọng để test tích hợp (Integration Testing).

```mermaid
flowchart LR
    subgraph External["Hệ thống bên ngoài"]
        CB["Core Banking\n(Tài khoản, Số dư, GD)"]
        CIF_SYS["Hệ thống CIF\n(Thông tin Khách hàng)"]
        APPROVAL["HT Phê duyệt\nMiễn/Giảm phí"]
        CHANNEL["Kênh GD Online\n(iBanking, mBanking)"]
    end

    subgraph ProfiX["ProfiX Phase 1"]
        PARAM["Module\nQuản trị Tham số"]
        ENGINE["Module\nEngine Tự động"]
        REPORT["Module\nTra cứu & Báo cáo"]
    end

    CIF_SYS -->|"API: Tra cứu CIF\n(US17, US26, US27)"| PARAM
    CIF_SYS -->|"API: Xác định Nhóm KH\n(US27)"| ENGINE
    CB -->|"API: Kiểm tra số dư\n& Thu tiền"| ENGINE
    CHANNEL -->|"API: Gửi GD Online\n(US33)"| ENGINE
    CB -->|"API: Gửi GD Quầy\n(US34)"| ENGINE
    APPROVAL -->|"API Trigger\n(US37)"| PARAM
    ENGINE -->|"Ghi log GD"| REPORT
    PARAM -->|"Cung cấp Biểu phí\n& CTƯĐ Active"| ENGINE
```

| Hệ thống ngoài | Giao tiếp với Module | Mục đích | User Stories |
| --- | --- | --- | --- |
| Core Banking | Engine Tự động | Nhận GD quầy, kiểm tra số dư, thu tiền | US34, US35, US36, US38 |
| Kênh Online | Engine Tự động | Nhận GD online realtime | US33 |
| Hệ thống CIF | Quản trị Tham số + Engine | Tra cứu thông tin KH, xác định nhóm KH | US17, US26, US27 |
| HT Phê duyệt Miễn/Giảm phí | Quản trị Tham số | Tự động khởi tạo CTƯĐ từ kết quả duyệt | US37 |

---

## 5. Quick Reference: Đọc tài liệu FSD theo Module — BỔ SUNG

Bảng tra cứu nhanh khi bạn cần đọc lại chi tiết FSD gốc cho một chức năng cụ thể:

| Khi bạn muốn tìm hiểu về... | Đọc các US | Nhóm Module |
| --- | --- | --- |
| Cây sản phẩm dịch vụ (SPDV) là gì? | US01, US14 | Quản trị Tham số |
| Code phí được tạo và cấu hình ra sao? | US02, US03, US04, US05 | Quản trị Tham số |
| Biểu phí là gì, tạo/sao chép thế nào? | US06, US07, US08, US09, US10, US15 | Quản trị Tham số |
| Chương trình ưu đãi hoạt động ra sao? | US11, US12, US13, US16, US20, US37 | Quản trị Tham số + Engine |
| Phân quyền & phê duyệt | US21-US25 | Quản trị Hệ thống |
| Quy tắc nền (điều kiện phí, nhóm KH) | US26, US27 | Quản trị Hệ thống |
| Tra cứu thông tin khách hàng | US17, US18, US19, US20, US28 | Tra cứu |
| Báo cáo quản trị | US29, US30, US31, US32 | Báo cáo |
| Tính phí tự động (realtime) | US33, US34, US39 | Engine |
| Thu phí định kỳ & truy thu nợ (batch) | US35, US36, US38, US40 | Engine |
| Quy tắc chung UI (Search, Filter, Paging) | Phụ lục FSD | Áp dụng toàn hệ thống |
