from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def select_sort_option(self, visible_text):
        dropdown = self.driver.find_element(*self.sort_dropdown)
        Select(dropdown).select_by_visible_text(visible_text)

    def get_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$", "")) for price in price_elements]

    def name_za_elements(self):
        name_za_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [name.text for name in name_za_elements]
