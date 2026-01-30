"""
Глобальные фикстуры для тестов.
Показывает понимание жизненного цикла тестов и переиспользования ресурсов.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ===== UI фикстура =====
@pytest.fixture(scope="function")
def browser():
    """
    Запускает Chrome в headless-режиме (без интерфейса).
    Автоматически закрывает браузер после теста — даже при падении.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options
    )
    driver.implicitly_wait(10)
    
    yield driver
    
    # Гарантированная очистка
    try:
        driver.quit()
    except Exception:
        pass


# ===== API хелпер =====
@pytest.fixture(scope="session")
def api_base_url():
    """Базовый URL для демо-API"""
    return "https://reqres.in/api"
