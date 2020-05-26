from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Alliframes():

    def iframe(self):
        driver=webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        iframes=(driver.find_elements(By.TAG_NAME,"iframe"))
        print (iframes)
        size=len(iframes)
        print (size)
        print ("Total no of iframes are :-",size)
        for elem in iframes:
            print(elem.get_attribute("src"))
a=Alliframes()
a.iframe()