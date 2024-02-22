import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\USER\PycharmProjects\ArnabNew\confignew\confignew.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
