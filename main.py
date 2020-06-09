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


def createPage(title):

    conflu().create_page(conn.getKey(),title,'', conn.getParentId())
    print('done create page')

def getData(data):

    os.chdir(data)
    print(os.getcwd())

    for d in os.listdir('.'):
        if os.path.isfile(d):
            print(f'file -> {d}')
        if os.path.isdir(d):
            os.chdir(d)
            print(f"{d} -> {os.listdir('.')}")

if __name__ == '__main__':
    #checkName(conn.getSpace(),conn.getPage())
   
    #print(spaceInfo(conn.getKey()))
    #createPage(getData(conn.getData()))

    getData(conn.getData())
    

    




