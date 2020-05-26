from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "103.250.148.82:6666"
prox.ssl_proxy = "103.250.148.82:6666"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)
driver.get("https://www.facebook.com/")

time.sleep(5)
driver.close()