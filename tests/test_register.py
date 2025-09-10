import allure
from api.user_client import UserClient


@allure.title("Регистрация нового пользователя")
def test_register_new_user_success(user_data):
    user_client = UserClient()
    response = user_client.create_user(
        email=user_data["email"],
        password=user_data["password"],
        name=user_data["name"]
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "accessToken" in response.json()
    assert response.json()["user"]["email"] == user_data["email"]