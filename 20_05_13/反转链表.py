# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代的方法
        # 判断节点是否为空，或只有一个节点
        if head is None or head.next is None:
            return head
        new_link = None
        cur = head
        while cur:
            # 记录下一个节点
            next_node = cur.next
            # 当前节点拼接之前的节点
            cur.next = new_link
            # 重新赋值
            new_link = cur
            # 下一次循环
            cur = next_node
        return new_link

    def reverseList2(self, head: ListNode) -> ListNode:
        # 使用递归的方法
        if not head or not head.next:
            return head

        p = self.reverseList2(head.next)
        head.next.next = head  # 3->2      2->1
        head.next = None       # 2->None   1->None
        return p   # 3   3


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    s = Solution()
    x = s.reverseList2(node1)
    while x:
        print(x.val)
        x = x.next
