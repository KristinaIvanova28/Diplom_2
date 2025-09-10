
import allure
import requests


class BaseClient:
    @allure.step("Отправить {method} запрос на {url}")
    def _request(self, method, url, **kwargs):
        response = requests.request(method, url, **kwargs)
        return response