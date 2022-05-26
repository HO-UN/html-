import time


def timestamp():
    return int(time.mktime(time.localtime(time.time())))