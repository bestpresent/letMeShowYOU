# letMeShowYOU
API &amp; UI tests with Python/Pytest/Selenium



##  Технологии

| Категория | Инструменты |
|-----------|-------------|
| Язык      | Python 3.9+ |
| Фреймворк | pytest |
| API       | requests, jsonschema |
| UI        | Selenium WebDriver, webdriver-manager |
| Отчёты    | pytest-html |
| Управление зависимостями | pip, virtualenv |

##  Как запустить

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ВАШ-ЛОГИН/qa-automation-showcase.git
cd qa-automation-showcase

# 2. Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить API-тесты
pytest tests/api/ -v --html=reports/api_report.html --self-contained-html

# 5. Запустить UI-тесты (браузер запустится автоматически)
pytest tests/ui/ -v --html=reports/ui_report.html --self-contained-html
