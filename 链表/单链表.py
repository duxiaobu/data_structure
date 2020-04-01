class Node(object):
    # 定义节点
    def __init__(self, value):
        self.data = value
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def add(self, value):
        # 头添加节点
        node = Node(value)
        node.next = self._head
        self._head = node

    def append(self, value):
        # 尾添加节点
        node = Node(value)
        # 判断是否为空链表
        if self.is_empty():
            self._head = node
        else:
            # 固定头节点，避免头节点被污染
            cur = self._head
            # 遍历找到最后一个节点，将最后个节点的next指向新节点
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def is_empty(self):
        # 链表是否为空
        return self._head is None

    def length(self):
        # 链表长度
        cur = self._head
        count = 0
        # 指针指向None，表示到达尾部
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        # 链表数据迭代器
        cur = self._head
        while cur is not None:
            # 返回迭代生成器
            yield cur.data
            cur = cur.next

    def insert(self, index, value):
        # 索引小于等于0,相当于在头插入
        if index <= 0:
            self.add(value)
        # 索引大于最大长度，相当于在尾插入
        if index > self.length() - 1:
            self.append(value)
        else:
            node = Node(value)
            cur = self._head
            # 找到被插入位置的前一个元素
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        # 删除节点，找到待删除节点和待删除节点的前一个节点，这样才能衔接
        cur = self._head
        pre = None
        while cur is not None:
            if cur.data == item:
                # 判断该节点是否是第一个节点
                if pre is None:
                    self._head = cur.next
                else:
                    # 将删除的下一个节点衔接到前一个节点
                    pre.next = cur.next
                return True
            else:
                # 如果当前节点的值不相等，则循环下一个值
                pre = cur
                cur = cur.next

    def find(self, item):
        # 查找节点是否存在
        return item in self.items()

    @staticmethod
    def reverse(head):
        # 1, 2, 3, 4
        # 判断是否是单节点、或只有一个节点
        if head is None or head.next is None:
            return head
        # 利用一个虚拟节点来承接倒序链表
        pre_link = None
        cur_node = head
        while cur_node.next is not None:
            # 记录下一个节点，因为cur_node后面会被覆盖
            next_node = cur_node.next
            # 倒序节点
            cur_node.next = pre_link
            # 记录倒序链表
            pre_link = cur_node
            cur_node = next_node


def merge_link_list(l1, l2):
    # 创建虚拟头节点，origin_node这个引用指向Node(-1)这个节点，用来保存头节点
    origin_node = Node(-1)
    # 创建工作节点，也指向Node(-1)这个节点，后续用来迭代连接链表
    work_node = origin_node
    # 遍历l1、l2，将小的值接在work_node后面
    while l1 and l2:
        if l1.data < l2.data:
            work_node.next, l1 = l1, l1.next
        else:
            work_node.next, l2 = l2, l2.next
        work_node = work_node.next
    work_node.next = l1 if l1 else l2
    # origin_node的头节点是虚拟节点，所以输出它的下一个节点
    return origin_node.next


if __name__ == '__main__':
    link_list1 = SingleLinkList()
    link_list2 = SingleLinkList()
    for i in [1, 2, 4]:
        link_list1.append(i)
    for i in [1, 3, 4]:
        link_list2.append(i)
    result = merge_link_list(link_list1._head, link_list2._head)
    while result:
        print(result.data)
        result = result.next