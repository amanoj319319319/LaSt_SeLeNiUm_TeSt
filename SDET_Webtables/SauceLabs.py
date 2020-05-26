from queue import Queue
from threading import Thread
from selenium import webdriver
import time

USERNAME = "manoj319"
API_KEY = "2d769987-ad0e-463b-876b-fbe2e9b027b8"

q = Queue(maxsize=0)

browsers = [
    {'browserName': 'chrome','browserVersion': '81.0','platformName': 'Windows 8',
     'sauce:options': {'screenResolution': '1024x768',}
    },
{'browserName': 'firefox','browserVersion': '62.0','platformName': 'Windows 8',
  'sauce:options': {'screenResolution': '1024x768',
  }
}]

# put all of the browsers into the queue before pooling workers
for browser in browsers:
    q.put(browser)

num_threads = 10

def test_runner(q):
    while q.empty() is False:
        try:
            browser = q.get()
            driver = webdriver.Remote(
                command_executor='https://manoj319:2d769987-ad0e-463b-876b-fbe2e9b027b8@ondemand.saucelabs.com:443/wd/hub',
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

