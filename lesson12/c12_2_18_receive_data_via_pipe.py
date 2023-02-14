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


def f(conn):
    conn.send(['test'])
    time.sleep(5)
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn,))
    p.start()
    logging.debug(child_conn.recv())
