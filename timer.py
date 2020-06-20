from datetime import datetime
from time import sleep
def start():
    start_time = datetime.now()
    return start_time
# do your work here

def stop():
    end_time = datetime.now()
    return end_time

def total(start, stop):
    total_time = 'Duration: {}'.format(stop - start)
    return total_time



