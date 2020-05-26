#https://www.edureka.co/community/53559/how-get-all-options-dropdown-using-python-selenium-webdriver
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
class Test(unittest.TestCase):
    def test_run(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://learn.letskodeit.com/p/practice")
        self.driver.implicitly_wait(5)

        time.sleep(4)
#        element = self.driver.find_elements(By.XPATH,"//input[contains(@id,'carselect') and contains(@name,'cars')]")
        select_box = self.driver.find_element_by_id("carselect")

        list1=[]
        list2=[]

        options = [x for x in select_box.find_elements_by_tag_name("option")]
        for element in options:
            list1.append(element.get_attribute("value"))
        print (list1)

        for i in list1:
            list2.append(i)

        self.assertTrue(list1 == list2)
        print("test is passed")



if __name__ == "__main__":
	unittest.main()

