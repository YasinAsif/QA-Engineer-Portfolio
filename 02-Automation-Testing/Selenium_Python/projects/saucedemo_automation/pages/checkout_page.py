"""
Checkout Page Objects
=====================
Page Objects for the Sauce Demo Checkout flow.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CheckoutPage(BasePage):
    """
    Page Object for Checkout Step One - Your Information.
    
    URL: https://www.saucedemo.com/checkout-step-one.html
    """
    
    # Page URL
    URL = "https://www.saucedemo.com/checkout-step-one.html"
    
    # Locators - Form Fields
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    
    # Locators - Buttons
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    # Locators - Error
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver: WebDriver):
        """Initialize CheckoutPage."""
        super().__init__(driver)
    
    # =========================================================================
    # FORM ACTIONS
    # =========================================================================
    
    def enter_first_name(self, first_name: str):
        """Enter first name."""
        self.type_text(self.FIRST_NAME, first_name)
        return self
    
    def enter_last_name(self, last_name: str):
        """Enter last name."""
        self.type_text(self.LAST_NAME, last_name)
        return self
    
    def enter_postal_code(self, postal_code: str):
        """Enter postal code."""
        self.type_text(self.POSTAL_CODE, postal_code)
        return self
    
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """
        Fill all checkout information fields.
        
        Args:
            first_name: Customer first name
            last_name: Customer last name
            postal_code: Postal/ZIP code
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self
    
    def click_continue(self):
        """Click continue button."""
        self.click(self.CONTINUE_BUTTON)
        # Check if we moved to overview page
        if self.wait_for_url_contains("checkout-step-two"):
            return CheckoutOverviewPage(self.driver)
        return self
    
    def click_cancel(self):
        """Click cancel button to go back to cart."""
        self.click(self.CANCEL_BUTTON)
        from .cart_page import CartPage
        return CartPage(self.driver)
    
    def complete_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill form and continue to overview."""
        self.fill_checkout_info(first_name, last_name, postal_code)
        return self.click_continue()
    
    # =========================================================================
    # VERIFICATIONS
    # =========================================================================
    
    def is_checkout_page_displayed(self) -> bool:
        """Check if checkout info page is displayed."""
        return "checkout-step-one" in self.get_current_url()
    
    def get_error_message(self) -> str:
        """Get error message text."""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_error_displayed(self) -> bool:
        """Check if error is displayed."""
        return self.is_element_visible(self.ERROR_MESSAGE)


class CheckoutOverviewPage(BasePage):
    """
    Page Object for Checkout Step Two - Overview.
    
    URL: https://www.saucedemo.com/checkout-step-two.html
    """
    
    # Page URL
    URL = "https://www.saucedemo.com/checkout-step-two.html"
    
    # Locators - Summary
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    
    # Locators - Totals
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    
    # Locators - Buttons
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    def __init__(self, driver: WebDriver):
        """Initialize CheckoutOverviewPage."""
        super().__init__(driver)
    
    # =========================================================================
    # ACTIONS
    # =========================================================================
    
    def click_finish(self):
        """Click finish button to complete order."""
        self.click(self.FINISH_BUTTON)
        return CheckoutCompletePage(self.driver)
    
    def click_cancel(self):
        """Click cancel to go back to inventory."""
        self.click(self.CANCEL_BUTTON)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    # =========================================================================
    # ORDER INFORMATION
    # =========================================================================
    
    def get_subtotal(self) -> float:
        """Get order subtotal."""
        text = self.get_text(self.SUMMARY_SUBTOTAL)
        # Extract number from "Item total: $XX.XX"
        return float(text.split("$")[1])
    
    def get_tax(self) -> float:
        """Get order tax."""
        text = self.get_text(self.SUMMARY_TAX)
        return float(text.split("$")[1])
    
    def get_total(self) -> float:
        """Get order total."""
        text = self.get_text(self.SUMMARY_TOTAL)
        return float(text.split("$")[1])
    
    def get_item_count(self) -> int:
        """Get number of items in order."""
        items = self.find_elements(self.CART_ITEM)
        return len(items)
    
    # =========================================================================
    # VERIFICATIONS
    # =========================================================================
    
    def is_overview_page_displayed(self) -> bool:
        """Check if overview page is displayed."""
        return "checkout-step-two" in self.get_current_url()
    
    def verify_totals(self) -> bool:
        """Verify that subtotal + tax = total."""
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        total = self.get_total()
        return abs((subtotal + tax) - total) < 0.01  # Allow small floating point variance


class CheckoutCompletePage(BasePage):
    """
    Page Object for Checkout Complete page.
    
    URL: https://www.saucedemo.com/checkout-complete.html
    """
    
    # Page URL
    URL = "https://www.saucedemo.com/checkout-complete.html"
    
    # Locators
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS = (By.CLASS_NAME, "pony_express")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def __init__(self, driver: WebDriver):
        """Initialize CheckoutCompletePage."""
        super().__init__(driver)
    
    # =========================================================================
    # ACTIONS
    # =========================================================================
    
    def click_back_home(self):
        """Click back home button."""
        self.click(self.BACK_HOME_BUTTON)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    # =========================================================================
    # VERIFICATIONS
    # =========================================================================
    
    def is_order_complete(self) -> bool:
        """Check if order was completed successfully."""
        return (self.is_element_visible(self.COMPLETE_HEADER) and 
                "checkout-complete" in self.get_current_url())
    
    def get_confirmation_header(self) -> str:
        """Get the confirmation header text."""
        return self.get_text(self.COMPLETE_HEADER)
    
    def get_confirmation_text(self) -> str:
        """Get the confirmation body text."""
        return self.get_text(self.COMPLETE_TEXT)
    
    def is_pony_express_displayed(self) -> bool:
        """Check if pony express image is displayed."""
        return self.is_element_visible(self.PONY_EXPRESS)
