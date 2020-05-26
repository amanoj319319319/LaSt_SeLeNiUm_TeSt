import unittest
from selenium import webdriver
import time
class Test(unittest.TestCase):
    def test_run(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://gmail.com")
        self.driver.implicitly_wait(5)

        login=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span")
        login.click()
        time.sleep(5)
        email_field=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div")

        actual_error=email_field.text
        expected_error="Enter an email or phone number"

        self.assertEqual(actual_error,expected_error,"actual error is not equal to expected error")
        self.assertTrue(actual_error == "Enter an email or phone number")
        print ("test_run is passed")

if __name__ == "__main__":
	unittest.main()





