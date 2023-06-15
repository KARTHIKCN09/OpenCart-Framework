import logging
import os
class LogGen():
    @staticmethod
    def loggen():
        #path=".\\Log\\automation.log"
        path=r'C:\KARTHIK C N\OpenCart-Framework\Log\automation.log'
        #path=os.path.abspath(os.curdir)+"\\Log\\"+"\\test_account_reg.log"
        logging.basicConfig(filename=path, format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%y %I:%M:%S %p',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
