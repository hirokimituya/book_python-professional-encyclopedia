import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(d):
    logging.debug('start')
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    logging.debug('end')


def worker2(d):
    logging.debug('start')
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    t1 = threading.Thread(target=worker1, args=(d, ))
    t2 = threading.Thread(target=worker2, args=(d, ))
    t1.start()
    t2.start()
