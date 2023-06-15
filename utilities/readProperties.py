import configparser
import os
# config=configparser.RawConfigParser()
# config.read(r'.\\configurations\\config.ini')
config=configparser.RawConfigParser()
#config.read(".\\configurations\\config.ini")
config.read(r'C:\KARTHIK C N\OpenCart-Framework\configurations\config.ini')
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common Info','baseURL')
        return url
    @staticmethod
    def getUseremail():
        username=config.get('common Info','email')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common Info','password')
        return password
