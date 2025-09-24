import random
import string


class Helper:
    """Класс для генерации тестовых данных и вспомогательных методов"""
    
    @staticmethod
    def generate_unique_user():
        """Генерация уникального пользователя"""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        return {
            "email": f"test_user_{random_string}@example.com",
            "password": "password123",
            "name": f"TestUser_{random_string}"
        }
    
    @staticmethod
    def get_random_ingredients():
        """Генерация случайных ингредиентов из валидного списка"""
        valid_ingredients = [
            "61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6e",
            "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa72"
        ]
        # Возвращаем 2-3 случайных ингредиента
        return {
            "ingredients": random.sample(valid_ingredients, random.randint(2, 3))
        }