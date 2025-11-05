from page.AuthPage import AuthPage


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("zainullinbd@gmail.com", "kokcJKE1993")
