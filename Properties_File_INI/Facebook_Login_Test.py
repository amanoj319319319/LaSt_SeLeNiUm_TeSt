'''
from selenium import webdriver
from Properties_File_INI.INI_File import *

if browser_name == "chrome":
    driver=webdriver.Chrome()
elif browser_name == "firefox":
    driver=webdriver.Firefox()
else:
    browser_name == "ie"
    driver=webdriver.Ie()

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(6)

user_name=driver.find_element_by_id(username_text_id).send_keys(user_name)
pass_word=driver.find_element_by_id(password_text_id).send_keys(pass_word)
login=driver.find_element_by_xpath("//*[@id='u_0_b']").click()

print ("You have reached to the facebook homepage.In this test you have used INI file to feed the data to the web elements")
'''

from selenium import webdriver
from Properties_File_INI.INI_File import *

if browser_name == "chrome":
    driver=webdriver.Chrome()
elif browser_name == "firefox":
    driver=webdriver.Firefox()
else:
    browser_name == "ie"
    driver=webdriver.Ie()

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(6)

user_name=driver.find_element_by_id(username_text_id).send_keys(user_name)
pass_word=driver.find_element_by_id(password_text_id).send_keys(pass_word)
login=driver.find_element_by_xpath("//*[@id='u_0_b']").click()

print ("You have reached to the facebook homepage.In this test you have used INI file to feed the data to the web elements")
