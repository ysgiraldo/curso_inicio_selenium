import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	
	def test_compare_products_removal_alert(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		# Como buena práctica se recomienda limpiar el texto que haya en los campos de busqueda
		search_field.clear()

		search_field.send_keys('tee') # Termino que queremos encontrar
		search_field.submit()

		driver.find_element_by_class_name('link-compare').click() # Agregar a la lista de comparación
		driver.find_element_by_link_text('Clear All').click()
		
		#creamos una variable para interactuar con el pop-up
		alert = driver.switch_to_alert()
		# alert = driver.switch_to.alert 
		#vamos a extraer el texto que muestra
		alert_text = alert.text

		#vamos a verificar el texto de la alerta
		self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
		
		alert.accept()

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes", report_name="prueba_alerts_pop-up"))

# Si sale algún error de "AttributeError: 'WebDriver' object has no attribute 'switch_to_alert'" esta es la solución
# Reemplazar esto
# alert = driver.switch_to_alert()

# Por esto
# alert = driver.switch_to.alert 