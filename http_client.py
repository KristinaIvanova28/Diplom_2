import requests
import allure


class HttpClient:
    """HTTP клиент в стиле Ильи - простой и эффективный"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    @allure.step("POST {path}")
    def post(self, path, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return self.session.post(url, json=json, headers=headers)
    
    @allure.step("GET {path}") 
    def get(self, path, headers=None):
        url = f"{self.base_url}{path}"
        return self.session.get(url, headers=headers)
    
    @allure.step("DELETE {path}")
    def delete(self, path, headers=None):
        url = f"{self.base_url}{path}"
        return self.session.delete(url, headers=headers)