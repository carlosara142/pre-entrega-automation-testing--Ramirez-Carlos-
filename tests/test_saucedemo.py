from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login( driver ):
    login(driver , "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    
def test_catalogo_productos( driver ):
    login(driver , "standard_user", "secret_sauce")
   
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"  

    #validar productos
    productos = driver.find_element(By.CSS_SELECTOR, 
    "[data-test='inventory-item']")
    assert len(productos) > 0
    nombre = productos[0].find_element(By.CLASS_NAME,"inventory-item-name").text
    assert nombre == "Sauce Labs Backpack"
       
def test_agregar_al_carrito( driver):
    login(driver , "standard_user", "secret_sauce")
    wait = WebDriverWait(driver , 10)

    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #agregar productos al carrito
    btn_agregar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
    btn_agregar.click()

    #validar contador del carrito

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    #validar nombre del producto en el carrito
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto

def test_menu_hamburguesa( driver):
    login(driver , "standard_user", "secret_sauce")
    wait = WebDriverWait(driver , 10)

    btn_hamburguesa = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
    btn_hamburguesa.click()
    #validar opciones del menu
    wait = WebDriverWait(driver , 10)

    opciones = wait.until(EC.element_to_be_clickable((By.ID, "inventory_sidebar_link")))
    opciones.click()
    


    

    
    
    