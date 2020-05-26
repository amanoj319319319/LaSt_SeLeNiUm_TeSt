'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/")
driver.maximize_window()
driver.implicitly_wait(5)

act=ActionChains(driver)
practice=driver.find_element_by_css_selector("#navbar > div > div > div > ul > li:nth-child(1) > a")
act.double_click(practice).perform()

time.sleep(5)

#Edureka code for double click
from selenium.webdriver.common.action_chains import ActionChains

driver=self.webdriver
user = self.find_element_by_id("selUsers")
for option in user.find_elements_by_tag_name("option"):
   if option.text == "Admin, Ascender":
      actionChains = ActionChains(driver)
      actionChains.double_click(option).perform()
'''

#https://www.guru99.com/double-click-and-right-click-selenium.html
#Code for RightClick Action in selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/")
driver.maximize_window()
driver.implicitly_wait(5)

act=ActionChains(driver)
practice=driver.find_element_by_css_selector("#navbar > div > div > div > ul > li:nth-child(1) > a")
act.context_click(practice).perform()

time.sleep(5)