#working very fine
'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        ele=self.driver.find_element_by_id("name")
        ele.send_keys("Test Python")
        time.sleep(5)

    def test_hide(self):
        ele2=self.driver.find_element_by_id("displayed-text")
        ele2.send_keys("Hai Manoj")
        time.sleep(5)

'''

#working very fine
'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    @pytest.mark.run(order=2)
    def test_title(self):
        ele=self.driver.find_element_by_id("name")
        ele.send_keys("Test Python")
        time.sleep(5)
        print("The title of the page is:-", self.driver.title)

    @pytest.mark.run(order=1)
    def test_hide(self):
        ele2=self.driver.find_element_by_id("displayed-text")
        ele2.send_keys("Hai Manoj")
        time.sleep(5)
        print ("The title of the page is:-",self.driver.title)
'''
#How to run it on the console
#pytest -v -s C:\Users\Manoj\PycharmProjects\LastSeleniumTest\Single_Ton_Pattern_Class\test_exampleOne.py


#working very fine

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
@pytest.mark.usefixtures("setup")
class TestExampleOne(unittest.TestCase):
    @pytest.mark.run(order=2)
    def test_title(self):
        ele=self.driver.find_element_by_id("name")
        ele.send_keys("Test Python")
        time.sleep(5)
        print("The title of the page is:-", self.driver.title)

    @pytest.mark.run(order=1)
    def test_hide(self):
        ele2=self.driver.find_element_by_id("displayed-text")
        ele2.send_keys("Hai Manoj")
        time.sleep(5)
        print ("The title of the page is:-",self.driver.title)

        hide_button=self.driver.find_element_by_id("hide-textbox")
        hide_button.click()
        text_box=self.driver.find_element_by_id("displayed-text")
        print ("is hide-button displayes:-",text_box.is_displayed())
        self.driver.refresh()

    @pytest.mark.run(order=3)
    def test_another(self):
        self.driver.get("https://letskodeit.teachable.com/")
        login=self.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a")
        login.click()
        time.sleep(6)
        print ("Title of the facebook page is:-",self.driver.title)

