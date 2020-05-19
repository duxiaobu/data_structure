# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        # 这里我们只知道待删除节点，我们就把待删除的下一个节点赋值到当前节点
        # 然后删除重复的第二个节点
        # 因为题目也说了至少两个节点，不是最后一个节点
        node.val = node.next.val
        node.next = node.next.next
