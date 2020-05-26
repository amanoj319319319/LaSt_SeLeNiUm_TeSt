import time
from selenium import webdriver
from JSON.JsonFileTest import *
if  browser== "Chrome":
    driver=webdriver.Chrome()
elif browser == "Firefox":
    driver=webdriver.Firefox()
else:
    browser == "ie"
    driver=webdriver.Ie()

driver.get(fb_url)
driver.maximize_window()
driver.implicitly_wait(6)

user_name=driver.find_element_by_id("email").send_keys(user_name)
pass_word=driver.find_element_by_id("pass").send_keys(pass_word)
time.sleep(5)
login=driver.find_element_by_xpath("//*[@id='u_0_b']").click()

print ("You have reached to the facebook homepage.In this test you have used INI file to feed the data to the web elements")
