"""
First Selenium Test
===================
Basic Selenium WebDriver examples for learning automation.
Demonstrates fundamental Selenium concepts with Sauce Demo.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# =============================================================================
# EXAMPLE 1: Basic Browser Operations
# =============================================================================
def example_basic_operations():
    """
    Demonstrates basic Selenium operations:
    - Opening browser
    - Navigating to URL
    - Getting page title
    - Closing browser
    """
    print("=" * 50)
    print("Example 1: Basic Browser Operations")
    print("=" * 50)
    
    # Setup Chrome driver
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Navigate to URL
        driver.get("https://www.saucedemo.com")
        print(f"Page Title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        # Wait to observe
        time.sleep(2)
        
    finally:
        driver.quit()
        print("Browser closed successfully")


# =============================================================================
# EXAMPLE 2: Finding Elements
# =============================================================================
def example_finding_elements():
    """
    Demonstrates different ways to find elements:
    - By ID
    - By Name
    - By Class Name
    - By CSS Selector
    - By XPath
    """
    print("\n" + "=" * 50)
    print("Example 2: Finding Elements")
    print("=" * 50)
    
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://www.saucedemo.com")
        
        # Find by ID
        username_field = driver.find_element(By.ID, "user-name")
        print(f"Found username field by ID: {username_field.get_attribute('placeholder')}")
        
        # Find by Name (if available)
        password_field = driver.find_element(By.ID, "password")
        print(f"Found password field by ID: {password_field.get_attribute('placeholder')}")
        
        # Find by CSS Selector
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        print(f"Found login button by CSS: {login_button.get_attribute('value')}")
        
        # Find by XPath
        logo = driver.find_element(By.XPATH, "//div[@class='login_logo']")
        print(f"Found logo by XPath: {logo.text}")
        
        # Find by Class Name
        login_container = driver.find_element(By.CLASS_NAME, "login_container")
        print("Found login container by class name")
        
    finally:
        driver.quit()


# =============================================================================
# EXAMPLE 3: Interacting with Elements
# =============================================================================
def example_element_interactions():
    """
    Demonstrates element interactions:
    - Typing text
    - Clicking buttons
    - Clearing fields
    """
    print("\n" + "=" * 50)
    print("Example 3: Element Interactions")
    print("=" * 50)
    
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://www.saucedemo.com")
        
        # Find elements
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")
        
        # Type into fields
        username.send_keys("standard_user")
        print("Entered username")
        
        password.send_keys("secret_sauce")
        print("Entered password")
        
        # Click button
        login_btn.click()
        print("Clicked login button")
        
        # Wait for page load
        time.sleep(2)
        
        # Verify login success
        if "inventory" in driver.current_url:
            print("✅ Login successful! Redirected to inventory page.")
        else:
            print("❌ Login failed!")
            
    finally:
        driver.quit()


# =============================================================================
# EXAMPLE 4: Explicit Waits
# =============================================================================
def example_explicit_waits():
    """
    Demonstrates explicit waits:
    - Wait for element visibility
    - Wait for element to be clickable
    - Wait for URL change
    """
    print("\n" + "=" * 50)
    print("Example 4: Explicit Waits")
    print("=" * 50)
    
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://www.saucedemo.com")
        
        # Create WebDriverWait object
        wait = WebDriverWait(driver, 10)
        
        # Wait for username field to be visible
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        print("Username field is visible")
        
        # Wait for login button to be clickable
        login_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        print("Login button is clickable")
        
        # Perform login
        username.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        login_btn.click()
        
        # Wait for URL to contain "inventory"
        wait.until(EC.url_contains("inventory"))
        print("✅ Successfully navigated to inventory page")
        
        # Wait for products to be visible
        products = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        print(f"Found {len(products)} products on the page")
        
    finally:
        driver.quit()


# =============================================================================
# EXAMPLE 5: Complete Login Test
# =============================================================================
def test_login_valid_credentials():
    """
    Complete test case: Login with valid credentials
    Follows test automation best practices.
    """
    print("\n" + "=" * 50)
    print("TEST: Login with Valid Credentials")
    print("=" * 50)
    
    # Test data
    test_url = "https://www.saucedemo.com"
    username = "standard_user"
    password = "secret_sauce"
    expected_url = "inventory.html"
    
    # Setup
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    
    test_passed = False
    
    try:
        # Step 1: Navigate to login page
        print("[Step 1] Navigate to login page")
        driver.get(test_url)
        assert "Swag Labs" in driver.title, "Page title mismatch"
        
        # Step 2: Enter username
        print("[Step 2] Enter username")
        username_field = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)
        
        # Step 3: Enter password
        print("[Step 3] Enter password")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        # Step 4: Click login button
        print("[Step 4] Click login button")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        # Step 5: Verify successful login
        print("[Step 5] Verify successful login")
        wait.until(EC.url_contains(expected_url))
        
        # Verify products are displayed
        products = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        assert len(products) == 6, f"Expected 6 products, found {len(products)}"
        
        test_passed = True
        print("\n" + "✅ TEST PASSED: Login successful")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: Assertion error - {e}")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        
    finally:
        driver.quit()
        print("-" * 50)
        
    return test_passed


# =============================================================================
# EXAMPLE 6: Login with Invalid Credentials
# =============================================================================
def test_login_invalid_credentials():
    """
    Test case: Login with invalid credentials
    Verifies error message is displayed.
    """
    print("\n" + "=" * 50)
    print("TEST: Login with Invalid Credentials")
    print("=" * 50)
    
    # Test data
    test_url = "https://www.saucedemo.com"
    username = "invalid_user"
    password = "wrong_password"
    expected_error = "Username and password do not match"
    
    # Setup
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    
    test_passed = False
    
    try:
        # Step 1: Navigate to login page
        print("[Step 1] Navigate to login page")
        driver.get(test_url)
        
        # Step 2: Enter invalid credentials
        print("[Step 2] Enter invalid credentials")
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        
        # Step 3: Click login button
        print("[Step 3] Click login button")
        driver.find_element(By.ID, "login-button").click()
        
        # Step 4: Verify error message
        print("[Step 4] Verify error message")
        error_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        
        error_text = error_element.text
        assert expected_error in error_text, f"Unexpected error: {error_text}"
        
        test_passed = True
        print(f"\n✅ TEST PASSED: Error displayed correctly")
        print(f"   Error message: {error_text}")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        
    finally:
        driver.quit()
        print("-" * 50)
        
    return test_passed


# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("   SELENIUM WEBDRIVER - LEARNING EXAMPLES")
    print("   Sauce Demo Automation")
    print("=" * 60)
    
    # Run examples
    # Uncomment the examples you want to run:
    
    # example_basic_operations()
    # example_finding_elements()
    # example_element_interactions()
    # example_explicit_waits()
    
    # Run test cases
    test_login_valid_credentials()
    test_login_invalid_credentials()
    
    print("\n" + "=" * 60)
    print("   All examples completed!")
    print("=" * 60)
