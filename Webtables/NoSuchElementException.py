'''
In the code , mainly this type of exception will comes based on these three things .

1)Timing issues
2)Incorrect locator(value of an attribute) or type of locator(ex:-ID,CSS,XPATH,CLASSNAME)
3)Element is in iframe(without switching on iframe , if we try to find an element ,webdriver gives,
an exception called as NoSuchElementException)
'''

#RUNNING SELENIUM SCRIPTS AND DEBUGGING THEM USING PDB MODULE .
'''
from selenium import webdriver
import time
import pdb
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
pdb.set_trace()
driver.get("https://learn.letskodeit.com/p/practice")
ele=driver.find_element_by_id("nam")
ele.send_keys("a.manoj16@gmail.com")
'''