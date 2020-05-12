class MyOpen(object):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print('开始执行enter函数')
        self._handler = open(self.path, self.mode)
        return self._handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('开始执行exit函数')
        self._handler.close()
        return True


with MyOpen('./字典实现.py', 'r') as f:
    print('开始读取')
    data = f.read()
    print(data)
