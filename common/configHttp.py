import os
import requests
import readConfig
from common.Log import MyLog as Log
import unittest
localConfigPath=readConfig.readConfig()


class ConfigHttp:
    global host, port, timeout, verson, token, appid
    host = localConfigPath.get_http("baseurl")
    port = localConfigPath.get_http("port")
    timeout = localConfigPath.get_http("timeout")
    verson = localConfigPath.get_http("verson")
    token = localConfigPath.get_http("token")
    appid = localConfigPath.get_http("appid")
    def __init__(self):

        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.params = {}
        self.data = {}
        self.url = None



    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param




    def set_url(self,case_name):
        self.url = host+":"+port+"/"+verson+"/"+appid+"/"+case_name

    def get_url(self):
        """
        set params
        :param param:
        :return:
        """
        return self.url

    def set_data(self,data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data


    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, params=self.params, timeout=float(timeout))
            # response.raise_for_status()
            print(response)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, data=self.data, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__=="__main__":
    unittest.main()