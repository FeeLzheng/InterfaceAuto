import os,sys
import readConfig
from datetime import datetime
import logging
import  threading

sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\InterfaceAuto\\common\\")


localReadConfig=readConfig.readConfig()

class Log:
    def __init__(self):
        prodir=readConfig.proDir
        resultPath=os.path.join(prodir,"result")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath=os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))

        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        """
        get logger
        :return:
        """
        return self.logger

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log




