import logging
import time, const


def setLog(s):

    logging.basicConfig(level = logging.WARNING, filename=const.PATH_LOG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    currentTime = time
    logging.warning(s)

