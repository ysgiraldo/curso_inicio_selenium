import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

class SearchTests(unittest.TestCase):
	def setUp(self):
		# self.driver = webdriver.Chrome(executable_path = r'.\chromedriver.exe')
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		# driver.get("http://demo.onestepcheckout.com")
		driver.get("http://demo-store.seleniumacademy.com/")

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		search_field.clear() #limpia el campo de búsqueda en caso de que haya algún texto. 
		
		search_field.send_keys('tee') #simulamos la escritura del teclado para poner "tee"
		search_field.submit() #envía los datos ('tee') para que la página muestre los resultados de "tee"
		
	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		
		search_field.send_keys('salt shaker') # escribimos 'salt shaker' en la barra de búsqueda
		search_field.submit() #envíamos la petición para obtener un resultados de búsqueda

		#hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
		products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#vamos a preguntar si la cantidad de resultados es igual a 1
		self.assertEqual(1, len(products))
		
	def tearDown(self):
		self.driver.quit()