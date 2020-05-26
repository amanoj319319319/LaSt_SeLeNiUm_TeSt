'''
import unittest
from selenium import webdriver
from Webtables.HighLightElements_2 import highlight
from time import sleep
class JSExe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.ufthelp.com/')

    def test_JSExe(self):
        driver = self.driver
        ele = driver.find_element_by_xpath("//a[contains(text(),'Home')]")
        highlight(ele)
        driver.get_screenshot_as_file("/home/rahul/PycharmProjects/Screenshots/highlight.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
'''

import unittest
from selenium import webdriver
from Webtables.HighLightElements_2 import highlight
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://learn.letskodeit.com/p/practice')
driver.implicitly_wait(6)
ele = driver.find_element_by_id("name")

highlight(ele)
#driver.get_screenshot_as_file("/home/rahul/PycharmProjects/Screenshots/highlight.png")

