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

def getSpace():
    space = readIniFile()['SPACE']['id']
    return space


def getPage():
    page = readIniFile()['SPACE']['page']
    return page

def getKey():
    key = readIniFile()['SPACE']['key']
    return key

def getParentId():
    parentID = readIniFile()['SPACE']['parent_id']
    return parentID

def getData():
    data = readIniFile()['DATA']['path']
    return data
