class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2.size() == 0:
            if self.stack1.size() == 0:
                return None
            else:
                while self.stack1.size():
                    self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2.size() == 0:
            if self.stack1.size() == 0:
                return None
            else:
                while self.stack1.size():
                    self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1.size() == 0 and self.stack2.size() == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    print(obj.peek())
    obj.pop()
    print(obj.peek())
    # print(obj.pop())
    # print(obj.empty())
    # obj.pop()
    # print(obj.stack1.size())
    # print(obj.stack2.size())
    # print(obj.empty())