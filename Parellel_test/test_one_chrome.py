from selenium import webdriver
import time
import pytest
import unittest
class test_chrome(unittest.TestCase):
    def test_method1(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("https://www.google.com/")


'''
#py.test -v -s path of file -n 2
#https://www.youtube.com/watch?v=Z-eg2t_zfg4
from selenium import webdriver
import time
import pytest
import unittest
class test_chrome(unittest.TestCase):
    def test_method1(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("https://www.google.com/")

    def test_method3(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get("https://www.facebook.com/")
'''