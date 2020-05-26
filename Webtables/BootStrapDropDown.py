
#HOW TO HANDLE BOOTSTRAP DROPDOWN/DROPBOX
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.jquery-az.com/boots/demo.php?ex=63.0_2")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]/div/span/div/button/span").click()
elements=driver.find_elements(By.XPATH,"//ul[contains(@class,multiselect-container)]//li//a//label")
size=len(elements)
print ("Total no of childrens under ul tag are:-",size)

for i in range(size+1):
    print ("text of element is:-",elements[i].text)
    if elements[i].text == "Angular":
        elements[i].click()
        break
'''


'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.jquery-az.com/boots/demo.php?ex=63.0_2")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[3]/div/span/div/button/span").click()
elements=driver.find_elements(By.XPATH,"//ul[contains(@class,multiselect-container)]//li//a//label")
size=len(elements)
print ("Total no of childrens under ul tag are:-",size)

for i in range(size+1):
    print ("text of element is:-",elements[i].text)
    elements[i].click()
'''


