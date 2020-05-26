from seleniumpagefactory.Pagefactory import PageFactory
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time

'''
class LoginPage(PageFactory):
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "Text_UserName": ('ID', 'email'),
        "Text_Password": ('ID', 'pass'),
        "Button_Login": ('XPATH', '//*[@id="u_0_b"]')}

    def Login(self):
        self.Text_UserName.set_text("a.manoj16@gmail.com")
        self.Text_Password.set_text("xyzxyzxyz")
        self.Button_Login.click_button()

'''

class LoginPage(PageFactory):
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver


    def email(self,Email):
        return self.driver.method_D1()



