# https://intellipaat.com/community/9329/python-disable-images-in-selenium-google-chromedriver

'''
from selenium import webdriver
option = webdriver.ChromeOptions()
chrome_prefs = {}
#The below three lines are given by chrome .. we should write as they said
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.flipkart.com/samsung-mobile-store?otracker=nmenu_sub_Electronics_0_Samsung")
driver.maximize_window()
driver.implicitly_wait(6)
'''


from selenium import webdriver
profile = webdriver.FirefoxProfile()
# 1 - Allow all images # 2 - Block all images # 3 - Block 3rd party images
profile.set_preference("permissions.default.image", 2)
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.flipkart.com/samsung-mobile-store?otracker=nmenu_sub_Electronics_0_Samsung")
driver.maximize_window()
driver.implicitly_wait(6)
