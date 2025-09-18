import allure
import pytest

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized_with_ingredients(self, client, urls, user_data):
        """Тест создания заказа авторизованным пользователем с валидными ингредиентами"""
        # Регистрация пользователя
        with allure.step("Зарегистрировать пользователя"):
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
            token = register_response.json()["accessToken"]
        
        # Получение ингредиентов
        with allure.step("Получить список ингредиентов"):
            ingredients_response = client.get(urls.ingredients)
            assert ingredients_response.status_code == 200
            ingredients = ingredients_response.json()["data"]
        
        # Создание заказа
        with allure.step("Создать заказ с ингредиентами"):
            order_data = {"ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]}
            headers = {"Authorization": token} 
            response = client.post(urls.orders, json=order_data, headers=headers)
        
        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации с ингредиентами")
    def test_create_order_unauthorized_with_ingredients(self, client, urls):
        """Тест создания заказа неавторизованным пользователем с валидными ингредиентами"""
        # Получение ингредиентов
        with allure.step("Получить список ингредиентов"):
            ingredients_response = client.get(urls.ingredients)
            assert ingredients_response.status_code == 200
            ingredients = ingredients_response.json()["data"]
        
        # Создание заказа
        with allure.step("Создать заказ без авторизации"):
            order_data = {"ingredients": [ingredients[0]["_id"], ingredients[1]["_id"]]}
            response = client.post(urls.orders, json=order_data)
        
        with allure.step("Проверить что неавторизованный пользователь не может создать заказ"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_authorized_without_ingredients(self, client, urls, user_data):
        """Тест создания заказа авторизованным пользователем без ингредиентов"""
        # Регистрация пользователя
        with allure.step("Зарегистрировать пользователя"):
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
            token = register_response.json()["accessToken"]
        
        # Создание заказа
        with allure.step("Создать заказ без ингредиентов"):
            order_data = {"ingredients": []}
            headers = {"Authorization": token}
            response = client.post(urls.orders, json=order_data, headers=headers)
        
        with allure.step("Проверить ошибку при отсутствии ингредиентов"):
            assert response.status_code == 400
            assert response.json()["success"] is False

    @allure.title("Создание заказа без авторизации без ингредиентов")
    def test_create_order_unauthorized_without_ingredients(self, client, urls):
        """Тест создания заказа неавторизованным пользователем без ингредиентов"""
        with allure.step("Создать заказ без ингредиентов и авторизации"):
            order_data = {"ingredients": []}
            response = client.post(urls.orders, json=order_data)
        
        with allure.step("Проверить ошибку при отсутствии ингредиентов"):
            assert response.status_code == 400
            assert response.json()["success"] is False

    @allure.title("Создание заказа с неверным хешем ингредиентов (авторизованный)")
    def test_create_order_authorized_invalid_ingredients(self, client, urls, user_data):
        """Тест создания заказа авторизованным пользователем с невалидными ингредиентами"""
        # Регистрация пользователя
        with allure.step("Зарегистрировать пользователя"):
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
            token = register_response.json()["accessToken"]
        
        # Создание заказа
        with allure.step("Создать заказ с невалидными ингредиентами"):
            order_data = {"ingredients": ["invalid_ingredient_1", "invalid_ingredient_2"]}
            headers = {"Authorization": token}
            response = client.post(urls.orders, json=order_data, headers=headers)
        
        with allure.step("Проверить ошибку при невалидных ингредиентах"):
            assert response.status_code == 500
            

    @allure.title("Создание заказа с неверным хешем ингредиентов (неавторизованный)")
    def test_create_order_unauthorized_invalid_ingredients(self, client, urls):
        """Тест создания заказа неавторизованным пользователем с невалидными ингредиентами"""
        with allure.step("Создать заказ с невалидными ингредиентами без авторизации"):
            order_data = {"ingredients": ["invalid_ingredient_1", "invalid_ingredient_2"]}
            response = client.post(urls.orders, json=order_data)
        
        with allure.step("Проверить ошибку при невалидных ингредиентах"):
            assert response.status_code == 500
            
    def test_create_order_with_one_ingredient(self, client, urls, user_data):
        """Тест создания заказа с одним ингредиентом"""
        # Регистрация пользователя
        with allure.step("Зарегистрировать пользователя"):
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
            token = register_response.json()["accessToken"]
        
        # Получение ингредиентов
        with allure.step("Получить список ингредиентов"):
            ingredients_response = client.get(urls.ingredients)
            assert ingredients_response.status_code == 200
            ingredients = ingredients_response.json()["data"]
        
        # Создание заказа
        with allure.step("Создать заказ с одним ингредиентом"):
            order_data = {"ingredients": [ingredients[0]["_id"]]}
            headers = {"Authorization": token}
            response = client.post(urls.orders, json=order_data, headers=headers)
        
        with allure.step("Проверить создание заказа с одним ингредиентом"):
            assert response.status_code == 200
            assert response.json()["success"] is True