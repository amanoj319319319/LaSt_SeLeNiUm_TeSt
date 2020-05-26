#The below one is not a perfect scenario of model popup
#sometimes when you open any webpages you come across some chat boxes right like chat with me
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.redbus.com/")
driver.maximize_window()
driver.implicitly_wait(6)

frame=driver.find_element_by_xpath("//div[@id='popup']/div/div[2]").click()

#First try with alert to know whether itis a alert or not
#First try with frame to know whether the element is presented in a frame or not