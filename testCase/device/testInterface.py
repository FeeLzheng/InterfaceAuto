import unittest
import paramunittest
import os
from common import Common
from common import myunit
import readConfig as readConfig
from common.configHttp import ConfigHttp
from common import Log as Log
import ddt


localConfigPath = readConfig.readConfig()
localxls = Common.get_xls("userCase.xlsx", "login")
ConfigHttp =ConfigHttp()
info = {}


@paramunittest.parametrized(*localxls)
class InterFace(unittest.TestCase):

    def setUp(self):

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info(u'测试'+self.case_name)

    def tearDown(self):

        pass

    def setParameters(self, case_name, method,verson,appid,token, deviceKey, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param devicekey:
        :param verson:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.deviceKey = str(deviceKey)
        self.verson=str(verson)
        self.appid=str(appid)
        self.token=str(token)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)


    # @ddt.data(*localxls)
    def test_01(self):
        """
        :param case_name:
        :param method:
        :param token:
        :param devicekey:
        :param verson:
        :param result:
        :param code:
        :param msg:
        :return:
        """

        # set url
        print(self.case_name)
        ConfigHttp.set_url(self.case_name)
        self.url = ConfigHttp.get_url()
        print("第一步：设置url  " + str(self.url))

        # set params
        # set params
        data = {"deviceKey":self.deviceKey,"token":self.token}
        ConfigHttp.set_data(data)
        print(data)
        print("第二步：设置发送请求的参数")

        # test interface
        self.return_json = ConfigHttp.post()
        print(self.return_json)
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第三步：发送请求\n\t\t请求方法：" + method)

        # check result
        self.checkResult()
        print("第四步：检查结果")

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        # show return message
        Common.show_return_msg(self.return_json)

        if self.result == '0':
            email = Common.get_value_from_return_json(self.info, 'member', 'email')
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(InterFace("test_01"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
