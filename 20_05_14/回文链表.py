# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
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


if __name__ == '__main__':
    pass
