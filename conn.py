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
    #passwd = getpass.getpass(prompt = f'Password for user: {getUser()} >: ', stream=None)
    passwd = readIniFile()['CONNECTOR']['passwd']
    return passwd

def getSpace():
    space = readIniFile()['SPACE']['id']
    return space


def getPage():
    page = readIniFile()['SPACE']['page']
    return page

def getKey():
    key = readIniFile()['SPACE']['key']
    return key

def getParentId(id):
    parentID = readIniFile()['SPACE'][id]
    return parentID

def getData(p):
    data = readIniFile()['DATA'][p]
    return data

