from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

try:
    # Iniciar sesión
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    element = driver.find_element(By.ID, 'user-name')
    element.send_keys('standard_user')

    element = driver.find_element(By.ID, 'password')
    element.send_keys('secret_sauce')
    time.sleep(3)
    element.submit()
    print("Me logueé con éxito")

    # Click en el menú
    Menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    Menu_button.click()
    time.sleep(3)

    # Click en la X del menú
    Menu_button = driver.find_element(By.ID, "react-burger-cross-btn")
    Menu_button.click()
    time.sleep(3)

    # Encontrar el elemento dropdown por su XPATH
    dropdown = Select(driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select"))
    dropdown.select_by_value('lohi')
    time.sleep(3)

    # Encontrar el elemento logout
    Menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    Menu_button.click()
    time.sleep(3)
    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()

except Exception as e:
    print(f"Ocurrió un error: {e}")
    driver.quit()

# Cerrar el navegador una vez que se hayan seleccionado todas las opciones
time.sleep(10)
driver.close()
