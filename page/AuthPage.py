from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team/settings-account"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str):
        # Ожидаем появления поля ввода email
        email_field = (WebDriverWait(self.__driver, 10)
                       .until(EC.visibility_of_element_located((
                          By.CSS_SELECTOR, "input[type='email']"))))
        email_field.send_keys(email)

        # Ожидаем появления поля ввода пароля
        password_field = (WebDriverWait(self.__driver, 10)
                          .until(EC.visibility_of_element_located((
                             By.CSS_SELECTOR, "input[type='password']"))))
        password_field.send_keys(password)

        # Находим и кликаем кнопку "Войти" для завершения авторизации
        submit_button = self.__driver.find_element(
            By.XPATH, "//div[contains(@class, 'cursor-pointer')"
            " and contains(text(), 'Войти')]")
        submit_button.click()
