import time
from time import sleep

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    cart_page = CartPage(driver)
    cart_page.add_product()

    time.sleep(2)
    cart_count = cart_page.get_cart_count()
    assert cart_count == "1"
    time.sleep(2)

def test_check_products_in_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")


    cart_page = CartPage(driver)
    cart_page.add_product()

    time.sleep(2)
    cart_page.open_cart()
    time.sleep(2)

    cart_items = cart_page.is_product_in_cart()
    assert len(cart_items) > 0, "No products in cart"