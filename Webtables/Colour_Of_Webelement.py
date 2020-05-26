from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://en-gb.facebook.com/login/")
time.sleep(5)
size=driver.find_element_by_id("loginbutton").value_of_css_property('font-size')
ele_colour=driver.find_element_by_id("loginbutton").value_of_css_property('background-color')
colour=driver.find_element_by_id("loginbutton").value_of_css_property('color')
print ("back ground colour of element is:-",ele_colour)
print ("size of element is:-",size)
print ("color of element is:-",colour)



