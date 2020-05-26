from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class key():
    def key_method(self):
        url="https://letskodeit.teachable.com/"
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        Login=driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a")
        Login.click()
        time.sleep(6)

        user_name=driver.find_element_by_xpath("//*[@id='user_email']")
        user_name.send_keys('keys.ENTER')

        password=driver.find_element_by_xpath("//*[@id='user_password']")
        password.send_keys('keys.ENTER')

        submit=driver.find_element_by_xpath("//*[@id='new_user']/div[3]/input")
        submit.click()
        time.sleep(5)
k=key()
k.key_method()
