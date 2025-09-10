
from .base_client import BaseClient
from utils.data import CREATE_ORDER, GET_ORDERS
import allure


class OrderClient(BaseClient):
    @allure.step("Создание заказа с ингредиентами")
    def create_order(self, ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        return self._request("POST", CREATE_ORDER, json=payload, headers=headers)

    @allure.step("Получение списка заказов пользователя")
    def get_user_orders(self, token):
        headers = {"Authorization": token}
        return self._request("GET", GET_ORDERS, headers=headers)