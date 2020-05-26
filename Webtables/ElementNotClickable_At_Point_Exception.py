from selenium import webdriver
import time

driver=webdriver.Chrome()
url="https://login.yahoo.com/config/login?.src=fpctx&.intl=in&.lang=en-IN&.done=https://in.yahoo.com"
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_id("persistent").click()
print ("checkbox waas clicked")