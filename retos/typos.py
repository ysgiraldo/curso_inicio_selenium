import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Typos').click()

    def test_add_remove(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text # Nosotros queremos es el texto
        print(text_to_check)
        
        # Variable de control
        tries = 1 # Número de intentos
        found = False # Definir si lo hemos encontrado o no
        correct_text = "Sometimes you'll see a typo, other times you won't."

        # Estará cargando nuevamente la página hasta que el texto sea igual al correcto
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True
        
        self.assertEqual(found, True)
        print(f"Se encontró el texto después de {tries} intentos")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)