# 左右都能进出

class DoubleQueue(object):
    def __init__(self):
        self.items = []

    def left_push(self, item):
        self.items.insert(0, item)

    def right_push(self, item):
        self.items.append(item)

    def left_pop(self):
        return self.items.pop(0)

    def right_pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
