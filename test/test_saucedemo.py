
from utils.helpers import login


def test_login(driver):
    login(driver, "standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url
#definir catalogo de productos  
