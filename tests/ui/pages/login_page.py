"""
Page Object для страницы логина: https://www.saucedemo.com
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"
    
    # Локаторы
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        """Открыть страницу логина"""
        self.driver.get(self.URL)
        return self
    
    def enter_username(self, username):
        """Ввести логин"""
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        return self
    
    def enter_password(self, password):
        """Ввести пароль"""
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        return self
    
    def click_login(self):
        """Нажать кнопку логина"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self
    
    def login(self, username, password):
        """Полный сценарий логина"""
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return InventoryPage(self.driver)
    
    def has_error_message(self):
        """Проверить наличие сообщения об ошибке"""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return True
        except:
            return False
    
    def get_error_text(self):
        """Получить текст ошибки"""
        return self.driver.find_element(*self.ERROR_MESSAGE).text


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        self.driver = driver
    
    def is_loaded(self):
        """Проверить, что страница товаров загружена"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.TITLE)
            )
            return True
        except:
            return False
    
    def get_title(self):
        """Получить заголовок страницы"""
        return self.driver.find_element(*self.TITLE).text
