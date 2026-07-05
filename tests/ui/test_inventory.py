from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_agregar_producto(driver):

    login = LoginPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.open_cart()

    assert "cart" in driver.current_url