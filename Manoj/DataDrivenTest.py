from selenium import webdriver
from selenium.webdriver.common.by import By
import Files.XLUtilities as xl
import time
import unittest

class Multipletests(unittest.TestCase):
    def test_multiple(self):
        url = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url)
        path = "C:\\Users\\Manoj\\PycharmProjects\\LastSeleniumTest\\Manoj\\laptop.xlsm"

#        login = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[2]/a")
#        login.click()
#        time.sleep(4)

        rows = xl.getRowcount(path, "Sheet1")
        login = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[2]/a")
        login.click()
        time.sleep(8)

        for r in range(1,rows+1):
#            login = driver.find_element(By.XPATH, "//*[@id='navbar']/div/div/div/ul/li[2]/a")
#            login.click()
#            time.sleep(8)

            user_name = xl.readData(path, "Sheet1", r, 1)
            pass_word = xl.readData(path, "Sheet1", r, 2)

            email = driver.find_element(By.ID, "user_email")
            email.clear()
            time.sleep(3)
            email.send_keys(user_name)
            passs = driver.find_element(By.ID, "user_password")
            passs.clear()
            time.sleep(3)
            passs.send_keys(pass_word)
            submit = driver.find_element(By.XPATH, "//*[@id='new_user']/div[3]/input")
            submit.click()
            time.sleep(4)

            if driver.title == driver.title:
                print ("test is passed")
                xl.writeData(path, "Sheet1", r, 3, "test passed")
                driver.back()
            else:
                print ("test is failed")
                xl.writeData(path, "Sheet1", r, 3, "test failed")


            time.sleep(5)


if __name__ == "__main__":
    unittest.main()