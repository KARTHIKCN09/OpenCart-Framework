from selenium.webdriver.common.by import By
class LoginPage():
    txt_email_xpath="//input[@name='email']"
    txt_password_xpath="//input[@name='password']"
    link_ForgotPassword_xpath="//input[@name='password']/following-sibling::a"
    btn_login_xpath="//button[text()='Login']"

    def __init__(self,driver):
        self.driver=driver
    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
    
    

    