import allure
from api.user_client import UserClient


@allure.title("Авторизация пользователя")
def test_login_user_success(user_data, registered_user):
    user_client = UserClient()
    response = user_client.login_user(
        email=user_data["email"],
        password=user_data["password"]
    )

    assert response.status_code == 200
    assert "accessToken" in response.json()