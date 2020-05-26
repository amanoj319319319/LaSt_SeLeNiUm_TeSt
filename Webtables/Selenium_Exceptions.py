#Example of ElementNotVisibleException
'''
from selenium import webdriver
import time

class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)


        # Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box
        dis=driver.find_element_by_id("displayed-text")
        dis.send_keys("manoj")

ff = HiddenElements()
ff.testLetsKodeIt()
'''

#NoSuchElementException
'''
Base: selenium.common.exceptions.WebDriverException

This exception can be imported as ‘from selenium.common.exceptions import NoSuchElementException’

This exception is raised or thrown when element could not be found.

There could many possible reasons for this exception to occur

Element locator is not correct
Page is not yet loaded
Element is not yet displayed on the screen at the time of the find operation

'''
#StaleElementReferenceException
'''
Base: selenium.common.exceptions.WebDriverException

This exception can be imported as ‘from selenium.common.exceptions import StaleElementReferenceException’

This exception is raised or thrown when a reference to an element is now “stale” – means that the element was available at the time of find operation but no longer appears on the DOM of the page while doing some operation.

There could many possible reasons for this exception to occur

The page is no longer the same or the page has been refreshed, since the element was located
The element may have been removed and re-added to the screen like relocation, since it was located
Element may have been inside a context which was refreshed
'''

#ElementNotVisibleException
'''
Base: selenium.common.exceptions.InvalidElementStateException

This exception can be imported as ‘from selenium.common.exceptions import ElementNotVisibleException’

This particular exception is raised or thrown when an element is present on the DOM, but it is not visible.

It occurs most commonly when trying to click or read text of an element that is hidden from view.
'''

#ElementNotInteractableException
'''
Base: selenium.common.exceptions.InvalidElementStateException

This exception can be imported as ‘from selenium.common.exceptions import ElementNotInteractableException’

This exception is raised or thrown when an element is present in the DOM but interactions with that element will hit another element

'''

#TimeoutException
'''
Base: selenium.common.exceptions.WebDriverException

This exception can be imported as ‘from selenium.common.exceptions import TimeoutException’

This exception is raised or thrown when a command does not complete with in time. Like with in implicit or explicit wait time specified.

For more exception details – Visit Here

Please provide your opinion on comments.

'''

# https://selenium-python.readthedocs.io/api.html   (please refer this url)

#https://www.youtube.com/watch?v=DJq1ZHMdw3E     (Naveens exceptions )
