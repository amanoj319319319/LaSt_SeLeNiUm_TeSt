from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages1.login_page import LoginPage
import unittest
import time
class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("a.manoj16@gmail.com", "319319319")
        time.sleep(4)
        driver.quit()

'''
        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
        driver.quit()

'''