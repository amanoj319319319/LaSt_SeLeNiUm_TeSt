from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

baseUrl = "https://letskodeit.teachable.com/pages/practice"
driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get(baseUrl)
time.sleep(4)

try:
    print("Waiting for maximum :: " + str(10) +
          " :: seconds for element to be clickable")
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5,
                         ignored_exceptions=[NoSuchElementException,
                                             ElementNotVisibleException,
                                             ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable((By.ID,"namefbdbgbgb")))
    print("Element appeared on the web page")

except Exception as e:
    print("Element not appeared on the web page")


