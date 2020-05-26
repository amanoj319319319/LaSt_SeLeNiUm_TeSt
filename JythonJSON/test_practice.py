import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    @pytest.mark.run(order=2)
    def test_title(self):
        ele=self.driver.find_element_by_id("name")
        ele.send_keys("Test Python")
        time.sleep(5)
        print("The title of the page is:-", self.driver.title)

    @pytest.mark.run(order=1)
    def test_hide(self):
        ele2=self.driver.find_element_by_id("displayed-text")
        ele2.send_keys("Hai Manoj")
        time.sleep(5)
        print ("The title of the page is:-",self.driver.title)

'''
import json
data = {}
data['browser'] = []
data['browser'].append({
    'name': 'Chrome'
})
data['browser'].append({
    'name': 'Firefox'
})
data['browser'].append({
    'name': 'Ie'
})

with open('browsers.json', 'w') as outfile:
    json.dump(data, outfile)
'''
