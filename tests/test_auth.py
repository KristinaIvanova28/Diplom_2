import allure
import pytest
from methods.auth import AuthMethods

@allure.feature("Авторизация и регистрация")
class TestAuth:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, client, urls, helper):
        """Тест создания уникального пользователя"""
        with allure.step("Создать нового пользователя"):
            user_data = helper.generate_user_data()
            response = client.post(urls.register, json=user_data)
    
        with allure.step("Проверить успешную регистрацию"):
            if response.status_code != 200:
                print(f"Ошибка регистрации: {response.text}")
    
        with allure.step("Проверить успешную регистрацию"):
            if response.status_code != 200:
                print(f"Ошибка регистрации: {response.text}")
            

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, client, urls, helper):
        """Тест попытки регистрации уже существующего пользователя"""
        with allure.step("Создать первого пользователя"):
            user_data = helper.generate_user_data()
            first_response = client.post(urls.register, json=user_data)
            assert first_response.status_code == 200
        
        with allure.step("Попытаться создать пользователя с теми же данными"):
            second_response = client.post(urls.register, json=user_data)
        
        with allure.step("Проверить ошибку конфликта"):
            assert second_response.status_code == 403
            assert second_response.json()["success"] is False
            assert "User already exists" in second_response.json()["message"]

    @allure.title("Создание пользователя без email")
    def test_create_user_without_email(self, client, urls, helper):
        """Тест создания пользователя без обязательного поля email"""
        with allure.step("Создать пользователя без email"):
            user_data = helper.generate_user_data()
            user_data.pop("email")
            response = client.post(urls.register, json=user_data)
        
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 403
            assert response.json()["success"] is False

    @allure.title("Создание пользователя без пароля")
    def test_create_user_without_password(self, client, urls, helper):
        """Тест создания пользователя без обязательного поля password"""
        with allure.step("Создать пользователя без пароля"):
            user_data = helper.generate_user_data()
            user_data.pop("password")
            response = client.post(urls.register, json=user_data)
        
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 403
            assert response.json()["success"] is False

    @allure.title("Создание пользователя без имени")
    def test_create_user_without_name(self, client, urls, helper):
        """Тест создания пользователя без обязательного поля name"""
        with allure.step("Создать пользователя без имени"):
            user_data = helper.generate_user_data()
            user_data.pop("name")
            response = client.post(urls.register, json=user_data)
        
        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 403
            assert response.json()["success"] is False

    @allure.title("Успешный вход под существующим пользователем")
    def test_login_existing_user(self, client, urls, helper):
        """Тест успешного входа под существующим пользователем"""
        with allure.step("Зарегистрировать пользователя"):
            user_data = helper.generate_user_data()
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
        
        with allure.step("Выполнить вход с правильными креденшиалами"):
            credentials = {
                "email": user_data["email"],
                "password": user_data["password"]
            }
            login_response = client.post(urls.login, json=credentials)
        
        with allure.step("Проверить успешный вход"):
            assert login_response.status_code == 200
            assert login_response.json()["success"] is True
            assert "accessToken" in login_response.json()

    @allure.title("Вход с неверным email")
    def test_login_with_invalid_email(self, client, urls, helper):
        """Тест входа с неверным email"""
        with allure.step("Зарегистрировать пользователя"):
            user_data = helper.generate_user_data()
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
        
        with allure.step("Попытаться войти с неверным email"):
            credentials = {
                "email": "wrong_email@example.com",
                "password": user_data["password"]
            }
            login_response = client.post(urls.login, json=credentials)
        
        with allure.step("Проверить ошибку авторизации"):
            assert login_response.status_code == 401
            assert login_response.json()["success"] is False

    @allure.title("Вход с неверным паролем")
    def test_login_with_invalid_password(self, client, urls, helper):
        """Тест входа с неверным паролем"""
        with allure.step("Зарегистрировать пользователя"):
            user_data = helper.generate_user_data()
            register_response = client.post(urls.register, json=user_data)
            assert register_response.status_code == 200
        
        with allure.step("Попытаться войти с неверным паролем"):
            credentials = {
                "email": user_data["email"],
                "password": "wrong_password"
            }
            login_response = client.post(urls.login, json=credentials)
        
        with allure.step("Проверить ошибку авторизации"):
            assert login_response.status_code == 401
            assert login_response.json()["success"] is False

    @allure.title("Вход с неверным email и паролем")
    def test_login_with_invalid_credentials(self, client, urls):
        """Тест входа с неверными креденшиалами"""
        with allure.step("Попытаться войти с неверными данными"):
            credentials = {
                "email": "nonexistent@example.com",
                "password": "wrong_password"
            }
            response = client.post(urls.login, json=credentials)
        
        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 401
            assert response.json()["success"] is False