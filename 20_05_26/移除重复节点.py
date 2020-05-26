# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node_list = []
        cur = head
        new_cur = new_node_list = ListNode(None)
        while cur:
            if cur.val not in node_list:
                node_list.append(cur.val)
                new_cur.next = ListNode(cur.val)
                new_cur = new_cur.next
            cur = cur.next
        return new_node_list.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s = Solution()
    new_list_node = s.removeDuplicateNodes(node1)
    while new_list_node:
        print(new_list_node.val)
        new_list_node = new_list_node.next