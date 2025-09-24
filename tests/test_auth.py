import pytest
import allure
from data.urls import Urls
from data.data import Data
from methods.auth import AuthMethods


@allure.feature("Логин пользователя")
class TestAuth:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, api_client, registered_user):
        """Вход под существующим пользователем"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        
        response = auth_methods.login_user(urls, {
            "email": registered_user['email'],
            "password": registered_user['password']
        })
        
        assert response.status_code == 200
        assert response.json()["success"] == True

    @allure.title("Вход с неверным логином и паролем")
    def test_login_invalid_credentials(self, api_client):
        """Вход с неверным логином и паролем"""
        urls = Urls()
        auth_methods = AuthMethods(api_client)
        
        response = auth_methods.login_user(urls, Data.INVALID_CREDENTIALS)
        
        assert response.status_code == 401
        assert response.json()["success"] == False