import time
import unittest
import pytest
from selenium import webdriver
driver_array = []

class MultiBrowsers(unittest.TestCase):
    def setUp(self):
        driver_array.append(webdriver.Chrome())
        driver_array.append(webdriver.Firefox())
        for driver in driver_array:
            driver.get("https://learn.letskodeit.com/p/practice")
            driver.maximize_window()
            driver.implicit_wait()


    def test_practice(self):
        self.driver.find_element_by_id("name").send_keys("Manoj")

    def test_google(self):
        print ("Title of the page is:-",self.driver.title)

    def tearDown(self):
        self.driver.close()


