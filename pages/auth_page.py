import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.wait = WebDriverWait(
            driver, self.config["test_settings"]["wait_time"])

    @allure.step("Открываем страницу авторизации")
    def go(self):
        """Переходит на страницу авторизации"""
        self.driver.get(self.config['base_url'])

    @allure.step("Авторизация пользователя")
    def login_as(self, email, password):
        """Выполняет авторизацию"""
        with allure.step("Вводим email"):
            email_field = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "input[type='email']"))
            )
            email_field.send_keys(email)

        with allure.step("Вводим пароль"):
            password_field = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "input[type='password']"))
            )
            password_field.send_keys(password)

        with allure.step("Нажимаем кнопку 'Войти'"):
            submit_button = self.driver.find_element(
                By.XPATH,
                "//div[contains(@class, 'cursor-pointer')"
                " and contains(text(), 'Войти')]"
            )
            submit_button.click()

    @allure.step("Проверяем успешность авторизации")
    def is_login_successful(self):
        """Проверяет успешность авторизации по наличию элементов интерфейса"""
        profile_elements = self.driver.find_elements(
            By.XPATH,
            "//div[contains(@class, 'cursor-pointer')"
            " and .//div[text()='Мой профиль']]"
        )
        return len(profile_elements) > 0
