import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

class DynamicElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_add_remove(self):
        driver = self.driver

        options = [] # Una lista vacía que son las que aparecen en el menú
        menu = 5 # El menú tiene 5 opciones
        tries = 1 # Contará cuantos intentos le tomó
        
        while len(options) < 5:
            options.clear() # Limpiar los valores que hay en options

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a') # /html/body/div[2]/div/div/ul/li[{i + 1}]/a
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i + 1} is NOT FOUND")
                    tries += 1
                    driver.refresh()
        
        print(f"Finished in {tries} tries")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)