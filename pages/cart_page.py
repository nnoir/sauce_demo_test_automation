from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_car_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shopping_car_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.shopping_car_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_item = (By.CLASS_NAME, "cart_item")

    def add_product(self):
        self.driver.find_element(*self.add_to_car_button).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.shopping_car_badge).text

    def open_cart(self):
        self.driver.find_element(*self.shopping_car_link).click()

    def is_product_in_cart(self):
        cart_items = self.driver.find_elements(*self.cart_item)
        return cart_items

