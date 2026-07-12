# -*- coding: utf-8 -*-
import os
import us07_data

def generate_html(output_path):
    # Dựng bảng Glossary
    glossary_rows = ""
    for item in us07_data.GLOSSARY_DATA:
        glossary_rows += f"<tr><td><strong>{item['term']}</strong></td><td>{item['original']}</td><td>{item['definition']}</td></tr>\n"

    # Dựng bảng Role Mapping
    role_rows = ""
    for item in us07_data.ROLE_DATA:
        role_rows += f"<tr><td><strong>{item['role']}</strong></td><td>{item['permission']}</td></tr>\n"

    # Dựng bảng API Index
    api_rows = ""
    for item in us07_data.API_DATA:
        badge_class = "badge-new" if item['type'] == 'New' else "badge-update"
        api_rows += f"<tr><td><code>{item['code']}</code></td><td><strong>{item['name']}</strong></td><td>{item['desc']}</td><td><span class='badge {badge_class}'>{item['type']}</span></td><td><code>{item['url']}</code></td><td>{item['spec']}</td></tr>\n"

    # Dựng bảng CRUD Matrix
    crud_rows = ""
    for item in us07_data.CRUD_DATA:
        crud_rows += f"<tr><td><strong>{item['entity']}</strong></td><td>{item['maker']}</td><td>{item['checker']}</td><td>{item['job']}</td><td>{item['note']}</td></tr>\n"

    # Dựng Common Rules Summary
    rules_content = ""
    for item in us07_data.RULES_DATA:
        rules_content += f"""
        <div style="margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid var(--border-color);">
            <h4 style="color: var(--accent-color); font-weight: 600; margin-bottom: 8px;">• {item['title']}</h4>
            <p style="font-size: 0.95rem; color: var(--text-color); margin-left: 15px;">{item['content']}</p>
        </div>
        """

    # Nội dung HTML template chính
    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>US07 - Tài khoản sinh lời: Luồng đăng ký bán Trái phiếu PVCB</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {{
                background: '#16213e',
                primaryColor: '#0f3460',
                primaryTextColor: '#fff',
                primaryBorderColor: '#e94560',
                lineColor: '#53a8b6',
                secondaryColor: '#1a1a2e',
                tertiaryColor: '#16213e'
            }}
        }});
    </script>
    <style>
        :root {{
            --bg-color: #0f0f1a;
            --card-bg: #16213e;
            --border-color: #243b55;
            --accent-color: #e94560;
            --accent-glow: rgba(233, 69, 96, 0.4);
            --text-color: #e2e8f0;
            --text-muted: #94a3b8;
            --accent2-color: #53a8b6;
            --success-color: #2e7d32;
            --warning-color: #e65100;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Outfit', sans-serif;
            line-height: 1.6;
            padding-bottom: 60px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f0f1a 100%);
            border-bottom: 2px solid var(--border-color);
            padding: 80px 0 60px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        .hero::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(233, 69, 96, 0.08) 0%, transparent 60%);
            pointer-events: none;
        }}

        .hero h1 {{
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(to right, #ffffff, #e94560);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }}

        .hero p {{
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 800px;
            margin: 0 auto 20px auto;
        }}

        .meta-tags {{
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .meta-tag {{
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--text-muted);
        }}

        .meta-tag span {{
            color: var(--accent-color);
            font-weight: 600;
        }}

        /* Navigation Bar */
        .navbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background-color: rgba(15, 15, 26, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 15px 0;
        }}

        .navbar-content {{
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
        }}

        .navbar a {{
            color: var(--text-muted);
            text-decoration: none;
            font-weight: 500;
            font-size: 1rem;
            transition: all 0.3s ease;
            position: relative;
            padding: 5px 0;
        }}

        .navbar a:hover, .navbar a.active {{
            color: #ffffff;
        }}

        .navbar a::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background-color: var(--accent-color);
            transition: width 0.3s ease;
        }}

        .navbar a:hover::after, .navbar a.active::after {{
            width: 100%;
        }}

        /* Section Styling */
        section {{
            padding: 60px 0 20px 0;
            scroll-margin-top: 70px;
        }}

        .section-title {{
            font-size: 2rem;
            margin-bottom: 30px;
            border-left: 5px solid var(--accent-color);
            padding-left: 15px;
            color: #ffffff;
            font-weight: 600;
        }}

        /* Card System */
        .card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }}

        .card:hover {{
            border-color: var(--accent-color);
        }}

        .card-title {{
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 15px;
            color: var(--accent2-color);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .card-desc {{
            color: var(--text-muted);
            margin-bottom: 25px;
            font-size: 1rem;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.95rem;
        }}

        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}

        th {{
            background-color: rgba(255, 255, 255, 0.03);
            color: #ffffff;
            font-weight: 600;
        }}

        tr:hover {{
            background-color: rgba(255, 255, 255, 0.01);
        }}

        /* Callout Boxes */
        .callout {{
            border-left: 4px solid var(--accent2-color);
            background-color: rgba(83, 168, 182, 0.05);
            padding: 15px 20px;
            border-radius: 0 8px 8px 0;
            margin: 20px 0;
            font-size: 0.95rem;
        }}

        .callout.warning {{
            border-left-color: var(--warning-color);
            background-color: rgba(230, 81, 0, 0.05);
        }}

        .callout-title {{
            font-weight: 600;
            margin-bottom: 5px;
            color: #ffffff;
        }}

        /* Diagrams render area */
        .diagram-container {{
            background-color: rgba(15, 15, 26, 0.5);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }}

        .mermaid {{
            width: 100%;
        }}

        /* Grid layout for Roles and Glossary */
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }}

        @media (min-width: 768px) {{
            .grid-2 {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        /* Workflow tabs */
        .tab-buttons {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}

        .tab-btn {{
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }}

        .tab-btn:hover, .tab-btn.active {{
            background-color: var(--accent-color);
            color: #ffffff;
            border-color: var(--accent-color);
            box-shadow: 0 0 10px var(--accent-glow);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
        }}

        .badge-new {{
            background-color: var(--accent-color);
            color: #ffffff;
        }}

        .badge-update {{
            background-color: var(--accent2-color);
            color: #0f0f1a;
        }}

        .badge-existing {{
            background-color: rgba(255, 255, 255, 0.1);
            color: var(--text-muted);
        }}

        footer {{
            text-align: center;
            padding: 40px 0;
            color: var(--text-muted);
            border-top: 1px solid var(--border-color);
            font-size: 0.9rem;
            margin-top: 60px;
        }}
    </style>
</head>
<body>

    <!-- Hero Banner -->
    <header class="hero">
        <div class="container">
            <h1>US07 - Tài khoản sinh lời: Đăng ký bán Trái phiếu PVCB</h1>
            <p>Tài liệu Mapping hệ thống trực quan, tóm lược kiến trúc, phân quyền và các luồng nghiệp vụ cốt lõi của chức năng bán trái phiếu đến hạn hoặc rút trước hạn.</p>
            <div class="meta-tags">
                <div class="meta-tag">Phiên bản: <span>V1.0</span></div>
                <div class="meta-tag">Cập nhật: <span>07/06/2026</span></div>
                <div class="meta-tag">Chuẩn: <span>system_mapping_synthesizer</span></div>
            </div>
        </div>
    </header>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="container navbar-content">
            <a href="#glossary" class="active">Glossary</a>
            <a href="#architecture">Kiến Trúc</a>
            <a href="#matrix">Ma Trận Nghiệp Vụ</a>
            <a href="#workflows">Luồng Cốt Lõi</a>
        </div>
    </nav>

    <div class="container">

        <!-- Glossary Section -->
        <section id="glossary">
            <h2 class="section-title">Glossary (Thuật ngữ chuyên ngành)</h2>
            <div class="card">
                <p class="card-desc">Danh sách thuật ngữ chuyên ngành và từ viết tắt được giải thích bằng Tiếng Việt dễ hiểu.</p>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%">Thuật ngữ</th>
                            <th style="width: 25%">Tên gốc</th>
                            <th>Giải thích nghiệp vụ</th>
                        </tr>
                    </thead>
                    <tbody>
                        {glossary_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Architecture Section -->
        <section id="architecture">
            <h2 class="section-title">1. Kiến Trúc Hệ Thống</h2>

            <!-- Feature Tree -->
            <div class="card">
                <h3 class="card-title">1.1 Feature Tree (Cây phân rã chức năng)</h3>
                <p class="card-desc">Sơ đồ mindmap thể hiện cấu trúc phân rã các yêu cầu chức năng (FR) của US07.</p>
                <div class="diagram-container">
                    <pre class="mermaid">
mindmap
  root((US07: Bán Trái Phiếu PVCB))
    FR01 Xem thông tin bán trái phiếu
      Tab Điều hướng Bán trái phiếu
      Hiển thị số dư chốt 12h A1 và A2
      Hiển thị hạn mức còn lại C1 thấu chi
      Hiển thị thông tin đầu tư bán trái phiếu
        Tổng tiền bán trái phiếu
        Số tiền trả khách hàng Gross
      Bộ lọc danh sách Trạng thái trái phiếu
        Tất cả
        Đang hoạt động
        Không hoạt động
      Lưới danh sách hợp đồng bán
        Lựa chọn số bản ghi trên trang
        Các cột thông tin hợp đồng bán
      Xem chi tiết hợp đồng SLCĐ
    Job Hệ thống
      Job 12h chốt số liệu hàng ngày
                    </pre>
                </div>
            </div>

            <!-- Role Mapping -->
            <div class="card">
                <h3 class="card-title">1.2 Role Mapping (Bản đồ vai trò)</h3>
                <p class="card-desc">Bảng mô tả phạm vi quyền hạn và trách nhiệm của từng tác nhân trong hệ thống.</p>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 30%">Vai trò / Tác nhân</th>
                            <th>Phạm vi quyền hạn & Trách nhiệm</th>
                        </tr>
                    </thead>
                    <tbody>
                        {role_rows}
                    </tbody>
                </table>
            </div>

            <!-- State Lifecycle -->
            <div class="card">
                <h3 class="card-title">1.3 State Lifecycle (Vòng đời trạng thái)</h3>
                <p class="card-desc">Sơ đồ chuyển đổi trạng thái của Hợp đồng SLCĐ trong luồng Bán Trái phiếu.</p>
                <div class="diagram-container">
                    <pre class="mermaid">
stateDiagram-v2
    [*] --> CURRENT : HĐ được tạo thành công (US06 Approved)
    CURRENT --> PENDING_EARLY_CLOSE : KH đăng ký rút trước hạn trên app (trước Cut-off)
    
    state "Luồng Bán Trái Phiếu (12h T-1 đến 11h59'59'' T)" as LuongBan {{
        CURRENT --> Chờ_Bán : Đến ngày đến hạn gốc
        PENDING_EARLY_CLOSE --> Chờ_Bán : Đến ngày rút trước hạn
        Chờ_Bán --> Đã_Bán : Hạch toán mua/bán thành công (Duyệt US06)
    }}
    
    Đã_Bán --> CLOSED : Đã tất toán hợp đồng gốc
    Đã_Bán --> EARLY_CLOSED : Đã tất toán rút trước hạn
    
    CLOSED --> [*]
    EARLY_CLOSED --> [*]
                    </pre>
                </div>
                <div class="callout warning">
                    <div class="callout-title">Quy tắc vàng về trạng thái</div>
                    Hợp đồng chỉ được đưa vào danh sách Bán khi ở trạng thái <strong>CURRENT</strong> (đến hạn gốc) hoặc <strong>PENDING_EARLY_CLOSE</strong> (đăng ký rút trước hạn trước giờ Cut-off) trong khung thời gian từ 12h00 ngày làm việc T-1 đến 11h59'59'' ngày làm việc T.
                </div>
            </div>

            <!-- Integration Map -->
            <div class="card">
                <h3 class="card-title">1.4 Integration Map (Bản đồ tích hợp)</h3>
                <p class="card-desc">Sơ đồ thể hiện kiến trúc giao tiếp giữa Web CMS và các dịch vụ nội bộ, cơ sở dữ liệu và hệ thống ngân hàng lõi T24 cho luồng bán.</p>
                <div class="diagram-container">
                    <pre class="mermaid">
flowchart TD
    subgraph Frontend
        CMS[Web CMS]
    end
    subgraph Backend Services
        FIS[Investment Service]
    end
    subgraph Database
        DB[DB Investment]
    end
    subgraph External Systems
        T24[Core Banking T24]
    end
    
    CMS -->|1. Chọn Bán trái phiếu / API002| FIS
    CMS -->|2. Lấy số dư chốt / API003| FIS
    FIS -->|3. Truy vấn danh sách HĐ & Số dư chốt| DB
    FIS -->|4. Lấy thấu chi C1 realtime| T24
    T24 -->|5. Trả về hạn mức C1| FIS
    FIS -->|6. Phản hồi thông tin số dư & danh sách| CMS
                    </pre>
                </div>
            </div>

            <!-- Quick Reference Index -->
            <div class="card">
                <h3 class="card-title">1.5 Quick Reference Index (Mục lục API)</h3>
                <p class="card-desc">Danh sách các API phục vụ cho US07, bao gồm API xây mới và API tích hợp nâng cấp.</p>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 12%">Mã API</th>
                            <th style="width: 25%">Tên API</th>
                            <th>Mô tả chức năng</th>
                            <th style="width: 15%">Loại API</th>
                            <th style="width: 20%">URL</th>
                            <th>Tham số bổ sung / Đặc tả</th>
                        </tr>
                    </thead>
                    <tbody>
                        {api_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Business Matrix Section -->
        <section id="matrix">
            <h2 class="section-title">2. Ma Trận Nghiệp Vụ</h2>

            <!-- CRUD Matrix -->
            <div class="card">
                <h3 class="card-title">2.1 CRUD Permission Matrix</h3>
                <p class="card-desc">Ma trận phân quyền chi tiết cho Maker, Checker và các tiến trình tự động đối với luồng bán.</p>
                <table>
                    <thead>
                        <tr>
                            <th>Chức năng / Entity</th>
                            <th style="width: 20%">Maker (Nguồn vốn)</th>
                            <th style="width: 20%">Checker (Nguồn vốn)</th>
                            <th style="width: 20%">Job / Core Banking</th>
                            <th>Ghi chú nghiệp vụ</th>
                        </tr>
                    </thead>
                    <tbody>
                        {crud_rows}
                    </tbody>
                </table>
            </div>

            <!-- Common Rules Summary -->
            <div class="card">
                <h3 class="card-title">2.2 Common Rules Summary (Quy tắc chung cốt lõi)</h3>
                <p class="card-desc">Tổng hợp các quy tắc tính toán tài chính, chốt số dư và dòng tiền bán trái phiếu trong US07.</p>
                {rules_content}
            </div>
        </section>

        <!-- Core Workflows Section -->
        <section id="workflows">
            <h2 class="section-title">3. Luồng Nghiệp Vụ Cốt Lõi</h2>
            
            <div class="tab-buttons">
                <button class="tab-btn active" data-tab="flow1" onclick="selectTab('flow1')">Job 12h chốt số liệu hàng ngày</button>
                <button class="tab-btn" data-tab="flow2" onclick="selectTab('flow2')">Hiển thị màn hình Bán trái phiếu</button>
                <button class="tab-btn" data-tab="flow3" onclick="selectTab('flow3')">Lọc danh sách theo Trạng thái trái phiếu</button>
                <button class="tab-btn" data-tab="flow4" onclick="selectTab('flow4')">Xem chi tiết Hợp đồng SLCĐ</button>
            </div>

            <!-- Flow 1 -->
            <div id="flow1" class="tab-content active">
                <div class="card">
                    <h3 class="card-title" style="color: var(--accent-color);">Job 12h chốt số liệu hàng ngày</h3>
                    <p class="card-desc" style="margin-bottom: 20px;">Quy trình hệ thống tự động tổng hợp số dư tài khoản A1, A2 và hạn mức thấu chi C1 từ Core Banking T24 lúc 12h00 hàng ngày (tham chiếu logic chốt số dư từ US06).</p>
                    <div class="diagram-container" style="background-color: #0f0f1a;">
                        <pre class="mermaid">
sequenceDiagram
    autonumber
    participant Job12h as Hệ thống (Job 12h)
    participant T24 as Core Banking T24
    participant FIS as Investment Service
    participant DB as DB Investment
    
    Note over Job12h: Chạy tự động lúc 12h00 ngày làm việc T
    Job12h->>T24: API001: Lấy số dư TKTT A1 (Y), A2, dư nợ & hạn mức C1
    T24-->>Job12h: Trả về thông tin số dư tài khoản
    Job12h->>Job12h: Tổng hợp danh sách HĐ SLCĐ bán & mua trái phiếu
    Job12h->>Job12h: Chốt số dư hiển thị X theo quy tắc chốt số dư (US06)
    Job12h->>FIS: Yêu cầu lưu thông tin số dư chốt 12h
    FIS->>DB: Ghi nhận số dư A1 (X), A2, dư nợ C1 và hạn mức thấu chi vào DB
    DB-->>Job12h: Xác nhận lưu thành công
                        </pre>
                    </div>
                </div>
            </div>
            
            <!-- Flow 2 -->
            <div id="flow2" class="tab-content">
                <div class="card">
                    <h3 class="card-title" style="color: var(--accent-color);">Hiển thị màn hình Bán trái phiếu</h3>
                    <p class="card-desc" style="margin-bottom: 20px;">Quy trình Maker/Checker truy cập màn hình Bán trái phiếu, hệ thống gọi các API để hiển thị danh sách hợp đồng bán và thông tin dòng tiền đầu tư bán.</p>
                    <div class="diagram-container" style="background-color: #0f0f1a;">
                        <pre class="mermaid">
sequenceDiagram
    autonumber
    actor User as Maker / Checker
    participant CMS as Web CMS
    participant FIS as Investment Service
    participant T24 as Core Banking T24
    participant DB as DB Investment
    
    User->>CMS: Click chọn menu "Quản lý danh mục đầu tư / Bán trái phiếu"
    CMS->>FIS: API002: Lấy danh sách HĐ SLCĐ đến hạn / rút trước hạn
    Note over FIS: Khung thời gian: 12h T-1 đến 11h59'59'' T<br>Trạng thái HĐ: CURRENT, PENDING_EARLY_CLOSE
    FIS->>DB: Query các HĐ SLCĐ thỏa mãn điều kiện
    DB-->>FIS: Trả về danh sách HĐ SLCĐ
    FIS-->>CMS: Trả về danh sách hợp đồng bán & thông tin tổng đầu tư
    
    CMS->>FIS: API003: Lấy số dư TKTT A1, A2 chốt 12h và thấu chi C1 realtime
    FIS->>T24: Gọi T24 lấy hạn mức thấu chi C1 realtime
    T24-->>FIS: Trả về hạn mức C1 realtime
    FIS->>DB: Query số dư chốt A1, A2 lúc 12h từ DB
    DB-->>FIS: Trả về số dư chốt A1, A2
    FIS-->>CMS: Trả về thông tin số dư (A1, A2, C1)
    
    Note over CMS: Tính toán hiển thị:<br>- Tổng tiền bán trái phiếu<br>- Số tiền trả khách hàng (Gross)<br>- Render lưới dữ liệu HĐ
    CMS-->>User: Hiển thị giao diện màn hình "Bán trái phiếu"
                        </pre>
                    </div>
                </div>
            </div>
            
            <!-- Flow 3 -->
            <div id="flow3" class="tab-content">
                <div class="card">
                    <h3 class="card-title" style="color: var(--accent-color);">Lọc danh sách theo Trạng thái trái phiếu</h3>
                    <p class="card-desc" style="margin-bottom: 20px;">Quy trình người dùng lọc danh sách hợp đồng bán dưới lưới theo trạng thái hoạt động của trái phiếu. Lưu ý là thông tin tổng ở header không bị thay đổi.</p>
                    <div class="diagram-container" style="background-color: #0f0f1a;">
                        <pre class="mermaid">
sequenceDiagram
    autonumber
    actor User as Maker / Checker
    participant CMS as Web CMS
    participant FIS as Investment Service
    participant DB as DB Investment
    
    User->>CMS: Chọn trạng thái trái phiếu tại bộ lọc (Tất cả / Đang hoạt động / Không hoạt động)
    CMS->>FIS: API002: Call lấy danh sách (truyền param bondStatus tương ứng)
    FIS->>DB: Truy vấn dữ liệu hợp đồng có trạng thái TP khớp với điều kiện lọc
    DB-->>FIS: Trả về danh sách Hợp đồng đã lọc
    FIS-->>CMS: Trả về danh sách đã lọc
    Note over CMS: Cập nhật lưới danh sách hợp đồng dưới giao diện.<br>(Giữ nguyên Tổng tiền bán và Tổng tiền trả KH ở header)
    CMS-->>User: Hiển thị danh sách kết quả sau khi lọc
                        </pre>
                    </div>
                </div>
            </div>
            
            <!-- Flow 4 -->
            <div id="flow4" class="tab-content">
                <div class="card">
                    <h3 class="card-title" style="color: var(--accent-color);">Xem chi tiết Hợp đồng SLCĐ</h3>
                    <p class="card-desc" style="margin-bottom: 20px;">Quy trình người dùng click chọn xem chi tiết của riêng một hợp đồng SLCĐ trên lưới danh sách bán.</p>
                    <div class="diagram-container" style="background-color: #0f0f1a;">
                        <pre class="mermaid">
sequenceDiagram
    autonumber
    actor User as Maker / Checker
    participant CMS as Web CMS
    
    User->>CMS: Click chọn một bản ghi Hợp đồng bất kỳ trên lưới
    CMS->>CMS: Điều hướng sang URL xem chi tiết hợp đồng (US05)
    Note over CMS: Luồng xem chi tiết HĐ SLCĐ được xử lý tại US05
    CMS-->>User: Hiển thị giao diện chi tiết Hợp đồng SLCĐ (US05)
                        </pre>
                    </div>
                </div>
            </div>
        </section>

    </div>

    <!-- Script to handle tabs and nav highlighting -->
    <script>
        function selectTab(tabId) {{
            // Remove active class from all tabs & contents
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            // Add active class to selected tab & content
            const selectedBtn = document.querySelector(`[data-tab="${{tabId}}"]`);
            const selectedContent = document.getElementById(tabId);
            
            if (selectedBtn && selectedContent) {{
                selectedBtn.classList.add('active');
                selectedContent.classList.add('active');
            }}
        }}

        // Navbar active state mapping
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.navbar a');

        window.addEventListener('scroll', () => {{
            let current = '';
            sections.forEach(section => {{
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (pageYOffset >= (sectionTop - 80)) {{
                    current = section.getAttribute('id');
                }}
            }});

            navLinks.forEach(a => {{
                a.classList.remove('active');
                if (a.getAttribute('href') === `#${{current}}`) {{
                    a.classList.add('active');
                }}
            }});
        }});
    </script>

    <footer>
        <p>© 2026 Hệ thống Profix - Tài liệu phân tích và mapping nghiệp vụ US07. Thiết kế bởi Antigravity.</p>
    </footer>
</body>
</html>
"""
    # Ghi file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Generated System Mapping HTML: {output_path}")

if __name__ == '__main__':
    generate_html("/Users/mac/antigravity-testing-kit/Tài liệu toàn hệ thống Profix/tài liệu/US07_SinhLoiChuDong_SystemMapping.html")
