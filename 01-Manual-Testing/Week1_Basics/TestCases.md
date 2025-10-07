# QA Portfolio: Sauce Demo Manual Test Report
**Tester:** Muhammad Yasin Asif  
**Role:** QA Engineer (In Training)  
**Part of:** Week 1 – Manual Testing Portfolio  
**Date:** October 08, 2025

## Project Overview

This report outlines the manual testing conducted on the Sauce Demo e-commerce application, which serves as a demo platform for practicing web application testing. The scope includes core functionalities across login, product browsing, shopping cart, and checkout modules. Testing was performed using Google Chrome on Windows 11 to ensure consistent results.

| Field | Details |
|-------|---------|
| **Application URL** | https://www.saucedemo.com/ |
| **Test Environment** | Staging (Demo Site) |
| **Browser** | Google Chrome Version 129.0 |
| **Operating System** | Windows 11 |
| **Test Type** | Manual Functional Testing |
| **Total Test Cases** | 20 |
| **Passed** | 18 |
| **Failed** | 2 |
| **Blocked** | 0 |

## Test Credentials

| Username | Password | Description |
|----------|----------|-------------|
| standard_user | secret_sauce | Valid standard user account |
| locked_out_user | secret_sauce | Locked out user account |
| problem_user | secret_sauce | User with UI issues |
| performance_glitch_user | secret_sauce | User with performance delays |
| error_user | secret_sauce | User triggering errors |
| visual_user | secret_sauce | User for visual testing |

---

## Login Module

### TC-001: Verify Login with Valid Standard User Credentials

| Field | Details |
|-------|---------|
| **Test ID** | TC-001 |
| **Module** | Login |
| **Priority** | High |
| **Preconditions** | User is on the login page with a stable internet connection. |

#### Test Steps
1. Navigate to https://www.saucedemo.com/.
2. Enter username: standard_user.
3. Enter password: secret_sauce.
4. Click the Login button.

#### Expected Result
- User should be redirected to the Products page.
- Inventory container should be visible with product listings.

#### Actual Result
```
✅ Successfully logged in.
✅ Redirected to Products page.
✅ Inventory displayed with 6 products.
```

**Status:** PASS  
**Notes:** Login functionality verified without issues. Test executed successfully.

### TC-002: Verify Login with Locked Out User Credentials

| Field | Details |
|-------|---------|
| **Test ID** | TC-002 |
| **Module** | Login |
| **Priority** | High |
| **Preconditions** | User is on the login page. |

#### Test Steps
1. Navigate to https://www.saucedemo.com/.
2. Enter username: locked_out_user.
3. Enter password: secret_sauce.
4. Click the Login button.

#### Expected Result
- Error message: "Epic sadface: Sorry, this user has been locked out." should display.
- User remains on the login page.

#### Actual Result
```
✅ Error message displayed as expected.
✅ Remained on login page.
```

**Status:** PASS  
**Notes:** Locked out behavior confirmed. All validation checks passed.

### TC-003: Verify Login with Invalid Username

| Field | Details |
|-------|---------|
| **Test ID** | TC-003 |
| **Module** | Login |
| **Priority** | Medium |
| **Preconditions** | User is on the login page. |

#### Test Steps
1. Navigate to https://www.saucedemo.com/.
2. Enter invalid username: invalid_user.
3. Enter password: secret_sauce.
4. Click the Login button.

#### Expected Result
- Error message: "Epic sadface: Username and password do not match any user in this service" should display.

#### Actual Result
```
✅ Error message displayed correctly.
```

**Status:** PASS  
**Notes:** Invalid credential handling works as intended.

### TC-004: Verify Login with Invalid Password

| Field | Details |
|-------|---------|
| **Test ID** | TC-004 |
| **Module** | Login |
| **Priority** | Medium |
| **Preconditions** | User is on the login page. |

#### Test Steps
1. Navigate to https://www.saucedemo.com/.
2. Enter username: standard_user.
3. Enter invalid password: wrong_pass.
4. Click the Login button.

