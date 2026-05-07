---
trigger: manual
---

# General Locator Strategies (Cross-Platform / Cross-Tool)

Locator stability and readability define an automation framework's health. 
**Core rule:** Never lock elements by visual DOM structures matching styling frames, build your structure independently using attributes.

## 1. Master Priority Map
1. **Accessibility Attributes / Aria Traits** (Screen readers & semantic data - Best for A11y tests)
2. **Dedicated Test Attributes** (`data-testid`, `data-test`, `data-qa`)
3. **Primary Structural ID/Names** (`id`, `resource-id`, `name`)
4. **Tool native specific semantic functions** (E.g. Playwright role/placeholder calls)
5. **CSS Selector**
6. **XPath Expressions**

## 2. Enforcing Stability Rules
Whatever the approach, all locators must explicitly verify they are:
* **Unique in scope:** Can only capture one exact entity representation throughout the interface.
* **Invariant Layout-wise:** Survives cosmetic DOM injections (i.e. changing a flexbox grouping `div/div`).

**Never utilize:**
* Dynamic string bindings and temporary hashing identifiers on CSS classes (e.g. `css-1n2xyz-btn`).
* `nth-child`, `nth-of-type` structure chains when better alternatives exist.
* Random auto-generated framework IDs.

## 3. Standard Verification / Generation
Before permanently placing a locator string inside the source files codebase, verify:
* Does the target matching represent only one object in Inspector views?
* Is this object the actual visual interactable component or an overlying blocked shadow DOM mask?
* Re-launch or reload the view frame and ensure the target pointer survives correctly.
