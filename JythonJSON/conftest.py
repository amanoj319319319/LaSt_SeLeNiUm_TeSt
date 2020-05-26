'''
import pytest
import json
from selenium import webdriver
from JythonJSON.test_readjson import *
#with open('browser.json') as json_file:
#    data = json.load(json_file)
@pytest.fixture(scope="class")
def setup(request):
    for p in data['browser']:
        browser_name=p['name']
        print(browser_name)
        if browser_name=="Firefox":
            driver=webdriver.Chrome()
        elif browser_name=="Chrome":
            driver=webdriver.Firefox()
#        else:
#            browser_name=="Ie"
#            driver=webdriver.Ie()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(6)

        request.cls.driver = driver

        yield driver
        driver.close()

'''

'''
import pytest
import json
from selenium import webdriver
from JythonJSON.test_readjson import *

@pytest.fixture(scope="class")
def setup(request):
   browsers=["Chrome","Firefox"]
   length=len(browsers)
   i=0
   while i<=length:
      browser_name=(browsers[i])
      i+=1
      if browser_name=="Chrome":
          driver=webdriver.Chrome()
      elif browser_name=="Firefox":
          driver=webdriver.Firefox()

      driver.get("https://learn.letskodeit.com/p/practice")
      driver.maximize_window()
      driver.implicitly_wait(6)

      request.cls.driver = driver

      yield driver
      driver.close()
'''

import pytest
import json
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
   driver_array = []
   driver_array.append(webdriver.Chrome())
   driver_array.append(webdriver.Firefox())
   for driver in driver_array:
      driver.maximize_window()
      driver.get('https://learn.letskodeit.com/p/practice')
      driver.implicitly_wait(6)
      request.cls.driver = driver
      yield driver
      driver.close()






