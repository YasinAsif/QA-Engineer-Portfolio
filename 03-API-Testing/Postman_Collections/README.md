# 📬 Postman Collections

This folder contains Postman collections demonstrating API testing skills.

---

## 📋 Collections

### 1. Sample API Tests
A collection testing public APIs to demonstrate:
- GET requests for data retrieval
- POST requests for resource creation
- Response validation
- Error handling tests

### Testing APIs Used
Since Sauce Demo doesn't have a public API, I've used these popular test APIs:

| API | URL | Purpose |
|-----|-----|---------|
| JSONPlaceholder | https://jsonplaceholder.typicode.com | REST API testing |
| ReqRes | https://reqres.in | User management API |
| HTTP Bin | https://httpbin.org | HTTP testing |

---

## 🔧 Environment Variables

```json
{
  "base_url": "https://jsonplaceholder.typicode.com",
  "user_id": "1",
  "auth_token": "{{generated_token}}"
}
```

---

## 📊 Test Cases Covered

### Users Endpoint
| Test Case | Method | Endpoint | Expected |
|-----------|--------|----------|----------|
| Get all users | GET | /users | 200, array |
| Get single user | GET | /users/1 | 200, user object |
| Get invalid user | GET | /users/999 | 404 |
| Create user | POST | /users | 201, created |
| Update user | PUT | /users/1 | 200, updated |
| Delete user | DELETE | /users/1 | 200 |

### Posts Endpoint
| Test Case | Method | Endpoint | Expected |
|-----------|--------|----------|----------|
| Get all posts | GET | /posts | 200, 100 posts |
| Get user posts | GET | /posts?userId=1 | 200, filtered |
| Create post | POST | /posts | 201 |
| Get post comments | GET | /posts/1/comments | 200, array |

---

## 🧪 Postman Tests

### Status Code Validation
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### Response Time Check
```javascript
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

### JSON Schema Validation
```javascript
pm.test("Response has required fields", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('name');
    pm.expect(jsonData).to.have.property('email');
});
```

### Array Length Check
```javascript
pm.test("Returns array of users", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
    pm.expect(jsonData.length).to.be.above(0);
});
```

---

## 📥 How to Use

### Import Collection
1. Open Postman
2. Click **Import**
3. Select the `.json` collection file
4. Import the environment file (if provided)

### Run Collection
1. Click **Run** on the collection
2. Select environment
3. Configure iterations if needed
4. Click **Run**

### View Results
- Check test results in the runner
- Export results as HTML/JSON

---

## 📸 Screenshots

*Add screenshots of Postman tests here*

---

## 🎯 Skills Demonstrated

- ✅ RESTful API understanding
- ✅ HTTP methods and status codes
- ✅ Request/response headers
- ✅ JSON data handling
- ✅ Postman scripting (JavaScript)
- ✅ Environment management
- ✅ Collection runner usage

---

*Part of QA Engineer Portfolio - API Testing*
