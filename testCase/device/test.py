import unittest
import paramunittest
import os
from common import Common
from common import myunit
import readConfig as readConfig
from common import configHttp
from common import Log as Log
import ddt


localConfigPath = readConfig.readConfig()
localxls = Common.get_xls("userCase.xlsx", "login")
print(localxls)
info = {}
print("输出helloworld!")


@ddt.ddt
class InterFace(unittest.TestCase):
    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()


    def tearDown(self):
        pass
    # @ddt.data(*localxls)
    # def test_01(self,data):
    #     self.case_name = data[0]
    #     self.method = data[1]
    #     self.devicekey = data[5]
    #     self.result = data[6]
    #     self.code = data[7]
    #     self.msg = data[8]
    #     print("chixing222" + self.case_name+ self.method+self.devicekey+self.result+self.code+self.msg )


if __name__ == "__main__":
    unittest.main()
