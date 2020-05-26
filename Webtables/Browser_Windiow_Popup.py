'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Browser_Window_Popup():

    def BrowserPopup(self):
        driver=webdriver.Chrome()
        driver.get("http://www.popuptest.com/goodpopups.html")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td/font/b/a[3]").click()
        handler=list(driver.window_handles())
        print (handler)
        it=handler.__iter__()
        parent_window_id=it.__next__()
        print ("parent window id is:-",parent_window_id)
        child_window_id=it.__next__()
        print ("child window id is:-",child_window_id)

b=Browser_Window_Popup()
b.BrowserPopup()
'''
#1st way to handle browser window popup
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)

ff = SwitchToWindow()
ff.test()

'''

#1st way continuation
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

ff = SwitchToWindow()
ff.test()

'''
