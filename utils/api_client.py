import requests
from typing import Dict, Any, Optional

class APIClient:
    """API client for making HTTP requests"""

    def __init__(self, base_url: str, session: Optional[requests.Session] = None):
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send GET request"""
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, **kwargs)

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send POST request"""
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, **kwargs)

    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send PUT request"""
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, data=data, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Send DELETE request"""
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)

    def patch(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send PATCH request"""
        url = f"{self.base_url}{endpoint}"
        return self.session.patch(url, data=data, json=json, **kwargs)