#### Expected Result
- Error message: "Epic sadface: Username and password do not match any user in this service" should display.

#### Actual Result
```
✅ Error message shown.
```

**Status:** PASS  
**Notes:** No issues observed.

### TC-005: Verify Login with Empty Credentials

| Field | Details |
|-------|---------|
| **Test ID** | TC-005 |
| **Module** | Login |
| **Priority** | Medium |
| **Preconditions** | User is on the login page. |

#### Test Steps
1. Navigate to https://www.saucedemo.com/.
2. Leave username and password fields empty.
3. Click the Login button.

#### Expected Result
- Error message: "Epic sadface: Username is required" should display.

#### Actual Result
```
✅ Username required error displayed.
```

**Status:** PASS  
**Notes:** Field validation is effective.

---

## Product Browsing Module

### TC-006: Verify Product Sorting by Name (A to Z)

| Field | Details |
|-------|---------|
| **Test ID** | TC-006 |
| **Module** | Product Browsing |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. On the Products page, select "Name (A to Z)" from the sort dropdown.

#### Expected Result
- Products should be sorted alphabetically from A to Z.

#### Actual Result
```
✅ Products sorted: Sauce Labs Backpack first, then Bike Light, etc.
```

**Status:** PASS  
**Notes:** Sorting functionality confirmed.

### TC-007: Verify Product Sorting by Name (Z to A)

| Field | Details |
|-------|---------|
| **Test ID** | TC-007 |
| **Module** | Product Browsing |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. Select "Name (Z to A)" from the sort dropdown.

#### Expected Result
- Products sorted alphabetically from Z to A.

#### Actual Result
```
✅ Products sorted: Test.allTheThings() T-Shirt first, then Onesie, etc.
```

**Status:** PASS  
**Notes:** Reverse sorting works fine.

### TC-008: Verify Product Sorting by Price (Low to High)

| Field | Details |
|-------|---------|
| **Test ID** | TC-008 |
| **Module** | Product Browsing |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. Select "Price (low to high)" from the sort dropdown.

#### Expected Result
- Products sorted by price ascending.

#### Actual Result
```
✅ Products sorted: Sauce Labs Onesie ($7.99) first, then Bike Light ($9.99), etc.
```

**Status:** PASS  
**Notes:** Price sorting ascending verified.

### TC-009: Verify Product Sorting by Price (High to Low)

| Field | Details |
|-------|---------|
| **Test ID** | TC-009 |
| **Module** | Product Browsing |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. Select "Price (high to low)" from the sort dropdown.

#### Expected Result
- Products sorted by price descending.

#### Actual Result
```
✅ Products sorted: Sauce Labs Fleece Jacket ($49.99) first, then Backpack ($29.99), etc.
```

**Status:** PASS  
**Notes:** Price sorting descending confirmed.

### TC-010: Verify Viewing Product Details

| Field | Details |
|-------|---------|
| **Test ID** | TC-010 |
| **Module** | Product Browsing |
| **Priority** | High |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. Click on a product name or image (e.g., Sauce Labs Backpack).

#### Expected Result
- Redirect to product details page with image, description, price, and Add to Cart button.

#### Actual Result
```
✅ Redirected to details page.
✅ All elements displayed: image, name, description, price ($29.99), button.
```

**Status:** PASS  
**Notes:** Product details page loads correctly.

---

## Shopping Cart Module

### TC-011: Verify Adding Item to Cart from Products Page

| Field | Details |
|-------|---------|
| **Test ID** | TC-011 |
| **Module** | Shopping Cart |
| **Priority** | High |
| **Preconditions** | User is logged in as standard_user and on the Products page. |

#### Test Steps
1. Login as standard_user.
2. Click "Add to cart" on Sauce Labs Backpack.
3. Check cart badge.

#### Expected Result
- Button changes to "Remove".
- Cart badge shows "1".

#### Actual Result
```
✅ Button updated to Remove.
✅ Cart badge displays 1.
```

