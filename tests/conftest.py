import pytest
from urls import Urls
from http_client import HttpClient
from helpers import Helper
from methods.auth import AuthMethods
from methods.order import OrderMethods
from methods.user import UserMethods

@pytest.fixture
def urls():
    return Urls()

@pytest.fixture
def client():
    return HttpClient()

@pytest.fixture
def helper():
    return Helper()

@pytest.fixture
def auth_methods(client):
    return AuthMethods(client)

@pytest.fixture
def order_methods(client):
    return OrderMethods(client)

@pytest.fixture
def user_methods(client):
    return UserMethods(client)

@pytest.fixture
def user_data(helper):
    return helper.generate_user_data()