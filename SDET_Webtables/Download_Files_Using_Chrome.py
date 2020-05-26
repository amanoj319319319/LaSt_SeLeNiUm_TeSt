#Download a textfile
#working very fine
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
class BrowseTypeWindowPopup():
    def Browse_Choose_TypePopup(self):
        chrome_options=Options()
        chrome_options.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\Manoj\\Desktop\\Naveens CRM course"})
        driver=webdriver.Chrome(options=chrome_options)
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


