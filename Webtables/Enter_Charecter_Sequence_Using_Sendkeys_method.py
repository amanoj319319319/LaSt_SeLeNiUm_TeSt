#Different ways of entering Character Sequence using SendKeys in Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(6)
que=driver.find_element_by_xpath("//input[@name='q']")

#First way using List data structure i can do it , i can do it with using .append() method also
'''
l1=["Java"," ","Interview"," ","Questions"]
que.send_keys(l1)
que.submit()
'''
#Second way using tuple data structure i can do it , but i can not apprend any words using tuple methods as tuple doesnt have ,
#append method why because tuple is a immutable object
l1=("Java"," ","Interview"," ","Questions")
que.send_keys(l1)
que.submit()
