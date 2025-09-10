import allure


@allure.title("Получение списка заказов пользователя")
def test_get_user_orders(auth_token, order_client):
    response = order_client.get_user_orders(auth_token)

    assert response.status_code == 200
    assert "orders" in response.json()
    assert isinstance(response.json()["orders"], list)