**Status:** PASS  
**Notes:** Item added successfully.

### TC-012: Verify Adding Item to Cart from Details Page

| Field | Details |
|-------|---------|
| **Test ID** | TC-012 |
| **Module** | Shopping Cart |
| **Priority** | High |
| **Preconditions** | User is logged in as problem_user and on the product details page. |

#### Test Steps
1. Login as problem_user.
2. Navigate to Sauce Labs Bike Light details.
3. Click "Add to cart".

#### Expected Result
- Button changes to "Remove".
- Cart badge updates.

#### Actual Result
```
❌ Button did not change to Remove (UI glitch observed).
❌ Cart badge not updated.
```

**Status:** FAIL  
**Notes:** UI issue with problem_user; item not added properly.

### TC-013: Verify Removing Item from Cart

| Field | Details |
|-------|---------|
| **Test ID** | TC-013 |
| **Module** | Shopping Cart |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user with an item in the cart. |

#### Test Steps
1. Login as standard_user.
2. Add an item to cart.
3. Click "Remove" on the item.

#### Expected Result
- Button changes back to "Add to cart".
- Cart badge disappears or updates to 0.

#### Actual Result
```
✅ Button updated to Add to cart.
✅ Cart badge removed.
```

**Status:** PASS  
**Notes:** Removal works as expected.

### TC-014: Verify Continue Shopping from Cart Page

| Field | Details |
|-------|---------|
| **Test ID** | TC-014 |
| **Module** | Shopping Cart |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user and on the Cart page. |

#### Test Steps
1. Login as standard_user.
2. Add item to cart.
3. Go to Cart page.
4. Click "Continue Shopping".

#### Expected Result
- Redirect back to Products page.

#### Actual Result
```
✅ Redirected to Products page.
✅ Inventory visible.
```

**Status:** PASS  
**Notes:** Navigation confirmed.

### TC-015: Verify Cart Contents Persistence

| Field | Details |
|-------|---------|
| **Test ID** | TC-015 |
| **Module** | Shopping Cart |
| **Priority** | Medium |
| **Preconditions** | User is logged in as standard_user. |

#### Test Steps
1. Login as standard_user.
2. Add two items to cart.
3. Navigate to Cart page.

#### Expected Result
- Cart displays both items with names, descriptions, prices.

#### Actual Result
```
✅ Both items listed correctly.
✅ Details match products.
```

**Status:** PASS  
**Notes:** Cart persistence verified.

---

## Checkout Module

### TC-016: Verify Checkout Button from Cart

| Field | Details |
|-------|---------|
| **Test ID** | TC-016 |
| **Module** | Checkout |
| **Priority** | High |
| **Preconditions** | User is logged in as standard_user with items in the cart. |

#### Test Steps
1. Login as standard_user.
2. Add item to cart.
3. Go to Cart page.
4. Click "Checkout".

#### Expected Result
- Redirect to Checkout: Your Information page.

#### Actual Result
```
✅ Redirected to information page.
✅ Fields for first name, last name, zip code visible.
```

**Status:** PASS  
**Notes:** Checkout initiation successful.

### TC-017: Verify Entering Checkout Information

| Field | Details |
|-------|---------|
| **Test ID** | TC-017 |
| **Module** | Checkout |
| **Priority** | High |
| **Preconditions** | User is on the Checkout: Your Information page. |

#### Test Steps
1. Reach checkout info page.
2. Enter First Name: Test, Last Name: User, Zip: 12345.
3. Click "Continue".

#### Expected Result
- Redirect to Checkout: Overview page.
- No validation errors.

#### Actual Result
```
✅ Redirected to overview.
✅ Summary displayed.
```

**Status:** PASS  
**Notes:** Information submission works.

### TC-018: Verify Checkout Overview and Finish

| Field | Details |
|-------|---------|
| **Test ID** | TC-018 |
| **Module** | Checkout |
| **Priority** | High |
| **Preconditions** | User is on the Checkout: Overview page. |

