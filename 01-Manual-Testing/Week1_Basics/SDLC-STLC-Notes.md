# QA Portfolio: SDLC & STLC Study Notes - Week 1
**Author:** Muhammad Yasin Asif  
**Role:** QA Engineer (In Training)  
**Part of:** Week 1 – Manual Testing Portfolio  
**Date:** October 8, 2025

## Introduction

These notes capture my key takeaways from studying the Software Development Life Cycle (SDLC) and Software Testing Life Cycle (STLC) during my first week of QA training. I've compiled this as a quick reference guide, drawing from various resources like textbooks, online tutorials, and practical examples I've encountered. The goal is to understand how software is built and tested in a structured way, emphasizing best practices that prevent issues down the line. I've added some real-world insights from my initial explorations to make it more relatable testing isn't just theory; it's about catching problems early to save time and headaches later.

---

## Software Development Life Cycle (SDLC)

### What is SDLC?
SDLC is essentially the roadmap for creating software. It's a structured approach that guides teams from the initial idea to a fully functional product and beyond. Think of it as building a house: you don't start hammering nails without a blueprint. SDLC ensures everyone from developers to stakeholders is on the same page, reducing risks and improving quality. In my experience so far, skipping phases here can lead to costly rework, which is why models like these are crucial.

### Common SDLC Models

I've focused on three popular models here, but there are others like Spiral or Iterative. Each has its place depending on project size, team dynamics, and how much flexibility you need.

#### 1. Waterfall Model
This is the classic, linear approach where each phase flows into the next like a waterfall. No overlaps, which makes it straightforward but rigid.

```
Requirements → Design → Implementation → Verification → Deployment → Maintenance
```

**When to Use It:** Ideal for small projects with well-defined requirements that aren't likely to change, like a simple internal tool or regulatory-compliant software where documentation is key.

**Pros:**
- Easy to manage and understand, especially for beginners like me.
- Clear timelines and milestones make progress tracking simple.
- Heavy emphasis on documentation, which helps in audits or handovers.

**Cons:**
- Inflexible if requirements change mid-way, you're stuck going back, which delays everything.
- Testing comes late, so bugs found at the end can be expensive to fix.
- Not great for complex, evolving projects like modern web apps with user feedback loops.

**Real-World Example:** Developing a basic banking report generator where specs are fixed by compliance rules. I read about a case where a team used Waterfall for a government project, but scope creep turned it into a nightmare—lesson learned: assess change likelihood first.

---

#### 2. Agile Model
Agile is all about iteration and adaptability. It's like cooking a meal: taste as you go and adjust seasonings. Work happens in short "sprints" (usually 2-4 weeks), with constant feedback.

```
Plan → Design → Develop → Test → Review → Deploy
              ↑________________________↓
                  (Repeat in Sprints with Feedback)
```

**When to Use It:** Perfect for dynamic environments, like startups or apps where user needs evolve, such as e-commerce platforms or mobile games.

**Pros:**
- Highly flexible, embrace changes without derailing the project.
- Testing is integrated throughout, catching issues early.
- Faster time-to-market with incremental releases; users get value sooner.

**Cons:**
- Can feel chaotic without strong team discipline; outcomes are less predictable.
- Requires constant client involvement, which isn't always feasible.
- Documentation might be lighter, leading to knowledge gaps if team members leave.

**Real-World Example:** Think of how Spotify develops features they release MVPs (Minimum Viable Products), gather user data, and iterate. From what I've learned, Agile helped Netflix pivot quickly during streaming booms, but it demands mature teams to avoid "scope sprawl."

**Additional Insight:** Agile often uses frameworks like Scrum (with roles like Product Owner, Scrum Master) or Kanban (visual boards for workflow). In practice, hybrid models blending Agile with Waterfall are common for larger enterprises.

---

#### 3. V-Model (Verification and Validation Model)
This extends Waterfall by pairing development phases with corresponding testing phases, forming a "V" shape. It's verification (did we build it right?) on the left and validation (does it meet needs?) on the right.

```
Requirements ←→ Acceptance Testing
   Design ←→ System Testing
Architecture ←→ Integration Testing
Module Design ←→ Unit Testing
         ↓
      Coding
```

**When to Use It:** High-stakes projects where quality is non-negotiable, like medical software or aerospace systems. Testing is planned from day one.

**Pros:**
- Early defect detection since testing aligns with each dev phase.
- Strong focus on requirements traceability.
- Comprehensive documentation and structured approach.

**Cons:**
- Still somewhat rigid; changes are tough mid-process.
- Time consuming upfront planning.
- Not as adaptive as Agile for volatile requirements.

**Real-World Example:** In automotive software for safety features, V-Model ensures every design element is verified and validated. I came across a study where it reduced post-release bugs by 40% in embedded systems, but it can extend timelines.

