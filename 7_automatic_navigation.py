import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("https://www.google.com/")

	def test_browser_navigation(self):
		driver = self.driver

		search_field = driver.find_element_by_name('q')
		search_field.clear()
		search_field.send_keys('platzi')
		search_field.submit()

		driver.back()# Retroceder navegador
		sleep(3) # Espera 3 segundos
		driver.forward() # Avanzar
		sleep(3) 
		driver.refresh() # Actualizar página
		sleep(3)


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="atomatizar_navegacion"))