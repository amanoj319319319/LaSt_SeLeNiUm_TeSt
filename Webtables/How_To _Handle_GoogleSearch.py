'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(4)
que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("Software testing")
que.send_keys(Keys.RETURN) #it is for click enter key
#que.click()
'''
#IT WORKS VERY FINE .. PLEASE FOLLOW THIS CODE
#How to handle Dynamic Google Search
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(6)
que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("java")

element=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li/descendant::div[@class='sbl1']")
print ("Length of elements is:-",len(element))

for ele in range(0,len(element)+1):
    listitem=element[ele].text
    if listitem == "java tutorial":
        element[ele].click()
        break

'''


#we can do like this also ... compare to this code , above code is very nice to remember techmicaly
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(6)
que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("java")

java_tutorial=driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li[7]")
java_tutorial.click()

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(6)
que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("selenium")

element=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li/descendant::div[@class='sbl1']")
print ("Length of elements is:-",len(element))

for ele in range(0,len(element)+1):
    listitem=element[ele].text
    time.sleep(4)
    if listitem == "selenium interview questions":
        element[ele].click()
        break



