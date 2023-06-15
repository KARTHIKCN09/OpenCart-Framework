import time
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    #path=os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsx"
    path=r"C:\KARTHIK C N\OpenCart-Framework\TestData\Opencart_LoginData.xlsx"

    
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_data Driven****")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')# Returns number of rows in a sheet.
        lst_status=[] #Empty list declaration to store the status.
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.hp=HomePage(self.driver)
        self.lp=LoginPage(self.driver)

        for r in range(2,self.rows+1): # range method will not consider last row thats y row+1 and 1st row is header thats y neglected.
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1) # First column data
            self.password=XLUtils.readData(self.path,"Sheet1",r,2) # second column data
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3) # Third column data

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            if self.exp=='Valid':
               lst_status.append('Pass')
            else:
                lst_status.append('Fail')
        self.driver.close()

        # Final Validation::::
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_DataDriven*****")











        
