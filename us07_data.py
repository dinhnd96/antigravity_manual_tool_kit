# -*- coding: utf-8 -*-

GLOSSARY_DATA = [
    {
        "term": "SLCĐ",
        "original": "Sinh lời chủ động",
        "definition": "Hợp đồng gửi tiền sinh lời của Khách hàng cá nhân phát sinh từ 12h ngày T-1 đến 11h59'59'' ngày T."
    },
    {
        "term": "TKTT A1",
        "original": "Tài khoản thanh toán A1",
        "definition": "Tài khoản thanh toán gốc của Khách hàng dùng để trích nợ đầu tư, chốt số dư lúc 12h hàng ngày."
    },
    {
        "term": "TKTT A2",
        "original": "Tài khoản thanh toán A2",
        "definition": "Tài khoản thanh toán trung gian để chuyển tiền đi đầu tư mua Trái phiếu."
    },
    {
        "term": "TKTC C1",
        "original": "Tài khoản thấu chi C1",
        "definition": "Tài khoản thấu chi hỗ trợ nguồn vốn khi số dư TKTT A1 không đủ để chi trả gốc/lãi."
    },
    {
        "term": "Maker",
        "original": "Người nhập (Khối Nguồn vốn)",
        "definition": "User thực hiện tải danh sách hợp đồng, cập nhật thông tin Trái phiếu và gửi yêu cầu phê duyệt."
    },
    {
        "term": "Checker",
        "original": "Người duyệt (Khối Nguồn vốn)",
        "definition": "User kiểm tra thông tin dòng tiền, danh sách khách hàng và thực hiện phê duyệt/từ chối yêu cầu."
    },
    {
        "term": "T24",
        "original": "Core Banking Temenos T24",
        "definition": "Hệ thống ngân hàng lõi thực hiện hạch toán chuyển tiền và quản lý số dư tài khoản."
    },
    {
        "term": "Investment Service",
        "original": "Dịch vụ quản lý đầu tư",
        "definition": "Hệ thống Backend (BE) xử lý logic nghiệp vụ, tính toán chỉ số dòng tiền và quản lý trạng thái yêu cầu."
    },
    {
        "term": "Web CMS",
        "original": "Hệ thống quản trị Web",
        "definition": "Giao diện Frontend (FE) dành cho Maker và Checker thực hiện thao tác nghiệp vụ."
    },
    {
        "term": "Cut-off Time",
        "original": "Giờ chốt giao dịch",
        "definition": "Thời điểm chốt số liệu giao dịch hàng ngày (12h00 trưa đối với luồng sinh lời của Profix)."
    },
    {
        "term": "Gross Payment",
        "original": "Số tiền trả khách hàng (Gross)",
        "definition": "Tổng tiền gốc đầu tư ban đầu cộng với Lãi gross thực trả cho Khách hàng (trước thuế)."
    }
]

ROLE_DATA = [
    {
        "role": "Maker (Khối Nguồn vốn)",
        "permission": "Truy cập menu Bán trái phiếu, xem danh sách hợp đồng bán, xem thông tin số dư A1, A2, C1 chốt 12h, lọc danh sách theo trạng thái trái phiếu (Tất cả / Đang hoạt động / Không hoạt động), click xem chi tiết từng hợp đồng SLCĐ."
    },
    {
        "role": "Checker (Khối Nguồn vốn)",
        "permission": "Tương tự Maker, truy cập tab Bán trái phiếu để theo dõi dòng tiền đầu tư bán ra và danh sách khách hàng tương ứng của ngày T để chuẩn bị dòng tiền chi trả và đối soát với luồng Mua (US06)."
    },
    {
        "role": "Job 12h (Hệ thống)",
        "permission": "Tự động chạy lúc 12h00 các ngày làm việc, gọi T24 lấy số dư A1, A2, C1, và lọc ra danh sách các hợp đồng SLCĐ đến hạn hoặc đăng ký rút trước hạn hợp lệ từ 12h T-1 đến 11h59'59'' T."
    }
]

API_DATA = [
    {
        "code": "API002",
        "name": "Danh sách HĐ SLCĐ",
        "desc": "Lấy danh sách hợp đồng sinh lời cố định thỏa mãn điều kiện đến hạn hoặc rút trước hạn trong khung thời gian. Đối với màn Bán trái phiếu, API được nâng cấp bổ sung trường bondStatus để lọc.",
        "type": "Update",
        "url": "/api/v1/investment/contracts/sales",
        "spec": "Bổ sung param bondStatus (Array String, Optional) truyền vào ['ACTIVE', 'INACTIVE'] để lọc."
    },
    {
        "code": "API003",
        "name": "Lấy số dư TKTT A1, A2, C1 chốt 12h",
        "desc": "Lấy số dư đã được chốt của tài khoản A1, A2 lúc 12h00 hàng ngày và hạn mức thấu chi C1 realtime từ Core Banking T24.",
        "type": "New",
        "url": "/api/v1/investment/accounts/balances",
        "spec": "Trả về số dư A1, A2 (chốt theo mốc 12h ngày T/T-1) và hạn mức còn lại C1 thấu chi realtime."
    }
]

