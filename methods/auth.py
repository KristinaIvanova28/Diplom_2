import allure
from http_client import HttpClient

class AuthMethods:
    def __init__(self, client: HttpClient):
        self.client = client
    
    @allure.step("Регистрация пользователя")
    def register_user(self, urls, user_data):
        return self.client.post(urls.REGISTER_URL, json=user_data)
    
    @allure.step("Вход пользователя")
    def login_user(self, urls, credentials):
        return self.client.post(urls.LOGIN_URL, json=credentials)
    
    @allure.step("Удаление пользователя")
    def delete_user(self, urls, token):
        headers = {"Authorization": token}
        return self.client.delete(urls.USER_URL, headers=headers)
    
    @allure.step("Обновление данных пользователя")
    def update_user(self, urls, user_data, token):
        headers = {"Authorization": token}
        return self.client.patch(urls.USER_URL, json=user_data, headers=headers)
    
    @allure.step("Получение данных пользователя")
    def get_user(self, urls, token):
        headers = {"Authorization": token}
        return self.client.get(urls.USER_URL, headers=headers)