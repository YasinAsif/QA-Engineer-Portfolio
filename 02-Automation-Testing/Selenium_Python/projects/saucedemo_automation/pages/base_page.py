"""
Base Page Class
================
Foundation class for all page objects in the framework.
Implements common methods used across all pages.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from typing import List, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """
    Base class for all Page Objects.
    
    Provides common functionality like:
    - Element finding with waits
    - Common actions (click, type, etc.)
    - Page verification methods
    """
    
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Initialize BasePage.
        
        Args:
            driver: WebDriver instance
            timeout: Default wait timeout in seconds
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
    
    # =========================================================================
    # ELEMENT FINDING METHODS
    # =========================================================================
    
    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find element with explicit wait.
        
        Args:
            locator: Tuple of (By, locator_string)
            
        Returns:
            WebElement if found
        """
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def find_visible_element(self, locator: Tuple[str, str]) -> WebElement:
        """Find element that is visible."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_clickable_element(self, locator: Tuple[str, str]) -> WebElement:
        """Find element that is clickable."""
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
    
    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Find multiple elements."""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def is_element_present(self, locator: Tuple[str, str]) -> bool:
        """Check if element exists in DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def is_element_visible(self, locator: Tuple[str, str]) -> bool:
        """Check if element is visible."""
        try:
            element = self.find_visible_element(locator)
            return element.is_displayed()
        except TimeoutException:
            return False
    
    # =========================================================================
    # INTERACTION METHODS
    # =========================================================================
    
    def click(self, locator: Tuple[str, str]):
        """Click on element."""
        self.find_clickable_element(locator).click()
    
    def type_text(self, locator: Tuple[str, str], text: str, clear_first: bool = True):
        """
        Type text into input field.
        
        Args:
            locator: Element locator
            text: Text to type
            clear_first: Clear field before typing
        """
        element = self.find_visible_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: Tuple[str, str]) -> str:
        """Get text content of element."""
        return self.find_visible_element(locator).text
    
    def get_attribute(self, locator: Tuple[str, str], attribute: str) -> str:
        """Get attribute value of element."""
        return self.find_element(locator).get_attribute(attribute)
    
    def select_by_text(self, locator: Tuple[str, str], text: str):
        """Select dropdown option by visible text."""
        select = Select(self.find_element(locator))
        select.select_by_visible_text(text)
    
    def select_by_value(self, locator: Tuple[str, str], value: str):
        """Select dropdown option by value."""
        select = Select(self.find_element(locator))
        select.select_by_value(value)
    
    def hover(self, locator: Tuple[str, str]):
        """Hover over element."""
        from selenium.webdriver.common.action_chains import ActionChains
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    # =========================================================================
    # WAIT METHODS
    # =========================================================================
    
    def wait_for_url_contains(self, text: str) -> bool:
        """Wait for URL to contain specific text."""
        try:
            return self.wait.until(EC.url_contains(text))
        except TimeoutException:
            return False
    
    def wait_for_title_contains(self, text: str) -> bool:
        """Wait for page title to contain text."""
        try:
            return self.wait.until(EC.title_contains(text))
        except TimeoutException:
            return False
    
    def wait_for_element_invisible(self, locator: Tuple[str, str]) -> bool:
        """Wait for element to become invisible."""
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
    
    # =========================================================================
    # PAGE METHODS
    # =========================================================================
    
    def get_current_url(self) -> str:
        """Get current page URL."""
        return self.driver.current_url
    
    def get_title(self) -> str:
        """Get page title."""
        return self.driver.title
    
    def navigate_to(self, url: str):
        """Navigate to URL."""
        self.driver.get(url)
    
    def refresh_page(self):
        """Refresh current page."""
        self.driver.refresh()
    
    def go_back(self):
        """Navigate back in browser history."""
        self.driver.back()
    
    def go_forward(self):
        """Navigate forward in browser history."""
        self.driver.forward()
    
    # =========================================================================
    # SCREENSHOT METHODS
    # =========================================================================
    
    def take_screenshot(self, filename: str):
        """Take screenshot and save to file."""
        self.driver.save_screenshot(filename)
    
    def get_screenshot_as_base64(self) -> str:
        """Get screenshot as base64 string."""
        return self.driver.get_screenshot_as_base64()
    
    # =========================================================================
    # JAVASCRIPT METHODS
    # =========================================================================
    
    def execute_script(self, script: str, *args):
        """Execute JavaScript."""
        return self.driver.execute_script(script, *args)
    
    def scroll_to_element(self, locator: Tuple[str, str]):
        """Scroll element into view."""
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_to_bottom(self):
        """Scroll to page bottom."""
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def scroll_to_top(self):
        """Scroll to page top."""
        self.execute_script("window.scrollTo(0, 0);")