**Key Point:** Unlike Waterfall, testing isn't an afterthought—it's parallel, which aligns well with STLC principles.

---

## Software Testing Life Cycle (STLC)

### What is STLC?
STLC is the testing specific subset of SDLC. It's a phased process to verify software meets requirements and is bug-free. From my notes, it's not just about finding errors but ensuring the product delivers value. Good STLC integrates with SDLC to shift left test early and often.

### Detailed STLC Phases

I've broken this down with more activities and examples based on what I've studied. Each phase builds on the last for thorough coverage.

#### Phase 1: Requirement Analysis
This is where QA dives into what needs testing. It's about understanding the "what" before the "how."

**QA Activities:**
- Thoroughly review requirements specs, user stories, and design docs.
- Identify ambiguities and seek clarifications from devs or stakeholders.
- Categorize requirements as functional (what it does) vs. non-functional (how well it does it).
- Build a Requirement Traceability Matrix (RTM) to link reqs to tests.
- Assess risks and prioritize based on impact.

**Deliverables:** RTM, ambiguity log, testable requirements list.

**Example:**
For a login feature:
- Testable: Valid/invalid creds, session management.
- Non-testable: Vague like "user-friendly"—clarify metrics.

**Tip from Training:** Involve QA early to prevent requirement gaps; I've seen how this avoids 30% of later defects.

---

#### Phase 2: Test Planning
The strategy phase plan your attack on potential bugs.

**QA Activities:**
- Outline test scope, objectives, and approach (manual vs. automated).
- Estimate resources, timelines, and costs using techniques like Work Breakdown Structure.
- Select tools (e.g., JIRA for tracking, Selenium for automation).
- Define entry/exit criteria, risks, and mitigation.
- Assign team roles and schedule reviews.

**Deliverables:** Comprehensive Test Plan document, resource matrix.

**Entry Criteria Example:** Stable requirements, approved design.
**Exit Criteria Example:** 90% test coverage, no high-severity open bugs.

**Additional Info:** Include contingency plans for delays. In real projects, this phase might take 20-30% of testing time.

---

#### Phase 3: Test Case Development
Here, we create the actual tests. Focus on clarity and coverage.

**QA Activities:**
- Develop positive/negative test cases based on techniques (see below).
- Prepare test data (e.g., dummy users, edge values).
- Peer review cases for gaps.
- Automate where feasible for regression.
- Get sign-off from leads.

**Deliverables:** Test case repository, data sets, scripts.

**Test Case Template Example:**
```
Test ID: TC-001
Module: Login
Title: Verify successful login with valid credentials
Preconditions: Application is running, user account exists
Steps:
1. Navigate to login page
2. Enter valid username
3. Enter valid password
4. Click 'Login'
Expected Result: Redirect to dashboard, welcome message displayed
Actual Result: [To be filled during execution]
Status: [Pass/Fail]
Priority: High
Severity: Critical
```

**Insight:** Aim for 100% requirement coverage via RTM. I've practiced writing 50+ cases for Sauce Demo it's tedious but essential.

---

#### Phase 4: Test Environment Setup
Get the playground ready for testing.

**QA Activities:**
- Provision hardware/software mimicking production (e.g., servers, browsers).
- Load test data and configure access.
- Install tools and integrate CI/CD if needed.
- Run smoke tests to validate setup.

**Deliverables:** Environment setup report, configuration checklist.

**Checklist Example:**
- [ ] OS and browser versions match specs
- [ ] Database seeded with test data
- [ ] Network/firewall configured
- [ ] Backup/restore procedures tested

**Common Pitfall:** Environment mismatches cause false positives; always verify.

---

#### Phase 5: Test Execution
The action phase run tests and hunt bugs.

**QA Activities:**
- Execute cases in order (smoke first, then detailed).
- Log defects with details (steps, screenshots).
- Retest fixes and run regressions.
- Track metrics daily.

**Deliverables:** Execution logs, defect reports, coverage reports.

**Workflow Diagram:**
```
Start Execution → Run Test Case → Compare Actual vs Expected
If Match: Pass → Next Case
If Not: Fail → Log Bug → Assign → Fix → Retest
```

**Tip:** Use tools like TestRail for tracking. In my simulations, parallel execution sped things up.

---

#### Phase 6: Test Cycle Closure
Wrap up and reflect.

**QA Activities:**
- Compile results and analyze trends (e.g., bug clusters).
- Document lessons learned and process improvements.
- Archive artifacts for audits.
- Present summary to stakeholders.

**Deliverables:** Closure report, metrics dashboard, recommendations.

**Key Metrics:**
- Defect Density: Bugs per KLOC (thousand lines of code)
- Test Coverage: % of code/reqs tested
- Pass Rate: (Passed / Total) * 100

