class Urls:
    """Класс с URL эндпоинтами API Stellar Burgers"""
    
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    
    # Auth endpoints
    REGISTER_URL = "/auth/register"
    LOGIN_URL = "/auth/login" 
    USER_URL = "/auth/user"
    LOGOUT_URL = "/auth/logout"
    
    # Order endpoints
    ORDERS_URL = "/orders"
    ORDERS_ALL_URL = "/orders/all"
    
    # Ingredients endpoint
    INGREDIENTS_URL = "/ingredients"