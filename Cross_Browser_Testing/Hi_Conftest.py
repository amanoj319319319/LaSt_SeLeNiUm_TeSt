#working very fine
'''
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome() #if not added in PATH
    driver.get("https://learn.letskodeit.com/p/practice")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield driver
    driver.close()
'''

#https://www.seleniumeasy.com/python/webdriver-tests-in-pytest-using-fixtures-and-conftest
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    browser_name="chrome"
    if browser_name == "chrome":
       driver = webdriver.Chrome() #if not added in PATH
    elif browser_name == "firefox":
       driver = webdriver.Firefox()
    else:
       driver = webdriver.Ie()

    driver.get("https://learn.letskodeit.com/p/practice")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield driver
    driver.close()
