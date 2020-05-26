from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
driver.implicitly_wait(4)
element=driver.find_element_by_id("name")
driver.refresh()
element.send_keys("Manoj")
time.sleep(4)
driver.close()

'''
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
driver.implicitly_wait(4)
driver.refresh()
element=driver.find_element_by_id("name")
element.send_keys("Manoj")
time.sleep(4)
driver.close()
'''