'''
from selenium import webdriver
import time
import pytest

@pytest.mark.parametrize()
def test_login():
'''

'''
import pytest
import unittest
from ddt import ddt, unpack, data
from selenium import  webdriver
import time
@ddt
class Test_Class_1(unittest.TestCase):
    def setUp(scope="module"):
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)

    @data(("Ruby", "Cucumber"), ("Python", "Behave"))
    @unpack
    def test_1(self, switchname, hidename):
        switch = driver.find_element_by_id("name")
        switch.send_keys(switchname)
        time.sleep(3)
        switch.clear()

        hide = driver.find_element_by_id("displayed-text")
        hide.send_keys(hidename)
        time.sleep(3)
        hide.clear()

    def tearDown(scope="module"):
        driver.close()

if __name__ == "__main__":
    unittest.main()

'''

import pytest
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def test_driver_init(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.get("https://www.google.com")
    web_driver.maximize_window()
    web_driver.implicitly_wait(6)
    yield
    web_driver.close()