#### Test Steps
1. Reach overview page.
2. Verify item total, tax, grand total.
3. Click "Finish".

#### Expected Result
- Redirect to Checkout: Complete page.
- Confirmation message: "Thank you for your order!"

#### Actual Result
```
✅ Totals correct (e.g., Item $29.99, Tax $2.40, Total $32.39).
✅ Redirected to complete page.
✅ Message displayed.
```

**Status:** PASS  
**Notes:** Purchase completion verified.

### TC-019: Verify Empty Fields Validation in Checkout

| Field | Details |
|-------|---------|
| **Test ID** | TC-019 |
| **Module** | Checkout |
| **Priority** | Medium |
| **Preconditions** | User is on the Checkout: Your Information page. |

#### Test Steps
1. Reach checkout info page.
2. Leave fields empty.
3. Click "Continue".

#### Expected Result
- Error message: "Error: First Name is required"

#### Actual Result
```
✅ Error message for first name displayed.
```

**Status:** PASS  
**Notes:** Validation effective.

### TC-020: Verify Error User Checkout Failure

| Field | Details |
|-------|---------|
| **Test ID** | TC-020 |
| **Module** | Checkout |
| **Priority** | Medium |
| **Preconditions** | User is logged in as error_user and on the overview page. |

#### Test Steps
1. Login as error_user.
2. Add item, proceed to checkout.
3. Enter info, go to overview.
4. Click "Finish".

#### Expected Result
- Error message or failure state.

#### Actual Result
```
❌ Unexpected error: "Error: Sorry, there was an error processing your request."
❌ Did not complete purchase.
```

**Status:** FAIL  
**Notes:** Error user triggers failure as intended, but message unclear.

## Test Summary

| Status | Count |
|--------|-------|
| **Passed** | 18 |
| **Failed** | 2 |
| **Total** | 20 |

All modules were tested thoroughly. The application performs well for standard users, but specific user types like problem_user and error_user expose intended defects for testing purposes.

## Bugs Reported

### Bug-001: UI Glitch When Adding to Cart as Problem User

| Field | Details |
|-------|---------|
| **Bug ID** | Bug-001 |
| **Title** | Add to Cart button does not update for problem_user |
| **Severity** | Medium |
| **Priority** | High |
| **Module** | Shopping Cart |
| **Steps to Reproduce** | 1. Login as problem_user.<br>2. Go to product details (e.g., Bike Light).<br>3. Click Add to Cart. |
| **Expected Result** | Button changes to Remove, cart updates. |
| **Actual Result** | Button remains Add to Cart, no update. |
| **Environment** | Chrome on Windows 11 |
| **Attachments** | Screenshot attached |

### Bug-002: Unclear Error Message During Checkout as Error User

| Field | Details |
|-------|---------|
| **Bug ID** | Bug-002 |
| **Title** | Vague error on Finish for error_user |
| **Severity** | Low |
| **Priority** | Medium |
| **Module** | Checkout |
| **Steps to Reproduce** | 1. Login as error_user.<br>2. Add item, proceed to checkout.<br>3. Enter info, go to overview.<br>4. Click Finish. |
| **Expected Result** | Specific error or failure. |
| **Actual Result** | Generic "Sorry, there was an error" message. |
| **Environment** | Chrome on Windows 11 |
| **Attachments** | None |

## Observations

- The application is stable for standard operations.
- Performance is good, no delays except for performance_glitch_user (as designed).
- UI is responsive, but images may load slowly on slower connections.
- Suggest adding more validation messages for clarity.

## Sign-off

This test cycle is complete. The Sauce Demo application meets basic functional requirements with noted exceptions for demo user types. Ready for further automation testing.

---
**Prepared by:** Muhammad Yasin Asif  
**Role:** QA Engineer (In Training)  
**Date:** October 08, 2025  
*Repository:* [QA-Engineer-Portfolio](https://github.com/YasinAsif/QA-Engineer-Portfolio)
