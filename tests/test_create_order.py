import allure


@allure.title("Создание заказа с авторизацией")
def test_create_order_authorized(auth_token, order_client, sample_ingredients):
    response = order_client.create_order(sample_ingredients, auth_token)

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "order" in response.json()
    assert "number" in response.json()["order"]
    assert response.json()["order"]["number"] > 0