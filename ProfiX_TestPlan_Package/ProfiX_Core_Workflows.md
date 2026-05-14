# ProfiX Phase 1 - Core Business Workflows

> [!NOTE]
> Tài liệu này xâu chuỗi các User Stories rời rạc thành 3 luồng nghiệp vụ (Business Flows) cốt lõi của hệ thống ProfiX Phase 1. Việc nhìn hệ thống theo "dòng chảy" sẽ giúp bạn dễ dàng viết Test Case Integration hoặc End-to-End.

## 1. Flow 1: Khởi tạo và Cấu hình Biểu phí (Fee Setup Workflow)
Đây là luồng hoạt động đầu tiên phải làm khi vận hành hệ thống.

```mermaid
sequenceDiagram
    participant M as Nhân viên Khai báo (Maker)
    participant C as Người Phê duyệt (Checker)
    participant P as Hệ thống ProfiX

    M->>P: 1. Khai báo Danh mục SPDV (US01)
    M->>P: 2. Sinh/Tạo Mã Code phí (US04/US02/US03)
    M->>P: 3. Cấu hình Quy tắc tính phí cho Code (US05)
    M->>P: 4. Gom Code phí tạo thành Biểu phí (US06/US07)
    P-->>M: Cập nhật Trạng thái "Chờ Duyệt"
    
    C->>P: 5. Tra cứu Biểu phí & Code phí
    C->>P: 6. Duyệt / Từ chối (US25)
    P-->>P: Nếu Duyệt -> Trạng thái "Active"
    
    Note over P: Lúc này, Biểu phí đã sẵn sàng để áp dụng cho Khách hàng
```

## 2. Flow 2: Khởi tạo Chương trình Ưu đãi (Promotion Setup Workflow)
CTƯĐ có thể được tạo bằng tay bởi Maker, hoặc tự động kích hoạt (trigger) từ một hệ thống bên ngoài.

```mermaid
flowchart TD
    A[Bắt đầu] --> B{Nguồn khởi tạo}
    
    B -->|Tự động| C[Hệ thống Miễn giảm phí khác]
    C -->|API Trigger (US37)| D[ProfiX: Tự động khởi tạo CTƯĐ]
    
    B -->|Thủ công| E[Nhân viên Khai báo]
    E --> F[Khai báo CTƯĐ định kỳ - US11]
    E --> G[Khai báo CTƯĐ theo DS KH - US12]
    E --> H[Khai báo CTƯĐ mở - US13]
    
    F --> I((Chờ Phê Duyệt - US25))
    G --> I
    H --> I
    D --> I
    
    I -->|Checker Duyệt| J[Trạng thái Active]
    J --> K[Sẵn sàng áp dụng ưu đãi]
```

## 3. Flow 3: Luồng Xử lý Giao dịch & Auto Billing (Core Engine Workflow)
Đây là "trái tim" của ProfiX. Khi có một giao dịch phát sinh từ Kênh Online hoặc Quầy, ProfiX sẽ tự động hứng, tính toán phí, trừ ưu đãi, và thu tiền.

```mermaid
sequenceDiagram
    participant Core as Core Banking / Kênh GD
    participant P as ProfiX Auto Engine
    participant DB as ProfiX Database

    Core->>P: 1. Đổ dữ liệu Giao dịch mới (Online/Quầy)
    
    activate P
    P->>DB: 2. Tra cứu CIF khách hàng & Mã SPDV
    DB-->>P: Trả về Biểu phí & CTƯĐ (nếu có)
    
    Note over P: Tính toán Phí = (Phí gốc) - (Mức ưu đãi)
    
    P->>P: 3. Tự động tính phí (US33/US34)
    P->>Core: 4. Gửi lệnh Thu tiền
    
    alt Thu tiền Thành công
        Core-->>P: ACK (Thành công)
        P->>DB: Ghi nhận Lịch sử thu phí (US18/US28)
    else Thu tiền Thất bại (Không đủ số dư)
        Core-->>P: NACK (Thất bại)
        P->>DB: Ghi nhận vào Báo cáo Nợ phí (US29)
    end
    deactivate P

    %% Tiến trình ngầm định kỳ
    loop Chạy Batch / Cronjob định kỳ
        P->>DB: Quét danh sách KH đang Nợ phí
        P->>P: Tự động Truy thu/Tận thu (US36)
        P->>P: Tự động Thu các phí định kỳ (US35/US38)
    end
```

### Các rủi ro (Loopholes) cần lưu ý khi review luồng này:
1. **Flow 3 (Auto Billing):** Cần làm rõ xử lý ngoại lệ khi Core Banking bị timeout không trả về ACK/NACK. Cơ chế retry (thử lại) thu tiền của ProfiX hoạt động như thế nào?
2. **Flow 3 (Truy thu - US36):** Việc quét nợ chạy tần suất bao lâu 1 lần (realtime, theo ngày, hay cuối tháng)? Điều này cực kỳ quan trọng để test hiệu năng.
3. **Mâu thuẫn giá trị:** Nếu Khách hàng thỏa mãn đồng thời 2 CTƯĐ (Ví dụ: Ưu đãi 1 từ US11, Ưu đãi 2 từ US12), hệ thống sẽ chọn ưu đãi nào để trừ? Cần hỏi BA.
