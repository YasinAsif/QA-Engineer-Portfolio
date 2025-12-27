# 🐍 Python API Automation

Python-based API automation testing using `requests` and `pytest`.

---

## 📁 Files

| File | Description |
|------|-------------|
| `api_utils.py` | Reusable API client and assertions |
| `test_api.py` | Test cases (20+ tests) |
| `requirements.txt` | Dependencies |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest test_api.py -v

# Run with HTML report
pytest test_api.py -v --html=report.html
```

---

## 🧪 Test Coverage

### JSONPlaceholder API
| Category | Tests |
|----------|-------|
| GET requests | 7 |
| POST requests | 2 |
| PUT requests | 1 |
| PATCH requests | 1 |
| DELETE requests | 1 |
| Error handling | 2 |

### ReqRes API
| Category | Tests |
|----------|-------|
| User management | 3 |
| Authentication | 2 |

---

## 📚 API Client Features

```python
from api_utils import APIClient

# Create client
client = APIClient('https://api.example.com')

# Set authentication
client.set_auth_token('your-token')

# Make requests
response = client.get('/users')
response = client.post('/users', data={'name': 'John'})

# Check response
if response.is_success:
    print(response.json_data)
```

---

## ✅ Assertions

```python
from api_utils import APIAssertions

# Status code
APIAssertions.assert_status_code(response, 200)

# Response time
APIAssertions.assert_response_time(response, 2.0)

# JSON structure
APIAssertions.assert_json_has_key(response, 'id')
APIAssertions.assert_json_value(response, 'status', 'active')
```

---

*Part of QA Engineer Portfolio*
