"""
Cart Test Suite
===============
Automated tests for Sauce Demo Shopping Cart functionality.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import pytest
from pages import LoginPage


class TestCart:
    """Test suite for Shopping Cart functionality."""
    
    # =========================================================================
    # ADD TO CART TESTS
    # =========================================================================
    
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_add_single_product_to_cart(self, logged_in_user):
        """
        TC-011: Verify adding single product to cart.
        
        Steps:
        1. Login as standard user
        2. Add Sauce Labs Backpack to cart
        
        Expected Result:
        - Cart badge shows "1"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        
        assert inventory_page.get_cart_count() == 1, \
            "Cart should have 1 item"
    
    @pytest.mark.cart
    def test_add_multiple_products_to_cart(self, logged_in_user):
        """
        TC-012: Verify adding multiple products to cart.
        
        Steps:
        1. Login as standard user
        2. Add Backpack to cart
        3. Add Bike Light to cart
        4. Add Bolt T-Shirt to cart
        
        Expected Result:
        - Cart badge shows "3"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        
        assert inventory_page.get_cart_count() == 3, \
            "Cart should have 3 items"
    
    @pytest.mark.cart
    def test_add_all_products_to_cart(self, logged_in_user):
        """
        TC-013: Verify adding all products to cart.
        
        Steps:
        1. Login and add all 6 products
        
        Expected Result:
        - Cart badge shows "6"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_all_products_to_cart()
        
        assert inventory_page.get_cart_count() == 6, \
            "Cart should have 6 items"
    
    # =========================================================================
    # REMOVE FROM CART TESTS
    # =========================================================================
    
    @pytest.mark.cart
    def test_remove_product_from_cart_on_inventory(self, logged_in_user):
        """
        TC-014: Verify removing product from inventory page.
        
        Steps:
        1. Add product to cart
        2. Remove product from inventory page
        
        Expected Result:
        - Cart count decreases
        - Add button reappears
        """
        inventory_page = logged_in_user
        
        # Add product
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_count() == 1
        
        # Remove product
        inventory_page.remove_product_from_cart("sauce-labs-backpack")
        
        assert inventory_page.get_cart_count() == 0, \
            "Cart should be empty after removal"
    
    @pytest.mark.cart
    def test_remove_product_from_cart_page(self, logged_in_user):
        """
        TC-015: Verify removing product from cart page.
        
        Steps:
        1. Add product to cart
        2. Go to cart
        3. Remove product
        
        Expected Result:
        - Product is removed from cart
        """
        inventory_page = logged_in_user
        
        # Add and go to cart
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        
        assert cart_page.get_cart_item_count() == 1
        
        # Remove from cart
        cart_page.remove_item("sauce-labs-backpack")
        
        assert cart_page.is_cart_empty(), \
            "Cart should be empty"
    
    # =========================================================================
    # CART PAGE TESTS
    # =========================================================================
    
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_view_cart_items(self, logged_in_user):
        """
        TC-016: Verify viewing items in cart.
        
        Steps:
        1. Add products to cart
        2. Navigate to cart page
        
        Expected Result:
        - Cart page displays correct items
        - Item details are shown
        """
        inventory_page = logged_in_user
        
        # Add products
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        
        # Go to cart
        cart_page = inventory_page.go_to_cart()
        
        assert cart_page.is_cart_page_displayed(), \
            "Cart page should be displayed"
        assert cart_page.get_cart_item_count() == 2, \
            "Cart should have 2 items"
    
    @pytest.mark.cart
    def test_continue_shopping_from_cart(self, logged_in_user):
        """
        TC-017: Verify continue shopping button.
        
        Steps:
        1. Add product and go to cart
        2. Click Continue Shopping
        
        Expected Result:
        - Returns to inventory page
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        
        # Continue shopping
        inventory_page = cart_page.continue_shopping()
        
        assert inventory_page.is_inventory_page_displayed(), \
            "Should return to inventory page"
    
    @pytest.mark.cart
    def test_cart_preserves_items_on_navigation(self, logged_in_user):
        """
        TC-018: Verify cart items persist during navigation.
        
        Steps:
        1. Add products to cart
        2. Navigate to cart
        3. Continue shopping
        4. Return to cart
        
        Expected Result:
        - Items remain in cart
        """
        inventory_page = logged_in_user
        
        # Add products
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        
        # Navigate away and back
        cart_page = inventory_page.go_to_cart()
        inventory_page = cart_page.continue_shopping()
        cart_page = inventory_page.go_to_cart()
        
        assert cart_page.get_cart_item_count() == 2, \
            "Cart items should persist"
    
    # =========================================================================
    # CART INFORMATION TESTS
    # =========================================================================
    
    @pytest.mark.cart
    def test_cart_displays_correct_item_info(self, logged_in_user):
        """
        TC-019: Verify cart displays correct item information.
        
        Expected Result:
        - Item name is correct
        - Price is correct
        - Quantity is correct
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        
        items = cart_page.get_all_cart_items()
        
        assert len(items) == 1
        assert "Sauce Labs Backpack" in items[0]['name']
        assert "$29.99" in items[0]['price']
        assert items[0]['quantity'] == "1"
    
    @pytest.mark.cart
    def test_cart_calculates_total_correctly(self, logged_in_user):
        """
        TC-020: Verify cart total calculation.
        
        Steps:
        1. Add known-price items
        2. Check total
        
        Expected Result:
        - Total matches sum of prices
        """
        inventory_page = logged_in_user
        
        # Add Backpack ($29.99) and Bike Light ($9.99)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        
        cart_page = inventory_page.go_to_cart()
        total = cart_page.get_cart_total_price()
        
        expected_total = 29.99 + 9.99
        assert abs(total - expected_total) < 0.01, \
            f"Total should be ${expected_total}, got ${total}"


# Run tests:
# pytest test_cart.py -v
# pytest test_cart.py -v -m smoke
