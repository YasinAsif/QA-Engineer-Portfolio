# SDLC & STLC Study Notes - Week 1

## 📚 Software Development Life Cycle (SDLC)

### Definition
SDLC is a systematic process for building software through multiple phases from planning to deployment and maintenance.

### SDLC Models

#### 1. Waterfall Model
```
Requirements → Design → Development → Testing → Deployment → Maintenance
```
**When to use:** Projects with clear, unchanging requirements

**Pros:**
- Simple and easy to understand
- Clear phases and milestones
- Good documentation

**Cons:**
- No going back to previous phase
- Testing happens late
- Not suitable for complex projects

---

#### 2. Agile Model
```
Plan → Design → Develop → Test → Review → Deploy
              ↑________________________↓
                  (Iterative Sprints)
```

**When to use:** Projects with changing requirements

**Pros:**
- Flexible to changes
- Continuous testing
- Faster delivery

**Cons:**
- Less predictable
- Requires active customer involvement

---

#### 3. V-Model (Verification & Validation)
```
Requirements ←→ Acceptance Testing
Design ←→ System Testing
Architecture ←→ Integration Testing
Module Design ←→ Unit Testing
         ↓
      Coding
```

**When to use:** Projects where testing is critical

**Key Point:** Testing is planned in parallel with development!

---

## 🧪 Software Testing Life Cycle (STLC)

### Definition
STLC is a sequence of specific activities conducted during the testing process to ensure software quality.

### STLC Phases

#### Phase 1: Requirement Analysis
**QA Activities:**
- Review requirements documents
- Identify testable requirements
- Clarify doubts with stakeholders
- Create Requirement Traceability Matrix (RTM)

**Deliverable:** RTM, List of testable requirements

**Example:**
```
Requirement: "User should be able to login"
Testable aspects:
- Valid credentials
- Invalid credentials
- Empty fields
- Session timeout
```

---

#### Phase 2: Test Planning
**QA Activities:**
- Define test strategy
- Estimate effort and cost
- Select tools
- Define entry/exit criteria
- Assign roles

**Deliverable:** Test Plan document

**Entry Criteria:**
- Requirements are finalized
- Test environment is ready

**Exit Criteria:**
- All test cases executed
- 95%+ pass rate achieved
- All critical bugs fixed

---

#### Phase 3: Test Case Development
**QA Activities:**
- Write detailed test cases
- Create test data
- Review test cases
- Get approval

**Deliverable:** Test cases, Test data, Test scripts

**Test Case Example:**
```
ID: TC-001
Title: Verify login with valid credentials
Precondition: User has active account
Steps:
  1. Go to login page
  2. Enter username
  3. Enter password
  4. Click Login
Expected: User sees dashboard
Priority: High
```

---

#### Phase 4: Test Environment Setup
**QA Activities:**
- Set up test server
- Configure test data
- Install necessary tools
- Perform smoke test on environment

**Deliverable:** Ready test environment

**Checklist:**
- [ ] Server configured
- [ ] Database populated
- [ ] Test users created
- [ ] Browsers installed
- [ ] Tools configured

---

#### Phase 5: Test Execution
**QA Activities:**
- Execute test cases
- Log defects
- Retest fixed bugs
- Update test results

**Deliverable:** Test execution report, Bug reports

**Process:**
```
Execute Test Case
       ↓
   Pass or Fail?
       ↓
   If Fail → Log Bug → Track → Retest → Update Status
       ↓
   If Pass → Mark as Passed
```

---

#### Phase 6: Test Cycle Closure
**QA Activities:**
- Analyze test results
- Document learnings
- Archive test artifacts
- Prepare summary report

**Deliverable:** Test summary report, Lessons learned

**Metrics to Report:**
- Total test cases: X
- Executed: Y
- Passed: Z
- Failed: A
- Blocked: B
- Pass percentage: Z/Y * 100

---

## 🔍 Testing Types

### 1. Functional Testing

#### a) Unit Testing
- **Who:** Developers
- **What:** Individual components
- **When:** During development
- **Example:** Testing a login function in isolation

