import pytest
import allure
from data.urls import Urls
from data.data import Data
from methods.order import OrderMethods


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api_client, registered_user):
        """Создание заказа с авторизацией"""
        urls = Urls()
        order_methods = OrderMethods(api_client)
        
        response = order_methods.create_order(
            urls, 
            Data.VALID_INGREDIENTS["ingredients"], 
            registered_user['token']
        )
        
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api_client):
        """Создание заказа без авторизации"""
        urls = Urls()
        order_methods = OrderMethods(api_client)
        
        response = order_methods.create_order(urls, Data.VALID_INGREDIENTS["ingredients"])
        
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api_client, registered_user):
        """Создание заказа с ингредиентами"""
        urls = Urls()
        order_methods = OrderMethods(api_client)
        
        response = order_methods.create_order(
            urls, 
            Data.VALID_INGREDIENTS["ingredients"], 
            registered_user['token']
        )
        
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api_client, registered_user):
        """Создание заказа без ингредиентов"""
        urls = Urls()
        order_methods = OrderMethods(api_client)
        
        response = order_methods.create_order(urls, [], registered_user['token'])
        
        assert response.status_code == 400
        assert response.json()["success"] == False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients_hash(self, api_client, registered_user):
        """Создание заказа с неверным хешем ингредиентов"""
        urls = Urls()
        order_methods = OrderMethods(api_client)

        response = order_methods.create_order(
            urls,
            Data.INVALID_INGREDIENTS["ingredients"],
            registered_user['token']
        )

        # Проверяем, что статус код указывает на ошибку
        assert response.status_code == 500, f"Ожидался статус код 500, но получен {response.status_code}"
    
        # Проверяем, что ответ содержит текст ошибки (HTML или plain text)
        assert "Internal Server Error" in response.text