from atlassian import Confluence
import conn, os, const, setLog
import requests

#configparser
import timer
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
    confluence.page_exists(space,title)


def spaceInfo(key):
    info = confluence.get_space(key, expand='description.plain,homepage')
    return info

def removerPage(page_id):
    confluence.remove_page(page_id, status=None, recursive=False)


def createPage(page_space, page_title, parent_id):
    confluence.create_page(space=page_space, title=page_title, body='Plné znění migrovaného předpisu naleznete v PDF souboru v příloze.', parent_id=parent_id)
    print(f'create page --> {page_title} ')

def get_page_id(space, title):
    if confluence.page_exists(space, title):
        return confluence.get_page_id(space, title)
    else:
        print('page doesnt exists')
    #print(f'create page --> {title}')

def getData(data, id):
    start = timer.start()
    os.chdir(data)
    #print(os.getcwd())
    status_update = []
    count = 0
    for d in os.listdir('.'):
        if os.path.isfile(d):

            cut_end = d[:-4]

            if confluence.page_exists(const.SPACE_KEY,cut_end):
                page_id = get_page_id(const.SPACE_KEY, cut_end)
                print(f'--> skipping file {cut_end} <-- ')
                setLog.setLog(f'page {cut_end} with id {page_id} already exist ==> skipping')
                continue

            createPage(const.SPACE_KEY, cut_end,id)
            upload_file(d, get_page_id(const.SPACE_KEY, cut_end), d)
            print(f'upload file {d} to page {d}')
            count += 1

            status_update.append(get_page_id(const.SPACE_KEY, cut_end))
            #set_page_status(get_page_id(const.SPACE_KEY, cut_end))


        if os.path.isdir(d):

            if id == const.PARENT_ID_WSS:
                cut_end = 'WSS_' + d
            else:
                cut_end = 'WHB_' + d


            if confluence.page_exists(const.SPACE_KEY,cut_end):
                print(f'--> skipping directory {cut_end} <-- ')
                setLog.setLog(f'page {cut_end} already exist == skipping')
                continue
            else:

                createPage(const.SPACE_KEY, cut_end, id)
                status_update.append(get_page_id(const.SPACE_KEY, cut_end))
                count += 1


                os.chdir(d)
                for f in os.listdir('.'):

                    page_id = get_page_id(const.SPACE_KEY, cut_end)
                    upload_file(f, page_id, f)
                    print(f'upload file {f} to page {d}')
                    '''
                    if confluence.page_exists(const.SPACE_KEY,cut_end):
                        print(f'--> skipping {cut_end} <-- ')
                        setLog.setLog(f'page {cut_end} with id {page_id} already exist')
                        continue
                    createPage(const.SPACE_KEY, cut_end, '',page_id)
                    set_page_status(get_page_id(const.SPACE_KEY, cut_end))
                    `'''
                os.chdir('../')

    for i in status_update:
        print(f'set status for created pages id {i}')
        set_page_status(i)
    stop = timer.stop()

    print(timer.total(start, stop))
    print(f'celkově vytvořeno {count} stránek')

def set_page_status(page_id):
    data = {}
    url = confluence_url + const.cw_status_endpoint.format(page_id)
    data['name'] = 'Zveřejněno'
    data['comment'] = 'Status updated by migration script'
    return requests.put(url=url, json=data, auth=(confluence.username, confluence.password))

def upload_file(pdf_file, page_id, title):
    confluence.attach_file(pdf_file, name=None, content_type=None, page_id=page_id, title=title, space=None, comment='migrate content')


if __name__ == '__main__':
    #removerPage(const.PARENT_ID_WHB)
    getData(const.PATH_WHB, const.PARENT_ID_WHB)
    #print(spaceInfo(const.SPACE_KEY))
    #createPage(const.SPACE_KEY, const.NAME_WHS,const.SPACE_ID)
    #createPage(const.SPACE_KEY, const.NAME_WSS, const.SPACE_ID)
    #pageid = get_page_id(const.SPACE_KEY, const.NAME_WHS)
    #print(pageid)
    #createPage(const.SPACE_KEY, '1 01 2018 KVK_Řídicí a kontrolní systém', '', const.PARENT_ID_WHB)
    #confluence.clean_all_caches()
    #upload_file(r'C:\Users\212437054\Documents\projects\confluence-api\data\WHB\1 01 2013 PER_Kodex chování skupiny WW_4.pdf', '1335197823','file')
    #confluence.attach_content('Pavel', name=None, content_type='application/pdf', page_id='1335197846', title='tst pdf', space=const.SPACE_KEY, comment=None)



