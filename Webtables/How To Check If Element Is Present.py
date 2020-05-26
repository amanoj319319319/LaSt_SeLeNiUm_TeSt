'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class ElementPresentCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)


    def isElementPresent(self):
        try:
            element = self.driver.find_element_by_id("name")
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self):
        try:
            elementList = self.driver.find_elements(By.ID,"name")
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

ff = ElementPresentCheck()
ff.isElementPresent()
'''

#It works very fine
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://letskodeit.teachable.com/pages/practice"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(baseUrl)

try:
    element = driver.find_element_by_id("name")
    if element is not None:
        print("Element Found")
    else:
        print("Element not found")
except:
    print("Element not found")

print ("********************************************************")

try:
    elementList = driver.find_elements(By.ID, "name")
    print (elementList[0].text)
    if len(elementList) > 0:
        print("Element Found")
    else:
        print("Element not found")

except:
    print("Element not found")


