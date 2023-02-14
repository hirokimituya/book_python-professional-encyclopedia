import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == '__main__':
    main()
