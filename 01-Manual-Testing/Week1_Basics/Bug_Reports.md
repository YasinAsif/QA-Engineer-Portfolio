# 🐛 Bug Reports - Sauce Demo Testing

**Project:** Sauce Demo E-commerce Application  
**Website:** https://www.saucedemo.com  
**Tested By:** Yasin Asif  
**Test Date:** October 2025  
**Browser:** Chrome (Latest Version)  

---

## 📊 Bug Summary

| Bug ID | Title | Severity | Priority | Status |
|--------|-------|----------|----------|--------|
| BUG-001 | Problem User Shows Incorrect Product Images | High | High | Open |
| BUG-002 | Performance Glitch User Has Significant Login Delay | Medium | Medium | Open |
| BUG-003 | Twitter Social Media Link Broken | Low | Low | Open |
| BUG-004 | Cart Badge Not Updated After Removing Last Item | Medium | High | Open |
| BUG-005 | Product Sorting Inconsistent with Problem User | Medium | Medium | Open |

---

## BUG-001: Problem User Shows Incorrect Product Images

**Severity:** High  
**Priority:** High  
**Status:** Open  
**Module:** Inventory Page  

### Description
When logged in as `problem_user`, all product images display the same incorrect image (a dog with goggles) instead of showing unique product images.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Login with credentials:
   - Username: `problem_user`
   - Password: `secret_sauce`
3. Click "Login" button
4. Observe product images on inventory page

### Expected Result
- Each product should display its unique, correct product image
- Sauce Labs Backpack should show a backpack image
- Sauce Labs Bike Light should show a bike light image
- And so on for all products

### Actual Result
- All 6 products display the same image: `/static/media/sl-404.168b1cce.jpg`
- Image shows a dog wearing goggles/googles
- No product shows its correct image

### Test Data
- **Username:** problem_user
- **Password:** secret_sauce

### Environment
- **URL:** https://www.saucedemo.com
- **Browser:** Chrome 118+
- **OS:** Windows 10/11
- **Screen Resolution:** 1920x1080

### Impact
- **User Experience:** Users cannot visually identify products
- **Business Impact:** May lead to wrong product selection and returns
- **Affected Users:** All users logged in as problem_user

### Attachments
📸 Screenshot needed: `BUG-001-incorrect-images.png`

### Notes
This appears to be intentional for testing purposes, as the username is `problem_user`. However, it represents a significant UI defect that would be critical in production.

---

## BUG-002: Performance Glitch User Has Significant Login Delay

**Severity:** Medium  
**Priority:** Medium  
**Status:** Open  
**Module:** Login Page  

### Description
When logging in with `performance_glitch_user` credentials, there is an unusually long delay (5-10 seconds) before the inventory page loads.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Enter credentials:
   - Username: `performance_glitch_user`
   - Password: `secret_sauce`
3. Click "Login" button
4. Observe loading time

### Expected Result
- Login should complete within 1-2 seconds (standard loading time)
- User should be redirected to inventory page promptly

### Actual Result
- Login takes approximately 5-10 seconds to complete
- Screen appears frozen during this time
- No loading indicator is shown to user
- Eventually redirects to inventory page successfully

### Test Data
- **Username:** performance_glitch_user
- **Password:** secret_sauce

### Environment
- **URL:** https://www.saucedemo.com
- **Browser:** Chrome 118+
- **OS:** Windows 10/11
- **Network:** High-speed internet connection

### Impact
- **User Experience:** Poor - users may think application crashed
- **Business Impact:** Users may abandon login process
- **Affected Users:** All users with performance_glitch_user account

### Attachments
📹 Video/GIF needed: `BUG-002-login-delay.gif`

### Notes
- Delay is consistent across multiple login attempts
- No loading spinner or progress indicator shown
- Other users (standard_user) login instantly

---

## BUG-003: Twitter Social Media Link Broken

**Severity:** Low  
**Priority:** Low  
**Status:** Open  
**Module:** Footer - Social Media Links  

### Description
The Twitter social media icon in the footer links to a non-existent or broken Twitter profile page, resulting in a "Profile doesn't exist" error.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Login with any valid credentials (e.g., standard_user/secret_sauce)
3. Scroll to the bottom of the page
4. Click on the Twitter icon in the footer

### Expected Result
- Should navigate to Sauce Labs' official Twitter profile
- Profile should load successfully
- OR link should be removed if company doesn't have Twitter presence

### Actual Result
- Redirects to Twitter/X
- Shows error: "This account doesn't exist" or similar
- User encounters a dead link

### Test Data
- **Username:** standard_user (or any valid user)
- **Password:** secret_sauce

### Environment
- **URL:** https://www.saucedemo.com
- **Browser:** Chrome 118+
- **OS:** Windows 10/11

### Impact
- **User Experience:** Unprofessional - suggests poor maintenance
- **Business Impact:** Lost opportunity for social media engagement
- **Affected Users:** All logged-in users

### Attachments
📸 Screenshot needed: `BUG-003-twitter-broken.png`

### Notes
- Facebook and LinkedIn links may need verification too
- Common issue when company changes social media handles

---

## BUG-004: Cart Badge Not Updated After Removing Last Item

**Severity:** Medium  
**Priority:** High  
**Status:** Open  
**Module:** Shopping Cart  

### Description
When removing the last item from the shopping cart, the cart badge counter does not update immediately. It continues to show "1" even though cart is empty.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Login with standard_user/secret_sauce
3. Add one product to cart (cart badge shows "1")
4. Click on cart icon to view cart
5. Click "Remove" button to remove the item
6. Observe cart badge in top-right corner

