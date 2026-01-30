"""
UI-тесты для демо-магазина: https://www.saucedemo.com
"""

import pytest
from pages.login_page import LoginPage


class TestLoginUI:
    
    def test_valid_login(self, browser):
        """Успешный логин → переход на страницу товаров"""
        login_page = LoginPage(browser)
        
        inventory_page = login_page.login(
            username="standard_user",
            password="secret_sauce"
        )
        
        assert inventory_page.is_loaded(), "Страница товаров не загрузилась"
        assert inventory_page.get_title() == "Products", "Неверный заголовок страницы"
    
    def test_invalid_login(self, browser):
        """Неверные креды → отображение ошибки"""
        login_page = LoginPage(browser)
        login_page.open()
        login_page.enter_username("locked_out_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        assert login_page.has_error_message(), "Сообщение об ошибке не отображается"
        error_text = login_page.get_error_text()
        assert "Sorry" in error_text, f"Ожидалось сообщение с 'Sorry', получено: {error_text}"
