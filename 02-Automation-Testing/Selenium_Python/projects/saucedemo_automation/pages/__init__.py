"""
Pages Package
=============
Page Object Model implementation for Sauce Demo.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

from .base_page import BasePage
from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage, CheckoutOverviewPage, CheckoutCompletePage

__all__ = [
    'BasePage',
    'LoginPage',
    'InventoryPage',
    'CartPage',
    'CheckoutPage',
    'CheckoutOverviewPage',
    'CheckoutCompletePage'
]
