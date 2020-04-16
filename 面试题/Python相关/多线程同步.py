from threading import Thread, Lock, Condition
import time

num = 0
lock = Lock()
condition = Condition()


def add():
    global num
    global lock
    for i in range(100000):
        lock.acquire()
        num += 1
        lock.release()


def desc():
    global num
    global lock
    for i in range(100000):
        lock.acquire()
        num -= 1
        lock.release()


def pro():
    global num
    global condition
    condition.acquire()
    if num == 20:
        condition.wait()
    else:
        print('\nProducer: ', end=' ')
    for i in range(20):
        print(i, end=' ')
        num += 1
    print(num)
    condition.notify()
    condition.release()


def cus():
    global num
    global condition
    while num > 0:
        condition.acquire()
        if num <= 0:
            condition.notify()
            condition.wait()
        else:
            print('\nCustomer1: ', end=' ')
        for i in range(20):
            print(i, end=' ')
            num -= 1
        condition.release()
        time.sleep(1)


def cus2():
    global num
    global condition
    while num > 0:
        condition.acquire()
        if num <= 0:
            condition.notify()
            condition.wait()
        else:
            print('\nCustomer2: ', end=' ')
        for i in range(20):
            print(i, end=' ')
            num -= 1
        condition.release()
        time.sleep(1)


t1 = Thread(target=pro)
t2 = Thread(target=cus)
t3 = Thread(target=cus2)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(num)
