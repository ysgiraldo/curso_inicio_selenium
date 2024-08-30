import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

def get_data(file_name):
    # Leyendo archivos csv
    rows = []
    data_file = open(file_name, "r") # Abrimos en modo lectura
    reader = csv.reader(data_file) 
    next(reader, None) # Saltar la primera fila

    for row in reader:
        rows.append(row)
    
    return rows


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(*get_data("testdata.csv"))
    @unpack # Desempaquetar estas duplas y puedan ser consultadas de forma individual

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count)              
        
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name("note-msg")
            self.assertEqual("Your search returns no results.", message.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)