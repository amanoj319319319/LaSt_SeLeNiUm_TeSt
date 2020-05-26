from selenium import webdriver
from Test178.login_page import LoginPage
import unittest
import pytest
import time
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearFields()
        self.lp.login("a.manoj16@gmail.com", "319319319")
        result1 = self.lp.verifyLoginSuccessful()
        assert result1 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result2 = self.lp.verifyLoginFailed()
        assert result2 == True


#(Robot) C:\Users\Manoj\PycharmProjects\ManojPracticePageTwo>py.test -v -s C:\Users\Manoj\PycharmProjects\ManojPracticePageTwo\Tests178\l
#ogin_tests.py --browser=chrome
