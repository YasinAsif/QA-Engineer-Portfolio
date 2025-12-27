"""
Cart Page Object
================
Page Object for the Sauce Demo Shopping Cart page.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class CartPage(BasePage):
    """
    Page Object for Sauce Demo Cart Page.
    
    URL: https://www.saucedemo.com/cart.html
    """
    
    # Page URL
    URL = "https://www.saucedemo.com/cart.html"
    
    # Locators - Page Elements
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    
    # Locators - Cart Item Details
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    
    # Locators - Buttons
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id^='remove-']")
    
    def __init__(self, driver: WebDriver):
        """Initialize CartPage."""
        super().__init__(driver)
    
    # =========================================================================
    # PAGE NAVIGATION
    # =========================================================================
    
    def open(self):
        """Navigate to cart page directly."""
        self.navigate_to(self.URL)
        return self
    
    def continue_shopping(self):
        """Go back to shopping (inventory page)."""
        self.click(self.CONTINUE_SHOPPING)
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def proceed_to_checkout(self):
        """Proceed to checkout."""
        self.click(self.CHECKOUT_BUTTON)
        from .checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
    
    # =========================================================================
    # CART ACTIONS
    # =========================================================================
    
    def remove_item(self, product_name: str):
        """
        Remove item from cart by product name.
        
        Args:
            product_name: Product ID like 'sauce-labs-backpack'
        """
        locator = (By.ID, f"remove-{product_name}")
        self.click(locator)
        return self
    
    def remove_all_items(self):
        """Remove all items from cart."""
        while self.get_cart_item_count() > 0:
            remove_buttons = self.find_elements(self.REMOVE_BUTTON)
            if remove_buttons:
                remove_buttons[0].click()
            else:
                break
        return self
    
    # =========================================================================
    # CART INFORMATION
    # =========================================================================
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart."""
        try:
            items = self.find_elements(self.CART_ITEM)
            return len(items)
        except:
            return 0
    
    def get_all_cart_items(self) -> List[Dict]:
        """
        Get information about all items in cart.
        
        Returns:
            List of dictionaries with item details
        """
        items = []
        cart_items = self.find_elements(self.CART_ITEM)
        
        for item in cart_items:
            items.append({
                'name': item.find_element(*self.ITEM_NAME).text,
                'description': item.find_element(*self.ITEM_DESCRIPTION).text,
                'price': item.find_element(*self.ITEM_PRICE).text,
                'quantity': item.find_element(*self.CART_QUANTITY).text
            })
        
        return items
    
    def get_cart_item_names(self) -> List[str]:
        """Get list of item names in cart."""
        name_elements = self.find_elements(self.ITEM_NAME)
        return [elem.text for elem in name_elements]
    
    def get_cart_total_price(self) -> float:
        """Calculate total price of items in cart."""
        price_elements = self.find_elements(self.ITEM_PRICE)
        total = 0.0
        for elem in price_elements:
            price_text = elem.text.replace("$", "")
            total += float(price_text)
        return total
    
    def is_item_in_cart(self, product_name: str) -> bool:
        """Check if specific item is in cart."""
        cart_items = self.get_cart_item_names()
        return product_name in cart_items
    
    # =========================================================================
    # PAGE VERIFICATIONS
    # =========================================================================
    
    def is_cart_page_displayed(self) -> bool:
        """Check if cart page is displayed."""
        return (self.is_element_visible(self.PAGE_TITLE) and 
                "cart" in self.get_current_url())
    
    def get_page_title(self) -> str:
        """Get the page title text."""
        return self.get_text(self.PAGE_TITLE)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty."""
        return self.get_cart_item_count() == 0
