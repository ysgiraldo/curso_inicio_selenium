import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
# Service nos ayuda a declarar el executable_path() de nuestro webdriver. 
# Yo utilizo chrome pero deberias poder hacerlo con otro navegador. 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Search(unittest.TestCase):

    def setUp(self):

        # creamos una variable s con una funcion Service('') que contiene la ruta del webdriver. 
        s=Service(ChromeDriverManager().install())
        # cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        # driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_text_field(self):
        dsearch_field = self.driver.find_element(By.ID, "search")
        # Para encontrar el elemento

    def test_search_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_by_class(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button(self):
        search_button = self.driver.find_element(By.CLASS_NAME, "search-button")

    def test_search_banner_img(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banner = banner_list.find_elements(By.TAG_NAME, "img")
        self.assertEqual(3, len(banner))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(By.XPATH,"//*[@id='top']/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img")

    def test_icon_cart(self):
        icon_cart = self.driver.find_element(By.CSS_SELECTOR,"div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'search-test-report'))