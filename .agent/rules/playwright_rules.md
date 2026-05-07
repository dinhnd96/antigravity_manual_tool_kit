---
trigger: manual
---

# Playwright Specific Rules

> Các Rule dành riêng cho việc thiết lập và chạy Automation với Playwright Tools.

## 1. Thuộc tính & Thiết Lập Browser (MANDATORY)
* **UI Debugging Viewport:** Mọi quá trình debug UI bắt buộc chạy với viewport của màn hình máy tính desktop (ví dụ tiêu chuẩn: `1920x1080`).
* **Headed Mode Base:** Bắt buộc mở browser có hiển thị (headed mode) trong quá trình thiết lập và debug test.
* **Headless Mode Deployment:** Chế độ `headless mode` chỉ được phép sử dụng khi test đã debug PASS 100% trên real UI, hoặc khi CI/CD build pipelines setup mặc định.

## 2. Workflow Phát Triển & Tìm Element (Recon & UI)
* Ưu tiên dùng tối đa công cụ **Playwright MCP** để chạy browser và tương tác với trang đích.
* **Inspect DOM Thực Tế:** Verify và capture trực tiếp các selector từ browser DOM.
* **TUYỆT ĐỐI KHÔNG SUY ĐOÁN** hoặc copy locator mù quáng từ cấu trúc mã cũ, hoặc dựa trên URL mà không verify sự tồn tại.

## 3. Playwright Locator Selection
Playwright defines a highly optimized list of User-facing semantic locators. Rely heavily on these instead of structural identifiers.

**Tiêu Chuẩn Ưu Tiên Locators (Priority Order):**
1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()`
5. `get_by_test_id()`
6. `locator("css")` – fallback when required.

*For example:* Use `page.get_by_role("button", new Page.GetByRoleOptions().setName("Submit"))` instead of XPath parsing. Avoid basic CSS / XPaths wherever roles/labels are clear.

## 4. Syncing & Waiting Strategy (Anti-patterns)
* **CẤM** sử dụng hard-coded timeout (`waitForTimeout`, `sleep`, cố định thời gian trễ).
* Tối ưu khả năng auto-waiting của Playwright thông qua Web-First Assertions:
  * `expect(locator).toBeVisible()`
  * `expect(locator).toBeEnabled()`
* Tối giản việc gọi các manual waits (`waitForSelector()`) tự xây dựng nếu Playwright `expect` đã bao phủ được sự kiện render.
