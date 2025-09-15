import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://api.yougile.com/api-v2"   # заменить при необходимости

@pytest.fixture(scope="session")
def headers():
    # !!! Наставнику: здесь нужно прописать свой актуальный токен авторизации
    return {
        "Authorization": "Bearer <YOUR_TOKEN>",
        "Content-Type": "application/json"
    }
