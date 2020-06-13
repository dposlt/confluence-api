from atlassian import Confluence
import conn, os, const

#configparser

'''
config = configparser.ConfigParser()
config.read('settings.ini')

confluence_url = config['CONNECTOR']['url']
confluence_username = config['CONNECTOR']['user']
confluence_password = config['CONNECTOR']['passwd']
space_key = config['SPACE']['key']
root_page_id = config['SPACE']['local_id']
'''
confluence_url = const.URL
confluence_username = const.USER
confluence_password = const.PASSWD

confluence = Confluence(url = confluence_url,
                        username = confluence_username,
                        password = confluence_password)

    #confluence.page_exists('1260453923','MP')
    #usr = confluence.get_space('MP', expand='description.plain,homepage')


def checkName(space,title):
    conflu().page_exists(space,title)


def spaceInfo(key):
    info = confluence.get_space(key, expand='description.plain,homepage')
    return info

def removerPage(page_id):
    confluence.remove_page(page_id, status=None, recursive=False)


def createPage(page_space, page_title, body, parent_id):
    page_status = confluence.create_page(space=page_space, title=page_title, body=body, parent_id=parent_id)
    print(f'create page --> {page_title} -> page_status')

def get_page_id(space, title):
    confluence.get_page_id(space, title)
    #print(f'create page --> {title}')

def getData(data):

    os.chdir(data)
    #print(os.getcwd())

    for d in os.listdir('.'):
        if os.path.isfile(d):
            cut_end = d[:-4]
            createPage(const.SPACE_KEY, cut_end, '',const.PARENT_ID_WHB)


        if os.path.isdir(d):
            createPage(const.SPACE_KEY, d, '', const.PARENT_ID_WHB)
            os.chdir(d)
            for f in os.listdir('.'):
                cut_end = d[:-4]
                createPage(const.SPACE_KEY, cut_end, '', const.PARENT_ID_WHB)
            os.chdir('../')
    #getData(conn.getData())

if __name__ == '__main__':

    #getData(conn.getData('pathWHB'))
    print(get_page_id(const.SPACE_KEY, 'WSS'))
    #c = confluence.get_page_child_by_type(const.SPACE_ID, type='page', start=None, limit=None)
    #print(c)
