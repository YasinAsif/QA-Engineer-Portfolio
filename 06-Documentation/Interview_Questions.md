# 🎤 QA Interview Preparation Guide

Common QA interview questions with detailed answers.

---

## 📋 Table of Contents

1. [Manual Testing Questions](#manual-testing-questions)
2. [Automation Testing Questions](#automation-testing-questions)
3. [API Testing Questions](#api-testing-questions)
4. [Selenium Questions](#selenium-questions)
5. [Behavioral Questions](#behavioral-questions)

---

## Manual Testing Questions

### Q1: What is the difference between Severity and Priority?

**Answer:**
| Aspect | Severity | Priority |
|--------|----------|----------|
| Definition | Technical impact on system | Business importance |
| Set by | QA/Tester | Product Manager/Business |
| Focuses on | How bad is the bug | How urgent to fix |

**Example:**
- **High Severity, Low Priority:** Crash on rarely used feature
- **Low Severity, High Priority:** CEO's name misspelled on homepage

---

### Q2: Explain the Software Testing Life Cycle (STLC)

**Answer:**
1. **Requirement Analysis** - Understand what to test
2. **Test Planning** - Define strategy and resources
3. **Test Case Development** - Write test cases
4. **Environment Setup** - Prepare test environment
5. **Test Execution** - Run tests and log results
6. **Test Cycle Closure** - Reports and metrics

---

### Q3: What is the difference between Verification and Validation?

**Answer:**
| Verification | Validation |
|--------------|------------|
| "Are we building the product right?" | "Are we building the right product?" |
| Process-oriented | Product-oriented |
| Reviews, inspections | Testing, demos |
| Done before validation | Done after verification |

---

### Q4: What are the different types of testing?

**Answer:**
- **Functional:** Unit, Integration, System, Acceptance
- **Non-Functional:** Performance, Security, Usability
- **Maintenance:** Regression, Smoke, Sanity

---

### Q5: How do you write a good bug report?

**Answer:**
A good bug report includes:
1. **Bug ID** - Unique identifier
2. **Title** - Clear, concise summary
3. **Severity/Priority** - Impact classification
4. **Steps to Reproduce** - Detailed steps
5. **Expected Result** - What should happen
6. **Actual Result** - What actually happened
7. **Environment** - Browser, OS, version
8. **Screenshots/Videos** - Visual evidence

---

## Automation Testing Questions

### Q6: What is Page Object Model (POM)?

**Answer:**
Page Object Model is a design pattern where:
- Each web page is represented as a class
- Page elements are defined as class variables
- Page actions are defined as class methods

**Benefits:**
- ✅ Code reusability
- ✅ Easy maintenance
- ✅ Reduced code duplication
- ✅ Better readability

```python
class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
```

---

### Q7: What are the advantages of automation testing?

**Answer:**
1. **Speed** - Runs faster than manual
2. **Repeatability** - Consistent execution
3. **Coverage** - More tests in less time
4. **Regression** - Easy to rerun all tests
5. **CI/CD** - Integrate with pipelines
6. **Cost** - Long-term cost savings

---

### Q8: When should you NOT automate?

**Answer:**
- ❌ Exploratory testing
- ❌ One-time tests
- ❌ Frequently changing features
- ❌ Usability testing
- ❌ Ad-hoc testing
- ❌ When ROI is negative

---

## Selenium Questions

### Q9: What are the different locator strategies in Selenium?

**Answer:**
| Locator | Example | When to Use |
|---------|---------|-------------|
| ID | `By.ID, "username"` | Unique IDs (preferred) |
| Name | `By.NAME, "email"` | Form elements |
| Class Name | `By.CLASS_NAME, "btn"` | Styled elements |
| CSS Selector | `By.CSS_SELECTOR, "#login"` | Complex selections |
| XPath | `By.XPATH, "//div[@id='x']"` | Complex DOM navigation |
| Link Text | `By.LINK_TEXT, "Click"` | Link elements |

**Priority:** ID > Name > CSS > XPath

---

### Q10: What is the difference between implicit and explicit wait?

**Answer:**
| Implicit Wait | Explicit Wait |
|---------------|---------------|
| Global setting | Specific condition |
| Applies to all elements | Applies to one element |
| Fixed wait time | Waits until condition met |
| `driver.implicitly_wait(10)` | `WebDriverWait(driver, 10)` |

**Best Practice:** Use explicit waits for reliability.

```python
# Explicit wait example
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "element")))
```

---

### Q11: How do you handle dropdowns in Selenium?

**Answer:**
```python
from selenium.webdriver.support.select import Select

dropdown = Select(driver.find_element(By.ID, "dropdown"))

# Select by visible text
dropdown.select_by_visible_text("Option 1")

# Select by value
dropdown.select_by_value("opt1")

# Select by index
dropdown.select_by_index(0)
```

---

### Q12: How do you handle alerts in Selenium?

**Answer:**
```python
# Switch to alert
alert = driver.switch_to.alert

# Get alert text
text = alert.text

# Accept alert (OK)
alert.accept()

# Dismiss alert (Cancel)
alert.dismiss()

# Send text to prompt
alert.send_keys("input text")
```

---

## API Testing Questions

### Q13: What are HTTP status codes?

**Answer:**
| Code | Category | Example |
|------|----------|---------|
| 1xx | Informational | 100 Continue |
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved, 304 Not Modified |
| 4xx | Client Error | 400 Bad Request, 404 Not Found |
| 5xx | Server Error | 500 Internal Server Error |

---

### Q14: What is the difference between PUT and PATCH?

**Answer:**
| PUT | PATCH |
|-----|-------|
| Full update | Partial update |
| Replaces entire resource | Updates specific fields |
| Idempotent | May not be idempotent |

```json
// PUT - Send complete object
{ "name": "John", "email": "john@example.com", "age": 30 }

// PATCH - Send only changed field
{ "email": "newemail@example.com" }
```

---

### Q15: What would you verify in API testing?

**Answer:**
1. **Status Code** - Correct response code
2. **Response Body** - Correct data
3. **Headers** - Content-Type, Auth
4. **Response Time** - Within limits
5. **Error Handling** - Proper error messages
6. **Schema Validation** - JSON structure
7. **Authentication** - Token handling
8. **Edge Cases** - Empty data, large payloads

---

## Behavioral Questions

### Q16: Tell me about yourself

**Answer Template:**
"I'm a passionate QA professional with experience in both manual and automation testing. I've built a comprehensive QA portfolio that demonstrates my skills in:
- Writing professional test cases and bug reports
- Selenium automation with Page Object Model
- API testing with Postman and Python
- CI/CD with GitHub Actions

I'm particularly excited about automation testing and always looking to learn new technologies. I built my portfolio from scratch, which shows my dedication and self-learning ability."

---

### Q17: Describe a bug you found that you're proud of

**Answer Framework:**
1. **Context** - What were you testing?
2. **Discovery** - How did you find it?
3. **Impact** - Why was it important?
4. **Resolution** - What happened after reporting?

---

### Q18: How do you prioritize your testing when time is limited?

**Answer:**
1. **Risk-based testing** - Focus on high-risk areas
2. **Critical paths** - Test main user journeys
3. **Smoke testing** - Verify basic functionality
4. **Regression on changed areas** - Focus near changes
5. **Communication** - Discuss with PM about priorities

---

### Q19: How do you stay updated with QA trends?

**Answer:**
- Reading blogs (Ministry of Testing, Test Automation University)
- Following QA influencers on LinkedIn
- Joining communities (Reddit r/QualityAssurance)
- Taking online courses
- Building personal projects
- Attending webinars

---

### Q20: Why should we hire you?

**Answer Template:**
"I bring a combination of:
1. **Strong foundation** - Solid understanding of testing principles
2. **Practical skills** - Hands-on automation experience
3. **Portfolio proof** - GitHub portfolio demonstrates my work
4. **Learning mindset** - Continuously improving
5. **Passion** - Genuinely interested in quality

My portfolio shows I can deliver - it has 30+ automated tests, API testing, and CI/CD integration. I'm ready to contribute from day one while continuing to grow."

---

## 🎯 Interview Tips

1. **Prepare examples** - Use STAR method
2. **Know your portfolio** - Be ready to explain each project
3. **Ask questions** - Show interest in the company
4. **Be honest** - Don't pretend to know something
5. **Practice coding** - Be ready for live coding
6. **Review basics** - SDLC, STLC, testing types

---

## 📚 Additional Resources

- [ISTQB Glossary](https://glossary.istqb.org/)
- [Ministry of Testing](https://www.ministryoftesting.com/)
- [Test Automation University](https://testautomationu.applitools.com/)

---

*Good luck with your interviews! 🍀*

*Part of QA Engineer Portfolio*
