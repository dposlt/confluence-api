from atlassian import Confluence
import conn, os, configparser

config = configparser.ConfigParser()
config.read('settings.ini')

confluence_url = config['CONNECTOR']['url']
confluence_username = config['CONNECTOR']['user']
confluence_password = config['CONNECTOR']['passwd']
space_key = config['SPACE']['key']
root_page_id = config['SPACE']['local_id']


def conflu():

    confluence = Confluence(url = confluence_url,
                        username = confluence_username,
                        password = confluence_password)

    #confluence.page_exists('1260453923','MP')
    #usr = confluence.get_space('MP', expand='description.plain,homepage')

    return confluence


def checkName(space,title):
    conflu().page_exists(space,title)


def spaceInfo(key):
    info = conflu().get_space(key, expand='description.plain,homepage')
    return info


def createPage(page_space, page_title, body, parent_id):
    page_status = conflu().create_page(space=page_space, title=page_title, body=body, parent_id=parent_id)
    print(f'create page --> {page_title}')
    return page_status

    #print(f'create page --> {title}')

def getData(data):

    os.chdir(data)
    #print(os.getcwd())

    for d in os.listdir('.'):
        if os.path.isfile(d):
            print(d)
            conflu().create_page(space_key, d, '',root_page_id)
            print(f'create FILE -> {d}\n')

        if os.path.isdir(d):
            os.chdir(d)
            conflu().create_page(space_key, d, '', root_page_id)
            print(f"create DIRECTORY {d} -> {os.listdir('.')}\n")
            os.chdir('../')
    #getData(conn.getData())

if __name__ == '__main__':
    #print(conflu())
    #conflu().clean_all_caches()
    #conflu().create_page('MP','test','','1260453923')
    #conflu()
    #print(spaceInfo('MP'))
    #print(getData(conn.getData('pathWHB'))) #vrati jen jednu !!!

    #conflu().create_page(conn.getKey(),'1 01 2013 PER_Kodex chování skupiny WW_4.pdf','',conn.getParentId('parent_id_whb'))
    getData(conn.getData('pathWHB'))