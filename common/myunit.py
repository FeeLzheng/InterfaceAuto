import os
import unittest
from common import Log as Log

class MyUnit(unittest.TestCase):
    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name+"测试开始前准备")


    def tearDown(self):
        pass




