import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

class SearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_language(self):
        #el orden respeta como aparecen en la página
        exp_options = ['English','French', 'German']
        # Para almacenar las opciones que elijamos
        act_options = []

        #para acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))
        #para comprobar que si esté la cantidad de  opciones correcta
		#'options' permite ingresar directamente a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        #verifico que la lista de opciones disponibles y activas sean indénticas
        self.assertEqual(exp_options, act_options)

        #vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
        self.assertEqual('English',select_language.first_selected_option.text)

        #seleccionamos "German" por el texto visible
        select_language.select_by_visible_text('German')

        #verificamos que el sitio cambio a Alemán
		#preguntamos a selenium si la url del sitio contiene esas palabras
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output="reportes", report_name="prueba_asssert"))
