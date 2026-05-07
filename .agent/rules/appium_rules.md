---
trigger: manual
---

# Appium Mobile Automation Rules

## 1. Appium Native Locator Rules
Follow native locating strategies that correlate directly with OS definitions (iOS / Android) instead of generic web equivalents.

**Priority Order for Locators:**
1. `accessibility id`
2. `resource-id` (Android natively specific)
3. `id`
4. `iOS predicate string` (iOS inherently specific and fast)
5. `iOS class chain` (iOS structural queries)
6. `xpath` (Use only as the absolute last resort)

*Optimized Implementation Standard:*
```java
// Accessibility id - Cross-platform robust
driver.findElement(AppiumBy.accessibilityId("login_button"));

// OS Explicit - Android (resource-id)
driver.findElement(AppiumBy.id("com.application.xyz:id/login_button"));

// OS Explicit - iOS (Predicate String)
driver.findElement(AppiumBy.iOSNsPredicateString("label == 'Login'"));
```

## 2. Things You MUST Avoid
* Deeply nested index-based absolute XPaths are strictly banned since minor layout modifications immediately result in false positive unhandled failures:
  **BAD:** `//android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[1]`
* Do not attempt querying non-scrollable off-screen UI rendering without proper Appium scrolling drivers/plugins.
