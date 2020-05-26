from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Login_page import LoginPage
from Environment_variables.Common_variables import Common
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        cm = Common()
#        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(cm.baseURL)

        lp = LoginPage(driver)
        lp.login(cm.user_name, cm.password)


        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")