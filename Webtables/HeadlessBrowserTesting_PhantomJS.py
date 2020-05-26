from selenium import webdriver
import time
driver=webdriver.PhantomJS(executable_path="C:\\Users\\Manoj\\Desktop\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get("https://letskodeit.teachable.com/")
driver.maximize_window()
driver.implicitly_wait(6)
print ("Before :-",driver.title)
practice=driver.find_element_by_xpath("/html/body/header/div/div/div/div/ul/li[1]/a")
practice.click()
time.sleep(5)
driver.find_element_by_id("name").send_keys("Manoj")
print ("After :-",driver.title)



