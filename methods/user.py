import allure
from http_client import HttpClient

class UserMethods:
    def __init__(self, client: HttpClient):
        self.client = client
    
    @allure.step("Создание тестового пользователя")
    def create_test_user(self, urls, helper):
        user_data = helper.generate_user_data()
        response = self.client.post(urls.register, json=user_data)
        if response.status_code == 200:
            token = response.json()["accessToken"]
            return {**user_data, "token": token}
        return None
    
    @allure.step("Создание и удаление тестового пользователя")
    def create_and_cleanup_user(self, urls, helper):
        user = self.create_test_user(urls, helper)
        yield user
        if user and "token" in user:
            self.client.delete(
                urls.user, 
                headers={"Authorization": f"Bearer {user['token']}"}
            )