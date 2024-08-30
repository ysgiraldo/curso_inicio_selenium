import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_add_remove(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        # Espere 15 segundos hasta que el elemento pueda ser clickeado y vamos a indicar el elemento por medio del CSS_SELECTOR
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_button.click()

        # Esta es una espera explicita, esperará hasta que el elemento sea clickeable
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
        # enable_disable_button.click()

        # Identificamos el textbox
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        # Ahora que ya está habilitado podemos enviar un texto
        text_area.send_keys("Platzi")

        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)