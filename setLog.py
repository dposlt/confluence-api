import logging
import time


def setLog(s):
    logging.basicConfig(level = logging.WARNING, filename='logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    currentTime = time
    logging.warning(s)




