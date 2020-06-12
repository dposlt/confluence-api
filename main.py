from atlassian import Confluence
import conn, os

def conflu():
    confluence = Confluence(url = conn.getUrl(),
                        username = conn.getUser(),
                        password = conn.getPass())

    #confluence.page_exists('1260453923','MP')
    #usr = confluence.get_space('MP', expand='description.plain,homepage')

    return confluence

def checkName(space,title):
    conflu().page_exists(space,title)


def spaceInfo(key):
    info = conflu().get_space(key, expand='description.plain,homepage')
    return info


def createPage():
    conflu().create_page('MP','TEST','','1332818238')
    #print(f'create page --> {title}')

def getData(data):

    os.chdir(data)
    print(os.getcwd())

    for d in os.listdir('.'):
        if os.path.isfile(d):
            #print(f'FILE -> {d}\n')
            return d
        if os.path.isdir(d):
            os.chdir(d)
            #print(f"DIRECTORY {d} -> {os.listdir('.')}\n")
            return d
            os.chdir('../')
    #getData(conn.getData())

if __name__ == '__main__':
    #print(spaceInfo('MP'))
    #createPage(conn.getKey(), getData(conn.getData('pathWSS')),  '1332818238')
    #getData(conn.getData('pathWSS'))
    #createPage()


    




