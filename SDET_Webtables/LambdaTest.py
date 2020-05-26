from queue import Queue
from threading import Thread
from selenium import webdriver
import time

USERNAME = "a.manoj16"
API_KEY = "FUNMEYtiX52ffwJjAmSZ8FMyUIvLGjSHaY9HzqWbCzkmActIfu"

q = Queue(maxsize=0)

browsers = [
    {"build" : "your build name","name" : "LambdaChrome","platform" : "Windows 8.1","browserName" : "Chrome","version" : "79.0"
    },
{"build" : "your build name","name" : "LambdaFirefox","platform" : "Windows 10","browserName" : "Firefox","version" : "73.0"
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
                command_executor='https://a.manoj16:FUNMEYtiX52ffwJjAmSZ8FMyUIvLGjSHaY9HzqWbCzkmActIfu@hub.lambdatest.com/wd/hub',
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

