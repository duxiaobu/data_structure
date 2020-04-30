# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycleDict(self, head: ListNode) -> bool:
        # 检测链表中是否有环，使用字典
        if head is None or head.next is None:
            return False
        node_dict = {}
        while head:
            if head not in node_dict:
                node_dict[head] = 1
                head = head.next
            else:
                return True
        return False

    def hasCycleQuick(self, head: ListNode) -> bool:
        # 使用双指针，一快一慢，快慢指针相遇就表示出现了环，如果快指针的next为None，表示这是一条单链表
        if head is None or head.next is None or head.next.next is None:
            return False
        quick_node = head.next.next
        while quick_node.next:
            if head == quick_node:
                return True
            head = head.next
            quick_node = quick_node.next.next
        return False
