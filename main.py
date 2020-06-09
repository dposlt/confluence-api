from atlassian import Confluence
import conn

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

if __name__ == '__main__':
    #checkName(conn.getSpace(),conn.getPage())
   
    print(spaceInfo(conn.getKey()))
    

    




