#https://www.youtube.com/watch?v=PjDQ_MIL8JI&list=PLhW3qG5bs-L9JjtXx-adxWdbjaxeRhi7h&index=15
#open chrome browser , click on more tools, clik on extensions , search for Katalon recorder , Click on Add it to chrome


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Udemy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_udemy(self):
        driver = self.driver
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.find_element_by_id("carselect").click()
        Select(driver.find_element_by_id("carselect")).select_by_visible_text("Benz")
        driver.find_element_by_id("carselect").click()
        driver.find_element_by_xpath("//input[@id='bmwcheck']").click()
        driver.find_element_by_id("benzcheck").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Manoj")
        driver.find_element_by_id("displayed-text").click()
        driver.find_element_by_id("displayed-text").clear()
        driver.find_element_by_id("displayed-text").send_keys("Hai")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

