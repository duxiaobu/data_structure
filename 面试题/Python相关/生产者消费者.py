def costumer():
    print('2、开始消费')
    words = None
    while True:
        r = yield words
        if not r:
            return
        print('消费了{}'.format(r))
        words = 'ok'


def producer(c):
    print('1、开始生产')
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('生产了{}'.format(n))
        r = c.send(n)
        print('消费者返回{}'.format(r))
    c.close()


if __name__ == '__main__':
    c = costumer()
    producer(c)
