# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 全部加入到数组中来判断,时间空间复杂度都是O(n)
        node_list = []
        cur = head
        while cur:
            node_list.append(cur.val)
            cur = cur.next
        return node_list == node_list[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        # 找到链表后半段,反转后半段,再依次比较
        if not head or not head.next:
            return True
        # 后半段链表起始节点
        back_half_node = self.getBackHalfNode(head)
        # 反转后半段链表
        back_half_list = self.getBackHalfList(back_half_node.next)
        # 依次比较
        back_cur = back_half_list
        cur = head
        is_pal = True
        while is_pal and back_cur:
            if cur.val != back_cur.val:
                is_pal = False
            cur = cur.next
            back_cur = back_cur.next
        return is_pal

    @staticmethod
    def getBackHalfNode(head: ListNode):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def getBackHalfList(head: ListNode):
        new_list = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = new_list
            new_list = cur
            cur = next_node
        return new_list


if __name__ == '__main__':
    a = [1, 2, 3]
    print(a[::-1])
