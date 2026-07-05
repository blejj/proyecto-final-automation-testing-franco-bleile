from selenium.webdriver.common.by import By

class CartPage:

    ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def is_empty(self):
        return len(self.driver.find_elements(*self.ITEMS)) == 0