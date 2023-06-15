from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class HomePage():
    #locators
    lnk_myaccount_xpath="//span[text()='My Account']"
    lnk_Register_xpath="//a[text()='Register']"
    lnk_login_linktext="Login"
    #constructor
    def __init__(self,driver):
         self.driver=driver
    #methods    
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()
    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_Register_xpath).click()
    def clickLogin(self):
         self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
         
            