**Example Report Snippet:**
Total Cases: 100 | Executed: 95 | Passed: 85 | Failed: 10 | Blocked: 5 | Pass %: 89%

---

## Testing Types in Depth

Testing isn't one-size-fits-all. Here's a breakdown with more context.

### Functional Testing (What the System Does)

#### a) Unit Testing
- **By:** Developers
- **Focus:** Isolated code units (functions, methods)
- **Tools:** JUnit, PyTest
- **Example:** Testing a password validation function alone.

#### b) Integration Testing
- **By:** Devs/QA
- **Focus:** Interactions between units (e.g., API calls)
- **Approaches:** Big Bang, Top-Down, Bottom-Up
- **Example:** Login module integrating with database.

#### c) System Testing
- **By:** QA
- **Focus:** End-to-end in integrated environment
- **Example:** Full user journey in an app.

#### d) Acceptance Testing
- **By:** Users/Clients
- **Types:** Alpha (internal), Beta (external)
- **Example:** UAT for a new feature rollout.

### Non-Functional Testing (How Well It Performs)

#### a) Performance Testing
- **Focus:** Response time, throughput
- **Tools:** JMeter, LoadRunner
- **Subtypes:** Endurance (long-duration), Volume (data handling)

#### b) Security Testing
- **Focus:** Threats like OWASP Top 10
- **Tools:** Burp Suite, ZAP
- **Example:** Penetration testing for vulnerabilities.

#### c) Usability Testing
- **Focus:** UX metrics like task completion time
- **Methods:** Heuristic evaluation, user sessions
- **Example:** A/B testing navigation menus.

**Other Types:** Compatibility (browsers/devices), Localization (languages), Accessibility (WCAG compliance).

---

## Bug Lifecycle Explained

Bugs have a life too—tracking them properly is key to resolution.

```
New → Assigned → Open → Fixed → Pending Retest → Retested
   ↑                                         ↓
Reopened (if fail)                          Closed (if pass)
```

**Statuses Expanded:**
- **New:** Freshly reported.
- **Rejected:** Not reproducible or invalid.
- **Deferred:** Postponed.
- **Duplicate:** Merge with existing.

**Best Practice:** Use tools like Bugzilla; include repro steps, environment, and expected/actual.

---

## Test Case Design Techniques

These help create efficient tests without exhaustive coverage.

### 1. Equivalence Partitioning
Group similar inputs; test one per group to infer behavior.

**Example Extended:** Password length 8-16 chars.
- Invalid: 7 chars
- Valid: 12 chars
- Invalid: 17 chars

### 2. Boundary Value Analysis
Test edges where errors lurk.

**Example:** File upload size 1-10MB.
- 0.9MB (fail), 1MB (pass), 5MB (pass), 10MB (pass), 10.1MB (fail)

### 3. Decision Table Testing
Matrix for input combos.

**Expanded Example:** Discount system.

| Age | Membership | Discount |
|-----|------------|----------|
| <18 | No        | 0%      |
| <18 | Yes       | 10%     |
| >=18| No        | 5%      |
| >=18| Yes       | 20%     |

**Other Techniques:** State Transition (e.g., order statuses), Pairwise (combo reduction).

---

## Severity vs. Priority: Don't Confuse Them

**Severity:** How bad is the impact?
- Blocker: App unusable.
- Critical: Data corruption.
- Major: Feature broken, no workaround.
- Minor: Annoyance.
- Trivial: Spelling error.

**Priority:** How soon to fix?
- P1: Immediate.
- P2: High urgency.
- P3: Medium.
- P4: Low.

**Scenario:** Crashing on rare device/ High Severity, Low Priority if user base is small.

---

## Key Learnings and Tips

From my week 1 reflections:
1. Start testing in requirements, cheaper to fix early.
2. Balance scripted and exploratory testing for better coverage.
3. Always trace back to business value; not all bugs are equal.
4. Collaborate: QA isn't isolated work with devs.
5. Stay updated: Tools evolve; learn automation basics next.
6. Prevention mindset: Use root cause analysis (5 Whys) for bugs.

---

## Glossary of Terms

- **Defect Leakage:** Bugs escaping to production.
- **Test Harness:** Setup for automated tests.
- **Black Box Testing:** No code knowledge, focus on inputs/outputs.
- **White Box:** Code-level insight.
- **Grey Box:** Mix of both.
- **Ad-hoc Testing:** Informal, no plan great for quick checks.

---

*These notes are from my personal study sessions, including hands-on practice with demo apps. I'll update as I learn more in Week 2.*

---
**Prepared by:** Muhammad Yasin Asif  
**Role:** QA Engineer (In Training)  
**Date:** October 8, 2025  
*Repository:* [QA-Engineer-Portfolio](https://github.com/YasinAsif/QA-Engineer-Portfolio)
