from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class multiple_browser():

    def BrowserPopup(self):
        driver=webdriver.Chrome()
        driver.get("https://in.bookmyshow.com/hyderabad")
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(5)
        print ("Title of the parent page is:-",driver.title)

        driver.find_element_by_id("wzrk-cancel").click()
        login=driver.find_element_by_id("preSignIn").click()
        time.sleep(4)

        login_popup=driver.find_element_by_id("iUserName").send_keys("8143335932")

        time.sleep(4)
m=multiple_browser()
m.BrowserPopup()
