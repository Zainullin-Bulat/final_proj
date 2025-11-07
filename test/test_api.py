import requests
import allure
import pytest
import json
import os


def load_config():
    path = os.path.join(os.getcwd(), "config.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.api
@allure.feature("API Тесты YouGile")
class TestYouGileAPI:
    config = load_config()

    BASE_URL = config["api_base_url"]
    AUTH_TOKEN = f"Bearer {config['test_credentials']['api_key']}"
    USER_ID = config["test_credentials"]["user_id"]

    project_id = None
    board_id = None
    column_id = None
    task_id = None

    @classmethod
    def setup_class(cls):
        cls.session = requests.Session()
        cls.session.headers.update({
            "Authorization": cls.AUTH_TOKEN,
            "Content-Type": "application/json",
        })

    @allure.title("1. Создание проекта")
    def test_01_create_project(self):
        with allure.step("Готовим запрос на создание проекта"):
            url = f"{self.BASE_URL}/projects"
            payload = {"title": "Новый проект", "users":
                       {self.USER_ID: "admin"}}

        with allure.step("POST запрос"):
            response = self.session.post(url, json=payload)

        with allure.step("Проверка 201"):
            assert response.status_code == 201, response.text

        with allure.step("Сохраняем project_id"):
            TestYouGileAPI.project_id = response.json().get("id")
            assert self.project_id

    @allure.title("2. Изменение проекта")
    def test_02_update_project(self):
        with allure.step("Готовим запрос на изменение проекта"):
            url = f"{self.BASE_URL}/projects/{self.project_id}"
            payload = {"title": "Измененный проект"}

        with allure.step("PUT запрос"):
            response = self.session.put(url, json=payload)

        with allure.step("Проверка 200"):
            assert response.status_code == 200, response.text

    @allure.title("3. Создание доски")
    def test_03_create_board(self):
        with allure.step("Готовим запрос на создание доски"):
            url = f"{self.BASE_URL}/boards"
            payload = {
                "title": "Новая доска",
                "projectId": self.project_id,
                "stickers": {
                    "timer": False,
                    "deadline": True,
                    "stopwatch": True,
                    "timeTracking": True,
                    "assignee": True,
                    "repeat": True,
                },
            }

        with allure.step("POST запрос"):
            response = self.session.post(url, json=payload)

        with allure.step("Проверка 201"):
            assert response.status_code == 201, response.text

        with allure.step("Сохраняем board_id"):
            TestYouGileAPI.board_id = response.json().get("id")
            assert self.board_id

    @allure.title("4. Изменение доски")
    def test_04_update_board(self):
        with allure.step("Готовим запрос на изменение доски"):
            url = f"{self.BASE_URL}/boards/{self.board_id}"
            payload = {"title": "Обновленная доска"}

        with allure.step("PUT запрос"):
            response = self.session.put(url, json=payload)

        with allure.step("Проверка 200"):
            assert response.status_code == 200, response.text

    @allure.title("5. Создание колонки")
    def test_05_create_column(self):
        with allure.step("Готовим запрос на создание колонки"):
            url = f"{self.BASE_URL}/columns"
            payload = {"title": "Новая колонка", "boardId": self.board_id}

        with allure.step("POST запрос"):
            response = self.session.post(url, json=payload)

        with allure.step("Проверка 201"):
            assert response.status_code == 201, response.text

        with allure.step("Сохраняем column_id"):
            TestYouGileAPI.column_id = response.json().get("id")
            assert self.column_id

    @allure.title("6. Изменение колонки")
    def test_06_update_column(self):
        with allure.step("Готовим запрос на изменение колонки"):
            url = f"{self.BASE_URL}/columns/{self.column_id}"
            payload = {"title": "Обновленная колонка"}

        with allure.step("PUT запрос"):
            response = self.session.put(url, json=payload)

        with allure.step("Проверка 200"):
            assert response.status_code == 200, response.text

    @allure.title("7. Создание задачи")
    def test_07_create_task(self):
        with allure.step("Готовим запрос на создание задачи"):
            url = f"{self.BASE_URL}/tasks"
            payload = {"title": "Новая задача", "columnId": self.column_id}

        with allure.step("POST запрос"):
            response = self.session.post(url, json=payload)

        with allure.step("Проверка 201"):
            assert response.status_code == 201, response.text

        with allure.step("Сохраняем task_id"):
            TestYouGileAPI.task_id = response.json().get("id")
            assert self.task_id

    @allure.title("8. Изменение задачи")
    def test_08_update_task(self):
        with allure.step("Готовим запрос на Изменение задачи"):
            url = f"{self.BASE_URL}/tasks/{self.task_id}"
            payload = {"title": "Измененная задача"}

        with allure.step("PUT запрос"):
            response = self.session.put(url, json=payload)

        with allure.step("Проверка 200"):
            assert response.status_code == 200, response.text
