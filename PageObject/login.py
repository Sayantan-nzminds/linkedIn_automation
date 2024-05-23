import csv
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    sign_in_button = "//a[normalize-space()='Sign in']"
    email_input= "//input[@id='username']"
    password_input = "//input[@id='password']"
    account_signin_button = "//button[normalize-space()='Sign in']"
    search_input= "//input[@placeholder='Search']"



    def __init__(self,driver):
        self.driver = driver

    def SignIn(self ):
        self.driver.find_element(By.XPATH,self.sign_in_button).click()

    def GiveInput(self,email,password):
        self.driver.find_element(By.XPATH, self.email_input).send_keys(email)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH,self.account_signin_button).click()


    def Search(self,search):
        self.driver.find_element(By.XPATH,self.search_input).click().send_keys(search)



