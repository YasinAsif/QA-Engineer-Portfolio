"""
Inventory Page Object
=====================
Page Object for the Sauce Demo Inventory/Products page.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for Sauce Demo Inventory Page.
    
    URL: https://www.saucedemo.com/inventory.html
    """
    
    # Page URL
    URL = "https://www.saucedemo.com/inventory.html"
    
    # Locators - Header
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    
    # Locators - Page Content
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    
    # Locators - Product Details
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    
    # Locators - Sorting
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    # Locators - Sidebar Menu
    CLOSE_MENU_BUTTON = (By.ID, "react-burger-cross-btn")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    
    # Product Add to Cart Buttons
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_TSHIRT_RED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    
    # Product Remove Buttons
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    
    def __init__(self, driver: WebDriver):
        """Initialize InventoryPage."""
        super().__init__(driver)
    
    # =========================================================================
    # PAGE NAVIGATION
    # =========================================================================
    
    def open(self):
        """Navigate to inventory page directly (requires login)."""
        self.navigate_to(self.URL)
        return self
    
    def go_to_cart(self):
        """Navigate to shopping cart."""
        self.click(self.SHOPPING_CART_LINK)
        from .cart_page import CartPage
        return CartPage(self.driver)
    
    def open_menu(self):
        """Open the hamburger menu."""
        self.click(self.HAMBURGER_MENU)
        return self
    
    def close_menu(self):
        """Close the hamburger menu."""
        self.click(self.CLOSE_MENU_BUTTON)
        return self
    
    def logout(self):
        """Logout from the application."""
        self.open_menu()
        self.click(self.LOGOUT_LINK)
        from .login_page import LoginPage
        return LoginPage(self.driver)
    
    def reset_app_state(self):
        """Reset the app state (clear cart, etc.)."""
        self.open_menu()
        self.click(self.RESET_LINK)
        self.close_menu()
        return self
    
    # =========================================================================
    # PRODUCT ACTIONS
    # =========================================================================
    
    def add_product_to_cart(self, product_name: str):
        """
        Add a product to cart by name.
        
        Args:
            product_name: Name like 'sauce-labs-backpack'
        """
        locator = (By.ID, f"add-to-cart-{product_name}")
        self.click(locator)
        return self
    
    def remove_product_from_cart(self, product_name: str):
        """
        Remove a product from cart by name.
        
        Args:
            product_name: Name like 'sauce-labs-backpack'
        """
        locator = (By.ID, f"remove-{product_name}")
        self.click(locator)
        return self
    
    def add_backpack_to_cart(self):
        """Add Sauce Labs Backpack to cart."""
        self.click(self.ADD_BACKPACK)
        return self
    
    def add_bike_light_to_cart(self):
        """Add Sauce Labs Bike Light to cart."""
        self.click(self.ADD_BIKE_LIGHT)
        return self
    
    def add_bolt_tshirt_to_cart(self):
        """Add Sauce Labs Bolt T-Shirt to cart."""
        self.click(self.ADD_BOLT_TSHIRT)
        return self
    
    def add_fleece_jacket_to_cart(self):
        """Add Sauce Labs Fleece Jacket to cart."""
        self.click(self.ADD_FLEECE_JACKET)
        return self
    
    def add_all_products_to_cart(self):
        """Add all products to cart."""
        self.add_backpack_to_cart()
        self.add_bike_light_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_fleece_jacket_to_cart()
        self.click(self.ADD_ONESIE)
        self.click(self.ADD_TSHIRT_RED)
        return self
    
    def click_product(self, product_name: str):
        """Click on a product to view details."""
        locator = (By.XPATH, f"//div[@class='inventory_item_name ' and text()='{product_name}']")
        self.click(locator)
        return self
    
    # =========================================================================
    # SORTING
    # =========================================================================
    
    def sort_by_name_a_to_z(self):
        """Sort products A to Z."""
        self.select_by_value(self.SORT_DROPDOWN, "az")
        return self
    
    def sort_by_name_z_to_a(self):
        """Sort products Z to A."""
        self.select_by_value(self.SORT_DROPDOWN, "za")
        return self
    
    def sort_by_price_low_to_high(self):
        """Sort products by price low to high."""
        self.select_by_value(self.SORT_DROPDOWN, "lohi")
        return self
    
    def sort_by_price_high_to_low(self):
        """Sort products by price high to low."""
        self.select_by_value(self.SORT_DROPDOWN, "hilo")
        return self
    
    # =========================================================================
    # PAGE VERIFICATIONS
    # =========================================================================
    
    def is_inventory_page_displayed(self) -> bool:
        """Check if inventory page is displayed."""
        return (self.is_element_visible(self.PAGE_TITLE) and 
                "inventory" in self.get_current_url())
    
    def get_page_title(self) -> str:
        """Get the page title text."""
        return self.get_text(self.PAGE_TITLE)
    
    def get_cart_count(self) -> int:
        """Get the number of items in cart."""
        if self.is_element_present(self.SHOPPING_CART_BADGE):
            badge_text = self.get_text(self.SHOPPING_CART_BADGE)
            return int(badge_text) if badge_text else 0
        return 0
    
    def get_product_count(self) -> int:
        """Get the number of products on the page."""
        products = self.find_elements(self.INVENTORY_ITEM)
        return len(products)
    
    def get_all_product_names(self) -> List[str]:
        """Get list of all product names."""
        name_elements = self.find_elements(self.ITEM_NAME)
        return [elem.text for elem in name_elements]
    
    def get_all_product_prices(self) -> List[float]:
        """Get list of all product prices."""
        price_elements = self.find_elements(self.ITEM_PRICE)
        prices = []
        for elem in price_elements:
            price_text = elem.text.replace("$", "")
            prices.append(float(price_text))
        return prices
    
    def get_product_info(self, index: int = 0) -> Dict:
        """
        Get information about a specific product.
        
        Args:
            index: Product index (0-based)
            
        Returns:
            Dictionary with product info
        """
        products = self.find_elements(self.INVENTORY_ITEM)
        if index >= len(products):
            return {}
        
        product = products[index]
        return {
            'name': product.find_element(*self.ITEM_NAME).text,
            'description': product.find_element(*self.ITEM_DESCRIPTION).text,
            'price': product.find_element(*self.ITEM_PRICE).text
        }
    
    def is_product_in_cart(self, product_name: str) -> bool:
        """Check if product has been added to cart (Remove button visible)."""
        locator = (By.ID, f"remove-{product_name}")
        return self.is_element_present(locator)
