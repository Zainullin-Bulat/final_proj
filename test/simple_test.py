from selenium import webdriver
from page.MainPage import MainPage
from time import sleep


def test_first():
    browser = webdriver.Edge()
    browser.implicitly_wait(4)
    browser.maximize_window()

    auth_page = MainPage(browser)
    auth_page.go()

    sleep(5)
