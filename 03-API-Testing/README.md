# 🔌 API Testing

This section demonstrates API testing skills using Postman and Python automation.

---

## 📚 Contents

### 1. Postman Collections
Professional Postman collections with:
- Environment variables
- Pre-request scripts
- Test assertions
- Collection runner examples

### 2. Python API Automation
API automation using `requests` and `pytest`:
- Request utilities
- Response validation
- Data-driven testing
- Authentication handling

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Postman** | Manual API testing & collection creation |
| **Python requests** | HTTP client for automation |
| **pytest** | Test framework |
| **jsonschema** | Response validation |

---

## 📋 API Testing Skills Demonstrated

1. **REST API Fundamentals**
   - HTTP methods (GET, POST, PUT, DELETE)
   - Status codes (200, 201, 400, 401, 404, 500)
   - Headers and authentication
   - Request/response body handling

2. **Test Types**
   - Functional testing
   - Integration testing
   - Data validation
   - Error handling
   - Performance basics

3. **Best Practices**
   - Environment management
   - Test data handling
   - Reusable utilities
   - Clear assertions

---

## 📁 Folder Structure

```
03-API-Testing/
├── README.md                    # This file
├── Postman_Collections/         # Postman exports
│   ├── README.md               # Collection documentation
│   └── Sample_API_Tests.postman_collection.json
│
└── Python_API/                  # Python automation
    ├── README.md               # Python API docs
    ├── requirements.txt        # Dependencies
    ├── api_utils.py            # API utilities
    ├── test_api.py             # API test cases
    └── conftest.py             # Pytest config
```

---

## 🚀 Quick Start

### Postman
1. Import the collection from `Postman_Collections/`
2. Set up environment variables
3. Run collection

### Python
```bash
cd Python_API
pip install -r requirements.txt
pytest test_api.py -v
```

---

## 📖 Learning Resources

- [Postman Learning Center](https://learning.postman.com/)
- [Python requests Documentation](https://requests.readthedocs.io/)
- [REST API Tutorial](https://restfulapi.net/)

---

*Part of QA Engineer Portfolio*
