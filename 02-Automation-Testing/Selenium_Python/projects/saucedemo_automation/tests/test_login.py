"""
Login Test Suite
================
Automated tests for Sauce Demo Login functionality.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import pytest
from pages import LoginPage


class TestLogin:
    """Test suite for Login functionality."""
    
    # =========================================================================
    # POSITIVE TESTS
    # =========================================================================
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_with_valid_credentials(self, driver):
        """
        TC-001: Verify login with valid standard user credentials.
        
        Steps:
        1. Navigate to login page
        2. Enter valid username
        3. Enter valid password
        4. Click login button
        
        Expected Result:
        - User is redirected to inventory page
        - Products are displayed
        """
        # Arrange
        login_page = LoginPage(driver)
        login_page.open()
        
        # Act
        inventory_page = login_page.login("standard_user", "secret_sauce")
        
        # Assert
        assert inventory_page.is_inventory_page_displayed(), \
            "Inventory page should be displayed after login"
        assert inventory_page.get_product_count() == 6, \
            "Should display 6 products"
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_with_problem_user(self, driver):
        """
        TC-002: Verify login with problem user credentials.
        
        Steps:
        1. Navigate to login page
        2. Login as problem_user
        
        Expected Result:
        - User is logged in successfully
        - Inventory page is displayed
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        inventory_page = login_page.login_as_problem_user()
        
        assert inventory_page.is_inventory_page_displayed()
    
    # =========================================================================
    # NEGATIVE TESTS
    # =========================================================================
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_locked_out_user(self, driver):
        """
        TC-003: Verify locked out user cannot login.
        
        Steps:
        1. Navigate to login page
        2. Enter locked_out_user credentials
        3. Click login
        
        Expected Result:
        - Error message is displayed
        - User remains on login page
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login("locked_out_user", "secret_sauce")
        
        assert login_page.is_error_displayed(), \
            "Error message should be displayed"
        assert "locked out" in login_page.get_error_message().lower(), \
            "Error should mention locked out"
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_invalid_username(self, driver):
        """
        TC-004: Verify login fails with invalid username.
        
        Steps:
        1. Navigate to login page
        2. Enter invalid username
        3. Enter valid password
        4. Click login
        
        Expected Result:
        - Error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login("invalid_user", "secret_sauce")
        
        assert login_page.is_error_displayed()
        assert "do not match" in login_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_invalid_password(self, driver):
        """
        TC-005: Verify login fails with invalid password.
        
        Steps:
        1. Navigate to login page
        2. Enter valid username
        3. Enter invalid password
        4. Click login
        
        Expected Result:
        - Error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.login("standard_user", "wrong_password")
        
        assert login_page.is_error_displayed()
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_empty_username(self, driver):
        """
        TC-006: Verify login fails with empty username.
        
        Expected Result:
        - Error message: "Username is required"
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        assert login_page.is_error_displayed()
        assert "username is required" in login_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_empty_password(self, driver):
        """
        TC-007: Verify login fails with empty password.
        
        Expected Result:
        - Error message: "Password is required"
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.enter_username("standard_user")
        login_page.click_login()
        
        assert login_page.is_error_displayed()
        assert "password is required" in login_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.login
    def test_login_with_empty_credentials(self, driver):
        """
        TC-008: Verify login fails with both fields empty.
        
        Expected Result:
        - Error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        login_page.click_login()
        
        assert login_page.is_error_displayed()
    
    # =========================================================================
    # UI TESTS
    # =========================================================================
    
    @pytest.mark.login
    def test_password_field_is_masked(self, driver):
        """
        TC-009: Verify password field masks characters.
        
        Expected Result:
        - Password field type is 'password'
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        assert login_page.is_password_masked(), \
            "Password field should mask characters"
    
    @pytest.mark.login
    def test_login_page_displayed_correctly(self, driver):
        """
        TC-010: Verify login page elements are displayed.
        
        Expected Result:
        - Logo is visible
        - Username field is visible
        - Password field is visible
        - Login button is visible
        """
        login_page = LoginPage(driver)
        login_page.open()
        
        assert login_page.is_login_page_displayed(), \
            "Login page should display logo"
        assert login_page.is_element_visible(login_page.USERNAME_INPUT), \
            "Username field should be visible"
        assert login_page.is_element_visible(login_page.PASSWORD_INPUT), \
            "Password field should be visible"
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), \
            "Login button should be visible"


# Run tests from command line:
# pytest test_login.py -v
# pytest test_login.py -v -m smoke
# pytest test_login.py -v -m negative
