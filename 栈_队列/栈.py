# 栈是后进先出数据结构，可以使用list或deque来模拟


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        # 入栈
        self.stack.append(item)

    def pop(self):
        # 弹出最后一个元素
        return self.stack.pop()

    def peek(self):
        # 返回最后一个元素
        return self.stack[-1]

    def size(self):
        # 栈大小
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


class Queue(object):
    # 两个栈实现一个队列
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, item):
        self.s1.push(item)

    def pop(self):
        if self.s2.size() == 0:
            if self.s1.size() == 0:
                return None
            else:
                while self.s1.size():
                    self.s2.push(self.s1.pop())
        return self.s2.pop()


if __name__ == '__main__':
    queue = Queue()
    for i in range(5):
        queue.push(i)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())