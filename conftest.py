import pytest
import json
from selenium import webdriver


@pytest.fixture
def config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture
def browser(config):
    driver = webdriver.Edge()

    driver.implicitly_wait(config["test_settings"]["wait_time"])
    driver.maximize_window()

    yield driver

    driver.quit()
