'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
desired_cap = {
 'browser': 'Chrome',
 'browser_version': '81.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor='https://amanoj1:S2VtYupjGW9ZjR8MDCiD@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_id("name").send_keys("Manoj")
print ("Title of the page is:-",driver.title)
time.sleep(5)
driver.quit()

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
desired_cap1 = {'browser': 'Chrome',
 'browser_version1': '80.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Very Simple Test'
}

desired_cap2 = {'browser_name': 'Firefox',
 'browser_version2': '55.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Very Simple Test'
}

desired_cap2.update(desired_cap1)

driver = webdriver.Remote(
    command_executor='https://amanoj1:S2VtYupjGW9ZjR8MDCiD@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap2)

driver.get("https://learn.letskodeit.com/p/practice")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_id("name").send_keys("Manoj")
print ("Title of the page is:-",driver.title)
time.sleep(5)
driver.quit()


'''
desired_cap1 = {'browser': 'Chrome',
 'browser_version1': '80.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Very Simple Test'
}

desired_cap2 = {'browser_name': 'Firefox',
 'browser_version2': '55.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Very Simple Test'
}


desired_cap2.update(desired_cap1)
print(desired_cap2)
'''