import pytest
from data.urls import Urls
from http_client import HttpClient
from helpers import Helper
from methods.auth import AuthMethods


@pytest.fixture
def api_client():
    """Простая фикстура для HTTP клиента"""
    return HttpClient(Urls.BASE_URL)


@pytest.fixture
def registered_user(api_client):
    """
    Простая фикстура - создает пользователя и удаляет после теста
    Минимум логики, только самое необходимое
    """
    # Создаем объекты прямо здесь
    helper = Helper()
    auth_methods = AuthMethods(api_client)
    urls = Urls()
    
    # Регистрируем пользователя
    user_data = helper.generate_unique_user()
    response = auth_methods.register_user(urls, user_data)
    
    # Проверяем что регистрация прошла успешно
    assert response.status_code == 200
    token = response.json()['accessToken']
    
    # Возвращаем данные пользователя
    yield {
        'email': user_data['email'],
        'password': user_data['password'], 
        'name': user_data['name'],
        'token': token
    }
    
    # Удаляем пользователя после теста
    auth_methods.delete_user(urls, token)