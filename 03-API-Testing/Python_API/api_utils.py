"""
API Testing Utilities
=====================
Reusable utilities for API automation testing.

Author: Muhammad Yasin Asif
Portfolio: QA Engineer Portfolio
"""

import requests
import json
import logging
from typing import Dict, Optional, Any
from dataclasses import dataclass


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class APIResponse:
    """Wrapper class for API responses."""
    status_code: int
    json_data: Optional[Dict]
    headers: Dict
    response_time: float
    text: str
    
    @property
    def is_success(self) -> bool:
        """Check if response is successful (2xx)."""
        return 200 <= self.status_code < 300
    
    @property
    def is_json(self) -> bool:
        """Check if response is JSON."""
        return self.json_data is not None


class APIClient:
    """
    HTTP API client for testing REST APIs.
    
    Features:
    - Session management
    - Request/response logging
    - Response time tracking
    - Easy authentication
    """
    
    def __init__(self, base_url: str, timeout: int = 30):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def set_auth_token(self, token: str, prefix: str = 'Bearer'):
        """Set authorization token for requests."""
        self.default_headers['Authorization'] = f'{prefix} {token}'
    
    def set_header(self, key: str, value: str):
        """Set custom header."""
        self.default_headers[key] = value
    
    def _make_request(self, method: str, endpoint: str, 
                      data: Optional[Dict] = None,
                      params: Optional[Dict] = None,
                      headers: Optional[Dict] = None) -> APIResponse:
        """
        Make HTTP request and return wrapped response.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint (will be appended to base_url)
            data: Request body (will be JSON-encoded)
            params: Query parameters
            headers: Additional headers
            
        Returns:
            APIResponse object
        """
        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        request_headers = {**self.default_headers, **(headers or {})}
        
        logger.info(f"Making {method} request to {url}")
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=request_headers,
                timeout=self.timeout
            )
            
            # Parse JSON if possible
            try:
                json_data = response.json()
            except (json.JSONDecodeError, ValueError):
                json_data = None
            
            logger.info(f"Response: {response.status_code} ({response.elapsed.total_seconds():.3f}s)")
            
            return APIResponse(
                status_code=response.status_code,
                json_data=json_data,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
                text=response.text
            )
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
    
    # HTTP Methods
    
    def get(self, endpoint: str, params: Optional[Dict] = None, 
            headers: Optional[Dict] = None) -> APIResponse:
        """Make GET request."""
        return self._make_request('GET', endpoint, params=params, headers=headers)
    
    def post(self, endpoint: str, data: Optional[Dict] = None,
             headers: Optional[Dict] = None) -> APIResponse:
        """Make POST request."""
        return self._make_request('POST', endpoint, data=data, headers=headers)
    
    def put(self, endpoint: str, data: Optional[Dict] = None,
            headers: Optional[Dict] = None) -> APIResponse:
        """Make PUT request."""
        return self._make_request('PUT', endpoint, data=data, headers=headers)
    
    def patch(self, endpoint: str, data: Optional[Dict] = None,
              headers: Optional[Dict] = None) -> APIResponse:
        """Make PATCH request."""
        return self._make_request('PATCH', endpoint, data=data, headers=headers)
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> APIResponse:
        """Make DELETE request."""
        return self._make_request('DELETE', endpoint, headers=headers)


class APIAssertions:
    """
    Helper class for API response assertions.
    """
    
    @staticmethod
    def assert_status_code(response: APIResponse, expected: int):
        """Assert response status code."""
        assert response.status_code == expected, \
            f"Expected status {expected}, got {response.status_code}"
    
    @staticmethod
    def assert_response_time(response: APIResponse, max_seconds: float):
        """Assert response time is within limit."""
        assert response.response_time < max_seconds, \
            f"Response time {response.response_time:.3f}s exceeded {max_seconds}s"
    
    @staticmethod
    def assert_json_has_key(response: APIResponse, key: str):
        """Assert JSON response contains key."""
        assert response.json_data is not None, "Response is not JSON"
        assert key in response.json_data, f"Key '{key}' not found in response"
    
    @staticmethod
    def assert_json_value(response: APIResponse, key: str, expected: Any):
        """Assert JSON response has expected value for key."""
        assert response.json_data is not None, "Response is not JSON"
        assert response.json_data.get(key) == expected, \
            f"Expected {key}={expected}, got {response.json_data.get(key)}"
    
    @staticmethod
    def assert_json_array_length(response: APIResponse, expected_length: int):
        """Assert JSON array has expected length."""
        assert response.json_data is not None, "Response is not JSON"
        assert isinstance(response.json_data, list), "Response is not an array"
        assert len(response.json_data) == expected_length, \
            f"Expected {expected_length} items, got {len(response.json_data)}"
    
    @staticmethod
    def assert_json_array_not_empty(response: APIResponse):
        """Assert JSON array is not empty."""
        assert response.json_data is not None, "Response is not JSON"
        assert isinstance(response.json_data, list), "Response is not an array"
        assert len(response.json_data) > 0, "Array is empty"


# Convenience function
def create_client(base_url: str) -> APIClient:
    """Create API client instance."""
    return APIClient(base_url)


# Example usage
if __name__ == '__main__':
    # Test with JSONPlaceholder API
    client = APIClient('https://jsonplaceholder.typicode.com')
    
    # GET users
    response = client.get('/users')
    print(f"Status: {response.status_code}")
    print(f"Users count: {len(response.json_data)}")
    
    # GET single user
    response = client.get('/users/1')
    print(f"User name: {response.json_data['name']}")
    
    # POST new user
    new_user = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    response = client.post('/users', data=new_user)
    print(f"Created user ID: {response.json_data['id']}")
