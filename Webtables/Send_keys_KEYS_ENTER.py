'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(6)
que=driver.find_element_by_xpath("//input[@name='q']")
#First way ,, Below two are working fine
#que.send_keys("java interview questions",Keys.ENTER)
que.send_keys("java interview questions",Keys.RETURN)

#Second way ,, it is working fine
#que.send_keys("java interview questions")
#que.submit()

#Third way ,, it will not work
'''
#que.send_keys("java interview questions")
#que.click()
'''

'''

