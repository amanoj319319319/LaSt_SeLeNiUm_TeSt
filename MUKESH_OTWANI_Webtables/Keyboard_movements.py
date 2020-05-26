from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)

act=ActionChains(driver)

user_name=driver.find_element_by_id("email").send_keys("a.manoj16@gmail.com")
act.send_keys(Keys.TAB)
act.send_keys("santhuji").perform()
act.send_keys(Keys.TAB)
act.send_keys(Keys.ENTER).perform()

time.sleep(5)