'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Alllinks():

    def Link(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/")
        links=(driver.find_elements(By.TAG_NAME,"a"))
        print (links)
        size=len(links)
        print (size)
        print ("Total no of links are :-",size)
        for elem in links:
            print(elem.get_attribute("href"))
a=Alllinks()
a.Link()

'''

#working very fine
'''
from selenium import webdriver
import requests
import time
driver=webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/")
time.sleep(6)
links = driver.find_elements_by_tag_name("a")

print ("Links are:-",links)
size=len(links)
print ("Total no of links are:-",size)

for link in links:
  print(link.get_attribute("href"))
  print ("*******************************************")
  if (requests.head(link.get_attribute('href')).status_code == 200):
     print(link.get_attribute("href"), "  Valid link  ")
  else:
     print(link.get_attribute("href"), "  InValid link  ")
'''

'''
import requests
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://letskodeit.teachable.com/')
time.sleep(5)
links = driver.find_elements_by_tag_name("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(r.status_code == 200)
'''
#working very fine
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(6)
links = driver.find_elements_by_tag_name("a")

print ("Links are:-",links)
size=len(links)
print ("Total no of links are:-",size)

for link in links:
  print(link.get_attribute("href"))
  print ("*******************************************")
  if (requests.head(link.get_attribute('href')).status_code == 200):
     print(link.get_attribute("href"), "  Valid link  ")
  else:
     print(link.get_attribute("href"), "  InValid link  ")

'''

'''
One of the key test case is to find broken links on a webpage. Due to existence of broken links,
your website reputation gets damaged and there will be a negative impact on your business.
It’s mandatory to find and fix all the broken links before release.
If a link is not working, we face a message as 404 Page Not Found.

Let’s see some of the HTTP status codes.
200 – Valid Link
404 – Link not found
400 – Bad request
401 – Unauthorized
500 – Internal Error

Consider a test case to test all the links in the home page of “http://newtours.demoaut.com"
Below code fetches all the links of a given website (i.e., http://newtours.demoaut.com) using WebDriver commands and,
reads the status of each href link with the help of HttpURLConnection class.
'''