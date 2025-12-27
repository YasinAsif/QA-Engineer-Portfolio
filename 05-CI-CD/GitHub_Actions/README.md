# 🔄 GitHub Actions

GitHub Actions workflow for automated test execution.

---

## 📋 Workflow Overview

The workflow file is located at `.github/workflows/selenium-tests.yml`

### Trigger Events

| Event | Description |
|-------|-------------|
| `push` | On push to main/develop |
| `pull_request` | On PR to main |
| `workflow_dispatch` | Manual trigger |

---

## 🔧 Workflow Jobs

### 1. Selenium Tests (`test`)

**Matrix Strategy:** Tests run on Python 3.10 and 3.11

**Steps:**
1. ✅ Checkout repository
2. ✅ Set up Python
3. ✅ Install Chrome browser
4. ✅ Install dependencies
5. ✅ Run pytest with HTML report
6. ✅ Upload test artifacts
7. ✅ Upload failure screenshots

### 2. API Tests (`api-tests`)

**Steps:**
1. ✅ Checkout repository
2. ✅ Set up Python
3. ✅ Install dependencies
4. ✅ Run API tests
5. ✅ Upload report

---

## 📊 Artifacts Generated

| Artifact | Description | Retention |
|----------|-------------|-----------|
| `test-report-{python-version}` | HTML test report | 30 days |
| `failure-screenshots-{python-version}` | Screenshots on failure | 7 days |
| `api-test-report` | API test HTML report | 30 days |

---

## 🚀 How to Use

### Automatic Runs
Push code or create a PR - tests run automatically.

### Manual Trigger
1. Go to **Actions** tab
2. Select **Selenium Tests** workflow
3. Click **Run workflow**

### View Results
1. Click on workflow run
2. View job logs
3. Download artifacts

---

## 📈 Benefits

1. **Automated Quality Checks** - Every change is tested
2. **Fast Feedback** - Know if something breaks quickly
3. **Consistent Environment** - Same setup every time
4. **Quality Gates** - Can block merges on failures
5. **Visibility** - Team can see test results

---

## 🔧 Customization

### Add More Browsers
```yaml
matrix:
  browser: [chrome, firefox, edge]
```

### Add Scheduled Runs
```yaml
on:
  schedule:
    - cron: '0 6 * * *'  # Run at 6 AM daily
```

### Add Slack Notifications
```yaml
- name: Notify Slack
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
```

---

*Part of QA Engineer Portfolio - CI/CD Section*
