#Download file using firefox browser
#it works very fine
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BrowseTypeWindowPopup():
    def Browse_Choose_TypePopup(self):
        firefox_profilee=webdriver.FirefoxProfile()
        firefox_profilee.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain.application/pdf")
        firefox_profilee.set_preference("browser.download.manager.showWhenStarting",False)
        firefox_profilee.set_preference("browser.download.dir","C:\\Users\\Manoj\\Desktop\\Naveens CRM course")
        firefox_profilee.set_preference("browser.download.folderList",2)
        firefox_profilee.set_preference("pdfjs.disabled",True)
        driver=webdriver.Firefox(firefox_profile=firefox_profilee)

        driver.get("http://demo.automationtesting.in/FileDownload.html")
        driver.maximize_window()
        driver.implicitly_wait(5)

        Enter_data=driver.find_element_by_id("textbox").send_keys("python")
        time.sleep(5)

        generate_file=driver.find_element_by_xpath("//button[@id='createTxt']")
        generate_file.click()
        Download_link=driver.find_element_by_id("link-to-download").click()
        time.sleep(4)

b=BrowseTypeWindowPopup()
b.Browse_Choose_TypePopup()
'''
