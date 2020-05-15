# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        这里将链表中的值全部加到数组中，再利用快慢指针检测是否回文
        时间、空间复杂度都是O（n）
        '''
        if not head or head.next:
            return False
        res = []
        cur = head
        while cur:
            res.append(cur.val)
        slow = 0
        fast = len(res) - 1
        while slow < fast:
            if res[slow] != res[fast]:
                return False
            slow += 1
            fast -= 1
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        '''
        寻找链表后半段，反转后半段，再挨个比较是否相等
        时间复杂度O（n）
        空间复杂度O（1），挨个节点判断
        '''
        # 判断空节点
        if not head or not head.next:
            return True
        # 找到前半部分链表的尾节点。快慢指针，快指针一次走两步，慢指针一次走一步，当快指针到达末尾时，慢指针就在中心
        first_half_end = self.get_first_half_end(head)
        # 反转后半部分链表。
        back_half_start = self.reverse_link(first_half_end.next)
        # 判断是否为回文。
        front = head
        back = back_half_start
        result = True
        while result and back:
            if front.val != back.val:
                result = False
            front = front.next
            back = back.next
        # 恢复链表。
        first_half_end.next = self.reverse_link(back_half_start)
        # 返回结果。
        return result

    @staticmethod
    def get_first_half_end(head: ListNode):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse_link(head: ListNode):
        # 承接反转后的链表
        new_link = None
        cur = head
        while cur:
            # 记录下一个节点
            next_node = cur.next
            # 衔接之前反转的节点
            cur.next = new_link
            # 覆盖反转后的链表
            new_link = cur
            # 反转下一个节点
            cur = next_node
        return new_link


if __name__ == '__main__':
    pass
