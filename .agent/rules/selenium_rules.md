---
trigger: manual
---

# Selenium Web Automation Rules

## 1. Selenium Locator Priority Rules
When automating browser operations directly with Java and Selenium WebDriver, adhere to the strict fallback locator hierarchies below to maintain speed and element stability.

**Priority Order:**
1. `id`
2. `data-testid` / `data-test` / `data-qa`
3. `name`
4. `css selector`
5. `xpath` (Final Option)

*Do's:*
```java
driver.findElement(By.id("login-txt"));
driver.findElement(By.cssSelector("button[data-testid='submit-btn']"));
```

*Don'ts:*
Avoid constructing heavy cascading structural identifiers through XPath.
`//div[3]/div[2]/form/div[1]/button`

## 2. Waiting Strategy & Synchronization
* **Absolutely DO NOT use `Thread.sleep()`** anywhere under any automation scenarios unless handling exceptionally rare external system interruptions where no web polling works.
* Only rely on Java Explicit Waits with `WebDriverWait` and `ExpectedConditions` classes.

*Example pattern:*
```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("profile")));
```
