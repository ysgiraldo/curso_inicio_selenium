import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')
        
        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2)
