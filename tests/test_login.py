from pages.login_page import LoginPage
#from data.users import USER
from utils.helpers import load_user_csv, load_user_jason
import pytest
from faker import Faker #pip install faker

load_csv = load_user_csv("data/users.csv")
load_json = load_user_jason("data/users.json")
fake = Faker()

#al final de carga del csv o json, se puede usar la lista de usuarios para parametrizar el test de login
@pytest.mark.parametrize("username, password", load_json)
def test_login(driver, username, password  ):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    
    name = fake.name() #nombre completo
    first_name = fake.first_name() #primer nombre
    last_name = fake.last_name() #apellido
    email = fake.email() #correo electronico
    codigo_postal = fake.postalcode() #codigo postal

    print("DATOS GENERADOS POR FAKER:", name, first_name, last_name, email, codigo_postal)
    