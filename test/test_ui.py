import pytest
import allure
import json
from pages.auth_page import AuthPage
from pages.projects_page import ProjectsPage


@pytest.mark.ui
@allure.feature("UI Тесты YouGile")
class TestYouGileUI:

    @pytest.fixture
    def logged_in_browser(self, browser):
        """Фикстура авторизации"""
        with allure.step("Загружаем конфиг"):
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)

        with allure.step("Открываем страницу авторизации"):
            auth_page = AuthPage(browser)
            auth_page.go()

        with allure.step("Вводим логин и пароль"):
            auth_page.login_as(
                config["test_credentials"]["email"],
                config["test_credentials"]["password"]
            )

        with allure.step("Ждём успешной авторизации"):
            auth_page.wait.until(
                lambda driver: auth_page.is_login_successful())

        return browser

    @allure.title("1. Успешная авторизация")
    def test_successful_login(self, browser):
        with allure.step("Загружаем конфигурацию"):
            with open('config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)

        with allure.step("Открываем страницу авторизации"):
            auth_page = AuthPage(browser)
            auth_page.go()

        with allure.step("Вводим логин и пароль"):
            auth_page.login_as(
                config["test_credentials"]["email"],
                config["test_credentials"]["password"]
            )

        with allure.step("Проверяем успешность входа"):
            assert auth_page.is_login_successful()

    @allure.title("2. Создание проекта из 1 символа")
    def test_create_project_1_symbol(self, logged_in_browser):
        with allure.step("Открываем проекты"):
            projects_page = ProjectsPage(logged_in_browser)

        with allure.step("Создаём проект"):
            project_name = "Я"
            projects_page.create_new_project(project_name)

        with allure.step("Проверяем наличие проекта"):
            assert len(projects_page.get_project_names()) > 0

    @allure.title("3. Создание проекта на кириллице")
    def test_create_project_cyrillic(self, logged_in_browser):
        with allure.step("Открываем проекты"):
            projects_page = ProjectsPage(logged_in_browser)

        with allure.step("Создаём проект"):
            project_name = "Тест"
            projects_page.create_new_project(project_name)

        with allure.step("Проверяем наличие проекта"):
            assert len(projects_page.get_project_names()) > 0

    @allure.title("4. Создание проекта на латинице")
    def test_create_project_latinic(self, logged_in_browser):
        with allure.step("Открываем проекты"):
            projects_page = ProjectsPage(logged_in_browser)

        with allure.step("Создаём проект"):
            project_name = "Test"
            projects_page.create_new_project(project_name)

        with allure.step("Проверяем наличие проекта"):
            assert len(projects_page.get_project_names()) > 0

    @allure.title("5. Создание проекта с цифрами")
    def test_create_project_with_numbers(self, logged_in_browser):
        with allure.step("Открываем проекты"):
            projects_page = ProjectsPage(logged_in_browser)

        with allure.step("Создаём проект"):
            project_name = "Проект123"
            projects_page.create_new_project(project_name)

        with allure.step("Проверяем наличие проекта"):
            assert len(projects_page.get_project_names()) > 0

    @allure.title("6. Создание проекта со спецсимволами")
    def test_create_project_with_special_chars(self, logged_in_browser):
        with allure.step("Открываем проекты"):
            projects_page = ProjectsPage(logged_in_browser)

        with allure.step("Создаём проект"):
            project_name = "Проект@#$%&*()"
            projects_page.create_new_project(project_name)

        with allure.step("Проверяем наличие проекта"):
            assert len(projects_page.get_project_names()) > 0
