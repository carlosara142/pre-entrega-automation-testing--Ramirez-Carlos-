from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker("es_AR")

class CheckoutPage:

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETION_MESSAGE = (By.CLASS_NAME, "complete-header")


    def __init__(self, driver):
        self.driver = driver

    def agregar_producto(self):
        self.driver.find_element(*self.ADD_TO_CART).click()
    
    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_ICON).click()
    
    def iniciar_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def completar_formulario(self):
        #llamar a los metodos que necesitemos para completar el formulario de checkout
        first_name = fake.first_name()
        last_name = fake.last_name()
        postal_code = fake.postcode()

        print(f"Datos generados para el formulario: {first_name} {last_name} {postal_code}")

        #con esto anda perfecto tendriamos que agregar ,usuario dentro de la fucion para que tome los datos del usuario que le pasamos desde el test
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continuar_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finalizar_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def obtener_mensaje_completado(self):
         self.driver.find_element(*self.COMPLETION_MESSAGE).click()
         
        # Lógica para agregar un producto al carrito
        
