import unittest
# Con unittest nos podemos traer todas nuestras pruebas
from pyunitreport import HTMLTestRunner
# Ayuda a orquestar cada una de las pruebas que estaremos ejecutando junto con los reportes
from selenium import webdriver
# Chrome Driver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
	    # Va a ejecutar todo lo necesario antes de empezar la prueba
        # cls.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
		# esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')
		
	# Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))