import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("***** Starting test_002_login******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()
    
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        



    
