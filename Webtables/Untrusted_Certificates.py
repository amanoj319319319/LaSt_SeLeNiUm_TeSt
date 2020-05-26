#it is for chrome
'''
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://cacert.org/')

driver.close()
'''

#it is for firefox
'''
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://cacert.org/')

driver.close()
'''

#it is for IE
'''
from selenium import webdriver

capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
capabilities['acceptSslCerts'] = True

driver = webdriver.Ie(capabilities=capabilities)
driver.get('https://cacert.org/')

driver.close()

'''