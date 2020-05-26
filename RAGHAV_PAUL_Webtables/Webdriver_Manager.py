from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
driver=webdriver.Firefox(GeckoDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://learn.letskodeit.com/p/practice")
driver.find_element_by_id("name").send_keys("Manoj")
time.sleep(5)
