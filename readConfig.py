import os
import configparser

proDir=os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(proDir,"config.ini")



class readConfig():

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value






