# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        # 将链表转换成数组,通过数组的索引来返回值
        data_queue = []
        cur = head
        while cur:
            data_queue.append(cur.val)
            cur = cur.next
        return data_queue.pop(-k)

    def kthToLast2(self, head: ListNode, k: int) -> int:
        # 双指针,快的指针先移动k步,后面快慢指针再同时移动,当快指针指向末尾时,慢指针指向k位值
        slow = fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    s = Solution()
    print(s.kthToLast2(node1, 2))
