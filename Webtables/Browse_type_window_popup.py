from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BrowseTypeWindowPopup():
    def Browse_Choose_TypePopup(self):
        driver=webdriver.Chrome()
        driver.get("http://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.switch_to.frame(0)
        #driver.switch_to.frame(name)
        #driver.switch_to.frame(numbers)
        driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D:\\Manoj.jpg")
        time.sleep(5)
        # switch back to parent frame
        driver.switch_to.default_content()

b=BrowseTypeWindowPopup()
b.Browse_Choose_TypePopup()