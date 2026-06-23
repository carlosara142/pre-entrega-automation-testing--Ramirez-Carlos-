from pages.login_page import LoginPage
from data.users import USER
import pytest

@pytest.mark.parametrize("username, password", USER)
def test_login(driver, username, password  ):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    
   