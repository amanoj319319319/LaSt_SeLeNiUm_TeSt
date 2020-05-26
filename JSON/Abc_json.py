'''
import json
from selenium import webdriver
with open('browser.json') as json_file:
    data = json.load(json_file)
    for p in data['browser']:
        browser_name=p['name']
        print(browser_name)

        if browser_name=="Chrome":
            driver=webdriver.Chrome()
        elif browser_name=="Firefox":
            driver=webdriver.Firefox()
#        else:
#            browser_name=="Ie"
#            driver=webdriver.Ie()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(6)

        ele=driver.find_element_by_id("name").send_keys("Manoj")

'''

'''
import json
with open('browser.json') as json_file:
    data = json.load(json_file)
    for p in data['browser']:
#        browser_name=p['name']
#        print(browser_name)
         print (p)

'''


import pytest
import json
from selenium import webdriver
with open('browser.json') as json_file:
    data = json.load(json_file)
@pytest.fixture(scope="class")
def setup(request):
    for p in data['browser']:
        browser_name=p['name']
        print(browser_name)
        if browser_name=="Chrome":
            driver=webdriver.Chrome()
        elif browser_name=="Firefox":
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

