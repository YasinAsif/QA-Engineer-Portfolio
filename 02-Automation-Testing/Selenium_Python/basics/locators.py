"""
Locators Module
===============
Centralized element locators for Sauce Demo application.
Demonstrates best practices for organizing locators.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Locators for the Login Page."""
    
    # Page URL
    URL = "https://www.saucedemo.com"
    
    # Form Elements
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    # Error Messages
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    
    # Page Elements
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    BOT_IMAGE = (By.CLASS_NAME, "bot_column")
    LOGIN_CREDENTIALS = (By.ID, "login_credentials")
    LOGIN_PASSWORD = (By.CLASS_NAME, "login_password")


class InventoryPageLocators:
    """Locators for the Inventory/Products Page."""
    
    # Page URL
    URL = "https://www.saucedemo.com/inventory.html"
    
    # Header Elements
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn")
    
    # Page Title
    PAGE_TITLE = (By.CLASS_NAME, "title")
    
    # Products
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    
    # Add to Cart Buttons (specific products)
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_TSHIRT_RED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    
    # Remove from Cart Buttons
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    REMOVE_BOLT_TSHIRT = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_FLEECE_JACKET = (By.ID, "remove-sauce-labs-fleece-jacket")
    REMOVE_ONESIE = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_TSHIRT_RED = (By.ID, "remove-test.allthethings()-t-shirt-(red)")
    
    # Sorting
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SORT_AZ = (By.XPATH, "//option[@value='az']")
    SORT_ZA = (By.XPATH, "//option[@value='za']")
    SORT_LOHI = (By.XPATH, "//option[@value='lohi']")
    SORT_HILO = (By.XPATH, "//option[@value='hilo']")
    
    # Sidebar Menu
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CLOSE_MENU = (By.ID, "react-burger-cross-btn")
    ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    
    # Footer
    FOOTER = (By.CLASS_NAME, "footer")
    TWITTER_LINK = (By.CSS_SELECTOR, "a[href*='twitter']")
    FACEBOOK_LINK = (By.CSS_SELECTOR, "a[href*='facebook']")
    LINKEDIN_LINK = (By.CSS_SELECTOR, "a[href*='linkedin']")


class CartPageLocators:
    """Locators for the Shopping Cart Page."""
    
    # Page URL
    URL = "https://www.saucedemo.com/cart.html"
    
    # Cart Elements
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    CART_ITEM_LABEL = (By.CLASS_NAME, "cart_item_label")
    
    # Item Details
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESCRIPTION = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    
    # Buttons
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id^='remove-']")


class CheckoutPageLocators:
    """Locators for the Checkout Pages."""
    
    # Step One - Your Information
    STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Step Two - Overview
    STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
    
    SUMMARY_INFO = (By.CLASS_NAME, "summary_info")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    # Complete
    COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"
    
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS = (By.CLASS_NAME, "pony_express")
    BACK_HOME = (By.ID, "back-to-products")


class ProductDetailLocators:
    """Locators for Product Detail Page."""
    
    # Back Button
    BACK_BUTTON = (By.ID, "back-to-products")
    
    # Product Details
    DETAIL_CONTAINER = (By.CLASS_NAME, "inventory_details_container")
    DETAIL_NAME = (By.CLASS_NAME, "inventory_details_name")
    DETAIL_DESC = (By.CLASS_NAME, "inventory_details_desc")
    DETAIL_PRICE = (By.CLASS_NAME, "inventory_details_price")
    DETAIL_IMAGE = (By.CLASS_NAME, "inventory_details_img")
    
    # Add/Remove Button
    ADD_TO_CART = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_FROM_CART = (By.CSS_SELECTOR, "button[id^='remove']")


# =============================================================================
# DYNAMIC LOCATORS
# =============================================================================
class DynamicLocators:
    """
    Helper class for creating dynamic locators.
    Useful when element attributes depend on runtime values.
    """
    
    @staticmethod
    def product_add_button(product_name: str) -> tuple:
        """Get add to cart button for specific product."""
        product_id = product_name.lower().replace(' ', '-')
        return (By.ID, f"add-to-cart-{product_id}")
    
    @staticmethod
    def product_remove_button(product_name: str) -> tuple:
        """Get remove button for specific product."""
        product_id = product_name.lower().replace(' ', '-')
        return (By.ID, f"remove-{product_id}")
    
    @staticmethod
    def product_link(product_name: str) -> tuple:
        """Get product link by name."""
        return (By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']")
    
    @staticmethod
    def cart_item_by_name(product_name: str) -> tuple:
        """Get cart item by product name."""
        return (By.XPATH, f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='cart_item']")


# =============================================================================
# USAGE EXAMPLE
# =============================================================================
if __name__ == '__main__':
    print("Locators Module - Usage Examples")
    print("=" * 50)
    
    # Show how to use locators
    print("\nLogin Page Locators:")
    print(f"  Username Input: {LoginPageLocators.USERNAME_INPUT}")
    print(f"  Password Input: {LoginPageLocators.PASSWORD_INPUT}")
    print(f"  Login Button: {LoginPageLocators.LOGIN_BUTTON}")
    
    print("\nInventory Page Locators:")
    print(f"  Cart Link: {InventoryPageLocators.SHOPPING_CART_LINK}")
    print(f"  Add Backpack: {InventoryPageLocators.ADD_BACKPACK}")
    
    print("\nDynamic Locators:")
    print(f"  Add 'Sauce Labs Bolt T-Shirt': {DynamicLocators.product_add_button('sauce-labs-bolt-t-shirt')}")
    
    print("\n" + "=" * 50)
    print("Import this module in your tests:")
    print("  from locators import LoginPageLocators, InventoryPageLocators")
