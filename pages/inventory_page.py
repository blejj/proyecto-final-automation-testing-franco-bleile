from selenium.webdriver.common.by import By

class InventoryPage:

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(*self.BACKPACK).click()

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK).click()

    def open_cart(self):
        self.driver.find_element(*self.CART).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text