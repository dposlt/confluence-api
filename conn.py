import configparser, getpass

def readIniFile():

    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config
    
    
def getUrl():
    url = readIniFile()['CONNECTOR']['url']
    return url

def getUser():
    user = readIniFile()['CONNECTOR']['user']
    return user


def getPass():
    passwd = getpass.getpass(prompt = f'Password for user: {getUser()} >: ', stream=None)
    return passwd



print(getPass())
