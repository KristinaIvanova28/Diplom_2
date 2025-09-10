import pytest
import allure
from api.user_client import UserClient
from api.order_client import OrderClient
from utils.helpers import generate_email, generate_password
from utils.data import BUN_ID, SAUCE_ID, FILLING_ID


class TestFixture:
    """Класс для хранения фикстур в conftest.py"""

    @pytest.fixture(scope="function")
    @allure.title("Подготовка данных пользователя")
    def user_data(self):
        return {
            "email": generate_email(),
            "password": generate_password(),
            "name": "Тестовый Пользователь"
        }

    @pytest.fixture(scope="function")
    @allure.title("Регистрация пользователя перед тестом")
    def registered_user(self, user_data):
        user_client = UserClient()
        response = user_client.create_user(
            email=user_data["email"],
            password=user_data["password"],
            name=user_data["name"]
        )

        assert response.status_code == 200
        data = response.json()
        user_data["token"] = data["accessToken"]
        # user_data["id"] = data["user"]["_id"]  # ❌ Удалено — поля нет в API
        # user_data["email"] = data["user"]["email"]  # ⚠️ Опционально: можно сохранить, но и так есть

        yield user_data

        # Очистка: удаление пользователя
        user_client.delete_user(user_data["token"])

    @pytest.fixture(scope="function")
    @allure.title("Получение авторизационного токена")
    def auth_token(self, registered_user):
        return registered_user["token"]

    @pytest.fixture(scope="function")
    @allure.title("Клиент для работы с заказами")
    def order_client(self):
        return OrderClient()

    @pytest.fixture(scope="function")
    @allure.title("Клиент для работы с пользователями")
    def user_client(self):
        return UserClient()

    @pytest.fixture(scope="function")
    @allure.title("Список ингредиентов для заказа")
    def sample_ingredients(self):
        return [BUN_ID, SAUCE_ID, FILLING_ID]


# Инициализация фикстур
fixture = TestFixture()

user_data = fixture.user_data
registered_user = fixture.registered_user
auth_token = fixture.auth_token
order_client = fixture.order_client
user_client = fixture.user_client
sample_ingredients = fixture.sample_ingredients