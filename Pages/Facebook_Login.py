from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get(baseURL)

        username=driver.find_element_by_id("email").send_keys("a.manoj16@gmail.com")
        password=driver.find_element_by_id("pass").send_keys("santhuji")
        login=driver.find_element_by_xpath("//*[@id='u_0_b']").click()

        print ("Title of the page is:-",driver.title)



