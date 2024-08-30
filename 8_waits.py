import unittest
from selenium import webdriver

#Herramienta para seleccionar elementos de la web con sus selectores
from selenium.webdriver.common.by import By
#Herramienta para hacer uso de las expected conditions y esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
#Importar esperar explicitas
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

class ExplicitWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_account_link(self): #Cuentas del sitio

        #Esperar 10 segundos hasta que se cumpla la funcion
        WebDriverWait(self.driver, 3).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self): #Creacion de nuevo usuario

        #Encontrar el elemento por el texto del enlace
        self.driver.find_element_by_link_text('ACCOUNT').click()
        # self.driver.find_element_by_link_text('ACCOUNT')

        #Hacer referencia a la cuenta
        my_account = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        #Referencia a crear una cuenta
        create_account = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account.click()

        #Verificacion de estado de pagina web
        WebDriverWait(self.driver, 3).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

if __name__ == "__main__":
    unittest.main(verbosity= 2)

"""
Más avanzado
"""

# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


# class ExplicitWaitTests(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls) -> None:
#         s = Service('./chromedriver')
#         cls.driver = webdriver.Chrome(service=s)

#         driver = cls.driver
#         driver.get('http://demo-store.seleniumacademy.com/')
#         driver.maximize_window()
#         driver.implicitly_wait(3)
    
#     def test_account_link(self):
#         WebDriverWait(self.driver, 10).until(
#                 lambda s: s.find_element(
# 			By.ID,
# 			'select-language'
# 			).get_attribute('length') == '3')
        
#         account = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located(
# 			(By.LINK_TEXT, 'ACCOUNT')
# 			)
#                 )
#         account.click()

#     def test_create_new_customer(self):
#         text = self.driver.find_element(
# 		By.LINK_TEXT,
# 		'ACCOUNT'
# 		)
        
#         my_account = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.LINK_TEXT, 'My Account'))
#                 )
#         my_account.click()

#         create_account_button = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT'))
#                 )
#         create_account_button.click()

#         WebDriverWait(self.driver, 10).until(
#                 EC.title_contains('Create New Customer Account')
#                 )

#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
