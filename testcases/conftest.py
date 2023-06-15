
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ChromeOptions, Chrome
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    #driver=webdriver.Chrome(ChromeDriverManager().install())
    if browser=='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("---Launching the Edge browser----")
        driver.implicitly_wait(5)
        return driver
    elif browser=='firefox':
        driver =webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) # This statement vary for selenium Version 3
        print("...Launching FireFox Browser..")
        driver.implicitly_wait(5)
        return driver
    elif browser=='chrome':
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = Chrome(chrome_options=opts)
        print("...Launching chrome browser...")
        driver.implicitly_wait(5)
        return driver
    else :
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = Chrome(chrome_options=opts)
        print("...Launching chrome browser...")
        driver.implicitly_wait(5)
        return driver
    
def pytest_addoption(parser): # This will get the value from CLI/hooks..
    parser.addoption("--browser")

@pytest.fixture() # This will return the Browser value to setup method..
def browser(request):
    return request.config.getoption("--browser")

########################## pytest HTML Report###################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Karthik C N'
    
# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+".\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    


