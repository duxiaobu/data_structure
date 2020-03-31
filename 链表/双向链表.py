class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class TwoLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index):
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        # 空
        if self.is_empty():
            return
        # 头
        cur = self._head
        if cur.data == item:
            # 只有一个节点
            if cur.next is None:
                self._head = None
                return True
            else:
                self._head = cur.next
                # 下一个节点删除
                cur.next.prev = None
                return True
        # 中间
        while cur.next is not None:
            if cur.data == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next
        # 最后一个节点
        if cur.data == item:
            cur.prev.next = None
            return True

    def find(self, item):
        return item in self.items()


if __name__ == '__main__':
    two_link_list = TwoLinkList()
    # print(two_link_list.length())
    for i in range(5):
        two_link_list.append(i)

    two_link_list.add(7)
    two_link_list.insert(3, 9)
    two_link_list.remove(3)
    for j in two_link_list.items():
        print(j)
    print(two_link_list.is_empty())
    print(two_link_list.length())
