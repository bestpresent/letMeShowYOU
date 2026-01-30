"""
Тесты авторизации через демо-API: https://reqres.in
"""

import pytest
import requests


class TestAuthAPI:
    
    def test_successful_login(self, api_base_url):
        """Позитивный сценарий: успешная авторизация"""
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        
        response = requests.post(f"{api_base_url}/login", json=payload)
        
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        assert "token" in response.json(), "В ответе отсутствует токен авторизации"
        assert len(response.json()["token"]) > 0, "Токен пустой"
    
    def test_failed_login_missing_password(self, api_base_url):
        """Негативный сценарий: отсутствует пароль"""
        payload = {
            "email": "eve.holt@reqres.in"
            # password intentionally missing
        }
        
        response = requests.post(f"{api_base_url}/login", json=payload)
        
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert "error" in response.json(), "В ответе должна быть ошибка"
