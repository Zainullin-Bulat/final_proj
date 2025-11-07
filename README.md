# Проект YouGile

Автоматизированные тесты для YouGile (https://ru.yougile.com/)    
API YouGile(https://ru.yougile.com/api-v2#/)

# Allure отчёты:

Браузер Edge Версия 142.0.3595.53 (Официальная сборка) (64-разрядная версия)

# Структура проекта

pages/ - Page Object модели    
test/ - Тесты (UI и API)    
config.json - Конфигурация тестов    
conftest.py - Фикстуры pytest    

# config.json

"test_credentials": {
    "email": "Ваш email",    
    "password": "Ваш pass",    
    "api_key": "Ваш API_KEY",    
    "user_id": "Ваш ID"    
    }
    

# Установите зависимости:

pip3 install -r requirements.txt

# Запуск тестов:

pytest - Все тесты    
pytest -m api - Только API    
pytest -m ui - Только UI    

# Allure отчёты:

pytest --alluredir=allure-results - Запуск тестов с генерацией отчёта    
allure serve allure-results - Просмотр отчёта    
