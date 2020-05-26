'''
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument("--disable-infobars");
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://learn.letskodeit.com/p/practice")
'''


#It works very well
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=chrome_options,)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://learn.letskodeit.com/p/practice")
