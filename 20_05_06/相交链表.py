# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    1.暴力法，链表A中的每一个节点去遍历链表B
    2.字典发，链表A中的节点放入字典中，用链表B去匹配
    3.双指针法，
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针方法
        pointA, pointB = headA, headB
        while pointA != pointB:
            pointA = pointA.next if pointA else pointB
            pointB = pointB.next if pointB else pointA
        return pointA
