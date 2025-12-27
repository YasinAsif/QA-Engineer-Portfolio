# 🚀 CI/CD and DevOps

This section demonstrates Continuous Integration and Continuous Deployment practices for QA automation.

---

## 📋 Contents

### 1. GitHub Actions
Automated workflows for:
- Running Selenium tests on push/PR
- Generating test reports
- Scheduled test runs

### 2. CI/CD Concepts
Documentation covering:
- Pipeline fundamentals
- Integration with test automation
- Best practices

---

## 🛠️ Technologies

| Tool | Purpose |
|------|---------|
| **GitHub Actions** | CI/CD platform |
| **Jenkins** | Alternative CI server |
| **Docker** | Containerization |

---

## 📁 Folder Structure

```
05-CI-CD/
├── README.md                    # This file
├── GitHub_Actions/              # Workflow files
│   └── README.md
└── Jenkins/                     # Jenkins documentation
    └── README.md
```

---

## 🔗 GitHub Actions Workflow

The workflow file is located at:
```
.github/workflows/selenium-tests.yml
```

### Trigger Events
- Push to `main` branch
- Pull requests
- Manual dispatch
- Scheduled (optional)

### Workflow Steps
1. Checkout code
2. Set up Python
3. Install dependencies
4. Run tests with pytest
5. Generate HTML report
6. Upload artifacts

---

## 💡 Key Learnings

1. **Automation** - Tests run automatically on every change
2. **Consistency** - Same environment every time
3. **Visibility** - Test results visible to team
4. **Quality Gates** - Block merges if tests fail

---

*Part of QA Engineer Portfolio*
