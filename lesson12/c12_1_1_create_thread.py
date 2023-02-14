import threading


def worker1():
    print(threading.current_thread().name, 'start')
    print(threading.current_thread().name, 'end')


def worker2():
    print(threading.current_thread().name, 'start')
    print(threading.current_thread().name, 'end')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
