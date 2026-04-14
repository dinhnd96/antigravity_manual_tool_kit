# GEMINI AI - GLOBAL AUTOMATION AGENT RULES

> **Scope:** Áp dụng cho mọi tác vụ Test Automation do Gemini (Antigravity) hoạt động trong dự án này.
> **Mục tiêu:** Sinh ra test scripts hiệu quả, ổn định – dễ debug – dễ scale – CI friendly.

## 1. Ngôn Ngữ & Giao Tiếp
* Luôn giao tiếp, giải thích ý tưởng và báo cáo bằng **Tiếng Việt**.
* Diễn giải **ngắn gọn, rõ ràng, dễ hiểu**.
* Tránh suy đoán lập trình hoặc giải thích mơ hồ về lỗi mà cần có căn cứ trực tiếp.

## 2. Quy Trình Làm Việc Hành Động (Workflow)
* **Recon (Điều tra):** Luôn inspect hiển thị giao diện thực tế hoặc cơ sở HTML/DOM/XML trước khi viết automation. Tuyệt đối KHÔNG ĐOÁN locator.
* **Implementation:** Giữ vững mô hình **Page Object Model (POM)**. Phân tách rõ Page objects, Test execution và Utils/Test data.
* **Execution & Self-fix:** Chạy test ngay sau khi code xong. Nếu test FAIL, tự đọc log, phân tích root cause và sửa code. Lặp lại đến khi PASS ổn định. Chỉ báo cáo cho User để xác nhận Business rule nếu gặp requirements mâu thuẫn.
* **Cleanup:** Gỡ bỏ các logs, code thừa, và locator rỗng/hỏng trước khi commit.

## 3. Kiến Trúc Khung Khuyến Nghị (Framework Stack)
* **Language:** Java
* **Web Automation:** Selenium WebDriver hoặc Playwright
* **Mobile Automation:** Appium
* **API Automation:** REST Assured
* **Test Framework:** TestNG

## 4. Tham Khảo Các Bộ Rules Chi Tiết
Agent phải luôn tham chiếu kiểm tra quy tắc chi tiết theo tool trong thư mục `.agent/rules/`:
* [Automation General Rules](.agent/rules/automation_rules.md)
* [Locator Strategy Rules](.agent/rules/locator_strategy.md)
* [Playwright Specific Rules](.agent/rules/playwright_rules.md)
* [Selenium Specific Rules](.agent/rules/selenium_rules.md)
* [Appium Specific Rules](.agent/rules/appium_rules.md)
