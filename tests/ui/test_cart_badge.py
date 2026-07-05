from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_cart_badge(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.add_backpack()
    
    assert inventory.get_cart_count() == "1"