### Expected Result
- Cart badge should disappear completely when cart is empty
- Badge should show no number when count is 0
- Cart page should show "Your cart is empty" or similar message

### Actual Result
- Cart badge may still show "1" for a moment
- Badge behavior is inconsistent
- Requires page refresh to properly update

### Test Data
- **Username:** standard_user
- **Password:** secret_sauce
- **Product:** Any product (e.g., Sauce Labs Backpack)

### Environment
- **URL:** https://www.saucedemo.com
- **Browser:** Chrome 118+
- **OS:** Windows 10/11

### Impact
- **User Experience:** Confusing - users think item still in cart
- **Business Impact:** May cause users to re-check cart unnecessarily
- **Affected Users:** All users removing items from cart

### Attachments
📸 Screenshot needed: `BUG-004-cart-badge-not-updated.png`

### Notes
- May be a JavaScript state management issue
- Test with multiple items (add 3, remove all one-by-one)

---

## BUG-005: Product Sorting Inconsistent with Problem User

**Severity:** Medium  
**Priority:** Medium  
**Status:** Open  
**Module:** Inventory - Product Sorting  

### Description
When logged in as `problem_user`, product sorting functionality appears inconsistent or broken. Products don't sort correctly when "Price (low to high)" option is selected.

### Steps to Reproduce
1. Navigate to https://www.saucedemo.com
2. Login with problem_user/secret_sauce
3. Locate the product sort dropdown (top-right of inventory)
4. Select "Price (low to high)" from dropdown
5. Observe product order

### Expected Result
- Products should be sorted by price in ascending order
- Lowest priced item should appear first
- Highest priced item should appear last

### Actual Result
- Product order doesn't change, OR
- Products sort incorrectly
- Order appears random or doesn't match selected sort option

### Test Data
- **Username:** problem_user
- **Password:** secret_sauce
- **Sort Options Tested:** Price (low to high), Price (high to low)

### Environment
- **URL:** https://www.saucedemo.com
- **Browser:** Chrome 118+
- **OS:** Windows 10/11

### Impact
- **User Experience:** Frustrating - can't find products by price
- **Business Impact:** Users may miss affordable options
- **Affected Users:** Users logged in as problem_user

### Attachments
📸 Screenshots needed: 
- `BUG-005-before-sort.png`
- `BUG-005-after-sort.png`

### Notes
- Test all sort options: Name (A-Z), Name (Z-A), Price (low-high), Price (high-low)
- Compare behavior with standard_user account
- May be related to the same underlying issue causing image problems

---

## 📋 Testing Notes

### Test Coverage
- **Total Test Cases Executed:** 20
- **Test Cases Passed:** 15
- **Test Cases Failed:** 5
- **Pass Rate:** 75%

### User Accounts Tested
✅ **standard_user** - Most functionality works correctly  
⚠️ **problem_user** - Multiple UI/functionality issues (BUG-001, BUG-005)  
⚠️ **performance_glitch_user** - Performance issues (BUG-002)  
❌ **locked_out_user** - Cannot login (Expected behavior)  

### Recommendations
1. **Immediate Fix Required:**
   - BUG-004 (Cart badge) - Affects all users
   - BUG-001 (Images) - If problem_user is for demo purposes, document it

2. **Short-term Fix:**
   - BUG-002 (Performance) - Add loading indicator at minimum
   - BUG-005 (Sorting) - Fix or document as known issue

3. **Low Priority:**
   - BUG-003 (Social media) - Update or remove broken links

### Tools Used
- **Browser:** Google Chrome DevTools
- **Documentation:** Manual testing with Excel test cases
- **Screenshots:** Windows Snipping Tool / Greenshot

---

## 📸 Screenshot Instructions

To capture evidence for these bugs:

1. **BUG-001:** Take screenshot of inventory page with problem_user showing identical images
2. **BUG-002:** Record GIF of login delay using LICEcap or ScreenToGif
3. **BUG-003:** Screenshot of Twitter error page
4. **BUG-004:** Screenshot showing cart badge with "1" when cart is empty
5. **BUG-005:** Before/after screenshots of sorting attempt

### Folder Structure for Screenshots
```
Bug-Reports/
├── screenshots/
│   ├── BUG-001-incorrect-images.png
│   ├── BUG-002-login-delay.gif
│   ├── BUG-003-twitter-broken.png
│   ├── BUG-004-cart-badge-not-updated.png
│   ├── BUG-005-before-sort.png
│   └── BUG-005-after-sort.png
```

---

## 🔄 Bug Report Template (For Future Use)

```markdown
## BUG-XXX: [Brief Bug Title]

**Severity:** [Critical/High/Medium/Low]
**Priority:** [High/Medium/Low]
**Status:** [Open/In Progress/Fixed/Closed]
**Module:** [Module Name]

### Description
[Clear description of the issue]

### Steps to Reproduce
1. Step one
2. Step two
3. Step three

### Expected Result
[What should happen]

### Actual Result
[What actually happens]

### Test Data
- **Username:** 
- **Password:** 
- **Other data:** 

### Environment
- **URL:** 
- **Browser:** 
- **OS:** 

### Impact
- **User Experience:** 
- **Business Impact:** 
- **Affected Users:** 

### Attachments
📸 Screenshot/Video needed

### Notes
[Additional observations]
```

---

**Last Updated:** October 2025  
