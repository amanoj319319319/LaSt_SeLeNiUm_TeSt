import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    browser="chrome"
    if browser == "chrome":
       driver = webdriver.Chrome() #if not added in PATH
    elif browser == "firefox":
       driver = webdriver.Firefox()
    else:
       driver = webdriver.Ie()

    driver.get("https://learn.letskodeit.com/p/practice")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")