class Data:
    """Класс с тестовыми данными"""
    
    # Существующий пользователь для тестов "пользователь уже зарегистрирован"
    EXISTING_USER = {
        "email": "test_user_existing@example.com",
        "password": "password123", 
        "name": "ExistingUser"
    }
    
    # Невалидные учетные данные
    INVALID_CREDENTIALS = {
        "email": "invalid_user@example.com",
        "password": "wrong_password"
    }
    
    # Валидные ингредиенты (реальные ID из API Stellar Burgers)
    VALID_INGREDIENTS = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
            "61c0c5a71d1f82001bdaaa6f",  # Филе Люминесцентного тетраодонтимформа
            "61c0c5a71d1f82001bdaaa70"   # Сыр с астероидной плесенью
        ]
    }
    
    # Невалидные ингредиенты (несуществующие ID)
    INVALID_INGREDIENTS = {
        "ingredients": [
            "invalid_ingredient_id_123",
            "another_invalid_id_456"
        ]
    }
    
    # Пустые ингредиенты
    EMPTY_INGREDIENTS = {
        "ingredients": []
    }