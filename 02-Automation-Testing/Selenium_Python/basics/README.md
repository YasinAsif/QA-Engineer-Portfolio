# 🤖 Selenium Python Basics

This folder contains fundamental Selenium WebDriver examples and learning materials for automation testing.

## 📚 Contents

### 1. `first_test.py`
Complete learning examples covering:
- Basic browser operations (open, navigate, close)
- Finding elements (ID, Name, CSS, XPath)
- Element interactions (click, type, clear)
- Explicit waits
- Complete test cases

### 2. `locators.py`
Centralized element locators organized by page:
- `LoginPageLocators` - Login page elements
- `InventoryPageLocators` - Products page elements
- `CartPageLocators` - Shopping cart elements
- `CheckoutPageLocators` - Checkout flow elements
- `DynamicLocators` - Runtime locator helpers

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install selenium webdriver-manager
```

### Running the Examples
```bash
# Run first test examples
python first_test.py

# View locators structure
python locators.py
```

---

## 📖 Learning Path

1. **Start with `first_test.py`**
   - Understand how to open a browser
   - Learn element location strategies
   - Practice interactions

2. **Study `locators.py`**
   - Understand Page Object Model preparation
   - Learn locator best practices
   - See how to organize selectors

3. **Move to `projects/` folder**
   - Apply learning to real automation
   - Use Page Object Model pattern
   - Write maintainable tests

---

## 🎯 Key Concepts Covered

### Locator Strategies
| Strategy | Example | When to Use |
|----------|---------|-------------|
| `By.ID` | `"user-name"` | Unique IDs (most reliable) |
| `By.NAME` | `"username"` | Form fields |
| `By.CLASS_NAME` | `"login_btn"` | Styled elements |
| `By.CSS_SELECTOR` | `"#login-button"` | Complex selections |
| `By.XPATH` | `"//div[@class='x']"` | Complex DOM navigation |
| `By.LINK_TEXT` | `"Click Here"` | Link elements |

### Wait Strategies
```python
# Implicit Wait (applies to all elements)
driver.implicitly_wait(10)

# Explicit Wait (specific conditions)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "element")))
```

### Common Expected Conditions
- `visibility_of_element_located` - Element visible
- `element_to_be_clickable` - Element clickable
- `presence_of_element_located` - Element in DOM
- `url_contains` - URL verification
- `title_contains` - Page title check

---

## 📁 File Structure

```
basics/
├── README.md           # This file
├── first_test.py       # Learning examples
└── locators.py         # Centralized locators
```

---

## ✅ Next Steps

After mastering basics, proceed to:
- `../projects/saucedemo_automation/` - Full Page Object Model project
- `../utilities/` - Reusable test utilities

---

*Part of QA Engineer Portfolio - Automation Testing*
