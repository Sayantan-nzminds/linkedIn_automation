import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.login import Login
from credential import email,password,search


class Test_Linkedin:
    baseURL = "https://www.linkedin.com"

    def test_01(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        test_page =Login(self.driver)
        test_page.SignIn()

        test_page.GiveInput(email,password)
        test_page.Message(name)



