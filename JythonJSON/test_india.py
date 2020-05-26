'''
import time
from selenium import webdriver
import unittest
import pytest
class test_india(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    @pytest.mark.run(order=2)
    def test_method1(self):
        driver=self.driver
        driver.get("https://www.google.com")
        print ("Title of the page is:-",driver.title)

    @pytest.mark.run(order=1)
    def test_method2(self):
        driver=self.driver
        driver.get("https://learn.letskodeit.com/p/practice")
        ele=driver.find_element_by_id("name").send_keys("Manoj")

    def tearDown(self):
        self.driver.close()
'''

import time
from selenium import webdriver
import unittest
import pytest
class test_india(unittest.TestCase):
    @pytest.yield_fixture(scope="module")
    def onetimesetUp(self):
        global driver
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        yield
        self.driver.close()

    @pytest.mark.run(order=2)
    def test_method1(self,onetimesetUp):
        driver.get("https://www.google.com")
        print ("Title of the page is:-",driver.title)

    @pytest.mark.run(order=1)
    def test_method2(self,onetimesetUp):
        driver.get("https://learn.letskodeit.com/p/practice")
        ele=driver.find_element_by_id("name").send_keys("Manoj")


