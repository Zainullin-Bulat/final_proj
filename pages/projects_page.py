import json
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class ProjectsPage:
    def __init__(self, driver):
        self.driver = driver
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.wait = WebDriverWait(
            driver, self.config["test_settings"]["wait_time"])

        self.PROJECT_CARDS = (By.CSS_SELECTOR, "[data-testid='project-card']")
        self.PROJECT_TITLES = (
            By.CSS_SELECTOR, "[data-testid='project-title']")
        self.PROJECT_LIST_CONTAINER = (
            By.CSS_SELECTOR, "[data-testid*='project']")

    @allure.step("Переход в раздел 'Проекты компании'")
    def navigate_to_company_projects(self):
        company_button = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, "//div[text()='Моя компания']"))
        )
        company_button.click()

        self.wait.until(EC.presence_of_element_located(self.PROJECT_CARDS))

    @allure.step("Создание нового проекта")
    def create_new_project(self, project_name, create_chat=False):

        with allure.step("Переходим в проекты компании"):
            self.navigate_to_company_projects()

        with allure.step("Нажимаем кнопку 'Добавить проект'"):
            add_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, "//span[text()='Добавить проект с задачами']"))
            )
            add_button.click()

        with allure.step("Вводим название проекта"):
            name_field = self.wait.until(
                EC.element_to_be_clickable((
                    By.CSS_SELECTOR, "input[placeholder="
                    "'Введите название проекта…']"))
            )
            name_field.clear()
            name_field.send_keys(project_name)

        with allure.step("Убираем параметр 'Создать групповой чат'"):
            if not create_chat:
                chat_checkbox = self.wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//div[contains(@class, 'group/checkbox')]//"
                        "div[text()=""'Создать групповой чат проекта']"
                        "/preceding-sibling::div"
                    ))
                )
                chat_checkbox.click()

        with allure.step("Подтверждаем создание проекта"):
            confirm_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[@role='button' and .//div[text()="
                    "'Добавить проект с задачами']]"
                ))
            )
            confirm_button.click()

        with allure.step("Ждём закрытия диалога"):
            self.wait.until(EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "[role='dialog']")
            ))

        with allure.step("Ждём появления проекта в списке"):
            self.wait.until(lambda driver: len(self.get_project_names()) > 0)

    @allure.step("Получение списка проектов")
    def get_project_names(self):

        try:
            self.wait.until(EC.presence_of_element_located(self.PROJECT_CARDS))
            title_elements = self.driver.find_elements(*self.PROJECT_TITLES)

            names = []
            for element in title_elements:
                try:
                    text = element.text.strip()
                    if text:
                        names.append(text)
                except StaleElementReferenceException:
                    continue

            return names

        except Exception as e:
            print(f"Ошибка при получении названий проектов: {e}")
            return []
