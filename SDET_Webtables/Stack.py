#It is working very very fine
#at this moment i loggined with google account
#i have to purchase this browser stack for one month
#https://automate.browserstack.com/dashboard/v2/builds/57ffe7c9b57a0a93f70a3d79ca1d4bbd8ef92eaa/sessions/fa6df92ab90fd5e9caa30c09b203cecdbc8e7630
#watch video in sdet chananel
'''
from queue import Queue
from threading import Thread
from selenium import webdriver
import time

USERNAME = "amanoj1"
API_KEY = "S2VtYupjGW9ZjR8MDCiD"

q = Queue(maxsize=0)

browsers = [
  {'browser': 'Firefox','browser_version': '57.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Pole'},
{'browser': 'Chrome','browser_version': '79.0',
 'os': 'Windows',
 'os_version': '8.1',
 'resolution': '1024x768',
 'name': 'Bstack-[Python] Length'}
]

# put all of the browsers into the queue before pooling workers
for browser in browsers:
    q.put(browser)

num_threads = 10

def test_runner(q):
    while q.empty() is False:
        try:
            browser = q.get()
            driver = webdriver.Remote(
                command_executor='https://amanoj1:S2VtYupjGW9ZjR8MDCiD@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=browser)

            driver.get("https://learn.letskodeit.com/p/practice")
            driver.maximize_window()
            driver.implicitly_wait(6)
            driver.find_element_by_id("name").send_keys("Manoj")
            print("Title of the page is:-", driver.title)
            time.sleep(5)
        except Exception as e:
            print(e)
        finally:
            driver.quit()
            time.sleep(15)
            q.task_done()


for i in range(num_threads):
    worker = Thread(target=test_runner, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()

'''