CRUD_DATA = [
    {
        "entity": "Danh sách HĐ SLCĐ (Bán)",
        "maker": "R",
        "checker": "R",
        "job": "-",
        "note": "Xem lưới danh sách hợp đồng bán của khách hàng cá nhân đến hạn hoặc rút trước hạn"
    },
    {
        "entity": "Bộ lọc Trạng thái Trái phiếu",
        "maker": "Execute (R)",
        "checker": "Execute (R)",
        "job": "-",
        "note": "Lọc lưới theo các trạng thái Tất cả, Đang hoạt động, Không hoạt động"
    },
    {
        "entity": "Số dư chốt 12h A1, A2",
        "maker": "R",
        "checker": "R",
        "job": "C, U",
        "note": "Hệ thống tự chốt số dư và lưu DB, người dùng chỉ xem read-only"
    },
    {
        "entity": "Hạn mức thấu chi C1",
        "maker": "R (Realtime)",
        "checker": "R (Realtime)",
        "job": "-",
        "note": "Gọi sang Core T24 lấy realtime khi người dùng truy cập màn hình"
    },
    {
        "entity": "Xem chi tiết HĐ SLCĐ",
        "maker": "Execute (R)",
        "checker": "Execute (R)",
        "job": "-",
        "note": "Click điều hướng sang màn hình xem chi tiết của riêng hợp đồng đó (US05)"
    }
]

RULES_DATA = [
    {
        "title": "Quy tắc chốt số dư tài khoản A1, A2",
        "content": "Hiển thị số dư chốt lúc 12h00 hàng ngày của tài khoản thanh toán A1 và A2:<br>• Trước 12h00 ngày T: Hiển thị số dư chốt lúc 12h00 ngày T-1.<br>• Sau 12h00 ngày T: Hiển thị số dư chốt lúc 12h00 ngày T.<br>• Hạn mức thấu chi C1: Lấy thông tin thấu chi realtime tại thời điểm người dùng truy cập màn hình."
    },
    {
        "title": "Điều kiện hiển thị hợp đồng bán trái phiếu",
        "content": "Danh sách gồm các hợp đồng thoả mãn đồng thời:<br>1. Là hợp đồng của Khách hàng cá nhân.<br>2. Trạng thái hợp đồng là <strong>CURRENT</strong> (đến hạn gốc trong ngày làm việc hiện tại) hoặc <strong>PENDING_EARLY_CLOSE</strong> (có yêu cầu rút trước hạn trước giờ cut-off).<br>3. Khung thời gian phát sinh giao dịch: Từ 12h00 ngày T-1 đến 11h59'59'' ngày T theo ngày làm việc."
    },
    {
        "title": "Công thức tính toán dòng tiền đầu tư bán",
        "content": "• <strong>Tổng tiền bán trái phiếu</strong> = Tổng giá trị của cột 'Giá trị bán trái phiếu' của toàn bộ danh sách HĐ SLCĐ bán trong ngày.<br>  - Trong đó: Giá trị bán trái phiếu = Giá trị mua trái phiếu = Số lượng trái phiếu x Giá trái phiếu + Phí giao dịch (nếu có).<br>• <strong>Số tiền trả khách hàng (Gross)</strong> = Tổng giá trị của cột 'Số tiền trả khách hàng (Gross)' của toàn bộ danh sách HĐ SLCĐ bán trong ngày.<br>  - Trả khách hàng (Gross) = Số tiền khách hàng đầu tư + Lãi gross phải trả cho khách hàng.<br>  - Nếu HĐ đến hạn: Lãi gross = (Số tiền đầu tư * Lãi suất đăng ký * Số ngày thực gửi) / 365.<br>  - Nếu HĐ rút trước hạn: Lãi gross = (Số tiền đầu tư * Lãi suất KKH * Số ngày thực gửi) / 365.<br>• <strong>Lưu ý quan trọng:</strong> Hai chỉ số tổng này là cố định cho phiên giao dịch ngày T, không thay đổi khi người dùng lọc trạng thái trái phiếu trên lưới."
    },
    {
        "title": "Quy tắc xác định Ngày đến hạn thực tế",
        "content": "• Đối với HĐ đến hạn: Ngày đến hạn thực tế = Ngày đến hạn theo HĐ gốc.<br>• Đối với HĐ rút trước hạn:<br>  - Đăng ký rút trước 12h00 ngày làm việc T: hiển thị Ngày đến hạn thực tế là ngày làm việc T.<br>  - Đăng ký rút sau 12h00 ngày làm việc T hoặc vào ngày nghỉ/Lễ: hiển thị Ngày đến hạn thực tế là ngày làm việc liền sau."
    }
]
