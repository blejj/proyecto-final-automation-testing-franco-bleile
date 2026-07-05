import pytest

from pages.login_page import LoginPage
from utils.data_reader import load_users


@pytest.mark.parametrize("usuario", load_users())
def test_login(driver, usuario):

    login = LoginPage(driver)

    login.open()

    login.login(
        usuario["username"],
        usuario["password"]
    )

    if usuario["resultado"] == "OK":
        assert "inventory" in driver.current_url
    else:
        assert "Username and password do not match" in login.get_error()