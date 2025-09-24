import pytest
import allure
from data.urls import Urls
from helpers import Helper
from methods.auth import AuthMethods


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self, api_client):
        """Создать уникального пользователя"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        helper = Helper()
        
        user_data = helper.generate_unique_user()
        response = auth_methods.register_user(urls, user_data)
        
        assert response.status_code == 200
        assert response.json()["success"] == True
        
        # Удаляем пользователя
        token = response.json()["accessToken"]
        auth_methods.delete_user(urls, token)

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, api_client, registered_user):
        """Создать пользователя, который уже зарегистрирован"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        
        response = auth_methods.register_user(urls, {
            "email": registered_user['email'],
            "password": "different_password",
            "name": "DifferentName"
        })
        
        assert response.status_code == 403
        assert response.json()["success"] == False

    @allure.title("Создать пользователя без email")
    def test_create_user_without_email(self, api_client):
        """Создать пользователя и не заполнить одно из обязательных полей (email)"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        helper = Helper()
        
        user_data = helper.generate_unique_user()
        user_data.pop("email")  # Удаляем обязательное поле
        
        response = auth_methods.register_user(urls, user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] == False

    @allure.title("Создать пользователя без пароля")
    def test_create_user_without_password(self, api_client):
        """Создать пользователя и не заполнить одно из обязательных полей (password)"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        helper = Helper()
        
        user_data = helper.generate_unique_user()
        user_data.pop("password")  # Удаляем обязательное поле
        
        response = auth_methods.register_user(urls, user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] == False

    @allure.title("Создать пользователя без имени")
    def test_create_user_without_name(self, api_client):
        """Создать пользователя и не заполнить одно из обязательных полей (name)"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        helper = Helper()
        
        user_data = helper.generate_unique_user()
        user_data.pop("name")  # Удаляем обязательное поле
        
        response = auth_methods.register_user(urls, user_data)
        
        assert response.status_code == 403
        assert response.json()["success"] == False