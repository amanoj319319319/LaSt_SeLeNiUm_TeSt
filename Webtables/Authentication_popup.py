'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Authentication_popup():

    def Authentication(self):
        driver=webdriver.Chrome()
        #username:-admin ,password:-admin ,after password after @ paste url of the site
        #url ;- http://the-internet.herokuapp.com/basic_auth
        driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(5)
        message=driver.find_element_by_xpath("//*[@id='content']/div/p").text
        print ("message is :-",message)

a=Authentication_popup()
a.Authentication()
'''


#DEBUGGING THE CODE BY PUTTING BREAK POINTS WITH THE HELP OF CURSOR
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pdb
class Authentication_popup():

    def Authentication(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        name="manoj"
        age=29
#        pdb.set_trace()
        print ("name is :-",name)
        print ("age is:-",age)
        message=driver.title
        print ("title  is :-",message)

a=Authentication_popup()
a.Authentication()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pdb
class Authentication_popup():
    driver=None
    def Authentication(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)
        name="manoj"
        age=29
#       pdb.set_trace()
        print ("name is :-",name)
        print ("age is:-",age)
        message=driver.title
        print ("title  is :-",message)

    def last(self):
        driver.quit()

a=Authentication_popup()
a.Authentication()
a.last()
'''