#### b) Integration Testing
- **Who:** Developers + QA
- **What:** Combined components
- **When:** After unit testing
- **Example:** Testing login + profile update together

#### c) System Testing
- **Who:** QA Team
- **What:** Complete system
- **When:** After integration
- **Example:** Testing entire e-commerce flow

#### d) Acceptance Testing (UAT)
- **Who:** End users / Client
- **What:** Business requirements
- **When:** Before release
- **Example:** Client validates features

---

### 2. Non-Functional Testing

#### a) Performance Testing
**Checks:** Speed, scalability, stability

**Types:**
- Load Testing: Normal load
- Stress Testing: Beyond capacity
- Spike Testing: Sudden traffic increase

#### b) Security Testing
**Checks:** Vulnerabilities, data protection

**Tests:**
- SQL Injection
- Cross-Site Scripting (XSS)
- Authentication bypass

#### c) Usability Testing
**Checks:** User-friendliness

**Aspects:**
- Navigation ease
- Visual appeal
- Error messages clarity

---

## 🐛 Bug Lifecycle

```
1. New (Bug reported by tester)
       ↓
2. Assigned (to developer)
       ↓
3. Open (Developer working on it)
       ↓
4. Fixed (Developer claims fix)
       ↓
5. Ready for Retest
       ↓
6. Retest (Tester verifies)
       ↓
   Pass → Closed
   Fail → Reopen (back to step 3)
```

**Alternative Paths:**
- **Rejected:** Not a bug
- **Deferred:** Fix in future release
- **Duplicate:** Already reported

---

## 🎯 Test Case Design Techniques

### 1. Equivalence Partitioning
**Concept:** Divide input into groups that behave similarly

**Example:** Age field (0-120)
- Invalid: -5, -1 (negative)
- Valid: 0-120
- Invalid: 121, 200 (too high)

**Test Cases:** Pick one value from each partition
- TC1: Age = -1 (should fail)
- TC2: Age = 25 (should pass)
- TC3: Age = 150 (should fail)

---

### 2. Boundary Value Analysis
**Concept:** Test at boundaries of input ranges

**Example:** Age field (18-65 for job application)

**Test Cases:**
- Just below: 17 ❌
- Minimum: 18 ✅
- Middle: 40 ✅
- Maximum: 65 ✅
- Just above: 66 ❌

---

### 3. Decision Table Testing
**Concept:** Test different combinations of inputs

**Example:** Login with Remember Me

| Username | Password | Remember Me | Result |
|----------|----------|-------------|--------|
| Valid | Valid | Yes | Login + Remember |
| Valid | Valid | No | Login only |
| Valid | Invalid | Yes | Fail |
| Invalid | Valid | Yes | Fail |

---

## 📊 Severity vs Priority

### Severity (Technical Impact)
**Critical:** System crash, data loss
**High:** Major feature broken
**Medium:** Feature works with workaround
**Low:** Cosmetic issue

### Priority (Business Urgency)
**P0/Immediate:** Fix now (production down)
**P1/High:** Fix in current sprint
**P2/Medium:** Fix in next release
**P3/Low:** Fix when time permits

### Real Example:
**Bug:** Company logo misspelled on homepage

- **Severity:** Low (no functional impact)
- **Priority:** High (brand reputation)

---

## 💡 Key Learnings

1. **Testing starts early** - Not just at the end
2. **Prevention > Detection** - Find bugs in requirements phase
3. **Document everything** - Test cases, bugs, results
4. **Severity ≠ Priority** - Business context matters
5. **Exploratory testing matters** - Don't just follow scripts

---

## 🎓 Glossary

**Test Case:** Step-by-step instructions to verify functionality  
**Test Suite:** Collection of test cases  
**Test Scenario:** High-level testing approach  
**Test Plan:** Document describing testing strategy  
**RTM:** Requirement Traceability Matrix - links requirements to test cases  
**Smoke Test:** Basic sanity check if build is testable  
**Sanity Test:** Focused test on specific functionality after bug fix  
**Regression Test:** Re-running tests to ensure new changes didn't break existing features  

---

*Notes compiled during Week 1 of QA learning journey*  
*Date: October 7,2025*


