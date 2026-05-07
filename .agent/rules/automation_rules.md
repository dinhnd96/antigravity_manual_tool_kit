---
trigger: manual
---

# QA Automation General Rules

These rules apply universally to all automation test implementation tasks.

## 1. Architecture & Framework
* **Design Pattern:** Always strictly use the Page Object Model (POM).
* **Separation of Concerns:** Keep Page Elements/Actions mapped properly in Page classes. Avoid keeping assertions within Page classes; place assertions in Test classes. Keep test data detached from functional code.

## 2. Test Data Generation
* **Uniqueness:** All fields requiring unique entities (e.g., Email, Username, Code, ID) must be generated dynamically. Use UUIDs or timestamping.
* **Random yet Deterministic Data:** Generated data must be traceable (e.g., `featurename + timestamp + prefix`) so that failures correspond to specific data entries.

## 3. Code Quality & Formatting
* Refrain from duplicated logic. Create highly reusable helper functions for widespread actions.
* Automation methods must be simple, easily readable, and heavily maintainable.
* Remove all temporary `print()`, debug outputs, unused locators, or commented blocks prior to finalizing scripts.

## 4. File Output & Preventions
* Do NOT auto-delete source files without explicitly checking repository intent.
* Check the current directory structure before recreating new utility or Page classes to prevent duplication.

## 5. Naming Conventions (Java Based)
* **Page Classes:** Class name with "Page" suffix (e.g., `LoginPage.java`, `CartPage.java`).
* **Test Classes:** Class name with "Test" suffix (e.g., `LoginTest.java`).
* **Test Methods:** Must start with prefix `test` and clearly state what behavior is verified (e.g., `testLoginWithValidCredentials()`).
* **Page Elements (Variables):** Standard lowerCamelCase with context-friendly suffixes (e.g., `loginButton`, `usernameInput`, `searchResultText`).