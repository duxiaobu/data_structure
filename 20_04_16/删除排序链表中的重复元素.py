# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        work_node = new_head = ListNode(head.val)
        while head.next:
            next_node = head.next
            if head.val != next_node.val:
                work_node.next = ListNode(next_node.val)
                work_node = work_node.next
            head = head.next
        return new_head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    pass
