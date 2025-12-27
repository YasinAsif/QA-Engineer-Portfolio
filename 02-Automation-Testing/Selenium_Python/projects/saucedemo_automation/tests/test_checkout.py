"""
Checkout Test Suite
===================
Automated tests for Sauce Demo Checkout functionality.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import pytest
from pages import LoginPage


class TestCheckout:
    """Test suite for Checkout functionality."""
    
    # =========================================================================
    # CHECKOUT FLOW TESTS
    # =========================================================================
    
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_complete_checkout_flow(self, logged_in_user):
        """
        TC-021: Verify complete checkout flow (E2E).
        
        Steps:
        1. Login and add product
        2. Go to cart
        3. Proceed to checkout
        4. Fill information
        5. Complete order
        
        Expected Result:
        - Order confirmation is displayed
        """
        inventory_page = logged_in_user
        
        # Add product and checkout
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        # Fill checkout info
        overview_page = checkout_page.complete_checkout_info(
            first_name="John",
            last_name="Doe",
            postal_code="12345"
        )
        
        # Verify overview
        assert overview_page.is_overview_page_displayed(), \
            "Overview page should be displayed"
        
        # Complete order
        complete_page = overview_page.click_finish()
        
        assert complete_page.is_order_complete(), \
            "Order should be complete"
        assert "thank you" in complete_page.get_confirmation_header().lower(), \
            "Should show thank you message"
    
    @pytest.mark.checkout
    def test_checkout_with_multiple_items(self, logged_in_user):
        """
        TC-022: Verify checkout with multiple items.
        
        Steps:
        1. Add multiple products
        2. Complete checkout
        
        Expected Result:
        - All items shown in overview
        - Order completes successfully
        """
        inventory_page = logged_in_user
        
        # Add multiple products
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        
        # Checkout
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        overview_page = checkout_page.complete_checkout_info("Jane", "Smith", "67890")
        
        # Verify items in overview
        assert overview_page.get_item_count() == 3, \
            "Should show 3 items in overview"
        
        # Complete
        complete_page = overview_page.click_finish()
        assert complete_page.is_order_complete()
    
    # =========================================================================
    # CHECKOUT INFORMATION VALIDATION
    # =========================================================================
    
    @pytest.mark.negative
    @pytest.mark.checkout
    def test_checkout_empty_first_name(self, logged_in_user):
        """
        TC-023: Verify error when first name is empty.
        
        Expected Result:
        - Error message: "First Name is required"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        # Fill only last name and postal code
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed()
        assert "first name" in checkout_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.checkout
    def test_checkout_empty_last_name(self, logged_in_user):
        """
        TC-024: Verify error when last name is empty.
        
        Expected Result:
        - Error message: "Last Name is required"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        checkout_page.enter_first_name("John")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed()
        assert "last name" in checkout_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.checkout
    def test_checkout_empty_postal_code(self, logged_in_user):
        """
        TC-025: Verify error when postal code is empty.
        
        Expected Result:
        - Error message: "Postal Code is required"
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed()
        assert "postal code" in checkout_page.get_error_message().lower()
    
    @pytest.mark.negative
    @pytest.mark.checkout
    def test_checkout_all_fields_empty(self, logged_in_user):
        """
        TC-026: Verify error when all fields are empty.
        
        Expected Result:
        - Error message is displayed
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed()
    
    # =========================================================================
    # CHECKOUT OVERVIEW TESTS
    # =========================================================================
    
    @pytest.mark.checkout
    def test_checkout_overview_shows_totals(self, logged_in_user):
        """
        TC-027: Verify checkout overview displays totals.
        
        Expected Result:
        - Subtotal is displayed
        - Tax is displayed
        - Total is displayed
        - Total = Subtotal + Tax
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        overview_page = checkout_page.complete_checkout_info("John", "Doe", "12345")
        
        # Verify totals
        subtotal = overview_page.get_subtotal()
        tax = overview_page.get_tax()
        total = overview_page.get_total()
        
        assert subtotal > 0, "Subtotal should be greater than 0"
        assert tax > 0, "Tax should be calculated"
        assert overview_page.verify_totals(), \
            "Total should equal subtotal + tax"
    
    @pytest.mark.checkout
    def test_cancel_from_checkout_info(self, logged_in_user):
        """
        TC-028: Verify cancel from checkout info page.
        
        Expected Result:
        - Returns to cart page
        - Items still in cart
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        
        # Cancel
        cart_page = checkout_page.click_cancel()
        
        assert cart_page.is_cart_page_displayed(), \
            "Should return to cart"
        assert cart_page.get_cart_item_count() == 1, \
            "Item should still be in cart"
    
    @pytest.mark.checkout
    def test_cancel_from_checkout_overview(self, logged_in_user):
        """
        TC-029: Verify cancel from checkout overview.
        
        Expected Result:
        - Returns to inventory page
        """
        inventory_page = logged_in_user
        
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        overview_page = checkout_page.complete_checkout_info("John", "Doe", "12345")
        
        # Cancel
        inventory_page = overview_page.click_cancel()
        
        assert inventory_page.is_inventory_page_displayed(), \
            "Should return to inventory"
    
    # =========================================================================
    # POST-CHECKOUT TESTS
    # =========================================================================
    
    @pytest.mark.checkout
    def test_back_home_after_checkout(self, logged_in_user):
        """
        TC-030: Verify Back Home button after checkout.
        
        Expected Result:
        - Returns to inventory page
        - Cart is empty
        """
        inventory_page = logged_in_user
        
        # Complete checkout
        inventory_page.add_backpack_to_cart()
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        overview_page = checkout_page.complete_checkout_info("John", "Doe", "12345")
        complete_page = overview_page.click_finish()
        
        # Go back home
        inventory_page = complete_page.click_back_home()
        
        assert inventory_page.is_inventory_page_displayed(), \
            "Should return to inventory"
        assert inventory_page.get_cart_count() == 0, \
            "Cart should be empty after order"


# Run tests:
# pytest test_checkout.py -v
# pytest test_checkout.py -v -m smoke
