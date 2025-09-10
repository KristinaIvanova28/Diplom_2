
from .base_client import BaseClient
from utils.data import REGISTER_USER, LOGIN_USER, DELETE_USER
import allure


class UserClient(BaseClient):
    @allure.step("Регистрация пользователя: {email}")
    def create_user(self, email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return self._request("POST", REGISTER_USER, json=payload)

    @allure.step("Авторизация пользователя: {email}")
    def login_user(self, email, password):
        payload = {"email": email, "password": password}
        return self._request("POST", LOGIN_USER, json=payload)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        headers = {"Authorization": token}
        return self._request("DELETE", DELETE_USER, headers=headers)