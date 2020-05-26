
from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from selenium import webdriver
import time
from Pages.Facebook_Login_page import Loginpage

class LoginTest(unittest.TestCase):
    #This test will going to be executed on chrome browser
    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(4)
        pglogin = Loginpage(driver)
        pglogin.login()
        time.sleep(4)
        driver.quit()

#if __name__ == "__main__":
#     unittest.main()









