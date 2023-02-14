import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
    return i


if __name__ == '__main__':
    with multiprocessing.Pool(3) as p:
        r = p.imap(worker1, [100, 200])
        logging.debug('executed')
        logging.debug([i for i in r])
