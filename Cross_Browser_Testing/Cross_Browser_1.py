'''
from selenium import webdriver

import time
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
#desired_cap=DesiredCapabilities()
#desired_cap = {
#'browserName': 'Chrome',
#'platform': 'Windows 8.1',
#}

#username="Manoj"
#password="319319319"
#api_session=requests.Session()
#api_session.auth(username,password)

caps = {}
caps['browserName'] = 'chrome'
caps['platform'] = 'WIN8'



node_url="http://localhost:4444/grid/wd/hub"
time.sleep(6)
driver=webdriver.Remote(desired_capabilities=caps,command_executor='http://localhost:4444/wd/hub')

driver.get("https://learn.letskodeit.com/p/practice")
driver.implicitly_wait(6)
print ("Title of the page is:-",driver.title)
driver.find_element_by_id("name").send_keys("Manoj")
time.sleep(5)
'''


#it works very fine
#Cross browser testing and then selenium grid parellel execution
'''
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = {}
caps['browserName'] = 'chrome'
caps['platform'] = 'WIN8'

node_url="http://localhost:4444/wd/hub"

time.sleep(6)
driver=webdriver.Remote(desired_capabilities=caps,command_executor='http://localhost:4444/wd/hub')

driver.get("https://learn.letskodeit.com/p/practice")
driver.implicitly_wait(6)
print ("Title of the page is:-",driver.title)
driver.find_element_by_id("name").send_keys("Manoj")
time.sleep(5)

'''