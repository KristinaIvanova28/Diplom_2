import allure
from http_client import HttpClient

class OrderMethods:
    def __init__(self, client: HttpClient):
        self.client = client
    
    @allure.step("Создание заказа")
    def create_order(self, urls, ingredients, token=None):
        payload = {"ingredients": ingredients}
        if token:
            headers = {"Authorization": token}
            return self.client.post(urls.ORDERS_URL, json=payload, headers=headers)
        return self.client.post(urls.ORDERS_URL, json=payload)
    
    @allure.step("Получение заказов пользователя")
    def get_user_orders(self, urls, token):
        headers = {"Authorization" : token}
        return self.client.get(urls.ORDERS_URL, headers=headers)
    
    @allure.step("Получение всех ингредиентов")
    def get_ingredients(self, urls):
        return self.client.get(urls.INGREDIENTS_URL)
    
    @allure.step("Получение заказов всех пользователей")
    def get_all_orders(self, urls):
        return self.client.get(urls.ORDERS_ALL_URL)