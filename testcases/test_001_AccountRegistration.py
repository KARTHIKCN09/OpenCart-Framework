import time
from selenium import webdriver
from PageObjects.AccountRegistrationPage import AccountRegistrationPage
from PageObjects.HomePage import HomePage
import utilities.randomString 
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_AccountRegistration:
    baseURL=ReadConfig.getApplicationURL()

    logger=LogGen.loggen()
    def test_account_reg(self,setup):
        self.logger.info("*** test_001_AccountRegistration started****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("****Launching the application*****")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("Clicking on MyAccount--> Register")
        self.hp.clickMyAccount()

        self.hp.clickRegister()
        self.logger.info("Providing customer details for registration")
        self.regPage=AccountRegistrationPage(self.driver)
        self.regPage.setFirstName("John")
        self.regPage.setLastName("Canedy")
      # self.regPage.setEmail("abc0890@gmail.com")
        self.email=utilities.randomString.random_string_generator()+"@gmail.com"
        self.regPage.setEmail(self.email)
        self.regPage.setPassword("abcxyz")
        self.regPage.clickSubscribe()
        self.regPage.clickAgreeCheckBox()
        self.regPage.clickContinueBtn()
        self.confmsg=self.regPage.getConfirmationmsg()
        print(self.confmsg)
        if self.confmsg=="Privacy Policy":
            self.logger.info(":::Account Registration is passed::::")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"\\test_account_reg.png")
            #self.driver.save_screenshot("C:\\KARTHIK C N\\OpenCart-Framework\\Screenshots\\test_account_reg.png")
            assert False

        self.logger.info("*** test_001_AccountRegistration Finished****")

