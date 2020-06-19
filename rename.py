######################################
##         RENAME ALL PDF FILES     ##
##         PREFIX WHB OR WSS        ##
######################################

import os, const

def rename_pdf(dir_name, pdf_prefix):

    os.chdir(dir_name)

    for pdf_file in os.listdir('.'):
        if os.path.isfile(pdf_file):
            print(f'rename --> {pdf_file}')
            os.rename(pdf_file, pdf_prefix + pdf_file)


        if os.path.isdir(pdf_file):
            os.chdir(pdf_file)
            for f in os.listdir('.'):
                print(f'{pdf_file} --> rename {f}')
                os.rename(f, pdf_prefix + f)

            os.chdir('../')

rename_pdf(const.PATH_TST,'whb_')


