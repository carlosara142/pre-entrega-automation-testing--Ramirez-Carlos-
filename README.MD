#Proyecto de pre entrega de pagina SauceDemo
"https://www.saucedemo.com/"

El proposito del protecto es validar el funcionamiento correcto de la pagina web asignada,
mediante el uso de las herramientas tecnologicas Pytes, Selenium y pytest-html. Se debe validar
el login, el menu de la pagina, catalogo de productos y su validacion, el poder agregar productos 
al carrito correctamente validando el contador y el nombre de dicho articulo.


#Datos
    Autor: Carlos Ramires
    DNI: 95933346
    Email: carlosara142@gmail.com

# instalacion
 - pip instal requirements.txt

#Rutas para pruebas unitarias en el termianl

# Validar el login
pytest tests/test_saucedemo.py::test_login -v

# Test de catalogo de productos y validar productos
pytest tests/test_saucedemo.py::test_catalogo_productos -v

# test de agregar productos al carrito, validar contador del carrito y validar nombre del producto en el carrito

pytest tests/test_saucedemo.py::test_agregar_al_carrito -v

inventory_sidebar_link

# test de menu hamburguesa

pytest tests/test_saucedemo.py::test_menu_hamburguesa -v