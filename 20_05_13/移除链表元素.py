# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 普通删除节点，只需要记录前一个节点和当前节点即可
        # 当时如果待删除元素是头节点时，我们就要构造哨兵节点，使链表保存完整
        sentinel = ListNode(0)
        sentinel.next = head
        prev = sentinel
        cur = head
        while cur:
            # 如果相等，前一个节点指向下一个节点
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return sentinel.next


if __name__ == '__main__':
    pass
