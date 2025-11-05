from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://shop.mts.ru/"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)
