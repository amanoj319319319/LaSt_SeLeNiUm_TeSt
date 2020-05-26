'''
from selenium import webdriver
import time

class Selenium_Test():
    def __init__(self):
        self.setBrowser()
        self.setBrowserConfig()
        self.setFunctionality()
        self.setQuitBrowser()

#we have to set browser name value in setBrowser method
    def setBrowser(self):
        self.browser="Firefox"

#we have to configure properties of the browser file
    def setBrowserConfig(self):
        if self.browser=="Chrome":
            self.driver=webdriver.Chrome()
        elif self.browser=="Firefox":
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Ie()
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#we have to write test functionalities
    def setFunctionality(self):
        user_name=self.driver.find_element_by_id("email").send_keys("a.manoj16@gmail.com")
        pass_word=self.driver.find_element_by_id("pass").send_keys("santhuji")
        login=self.driver.find_element_by_xpath("//input[@id='u_0_b']").click()
        time.sleep(5)

##quit from the browser
    def setQuitBrowser(self):
        self.driver.close()

s=Selenium_Test()
'''


