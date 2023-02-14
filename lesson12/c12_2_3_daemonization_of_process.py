import logging
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    i = 10
    p1 = multiprocessing.Process(target=worker1, args=(i, ))
    p1.daemon = True
    p2 = multiprocessing.Process(name='renamed worker2', target=worker2, args=(i, ))
    p1.start()
    p2.start()
    p1.join()
