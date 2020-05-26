'''
from selenium import webdriver
import pytest
import time
import unittest

class Testexample1():
    @pytest.yield_fixture()
    def test_setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/")
        driver.maximize_window()
        yield
        driver.close()

    a=10
    b=20

    def test_Login(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a").click()
        time.sleep(10)
        title_page=driver.title
        print (title_page)
        if title_page==driver.title:
            print ("hai test_login method has been executed successfully")
            assert True
        else:
            assert False

    #@pytest.mark.flaky(reruns=2)
    @pytest.mark.flaky(reruns=5, reruns_delay=5)
    def test_practice(self,test_setUp):
        driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a").click()
        time.sleep(10)
        title=driver.title
        print (title)
        assert title=="manoj"
        print ("hai test_login method has been executed successfully")
        a=10
        b=20
        print ("The addition of a and b is:-",(a+b))


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
