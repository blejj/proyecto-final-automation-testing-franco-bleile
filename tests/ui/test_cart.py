from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_eliminar_producto(driver):

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.remove_backpack()

    inventory.open_cart()

    cart = CartPage(driver)

    assert cart.is_empty()