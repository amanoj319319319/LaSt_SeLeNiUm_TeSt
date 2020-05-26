import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("https://letskodeit.teachable.com/")
        driver.maximize_window()
        time.sleep(3)
    #Locaters
    __Login = '//*[@id="navbar"]/div/div/div/ul/li[2]/a'
    __email = "user_email"
    __password = "user_password"
    __enter = "//*[@id='new_user']/div[3]/input"
    __practice = '//*[@id="navbar"]/div/div/div/ul/li[1]/a'
    def test_Login(self):
        loginbutton = driver.find_element(By.XPATH, self.__Login)
        loginbutton.click()
        time.sleep(3)
        email=driver.find_element(By.ID, self.__email)
        email.send_keys("a.manoj16@gmail.com")
        passw=driver.find_element(By.ID, self.__password)
        passw.send_keys("319319319")
        enter=driver.find_element(By.XPATH, self.__enter)
        enter.click()
        time.sleep(3)

    def test_practice(self):
        practice = driver.find_element(By.XPATH, self.__practice)
        practice.click()
        time.sleep(3)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()





