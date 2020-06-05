class MinStack:

    def __init__(self):
        """
        双栈，一个栈用来实现栈操作，一个栈用来记录最小值
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 如果最小栈没有值，或者入栈小于最小栈顶值，minStack也存值
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
            if x == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(obj.getMin())
    print(obj.top())
    print(obj.stack)
    print(obj.minStack)
    obj.pop()
    print()
    print(obj.getMin())
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
