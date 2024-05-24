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
    message_button = "//span[contains(@title,'Messaging')]"
    meassage_search_Input = "//input[@placeholder='Type a name or multiple names']"
    click_sayantan = "(//div[contains(@class,'msg-connections-typeahead__entity-description')])[1]"
    message_send_button ="//button[normalize-space()='Send']"
    search_input= "//input[@placeholder='Search']"



    def __init__(self,driver):
        self.driver = driver

    def SignIn(self ):
        self.driver.find_element(By.XPATH,self.sign_in_button).click()

    def GiveInput(self,email,password):
        self.driver.find_element(By.XPATH, self.email_input).send_keys(email)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH,self.account_signin_button).click()
        time.sleep(3)

    def Message(self,name):
        self.driver.find_element(By.XPATH,self.message_button).click()
        self.driver.find_element(By.XPATH,self.meassage_search_Input).send_keys(name)



        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,self.click_sayantan)))
        element.click()
        time.sleep(2)


        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,self.message_send_button)))
        element.click()

        print("message is sent")





