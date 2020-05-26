'''
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "user_email")
        emailField.send_keys(username)

        passwordField = self.driver.find_element(By.ID, "user_password")
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.NAME, "commit")
        loginButton.click()

'''



# 1st way .........
'''
from selenium.webdriver.common.by import By

class Loginpage():

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        username = self.driver.find_element(By.ID,"email")
        username.send_keys("a.manoj16@gmail.com")

        password = self.driver.find_element(By.ID,"pass")
        password.send_keys("santhuji")

        login = self.driver.find_element_by_xpath("//*[@id='u_0_b']")
        login.click()

'''

from selenium.webdriver.common.by import By

class Loginpage():

    def __init__(self, driver):
        self.driver = driver
    #Locaters
    __username="email"
    __password="pass"
    __login="//*[@id='u_0_b']"

    def getEmailtextvalue(self):
        return self.driver.find_element(By.ID,self.__username)
    def getPasswordtextvalue(self):
        return self.driver.find_element(By.ID,self.__password)
    def getLoginlinkvalue(self):
        return self.driver.find_element(By.XPATH,self.__login)

    def enterEmailtextfield(self):
        self.getEmailtextvalue().send_keys("a.manoj16@gmail.com")
    def enterPasswordtextfield(self):
        self.getPasswordtextvalue().send_keys("santhuji")
    def clickLoginbuttonfield(self):
        self.getLoginlinkvalue().click()

    def login(self):
        self.enterEmailtextfield()
        self.enterPasswordtextfield()
        self.clickLoginbuttonfield()












