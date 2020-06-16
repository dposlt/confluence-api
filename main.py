from atlassian import Confluence
import conn, os, const, setLog
import requests

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
    confluence.create_page(space=page_space, title=page_title, body=body, parent_id=parent_id)
    print(f'create page --> {page_title} ')

def get_page_id(space, title):
    if confluence.page_exists(space, title):
        return confluence.get_page_id(space, title)
    else:
        print('page doesnt exists')
    #print(f'create page --> {title}')

def getData(data, id):

    os.chdir(data)
    #print(os.getcwd())

    for d in os.listdir('.'):
        if os.path.isfile(d):
            cut_end = d[:-4]
            if confluence.page_exists(const.SPACE_KEY,cut_end):
                page_id = get_page_id(const.SPACE_KEY, cut_end)
                print(f'--> skipping {cut_end} <-- ')
                setLog.setLog(f'page {cut_end} with id {page_id} already exist ==> skipping')
                continue

            createPage(const.SPACE_KEY, cut_end, '',id)
            set_page_status(get_page_id(const.SPACE_KEY, cut_end))


        if os.path.isdir(d):
            if confluence.page_exists(const.SPACE_KEY,d):
                print(f'--> skipping {d} <-- ')
                setLog.setLog(f'page {d} already exist == skipping')
                continue

            createPage(const.SPACE_KEY, d, '', id)
            set_page_status(get_page_id(const.SPACE_KEY, d))

            os.chdir(d)
            for f in os.listdir('.'):
                cut_end = f[:-4]
                page_id = get_page_id(const.SPACE_KEY, d)
                if confluence.page_exists(const.SPACE_KEY,cut_end):
                    print(f'--> skipping {cut_end} <-- ')
                    setLog.setLog(f'page {cut_end} with id {page_id} already exist')
                    continue
                createPage(const.SPACE_KEY, cut_end, '',page_id)
                set_page_status(get_page_id(const.SPACE_KEY, cut_end))

            os.chdir('../')

def set_page_status(page_id):
    data = {}
    url = confluence_url + const.cw_status_endpoint.format(page_id)
    print(url)
    data['name'] = 'Zveřejněno'
    data['comment'] = 'Status updated by migration script'
    return requests.put(url=url, json=data, auth=(confluence.username, confluence.password))

if __name__ == '__main__':
    #removerPage(const.PARENT_ID_WHB)
    getData(const.PATH_TST, const.PARENT_ID_WHB)
    #print(spaceInfo(const.SPACE_KEY))
    #createPage(const.SPACE_KEY, const.NAME_WHS,'',const.SPACE_ID)
    #createPage(const.SPACE_KEY, const.NAME_WSS, '', const.SPACE_ID)
    #pageid = get_page_id(const.SPACE_KEY, const.NAME_WHS)
    #print(pageid)
    #createPage(const.SPACE_KEY, '1 01 2018 KVK_Řídicí a kontrolní systém', '', const.PARENT_ID_WHB)
    #confluence.clean_all_caches()



