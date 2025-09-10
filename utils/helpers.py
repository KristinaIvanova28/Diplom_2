import random
import string


def generate_email():
    """Генерирует уникальный email"""
    return f"user_{random.randint(10000, 99999)}@gmail.com"


def generate_password():
    """Генерирует валидный пароль (минимум 6 символов, есть цифра)"""
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(10))
    return password if any(c.isdigit() for c in password) else password[:-1] + "1"