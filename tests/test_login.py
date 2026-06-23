from pages.login_page import LoginPage
#from data.users import USER
from utils.helpers import load_user_csv, load_user_jason
import pytest

load_csv = load_user_csv("data/users.csv")
load_json = load_user_jason("data/users.json")

#al final de carga del csv o json, se puede usar la lista de usuarios para parametrizar el test de login
@pytest.mark.parametrize("username, password", load_json)
def test_login(driver, username, password  ):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    
   