import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_add_remove(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span') # //*[@id="table1"]/thead/tr/th[{i+1}]
            table_data[i].append(header.text)

            for j in range(4):
                # esto es para que la información llegue en columnas
                col_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(col_data.text)
                # esto es para que la información llegue en filas
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{j+1}]') 
                table_data[i].append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)