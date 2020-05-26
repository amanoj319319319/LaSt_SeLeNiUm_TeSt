from selenium import webdriver
import time
import threading
import unittest
#class Multithreading(unittest.TestCase):
def chrom():
    driver=webdriver.Chrome()
    driver.get("https://learn.letskodeit.com/p/practice")
    driver.maximize_window()
    driver.implicitly_wait(6)
    driver.find_element_by_id("name").send_keys("Manoj")
    time.sleep(5)

def firfo():
    driver1=webdriver.Firefox()
    driver1.get("https://learn.letskodeit.com/p/practice")
    driver1.maximize_window()
    driver1.implicitly_wait(6)
    driver1.find_element_by_id("name").send_keys("Anki")
    time.sleep(5)
#m=Multithreading()
t1=threading.Thread(target=chrom)
t2=threading.Thread(target=firfo)
t1.start()
t2.start()

