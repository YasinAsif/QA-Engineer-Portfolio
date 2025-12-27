# 🤖 Sauce Demo Automation Project

A professional Selenium WebDriver automation framework with Page Object Model for the Sauce Demo e-commerce application.

## 📋 Project Overview

| Feature | Description |
|---------|-------------|
| **Application Under Test** | [Sauce Demo](https://www.saucedemo.com) |
| **Framework** | Selenium WebDriver + Python |
| **Design Pattern** | Page Object Model (POM) |
| **Test Framework** | Pytest |
| **Author** | Muhammad Yasin Asif |

---

## 🏗️ Project Structure

```
saucedemo_automation/
├── pages/                      # Page Object Classes
│   ├── __init__.py            # Package exports
│   ├── base_page.py           # Base class with common methods
│   ├── login_page.py          # Login page object
│   ├── inventory_page.py      # Products/Inventory page object
│   ├── cart_page.py           # Shopping cart page object
│   └── checkout_page.py       # Checkout flow page objects
│
├── tests/                      # Test Suites
│   ├── __init__.py
│   ├── test_login.py          # Login functionality tests (10 tests)
│   ├── test_cart.py           # Shopping cart tests (10 tests)
│   └── test_checkout.py       # Checkout flow tests (10 tests)
│
├── conftest.py                 # Pytest fixtures and configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google Chrome browser
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YasinAsif/QA-Engineer-Portfolio.git
cd QA-Engineer-Portfolio/02-Automation-Testing/Selenium_Python/projects/saucedemo_automation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Test Files
```bash
pytest tests/test_login.py -v
pytest tests/test_cart.py -v
pytest tests/test_checkout.py -v
```

### Run Tests by Markers
```bash
# Smoke tests (critical functionality)
pytest -v -m smoke

# Login tests only
pytest -v -m login

# Cart tests only
pytest -v -m cart

# Checkout tests only
pytest -v -m checkout

# Negative tests
pytest -v -m negative
```

### Run with HTML Report
```bash
pytest -v --html=reports/report.html --self-contained-html
```

### Run in Headless Mode
```bash
pytest -v --headless
```

---

## 📊 Test Coverage

### Test Summary

| Module | Test Cases | Description |
|--------|------------|-------------|
| **Login** | 10 | Valid/invalid login, validation, UI checks |
| **Cart** | 10 | Add/remove items, persistence, totals |
| **Checkout** | 10 | Complete flow, validation, cancel actions |
| **Total** | **30** | Comprehensive E2E coverage |

### Test Types

| Type | Count | Description |
|------|-------|-------------|
| Smoke | 5 | Critical path tests |
| Regression | 25 | Full functionality |
| Negative | 8 | Error handling |
| UI | 3 | Visual verification |

---

## 🎨 Page Object Model

### Benefits of POM
- ✅ **Maintainability** - Locators in one place
- ✅ **Reusability** - Methods shared across tests
- ✅ **Readability** - Tests read like user actions
- ✅ **Scalability** - Easy to add new tests

### Usage Example

```python
from pages import LoginPage, InventoryPage

def test_add_to_cart(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    
    # Add product
    inventory_page.add_backpack_to_cart()
    
    # Verify
    assert inventory_page.get_cart_count() == 1
```

---

## 🔧 Configuration

### Pytest Markers

| Marker | Description |
|--------|-------------|
| `@pytest.mark.smoke` | Critical tests |
| `@pytest.mark.regression` | Full suite |
| `@pytest.mark.login` | Login tests |
| `@pytest.mark.cart` | Cart tests |
| `@pytest.mark.checkout` | Checkout tests |
| `@pytest.mark.negative` | Error cases |

### Fixtures

| Fixture | Scope | Description |
|---------|-------|-------------|
| `driver` | function | Fresh WebDriver per test |
| `driver_headless` | function | Headless browser |
| `login_page` | function | LoginPage instance |
| `logged_in_user` | function | Pre-authenticated state |

---

## 📸 Screenshots on Failure

Screenshots are automatically captured when a test fails and saved to:
```
screenshots/{test_name}_{timestamp}.png
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Programming language |
| **Selenium** | Browser automation |
| **Pytest** | Test framework |
| **WebDriver Manager** | Driver management |
| **Page Object Model** | Design pattern |

---

## 📈 Future Enhancements

- [ ] Allure reporting integration
- [ ] Parallel test execution
- [ ] Cross-browser testing (Firefox, Edge)
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions

---

## 📚 Learning Outcomes

Building this project helped me learn:
1. **Page Object Model** - Professional framework design
2. **Pytest Fixtures** - Test setup and teardown
3. **Explicit Waits** - Reliable element interactions
4. **Test Organization** - Markers and structure
5. **Error Handling** - Robust test cases

---

## 🔗 Related Documentation

- [Selenium Basics](../../basics/)
- [Main Portfolio](../../../../README.md)
- [Manual Testing](../../../../01-Manual-Testing/)

---

*Part of QA Engineer Portfolio - Automation Testing Phase*
