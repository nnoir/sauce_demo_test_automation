

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_password")
    error = login_page.invalid_login()

    assert "Epic sadface: Username and password do not match any user in this service" in error


