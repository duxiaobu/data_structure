class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        if self._head is None:
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def items(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            yield cur.data
            cur = cur.next
        yield cur.data

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            cur = self._head
            # 找到最后一个节点
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        if index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def find(self, item):
        return item in self.items()

    def remove(self, item):
        if self.is_empty():
            return
        cur = self._head
        # 如果第一个节点就是待删除节点
        if cur.data == item:
            # 判断是否只有一个节点
            if cur.next == self._head:
                self._head = None
            else:
                # 不止一个节点,定位到最后一个节点
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
        else:
            pre = self._head
            while cur.next != self._head:
                if cur.data == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # 判断最后一个元素是否为待删除元素
            if cur.data == item:
                pre.next = cur.next


if __name__ == '__main__':
    link_list = SingleCycleLinkList()
    for i in range(5):
        link_list.append(i)

    link_list.insert(2, 8)
    link_list.remove(3)
    for j in link_list.items():
        print(j)
