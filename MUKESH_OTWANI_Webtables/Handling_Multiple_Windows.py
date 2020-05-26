from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class multiple_browser():

    def BrowserPopup(self):
        driver=webdriver.Chrome()
        driver.get("http://www.popuptest.com/goodpopups.html")
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(5)
        print ("Title of the parent page is:-",driver.title)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        first_link=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/font/b/a[1]").click()
        second_link=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/font/b/a[2]").click()
        third_link=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/font/b/a[3]").click()
        fourth_link=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/font/b/a[4]").click()

        all_windows=driver.window_handles
        print (all_windows)

        time.sleep(5)
        driver.switch_to.window(all_windows[3])
        driver.close()

        after_close_window=driver.window_handles
        print (after_close_window)



m=multiple_browser()
m.BrowserPopup()