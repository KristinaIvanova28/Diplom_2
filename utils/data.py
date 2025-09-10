BASE_URL = "https://stellarburgers.nomoreparties.site/api"

# Эндпоинты
REGISTER_USER = f"{BASE_URL}/auth/register"
LOGIN_USER = f"{BASE_URL}/auth/login"
DELETE_USER = f"{BASE_URL}/auth/user"
CREATE_ORDER = f"{BASE_URL}/orders"
GET_ORDERS = f"{BASE_URL}/orders"
GET_INGREDIENTS = f"{BASE_URL}/ingredients"

# Тексты из модального окна
ORDER_MODAL_TITLE = "идентификатор заказа"
ORDER_SUCCESS_MESSAGE = "Ваш заказ начали готовить"
ORBIT_STATION_MESSAGE = "Дождитесь готовности на орбитальной станции"

# Примеры хешей ингредиентов (можно получить через GET /api/ingredients)
BUN_ID = "61c0c5a71d1f82001bdaaa6d"
SAUCE_ID = "61c0c5a71d1f82001bdaaa71"
FILLING_ID = "61c0c5a71d1f82001bdaaa72"