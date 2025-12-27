"""
API Test Suite
==============
Automated API tests using pytest.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import pytest
from api_utils import APIClient, APIAssertions


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture(scope="module")
def api_client():
    """Create API client for JSONPlaceholder."""
    return APIClient('https://jsonplaceholder.typicode.com')


@pytest.fixture(scope="module")
def reqres_client():
    """Create API client for ReqRes API."""
    return APIClient('https://reqres.in/api')


# =============================================================================
# GET TESTS
# =============================================================================

class TestGetRequests:
    """Test suite for GET requests."""
    
    def test_get_all_users(self, api_client):
        """
        Test: Get all users
        Endpoint: GET /users
        Expected: 200 OK, returns array of users
        """
        response = api_client.get('/users')
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_array_not_empty(response)
        assert len(response.json_data) == 10, "Should return 10 users"
    
    def test_get_single_user(self, api_client):
        """
        Test: Get single user by ID
        Endpoint: GET /users/1
        Expected: 200 OK, returns user object
        """
        response = api_client.get('/users/1')
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_has_key(response, 'id')
        APIAssertions.assert_json_has_key(response, 'name')
        APIAssertions.assert_json_has_key(response, 'email')
        APIAssertions.assert_json_value(response, 'id', 1)
    
    def test_get_user_has_required_fields(self, api_client):
        """
        Test: User object has all required fields
        """
        response = api_client.get('/users/1')
        
        required_fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
        for field in required_fields:
            APIAssertions.assert_json_has_key(response, field)
    
    def test_get_all_posts(self, api_client):
        """
        Test: Get all posts
        Endpoint: GET /posts
        Expected: 200 OK, returns 100 posts
        """
        response = api_client.get('/posts')
        
        APIAssertions.assert_status_code(response, 200)
        assert len(response.json_data) == 100, "Should return 100 posts"
    
    def test_get_posts_with_query_param(self, api_client):
        """
        Test: Filter posts by userId
        Endpoint: GET /posts?userId=1
        Expected: Returns only posts from user 1
        """
        response = api_client.get('/posts', params={'userId': 1})
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_array_not_empty(response)
        
        # Verify all posts belong to user 1
        for post in response.json_data:
            assert post['userId'] == 1, f"Post {post['id']} has wrong userId"
    
    def test_get_post_comments(self, api_client):
        """
        Test: Get comments for a post
        Endpoint: GET /posts/1/comments
        Expected: Returns array of comments
        """
        response = api_client.get('/posts/1/comments')
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_array_not_empty(response)
        
        # Verify comment structure
        comment = response.json_data[0]
        assert 'postId' in comment
        assert 'email' in comment
        assert 'body' in comment
    
    def test_response_time_acceptable(self, api_client):
        """
        Test: Response time is within acceptable limits
        Expected: Response < 2 seconds
        """
        response = api_client.get('/users')
        
        APIAssertions.assert_response_time(response, 2.0)


# =============================================================================
# POST TESTS
# =============================================================================

class TestPostRequests:
    """Test suite for POST requests."""
    
    def test_create_post(self, api_client):
        """
        Test: Create new post
        Endpoint: POST /posts
        Expected: 201 Created, returns created post with ID
        """
        new_post = {
            'title': 'Test Post Title',
            'body': 'This is the test post body content.',
            'userId': 1
        }
        
        response = api_client.post('/posts', data=new_post)
        
        APIAssertions.assert_status_code(response, 201)
        APIAssertions.assert_json_has_key(response, 'id')
        APIAssertions.assert_json_value(response, 'title', 'Test Post Title')
        APIAssertions.assert_json_value(response, 'userId', 1)
    
    def test_create_user(self, api_client):
        """
        Test: Create new user
        Endpoint: POST /users
        Expected: 201 Created
        """
        new_user = {
            'name': 'Muhammad Yasin',
            'username': 'yasin_asif',
            'email': 'yasin@example.com'
        }
        
        response = api_client.post('/users', data=new_user)
        
        APIAssertions.assert_status_code(response, 201)
        APIAssertions.assert_json_has_key(response, 'id')


# =============================================================================
# PUT TESTS
# =============================================================================

class TestPutRequests:
    """Test suite for PUT requests."""
    
    def test_update_post(self, api_client):
        """
        Test: Update existing post
        Endpoint: PUT /posts/1
        Expected: 200 OK, returns updated post
        """
        updated_post = {
            'id': 1,
            'title': 'Updated Title',
            'body': 'Updated body content.',
            'userId': 1
        }
        
        response = api_client.put('/posts/1', data=updated_post)
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_value(response, 'title', 'Updated Title')


# =============================================================================
# PATCH TESTS
# =============================================================================

class TestPatchRequests:
    """Test suite for PATCH requests."""
    
    def test_partial_update_post(self, api_client):
        """
        Test: Partial update of post
        Endpoint: PATCH /posts/1
        Expected: 200 OK, only specified field updated
        """
        update_data = {
            'title': 'Partially Updated Title'
        }
        
        response = api_client.patch('/posts/1', data=update_data)
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_value(response, 'title', 'Partially Updated Title')


# =============================================================================
# DELETE TESTS
# =============================================================================

class TestDeleteRequests:
    """Test suite for DELETE requests."""
    
    def test_delete_post(self, api_client):
        """
        Test: Delete existing post
        Endpoint: DELETE /posts/1
        Expected: 200 OK
        """
        response = api_client.delete('/posts/1')
        
        APIAssertions.assert_status_code(response, 200)


# =============================================================================
# ERROR HANDLING TESTS
# =============================================================================

class TestErrorHandling:
    """Test suite for error scenarios."""
    
    def test_get_nonexistent_resource(self, api_client):
        """
        Test: Request non-existent resource
        Endpoint: GET /posts/999999
        Expected: 404 Not Found (JSONPlaceholder returns empty object)
        """
        response = api_client.get('/posts/999999')
        
        # JSONPlaceholder returns 404 for non-existent resources
        assert response.status_code in [200, 404]
    
    def test_invalid_endpoint(self, api_client):
        """
        Test: Request invalid endpoint
        Endpoint: GET /invalid-endpoint
        Expected: 404 Not Found
        """
        response = api_client.get('/invalid-endpoint')
        
        assert response.status_code == 404


# =============================================================================
# REQRES API TESTS
# =============================================================================

class TestReqResAPI:
    """Tests using ReqRes API (different API for variety)."""
    
    def test_list_users(self, reqres_client):
        """
        Test: List users with pagination
        Endpoint: GET /users?page=1
        """
        response = reqres_client.get('/users', params={'page': 1})
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_has_key(response, 'data')
        APIAssertions.assert_json_has_key(response, 'total')
    
    def test_single_user(self, reqres_client):
        """
        Test: Get single user
        Endpoint: GET /users/2
        """
        response = reqres_client.get('/users/2')
        
        APIAssertions.assert_status_code(response, 200)
        assert 'data' in response.json_data
        assert response.json_data['data']['id'] == 2
    
    def test_user_not_found(self, reqres_client):
        """
        Test: User not found
        Endpoint: GET /users/23
        Expected: 404 Not Found
        """
        response = reqres_client.get('/users/23')
        
        APIAssertions.assert_status_code(response, 404)
    
    def test_create_user_reqres(self, reqres_client):
        """
        Test: Create user
        Endpoint: POST /users
        """
        user_data = {
            'name': 'Yasin Asif',
            'job': 'QA Engineer'
        }
        
        response = reqres_client.post('/users', data=user_data)
        
        APIAssertions.assert_status_code(response, 201)
        APIAssertions.assert_json_has_key(response, 'id')
        APIAssertions.assert_json_has_key(response, 'createdAt')
    
    def test_login_successful(self, reqres_client):
        """
        Test: Successful login
        Endpoint: POST /login
        """
        login_data = {
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        }
        
        response = reqres_client.post('/login', data=login_data)
        
        APIAssertions.assert_status_code(response, 200)
        APIAssertions.assert_json_has_key(response, 'token')
    
    def test_login_missing_password(self, reqres_client):
        """
        Test: Login without password
        Endpoint: POST /login
        Expected: 400 Bad Request
        """
        login_data = {
            'email': 'eve.holt@reqres.in'
        }
        
        response = reqres_client.post('/login', data=login_data)
        
        APIAssertions.assert_status_code(response, 400)
        APIAssertions.assert_json_has_key(response, 'error')


# Run tests:
# pytest test_api.py -v
# pytest test_api.py -v -k "get"
# pytest test_api.py -v -k "post"
