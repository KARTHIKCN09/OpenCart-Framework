from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountRegistrationPage():
        #locators
        txt_firstname_xpath="//input[@name='firstname']"
        txt_lastname_xpath="//input[@name='lastname']"
        txt_email_xpath="//input[@name='email']"
        txt_password_xpath="//input[@name='password']"
        radioBtn_Subscribe_xpath="(//input[@type='radio'])[2]"
        check_agree_xpath="agree"
        btn_continue_xpath="//button[text()='Continue']"
        text_privacy_xpath="//a[text()='Privacy Policy']"
        
        #constructor
        def __init__(self,driver) :
            self.driver=driver
        #Methods
        def setFirstName(self,fname):
            self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)
        def setLastName(self,lname):
            self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)
        def setEmail(self,email):
            self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
        def setPassword(self,pwd):
            self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)
        def clickSubscribe(self):
            self.driver.find_element(By.XPATH,self.radioBtn_Subscribe_xpath).click()
        def clickAgreeCheckBox(self):
           # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,self.check_agree_xpath)))
           element= self.driver.find_element(By.NAME,self.check_agree_xpath)
           self.driver.execute_script ("arguments[0].click();",element)
        def clickContinueBtn(self):
            self.driver.execute_script ("arguments[0].click();", self.driver.find_element(By.XPATH,self.btn_continue_xpath))
        def getConfirmationmsg(self):
            try:
               return self.driver.find_element(By.XPATH,self.text_privacy_xpath).text
            except:
                None
