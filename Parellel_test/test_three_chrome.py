from selenium import webdriver
import time
import pytest
import unittest
class test_chrome(unittest.TestCase):
    def test_method1(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("https://www.facebook.com/")