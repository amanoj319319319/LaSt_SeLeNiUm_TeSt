#working with expedia.com
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.implicitly_wait(5)

flights_tab=driver.find_element_by_id("tab-flight-tab-hp").click()

departind_date=driver.find_element_by_id("flight-departing-hp-flight").click()

cal_month=driver.find_element_by_xpath("//*[@id='flight-departing-wrapper-hp-flight']/div/div/div[2]")

allvaliddates=cal_month.find_elements(By.TAG_NAME,"button")
time.sleep(4)

for date in allvaliddates:
    if "23" in date.text:
        date.click()
        break
'''

#working with goibibo.com
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.goibibo.com/")
driver.implicitly_wait(5)

departure=driver.find_element_by_id("departureCalendar").click()

calmonth=driver.find_element_by_xpath("//div[@id='searchWidgetCommon']/div[1]/div[1]/div[1]/div/div[5]/div/div")

all_available_dates=calmonth.find_elements(By.TAG_NAME,"div")

time.sleep(10)

for date1 in all_available_dates:
    if date1.text == "23":
        date1.click()
        break
'''


#working with makemytrip calender
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.makemytrip.com/flights/")
driver.implicitly_wait(5)

departure=driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/label").click()

calmonth=driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]")

all_available_dates=calmonth.find_elements(By.TAG_NAME,"div")


time.sleep(10)

for date1 in all_available_dates:
    if date1.text=="24":
        date1.click()
        break
'''


#Automating Date Picker In Selenium Webdriver in selenium
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://ui.freecrm.com/calendar")
driver.implicitly_wait(5)

email=driver.find_element_by_name("email").send_keys("a.manoj16@gmail.com")
password=driver.find_element_by_name("password").send_keys("319319319")
login=driver.find_element_by_xpath("//div[@id='ui']/div/div/form/div/div[3]").click()
time.sleep(4)

month="May 2020"
#april_month=driver.find_element_by_xpath("//div[@id='ui']/div/div[2]/div[2]/div/div[2]/div/div[2]/div")
while True:
    time.sleep(3)
    texti=driver.find_element_by_class_name("rbc-toolbar-label").text
    print (texti)
    if texti==month:
        break
    else:
        time.sleep(3)
        a="/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/span[1]/button[3]"
        driver.find_element_by_xpath(a).click()


may_month=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div")

all_available_dates=may_month.find_elements(By.TAG_NAME,"a")


time.sleep(10)

for date1 in all_available_dates:
    if date1.text=="24":
        date1.click()
        break

#//*[@id="ui"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/span[1]/button[3]/i
#/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div

'''






