'''
import json
from JythonJSON import *
# Opening JSON file
with open('C:\\Users\\Manoj\\PycharmProjects\\LastSeleniumTest\\JythonJSON\\browsers.json') as openfile:
    # Reading from json file
    data = json.load(openfile)
'''

#https://gist.github.com/devinmancuso/17f2f41599f55702fdb3
import self as self


#https://gist.github.com/devinmancuso/17f2f41599f55702fdb3    refer this
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# Define array to hold all drivers
driver_array = []

class PythonOrgSearchChrome(unittest.TestCase):

    def setUp(self):
#        chrome_options = webdriver.ChromeOptions()
        driver_array.append(webdriver.Chrome())
        driver_array.append(webdriver.Firefox())

    def test_search_in_python_chrome(self):
        # Loop through each driver in the array
        for driver in driver_array:
            driver.maximize_window()
            driver.get('https://learn.letskodeit.com/p/practice')
            driver.find_element_by_id('name').send_keys("Manoj")
            
    def tearDown(self):
        driver.close()

# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()
'''


'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# Define array to hold all drivers
driver_array = []

class PythonOrgSearchChrome(unittest.TestCase):

    def setUp(self):
#        chrome_options = webdriver.ChromeOptions()
        driver_array.append("Chrome")
        driver_array.append("Firefox")

    for browser in driver_array:
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://learn.letskodeit.com/p/practice')
        driver.implicitly_wait(6)

    def test_search_in_python_chrome(self):
        self.driver.find_element_by_id('name').send_keys("Manoj")
        

    def tearDown(self):
        self.driver.close()


# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()

'''


