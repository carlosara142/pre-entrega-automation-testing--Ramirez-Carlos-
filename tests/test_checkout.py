import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from data.users import USER
from data.checkout_data import usuarios_checkout
import time


@pytest.mark.parametrize("username, password", USER)
@pytest.mark.parametrize("checkout_data", usuarios_checkout)

def test_checkout(driver, username, password, checkout_data):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_al_carrito()
    checkout_page.iniciar_checkout()
    time.sleep(3)  # Espera para que se procese el formulario
    checkout_page.completar_formulario(checkout_data)
    
    checkout_page.continuar_checkout()
    checkout_page.finalizar_checkout()
    checkout_page.obtener_mensaje_completado()

    
