import time
from time import sleep

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_sort_by_lower_price(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    time.sleep(2)
    products_page.select_sort_option("Price (low to high)")
    time.sleep(2)
    prices = products_page.get_prices()

    assert prices == sorted(prices)

def test_sort_by_name_za(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)

    time.sleep(2)
    products_page.select_sort_option("Name (Z to A)")
    time.sleep(2)
    name = products_page.name_za_elements()

    assert name == sorted(name, reverse=True)