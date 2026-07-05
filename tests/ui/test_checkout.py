from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver):

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    driver.find_element("id", "checkout").click()

    checkout = CheckoutPage(driver)
    checkout.fill_information("Juan", "Perez", "1234")

    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_success_message() == "Thank you for your order!"