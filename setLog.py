import logging
import time

log = logging.getLogger("my-logger")
logging.basicConfig(filename='logs/skip.log')
time = time.asctime()
log.info(time)