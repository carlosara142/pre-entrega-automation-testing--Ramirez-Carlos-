import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from data.users import USER
#from data.checkout_data import usuarios_checkout
import time
from utils.helpers import load_user_csv , load_user_jason

load_cvs=load_user_csv("data/users.csv")
load_jason=load_user_jason("data/users.json")


@pytest.mark.parametrize("username, password", load_jason)
#@pytest.mark.parametrize("checkout_data", usuarios_checkout)
#no se becesita el checkout_data porque ya generamos los datos de forma aleatoria con faker
def test_checkout(driver, username, password):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_al_carrito()
    checkout_page.iniciar_checkout()
    time.sleep(3)  # Espera para que se procese el formulario
    checkout_page.completar_formulario()
    checkout_page.continuar_checkout()
    checkout_page.finalizar_checkout()
    checkout_page.obtener_mensaje_completado()

    
