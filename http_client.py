import requests

class HttpClient:
    def post(self, url, data=None, json=None, headers=None):
        return requests.post(url, data=data, json=json, headers=headers)
    
    def get(self, url, headers=None):
        return requests.get(url, headers=headers)
    
    def delete(self, url, headers=None):
        return requests.delete(url, headers=headers)
    
    def patch(self, url, data=None, json=None, headers=None):
        return requests.patch(url, data=data, json=json, headers=headers)