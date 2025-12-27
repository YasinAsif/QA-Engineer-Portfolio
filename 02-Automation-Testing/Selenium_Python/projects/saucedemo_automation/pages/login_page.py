"""
Login Page Object
=================
Page Object for the Sauce Demo Login page.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for Sauce Demo Login Page.
    
    URL: https://www.saucedemo.com
    """
    
    # Page URL
    URL = "https://www.saucedemo.com"
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CLASS_NAME, "error-button")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    
    def __init__(self, driver: WebDriver):
        """Initialize LoginPage."""
        super().__init__(driver)
    
    # =========================================================================
    # PAGE ACTIONS
    # =========================================================================
    
    def open(self):
        """Navigate to login page."""
        self.navigate_to(self.URL)
        return self
    
    def enter_username(self, username: str):
        """Enter username in the username field."""
        self.type_text(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password: str):
        """Enter password in the password field."""
        self.type_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)
        return self
    
    def login(self, username: str, password: str):
        """
        Perform complete login action.
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            InventoryPage if login successful
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
        # Return InventoryPage if login successful
        if self.is_login_successful():
            from .inventory_page import InventoryPage
            return InventoryPage(self.driver)
        return self
    
    def login_as_standard_user(self):
        """Login using standard_user credentials."""
        return self.login("standard_user", "secret_sauce")
    
    def login_as_problem_user(self):
        """Login using problem_user credentials."""
        return self.login("problem_user", "secret_sauce")
    
    def login_as_performance_user(self):
        """Login using performance_glitch_user credentials."""
        return self.login("performance_glitch_user", "secret_sauce")
    
    # =========================================================================
    # PAGE VERIFICATIONS
    # =========================================================================
    
    def is_login_page_displayed(self) -> bool:
        """Check if login page is displayed."""
        return self.is_element_visible(self.LOGIN_LOGO)
    
    def is_login_successful(self) -> bool:
        """Check if login was successful (redirected to inventory)."""
        return self.wait_for_url_contains("inventory")
    
    def get_error_message(self) -> str:
        """Get the error message text."""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def close_error_message(self):
        """Close the error message."""
        if self.is_element_visible(self.ERROR_CLOSE_BUTTON):
            self.click(self.ERROR_CLOSE_BUTTON)
        return self
    
    # =========================================================================
    # FIELD VALIDATIONS
    # =========================================================================
    
    def get_username_value(self) -> str:
        """Get current value in username field."""
        return self.get_attribute(self.USERNAME_INPUT, "value")
    
    def get_password_value(self) -> str:
        """Get current value in password field."""
        return self.get_attribute(self.PASSWORD_INPUT, "value")
    
    def is_password_masked(self) -> bool:
        """Check if password field is masked (type=password)."""
        field_type = self.get_attribute(self.PASSWORD_INPUT, "type")
        return field_type == "password"
    
    def clear_fields(self):
        """Clear both username and password fields."""
        self.find_element(self.USERNAME_INPUT).clear()
        self.find_element(self.PASSWORD_INPUT).clear()
        return self
