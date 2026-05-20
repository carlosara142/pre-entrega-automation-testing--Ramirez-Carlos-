# Proyecto de pre entrega de pagina SauceDemo
"https://www.saucedemo.com/"

# Datos personales
    Autor: Carlos Ramirez
    Email: carlosara142@gmail.com

# El propósito del proyecto es validar el correcto funcionamiento de la página web asignada mediante el uso de las herramientas tecnológicas Pytest, Selenium y pytest-html. Se debe validar el inicio de sesión, el menú de la página, el catálogo de productos y su validación, así como la capacidad de agregar productos al carrito correctamente, validando el contador y el nombre de dicho artículo. Dentro de la carpeta de capturas se encuentra evidencia de resultados de test fallidos y excitosos.

# instalacion mediante terminal
 - pip instal requirements.txt

# Comando del terminal para ejecutar todas las pruebas
pytest -v

# Rutas para pruebas unitarias en el termianl #

# Validar el login
pytest tests/test_saucedemo.py::test_login -v

# Test de catalogo de productos y validar productos
pytest tests/test_saucedemo.py::test_catalogo_productos -v

# test de agregar productos al carrito, validar contador del carrito y validar nombre del producto en el carrito

pytest tests/test_saucedemo.py::test_agregar_al_carrito -v

inventory_sidebar_link

# test de menu hamburguesa

pytest tests/test_saucedemo.py::test_menu_hamburguesa -v

# Generar reporte HTML
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html