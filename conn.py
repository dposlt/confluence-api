import configparser

class Connector:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('setting.ini')

    def confUrl(self):
        url = self.config['CONNECTOR']['url']
        return url

    def confUser(self):
        user = self.config['CONNECTOR']['user']
        return user

    def confPass(self):
        passwd = self.config['CONNECTOR']['passwd']
        return passwd

    def getData(self):
        data = self.config['DATA']['url']
        return data


c = Connector()
print(c.confUrl())
print(c.confUser())
print(c.confPass())
print(c.getData())
