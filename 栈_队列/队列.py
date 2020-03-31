# 先进先出数据结构


class Queue(object):

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.queue.pop()

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


class Stack(object):
    # 两个队列实现一个栈
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.push(item)

    def pop(self):
        # 输入1 2 3 4
        # 输出4 3 2 1
        if self.q1.size() == 0:
            return None
        while self.q1.size() != 1:
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.pop()


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 5):
        stack.push(i)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
