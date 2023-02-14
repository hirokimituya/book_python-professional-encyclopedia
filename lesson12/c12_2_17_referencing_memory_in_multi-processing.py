import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(d, lock):
    with lock:
        i = d['x']
        time.sleep(2)
        d['x'] = i + 1
    logging.debug(d)


def worker2(d, lock):
    with lock:
        i = d['x']
        d['x'] = i + 1
    logging.debug(d)


if __name__ == '__main__':
    d = {'x': 0}
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=worker1, args=(d, lock))
    p2 = multiprocessing.Process(target=worker2, args=(d, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    logging.debug(d)
