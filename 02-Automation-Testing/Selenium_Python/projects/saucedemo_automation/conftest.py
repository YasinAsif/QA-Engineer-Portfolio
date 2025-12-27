"""
Pytest Configuration
====================
Fixtures and configuration for Sauce Demo test automation.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages import LoginPage


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to create and quit WebDriver for each test.
    
    Yields:
        WebDriver instance
    """
    # Setup Chrome options
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    
    # Create driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture(scope="function")
def driver_headless():
    """
    Fixture for headless browser testing.
    
    Yields:
        WebDriver instance in headless mode
    """
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """
    Fixture to provide LoginPage instance.
    
    Args:
        driver: WebDriver fixture
        
    Yields:
        LoginPage instance
    """
    page = LoginPage(driver)
    page.open()
    yield page


@pytest.fixture(scope="function")
def logged_in_user(driver):
    """
    Fixture to provide logged-in state.
    
    Args:
        driver: WebDriver fixture
        
    Yields:
        InventoryPage instance (user logged in)
    """
    login_page = LoginPage(driver)
    login_page.open()
    inventory_page = login_page.login_as_standard_user()
    yield inventory_page


# =============================================================================
# PYTEST HOOKS
# =============================================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots on test failure.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get driver from fixture
        driver = item.funcargs.get('driver')
        if driver:
            # Create screenshots directory
            screenshots_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            
            # Take screenshot
            driver.save_screenshot(filepath)
            print(f"\nScreenshot saved: {filepath}")


def pytest_configure(config):
    """
    Configure pytest with custom markers.
    """
    config.addinivalue_line("markers", "smoke: Smoke tests - critical functionality")
    config.addinivalue_line("markers", "regression: Regression tests - full test suite")
    config.addinivalue_line("markers", "login: Tests related to login functionality")
    config.addinivalue_line("markers", "cart: Tests related to shopping cart")
    config.addinivalue_line("markers", "checkout: Tests related to checkout flow")
    config.addinivalue_line("markers", "negative: Negative test cases")


# =============================================================================
# TEST DATA
# =============================================================================

class TestData:
    """Test data constants."""
    
    # URLs
    BASE_URL = "https://www.saucedemo.com"
    INVENTORY_URL = f"{BASE_URL}/inventory.html"
    CART_URL = f"{BASE_URL}/cart.html"
    
    # Valid Users
    STANDARD_USER = ("standard_user", "secret_sauce")
    PROBLEM_USER = ("problem_user", "secret_sauce")
    PERFORMANCE_USER = ("performance_glitch_user", "secret_sauce")
    
    # Invalid Users
    LOCKED_USER = ("locked_out_user", "secret_sauce")
    INVALID_USER = ("invalid_user", "wrong_password")
    
    # Checkout Data
    CHECKOUT_INFO = {
        'first_name': 'John',
        'last_name': 'Doe',
        'postal_code': '12345'
    }
    
    # Products
    PRODUCTS = [
        'Sauce Labs Backpack',
        'Sauce Labs Bike Light',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Fleece Jacket',
        'Sauce Labs Onesie',
        'Test.allTheThings() T-Shirt (Red)'
    ]


# Make TestData available to tests
@pytest.fixture
def test_data():
    """Provide test data to tests."""
    return TestData
