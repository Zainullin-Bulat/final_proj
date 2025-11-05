from selenium import webdriver
from page.MainPage import MainPage
from time import sleep


def first_test():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()

    main_page = MainPage(browser)
    main_page.go()

    sleep(5)